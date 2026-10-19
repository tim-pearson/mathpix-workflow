#!/usr/bin/env python3
"""Run the whole book -> React frontend pipeline in one command, from the raw
Mathpix Markdown export all the way to a running Docker container.

    python build_frontend.py [book_dir] [--skip-docker] [--corrections PATH]

Steps (in order) — the pipeline scripts live in ./scripts:
  1. scripts/fix-mathpix.py    raw Mathpix export  -> <book>/<raw>-fixed.md
  2. scripts/split_chapter.py   fixed markdown      -> <book>/split/*.md
  3. scripts/fix_sections.py    split/*.md          -> headings/anchors +
                                                      index.json (applies
                                                      scripts/corrections.json)
  4. scripts/export_data.py     split/ + images/    -> frontend-data/ (the
                                                      React app's data bundle)
  5. docker compose up --build -d   frontend/       -> build + start the app
                                                      (served on
                                                      http://127.0.0.1:5173)

Only the stdlib is needed; `docker` (with compose) is required for step 5.
Use --skip-docker to stop after the data bundle has been regenerated.
"""
import argparse
import shutil
import subprocess
import sys
from pathlib import Path

BOOK_DEFAULT = Path("Maths Pure 2 & 3-clean_MD")
SCRIPTS = Path(__file__).resolve().parent / "scripts"
FRONTEND = Path(__file__).resolve().parent / "frontend"


def run(step, *args):
    cmd = [sys.executable, str(SCRIPTS / step), *[str(a) for a in args]]
    print(f"\n$ {' '.join(cmd)}")
    r = subprocess.run(cmd)
    if r.returncode:
        sys.exit(f"{step} failed with exit code {r.returncode}")


def main():
    ap = argparse.ArgumentParser(description="Full book -> React frontend pipeline")
    ap.add_argument("book", nargs="?", default=str(BOOK_DEFAULT))
    ap.add_argument("--skip-docker", action="store_true",
                    help="stop after frontend-data is regenerated "
                         "(don't build/start the Docker container)")
    ap.add_argument("--corrections", default=None,
                    help="corrections JSON to pass to fix_sections "
                         "(default: scripts/corrections.json)")
    args = ap.parse_args()

    book = Path(args.book)
    if not book.is_dir():
        sys.exit(f"not a directory: {book}")

    raws = sorted(p for p in book.glob("*.md")
                  if not p.name.endswith("-fixed.md"))
    if not raws:
        sys.exit(f"no raw Mathpix markdown found in {book}")
    raw = raws[0]
    fixed = book / (raw.stem + "-fixed.md")

    run("fix-mathpix.py", raw)
    run("split_chapter.py", fixed, "-o", book / "split")

    fix_sections_args = [book / "split"]
    if args.corrections:
        fix_sections_args += ["--corrections", args.corrections]
    run("fix_sections.py", *fix_sections_args)

    run("export_data.py", book)

    if args.skip_docker:
        print("\nData bundle ready (Docker skipped). Start the app with:")
        print("  cd frontend && docker compose up --build -d")
        return

    if not shutil.which("docker"):
        sys.exit(
            "docker is not installed; install Docker + Compose, then run:"
            "\n  cd frontend && docker compose up --build -d"
            "\n(or re-run this script with --skip-docker and serve "
            "frontend-data via `npm run dev` in frontend/).")

    print("\n$ docker compose up --build -d")
    r = subprocess.run(["docker", "compose", "up", "--build", "-d"],
                       cwd=FRONTEND)
    if r.returncode:
        sys.exit(f"docker compose up failed with exit code {r.returncode}")

    print("\nPipeline complete. The React app is served at:")
    print("  http://127.0.0.1:5173")


if __name__ == "__main__":
    main()
