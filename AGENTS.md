# AGENTS.md

## What this repo is

Converts the Mathpix OCR Markdown export of the *Pure Mathematics 2 & 3*
coursebook into a React (Vite + TS) reader app. The raw export →
`frontend-data/` pipeline is deterministic Python (stdlib only) in
`scripts/`. Full docs in `README.md`.

## The pipeline (in order)

```sh
python scripts/fix-mathpix.py  "Maths Pure 2 & 3-clean_MD/<raw>.md"   # -> -fixed.md
python scripts/split_chapter.py "-fixed.md" -o ".../split"            # -> split/chNN-*.md etc.
python scripts/fix_sections.py  ".../split"                            # headings + anchors + index.json
python scripts/export_data.py   "Maths Pure 2 & 3-clean_MD"            # -> frontend-data/
```

Or all at once: `python build_frontend.py [--skip-docker] [--corrections PATH]`.

Never edit `split/`, `images/` or `frontend-data/` by hand — regenerate.

## Where each class of fix belongs

- **Glued labels/numbers** (`cUse`, `3In`, `7The`, …) — auto-fixed in
  `scripts/fix-mathpix.py`. It bolds a glued token only when it is the next
  expected label/number (prev + 1), so `3D`/`iOS`/`kHz` are never touched,
  and a bare `Answer` line resets the part-label state for worked examples.
  Tests: `python scripts/test_fix_mathpix.py`.
- **Question/answer bodies the heuristics mis-attribute** — hand-curated in
  `scripts/corrections.json`, keyed by anchor id (see README "Corrections").
  Applied inside `fix_sections.py` on every run. This is the ONLY durable
  place for hand edits to question/answer content. Corrections can create a
  missing question in place (number-ordered) and trim a parent question's
  body — used to repair questions whose OCR-mangled heading was merged into
  the previous question (e.g. review/cross questions missing their exam
  citation). `ch06-ans-review-q12/13/14` are left as orphans because
  `#### FAST FORWARD` boxes inside the block break the split.
- **Structural parsing** (headings, anchors, numbering) — `scripts/fix_sections.py`.
  It is idempotent; verify with `python scripts/fix_sections.py split --check`
  (expect `files that changed on re-run: 0`).

## Rules

- Commit script changes, `corrections.json`, tests and docs — **never
  `split/`, `images/` or `frontend-data/`** (regenerated + copyrighted; all
  gitignored via `*Maths*`).
- After changing a pipeline script, re-run the affected stages and confirm
  `fix_sections.py --check` reports 0 and `export_data.py` says "(idempotent)".
- If you hand-edit `split/` to prototype a fix, capture it as a
  `corrections.json` entry (or a `fix-mathpix.py` rule) — the raw edit will
  be overwritten on the next build.

## Commands

```sh
python scripts/test_fix_mathpix.py    # glued label/number unit tests
python scripts/test_fix_sections.py   # structural parser tests
python scripts/test_math_normalize.py # math normalisation tests
cd frontend && npm run typecheck && npm run test
```
