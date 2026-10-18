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
