#!/usr/bin/env python3
"""Focused tests for the ground-truth resync/promotion rules in fix_sections.py.

Run:  python scripts/test_fix_sections.py

Covers:
  * _form_tag(): no false PS/P/M tags for the forms CH_FORM/MESSY_NUM match.
  * chapter-side promotion of malformed number forms (answer set = ground truth),
    including tagged PS/P forms and untagged exam forms.
  * answer-side `$N <answer>$` splits WITH and WITHOUT chapter-ground-truth.
"""
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import fix_sections as fs


def eq(a, b, label):
    if a != b:
        raise AssertionError(f"{label}\n  expected: {b!r}\n  actual:   {a!r}")


def make_fp(name, text, **kw):
    """Build a FileProcessor over a temp file."""
    d = tempfile.mkdtemp(prefix="fix_sections_test_")
    p = Path(d) / name
    p.write_text(text, encoding="utf-8")
    return fs.FileProcessor(p, **kw), p


def run_fp(name, text, **kw):
    fp, _ = make_fp(name, text, **kw)
    return fp, fp.run()


# --------------------------------------------------------------------------
# _form_tag() — only run on lines that CH_FORM / MESSY_NUM would accept
# --------------------------------------------------------------------------
def test_form_tag():
    _, p = make_fp("ch01-test.md", "# Chapter 1: Test\n")
    fp = fs.FileProcessor(p)
    cases = {
        "(7) 3": None,       # paren-number, no tag
        "(74) 4": None,      # paren-number, no tag
        "(E) 4": None,       # exam marker, not PS/P/M
        "(P) 8": "P",
        "(M) 3": "M",
        ") 5": None,
        "E1": None,
        "E 12": None,        # exam prefix, not a PS/P/M tag
        "e 3": None,
        "PS 17": "PS",
        "PS $14": "PS",
        "$3 x": None,        # inline-math number, no tag
        "9": None,           # bare number (MESSY_NUM), no tag
    }
    for line, want in cases.items():
        eq(fp._form_tag(line), want, f"_form_tag({line!r})")


# --------------------------------------------------------------------------
# chapter-side promotion (answer set = ground truth), incl. tagged forms
# --------------------------------------------------------------------------
CH_TAGGED = """# Chapter 3: Test

## 3.1 Section

<a id="ch03-ex3C"></a>
### EXERCISE 3C

<a id="ch03-ex3C-q1"></a>
##### Question 1
Question one.

PS 17

Prove that $a=4b$.

<a id="ch03-ex3C-q2"></a>
##### Question 2
Question two.

(P) 8 Prove that $y=\\frac{5}{2}$.
"""


def test_chapter_promotion_tagged():
    fp, out = run_fp("ch03-test.md", CH_TAGGED,
                     ans_nums={"ch03-ex3C": {1, 2, 8, 17}})
    eq('<a id="ch03-ex3C-ps17"></a>' in out, True,
       "PS 17 promoted with ps anchor")
    eq("##### Question PS 17" in out, True, "PS tag kept in heading")
    eq('<a id="ch03-ex3C-p8"></a>' in out, True, "(P) 8 promoted with p anchor")
    eq("##### Question P 8" in out, True, "P tag kept in heading")
    eq("Prove that $y=\\frac{5}{2}$." in out, True, "P 8 body preserved")
    # not promoted when the number is NOT in the answer set
    fp2, out2 = run_fp("ch03-test.md", CH_TAGGED,
                       ans_nums={"ch03-ex3C": {1, 2}})
    eq("##### Question PS 17" in out2, False,
       "PS 17 NOT promoted when 17 not an answer")
    eq("##### Question P 8" in out2, False,
       "(P) 8 NOT promoted when 8 not an answer")


CH_EXAM = """# Chapter 5: Test

## 5.1 Section

<a id="ch05-review"></a>
### END-OF-CHAPTER REVIEW EXERCISE 5

<a id="ch05-review-q1"></a>
##### Question 1
Question one.

E 12 i By differentiating $\\frac{\\cos x}{\\sin x}$, show that if $y=\\cot x$ then $y'=-\\csc^2 x$.
"""


def test_chapter_promotion_exam_form_untagged():
    fp, out = run_fp("ch05-test.md", CH_EXAM,
                     ans_nums={"ch05-review": {1, 12}})
    eq('<a id="ch05-review-q12"></a>' in out, True,
       "E 12 promoted with plain q12 anchor (no tag)")
    eq("##### Question 12" in out, True, "no exam tag in heading")
    eq("i By differentiating $\\frac{\\cos x}{\\sin x}$" in out, True,
       "E 12 body kept")


# --------------------------------------------------------------------------
# answer-side $N <answer>$ split with/without chapter ground truth
# --------------------------------------------------------------------------
ANS = """# Answers: 5 Test

<a id="ch05-ans-review"></a>
### END-OF-CHAPTER REVIEW EXERCISE 5

<a id="ch05-ans-review-q1"></a>
##### Answer 1
Body of answer 1.

<a id="ch05-ans-review-q3"></a>
##### Answer 3
Body of answer 3.

$7 K=7.39, m=1.37$
"""


def test_answer_split_with_chapter_ground_truth():
    fp, out = run_fp("ans05-test.md", ANS,
                     ch_qnums={"ch05-review": {1, 2, 3, 4, 5, 6, 7, 8, 9}})
    eq('<a id="ch05-ans-review-q7"></a>' in out, True,
       "$7 ..$ split via chapter ground truth (7 != prev+1=4)")
    eq("##### Answer 7" in out, True, "Answer 7 heading created")
    eq("$K=7.39, m=1.37$" in out, True, "answer body kept")


def test_answer_no_split_without_ground_truth():
    fp, out = run_fp("ans05-test.md", ANS,
                     ch_qnums={"ch05-review": {1, 2, 3}})
    eq("##### Answer 7" in out, False,
       "no split when 7 is not a chapter question")
    eq("$7 K=7.39, m=1.37$" in out, True, "ambiguous line left untouched")


def test_answer_split_prev_plus_one_still_works():
    # even without chapter truth, n == prev+1 splits (existing behaviour)
    fp, out = run_fp("ans05-test.md", ANS.replace("$7 K=7.39, m=1.37$",
                                                  "$4 K=7.39$"),
                     ch_qnums={"ch05-review": {1, 2, 3}})
    eq("##### Answer 4" in out, True, "n == prev+1 splits without ground truth")


if __name__ == "__main__":
    test_form_tag()
    test_chapter_promotion_tagged()
    test_chapter_promotion_exam_form_untagged()
    test_answer_split_with_chapter_ground_truth()
    test_answer_no_split_without_ground_truth()
    test_answer_split_prev_plus_one_still_works()
    print("ALL FIX_SECTIONS TESTS PASSED")
