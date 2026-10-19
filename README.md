# Maths Pure 2 & 3 — Coursebook → MkDocs Material site

A small, dependency-light pipeline that turns the Mathpix-converted export of the
*Pure Mathematics 2 & 3* coursebook into a local, searchable MkDocs Material site
with a "Practice" section (per-chapter exercises with collapsible answers, plus
key-point round-ups).

## Layout

```
scripts/fix-mathpix.py     raw Mathpix .md        -> <book>/<name>-fixed.md
scripts/split_chapter.py   <name>-fixed.md        -> <book>/split/*.md  (one file per chapter / answers / back matter)
scripts/fix_sections.py    <book>/split/*.md      -> headings + anchors, <book>/split/index.json
scripts/build_site.py      <book>                 -> ./site/   (docs/ + mkdocs.yml, calls build_practice.py)
scripts/build_practice.py  (called by build_site) -> ./site/docs/practice/* (exercises, key points, filter JS/CSS)
scripts/make_stats.py      <book>                 -> ./stats/*.json + ./site-structure.md  (for planning views/searches)
build_all.py               one command for everything above
```

`book` defaults to `Maths Pure 2 & 3-clean_MD` (the folder containing the raw
Mathpix markdown, `images/` and `split/`). The source files and `split/` are never
modified by the site tooling; everything generated lives under `site/`.

## One command

```sh
python build_all.py                          # full pipeline
python build_all.py --local-mathjax          # vendor MathJax instead of the CDN
```

Or step by step:

```sh
pip install -r requirements.txt              # only needed for mkdocs build/serve

python scripts/fix-mathpix.py "Maths Pure 2 & 3-clean_MD/<name>.md"
python scripts/split_chapter.py "Maths Pure 2 & 3-clean_MD/<name>-fixed.md" -o "Maths Pure 2 & 3-clean_MD/split"
python scripts/fix_sections.py "Maths Pure 2 & 3-clean_MD/split"
python scripts/build_site.py "Maths Pure 2 & 3-clean_MD"

cd site && mkdocs serve                      # then open http://127.0.0.1:8000
```

## Site stats / structure (for planning views & searches)

```sh
python scripts/make_stats.py                 # writes stats/ + site-structure.md
```

- `stats/overview.json` — totals and a per-chapter breakdown.
- `stats/connections.json` — every id and what it links to: questions → answers
  (id rule `ch<NN>-<block>-qN` ↔ `ch<NN>-ans-<block>-qN`, `psN`/`pN` normalise
  to `qN`), exercise blocks → their question ids, key points with their
  `next_id` slice boundaries, worked examples, unlinked questions and orphan
  answers.
- `site-structure.md` — a dump of the current MkDocs front end: the generated
  `nav:`, the page list, the anchor inventory per file, and a short
  “how content connects” section.

PREREQUISITE KNOWLEDGE answers are excluded from the stats/answer inventory
(the answers themselves are kept).

## What each step does

### 1. `scripts/fix-mathpix.py` — clean the raw export
Runs inside `$$…$$` display blocks and cleans prose: joins hard-wrapped lines,
normalises `aligned`/`align*` → `align` (so MathJax gets plain `aligned` later),
fixes inline `$…$` spans, escapes table pipes, tidies bolded question numbers
(`**1**`, `**a**`, `**i**`), puts exam-source citations on their own line, and
normalises headings. Idempotent; writes `<name>-fixed.md`.

### 2. `scripts/split_chapter.py` — one file per section
Splits the fixed book into `split/`: one file per chapter (`chNN-…`), one per
answers section (`ansNN-…`), practice papers (`paper-pm2/3`, `anspaper-pm2/3`),
plus `00-front-matter.md`, `zz-glossary.md`, `zz-index.md`. Rewrites image links
for the folder layout.

### 3. `scripts/fix_sections.py` — stable structure + anchors
Runs over `split/*.md` (chapters + answers) and applies a consistent heading
scheme (`#` chapter, `##` numbered sections, `###` exercises/reviews/prereq,
`####` boxes, `##### Question N` / `Answer N`), inserts stable `<a id="…">`
anchors for exercises, worked examples, key points and questions, italicises
exam citations, and wraps trailing `[marks]` in backticks. Writes
`split/index.json` keyed by id (`id`, `type`, `chapter`, `file`, `line`,
`next_id`). `next_id` lets later scripts slice content as *“this anchor → next
anchor”* without trusting line numbers. Re-run with `--check` to verify
idempotency, unique anchors and question↔answer matching.

### 4. `scripts/build_site.py` — the site
Recreates `site/` from scratch:
- copies `split/` → `site/docs/split/` and `images/` → `site/docs/images/`
  (the `../images/…` links keep working);
- in the copies only: `align*`/`align` → `aligned`, trims `$ x $`-style maths,
  strips maths from headings (so the sidebar/TOC shows plain text);
- writes `index.md`, `javascripts/mathjax.js` (with the `[tex]/boldsymbol`
  extension and a re-typeset hook for Material's instant navigation),
  `mkdocs.yml` (Material theme, search, arithmatex `generic`, admonitions,
  explicit `nav:`), and calls `build_practice.py`;
- optional `--local-mathjax` downloads the MathJax bundle + boldsymbol
  extension into `site/docs/javascripts/`.

### 5. `scripts/build_practice.py` — the Practice section
Per-chapter pages under `site/docs/practice/`:
- `chNN-exercises.md` — one `##` section per exercise/review/prereq block; each
  question is `### Question N` with its body, a source link, and a collapsible
  answer (`??? success "Answer"`) paired by id (`chNN-ans-<block>-qN`). The
  prerequisite questions are extracted from the source table. Questions with no
  linkable answer show “Answer not linked”.
- `chNN-keypoints.md` and `all-keypoints.md` — key points sliced from the
  chapter files (tight rule by default, `--full-keypoints` for the whole
  slice), each with a “see in context” link.
- `practice-filter.js` + `practice.css` — a small vanilla toolbar: section
  dropdown, text filter, expand/collapse all. A question and its answer are
  hidden/shown together.

Maths renders via MathJax; a literal `<` inside inline maths is rewritten to
`\lt` because a raw `<` in a `markdown="1"` div breaks Python-Markdown's
raw-HTML parsing.

## Notes & quirks

- **Never edit `split/` or `images/` directly.** Regenerate them with
  `build_all.py` / the individual steps instead; the whole pipeline is
  deterministic and idempotent (`build_site.py` run twice produces identical
  `site/docs`).
- **MathJax + `align`**: MathJax rejects `align` inside display maths, so
  `build_site.py` converts display environments to `aligned`. The 16 inline
  `aligned` inside tables are left alone.
- **`--callouts`** is accepted by `build_site.py` for future use but is off by
  default (headings only).

## Requirements

- Python 3.9+ (standard library).
- `mkdocs-material` (see `requirements.txt`) only for `mkdocs build` / `mkdocs serve`.