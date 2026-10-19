#!/usr/bin/env python3
"""One shared maths-normalisation module for every generated page.

The full-textbook pages (build_site.py) and the practice pages
(build_practice.py) must get identical maths treatment, so every transform
lives here and nowhere else.

Usage as a library:
    import math_normalize as mn
    mn.normalise(text, "mathjax")     # text with maths fixes applied
    mn.normalise(text, "katex")       # same but align untouched, heading
                                     # maths kept (reported via check())
    mn.normalise(text, "nvim")        # identity (source form)
    mn.check(text)                    # list of problems, each a dict:
                                      #   {"line": N, "kind": str, "msg": str}

CLI:
    python math_normalize.py FILE [--target mathjax|katex|nvim] [--check] [--diff]

Guarantees:
  * line counts are never changed and blank lines stay blank (so the
    markdown-in-html structure of the practice pages is untouched);
  * normalising twice is the same as normalising once (idempotent);
  * code fences (``` ... ```) are never modified;
  * `\\$` escapes are respected (an escaped dollar is not a delimiter).
"""
import argparse
import difflib
import re
import sys
from pathlib import Path

# --- maths-to-plain-text for headings (sidebar/TOC cannot typeset) ----------
SYMBOLS = {"pm": "\u00b1", "cdot": "\u00b7", "cdots": "\u2026",
           "ldots": "\u2026", "to": "\u2192", "Rightarrow": "\u21d2",
           "Leftrightarrow": "\u21d4", "ne": "\u2260", "le": "\u2264",
           "ge": "\u2265", "leq": "\u2264", "geq": "\u2265",
           "infty": "\u221e", "times": "\u00d7", "div": "\u00f7",
           "circ": "\u00b0", "prime": "\u2032", "alpha": "\u03b1",
           "beta": "\u03b2", "theta": "\u03b8", "gamma": "\u03b3",
           "delta": "\u03b4", "pi": "\u03c0", "mu": "\u03bc",
           "lambda": "\u03bb", "phi": "\u03c6", "omega": "\u03c9"}

ALIGN_SUBS = [("\\begin{align*}", "\\begin{aligned*}"),
              ("\\end{align*}", "\\end{aligned*}"),
              ("\\begin{align}", "\\begin{aligned}"),
              ("\\end{align}", "\\end{aligned}")]

FENCE_RE = re.compile(r"^\s*`{3,}\s*$")
DOLLAR_OPEN_RE = re.compile(r"^\s*\$\$\s*$")
TABLE_ROW_RE = re.compile(r"^\s*\|")


def math_to_plain(s):
    """Crude LaTeX -> readable plain text for heading maths."""
    s = re.sub(r"\\(?:operatorname)\s*\{\s*([^{}]*?)\s*\}",
               lambda m: re.sub(r"\s+", "", m.group(1)), s)
    for cmd in ("boldsymbol", "mathbf", "mathbb", "mathrm", "text"):
        s = re.sub(r"\\" + cmd + r"\s*\{([^{}]*)\}", r"\1", s)
    brace = r"([^{}]*(?:\{[^{}]*\}[^{}]*)*)"
    s = re.sub(r"\\frac\s*\{" + brace + r"\}\s*\{" + brace + r"\}",
               lambda m: m.group(1) + "/" + m.group(2), s)
    s = re.sub(r"\\sqrt(?:\[[^\]]*\])?\s*\{([^{}]*(?:\{[^{}]*\}[^{}]*)*)\}",
               lambda m: "sqrt(" + m.group(1) + ")", s)
    for cmd, rep in SYMBOLS.items():
        s = s.replace("\\" + cmd, rep)
    s = re.sub(r"\\(?:left|right)\b", "", s)
    s = re.sub(r"\\[a-zA-Z@]+\b", "", s)
    return re.sub(r"\s+", " ", s.replace("\\", "").replace("{", "")
                  .replace("}", "").replace("~", "")).strip()


def _unescaped_dollars(line):
    """Positions of `$` characters not preceded by a backslash."""
    out, i = [], 0
    while i < len(line):
        if line[i] == "\\" and i + 1 < len(line):
            i += 2
            continue
        if line[i] == "$":
            out.append(i)
        i += 1
    return out


def _inline_spans(line):
    """[(start, end, inner)] for every inline $...$ span (respects \\$)."""
    spans = []
    dollars = _unescaped_dollars(line)
    i = 0
    while i < len(dollars):
        s = dollars[i]
        if s + 1 < len(line) and line[s + 1] == "$":  # part of a $$ pair
            i += 1
            continue
        closer = None
        for e in dollars[i + 1:]:
            if e + 1 < len(line) and line[e + 1] == "$":
                continue          # first $ of a "$$" is not a closer
            closer = e
            break
        if closer is None:
            break                 # unmatched opener; leave the rest alone
        spans.append((s, closer + 1, line[s + 1:closer]))
        i = dollars.index(closer) + 1
    return spans


def _apply_span(inner, table_row, do_align):
    inner = inner.strip()
    inner = inner.replace("<", r"\lt ").replace(">", r"\gt ")
    if table_row:
        inner = inner.replace("|", r"\vert ")
    if do_align:
        for a, b in ALIGN_SUBS:
            inner = inner.replace(a, b)
    return inner


def _fix_line_maths(line, table_row, do_align):
    spans = _inline_spans(line)
    if not spans:
        return line
    out = list(line)
    for s, e, inner in reversed(spans):
        new = _apply_span(inner, table_row, do_align)
        out[s:e] = list("$" + new + "$")
    return "".join(out)


def _strip_heading_maths(line):
    spans = _inline_spans(line)
    if not spans:
        return line
    out = list(line)
    for s, e, inner in reversed(spans):
        plain = math_to_plain(inner)
        out[s:e] = list(plain)
    return "".join(out)


def normalise(text, target="nvim"):
    """Apply the target's maths normalisations to `text`.

    target:
      "nvim"    returns text unchanged (source form)
      "mathjax" align->aligned, `$ x $` trims, `<`/`>`->\\lt/\\gt,
                `|`->\\vert in table-row maths, stray `$` rebalancing,
                heading maths stripped to plain text, \\boldsymbol kept
      "katex"   same as mathjax EXCEPT align is left alone and heading
                maths is kept (report it via check() instead)
    Never changes line counts or blank-line positions; never touches code
    fences.
    """
    if target == "nvim":
        return text
    do_align = (target == "mathjax")
    strip_headings = (target == "mathjax")
    in_fence = in_block = False
    out = []
    for line in text.split("\n"):
        stripped = line.strip()
        if FENCE_RE.match(line):
            in_fence = not in_fence
            out.append(line)
            continue
        if in_fence:
            out.append(line)
            continue
        if DOLLAR_OPEN_RE.match(stripped):
            in_block = not in_block
            out.append(line)
            continue
        if in_block:
            fixed = line
            if do_align:
                for a, b in ALIGN_SUBS:
                    fixed = fixed.replace(a, b)
            fixed = fixed.replace("<", r"\lt ").replace(">", r"\gt ")
            out.append(fixed)
            continue
        # normal line (outside code/$$)
        table_row = bool(TABLE_ROW_RE.match(line))
        fixed = _fix_line_maths(line, table_row, do_align)
        if stripped.startswith("#"):
            if "$" in fixed:
                if strip_headings:
                    fixed = _strip_heading_maths(fixed)
        else:
            # rebalance a stray trailing $ on lines with an odd dollar count
            if not table_row and len(_unescaped_dollars(fixed)) % 2 == 1:
                dollars = _unescaped_dollars(fixed)
                if dollars:
                    k = dollars[-1]
                    fixed = fixed[:k] + fixed[k + 1:]
        out.append(fixed)

    result = "\n".join(out)
    if len(result.split("\n")) != len(text.split("\n")):
        raise AssertionError("normalise changed the line count")
    return result


def find_math_headings(text):
    """[(line_no, heading_text)] for heading lines containing maths."""
    found, in_fence = [], False
    for n, line in enumerate(text.split("\n"), 1):
        if FENCE_RE.match(line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        if line.lstrip().startswith("#") and "$" in line:
            found.append((n, line.strip()))
    return found


ENV_TOKEN = re.compile(r"\\(begin|end)\{([^}]+)\}")


def _envs_in_order(line):
    for m in ENV_TOKEN.finditer(line):
        yield m.start(), m.group(1), m.group(2)


def check(text):
    """Return a list of problems: unbalanced $, unclosed $$,
    \\begin without \\end, unknown environments, and headings with maths."""
    problems = []
    in_fence = in_block = False
    begin_stack = []          # (line, env)
    env_names = set()
    for n, line in enumerate(text.split("\n"), 1):
        stripped = line.strip()
        if FENCE_RE.match(line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        if DOLLAR_OPEN_RE.match(stripped):
            in_block = not in_block
            continue
        for _, kind, env in _envs_in_order(line):
            env_names.add(env)
            if kind == "begin":
                begin_stack.append((n, env))
            elif begin_stack:
                top_line, top_env = begin_stack.pop()
                if top_env != env:
                    problems.append(
                        {"line": n, "kind": "begin-end-mismatch",
                         "msg": f"\\begin{{{top_env}}} (line {top_line}) "
                                f"closed by \\end{{{env}}}"})
            else:
                problems.append({"line": n, "kind": "end-without-begin",
                                 "msg": line.strip()[:60]})
        if in_block:
            continue
        if "$" in line:
            if len(_unescaped_dollars(line)) % 2 == 1:
                problems.append({"line": n, "kind": "unbalanced-dollar",
                                 "msg": line.strip()[:60]})
    if in_block:
        problems.append({"line": None, "kind": "unclosed-dollar-block",
                         "msg": "$$ block opened but never closed"})
    for n, env in begin_stack:
        problems.append({"line": n, "kind": "begin-without-end",
                         "msg": f"\\begin{{{env}}} without \\end"})
    for n, heading in find_math_headings(text):
        problems.append({"line": n, "kind": "heading-math",
                         "msg": heading[:60]})
    if env_names:
        problems.append({"line": None, "kind": "environments",
                         "msg": " ".join(sorted(env_names))})
    return problems


KNOWN_ENVS = {
    "align", "align*", "aligned", "aligned*", "alignedat", "gathered",
    "split", "array", "cases", "matrix", "pmatrix", "bmatrix", "vmatrix",
    "Vmatrix", "smallmatrix", "equation", "equation*", "substack", "rcases",
    "dcases", "CD", "subarray", "matrix*", "pmatrix*", "bmatrix*",
    "vmatrix*", "Vmatrix*",
}


def unknown_environments(text):
    """Env names used in `text` that are not in KNOWN_ENVS (uncertain)."""
    found = set(re.findall(r"\\begin\{([^}]+)\}", text))
    return sorted(found - KNOWN_ENVS)


def main(argv=None):
    ap = argparse.ArgumentParser(description="Maths normalisation for the "
                                             "MkDocs build")
    ap.add_argument("file", type=Path)
    ap.add_argument("--target", choices=("nvim", "mathjax", "katex"),
                    default="nvim")
    ap.add_argument("--check", action="store_true",
                    help="print problems instead of normalised text")
    ap.add_argument("--diff", action="store_true",
                    help="print a unified diff of what the target would change")
    args = ap.parse_args(argv)

    text = args.file.read_text(encoding="utf-8")

    if args.check:
        for p in check(text):
            loc = f"line {p['line']}" if p["line"] else "file"
            print(f"{loc}  [{p['kind']}] {p['msg']}")
        uk = unknown_environments(text)
        if uk:
            print(f"file  [unknown-environment] {', '.join(uk)}")
        return

    if args.target == "nvim":
        print("(nvim: identity — no output)")
        return

    out = normalise(text, args.target)
    if args.diff:
        before = text.splitlines()
        after = out.splitlines()
        diff = difflib.unified_diff(before, after, "source", "normalised",
                                    lineterm="")
        for line in diff:
            print(line)
    else:
        print(out, end="" if text.endswith("\n") else "")


if __name__ == "__main__":
    main()