#!/usr/bin/env python3
"""Stats + structure dump for the site, for building new views/searches.

Usage:  python scripts/make_stats.py [book_dir]

Reads <book>/split/index.json and the generated site, then writes:
  stats/overview.json       totals + per-chapter breakdown
  stats/connections.json    every id and what it links to
  site-structure.md         current MkDocs front-end structure (for planning)

The answer-side inventory excludes PREREQUISITE KNOWLEDGE (those answers live
in tables and aren't needed for the answer pages); the rest of the answers are
kept.
"""
import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

BOOK_DEFAULT = Path("Maths Pure 2 & 3-clean_MD")

QID_RE = re.compile(r"^(ch\d\d)-(.+?)-(?:q|ps|p)(\d+)$")


def answer_id_for(qid):
    m = QID_RE.match(qid)
    if not m:
        return None
    return f"{m.group(1)}-ans-{m.group(2)}-q{m.group(3)}"


def question_id_for(aid):
    m = re.match(r"^(ch\d\d)-ans-(.+?)-q(\d+)$", aid)
    if not m:
        return None
    return f"{m.group(1)}-{m.group(2)}-q{m.group(3)}"


def block_of(qid):
    m = QID_RE.match(qid)
    return m.group(2) if m else None


def chapter_of(aid):
    m = re.match(r"^ch(\d\d)-", aid)
    return int(m.group(1)) if m else None


def page_title(path):
    for ln in path.read_text(encoding="utf-8").splitlines():
        if ln.startswith("# "):
            return ln[2:].strip()
    return path.stem


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("book", nargs="?", default=str(BOOK_DEFAULT))
    args = ap.parse_args()
    book = Path(args.book)
    split = book / "split"

    idx = json.loads((split / "index.json").read_text(encoding="utf-8"))

    types = defaultdict(int)
    for e in idx.values():
        types[e["type"]] += 1

    # --- group everything -------------------------------------------------
    by_file = defaultdict(list)
    for iid, e in idx.items():
        by_file[e["file"]].append((iid, e))

    ch_files = sorted(f for f in by_file if re.match(r"^ch\d\d-", f))
    ans_files = sorted(f for f in by_file if re.match(r"^ans\d\d-", f))

    # chapters
    chapters = {}
    for f in ch_files:
        n = int(re.match(r"^ch(\d\d)-", f).group(1))
        chapters[n] = {
            "num": n,
            "file": f,
            "title": page_title(split / f),
            "answers_file": next((a for a in ans_files
                                  if a.startswith(f"ans{n:02d}-")), None),
            "exercises": [],      # {id, kind, questions:[...]}
            "key_points": [],
            "worked_examples": [],
        }

    exercises = {}     # block id -> {kind, chapter, file, questions:[]}
    for iid, e in idx.items():
        if e["type"] != "exercise":
            continue
        n = chapter_of(iid)
        rec = {"id": iid, "kind": e.get("kind"), "chapter": n,
               "file": e["file"], "questions": []}
        exercises[iid] = rec
        if n in chapters and not e["file"].startswith("ans"):
            chapters[n]["exercises"].append(rec)

    # attach questions to their exercise block
    questions = {}
    for iid, e in idx.items():
        if e["type"] != "question":
            continue
        n = chapter_of(iid)
        blk = block_of(iid)
        aid = answer_id_for(iid)
        linked = aid in idx
        rec = {"chapter": n, "block": f"ch{n:02d}-{blk}" if n else blk,
               "answer": aid if linked else None, "linked": linked}
        questions[iid] = rec
        if blk:
            blkid = f"ch{n:02d}-{blk}"
            if blkid in exercises:
                exercises[blkid]["questions"].append(iid)

    # answers (PREREQUISITE KNOWLEDGE excluded)
    answers = {}
    for iid, e in idx.items():
        if e["type"] != "answer":
            continue
        if "-ans-prerequisite-" in iid:
            continue
        m = re.match(r"^(ch\d\d)-ans-(.+?)-q(\d+)$", iid)
        if m:
            ch, blk, num = m.group(1), m.group(2), m.group(3)
            # a question may be numbered qN, psN or pN
            qid = next((f"{ch}-{blk}-{t}{num}" for t in ("q", "ps", "p")
                        if f"{ch}-{blk}-{t}{num}" in idx), None)
        else:
            qid = None
        answers[iid] = {"chapter": chapter_of(iid), "file": e["file"],
                        "question": qid}

    key_points = {iid: {"chapter": chapter_of(iid), "file": e["file"],
                        "next_id": e.get("next_id")}
                  for iid, e in idx.items() if e["type"] == "key-point"}
    worked = {iid: {"chapter": chapter_of(iid), "file": e["file"]}
              for iid, e in idx.items() if e["type"] == "worked-example"}

    for iid, e in key_points.items():
        n = e["chapter"]
        if n in chapters:
            chapters[n]["key_points"].append(iid)
    for iid, e in worked.items():
        n = e["chapter"]
        if n in chapters:
            chapters[n]["worked_examples"].append(iid)

    unlinked = sorted(i for i, r in questions.items() if not r["linked"])
    orphans = sorted(i for i, r in answers.items() if r["question"] is None)

    # --- overview ---------------------------------------------------------
    per_chapter = []
    for n in sorted(chapters):
        c = chapters[n]
        qs = [i for i, r in questions.items() if r["chapter"] == n]
        per_chapter.append({
            "num": n,
            "file": c["file"],
            "title": c["title"],
            "answers_file": c["answers_file"],
            "questions": len(qs),
            "linked": sum(1 for i in qs if questions[i]["linked"]),
            "unlinked": sum(1 for i in qs if not questions[i]["linked"]),
            "key_points": len(c["key_points"]),
            "worked_examples": len(c["worked_examples"]),
            "exercise_blocks": [
                {"id": e["id"], "kind": e["kind"],
                 "questions": len(e["questions"])}
                for e in c["exercises"]],
        })

    overview = {
        "book": str(book),
        "generated": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "source": "split/index.json",
        "totals": dict(types),
        "exercises_by_kind": dict(
            sorted(defaultdict(int,
                    ((e["kind"], 1) for e in exercises.values())).items())),
        "questions": len(questions),
        "linked_answers": len(questions) - len(unlinked),
        "unlinked_questions": len(unlinked),
        "answers_in_inventory": len(answers),
        "prerequisite_answers_excluded": True,
        "orphan_answers": len(orphans),
        "per_chapter": per_chapter,
    }

    connections = {
        "generated": overview["generated"],
        "types": dict(types),
        "chapters": chapters,
        "exercises": {iid: {"kind": e["kind"], "chapter": e["chapter"],
                            "file": e["file"], "questions": e["questions"]}
                      for iid, e in exercises.items()},
        "questions": questions,
        "answers": answers,
        "key_points": key_points,
        "worked_examples": worked,
        "unlinked_questions": unlinked,
        "answers_without_question": orphans,
    }

    stats = Path("stats")
    stats.mkdir(exist_ok=True)
    (stats / "overview.json").write_text(
        json.dumps(overview, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    (stats / "connections.json").write_text(
        json.dumps(connections, indent=1, sort_keys=True) + "\n",
        encoding="utf-8")

    write_structure(book, Path("site"), overview, connections,
                          types, idx)

    # --- human summary ----------------------------------------------------
    print(f"source: {book}/split/index.json")
    print(f"types: {dict(types)}")
    print(f"questions: {len(questions)} "
          f"({len(questions) - len(unlinked)} linked, "
          f"{len(unlinked)} unlinked)")
    print(f"answers in inventory (prereq excluded): {len(answers)} "
          f"({len(orphans)} without a question)")
    print(f"exercise blocks: {len(exercises)}")
    print(f"key points: {len(key_points)} | worked examples: {len(worked)}")
    print("wrote stats/overview.json, stats/connections.json, site-structure.md")


def write_structure(book, site, overview, connections, types, idx):
    lines = ["# Site structure", "",
             "Generated by `scripts/make_stats.py` — a map of the current "
             "MkDocs front end, so new views/searches can be planned.",
             "",
             f"- Book: `{book}`",
             f"- Stats: see `stats/overview.json`, `stats/connections.json`",
             f"- Generated: {overview['generated']}",
             ""]

    # nav from the generated mkdocs.yml (verbatim indented block)
    yml = site / "mkdocs.yml"
    if yml.exists():
        text = yml.read_text(encoding="utf-8")
        lines += ["## MkDocs nav (`site/mkdocs.yml`)", "", "```yaml"]
        nav = text.split("nav:", 1)[1] if "nav:" in text else ""
        lines += [ln for ln in nav.splitlines() if ln.strip()][:200]
        lines += ["```", ""]

    # pages
    docs = site / "docs"
    md_pages = sorted(p.relative_to(docs).as_posix()
                      for p in docs.rglob("*.md"))
    imgs = sum(1 for p in docs.rglob("*") if p.suffix.lower() in
               (".jpg", ".jpeg", ".png", ".gif", ".svg"))
    lines += ["## Pages", "",
              f"- Markdown pages: {len(md_pages)} "
              f"(under `site/docs/`), images: {imgs}",
              ""]
    for p in md_pages:
        lines.append(f"  - `{p}`")

    # anchor inventory by file (from index.json)
    by_file = defaultdict(Counter)
    for iid, e in idx.items():
        by_file[e["file"]][e["type"]] += 1
    lines += ["", "## Anchor inventory (from `split/index.json`)", "",
              "| file | key-point | worked-example | question | answer | "
              "exercise |", "|---|---|---|---|---|---|"]
    for f in sorted(by_file):
        c = by_file[f]
        lines.append(
            f"| `{f}` | {c['key-point']} | {c['worked-example']} | "
            f"{c['question']} | {c['answer']} | {c['exercise']} |")
    lines += ["", "Every anchor id is unique across files; ids encode the "
              "chapter (`ch02-…`).", ""]

    # how things connect
    lines += ["## How content connects", "",
              "- **question → answer**: id rule "
              "`ch<NN>-<block>-qN` ↔ `ch<NN>-ans-<block>-qN` "
              "(`psN`/`pN` normalise to `qN`). Unlinked ids are listed in "
              "`connections.unlinked_questions`.",
              "- **exercise block → questions**: each exercise id "
              "(`ch<NN>-ex2A`, `…-review`, `…-prerequisite`) lists its "
              "question ids (`connections.exercises`).",
              "- **key point**: body is sliced from its anchor up to "
              "`next_id` (`connections.key_points`); practice pages link "
              "“see in context” to the chapter anchor.",
              "- **practice pages**: `site/docs/practice/chNN-exercises.md` "
              "pairs each question with its answer `<details>` by the same "
              "id rule; `chNN-keypoints.md` and `all-keypoints.md` collect "
              "key points.",
              "- **answers**: `ansNN-*.md` pages; PREREQUISITE KNOWLEDGE "
              "answers are excluded from the inventory.",
              ""]

    Path("site-structure.md").write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    main()