#!/usr/bin/env python3
"""Plain-assert unit tests for math_normalize.py.

Run:  python scripts/test_math_normalize.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import math_normalize as mn


def eq(a, b, label):
    if a != b:
        raise AssertionError(f"{label}\n  expected: {b!r}\n  actual:   {a!r}")


# --------------------------------------------------------------------------
# 1. WORKED EXAMPLE 2.11 (align inside $$)
# --------------------------------------------------------------------------
WE211 = """Answer

a

$$
\\begin{align}
5^{2 x+1} & =7 \\\\
\\log 5^{2 x+1} & =\\log 7
\\end{align}
$$

b

$$
\\begin{align}
3^{2 x} & =4^{x+5}
\\end{align}
$$
"""
we211_mj = mn.normalise(WE211, "mathjax")
eq("\\begin{align}" not in we211_mj, True, "mathjax must replace align")
eq(we211_mj.count("\\begin{aligned}"), 2, "two blocks aligned")
we211_kx = mn.normalise(WE211, "katex")
eq("\\begin{align}" not in we211_kx, True,
   "katex must replace align too (KaTeX has no align)")
eq(we211_kx.count("\\begin{aligned}"), 2, "katex makes aligned")

# --------------------------------------------------------------------------
# 1b. equation / equation* wrappers dropped by katex, kept by mathjax
# --------------------------------------------------------------------------
EQ1 = """$$
\\begin{equation}
x+5=2 \\tag{1}
\\end{equation}
$$"""
eq_kx = mn.normalise(EQ1, "katex")
eq("\\begin{equation}" not in eq_kx, True, "katex drops begin{equation}")
eq("\\end{equation}" not in eq_kx, True, "katex drops end{equation}")
eq("x+5=2 \\tag{1}" in eq_kx, True, "equation content kept inside $$")
eq(mn.normalise(EQ1, "mathjax"), EQ1, "mathjax keeps equation wrapper")
EQ2 = """$$
\\begin{equation*}
y-5=0
\\end{equation*}
$$"""
eq2_kx = mn.normalise(EQ2, "katex")
eq("equation*" not in eq2_kx, True, "katex drops equation* wrapper")
eq("y-5=0" in eq2_kx, True, "equation* content kept")

# --------------------------------------------------------------------------
# 2. KEY POINT 2.3 tables (inline \\begin{aligned} in cells + pipes)
# --------------------------------------------------------------------------
KP23 = """| Multiplication law | Division law | Power law |
| :--- | :--- | :--- |
| $\\begin{aligned} & \\log _{a}(x y) \\\\ & =\\log _{a} x+\\log _{a} y \\end{aligned}$ | $x$ | $y$ |
| $\\left| x \\right|$ | $\\log _{a}\\left(\\frac{x}{y}\\right)$ | $a^{m}$ |
"""
kp23 = mn.normalise(KP23, "mathjax")
eq("\\begin{aligned}" in kp23, True, "table-cell aligned stays")
eq("\\vert" in kp23, True, "pipe inside table-cell maths becomes \\vert")
eq("\\left| x \\right|" in kp23, False, "no bare | inside table maths")
eq("\\left\\vert  x \\right\\vert" in kp23, True,
   "\\left\\vert form kept")

# --------------------------------------------------------------------------
# 3. ch04 heading with \\boldsymbol\\operatorname
# --------------------------------------------------------------------------
HEAD = "### The derivative of $\\boldsymbol{\\operatorname { l n }} \\boldsymbol{x}$"
head_mj = mn.normalise(HEAD, "mathjax")
eq(head_mj, "### The derivative of ln x", "mathjax strips heading maths")
eq("$" not in head_mj, True, "no dollars left in stripped heading")
head_kx = mn.normalise(HEAD, "katex")
eq(head_kx, HEAD, "katex keeps heading maths")
info = mn.find_math_headings(HEAD)
eq(len(info), 1, "heading reported for katex/frontend")
eq(info[0][1], HEAD, "heading text reported")

# --------------------------------------------------------------------------
# 4. sloppy `$ x $` spans (not present in split; covered here anyway)
# --------------------------------------------------------------------------
SLOPPY = "Find $ x $ for values, keep $x$ and $ y $ here."
eq(mn.normalise(SLOPPY, "mathjax"),
   "Find $x$ for values, keep $x$ and $y$ here.",
   "$ x $ / $ y $ trimmed to $x$ / $y$")
eq(mn.normalise(SLOPPY, "katex"),
   "Find $x$ for values, keep $x$ and $y$ here.",
   "katex trims too")

# --------------------------------------------------------------------------
# 5. \\boldsymbol kept by both targets
# --------------------------------------------------------------------------
BM = "The graphs of $\\boldsymbol{y}=\\boldsymbol{\\operatorname { c o s }} \\boldsymbol{\\theta}$."
eq(mn.normalise(BM, "mathjax"), BM, "mathjax keeps \\boldsymbol")
eq(mn.normalise(BM, "katex"), BM, "katex keeps \\boldsymbol")

# --------------------------------------------------------------------------
# idempotency
# --------------------------------------------------------------------------
SAMPLE = (
    "## 1.2 Graphs of $\\boldsymbol{y}=|\\mathbf{f}(\\boldsymbol{x})|$ "
    "where $\\mathbf{f}(\\boldsymbol{x})$ is linear\n\n"
    "Solve $ x < 3 $.\n\n"
    "$$\n\\begin{align}\nx & = 1 \\\\\ny & = 2\n\\end{align}\n$$\n\n"
    "| cell |\n| :--- |\n| $\\left|a\\right| < 5$ |\n"
)
for target in ("mathjax", "katex"):
    once = mn.normalise(SAMPLE, target)
    twice = mn.normalise(once, target)
    eq(once, twice, f"idempotent for {target}")

# --------------------------------------------------------------------------
# \\$ escapes are respected
# --------------------------------------------------------------------------
ESCAPE = "The cost was $\\$ A$ per item, and $x = \\$5$."
eq(mn.normalise(ESCAPE, "mathjax"),
   "The cost was $\\$ A$ per item, and $x = \\$5$.",
   "escaped \\$ inside maths is not a delimiter")
# two unescaped dollars = one inline span; a lone escaped $ outside maths
eq(mn._unescaped_dollars(r"a \$ b $x$ c"), [7, 9],
   "escaped dollar ignored by delimiter scan")

# --------------------------------------------------------------------------
# code fences are never touched
# --------------------------------------------------------------------------
FENCE = ("before\n\n```\n$ x $ not math\n\\begin{align} nope\n"
         "$$\nstill code\n```\n\nafter $ y $ fine\n")
fenced = mn.normalise(FENCE, "mathjax")
eq("$ x $ not math" in fenced, True, "code fence maths untouched")
eq("\\begin{align} nope" in fenced, True, "code fence align untouched")
eq("after $y$ fine" in fenced, True, "prose after fence still normalised")

# --------------------------------------------------------------------------
# line-count / blank-line invariant
# --------------------------------------------------------------------------
blobs = [SAMPLE, WE211, KP23, FENCE, EQ1, EQ2]
for b in blobs:
    a = b.split("\n")
    for target in ("mathjax", "katex"):
        c = mn.normalise(b, target).split("\n")
        eq(len(c), len(a), f"line count preserved ({target})")
        for x, y in zip(a, c):
            eq(not bool(x.strip()) and bool(y.strip()), False,
               f"blank lines stay blank ({target})")

# --------------------------------------------------------------------------
# check() reports problems
# --------------------------------------------------------------------------
bad = "$$\n\\begin{align}\nx & = 1\n\\end{gathered}\n"
probs = mn.check(bad)
kinds = {p["kind"] for p in probs}
eq("unclosed-dollar-block" in kinds, True, "check finds unclosed $$")
eq("begin-end-mismatch" in kinds, True, "check finds mismatched env")

# --------------------------------------------------------------------------
# 6. \\longdiv -> \\,\\big)\\,\\overline{...} (katex + mathjax, maths only)
# --------------------------------------------------------------------------
# real ch01 block (the line lives inside a $$ align)
LD = ("$$\n"
      r"& x - 2 \longdiv { x ^ { 3 } + 2 x ^ { 2 } - 1 1 x + 6 } x^{2} \\"
      "\n$$")
LD_EXPECT = ("$$\n"
             r"& x - 2 \,\big)\,\overline{x ^ { 3 } + 2 x ^ { 2 } - 1 1 x + 6}"
             r" x^{2} \\"
             "\n$$")
for tgt in ("mathjax", "katex"):
    eq(mn.normalise(LD, tgt), LD_EXPECT, f"longdiv rewritten ({tgt})")
eq(mn.normalise(LD, "nvim"), LD, "nvim leaves longdiv untouched")

# a bare longdiv line (not maths) is not rewritten
eq(mn.normalise(r"x - 2 \longdiv { x }", "katex"),
   r"x - 2 \longdiv { x }", "prose longdiv untouched")

# control word must not merge when whitespace collapses
LD_ALPHA = "$$\n\\longdiv { \\alpha x + 1 }\n$$"
eq(mn.normalise(LD_ALPHA, "katex"),
   "$$\n\\,\\big)\\,\\overline{\\alpha x + 1}\n$$",
   "whitespace collapses to one space, control words kept")

# nested braces inside the dividend (a fraction)
LD_NEST = "$$\n\\longdiv { \\frac { x ^ { 2 } + 1 } { x + 3 } }\n$$"
eq(mn.normalise(LD_NEST, "katex"),
   "$$\n\\,\\big)\\,\\overline{\\frac { x ^ { 2 } + 1 } { x + 3 }}\n$$",
   "brace-balanced matcher handles nested braces")

# inside an inline span
eq(mn.normalise("Use $x - 2 \\longdiv { 1 0 x }$ here.", "katex"),
   "Use $x - 2 \\,\\big)\\,\\overline{1 0 x}$ here.",
   "inline longdiv rewritten")

# unbalanced: left untouched and reported by check()
LD_BAD = "$$\n\\longdiv { x ^ { 3 } + 2 x ^ { 2 }"
eq(mn.normalise(LD_BAD, "katex"), LD_BAD, "unbalanced longdiv left untouched")
eq(mn.normalise(LD_BAD, "mathjax"), LD_BAD, "unbalanced longdiv (mathjax)")
ldkinds = {p["kind"] for p in mn.check(LD_BAD)}
eq("longdiv-unbalanced" in ldkinds, True, "check reports unbalanced longdiv")

# multi-line dividend keeps the newline count
LD_MULTI = "$$\n\\longdiv { x ^ { 2 }\n+ y ^ { 2 } }\n$$"
out_multi = mn.normalise(LD_MULTI, "katex")
eq(out_multi.count("\n"), LD_MULTI.count("\n"),
   "longdiv multi-line dividend keeps newline count")
eq("\\,\\big)\\,\\overline{x ^ { 2 } + y ^ { 2 }\n}" in out_multi, True,
   "multi-line dividend still rewritten")

print("ALL TESTS PASSED")


def _main():
    pass


if __name__ == "__main__":
    # place all assertions in module scope so `python test_math_normalize.py`
    # runs them; call a no-op here to keep the script self-runnable.
    _main()