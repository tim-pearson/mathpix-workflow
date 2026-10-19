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


CH_EXEX = """# Chapter 8: Test

## 8.1 Section

<a id="ch08-review"></a>
### END-OF-CHAPTER REVIEW EXERCISE 8

<a id="ch08-review-q1"></a>
##### Question 1
Question one.

EX 11 Solve the equation $2\\sin x=1$.

Ex 13 Find the exact value of $\\int_{0}^{1} 3 \\tan x \\, \\mathrm{d}x$.
"""


def test_chapter_promotion_ex_ex_forms():
    # CH_FORM accepts "Ex N" / "EX N" (exam prefix with optional x)
    fp, out = run_fp("ch08-test.md", CH_EXEX,
                     ans_nums={"ch08-review": {1, 11, 13}})
    eq('<a id="ch08-review-q11"></a>' in out, True,
       "EX 11 promoted with plain q11 anchor (no tag)")
    eq("##### Question 11" in out, True, "EX 11 heading")
    eq("Solve the equation $2\\sin x=1$" in out, True, "EX 11 body kept")
    eq('<a id="ch08-review-q13"></a>' in out, True,
       "Ex 13 promoted with plain q13 anchor (no tag)")
    eq("##### Question 13" in out, True, "Ex 13 heading")
    eq("Find the exact value of $\\int_{0}^{1} 3 \\tan x \\, \\mathrm{d}x$"
       in out, True, "Ex 13 body kept")
    # not promoted when the number is not in the answer set
    fp2, out2 = run_fp("ch08-test.md", CH_EXEX,
                       ans_nums={"ch08-review": {1}})
    eq("##### Question 11" in out2, False,
       "EX 11 NOT promoted when 11 is not an answer")
    eq("##### Question 13" in out2, False,
       "Ex 13 NOT promoted when 13 is not an answer")


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


# --------------------------------------------------------------------------
# answer-side bare/glued numbered lines (digit-run resolution)
# --------------------------------------------------------------------------
ANS_BARE = """# Answers: 4 Test

<a id="ch04-ans-ex4A"></a>
### EXERCISE 4A

<a id="ch04-ans-ex4A-q1"></a>
##### Answer 1
body one.

<a id="ch04-ans-ex4A-q2"></a>
##### Answer 2
$316 x+y=32$

45

7a

b 2
"""


def test_answer_bare_split_unique_math():
    # "$316 x+y=32$" = question 3 glued to "$16 x+y=32$"; 31/316 are not
    # chapter questions so the reading is unique.
    fp, out = run_fp("ans04-test.md", ANS_BARE,
                     ch_qnums={"ch04-ex4A": {1, 2, 3, 4, 5, 6, 7, 8}})
    lines = out.split("\n")
    eq('<a id="ch04-ans-ex4A-q3"></a>' in out, True,
       "Answer 3 anchor created from $316 x+y=32$")
    eq("##### Answer 3" in out, True, "Answer 3 heading created")
    eq("$16 x+y=32$" in lines, True, "glued remainder kept as Answer 3 body")


def test_answer_bare_split_unique_plain():
    # bare/glued non-math lines split on a unique expected number
    text = ANS_BARE.replace("$316 x+y=32$", "316 x+y=32")
    fp, out = run_fp("ans04-test.md", text,
                     ch_qnums={"ch04-ex4A": {1, 2, 3, 4, 5, 6, 7, 8}})
    lines = out.split("\n")
    eq('<a id="ch04-ans-ex4A-q3"></a>' in out, True,
       "Answer 3 anchor created from bare '316 x+y=32'")
    eq("16 x+y=32" in lines, True, "plain glued remainder as Answer 3 body")
    eq('<a id="ch04-ans-ex4A-q4"></a>' in out, True,
       "'45' split as Answer 4 (4 == prev+1)")
    eq("5" in lines, True, "'45' -> Answer 4 body '5'")
    eq('<a id="ch04-ans-ex4A-q7"></a>' in out, True,
       "'7a' split as Answer 7 (7 in chapter set)")
    eq("a" in lines, True, "'7a' -> Answer 7 body 'a'")


def test_answer_bare_split_ambiguous_math():
    # 3, 31 AND 316 are all plausible -> no split, flagged ambiguous
    fp, out = run_fp("ans04-test.md", ANS_BARE,
                     ch_qnums={"ch04-ex4A": {1, 2, 3, 31, 316}})
    eq("##### Answer 3" in out, False,
       "no split when 3/31/316 are all plausible")
    eq("$316 x+y=32$" in out, True, "ambiguous math line left untouched")
    eq(any("math-split-ambiguous" in fl and "ambiguous:" in fl
           for fl in fp.flags), True, "math ambiguity flagged")


def test_answer_bare_split_ambiguous_glued():
    fp, out = run_fp("ans04-test.md",
                     ANS_BARE.replace("$316 x+y=32$", "316x+y=32"),
                     ch_qnums={"ch04-ex4A": {1, 2, 3, 31, 316}})
    eq("##### Answer 3" in out, False,
       "no split when several readings for glued line")
    eq("316x+y=32" in out, True, "ambiguous glued line left untouched")
    eq(any("bare-num-ambiguous" in fl for fl in fp.flags), True,
       "glued ambiguity flagged")


def test_answer_bare_split_requires_remainder():
    # a dangling "45" (Answer 45 with no content) must NOT split, even when 45
    # is a chapter question, because the only full-number reading has an empty
    # remainder.
    text = """# Answers: 4 Test

<a id="ch04-ans-ex4A"></a>
### EXERCISE 4A

<a id="ch04-ans-ex4A-q1"></a>
##### Answer 1
body one.

45
"""
    fp, out = run_fp("ans04-test.md", text,
                     ch_qnums={"ch04-ex4A": {1, 45}})
    eq("##### Answer 45" in out, False, "no split when remainder is empty")
    eq("45" in out, True, "dangling number left in place")


def test_answer_bare_split_cascade_rejected():
    # "$36 a=...$" = 3 + "$6 a=...$" where 6 is ALSO a question: splitting as
    # Answer 3 would leave a body that re-splits as Answer 6, so the cascade
    # is refused and flagged instead (keeps re-runs a no-op).
    text = """# Answers: 9 Test

<a id="ch09-ans-ex9C"></a>
### EXERCISE 9C

<a id="ch09-ans-ex9C-q2"></a>
##### Answer 2
$36 a+(-2)(4)+(5)(-2)=0 a=3$
"""
    fp, out = run_fp("ans09-test.md", text,
                     ch_qnums={"ch09-ex9C": {1, 2, 3, 4, 5, 6}})
    eq("##### Answer 3" in out, False, "cascading split refused")
    eq("$36 a+(-2)(4)+(5)(-2)=0 a=3$" in out, True, "line left untouched")
    eq(any("would re-split" in fl for fl in fp.flags), True, "cascade flagged")


def test_answer_bare_split_idempotent():
    # running the splitter on its own output must produce identical text
    kw = {"ch_qnums": {"ch04-ex4A": {1, 2, 3, 4, 5, 6, 7, 8}}}
    fp1, out1 = run_fp("ans04-test.md", ANS_BARE, **kw)
    fp2, out2 = run_fp("ans04-test.md", out1, **kw)
    eq(out1, out2, "second run on own output is a no-op")


# --------------------------------------------------------------------------
# corrections.json (id-keyed overrides / creation / deletion)
# --------------------------------------------------------------------------
CORR = {"ch04-ans-ex4A-q3": ["$16 x + y = 32$"]}


def test_corr_override_on_heuristic_split():
    # the bare/math split emits Answer 3, but the corrected body wins
    fp, out = run_fp("ans04-test.md", ANS_BARE,
                     ch_qnums={"ch04-ex4A": {1, 2, 3, 4, 5, 6, 7, 8}},
                     ans_corr=CORR)
    eq("$16 x + y = 32$" in out, True, "corrected body used")
    eq("$16x+y=32$" in out, False, "raw heuristic body suppressed")
    eq(any("corr-override" in n and "ch04-ans-ex4A-q3" in n
           for n in fp.corr_notes), True, "corr-override noted")


def test_corr_override_existing_heading():
    # post-hoc fix: an already-emitted Answer 3 with the old body is replaced
    text = """# Answers: 4 Test

<a id="ch04-ans-ex4A"></a>
### EXERCISE 4A

<a id="ch04-ans-ex4A-q2"></a>
##### Answer 2
-1.5

<a id="ch04-ans-ex4A-q3"></a>
##### Answer 3
$16x+y=32$

<a id="ch04-ans-ex4A-q4"></a>
##### Answer 4
5
"""
    fp, out = run_fp("ans04-test.md", text,
                     ch_qnums={"ch04-ex4A": {1, 2, 3, 4, 5, 6, 7, 8}},
                     ans_corr=CORR)
    eq("$16 x + y = 32$" in out, True, "corrected body replaces old body")
    eq("$16x+y=32$" in out, False, "old body dropped")
    eq("##### Answer 4" in out, True, "following answer kept")


def test_corr_resolve_ambiguous_line():
    # a candidate the heuristic leaves flagged is forced through to its id
    text = """# Answers: 11 Test

<a id="ch11-ans-ex11C"></a>
### EXERCISE 11C

<a id="ch11-ans-ex11C-q2"></a>
##### Answer 2
$z=1$

$5 x=8, y=3$
"""
    fp, out = run_fp("ans11-test.md", text,
                     ch_qnums={"ch11-ex11C": {1, 2, 3, 4}},
                     ans_corr={"ch11-ans-ex11C-q5": ["$x=8, y=3$"]})
    eq('<a id="ch11-ans-ex11C-q5"></a>' in out, True, "Answer 5 created")
    eq("##### Answer 5" in out, True, "Answer 5 heading")
    eq("$x=8, y=3$" in out, True, "corrected body")
    eq("$5 x=8, y=3$" in out, False, "raw line consumed")
    eq(any("corr-create" in n for n in fp.corr_notes), True, "corr-create noted")


def test_corr_force_create_missing_answer():
    text = """# Answers: 3 Test

<a id="ch03-ans-ex3A"></a>
### EXERCISE 3A

<a id="ch03-ans-ex3A-q1"></a>
##### Answer 1
$x=1$

<a id="ch03-ans-ex3A-q2"></a>
##### Answer 2
$x=2$
"""
    fp, out = run_fp("ans03-test.md", text,
                     ch_qnums={"ch03-ex3A": {1, 2, 3, 4}},
                     ans_corr={"ch03-ans-ex3A-q3": ["3.5"]})
    eq('<a id="ch03-ans-ex3A-q3"></a>' in out, True, "Answer 3 anchor created")
    eq("##### Answer 3" in out, True, "Answer 3 heading created")
    eq("3.5" in out, True, "corrected body present")
    eq(any("corr-create" in n and "ch03-ans-ex3A-q3" in n
           for n in fp.corr_notes), True, "force-create noted")


def test_corr_question_override():
    text = """# Chapter 4: Test

<a id="ch04-ex4A"></a>
### EXERCISE 4A

<a id="ch04-ex4A-q3"></a>
##### Question 3
Old question text.
"""
    fp, out = run_fp("ch04-test.md", text,
                     ans_nums={"ch04-ex4A": {1, 2, 3}},
                     q_corr={"ch04-ex4A-q3": ["Corrected question text."]})
    eq("Corrected question text." in out, True, "question body corrected")
    eq("Old question text." in out, False, "old question body dropped")


def test_corr_delete_answer():
    text = """# Answers: 4 Test

<a id="ch04-ans-ex4A"></a>
### EXERCISE 4A

<a id="ch04-ans-ex4A-q2"></a>
##### Answer 2
-1.5

<a id="ch04-ans-ex4A-q3"></a>
##### Answer 3
5

<a id="ch04-ans-ex4A-q4"></a>
##### Answer 4
7
"""
    fp, out = run_fp("ans04-test.md", text,
                     ch_qnums={"ch04-ex4A": {1, 2, 3, 4, 5}},
                     ans_corr={"ch04-ans-ex4A-q3": None})
    eq("ch04-ans-ex4A-q3" in out, False, "deleted answer anchor removed")
    eq("##### Answer 3" in out, False, "deleted heading removed")
    eq("##### Answer 2" in out, True, "previous answer kept")
    eq("##### Answer 4" in out, True, "following answer kept")


def test_corr_idempotent():
    kw = {"ch_qnums": {"ch04-ex4A": {1, 2, 3, 4, 5, 6, 7, 8}},
          "ans_corr": CORR}
    fp1, out1 = run_fp("ans04-test.md", ANS_BARE, **kw)
    fp2, out2 = run_fp("ans04-test.md", out1, **kw)
    eq(out1, out2, "corrections do not break re-run no-op")


def test_corr_match_line():
    # a correction's "match" owns a body line that would otherwise be
    # re-split: "131.8°" is Answer 2's content, not "13"+"1.8°"
    text = """# Answers: 3 Test

<a id="ch03-ans-review"></a>
### END-OF-CHAPTER REVIEW EXERCISE 3

<a id="ch03-ans-review-q1"></a>
##### Answer 1
![](../images/x.jpg)

<a id="ch03-ans-review-q2"></a>
##### Answer 2
131.8°

$3-\\frac{\\sqrt{15}}{8}$

<a id="ch03-ans-review-q4"></a>
##### Answer 4
0\u00b0, 131.8\u00b0, 228.2\u00b0, 360\u00b0
"""
    corr = {
        "ch03-ans-review-q2": {"body": "131.8\u00b0", "match": "131.8\u00b0"},
        "ch03-ans-review-q3":
            {"body": "$-\\frac{\\sqrt{15}}{8}$",
             "match": "$3-\\frac{\\sqrt{15}}{8}$"},
    }
    fp, out = run_fp("ans03-test.md", text,
                     ch_qnums={"ch03-review": {1, 2, 3, 4}},
                     ans_corr=corr)
    eq("##### Answer 2" in out, True, "Answer 2 kept")
    eq("131.8\u00b0" in out, True, "Answer 2 body = 131.8\u00b0")
    eq('<a id="ch03-ans-review-q3"></a>' in out, True, "Answer 3 created")
    eq("$-\\frac{\\sqrt{15}}{8}$" in out, True, "Answer 3 body kept")
    eq("##### Answer 13" in out, False, "no bogus Answer 13 split")
    eq("ch03-ans-review-q13" in out, False, "no duplicate q13 anchor")


def test_corr_override_does_not_swallow_neighbour():
    # overriding Answer 2's body must not delete the next answer's line
    text = """# Answers: 3 Test

<a id="ch03-ans-review"></a>
### END-OF-CHAPTER REVIEW EXERCISE 3

<a id="ch03-ans-review-q1"></a>
##### Answer 1
![](../images/x.jpg)

<a id="ch03-ans-review-q2"></a>
##### Answer 2
old body

<a id="ch03-ans-review-q4"></a>
##### Answer 4
0\u00b0, 131.8\u00b0, 228.2\u00b0, 360\u00b0
"""
    corr = {
        "ch03-ans-review-q2": {"body": "131.8\u00b0", "match": "131.8\u00b0"},
        "ch03-ans-review-q3":
            {"body": "$-\\frac{\\sqrt{15}}{8}$",
             "match": "$3-\\frac{\\sqrt{15}}{8}$"},
    }
    fp, out = run_fp("ans03-test.md", text,
                     ch_qnums={"ch03-review": {1, 2, 3, 4}},
                     ans_corr=corr)
    eq("old body" in out, False, "old Answer 2 body dropped")
    eq("131.8\u00b0" in out, True, "corrected Answer 2 body present")
    eq("##### Answer 4" in out, True, "Answer 4 kept")


if __name__ == "__main__":
    test_form_tag()
    test_chapter_promotion_tagged()
    test_chapter_promotion_exam_form_untagged()
    test_chapter_promotion_ex_ex_forms()
    test_answer_split_with_chapter_ground_truth()
    test_answer_no_split_without_ground_truth()
    test_answer_split_prev_plus_one_still_works()
    test_answer_bare_split_unique_math()
    test_answer_bare_split_unique_plain()
    test_answer_bare_split_ambiguous_math()
    test_answer_bare_split_ambiguous_glued()
    test_answer_bare_split_requires_remainder()
    test_answer_bare_split_cascade_rejected()
    test_answer_bare_split_idempotent()
    test_corr_override_on_heuristic_split()
    test_corr_override_existing_heading()
    test_corr_resolve_ambiguous_line()
    test_corr_force_create_missing_answer()
    test_corr_question_override()
    test_corr_delete_answer()
    test_corr_idempotent()
    test_corr_match_line()
    test_corr_override_does_not_swallow_neighbour()
    print("ALL FIX_SECTIONS TESTS PASSED")
