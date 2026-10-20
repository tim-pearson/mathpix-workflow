#!/usr/bin/env python3
"""Focused tests for the glued label/number fixes in fix-mathpix.py.

Run:  python scripts/test_fix_mathpix.py

Covers:
  * glued question/item numbers ("3In ..." -> "**3** In ...") only when the
    number is the next expected one (prev_num + 1)
  * glued part labels ("cUse ..." -> "**c** Use ...") only when the letter is
    the next expected label
  * no false positives for real text like "3D" / "iOS" / "kHz" at line start
  * a bare "Answer" line resets label state so solutions restart at "a"
  * idempotency: re-running on the fixed output changes nothing
"""
import subprocess
import sys
import tempfile
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent / "fix-mathpix.py"


def run_fix(text):
    """Run fix-mathpix.py over `text`, return the fixed output."""
    with tempfile.TemporaryDirectory(prefix="fix_mathpix_test_") as d:
        d = Path(d)
        src = d / "in.md"
        dst = d / "out.md"
        src.write_text(text, encoding="utf-8")
        r = subprocess.run(
            [sys.executable, str(SCRIPT), str(src), str(dst)],
            capture_output=True, text=True)
        assert r.returncode == 0, r.stderr
        return dst.read_text(encoding="utf-8")


def eq(a, b, label):
    if a != b:
        raise AssertionError(f"{label}\n  expected: {b!r}\n  actual:   {a!r}")


def has(text, needle, label):
    if needle not in text:
        raise AssertionError(f"{label}\n  missing: {needle!r}\n  in:\n{text}")


def lacks(text, needle, label):
    if needle in text:
        raise AssertionError(f"{label}\n  unexpected: {needle!r}\n  in:\n{text}")


def test_glued_number_promotes():
    text = """### EXERCISE 1A

**1** First question.

**2** Second question.

3Third question.
"""
    out = run_fix(text)
    has(out, "**3** Third question.", "glued number bolded")


def test_glued_number_plus_part_label():
    # "2a Complete ..." -> "**2** **a** Complete ..." (question glued to its
    # first part label, e.g. ch01-ex1B Q2)
    text = """### EXERCISE 1B

**1** Sketch the graphs.

**a** $y=|x+2|$

2a Complete the table of values for $y=|x-3|+2$.

b Draw the graph.

c Describe the transformation.
"""
    out = run_fix(text)
    has(out, "**2** **a** Complete the table", "glued number + part label")
    has(out, "**b** Draw the graph.", "part b bolded after Q2")
    has(out, "**c** Describe the transformation.", "part c bolded after Q2")
    lacks(out, "**1** Sketch the graphs.\n\n**a** $y=|x+2|$\n\n**b** Draw the graph.",
          "Q1 does not swallow Q2's parts")


def test_glued_number_plus_lone_label():
    # answer-side "2a" (number glued to a lone part label) -> "**2** **a**"
    text = """### EXERCISE 1B

**1** a 357

2a

![](./images/x.jpg)

b $x=42$
"""
    out = run_fix(text)
    has(out, "**2** **a**", "lone glued number+label bolded")
    has(out, "**b** $x=42$", "next part bolded")



def test_glued_number_sequence_explore():
    # mirrors the ch03 EXPLORE 3.1 case: items 3 and 4 glued after **1**/**2**
    text = """#### EXPLORE 3.1

**1** Sunita says that.

**2** The diagram shows.

3In the identity.

4In the identity.
"""
    out = run_fix(text)
    has(out, "**3** In the identity.", "explore item 3 bolded")
    has(out, "**4** In the identity.", "explore item 4 bolded")


def test_glued_label_bolds():
    text = """### EXERCISE 1A

**1** Solve.

**a** Part a.

**b** Part b.

cPart c.
"""
    out = run_fix(text)
    has(out, "**c** Part c.", "glued part label bolded")


def test_no_false_positive_not_next_expected():
    # 3D follows nothing (prev_num is None); iOS / kHz aren't next labels
    text = """### EXERCISE 1A

3D diagrams are useful.

iOS and kHz are examples.
"""
    out = run_fix(text)
    has(out, "3D diagrams are useful.", "3D left alone")
    has(out, "iOS and kHz are examples.", "iOS / kHz left alone")


def test_glued_number_not_next_expected_skipped():
    # 5 after prev 2 is not prev+1 -> must be left alone
    text = """### EXERCISE 1A

**2** Second question.

5Fifth question.
"""
    out = run_fix(text)
    has(out, "5Fifth question.", "non-consecutive glued number left alone")


def test_answer_resets_state():
    text = """### WORKED EXAMPLE 1.1

**a** Part a.

**b** Part b.

Answer

aUsing mu as the parameter.
"""
    out = run_fix(text)
    has(out, "**a** Using mu as the parameter.", "label restarts after Answer")


def test_idempotent():
    text = """### EXERCISE 1A

**2** Second question.

3Third question.

**b** Part b.

cPart c.
"""
    once = run_fix(text)
    twice = run_fix(once)
    eq(twice, once, "second pass is a no-op")


if __name__ == "__main__":
    test_glued_number_promotes()
    test_glued_number_plus_part_label()
    test_glued_number_plus_lone_label()
    test_glued_number_sequence_explore()
    test_glued_label_bolds()
    test_no_false_positive_not_next_expected()
    test_glued_number_not_next_expected_skipped()
    test_answer_resets_state()
    test_idempotent()
    print("ALL FIX_MATHPIX TESTS PASSED")
