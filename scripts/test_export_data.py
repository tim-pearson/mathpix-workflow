#!/usr/bin/env python3
"""Focused tests for the answer<->question matching in export_data.py.

Run:  python scripts/test_export_data.py

Covers:
  * resolve_answer_question(): direct q/ps/p/m linking and the prerequisite
    convention (chNN-ans-prerequisite-qN -> chNN-prerequisite-qN).
  * genuinely orphaned answers (question not indexed, not prerequisite) stay
    None.
  * build_stats() orphan classification: prerequisite answers are not orphans;
    genuinely unresolved answers still are.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import export_data as ed


def eq(a, b, label):
    if a != b:
        raise AssertionError(f"{label}\n  expected: {b!r}\n  actual:   {a!r}")


def test_resolve_normal_q():
    qs = {"ch01-ex1A-q1", "ch01-ex1A-ps3"}
    eq(ed.resolve_answer_question("ch01-ans-ex1A-q1", qs),
       "ch01-ex1A-q1", "plain q links directly")


def test_resolve_fallback_qpspm():
    # a `-qN` answer whose question is actually tagged PS/P/M still resolves
    # via the q/ps/p/m fallback (answer ids are always -qN in the index)
    qs = {"ch01-ex1A-q1", "ch01-ex1A-p5", "ch01-ex1A-ps3"}
    eq(ed.resolve_answer_question("ch01-ans-ex1A-q5", qs),
       "ch01-ex1A-p5", "qN answer finds P question")
    eq(ed.resolve_answer_question("ch01-ans-ex1A-q3", qs),
       "ch01-ex1A-ps3", "qN answer finds PS question")


def test_resolve_prerequisite():
    # prerequisite questions live in the "Check your skills" table, not as
    # `##### Question` blocks; their answers must still resolve to the
    # frontend's chNN-prerequisite-qN convention
    qs = {"ch01-ex1A-q1"}  # no indexed prerequisite questions
    eq(ed.resolve_answer_question("ch01-ans-prerequisite-q1", qs),
       "ch01-prerequisite-q1", "prerequisite answer resolves by convention")
    eq(ed.resolve_answer_question("ch01-ans-prerequisite-q5", qs),
       "ch01-prerequisite-q5", "prerequisite answer q5 resolves")


def test_resolve_genuine_orphan():
    # an answer whose question is not indexed and is not a prerequisite is a
    # genuine orphan -> None
    qs = {"ch01-ex1A-q1"}
    eq(ed.resolve_answer_question("ch01-ans-cross-q11", qs), None,
       "unresolvable cross answer stays orphaned")
    eq(ed.resolve_answer_question("ch02-ans-ex1A-q1", qs), None,
       "answer referencing another chapter stays orphaned")


def test_build_stats_orphan_classification():
    chapter = {
        "slug": "ch01-algebra",
        "chapter": 1,
        "title": "Algebra",
        "questions": {"ch01-ex1A-q1": {"answer_id": "ch01-ans-ex1A-q1"},
                      "ch01-ex1A-q2": {"answer_id": "ch01-ans-ex1A-q2"}},
        "answers": {
            "ch01-ans-ex1A-q1": {"question_id": "ch01-ex1A-q1"},
            "ch01-ans-ex1A-q2": {"question_id": "ch01-ex1A-q2"},
            "ch01-ans-prerequisite-q1": {"question_id": "ch01-prerequisite-q1"},
            "ch01-ans-prerequisite-q2": {"question_id": "ch01-prerequisite-q2"},
            "ch01-ans-cross-q11": {"question_id": None},
        },
        "key_points": [], "worked_examples": [], "exercises": [],
    }
    stats = ed.build_stats([chapter])
    c = stats["chapters"]["ch01-algebra"]
    eq(c["orphan_answers"], ["ch01-ans-cross-q11"],
       "only the genuinely-unresolved answer is orphaned")
    eq(c["answers"], 5, "all answers counted")
    eq(c["linked_answers"], 2, "linked_answers = questions with answers")


if __name__ == "__main__":
    test_resolve_normal_q()
    test_resolve_fallback_qpspm()
    test_resolve_prerequisite()
    test_resolve_genuine_orphan()
    test_build_stats_orphan_classification()
    print("ALL EXPORT_DATA TESTS PASSED")
