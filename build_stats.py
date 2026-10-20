
#!/usr/bin/env python3
"""Rebuild frontend-data/stats.json from existing chapter JSON files only."""

import argparse
import json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--data-dir",
        type=Path,
        default=Path(__file__).resolve().parent.parent / "frontend-data",
        help="Frontend data directory (default: ../frontend-data)",
    )
    args = parser.parse_args()

    data_dir = args.data_dir.resolve()
    chapters_dir = data_dir / "chapters"
    stats_path = data_dir / "stats.json"
    manifest_path = data_dir / "manifest.json"

    if not chapters_dir.is_dir():
        raise SystemExit(f"Missing chapters directory: {chapters_dir}")

    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    chapter_files = sorted(chapters_dir.glob("ch??-*.json"))

    if not chapter_files:
        raise SystemExit(f"No chapter JSON files found in {chapters_dir}")

    totals = {
        key: 0
        for key in (
            "questions", "answers", "linked_answers",
            "key_points", "worked_examples", "exercises",
        )
    }
    per_chapter = {}

    for path in chapter_files:
        ch = json.loads(path.read_text(encoding="utf-8"))

        questions = ch.get("questions", {})
        answers = ch.get("answers", {})

        counts = {
            "questions": len(questions),
            "answers": len(answers),
            "linked_answers": sum(
                1 for q in questions.values() if q.get("answer_id")
            ),
            "key_points": len(ch.get("key_points", [])),
            "worked_examples": len(ch.get("worked_examples", [])),
            "exercises": len(ch.get("exercises", [])),
        }

        for key, value in counts.items():
            totals[key] += value

        per_chapter[ch["slug"]] = {
            "chapter": ch["chapter"],
            "title": ch["title"],
            **counts,
            "unlinked_questions": sorted(
                qid for qid, q in questions.items()
                if not q.get("answer_id")
            ),
            "orphan_answers": sorted(
                aid for aid, answer in answers.items()
                if answer.get("question_id") is None
            ),
        }

    stats = {
        "schema_version": manifest.get("schema_version", 1),
        "totals": totals,
        "chapters": per_chapter,
    }

    # This is the only file this script writes.
    stats_path.write_text(
        json.dumps(stats, indent=1, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    print(f"Updated: {stats_path}")
    print(f"Chapters: {len(per_chapter)}")
    print(f"Questions: {totals['questions']}")
    print(f"Answers: {totals['answers']}")
    print(f"Linked answers: {totals['linked_answers']}")
    print(
        "Orphan answers:",
        sum(len(c["orphan_answers"]) for c in per_chapter.values()),
    )
    print(
        "Unlinked questions:",
        sum(len(c["unlinked_questions"]) for c in per_chapter.values()),
    )


if __name__ == "__main__":
    main()

