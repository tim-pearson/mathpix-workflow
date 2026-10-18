#!/usr/bin/env python3
"""Clean up Mathpix Markdown (normal export) for rendering and querying.

Usage: python fix_md.py input.md [output.md]
       (no output given -> writes <input>-fixed.md)

Fixes:
  - $$ blocks: delimiters on their own lines, one `\\` row per line,
    hard-wrapped lines inside a block re-joined, aligned -> align
  - inline $...$ maths never spans more than one line
  - dotted leaders (\\cdots / \\ldots chains) removed
  - hard-wrapped prose lines re-joined
  - parts split onto separate lines and bolded: letters (**a**) AND
    roman numerals (**i**, **ii**, **iii** ...), including nested a/b under ii
  - question numbers bolded (**1** ...), PS / P markers tidied
  - "Cambridge International ..." source lines put on their own line
  - headings normalised (### EXERCISE 2E, #### WORKED EXAMPLE 2.11)
  - OCR artefacts: `$\\quad`, `4{ }^{100}`, `3significant`, stray final $$
  - indentation stripped (4 spaces would render as a code block)
  - final sanity check warns about any line with an unbalanced inline $
Idempotent: running it on its own output changes nothing.
"""
import re
import sys
from pathlib import Path

src = Path(sys.argv[1])
dst = Path(sys.argv[2]) if len(sys.argv) > 2 else src.with_name(src.stem + "-fixed.md")
text = src.read_text(encoding="utf-8")

# ---------- generic cleanups (apply to maths and prose) ----------
LEADER = re.compile(
    r"(?:\\quad\s*)?(?:\\cdots|\\ldots)(?:[\s.]*(?:\\cdots|\\ldots|\\cdot\b))*[\s.]*"
)

def drop_leaders(s: str) -> str:
    def rep(m):
        rest = s[m.end():m.end() + 1]
        return r"\qquad " if rest and rest not in "$}\n" else ""
    return LEADER.sub(rep, s)

def clean(s: str) -> str:
    s = drop_leaders(s)
    s = re.sub(r"\$\\quad\s*", "$", s)
    s = re.sub(r"\{\s*\}\^", "^", s)
    s = re.sub(r"(\d)(significant)", r"\1 \2", s)
    return s

if text.count("$$") % 2:
    i = text.rfind("$$")
    text = text[:i] + text[i + 2:]

# ---------- 1. maths blocks ----------
stash = []

def block(m):
    inner = clean(" ".join(m.group(1).split()))
    inner = inner.replace(r"\begin{aligned}", r"\begin{align}")
    inner = inner.replace(r"\end{aligned}", r"\end{align}")
    inner = re.sub(r"\s*\\begin\{align\}\s*", lambda _: "\\begin{align}\n", inner)
    inner = re.sub(r"\s*\\end\{align\}\s*", lambda _: "\n\\end{align}", inner)
    inner = re.sub(r"\s*\\\\\s*(?!\\end\{align\})", lambda _: " \\\\\n", inner)
    stash.append("$$\n" + inner.strip() + "\n$$")
    return f"\n@@MATH{len(stash) - 1}@@\n"

text = re.sub(r"\$\$(.*?)\$\$", block, text, flags=re.S)
text = clean(text)

# ---------- 1b. inline maths must live on ONE line ----------
def join_inline_math(s: str) -> str:
    """Pair up single $ ... $ and collapse any newlines inside the pair.
    $$ blocks are already stashed as @@MATH..@@, so every $ here is inline.
    A $ with no partner (or whose 'partner' is across a blank line or
    more than 400 chars away) is treated as stray and left alone."""
    out, i, n = [], 0, len(s)
    while i < n:
        if s[i] == "$" and (i == 0 or s[i - 1] != "\\"):
            j = i + 1
            while j < n and not (s[j] == "$" and s[j - 1] != "\\"):
                j += 1
            inner = s[i + 1:j] if j < n else None
            if (inner is not None and not re.search(r"\n\s*\n", inner)
                    and len(inner) <= 400):
                out.append("$" + " ".join(inner.split()) + "$")
                i = j + 1
                continue
            out.append("$")          # stray $
            i += 1
            continue
        out.append(s[i])
        i += 1
    return "".join(out)

text = join_inline_math(text)

# ---------- 2. unwrap hard-wrapped prose ----------
ROMAN = ["i", "ii", "iii", "iv", "v", "vi", "vii", "viii"]
ROMAN_RE = r"(?:iv|vi{0,3}|i{1,3})"

START = re.compile(
    r"^(\d+\s|PS\s|\(?P\s|\d\)\s|[a-z]\)?\s+(\$|@@|[A-Z])|[a-z]\)?$|#|[-*]\s|\*\*|@@|!\[|"
    + ROMAN_RE + r"\s+[A-Z$]|Cambridge International|"
    r"WORKED EXAMPLE|EXERCISE|Answer|KEY POINT|DID YOU KNOW|When |Hence|Solve|Prove|Find|Show|Use|Given)"
)
raw = []
for l in text.split("\n"):
    l = l.strip()
    # put the exam-source citation on its own line
    m = re.search(r"\s+(Cambridge International .*)$", l)
    if m and not l.startswith("Cambridge International"):
        raw.append(l[:m.start()].strip())
        raw.append(m.group(1).strip())
    else:
        raw.append(l)

lines = []
for l in raw:
    if not l:
        lines.append("")
        continue
    prev = lines[-1] if lines else ""
    if (prev and len(prev) >= 70 and not re.search(r"[.:?!\]]$|@@$", prev)
            and not prev.startswith(("#", "@@", "![", "Cambridge International"))
            and not START.match(l)):
        lines[-1] = prev + " " + l
    else:
        lines.append(l)

# ---------- 3. structure: headings, numbers, part labels ----------
out = []
prev_label = None   # last letter label (a, b, ...)
prev_roman = None   # last roman label (i, ii, ...)

def reset():
    global prev_label, prev_roman
    prev_label = prev_roman = None

def label_ok(letter):
    if prev_label is None:
        return letter == "a"
    return ord(letter) == ord(prev_label) + 1

def next_roman():
    if prev_roman is None:
        return ROMAN[0]
    k = ROMAN.index(prev_roman)
    return ROMAN[k + 1] if k + 1 < len(ROMAN) else None

def note_existing(tok):
    """Update state for an already-bolded label like **ii** or **b**."""
    global prev_label, prev_roman
    if tok in ROMAN and tok == next_roman() and not (tok == "i" and prev_label == "h"):
        prev_roman = tok
    elif len(tok) == 1:
        prev_label, prev_roman = tok, None

TOKEN = re.compile(
    r"(?:^|(?<=\s))(iv|vi{0,3}|i{1,3}|[a-z])\)?\s+(?=([$!@A-Za-z]))"
)

def split_labels(line):
    """Split 'x [3] ii Hence a solve ... b find ...' into labelled lines."""
    global prev_label, prev_roman
    cuts = []  # (start, end, label)
    # inline maths spans: never look for labels inside these
    spans = [(m.start(), m.end())
             for m in re.finditer(r"(?<!\\)\$[^$]*\$", line)]
    for m in TOKEN.finditer(line):
        if any(s <= m.start() < e for s, e in spans):
            continue
        tok, follow = m.group(1), m.group(2)
        lower = follow.islower()
        before = line[:m.start()]
        if (tok in ROMAN and tok == next_roman() and not lower
                and not (tok == "i" and prev_label == "h")):
            prev_roman = tok
            cuts.append((m.start(), m.end(), tok))
            continue
        if len(tok) == 1 and label_ok(tok):
            if lower and not (prev_label is not None
                              or before.rstrip().lower().endswith("hence")):
                continue
            prev_label, prev_roman = tok, None
            cuts.append((m.start(), m.end(), tok))
    if not cuts:
        return [line.strip()] if line.strip() else []
    res = []
    if line[:cuts[0][0]].strip():
        res.append(line[:cuts[0][0]].strip())
    for k, (s, e, lab) in enumerate(cuts):
        end = cuts[k + 1][0] if k + 1 < len(cuts) else len(line)
        res.append(f"**{lab}** {line[e:end].strip()}".rstrip())
    return res
for l in lines:
    if not l:
        continue
    m = re.match(r"^#*\s*(EXERCISE \d+[A-Z])\s*$", l)
    if m:
        out.append(f"### {m.group(1)}"); reset(); continue
    m = re.match(r"^#*\s*(WORKED EXAMPLE [\d.]+)\s*$", l)
    if m:
        out.append(f"#### {m.group(1)}"); reset(); continue
    if l.startswith("#"):
        out.append(l); reset(); continue

    # OCR'd margin markers: "(P 4 Prove" / "7) PS 5 In"
    l = re.sub(r"^\(P\s+(\d+)", r"P \1", l)
    l = re.sub(r"^\d\)\s+(PS\s+\d+)", r"\1", l)

    # question number (plain or already bolded)
    m = re.match(r"^(?:\*\*)?(?:(PS|P)\s+)?(\d+)(?:\*\*)?\s+(.*)$", l)
    if m and not l.startswith("@@"):
        tag = f"{m.group(1)} " if m.group(1) else ""
        reset()
        head = f"**{tag}{m.group(2)}**"
        rest = m.group(3)
        lead = re.match(r"^\*\*([a-z]+)\*\*\s", rest)
        if lead:
            note_existing(lead.group(1))
            out.append(head + " " + rest)
            continue
        parts = split_labels(rest)
        if parts and re.match(r"\*\*[a-z]+\*\* ", parts[0]):
            parts[0] = head + " " + parts[0]
            out.extend(parts)
        else:
            out.append(head + (" " + parts[0] if parts else ""))
            out.extend(parts[1:])
        continue

    # already-bolded label at line start: keep it, but track state
    m = re.match(r"^\*\*([a-z]+)\*\*(\s|$)", l)
    if m:
        note_existing(m.group(1))
        out.append(l); continue

    # lone label line ("a", "b)", "ii")
    m = re.match(r"^([a-z]+)\)?$", l)
    if m:
        tok = m.group(1)
        if tok in ROMAN and tok == next_roman() and not (tok == "i" and prev_label == "h"):
            prev_roman = tok; out.append(f"**{tok}**"); continue
        if len(tok) == 1 and label_ok(tok):
            prev_label, prev_roman = tok, None
            out.append(f"**{tok}**"); continue

    out.extend(split_labels(l))

# ---------- 4. restore blocks, one blank line between everything ----------
result = "\n\n".join(out)
result = re.sub(r"@@MATH(\d+)@@", lambda m: stash[int(m.group(1))], result)
result = re.sub(r"\n{3,}", "\n\n", result).strip() + "\n"

# ---------- 5. sanity check: report any line with an unbalanced inline $ ----------
in_block, bad = False, 0
for no, ln in enumerate(result.split("\n"), 1):
    if ln.strip() == "$$":
        in_block = not in_block
        continue
    if in_block:
        continue
    if len(re.findall(r"(?<!\\)\$", ln)) % 2:
        bad += 1
        print(f"WARNING line {no}: unbalanced inline $: {ln[:80]}")
if bad:
    print(f"{bad} line(s) need a manual look")

dst.write_text(result, encoding="utf-8")
print(f"wrote {dst}  ({len(stash)} maths blocks)")
