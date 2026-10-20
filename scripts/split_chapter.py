#!/usr/bin/env python3
"""Split a fixed Mathpix book .md into one file per chapter / answers section.

Usage: python split_chapters.py book-fixed.md [-o outdir]
       (default outdir: <input folder>/split)

Output files:
  00-front-matter.md
  ch01-algebra.md ... ch11-complex-numbers.md
  paper-pm2.md, paper-pm3.md              (practice papers, question side)
  ans01-algebra.md ... ans11-...md        (worked answers per chapter)
  anspaper-pm2.md, anspaper-pm3.md        (practice papers, answer side)
  zz-glossary.md, zz-index.md

Image links are rewritten ./images/ -> ../images/ because the files live
one folder below the images folder.

Normalisations applied to the raw Mathpix output before splitting:
  * `## Chapter N` with its title on the following line is joined into
    `## Chapter N <br> Title` (Mathpix sometimes drops the `<br>`).
  * a bare `PREREQUISITE KNOWLEDGE` line (no `#`) gets a `##` prefix so the
    structural pass recognises it.
  * a chapter whose `## Chapter N` heading is missing entirely (OCR drop) is
    detected from a PREREQUISITE KNOWLEDGE block that sits far from the
    previous chapter heading; its title is taken from the matching answer
    section (`## N Title`), so split_chapter.py still produces every chapter
    and answers file.
"""
import argparse
import re
from pathlib import Path

ap = argparse.ArgumentParser()
ap.add_argument("src")
ap.add_argument("-o", "--out", default=None)
args = ap.parse_args()

src = Path(args.src)
out = Path(args.out) if args.out else src.parent / "split"
out.mkdir(parents=True, exist_ok=True)
lines = src.read_text(encoding="utf-8").split("\n")

CHAPTER = re.compile(r"^##\s+Chapter\s+(\d+)\s*(?:<br\s*/?>)?\s*(.*?)\s*$", re.I)
ANSWER = re.compile(r"^##\s+(\d+)\s+(.+?)\s*$")
PAPER = re.compile(r"^##\s+PURE MATHEMATICS\s+(\d)\s+PRACTICE EXAM-STYLE PAPER\s*$", re.I)
GLOSSARY = re.compile(r"^##\s+Glossary\s*$", re.I)
INDEX = re.compile(r"^##\s+Index\s*$", re.I)
PREREQ = re.compile(r"^#{0,2}\s*PREREQUISITE KNOWLEDGE\s*$", re.I)
CHECKLIST = re.compile(r"^#{1,2}\s*Checklist of learning and understanding\s*$", re.I)
REVIEW = re.compile(r"^#{0,2}\s*END-OF-CHAPTER REVIEW EXERCISE\s+(\d+)\s*$", re.I)

# --------------------------------------------------------------------------
# normalise the raw output before structural splitting
# --------------------------------------------------------------------------

# 1. chapter titles: titles for every chapter, falling back to the answer
#    section heading (`## N Title`). `chapter_headings` records which chapters
#    actually have a `## Chapter N` heading in the body.
titles = {}
chapter_headings = set()
for ln in lines:
    m = ANSWER.match(ln)
    if m and int(m.group(1)) not in titles:
        titles[int(m.group(1))] = m.group(2).strip()
for i, ln in enumerate(lines):
    m = CHAPTER.match(ln)
    if not m:
        continue
    n = int(m.group(1))
    chapter_headings.add(n)
    t = m.group(2).strip()
    if not t:
        # title on the following line, e.g. "## Chapter 3\n## Trigonometry"
        for j in range(i + 1, min(i + 4, len(lines))):
            tm = re.match(r"^#{1,2}\s+(.+?)\s*$", lines[j].strip())
            if tm:
                t = tm.group(1).strip()
                break
    titles[n] = t

missing = sorted(n for n in range(1, max(titles) + 1)
                 if n not in chapter_headings)

# 2. normalise lines: join split chapter titles, prefix bare prerequisites,
#    inject headings for chapters the OCR dropped entirely, and restore a
#    missing END-OF-CHAPTER REVIEW EXERCISE N heading (the review questions
#    are present but their heading was dropped: they directly follow the
#    chapter's "Checklist of learning and understanding").
norm = []
last_ch = None          # (chapter number, line index) of the last ## Chapter N
skip_until = -1
reviewed = set()        # chapters whose END-OF-CHAPTER REVIEW heading was seen
after_checklist = None  # chapter number whose checklist was just seen
for i, ln in enumerate(lines):
    if i == skip_until:
        continue
    m = CHAPTER.match(ln)
    if m:
        n = int(m.group(1))
        last_ch = (n, i)
        reviewed.discard(n)
        after_checklist = None
        if not m.group(2).strip():
            for j in range(i + 1, min(i + 4, len(lines))):
                tm = re.match(r"^#{1,2}\s+(.+?)\s*$", lines[j].strip())
                if tm:
                    norm.append(f"## Chapter {n} <br> {tm.group(1).strip()}")
                    skip_until = j      # title line consumed into the heading
                    break
            else:
                norm.append(ln)
            continue
        norm.append(ln)
        continue
    r = REVIEW.match(ln)
    if r:
        reviewed.add(int(r.group(1)))
        after_checklist = None
        norm.append("## " + ln.lstrip("#").strip()
                    if not ln.strip().startswith("#") else ln)
        continue
    c = CHECKLIST.match(ln)
    if c:
        after_checklist = last_ch[0] if last_ch else None
        norm.append(ln)
        continue
    if after_checklist is not None \
            and after_checklist not in reviewed \
            and re.match(r"^(?:\*\*)?[0-9]{1,2}(?:\*\*)?\s+[A-Z($]", ln):
        norm.append(f"## END-OF-CHAPTER REVIEW EXERCISE {after_checklist}")
        reviewed.add(after_checklist)
        after_checklist = None
    if PREREQ.match(ln):
        # a prerequisite sitting far from the previous chapter heading means
        # the chapter-title heading was dropped by the OCR: re-inject it
        if missing and last_ch is not None \
                and i - last_ch[1] > 50 and last_ch[0] + 1 in missing:
            n = last_ch[0] + 1
            norm.append(f"## Chapter {n} <br> {titles.get(n, '')}")
            missing.remove(n)
            last_ch = (n, i)
        norm.append("## " + ln.strip() if not ln.strip().startswith("#") else ln)
        continue
    norm.append(ln)

lines = norm


def norm(s):
    return re.sub(r"[^a-z0-9]", "", s.lower())


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


# pass 1: chapter titles from the body
titles = {}
for ln in lines:
    m = CHAPTER.match(ln)
    if m and int(m.group(1)) not in titles:
        titles[int(m.group(1))] = m.group(2).strip()

# pass 2: boundaries (line index, filename stem, replacement heading)
bounds = []
in_answers = False
for i, ln in enumerate(lines):
    m = CHAPTER.match(ln)
    if m and not in_answers:
        n, t = int(m.group(1)), m.group(2).strip()
        bounds.append((i, f"ch{n:02d}-{slug(t)}", f"# Chapter {n}: {t}"))
        continue
    m = PAPER.match(ln)
    if m:
        d = m.group(1)
        key = "anspaper" if in_answers else "paper"
        bounds.append((i, f"{key}-pm{d}", ln.replace("## ", "# ", 1)))
        continue
    m = ANSWER.match(ln)
    if m:
        n, t = int(m.group(1)), m.group(2)
        ref = titles.get(n)
        if ref and (norm(t) == norm(ref) or norm(t).startswith(norm(ref))
                    or norm(ref).startswith(norm(t))):
            in_answers = True
            bounds.append((i, f"ans{n:02d}-{slug(ref)}", f"# Answers: {n} {ref}"))
        continue
    if in_answers and GLOSSARY.match(ln):
        bounds.append((i, "zz-glossary", "# Glossary"))
    elif in_answers and INDEX.match(ln):
        bounds.append((i, "zz-index", "# Index"))

if not bounds:
    raise SystemExit("no chapter headings found - is this the right file?")

# pass 3: write files
used, report = set(), []


def write(stem, body_lines):
    name, k = stem, 2
    while name in used:
        name, k = f"{stem}-{k}", k + 1
    used.add(name)
    text = "\n".join(body_lines).strip() + "\n"
    text = text.replace("](./images/", "](../images/")
    (out / f"{name}.md").write_text(text, encoding="utf-8")
    report.append((name, len(body_lines)))


if bounds[0][0] > 0:
    write("00-front-matter", lines[:bounds[0][0]])

for k, (start, stem, heading) in enumerate(bounds):
    end = bounds[k + 1][0] if k + 1 < len(bounds) else len(lines)
    write(stem, [heading] + lines[start + 1:end])

# report
print(f"wrote {len(report)} files to {out}\n")
for name, n in report:
    print(f"  {name + '.md':<55} {n:>6} lines")

missing = [n for n in sorted(titles)
           if not any(r[0].startswith(f"ans{n:02d}-") for r in report)]
if missing:
    print(f"\nWARNING: no answers section found for chapter(s): {missing}")
expected = max(titles) if titles else 0
gaps = [n for n in range(1, expected + 1) if n not in titles]
if gaps:
    print(f"WARNING: chapter heading(s) not found for: {gaps}")
