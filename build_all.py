#!/usr/bin/env python3
"""Run the whole book -> site pipeline in one command.

    python build_all.py [book_dir] [--local-mathjax] [--full-keypoints]

Steps (in order) — the pipeline scripts live in ./scripts:
  1. scripts/fix-mathpix.py     raw Mathpix export  -> <book>/<raw>-fixed.md
  2. scripts/split_chapter.py   fixed markdown      -> <book>/split/*.md
  3. scripts/fix_sections.py    split/*.md          -> headings/anchors + index.json
  4. scripts/build_site.py      book dir            -> ./site/ (incl. practice pages)

Only the stdlib is needed to run this; `mkdocs-material` (requirements.txt)
is required for `mkdocs build` / `mkdocs serve`, which build_site.py does not
call itself.
"""
import argparse
import subprocess
import sys
from pathlib import Path

BOOK_DEFAULT = Path("Maths Pure 2 & 3-clean_MD")
SCRIPTS = Path(__file__).resolve().parent / "scripts"


def run(step, *args):
    cmd = [sys.executable, str(SCRIPTS / step), *[str(a) for a in args]]
    print(f"\n$ {' '.join(cmd)}")
    r = subprocess.run(cmd)
    if r.returncode:
        sys.exit(f"{step} failed with exit code {r.returncode}")


def main():
    ap = argparse.ArgumentParser(description="Full book -> site pipeline")
    ap.add_argument("book", nargs="?", default=str(BOOK_DEFAULT))
    ap.add_argument("--local-mathjax", action="store_true",
                    help="bundle MathJax into site/docs/javascripts/ "
                         "instead of using the CDN")
    ap.add_argument("--full-keypoints", action="store_true",
                    help="key point bodies use the whole next-anchor slice")
    args = ap.parse_args()

    book = Path(args.book)
    if not book.is_dir():
        sys.exit(f"not a directory: {book}")

    raws = sorted(p for p in book.glob("*.md") if not p.name.endswith("-fixed.md"))
    if not raws:
        sys.exit(f"no raw Mathpix markdown found in {book}")
    raw = raws[0]
    fixed = book / (raw.stem + "-fixed.md")

    run("fix-mathpix.py", raw)
    run("split_chapter.py", fixed, "-o", book / "split")
    run("fix_sections.py", book / "split")

    extra = []
    if args.local_mathjax:
        extra.append("--local-mathjax")
    if args.full_keypoints:
        extra.append("--full-keypoints")
    run("build_site.py", book, *extra)

    print("\nPipeline complete. Serve locally with:")
    print("  pip install -r requirements.txt")
    print("  cd site && mkdocs serve")
    print("Stats / structure for planning:  python scripts/make_stats.py")


if __name__ == "__main__":
    main()
