#!/usr/bin/env python3
"""Run the whole book -> React frontend pipeline in one command, from the raw
Mathpix Markdown export all the way to a running Docker container, including
the SQLite-backed question progress + flags backend.

    python build_frontend.py [book_dir] [--skip-docker] [--corrections PATH]

Steps (in order) — the pipeline scripts live in ./scripts:
  1. scripts/fix-mathpix.py    raw Mathpix export  -> <book>/<raw>-fixed.md
  2. scripts/split_chapter.py   fixed markdown      -> <book>/split/*.md
  3. scripts/fix_sections.py    split/*.md          -> headings/anchors +
                                                      index.json (applies
                                                      scripts/corrections.json)
  4. scripts/export_data.py     split/ + images/    -> frontend-data/ (the
                                                      React app's data bundle)
  5. backend/db.py              ensure the local progress.db exists (dev) or
                                                      that the docker volume
                                                      backend serves both
                                                      /api/progress + /api/flags
  6. docker compose down && up --build -d   frontend/ -> build + start the app
                                                      (served on
                                                      http://127.0.0.1:5173)

The DB is created automatically: in Docker it lives at /data/progress.db on the
named `progress-data` volume (kept across rebuilds); when running without
Docker a local `progress.db` is created in the repo root with both the
`progress` and `flags` tables.  Only the stdlib is needed for steps 1-5;
`docker` (with compose) is required for step 6.

Use --skip-docker to stop after the data bundle + local DB are ready.
"""
import argparse
import json
import shutil
import subprocess
import sys
import time
import urllib.request
from pathlib import Path

BOOK_DEFAULT = Path("Maths Pure 2 & 3-clean_no_badges_covered_margins-p1-p352pages")
SCRIPTS = Path(__file__).resolve().parent / "scripts"
BACKEND = Path(__file__).resolve().parent / "backend"
FRONTEND = Path(__file__).resolve().parent / "frontend"
LOCAL_DB = Path(__file__).resolve().parent / "progress.db"

BACKEND_URL = "http://127.0.0.1:5173/api"  # via nginx proxy (frontend port)
CHECK_ID = "ch99-buildcheck-q0"            # throwaway id used for the check
READY_TIMEOUT = 90  # seconds


def run(step, *args):
    cmd = [sys.executable, str(SCRIPTS / step), *[str(a) for a in args]]
    print(f"\n$ {' '.join(cmd)}")
    r = subprocess.run(cmd)
    if r.returncode:
        sys.exit(f"{step} failed with exit code {r.returncode}")


def ensure_local_db():
    """Create progress.db (progress + flags tables) so a non-Docker run has a
    database file to write to.  Idempotent."""
    sys.path.insert(0, str(BACKEND))
    import db as pdb  # stdlib-only sqlite3 layer

    pdb.init(str(LOCAL_DB))  # CREATE TABLE IF NOT EXISTS ...
    print(f"local progress database ready: {LOCAL_DB}"
          f" (tables: progress, flags)")
    return str(LOCAL_DB)


def backend_ok():
    """Full read/write round-trip through the nginx proxy.

    GETs both endpoints (must be real JSON), PUTs a throwaway flag, verifies
    it persisted, then DELETEs it.  This catches every failure mode the plain
    status-200 probe misses: an nginx that isn't proxying /api (it would serve
    index.html with 200), a backend that can't write to SQLite, etc.
    Returns (ok, detail)."""
    try:
        for path in ("/progress/questions", "/flags"):
            with urllib.request.urlopen(BACKEND_URL + path, timeout=5) as r:
                json.loads(r.read().decode())  # must be real JSON
        req = urllib.request.Request(
            BACKEND_URL + "/flags/" + CHECK_ID, method="PUT",
            data=json.dumps({"note": "build-check"}).encode(),
            headers={"Content-Type": "application/json"})
        with urllib.request.urlopen(req, timeout=5) as r:
            if r.status != 200:
                return False, f"PUT /api/flags returned {r.status}"
        with urllib.request.urlopen(BACKEND_URL + "/flags", timeout=5) as r:
            flags = json.loads(r.read().decode())
        if CHECK_ID not in flags:
            return False, "test flag was not persisted (write failed)"
        req = urllib.request.Request(BACKEND_URL + "/flags/" + CHECK_ID,
                                     method="DELETE")
        with urllib.request.urlopen(req, timeout=5) as r:
            if r.status != 204:
                return False, f"DELETE /api/flags returned {r.status}"
        return True, ""
    except Exception as e:  # noqa: BLE001
        return False, f"{type(e).__name__}: {e}"


def wait_roundtrip(timeout):
    deadline = time.time() + timeout
    detail = "timed out"
    while time.time() < deadline:
        ok, detail = backend_ok()
        if ok:
            return True
        time.sleep(2)
    return False


def compose(*args):
    cmd = ["docker", "compose", *[str(a) for a in args]]
    print(f"\n$ {' '.join(cmd)}")
    r = subprocess.run(cmd, cwd=FRONTEND)
    if r.returncode:
        sys.exit(f"docker compose {' '.join(args)} failed with exit code "
                 f"{r.returncode}")


def backend_diagnostics():
    print("\nbackend still did not pass the read/write round-trip. Run these "
          "to see what nginx/backend are actually returning:")
    print("  cd frontend")
    print("  docker compose ps")
    print("  docker compose logs --tail 50 backend")
    print("  curl -i http://127.0.0.1:5173/api/progress/questions")
    print("  curl -i -X PUT http://127.0.0.1:5173/api/flags/ch99-buildcheck-q0"
          " -H 'Content-Type: application/json' -d '{\"note\":\"x\"}'")
    print("\nThe backend stores its SQLite file at /data/progress.db on the")
    print("`progress-data` volume; the progress + flags tables are created on")
    print("startup. If curl returns index.html (not JSON) the frontend image is")
    print("stale — rebuild it with:  docker compose build --no-cache frontend")


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
        ensure_local_db()
        print("\nData bundle ready (Docker skipped). Start the app with:")
        print("  cd frontend && docker compose up --build -d")
        print("or without Docker:")
        print("  PROGRESS_DB=progress.db uvicorn main:app "
              "--app-dir backend --port 8000")
        print("  cd frontend && npm run dev")
        return

    if not shutil.which("docker"):
        ensure_local_db()
        sys.exit(
            "docker is not installed. Install Docker + Compose, then run:"
            "\n  cd frontend && docker compose up --build -d"
            "\nor serve without Docker:"
            "\n  PROGRESS_DB=progress.db uvicorn main:app "
            "--app-dir backend --port 8000"
            "\n  cd frontend && npm run dev   (vite proxies /api -> :8000)")

    # cleanly recreate the stack: remove stale containers/networks but KEEP the
    # progress-data volume (progress + flags survive rebuilds)
    compose("down")
    compose("up", "--build", "-d")

    print(f"\nwaiting for the progress/flags backend (read/write round-trip "
          f"via {BACKEND_URL} ...)")
    if not wait_roundtrip(READY_TIMEOUT):
        # a stale frontend image (nginx without the /api proxy) is the usual
        # cause — rebuild from scratch to rule it out before giving up
        print("  round-trip failed — rebuilding images with --no-cache to "
              "rule out a stale image ...")
        compose("down")
        compose("build", "--no-cache")
        compose("up", "-d")
        if not wait_roundtrip(READY_TIMEOUT):
            backend_diagnostics()
            sys.exit(1)

    print("  backend ready: /api/progress + /api/flags read/write "
          "round-trip passed")

    print("\nPipeline complete. The React app is served at:")
    print("  http://127.0.0.1:5173")
    print("Question progress (green/yellow/red) and flags are persisted in")
    print("SQLite on the `progress-data` volume — safe across rebuilds.")


if __name__ == "__main__":
    main()
