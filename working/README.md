# working/ — working-out files for the exercise frontend

Drop a markdown file here named after the exact question id, e.g.

    working/ch02-ex2E-q1.md

and `scripts/export_data.py` will attach it to the matching question as
`questions[id].working_md` in `frontend-data/chapters/ch02-*.json`.

Naming convention
-----------------
The file name (without the `.md` extension) must be the question's anchor id
from `split/index.json`:

- plain question    `ch<NN>-<block>-qN`          e.g. `ch02-ex2E-q1`
- PS / P question   `ch<NN>-<block>-psN` / `-pN` e.g. `ch03-ex3A-ps14`

`<NN>` is the zero-padded chapter number (01-11) and `<block>` is the
exercise block id (`ex2E`, `review`, `cross`, `prerequisite`).

Content
-------
The file is normalised with the same KaTeX target as everything else in the
export, so write it in the same markdown-with-maths style as the book:
`$...$` for inline maths, `$$ ... $$` for display maths.

A file whose id does not match any question is reported but ignored.
A template lives at `ch02-ex2E-q1.md.sample` (`.sample` is not picked up).
