# Maths Pure 2 & 3 — Coursebook → React app

Turns the Mathpix-converted export of the *Pure Mathematics 2 & 3* coursebook
into a **`frontend/` — a React (Vite + TypeScript) app**: reader + exercise
modes, search, formulas, statistics, themes. It renders Markdown + KaTeX from
a self-contained data bundle (`frontend-data/`).

## Quick start (React app)

Requirements: Python 3.9+, Node 20+.

```sh
# 1. generate the data bundle the React app reads
python scripts/export_data.py          # split/ + images/ + working/ -> frontend-data/

# 2. install + run the app (npm run dev auto-copies frontend-data -> public/data)
cd frontend
npm install
npm run dev                            # http://localhost:5173
```

That's it. Search, reader, exercises, key points, formulas and stats all work
from the dev server. If you ever see "Search is unavailable" in the search
box, re-run the sync: `npm run sync-data` (copies `frontend-data/` →
`frontend/public/data/`; `npm run dev` / `npm run build` do this automatically
via their `pre` hooks).

## The full pipeline (from raw export to running app)

### One command (build + start the Docker container)

```sh
python build_frontend.py            # everything below, then builds + starts
                                     # the app in Docker at http://127.0.0.1:5173
```

`build_frontend.py [book_dir] [--skip-docker] [--corrections PATH]` runs the
whole chain from the raw Mathpix Markdown export to a running container:
`fix-mathpix.py` → `split_chapter.py` → `fix_sections.py` (with
`scripts/corrections.json`) → `export_data.py` → `docker compose up --build -d`
in `frontend/`. Use `--skip-docker` to stop after the data bundle is
regenerated (e.g. when Docker isn't available).

### Step by step

```sh
# step by step:
python scripts/fix-mathpix.py   "Maths Pure 2 & 3-clean_MD/2afc0d63-1794-4496-986e-418499784b49.md"
python scripts/split_chapter.py "Maths Pure 2 & 3-clean_MD/2afc0d63-1794-4496-986e-418499784b49-fixed.md" -o "Maths Pure 2 & 3-clean_MD/split"
python scripts/fix_sections.py  "Maths Pure 2 & 3-clean_MD/split"          # applies scripts/corrections.json
python scripts/export_data.py                       # -> frontend-data/

cd frontend
npm install
npm run dev                                         # -> http://localhost:5173
# or serve in Docker:
cd frontend && docker compose up --build -d        # -> http://127.0.0.1:5173
```

`book` defaults to `Maths Pure 2 & 3-clean_MD`. **Never edit `split/`,
`images/` or `frontend-data/` by hand** — always regenerate them through the
scripts above.

## Frontend commands (`frontend/`)

| command | what it does |
| --- | --- |
| `npm run dev` | Vite dev server (runs `sync-data` first) |
| `npm run sync-data` | copy `../frontend-data/` → `public/data/` (idempotent, no rewrites unless changed) |
| `npm run typecheck` | `tsc --noEmit` |
| `npm run test` | Vitest suite (clipboard, resolveImage, working-out, search init, prereq parsing, data shapes) |
| `npm run build` | typecheck + Vite build → `dist/` (runs `sync-data` first) |
| `npm run preview` | serve the built `dist/` locally |
| `npm run audit:katex` | KaTeX compatibility audit over every block in `frontend-data/` |

The app uses hash routing (`#/…`) so it works under any subpath such as
`/tutex/` (`base: "./"`).

### Routes

| route | view |
| --- | --- |
| `#/` | Home — chapter grid, key points, prerequisites, progress placeholder |
| `#/read/:chapter/:sectionId?` | Reader — sections, worked-example cards, key-point callouts, boxes; `…/keypoints` shows all key points |
| `#/practice/:chapter/:exerciseId?` | Exercises — question cards, answers, working-out, copy, formulas panel; `?q=<id>` deep-links a question |
| `#/stats` | Statistics from `stats.json` |

### Data bundle (`frontend-data/`)

Produced by `scripts/export_data.py` (its only reader of `split/`):
`manifest.json`, `chapters/chNN-*.json` (sections, exercises, questions,
answers, key_points, worked_examples, formulas, mentions/mentioned_by),
`search-index.json`, `stats.json`, `images/`. All Markdown is KaTeX-normalised
(`align`→`aligned`, `equation*` wrappers dropped, `\longdiv`→
`\,\big)\,\overline{…}`, `<`/`>`→`\lt`/`\gt`). An answer is "orphaned" only
when its question id cannot be resolved; PREREQUISITE KNOWLEDGE answers are
excluded from that check because their questions live in the "Check your
skills" table, not as `##### Question` blocks (the frontend resolves them as
`chNN-prerequisite-qN` — see `frontend/src/lib/prereq.ts`).

### Progress tracking

Each question card has a **green / yellow / red** status picker (and a ✕ to
clear it). A "Your progress" dashboard on the home page shows per-chapter
attempted/total, green/yellow/red counts and a mastery percentage
(red = 1, yellow = 2, green = 3; mastery is the sum over all questions
divided by all-questions-×-3, so 100% only when everything is green and
unattempted questions count as 0).

Progress is persisted in SQLite by a small FastAPI backend (`backend/`) and is
never part of the exported course data:

```sh
# dev (two terminals):
python -m uvicorn main:app --app-dir backend --reload     # http://localhost:8000
cd frontend && npm run dev                                # http://localhost:5173
                                                        # (vite proxies /api -> :8000)

# docker (build + run both services; nginx proxies /api -> backend):
cd frontend && docker compose up --build -d
```

API (`/api/progress/...`): `PUT /api/progress/<question_id>` with
`{"status":"green"|"yellow"|"red"}`, `DELETE /api/progress/<question_id>`,
`GET /api/progress/questions` (all records), `GET /api/progress/summary`
(per-chapter rollups). The SQLite file lives at `$PROGRESS_DB` — `progress.db`
in dev, `/data/progress.db` inside the backend container — and the compose
file mounts a named `progress-data` volume, so rebuilds and restarts never
erase progress. Tests: `python backend/test_progress.py` and
`npm run test` (frontend).

### Working-out files (`working/`)

Drop a file named after a question id, e.g. `working/ch02-ex2E-q1.md`, and
re-run `python scripts/export_data.py` — it becomes `questions[id].working_md`
and the app shows a "Working out" panel beside the answer. See
`working/README.md` for the convention (a template lives at
`working/ch02-ex2E-q1.md.sample`).

`working/ch03-*.md` are pre-populated (102 files, one per linked question in
the trigonometry chapter) by `scripts/gen_ch03_working.py`. Each opens with an
`AI-GENERATED WORKING` marker (a Markdown comment) so it is clearly
machine-written — review before relying on it, and comment/delete the marker
(or the whole file) as needed.

### Corrections (`scripts/corrections.json`)

The OCR heuristics in `fix_sections.py` recover most answer headings and glue
errors automatically, but a hand-curated `scripts/corrections.json` fixes the
rest — keyed by the anchor ids in `split/index.json`. `fix_sections.py` reads
it on every run (`--corrections PATH` overrides the default). There are three
kinds of entry:

```jsonc
{
  "answers": {
    // override an answer's body (string = one line, list = many lines)
    "ch07-ans-review-q13": "k=16",
    // "match" names the exact source line this answer owns, so a body line
    // the heuristics would otherwise re-split is consumed by this id
    "ch03-ans-review-q2": { "body": "131.8\u00b0", "match": "131.8\u00b0" },
    // null deletes the answer
    "ch04-ans-ex4A-q99": null
  },
  "questions": {
    // same semantics for chapter-side questions
    "ch04-ex4A-q3": "Find the equation of the tangent ...",
    "ch04-ex4A-q99": null
  }
}
```

- **Body override / delete** apply whether the heading already exists on disk
  or is created by the heuristics in the same run.
- **Missing ids are created** (anchor + heading + corrected body) and
  **inserted in number order in place** (not appended at block end), so a
  question the OCR mangled and merged into the previous question's body is
  reinserted where it belongs. The parent question is trimmed by overriding
  its body (the old merged content is discarded).
- **`match`** attaches a specific source line to an id (e.g.
  `"131.8\u00b0"` is Answer 2's content, not a split `"13" + "1.8\u00b0"`).
- Ambiguous `N rest` answer lines are resolved to the corrected id when a
  correction names one of their candidate numbers.

`corrections.json` is the **single central place** for hand-fixed parsing
(OCR-glued headings, merged review/cross/exercise questions, mis-attributed
answer bodies). To repair a question whose heading was mangled: override the
parent question's body to its real content and add the missing question's id
with its real body — `fix_sections.py` recreates it in place. A generator that
extracts the split bodies from `split/` (per-case markers) is a good starting
point for new batches.

Everything is applied inside the structural pass, so corrections work on the
first run and on re-runs, and `fix_sections.py` stays a no-op on its own
output (`--check` reports `files that changed on re-run: 0`). The report
prints which correction ids were applied and any that never matched an id
(typos), and duplicate anchor ids are reported.

### KaTeX audit

`npm run audit:katex` (in `frontend/`) renders every `$…$`/`$$…$$` expression
across all chapters with `throwOnError:true` and lists failing block ids.
Known genuine incompatibilities (shown inline in red by the app): multiple
`\tag` in one `aligned` block, bare `^{\circ}`/`_{\text{…}}` (OCR-dropped
bases), and stray `\` characters (ch09/ch10). These come from the source
export, not the pipeline.

## What each pipeline step does

1. **`scripts/fix-mathpix.py`** — clean the raw Mathpix export → `<name>-fixed.md`
   (joins hard-wrapped lines, normalises `$$` blocks, bolds question numbers
   and part labels, isolates exam citations, normalises headings). Also fixes
   **glued** labels/numbers the OCR leaves attached to the next word — `cUse`
   → `**c** Use`, `7The …` → `**7** The …` — but only when the token is the
   *next expected* one (previous label/number + 1), so real text like `3D` is
   never touched. A bare `Answer` line resets the label state so worked-example
   solutions restart their parts at `a`.
2. **`scripts/split_chapter.py`** — split the fixed book into
   `<book>/split/`: `chNN-*`, `ansNN-*`, `paper-pm2/3`, `anspaper-pm2/3`,
   `00-front-matter`, `zz-glossary`, `zz-index`; rewrites image links.
3. **`scripts/fix_sections.py`** — consistent heading scheme + stable
   `<a id>` anchors, writes `split/index.json`; question numbering uses a
   resync rule with the answer files as ground truth (`ps`/`p`/`m` tags
   supported), plus bare/glued answer-number splitting. Applies
   `scripts/corrections.json` (see above). Idempotent (`--check` verifies).
4. **`scripts/export_data.py`** — split/ → `frontend-data/` (the React data
   bundle; see above). Byte-identical on re-run.

---

### `build_frontend.py` — React pipeline in one command

`python build_frontend.py [book_dir] [--skip-docker] [--corrections PATH]` is
the React path end to end: `fix-mathpix.py` → `split_chapter.py` →
`fix_sections.py` (with corrections) → `export_data.py` → `docker compose down
&& docker compose up --build -d` in `frontend/`. It also sorts out the
progress/flags database:

- **Docker:** recreates the stack cleanly (`down` then `up` — stale
  `maths-backend`/`maths-frontend` containers are replaced) while **keeping
  the `progress-data` volume**, then waits for the backend to answer both
  `/api/progress` and `/api/flags` (a clear diagnostic is printed if it never
  comes up). The SQLite file `/data/progress.db` and its `progress` + `flags`
  tables are created automatically inside the volume on first start.
- **No Docker / `--skip-docker`:** creates a local `progress.db` (with both
  tables) in the repo root and prints the `uvicorn` + `npm run dev` commands.

Requires Docker + Compose for the final step; use `--skip-docker` to stop
after `frontend-data/` (and the local DB) are ready.

## Notes & quirks

- **Never edit `split/`, `images/` or `frontend-data/` directly.** Regenerate
  with the scripts; the whole pipeline is deterministic and idempotent
  (`fix_sections.py --check` and `export_data.py` verify on re-run).
- **Hard fixes the parser can't make** go in `scripts/corrections.json`
  (question/answer bodies keyed by anchor id — see above). Glued labels and
  question numbers are auto-fixed by `fix-mathpix.py`; any remaining hand
  edits to `split/` are lost on the next build, so keep them as corrections.
- **`split/` is gitignored** (it's regenerated + full copyrighted textbook
  text) — commit script changes, `corrections.json` and tests, not `split/`.
- **KaTeX limitations** are handled in `math_normalize.py`
  (`equation*`, `align`, `\longdiv`) — anything remaining is reported by the
  audit and rendered in red by the app.

## Requirements

- Python 3.9+ (standard library only for the pipeline).
- Node 20+ for the React app (`frontend/package.json` is pinned; commit the
  lockfile).
- Docker + Compose for `build_frontend.py`'s final step / `docker compose up`
  (the Docker image builds the app with `npm run build` and serves it via
  nginx).
