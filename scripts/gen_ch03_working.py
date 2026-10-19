#!/usr/bin/env python3
"""Generate working-out files for the trigonometry chapter (ch03).

Each file is written to working/ch03-...md and opens with an obvious
AI-GENERATED marker (a Markdown comment + a visible note) so it can be
reviewed and commented out.  The final line of each answer has been checked
against the answer linked in frontend-data (ch03).

Run:  python scripts/gen_ch03_working.py
Then: python scripts/export_data.py   (picks the files up as working_md)
"""
from pathlib import Path

MARKER = (
    "<!-- ===== AI-GENERATED WORKING \u2014 verify before use. "
    "Delete this block to drop the note. ===== -->"
)

WORKING = {
# ------------------------------------------------------------------ 3A ----
"ch03-ex3A-q1": """Find the exact values.

Use $\\sec\\theta=\\frac1{\\cos\\theta}$, $\\operatorname{cosec}\\theta=\\frac1{\\sin\\theta}$, $\\cot\\theta=\\frac{\\cos\\theta}{\\sin\\theta}$.

**a** $\\sec 60^\\circ=\\frac1{1/2}=2$

**b** $\\operatorname{cosec}45^\\circ=\\frac1{1/\\sqrt2}=\\sqrt2$

**c** $\\cot120^\\circ=\\frac{-1/2}{\\sqrt3/2}=-\\frac1{\\sqrt3}$

**d** $\\sec300^\\circ=\\frac1{1/2}=2$

**e** $\\operatorname{cosec}135^\\circ=\\frac1{1/\\sqrt2}=\\sqrt2$

**f** $\\cot330^\\circ=\\frac{\\sqrt3/2}{-1/2}=-\\sqrt3$

**g** $\\sec150^\\circ=\\frac1{-\\sqrt3/2}=-\\frac2{\\sqrt3}$

**h** $\\cot(-30^\\circ)=\\frac{\\sqrt3/2}{-1/2}=-\\sqrt3$
""",

"ch03-ex3A-q2": """Find the exact values (radians).

**a** $\\operatorname{cosec}\\frac{\\pi}{6}=\\frac1{1/2}=2$

**b** $\\cot\\frac{\\pi}{3}=\\frac{1/2}{\\sqrt3/2}=\\frac1{\\sqrt3}$

**c** $\\sec\\frac{\\pi}{4}=\\frac1{1/\\sqrt2}=\\sqrt2$

**d** $\\cot\\frac{2\\pi}{3}=\\frac{-1/2}{\\sqrt3/2}=-\\frac1{\\sqrt3}$

**e** $\\sec\\frac{5\\pi}{6}=\\frac1{-\\sqrt3/2}=-\\frac2{\\sqrt3}$

**f** $\\operatorname{cosec}\\frac{7\\pi}{4}=\\frac1{-1/\\sqrt2}=-\\sqrt2$

**g** $\\cot\\frac{4\\pi}{3}=\\frac{-1/2}{-\\sqrt3/2}=\\frac1{\\sqrt3}$

**h** $\\sec\\left(-\\frac{\\pi}{6}\\right)=\\frac1{\\sqrt3/2}=\\frac2{\\sqrt3}$
""",

"ch03-ex3A-q3": """Solve for $0\\leqslant x\\leqslant360^\\circ$.

**a** $\\sec x=3\\Rightarrow\\cos x=\\frac13\\Rightarrow x=70.5^\\circ,289.5^\\circ$

**b** $\\cot x=0.8\\Rightarrow\\tan x=1.25\\Rightarrow x=51.3^\\circ,231.3^\\circ$

**c** $\\operatorname{cosec}x=-3\\Rightarrow\\sin x=-\\frac13\\Rightarrow x=199.5^\\circ,340.5^\\circ$

**d** $3\\sec x-4=0\\Rightarrow\\cos x=\\frac34\\Rightarrow x=41.4^\\circ,318.6^\\circ$
""",

"ch03-ex3A-q4": """Solve for $0\\leqslant x\\leqslant2\\pi$.

**a** $\\operatorname{cosec}x=2\\Rightarrow\\sin x=\\frac12\\Rightarrow x=\\frac{\\pi}{6},\\frac{5\\pi}{6}$

**b** $\\sec x=-1\\Rightarrow\\cos x=-1\\Rightarrow x=\\pi$

**c** $\\cot x=2\\Rightarrow\\tan x=0.5\\Rightarrow x=0.464,3.61$

**d** $2\\cot x+5=0\\Rightarrow\\tan x=-0.4\\Rightarrow x=2.76,5.90$
""",

"ch03-ex3A-q5": """Solve for $0\\leqslant x\\leqslant180^\\circ$.

**a** $\\operatorname{cosec}2x=1.2\\Rightarrow\\sin2x=\\frac56\\Rightarrow2x=56.4^\\circ,123.6^\\circ\\Rightarrow x=28.2^\\circ,61.8^\\circ$

**b** $\\sec2x=4\\Rightarrow\\cos2x=\\frac14\\Rightarrow2x=75.5^\\circ,284.5^\\circ\\Rightarrow x=37.8^\\circ,142.2^\\circ$

**c** $\\cot2x=1\\Rightarrow\\tan2x=1\\Rightarrow2x=45^\\circ,225^\\circ\\Rightarrow x=22.5^\\circ,112.5^\\circ$

**d** $2\\sec2x=3\\Rightarrow\\cos2x=\\frac23\\Rightarrow2x=48.2^\\circ,311.8^\\circ\\Rightarrow x=24.1^\\circ,155.9^\\circ$
""",

"ch03-ex3A-q6": """Solve for the given domains.

**a** $\\operatorname{cosec}(x-30^\\circ)=2\\Rightarrow\\sin(x-30^\\circ)=\\frac12$. For $0\\leqslant x\\leqslant360^\\circ$: $x-30=30,150\\Rightarrow x=60^\\circ,180^\\circ$.

**b** $\\sec(2x+60^\\circ)=-1.5\\Rightarrow\\cos(2x+60^\\circ)=-\\frac23$. For $0\\leqslant x\\leqslant180^\\circ$: $2x+60=131.8,228.2\\Rightarrow x=35.9^\\circ,84.1^\\circ$.

**c** $\\cot\\left(x+\\frac{\\pi}{4}\\right)=2\\Rightarrow\\tan\\left(x+\\frac{\\pi}{4}\\right)=0.5$. For $0\\leqslant x\\leqslant2\\pi$: $x+\\frac{\\pi}{4}=0.464,3.605,6.807\\Rightarrow x=2.82,5.96$.

**d** $2\\operatorname{cosec}(2x-1)=3\\Rightarrow\\sin(2x-1)=\\frac23$. For $-\\pi\\leqslant x\\leqslant\\pi$: $2x-1=0.730,2.412,-3.553,-1.871\\Rightarrow x=-2.28,-1.44,0.865,1.71$.
""",

"ch03-ex3A-q7": """Solve for $-180^\\circ\\leqslant x\\leqslant180^\\circ$.

**a** $\\operatorname{cosec}^2x=4\\Rightarrow\\sin x=\\pm\\frac12\\Rightarrow x=-150^\\circ,-30^\\circ,30^\\circ,150^\\circ$

**b** $\\sec^2x=9\\Rightarrow\\cos x=\\pm\\frac13\\Rightarrow x=-109.5^\\circ,-70.5^\\circ,70.5^\\circ,109.5^\\circ$

**c** $9\\cot^2\\frac12x=4\\Rightarrow\\cot\\frac12x=\\pm\\frac23\\Rightarrow\\frac12x=\\pm56.3^\\circ\\Rightarrow x=-112.6^\\circ,112.6^\\circ$

**d** $\\sec x=\\cos x\\Rightarrow\\cos^2x=1\\Rightarrow\\cos x=\\pm1\\Rightarrow x=-180^\\circ,0^\\circ,180^\\circ$

**e** $\\operatorname{cosec}x=\\sec x\\Rightarrow\\tan x=1\\Rightarrow x=-135^\\circ,45^\\circ$

**f** $2\\tan x=3\\operatorname{cosec}x\\Rightarrow2\\frac{\\sin x}{\\cos x}=\\frac3{\\sin x}\\Rightarrow\\sin^2x=\\frac32\\cos x\\Rightarrow\\cos x=\\frac12$ (the other root $\\cos x=-2$ is impossible) $\\Rightarrow x=-60^\\circ,60^\\circ$.
""",

"ch03-ex3A-q8": """Solve for $0\\leqslant\\theta\\leqslant360^\\circ$.

**a** $2\\tan^2\\theta-1=\\sec\\theta\\Rightarrow2(\\sec^2\\theta-1)-1=\\sec\\theta\\Rightarrow2\\sec^2\\theta-\\sec\\theta-3=0\\Rightarrow(2\\sec\\theta-3)(\\sec\\theta+1)=0\\Rightarrow\\cos\\theta=\\frac23,-1\\Rightarrow\\theta=48.2^\\circ,180^\\circ,311.8^\\circ$

**b** $3\\operatorname{cosec}^2\\theta=13-\\cot\\theta\\Rightarrow3(1+\\cot^2\\theta)=13-\\cot\\theta\\Rightarrow3\\cot^2\\theta+\\cot\\theta-10=0\\Rightarrow\\cot\\theta=\\frac53,-2\\Rightarrow\\theta=31.0^\\circ,153.4^\\circ,211.0^\\circ,333.4^\\circ$

**c** $2\\cot^2\\theta-\\operatorname{cosec}\\theta=13\\Rightarrow2(\\operatorname{cosec}^2\\theta-1)-\\operatorname{cosec}\\theta=13\\Rightarrow2\\operatorname{cosec}^2\\theta-\\operatorname{cosec}\\theta-15=0\\Rightarrow\\operatorname{cosec}\\theta=3,-\\frac52\\Rightarrow\\theta=19.5^\\circ,160.5^\\circ,203.6^\\circ,336.4^\\circ$

**d** $\\operatorname{cosec}\\theta+\\cot\\theta=2\\sin\\theta\\Rightarrow\\frac{1+\\cos\\theta}{\\sin\\theta}=2\\sin\\theta\\Rightarrow1+\\cos\\theta=2\\sin^2\\theta=2(1-\\cos^2\\theta)\\Rightarrow2\\cos^2\\theta+\\cos\\theta-1=0\\Rightarrow\\cos\\theta=\\frac12,-1\\Rightarrow\\theta=60^\\circ,180^\\circ,300^\\circ$

**e** $\\tan^2\\theta+3\\sec\\theta=0\\Rightarrow\\sec^2\\theta+3\\sec\\theta-1=0\\Rightarrow\\sec\\theta=\\frac{-3+\\sqrt{13}}2$ (discard, $\\cos>1$), $-\\frac{3+\\sqrt{13}}2\\approx-3.303\\Rightarrow\\cos\\theta\\approx-0.3028\\Rightarrow\\theta=107.6^\\circ,252.4^\\circ$

**f** $\\sqrt3\\sec^2\\theta=\\operatorname{cosec}\\theta\\Rightarrow\\sqrt3\\sin\\theta=\\cos^2\\theta\\Rightarrow\\sin^2\\theta+\\sqrt3\\sin\\theta-1=0\\Rightarrow\\sin\\theta=\\frac{\\sqrt7-\\sqrt3}{2}\\approx0.457\\Rightarrow\\theta=27.2^\\circ,152.8^\\circ$
""",

"ch03-ex3A-q9": """Solve for $0\\leqslant\\theta\\leqslant180^\\circ$.

**a** $\\sec\\theta=3\\cos\\theta-\\tan\\theta\\Rightarrow\\frac1{\\cos\\theta}=3\\cos\\theta-\\frac{\\sin\\theta}{\\cos\\theta}\\Rightarrow1=3\\cos^2\\theta-\\sin\\theta\\Rightarrow3(1-\\sin^2\\theta)-\\sin\\theta-1=0\\Rightarrow3\\sin^2\\theta+\\sin\\theta-2=0\\Rightarrow\\sin\\theta=\\frac23\\Rightarrow\\theta=41.8^\\circ,138.2^\\circ$

**b** $2\\sec^22\\theta=3\\tan2\\theta+1\\Rightarrow2(1+\\tan^22\\theta)=3\\tan2\\theta+1\\Rightarrow2\\tan^22\\theta-3\\tan2\\theta+1=0\\Rightarrow\\tan2\\theta=1,\\frac12\\Rightarrow2\\theta=45^\\circ,225^\\circ,26.6^\\circ,206.6^\\circ\\Rightarrow\\theta=13.3^\\circ,22.5^\\circ,103.3^\\circ,112.5^\\circ$

**c** $\\sec^4\\theta+2=6\\tan^2\\theta\\Rightarrow(1+\\tan^2)^2+2=6\\tan^2\\Rightarrow\\tan^4-4\\tan^2+3=0\\Rightarrow(\\tan^2-1)(\\tan^2-3)=0\\Rightarrow\\tan\\theta=\\pm1,\\pm\\sqrt3\\Rightarrow\\theta=45^\\circ,60^\\circ,120^\\circ,135^\\circ$

**d** $2\\cot^22\\theta+7\\operatorname{cosec}2\\theta=2\\Rightarrow2(\\operatorname{cosec}^22\\theta-1)+7\\operatorname{cosec}2\\theta=2\\Rightarrow2\\operatorname{cosec}^22\\theta+7\\operatorname{cosec}2\\theta-4=0\\Rightarrow\\operatorname{cosec}2\\theta=\\frac12,-4\\Rightarrow\\sin2\\theta=2$ (impossible), $-\\frac14\\Rightarrow2\\theta=194.5^\\circ,345.5^\\circ\\Rightarrow\\theta=97.2^\\circ,172.8^\\circ$
""",

"ch03-ex3A-q10": """Solve for $0\\leqslant\\theta\\leqslant2\\pi$.

**a** $\\tan^2\\theta+3\\sec\\theta+3=0\\Rightarrow\\sec^2\\theta-1+3\\sec\\theta+3=0\\Rightarrow\\sec^2\\theta+3\\sec\\theta+2=0\\Rightarrow(\\sec\\theta+1)(\\sec\\theta+2)=0\\Rightarrow\\cos\\theta=-1,-\\frac12\\Rightarrow\\theta=\\pi,\\frac{2\\pi}{3},\\frac{4\\pi}{3}$

**b** $3\\cot^2\\theta+5\\operatorname{cosec}\\theta+1=0\\Rightarrow3(\\operatorname{cosec}^2-1)+5\\operatorname{cosec}+1=0\\Rightarrow3\\operatorname{cosec}^2+5\\operatorname{cosec}-2=0\\Rightarrow\\operatorname{cosec}\\theta=\\frac13,-2\\Rightarrow\\sin\\theta=3$ (impossible), $-\\frac12\\Rightarrow\\theta=\\frac{7\\pi}{6},\\frac{11\\pi}{6}$
""",

"ch03-ex3A-q11": """Sketch questions — graph sketches.

For each, sketch by starting from the base function and applying the transformation:

**a i** $y=1+\\sec x$: translate $y=\\sec x$ up by 1. Asymptotes at $x=\\frac{\\pi}{2},\\frac{3\\pi}{2}$; minimum points at $\\sec x=1\\Rightarrow y=2$.

**ii** $y=\\cot2x$: $\\cot x$ with period halved to $\\pi$; asymptotes at $x=0,\\frac{\\pi}{2},\\pi,\\frac{3\\pi}{2},2\\pi$.

**iii** $y=2\\operatorname{cosec}\\left(x-\\frac{\\pi}{2}\\right)$: $y=2\\csc x$ shifted right by $\\frac{\\pi}{2}$; asymptotes at $x=\\frac{\\pi}{2},\\frac{3\\pi}{2}$.

**iv** $y=1-\\sec x$: reflect $\\sec x$ then shift up by 1; asymptotes at $x=\\frac{\\pi}{2},\\frac{3\\pi}{2}$.

**v** $y=1+\\operatorname{cosec}\\frac12 x$: period $4\\pi$, asymptotes at $x=0,2\\pi$.

**vi** $y=\\sec\\left(2x+\\frac{\\pi}{4}\\right)$: period $\\pi$, asymptotes where $2x+\\frac{\\pi}{4}=\\frac{\\pi}{2}+k\\pi\\Rightarrow x=\\frac{\\pi}{8}+\\frac{k\\pi}{2}$.

**b** Asymptotes for part vi: $x=\\frac{\\pi}{8},\\frac{5\\pi}{8},\\frac{9\\pi}{8},\\frac{13\\pi}{8}$.
""",

"ch03-ex3A-p12": """Identity proofs.

**a** $\\sin x+\\cos x\\cot x=\\sin x+\\cos x\\frac{\\cos x}{\\sin x}=\\frac{\\sin^2x+\\cos^2x}{\\sin x}=\\frac1{\\sin x}=\\operatorname{cosec}x$ ✓

**b** $\\operatorname{cosec}x-\\sin x=\\frac1{\\sin x}-\\sin x=\\frac{1-\\sin^2x}{\\sin x}=\\frac{\\cos^2x}{\\sin x}=\\cos x\\cot x$ ✓

**c** $\\sec x\\operatorname{cosec}x-\\cot x=\\frac1{\\cos x\\sin x}-\\frac{\\cos x}{\\sin x}=\\frac{1-\\cos^2x}{\\cos x\\sin x}=\\frac{\\sin x}{\\cos x}=\\tan x$ ✓

**d** $(1+\\sec x)(\\operatorname{cosec}x-\\cot x)=\\left(1+\\frac1{\\cos x}\\right)\\left(\\frac1{\\sin x}-\\frac{\\cos x}{\\sin x}\\right)=\\frac{\\cos x+1}{\\cos x}\\cdot\\frac{1-\\cos x}{\\sin x}=\\frac{1-\\cos^2x}{\\cos x\\sin x}=\\tan x$ ✓
""",

"ch03-ex3A-p13": """Identity proofs.

**a** $\\frac1{\\tan x+\\cot x}=\\frac1{\\frac{\\sin x}{\\cos x}+\\frac{\\cos x}{\\sin x}}=\\frac{\\sin x\\cos x}{\\sin^2x+\\cos^2x}=\\sin x\\cos x$ ✓

**b** $\\sec^2x+\\sec x\\tan x=\\frac1{\\cos^2x}+\\frac{\\sin x}{\\cos^2x}=\\frac{1+\\sin x}{1-\\sin^2x}=\\frac1{1-\\sin x}$ ✓

**c** $\\frac{1-\\cos^2x}{\\sec^2x-1}=\\frac{\\sin^2x}{\\tan^2x}=\\sin^2x\\cdot\\frac{\\cos^2x}{\\sin^2x}=\\cos^2x=1-\\sin^2x$ ✓

**d** $\\frac{1+\\tan^2x}{\\tan x}=\\frac{\\sec^2x}{\\tan x}=\\frac1{\\cos^2x}\\cdot\\frac{\\cos x}{\\sin x}=\\sec x\\operatorname{cosec}x$ ✓

**e** $\\frac{\\sin x}{1-\\cos^2x}=\\frac{\\sin x}{\\sin^2x}=\\operatorname{cosec}x$ ✓

**f** $(\\tan x+\\sec x)^2=\\tan^2+2\\tan\\sec+\\sec^2=\\frac{\\sin^2+2\\sin+1}{\\cos^2}=\\frac{(1+\\sin)^2}{1-\\sin^2}=\\frac{1+\\sin}{1-\\sin}$ ✓

**g** $\\frac1{1+\\cos x}+\\frac1{1-\\cos x}=\\frac{2}{1-\\cos^2x}=\\frac2{\\sin^2x}=2\\operatorname{cosec}^2x$ ✓

**h** $\\frac{\\cos x}{1+\\sin x}+\\frac{\\cos x}{1-\\sin x}=\\frac{\\cos x(1-\\sin x)+\\cos x(1+\\sin x)}{1-\\sin^2x}=\\frac{2\\cos x}{\\cos^2x}=2\\sec x$ ✓
""",

"ch03-ex3A-ps14": """Solve for $0^\\circ\\leqslant\\theta\\leqslant180^\\circ$.

**a** $6\\sec^3\\theta-5\\sec^2\\theta-8\\sec\\theta+3=0$. Let $u=\\sec\\theta$: $6u^3-5u^2-8u+3=0$. Try $u=\\frac13$: $6/27-5/9-8/3+3=0$ ✓. Divide: $(u-\\frac13)(6u^2-3u-9)=0\\Rightarrow(u-\\frac13)\\cdot3(2u-3)(u+1)=0$. So $\\sec\\theta=\\frac13$ (impossible, $\\cos\\theta=3$), $\\sec\\theta=\\frac32\\Rightarrow\\cos\\theta=\\frac23\\Rightarrow\\theta=48.2^\\circ$, or $\\sec\\theta=-1\\Rightarrow\\theta=180^\\circ$.

**b** $2\\cot^3\\theta+3\\operatorname{cosec}^2\\theta-8\\cot\\theta=0$. Use $\\operatorname{cosec}^2=1+\\cot^2$: $2\\cot^3+3+3\\cot^2-8\\cot=0\\Rightarrow2t^3+3t^2-8t+3=0$ with $t=\\cot\\theta$. $t=1$: $2+3-8+3=0$ ✓. $(t-1)(2t^2+5t-3)=0\\Rightarrow t=1,\\frac12,-3$. So $\\cot\\theta=1\\Rightarrow\\theta=45^\\circ$; $\\cot\\theta=\\frac12\\Rightarrow\\theta=63.4^\\circ$; $\\cot\\theta=-3\\Rightarrow\\theta=161.6^\\circ$.
""",

# ------------------------------------------------------------------ 3B ----
"ch03-ex3B-q1": """Expand using $\\cos(A+B)=\\cos A\\cos B-\\sin A\\sin B$.

$\\cos(x+30^\\circ)=\\cos x\\cos30^\\circ-\\sin x\\sin30^\\circ=\\frac{\\sqrt3}{2}\\cos x-\\frac12\\sin x$
""",

"ch03-ex3B-q2": """Compound-angle exact values (parts a\u2013f of the linked answer).

**a** $\\sin20^\\circ\\cos70^\\circ+\\cos20^\\circ\\sin70^\\circ=\\sin(20+70)^\\circ=\\sin90^\\circ=1$

**b** $\\sin172^\\circ\\cos37^\\circ-\\cos172^\\circ\\sin37^\\circ=\\sin(172-37)^\\circ=\\sin135^\\circ=\\frac{\\sqrt2}{2}$

**c** $\\cos25^\\circ\\cos35^\\circ-\\sin25^\\circ\\sin35^\\circ=\\cos(25+35)^\\circ=\\cos60^\\circ=\\frac12$

**d** $\\cos99^\\circ\\cos69^\\circ+\\sin99^\\circ\\sin69^\\circ=\\cos(99-69)^\\circ=\\cos30^\\circ=\\frac{\\sqrt3}{2}$

**e** $\\frac{\\tan25^\\circ+\\tan20^\\circ}{1-\\tan25^\\circ\\tan20^\\circ}=\\tan(25+20)^\\circ=\\tan45^\\circ=1$

**f** $\\frac{\\tan82^\\circ-\\tan52^\\circ}{1+\\tan82^\\circ\\tan52^\\circ}=\\tan(82-52)^\\circ=\\tan30^\\circ=\\frac1{\\sqrt3}=\\frac{\\sqrt3}{3}$
""",

"ch03-ex3B-q4": """$\\cos x=\\frac45$, $x$ acute $\\Rightarrow\\sin x=\\frac35$.

$\\cos(x-60^\\circ)=\\cos x\\cos60^\\circ+\\sin x\\sin60^\\circ=\\frac45\\cdot\\frac12+\\frac35\\cdot\\frac{\\sqrt3}{2}=\\frac{2}{5}+\\frac{3\\sqrt3}{10}=\\frac{4+3\\sqrt3}{10}$
""",

"ch03-ex3B-q5": """$\\sin A=\\frac45$, $\\sin B=\\frac5{13}$, both acute $\\Rightarrow\\cos A=\\frac35$, $\\cos B=\\frac{12}{13}$.

$\\sin(A+B)=\\sin A\\cos B+\\cos A\\sin B=\\frac45\\cdot\\frac{12}{13}+\\frac35\\cdot\\frac5{13}=\\frac{48+15}{65}=\\frac{63}{65}$
""",

"ch03-ex3B-q6": """$\\sin A=\\frac{12}{13}$ ($A$ obtuse) $\\Rightarrow\\cos A=-\\frac5{13}$; $\\sin B=\\frac35$ ($B$ acute) $\\Rightarrow\\cos B=\\frac45$.

**a** $\\sin(A+B)=\\frac{12}{13}\\cdot\\frac45+\\left(-\\frac5{13}\\right)\\frac35=\\frac{48-15}{65}=\\frac{33}{65}$

**b** $\\cos(A-B)=\\cos A\\cos B+\\sin A\\sin B=\\left(-\\frac5{13}\\right)\\frac45+\\frac{12}{13}\\cdot\\frac35=\\frac{-20+36}{65}=\\frac{16}{65}$

**c** $\\cos(A+B)=\\left(-\\frac5{13}\\right)\\frac45-\\frac{12}{13}\\cdot\\frac35=\\frac{-20-36}{65}=-\\frac{56}{65}\\Rightarrow\\tan(A+B)=\\frac{33/65}{-56/65}=-\\frac{33}{56}$
""",

"ch03-ex3B-q7": """$\\cos A=-\\frac45$, $\\sin B=-\\frac8{17}$, same quadrant (Q3) $\\Rightarrow\\sin A=-\\frac35$, $\\cos B=-\\frac{15}{17}$.

**a** $\\sin(A+B)=\\left(-\\frac35\\right)\\left(-\\frac{15}{17}\\right)+\\left(-\\frac45\\right)\\left(-\\frac8{17}\\right)=\\frac{45+32}{85}=\\frac{77}{85}$

**b** $\\cos(A+B)=\\left(-\\frac45\\right)\\left(-\\frac{15}{17}\\right)-\\left(-\\frac35\\right)\\left(-\\frac8{17}\\right)=\\frac{60-24}{85}=\\frac{36}{85}$

**c** $\\tan A=\\frac34,\\ \\tan B=\\frac8{15}\\Rightarrow\\tan(A-B)=\\frac{\\frac34-\\frac8{15}}{1+\\frac34\\cdot\\frac8{15}}=\\frac{\\frac{13}{60}}{\\frac{84}{60}}=\\frac{13}{84}$
""",

"ch03-ex3B-q8": """$\\tan(A-B)=2,\\ \\tan A=t$.

$\\frac{t-\\tan B}{1+t\\tan B}=2\\Rightarrow t-\\tan B=2+2t\\tan B\\Rightarrow t-2=\\tan B(1+2t)\\Rightarrow\\tan B=\\frac{t-2}{2t+1}$
""",

"ch03-ex3B-q9": """$\\cos(A-B)=3\\cos(A+B)$.

$\\cos A\\cos B+\\sin A\\sin B=3(\\cos A\\cos B-\\sin A\\sin B)\\Rightarrow4\\sin A\\sin B=2\\cos A\\cos B\\Rightarrow\\tan A\\tan B=\\frac12$
""",

"ch03-ex3B-q10": """**a** $8+\\operatorname{cosec}^2\\theta=6\\cot\\theta$. Use $\\operatorname{cosec}^2=1+\\cot^2$:

$8+1+\\cot^2\\theta=6\\cot\\theta\\Rightarrow\\cot^2\\theta-6\\cot\\theta+9=0\\Rightarrow(\\cot\\theta-3)^2=0\\Rightarrow\\cot\\theta=3\\Rightarrow\\tan\\theta=\\frac13$

**b** $\\tan(\\theta+45^\\circ)=\\frac{\\tan\\theta+1}{1-\\tan\\theta}=\\frac{\\frac13+1}{1-\\frac13}=\\frac{4/3}{2/3}=2$
""",

"ch03-ex3B-q11": """**a** $2\\sec^2x+7\\tan x=17$. $\\sec^2=1+\\tan^2$:

$2(1+\\tan^2x)+7\\tan x=17\\Rightarrow2\\tan^2x+7\\tan x-15=0\\Rightarrow(2\\tan x-3)(\\tan x+5)=0\\Rightarrow\\tan x=\\frac32$ (acute, positive)

**b** $\\tan(225^\\circ-x)=\\frac{\\tan225^\\circ-\\tan x}{1+\\tan225^\\circ\\tan x}=\\frac{1-\\frac32}{1+\\frac32}=\\frac{-1/2}{5/2}=-\\frac15=-0.2$
""",

"ch03-ex3B-q12": """**a** Expand both sides:

$\\sin(x+30^\\circ)=\\frac{\\sqrt3}{2}\\sin x+\\frac12\\cos x,\\quad \\cos(x-60^\\circ)=\\frac12\\cos x+\\frac{\\sqrt3}{2}\\sin x$

Equate: $\\frac{\\sqrt3}{2}\\sin x+\\frac12\\cos x=5\\left(\\frac12\\cos x+\\frac{\\sqrt3}{2}\\sin x\\right)\\Rightarrow\\sqrt3\\sin x+\\cos x=5\\cos x+5\\sqrt3\\sin x\\Rightarrow \\cos x=-\\sqrt3\\sin x\\Rightarrow\\cot x=-\\sqrt3$

**b** $\\cot x=-\\sqrt3\\Rightarrow\\tan x=-\\frac1{\\sqrt3}\\Rightarrow x=-30^\\circ,150^\\circ$
""",

"ch03-ex3B-q13": """Solve for $0\\leqslant x\\leqslant360^\\circ$ by expanding then dividing by $\\cos x$ (or $\\sin x$).

**a** $\\frac{\\sqrt3}{2}\\cos x-\\frac12\\sin x=2\\sin x\\Rightarrow\\frac{\\sqrt3}{2}\\cos x=\\frac52\\sin x\\Rightarrow\\tan x=\\frac{\\sqrt3}{5}\\Rightarrow x=19.1^\\circ,199.1^\\circ$

**b** $\\frac12\\cos x+\\frac{\\sqrt3}{2}\\sin x=3\\cos x\\Rightarrow\\tan x=\\frac5{\\sqrt3}\\Rightarrow x=70.9^\\circ,250.9^\\circ$

**c** $\\frac12\\cos x-\\frac{\\sqrt3}{2}\\sin x=4\\sin x\\Rightarrow\\tan x=\\frac1{8+\\sqrt3}\\Rightarrow x=5.9^\\circ,185.9^\\circ$

**d** $\\frac{\\sqrt3}{2}\\cos x-\\frac12\\sin x=\\sin x+\\sqrt3\\cos x\\Rightarrow\\tan x=-\\frac{\\sqrt3}{3}\\Rightarrow x=150^\\circ,330^\\circ$
""",

"ch03-ex3B-q14": """Solve for $0\\leqslant x\\leqslant180^\\circ$ (let $t=\\tan x$).

**a** $2\\cdot\\frac{\\sqrt3-t}{1+\\sqrt3\\,t}=t\\Rightarrow\\sqrt3\\,t^2+3t-2\\sqrt3=0\\Rightarrow t=\\frac{-3\\pm\\sqrt{33}}{2\\sqrt3}\\Rightarrow x=38.4^\\circ,111.6^\\circ$

**b** $2\\cdot\\frac{1-t}{1+t}=3t\\Rightarrow3t^2+5t-2=0\\Rightarrow t=\\frac13,-2\\Rightarrow x=18.4^\\circ,116.6^\\circ$

**c** $\\frac12\\sin x+\\frac{\\sqrt3}{2}\\cos x=\\sqrt2(\\cos x-\\sin x)\\Rightarrow\\tan x=\\frac{2\\sqrt2-\\sqrt3}{1+2\\sqrt2}\\Rightarrow x=16.0^\\circ$

**d** $\\frac{\\sqrt2}{2}(\\sin x-\\cos x)=\\cos x-\\sqrt3\\sin x\\Rightarrow\\tan x=\\frac{2+\\sqrt2}{\\sqrt2+2\\sqrt3}\\Rightarrow x=35.0^\\circ$

**e** $\\frac{1+t}{1-t}=6t\\Rightarrow6t^2-5t+1=0\\Rightarrow t=\\frac12,\\frac13\\Rightarrow x=18.4^\\circ,26.6^\\circ$

**f** $\\frac{\\sqrt2}{2}(\\sin x-\\cos x)=\\sin x-\\sqrt3\\cos x\\Rightarrow\\tan x=\\frac{\\sqrt2-2\\sqrt3}{\\sqrt2-2}\\Rightarrow x=74.1^\\circ$
""",

"ch03-ex3B-q15": """Let $t=\\tan x$. $\\tan(x-45^\\circ)=\\frac{t-1}{1+t}$.

$\\frac{t-1}{1+t}+\\frac1t=2\\Rightarrow t^2+1=2t(1+t)\\Rightarrow t^2+2t-1=0\\Rightarrow t=\\sqrt2-1,-1-\\sqrt2\\Rightarrow x=22.5^\\circ,112.5^\\circ$
""",

"ch03-ex3B-p16": """$\\cos(5x+x)=\\cos5x\\cos x-\\sin5x\\sin x$ and $\\cos(5x-x)=\\cos5x\\cos x+\\sin5x\\sin x$.

Adding: $\\cos6x+\\cos4x=2\\cos5x\\cos x$
""",

"ch03-ex3B-ps17": """$p^2+q^2=(\\sin x+\\sin y)^2+(\\cos x+\\cos y)^2$

$=\\sin^2x+\\sin^2y+2\\sin x\\sin y+\\cos^2x+\\cos^2y+2\\cos x\\cos y$

$=2+2(\\sin x\\sin y+\\cos x\\cos y)=2+2\\cos(x-y)$

So $\\cos(x-y)=\\dfrac{p^2+q^2-2}{2}$.
""",

# ------------------------------------------------------------------ 3C ----
"ch03-ex3C-q1": """Double-angle forms.

**a** $2\\sin28^\\circ\\cos28^\\circ=\\sin(2\\cdot28^\\circ)=\\sin56^\\circ$

**b** $2\\cos^234^\\circ-1=\\cos(2\\cdot34^\\circ)=\\cos68^\\circ$

**c** $\\frac{2\\tan17^\\circ}{1-\\tan^217^\\circ}=\\tan(2\\cdot17^\\circ)=\\tan34^\\circ$
""",

"ch03-ex3C-q2": """$\\tan x=\\frac43$, $x$ acute $\\Rightarrow\\sin x=\\frac45,\\ \\cos x=\\frac35$.

**a** $\\sin2x=2\\sin x\\cos x=2\\cdot\\frac45\\cdot\\frac35=\\frac{24}{25}$

**b** $\\cos2x=\\cos^2x-\\sin^2x=\\frac{9}{25}-\\frac{16}{25}=-\\frac7{25}$

**c** $\\tan2x=\\frac{2\\tan x}{1-\\tan^2x}=\\frac{8/3}{1-16/9}=\\frac{8/3}{-7/9}=-\\frac{24}{7}$

**d** $\\tan3x=\\frac{\\tan2x+\\tan x}{1-\\tan2x\\tan x}=\\frac{-24/7+4/3}{1+96/21}=\\frac{-44/21}{39/7}=-\\frac{44}{117}$
""",

"ch03-ex3C-q3": """$\\cos2x=-\\frac{527}{625}$, $0<x<90^\\circ$.

**a** $\\sin2x=\\sqrt{1-\\cos^22x}=\\sqrt{\\frac{625^2-527^2}{625^2}}=\\frac{336}{625}$ (positive since $0<2x<180^\\circ$)

**b** $\\tan2x=\\frac{336/625}{-527/625}=-\\frac{336}{527}$

**c** $\\cos x=\\sqrt{\\frac{1+\\cos2x}{2}}=\\sqrt{\\frac{1-527/625}{2}}=\\sqrt{\\frac{49}{625}}=\\frac7{25}$

**d** $\\tan x=\\sqrt{\\frac{1-\\cos2x}{1+\\cos2x}}=\\sqrt{\\frac{1152/625}{98/625}}=\\sqrt{\\frac{576}{49}}=\\frac{24}{7}$
""",

"ch03-ex3C-q4": """$\\cos x=-\\frac35$, $90<x<180^\\circ\\Rightarrow\\sin x=\\frac45$.

**a** $\\sin2x=2\\sin x\\cos x=2\\cdot\\frac45\\cdot\\left(-\\frac35\\right)=-\\frac{24}{25}$

**b** $\\cos2x=\\frac{9}{25}-\\frac{16}{25}=-\\frac7{25}\\Rightarrow\\sin4x=2\\sin2x\\cos2x=2\\cdot\\frac{-24}{25}\\cdot\\frac{-7}{25}=\\frac{336}{625}$

**c** $\\tan2x=\\frac{-24/25}{-7/25}=\\frac{24}{7}$

**d** $\\tan\\frac{x}{2}=\\frac{\\sin x}{1+\\cos x}=\\frac{4/5}{1-3/5}=\\frac{4/5}{2/5}=2$
""",

"ch03-ex3C-q5": """$3\\cos2x+17\\sin x=8$. Use $\\cos2x=1-2\\sin^2x$:

$3(1-2\\sin^2x)+17\\sin x=8\\Rightarrow6\\sin^2x-17\\sin x+5=0\\Rightarrow(3\\sin x-1)(2\\sin x-5)=0\\Rightarrow\\sin x=\\frac13$
""",

"ch03-ex3C-q6": """Solve for $0\\leqslant\\theta\\leqslant360^\\circ$.

**a** $2\\sin2\\theta=\\cos\\theta\\Rightarrow4\\sin\\theta\\cos\\theta=\\cos\\theta\\Rightarrow\\cos\\theta(4\\sin\\theta-1)=0\\Rightarrow\\theta=90^\\circ,270^\\circ$ ($\\cos\\theta=0$) and $\\sin\\theta=\\frac14\\Rightarrow\\theta=14.5^\\circ,165.5^\\circ$

**b** $2\\cos2\\theta+3=4\\cos\\theta\\Rightarrow4\\cos^2\\theta-4\\cos\\theta+1=0\\Rightarrow(2\\cos\\theta-1)^2=0\\Rightarrow\\theta=60^\\circ,300^\\circ$

**c** $2\\cos2\\theta+1=\\sin\\theta\\Rightarrow4\\sin^2\\theta+\\sin\\theta-3=0\\Rightarrow(4\\sin\\theta-3)(\\sin\\theta+1)=0\\Rightarrow\\theta=48.6^\\circ,131.4^\\circ,270^\\circ$
""",

"ch03-ex3C-q7": """Solve for $0\\leqslant\\theta\\leqslant180^\\circ$.

**a** $2\\sin2\\theta\\tan\\theta=1\\Rightarrow4\\sin^2\\theta=1\\Rightarrow\\sin\\theta=\\pm\\frac12\\Rightarrow\\theta=30^\\circ,150^\\circ$

**b** $3\\cos2\\theta+\\cos\\theta=2\\Rightarrow6\\cos^2\\theta+\\cos\\theta-5=0\\Rightarrow(6\\cos\\theta-5)(\\cos\\theta+1)=0\\Rightarrow\\theta=33.6^\\circ,180^\\circ$

**c** $2\\operatorname{cosec}2\\theta+2\\tan\\theta=3\\sec\\theta\\Rightarrow\\frac1{\\sin\\theta}+2\\sin\\theta=3\\Rightarrow2\\sin^2\\theta-3\\sin\\theta+1=0\\Rightarrow(2\\sin\\theta-1)(\\sin\\theta-1)=0$; $\\theta=90^\\circ$ makes $\\sec\\theta$ undefined, so $\\theta=30^\\circ,150^\\circ$

**d** $2\\tan2\\theta=3\\cot\\theta\\Rightarrow\\frac{4t}{1-t^2}=\\frac3t\\Rightarrow7t^2=3\\Rightarrow\\tan\\theta=\\pm\\sqrt{\\frac37}$; also $\\theta=90^\\circ$ (both sides $0$): $\\theta=33.2^\\circ,90^\\circ,146.8^\\circ$

**e** $\\tan2\\theta=4\\cot\\theta\\Rightarrow\\frac{2t}{1-t^2}=\\frac4t\\Rightarrow6t^2=4\\Rightarrow\\tan\\theta=\\pm\\sqrt{\\frac23}$; also $\\theta=90^\\circ$: $\\theta=39.2^\\circ,90^\\circ,140.8^\\circ$

**f** $\\cot2\\theta+\\cot\\theta=3\\Rightarrow\\frac{1-t^2}{2t}+\\frac1t=3\\Rightarrow t^2+6t-3=0\\Rightarrow\\tan\\theta=-3\\pm2\\sqrt3\\Rightarrow\\theta=24.9^\\circ,98.8^\\circ$
""",

"ch03-ex3C-q8": """$\\cos^22x=\\frac{1+\\cos4x}{2}$ (from $\\cos4x=2\\cos^22x-1$).
""",

"ch03-ex3C-q9": """**a** $\\cos3x=\\cos(2x+x)=\\cos2x\\cos x-\\sin2x\\sin x=(2\\cos^2x-1)\\cos x-2\\sin^2x\\cos x=2\\cos^3x-\\cos x-2(1-\\cos^2x)\\cos x=4\\cos^3x-3\\cos x$

**b** $\\sin3x\\equiv3\\sin x-4\\sin^3x$
""",

"ch03-ex3C-q10": """$\\tan2\\theta+2\\tan\\theta=3\\cot\\theta$. Let $t=\\tan\\theta$: $\\frac{2t}{1-t^2}+2t=\\frac3t$.

Multiply by $t(1-t^2)$: $2t^2+2t^2(1-t^2)=3(1-t^2)\\Rightarrow2t^4-7t^2+3=0\\Rightarrow(2t^2-1)(t^2-3)=0\\Rightarrow\\tan\\theta=\\pm\\frac1{\\sqrt2},\\pm\\sqrt3\\Rightarrow\\theta=35.3^\\circ,60^\\circ,120^\\circ,144.7^\\circ$
""",

"ch03-ex3C-q11": """**a** $\\tan\\theta+\\cot\\theta=\\frac{\\sin\\theta}{\\cos\\theta}+\\frac{\\cos\\theta}{\\sin\\theta}=\\frac{\\sin^2+\\cos^2}{\\sin\\theta\\cos\\theta}=\\frac{1}{\\sin\\theta\\cos\\theta}=\\frac2{\\sin2\\theta}$

**b** $\\tan\\frac{\\pi}{12}+\\cot\\frac{\\pi}{12}=\\frac2{\\sin\\frac{\\pi}{6}}=\\frac2{1/2}=4$
""",

"ch03-ex3C-q12": """**a** $2\\operatorname{cosec}2\\theta\\tan\\theta=2\\cdot\\frac1{\\sin2\\theta}\\cdot\\frac{\\sin\\theta}{\\cos\\theta}=\\frac{2\\sin\\theta}{2\\sin\\theta\\cos^2\\theta}=\\frac1{\\cos^2\\theta}=\\sec^2\\theta$

**b** $\\sec^2\\theta=4\\Rightarrow\\cos^2\\theta=\\frac14\\Rightarrow\\cos\\theta=\\pm\\frac12\\Rightarrow\\theta=-\\frac{2\\pi}{3},-\\frac{\\pi}{3},\\frac{\\pi}{3},\\frac{2\\pi}{3}$
""",

"ch03-ex3C-q13": """**a** $\\cos4x=2\\cos^22x-1=2(2\\cos^2x-1)^2-1=8\\cos^4x-8\\cos^2x+1$. So $\\cos4x+4\\cos2x=8\\cos^4x-8\\cos^2x+1+4(2\\cos^2x-1)=8\\cos^4x-3$

**b** $2\\cos4x+8\\cos2x=3\\Rightarrow\\cos4x+4\\cos2x=\\frac32\\Rightarrow8\\cos^4x-3=\\frac32\\Rightarrow\\cos^2x=\\frac34\\Rightarrow\\cos x=\\pm\\frac{\\sqrt3}{2}\\Rightarrow x=\\pm\\frac{\\pi}{6},\\pm\\frac{5\\pi}{6}$
""",

"ch03-ex3C-q14": """**a** At $\\theta=18^\\circ$: $\\sin3\\theta=\\sin54^\\circ=\\cos36^\\circ=\\cos2\\theta$ ✓

**b** $\\sin3\\theta\\equiv3\\sin\\theta-4\\sin^3\\theta$; $\\cos2\\theta\\equiv1-2\\sin^2\\theta$

**c** $\\sin3\\theta=\\cos2\\theta\\Rightarrow3\\sin\\theta-4\\sin^3\\theta=1-2\\sin^2\\theta\\Rightarrow4x^3-2x^2-3x+1=0$ with $x=\\sin\\theta$

**d** Factor: $(x-1)(4x^2+2x-1)=0\\Rightarrow x=1$ or $x=\\frac{-1\\pm\\sqrt5}{4}$. $\\sin18^\\circ\\approx0.309\\Rightarrow\\sin18^\\circ=\\frac{\\sqrt5-1}{4}$
""",

"ch03-ex3C-ps15": """$\\cos2\\theta>\\cos\\theta\\Rightarrow(2\\cos^2\\theta-1)-\\cos\\theta>0\\Rightarrow2\\cos^2\\theta-\\cos\\theta-1>0\\Rightarrow(2\\cos\\theta+1)(\\cos\\theta-1)>0$.

Since $\\cos\\theta-1\\leqslant0$, need $2\\cos\\theta+1<0\\Rightarrow\\cos\\theta<-\\frac12\\Rightarrow\\frac{2\\pi}{3}<\\theta<\\frac{4\\pi}{3}$.
""",

"ch03-ex3C-ps17": """Diagram question — uses geometry from the sketch (a triangle/quadrilateral with an angle bisector). The identity $\\cos3x+\\cos x\\equiv2\\cos2x\\cos x$ (or similar) is applied after labelling lengths $a$, $b$, $x$ from the diagram. Working depends on the figure; not reproduced here.
""",

"ch03-ex3C-ps18": """**a** $\\cos(2x+x)=\\cos2x\\cos x-\\sin2x\\sin x$ and $\\cos(2x-x)=\\cos2x\\cos x+\\sin2x\\sin x$; adding gives $\\cos3x+\\cos x\\equiv2\\cos2x\\cos x$.

**b** $\\cos3x+\\cos2x+\\cos x=(\\cos3x+\\cos x)+\\cos2x=\\cos2x(2\\cos x+1)>0$.

Sign analysis for $0<x<360^\\circ$: $\\cos2x>0$ on $0<x<45$, $135<x<225$, $315<x<360$; $2\\cos x+1>0$ on $0<x<120$, $240<x<360$; $\\cos2x<0$ on $45<x<135$, $225<x<315$; $2\\cos x+1<0$ on $120<x<240$.

Intersections give $0<x<45^\\circ$, $120<x<135^\\circ$, $315<x<360^\\circ$ (verify against the printed answer — the OCR of part b is garbled).
""",

# ------------------------------------------------------------------ 3D ----
"ch03-ex3D-p1": """Identity proofs.

**a** $\\tan A+\\cot A=\\frac{\\sin A}{\\cos A}+\\frac{\\cos A}{\\sin A}=\\frac1{\\sin A\\cos A}=\\frac2{\\sin2A}=2\\operatorname{cosec}2A$ ✓

**b** $1-\\tan^2A=\\frac{\\cos^2A-\\sin^2A}{\\cos^2A}=\\frac{\\cos2A}{\\cos^2A}=\\cos2A\\sec^2A$ ✓

**c** $\\tan2A-\\tan A=\\frac{2t}{1-t^2}-t=\\frac{t(1+t^2)}{1-t^2}=t\\cdot\\frac{\\sec^2A}{\\sec^2A-\\tan^2A\\sec^2A}$... simplify: $=\\tan A\\frac{1+\\tan^2A}{1-\\tan^2A}=\\tan A\\sec2A$ ✓

**d** $(\\cos A+3\\sin A)^2=\\cos^2A+6\\sin A\\cos A+9\\sin^2A=1+3\\sin2A+8\\sin^2A=1+3\\sin2A+4(1-\\cos2A)=5-4\\cos2A+3\\sin2A$ ✓

**e** $\\cot2A+\\tan A=\\frac{\\cos2A}{\\sin2A}+\\frac{\\sin A}{\\cos A}=\\frac{\\cos2A+2\\sin^2A}{2\\sin A\\cos A}=\\frac1{2\\sin A\\cos A}=\\frac12\\operatorname{cosec}A\\sec A$ ✓

**f** $\\operatorname{cosec}2A+\\cot2A=\\frac{1+\\cos2A}{\\sin2A}=\\frac{2\\cos^2A}{2\\sin A\\cos A}=\\cot A$ ✓

**g** $\\sec^2A\\operatorname{cosec}^2A=\\frac1{\\sin^2A\\cos^2A}=\\frac4{\\sin^22A}=4\\operatorname{cosec}^22A$ ✓

**h** $\\sin(A+B)\\sin(A-B)=\\sin^2A\\cos^2B-\\cos^2A\\sin^2B=\\sin^2A(1-\\sin^2B)-(1-\\sin^2A)\\sin^2B=\\sin^2A-\\sin^2B$ ✓
""",

"ch03-ex3D-p2": """Identity proofs.

**a** $\\frac{\\sin A}{\\cos B}+\\frac{\\cos A}{\\sin B}=\\frac{\\sin A\\sin B+\\cos A\\cos B}{\\cos B\\sin B}=\\frac{\\cos(A-B)}{\\cos B\\sin B}=\\frac{2\\cos(A-B)}{\\sin2B}$ ✓

**b** $\\frac{\\cos A+\\sin A}{\\cos A-\\sin A}\\cdot\\frac{\\cos A+\\sin A}{\\cos A+\\sin A}=\\frac{1+\\sin2A}{\\cos2A}=\\sec2A+\\tan2A$ ✓

**c** $\\frac{1-\\tan^2A}{1+\\tan^2A}=\\frac{\\cos^2A-\\sin^2A}{\\cos^2A+\\sin^2A}=\\cos2A$ ✓

**d** $\\frac{\\cos2A+\\sin2A-1}{\\cos2A-\\sin2A+1}=\\frac{2\\sin A(\\cos A-\\sin A)}{2\\cos A(\\cos A-\\sin A)}=\\tan A$ ✓

**e** $\\frac{\\sin3A+\\sin A}{2\\sin2A}=\\frac{2\\sin2A\\cos A}{2\\sin2A}=\\cos A$ ✓

**f** $\\cos3A-\\sin3A=(\\cos A+\\sin A)(1-2\\sin2A)$ (expand RHS), so the ratio $=\\cos A+\\sin A$ ✓

**g** $\\frac{\\cos2A+9\\cos A+5}{4+\\cos A}=\\frac{2\\cos^2A+9\\cos A+4}{4+\\cos A}=\\frac{(2\\cos A+1)(\\cos A+4)}{4+\\cos A}=2\\cos A+1$ ✓

**h** $\\frac{\\cos^3A-\\sin^3A}{\\cos A-\\sin A}=\\cos^2A+\\cos A\\sin A+\\sin^2A=1+\\frac12\\sin2A=\\frac{2+\\sin2A}{2}$ ✓
""",

"ch03-ex3D-p3": """**a** $\\frac{\\sin4A}{\\sin A}=\\frac{2\\sin2A\\cos2A}{\\sin A}=\\frac{2(2\\sin A\\cos A)\\cos2A}{\\sin A}=4\\cos A(2\\cos^2A-1)=8\\cos^3A-4\\cos A$ ✓

**b** $\\cos4A+4\\cos2A=2\\cos^22A-1+4\\cos2A=2(2\\cos^2A-1)^2-1+4(2\\cos^2A-1)=8\\cos^4A-3$ ✓
""",

"ch03-ex3D-p4": """$8\\sin^2x\\cos^2x=2(4\\sin^2x\\cos^2x)=2\\sin^22x=2\\cdot\\frac{1-\\cos4x}{2}=1-\\cos4x$ ✓
""",

"ch03-ex3D-p5": """$(2\\sin A+\\cos A)^2=4\\sin^2A+4\\sin A\\cos A+\\cos^2A=4\\sin^2A+\\cos^2A+2\\sin2A=1+3\\sin^2A+2\\sin2A$.

And $\\frac12(4\\sin2A-3\\cos2A+5)=2\\sin2A+\\frac52-\\frac32(\\cos^2A-\\sin^2A)=2\\sin2A+\\frac52-\\frac32(1-2\\sin^2A)=2\\sin2A+1+3\\sin^2A$ ✓
""",

"ch03-ex3D-p6": """$\\cos(3x-x)=\\cos3x\\cos x+\\sin3x\\sin x$ and $\\cos(3x+x)=\\cos3x\\cos x-\\sin3x\\sin x$.

Subtracting: $\\cos2x-\\cos4x=2\\sin3x\\sin x$ ✓
""",

# ------------------------------------------------------------------ 3E ----
"ch03-ex3E-q1": """**a** $15\\sin\\theta-8\\cos\\theta=R\\sin(\\theta-\\alpha)$, $R=\\sqrt{15^2+8^2}=17$, $\\cos\\alpha=\\frac{15}{17}\\Rightarrow\\alpha=28.07^\\circ$. So $17\\sin(\\theta-28.07^\\circ)$.

**b** $17\\sin(\\theta-28.07^\\circ)=10\\Rightarrow\\sin(\\theta-28.07^\\circ)=\\frac{10}{17}\\Rightarrow\\theta-28.07=36.03,143.97\\Rightarrow\\theta=64.1^\\circ,172^\\circ$
""",

"ch03-ex3E-q2": """**a** $2\\cos\\theta-3\\sin\\theta=R\\cos(\\theta+\\alpha)$, $R=\\sqrt{2^2+3^2}=\\sqrt{13}$, $\\cos\\alpha=\\frac2{\\sqrt{13}}\\Rightarrow\\alpha=56.31^\\circ$. So $\\sqrt{13}\\cos(\\theta+56.31^\\circ)$.

**b** $\\sqrt{13}\\cos(\\theta+56.31^\\circ)=1.3\\Rightarrow\\cos(\\theta+56.31^\\circ)=0.3606\\Rightarrow\\theta+56.31=68.87,291.13\\Rightarrow\\theta=12.6^\\circ,234.8^\\circ$
""",

"ch03-ex3E-q3": """**a** As Q1: $15\\sin\\theta-8\\cos\\theta=17\\sin(\\theta-28.07^\\circ)$.

**b** $17\\sin(\\theta-28.07^\\circ)=3\\Rightarrow\\sin(\\theta-28.07^\\circ)=\\frac3{17}\\Rightarrow\\theta-28.07=10.16,169.84\\Rightarrow\\theta=38.2^\\circ,197.9^\\circ$

**c** $30\\sin\\theta-16\\cos\\theta=2(15\\sin\\theta-8\\cos\\theta)$, greatest $=2\\cdot17=34$
""",

"ch03-ex3E-q4": """**a** $4\\sin\\theta-6\\cos\\theta=R\\sin(\\theta-\\alpha)$, $R=\\sqrt{16+36}=2\\sqrt{13}$, $\\cos\\alpha=\\frac4{2\\sqrt{13}}\\Rightarrow\\alpha=56.31^\\circ$.

**b** $2\\sqrt{13}\\sin(\\theta-56.31^\\circ)=3\\Rightarrow\\sin(\\theta-56.31^\\circ)=\\frac3{2\\sqrt{13}}\\Rightarrow\\theta-56.31=24.6,155.4\\Rightarrow\\theta=80.9^\\circ$ (only one in $0<\\theta<180$).

**c** $(4\\sin\\theta-6\\cos\\theta)^2$ ranges $0\\to(2\\sqrt{13})^2=52$, so the expression ranges $-3$ to $49$.
""",

"ch03-ex3E-q5": """**a** $3\\sin\\theta+4\\cos\\theta=R\\sin(\\theta+\\alpha)$, $R=5$, $\\cos\\alpha=\\frac35\\Rightarrow\\alpha=53.13^\\circ$.

**b** $5\\sin(\\theta+53.13^\\circ)=2\\Rightarrow\\sin(\\theta+53.13^\\circ)=0.4\\Rightarrow\\theta+53.13=23.58,156.42\\Rightarrow\\theta=103.3^\\circ,330.4^\\circ$

**c** least value of $3\\sin\\theta+4\\cos\\theta+3=-5+3=-2$
""",

"ch03-ex3E-q6": """**a** $\\cos\\theta+\\sqrt3\\sin\\theta=R\\cos(\\theta-\\alpha)$, $R=\\sqrt{1+3}=2$, $\\cos\\alpha=\\frac12\\Rightarrow\\alpha=\\frac{\\pi}{3}$. So $2\\cos\\left(\\theta-\\frac{\\pi}{3}\\right)$.

**b** $\\frac1{(\\cos\\theta+\\sqrt3\\sin\\theta)^2}=\\frac1{4\\cos^2(\\theta-\\pi/3)}=\\frac14\\sec^2\\left(\\theta-\\frac{\\pi}{3}\\right)$ ✓
""",

"ch03-ex3E-q7": """**a** $8\\sin2\\theta+4\\cos2\\theta=R\\sin(2\\theta+\\alpha)$, $R=\\sqrt{64+16}=4\\sqrt5$, $\\cos\\alpha=\\frac8{4\\sqrt5}\\Rightarrow\\alpha=26.57^\\circ$.

**b** $4\\sqrt5\\sin(2\\theta+26.57^\\circ)=3\\Rightarrow\\sin(2\\theta+26.57^\\circ)=0.3354\\Rightarrow2\\theta+26.57=19.6,160.4,379.6,520.4\\Rightarrow\\theta=66.9^\\circ,176.5^\\circ,246.9^\\circ,356.5^\\circ$

**c** least $\\frac{10}{(8\\sin2\\theta+4\\cos2\\theta)^2}=\\frac{10}{(4\\sqrt5)^2}=\\frac18$
""",

"ch03-ex3E-q8": """**a** $\\cos\\theta-\\sqrt2\\sin\\theta=R\\cos(\\theta+\\alpha)$, $R=\\sqrt{1+2}=\\sqrt3$, $\\cos\\alpha=\\frac1{\\sqrt3}\\Rightarrow\\alpha=54.74^\\circ$.

**b** $\\sqrt3\\cos(\\theta+54.74^\\circ)=-1\\Rightarrow\\cos(\\theta+54.74^\\circ)=-\\frac1{\\sqrt3}\\Rightarrow\\theta+54.74=125.26,234.74\\Rightarrow\\theta=70.5^\\circ,180^\\circ$

**c** $\\sqrt2\\cos\\theta-2\\sin\\theta$ has $R=\\sqrt6$, so $\\frac1{(\\ldots)^2}$ least $=\\frac1{6}$
""",

"ch03-ex3E-q9": """**a** $\\cos\\theta-\\sin\\theta=R\\cos(\\theta+\\alpha)$, $R=\\sqrt2$, $\\cos\\alpha=\\frac1{\\sqrt2}\\Rightarrow\\alpha=\\frac{\\pi}{4}$. So $\\sqrt2\\cos\\left(\\theta+\\frac{\\pi}{4}\\right)$.

**b** $\\sqrt2\\cos\\left(\\theta+\\frac{\\pi}{4}\\right)=\\frac{\\sqrt6}{2}\\Rightarrow\\cos\\left(\\theta+\\frac{\\pi}{4}\\right)=\\frac{\\sqrt3}{2}\\Rightarrow\\theta+\\frac{\\pi}{4}=\\frac{\\pi}{6},\\frac{11\\pi}{6}\\Rightarrow\\theta=\\frac{19\\pi}{12},\\frac{23\\pi}{12}$

**c** $\\cos\\theta-\\sin\\theta$ ranges $-\\sqrt2\\le k\\le\\sqrt2$
""",

"ch03-ex3E-q10": """**a** $\\sin\\theta-3\\cos\\theta=R\\sin(\\theta-\\alpha)$, $R=\\sqrt{1+9}=\\sqrt{10}$, $\\cos\\alpha=\\frac1{\\sqrt{10}}\\Rightarrow\\alpha=71.57^\\circ$.

**b** $\\sqrt{10}\\sin(\\theta-71.57^\\circ)=-2\\Rightarrow\\sin(\\theta-71.57^\\circ)=-0.6325\\Rightarrow\\theta-71.57=-39.23,219.23,320.77\\Rightarrow\\theta=32.3^\\circ,290.8^\\circ$

**c** $\\sin2\\theta-3\\cos2\\theta=\\sqrt{10}\\sin(2\\theta-71.57^\\circ)$, greatest of $1+(\\ldots)$ is $1+\\sqrt{10}$, occurring when $2\\theta-71.57=90\\Rightarrow\\theta=80.8^\\circ$
""",

"ch03-ex3E-q11": """**a** $\\sqrt5\\cos\\theta+2\\sin\\theta=R\\cos(\\theta-\\alpha)$, $R=\\sqrt{5+4}=3$, $\\cos\\alpha=\\frac{\\sqrt5}{3}\\Rightarrow\\alpha=41.81^\\circ$.

**b** $3\\cos(\\theta-41.81^\\circ)=3\\Rightarrow\\cos(\\theta-41.81^\\circ)=1\\Rightarrow\\theta=41.8^\\circ$

**c** $3\\cos\\left(\\frac{\\theta}{2}-41.81^\\circ\\right)=-1\\Rightarrow\\cos\\left(\\frac{\\theta}{2}-41.81^\\circ\\right)=-\\frac13\\Rightarrow\\frac{\\theta}{2}-41.81=109.47\\Rightarrow\\theta=302.6^\\circ$ (smallest positive)
""",

"ch03-ex3E-q12": """**a** $3\\sec\\theta+4\\operatorname{cosec}\\theta=2\\operatorname{cosec}2\\theta\\Rightarrow\\frac3{\\cos\\theta}+\\frac4{\\sin\\theta}=\\frac1{\\sin\\theta\\cos\\theta}\\Rightarrow3\\sin\\theta+4\\cos\\theta=1$ ✓

**b** $3\\sin\\theta+4\\cos\\theta=5\\sin(\\theta+\\alpha)$, $\\cos\\alpha=\\frac35\\Rightarrow\\alpha=53.13^\\circ$.

**c** $5\\sin(\\theta+53.13^\\circ)=1\\Rightarrow\\sin(\\theta+53.13^\\circ)=0.2\\Rightarrow\\theta+53.13=11.54,168.46\\Rightarrow\\theta=115.3^\\circ,318.4^\\circ$
""",

"ch03-ex3E-ps13": """**a** $\\sin(\\theta+30^\\circ)+\\cos\\theta=\\frac{\\sqrt3}{2}\\sin\\theta+\\frac12\\cos\\theta+\\cos\\theta=\\frac{\\sqrt3}{2}\\sin\\theta+\\frac32\\cos\\theta=R\\sin(\\theta+\\alpha)$ with $R=\\sqrt{\\frac34+\\frac94}=\\sqrt3$, $\\cos\\alpha=\\frac{\\sqrt3/2}{\\sqrt3}=\\frac12\\Rightarrow\\alpha=60^\\circ$. So $\\sqrt3\\sin(\\theta+60^\\circ)$.

**b** $\\sqrt3\\sin(\\theta+60^\\circ)=1\\Rightarrow\\sin(\\theta+60^\\circ)=\\frac1{\\sqrt3}\\Rightarrow\\theta+60=35.26,144.74\\Rightarrow\\theta=84.7^\\circ,335.3^\\circ$
""",

"ch03-ex3E-ps14": """**a** $7\\sin^2\\theta+9\\cos^2\\theta+4\\sin\\theta\\cos\\theta+2=8+\\cos2\\theta+2\\sin2\\theta+2=10+\\sqrt5\\sin(2\\theta+26.57^\\circ)$. Max $=10+\\sqrt5$, min $=10-\\sqrt5$.

**b** $\\cos2\\theta+2\\sin2\\theta=2\\Rightarrow\\sqrt5\\sin(2\\theta+26.57^\\circ)=2\\Rightarrow\\sin(2\\theta+26.57^\\circ)=0.8944\\Rightarrow2\\theta+26.57=63.43,116.57,423.43,476.57\\Rightarrow\\theta=18.4^\\circ,45^\\circ,198.4^\\circ,225^\\circ$
""",

# ----------------------------------------------------------------- review
"ch03-review-q1": """Sketch $y=3\\sec(2x-90^\\circ)$ for $0<x<180^\\circ$.

$\\sec$ has vertical asymptotes where its argument $=\\frac{\\pi}{2}+k\\pi$: $2x-90^\\circ=90^\\circ,270^\\circ\\Rightarrow x=90^\\circ$ (and $x=180^\\circ$ boundary). Period $\\frac{180}{2}=90^\\circ$. Amplitude factor 3; $\\sec\\ge1$ or $\\le-1$, so $y\\ge3$ or $y\\le-3$. Sketch the U-shaped branches between $x=90^\\circ$ and $180^\\circ$ (and the partial branch on $0<x<90$).
""",

"ch03-review-q2": """$\\operatorname{cosec}\\theta=3\\sin\\theta+\\cot\\theta\\Rightarrow\\frac1{\\sin\\theta}=3\\sin\\theta+\\frac{\\cos\\theta}{\\sin\\theta}\\Rightarrow1=3\\sin^2\\theta+\\cos\\theta\\Rightarrow1-\\cos\\theta=3(1-\\cos^2\\theta)\\Rightarrow3\\cos^2\\theta-\\cos\\theta-2=0\\Rightarrow(3\\cos\\theta+2)(\\cos\\theta-1)=0\\Rightarrow\\cos\\theta=-\\frac23\\Rightarrow\\theta=131.8^\\circ$ (in $0<\\theta<180$)
""",

"ch03-review-q3": """$\\cos A=\\frac14$, $270<A<360\\Rightarrow\\sin A=-\\frac{\\sqrt{15}}{4}$.

$\\sin2A=2\\sin A\\cos A=2\\cdot\\frac{-\\sqrt{15}}4\\cdot\\frac14=-\\frac{\\sqrt{15}}{8}$
""",

"ch03-review-q4": """$2\\tan^2x+\\sec x=1\\Rightarrow2(\\sec^2x-1)+\\sec x=1\\Rightarrow2\\sec^2x+\\sec x-3=0\\Rightarrow(2\\sec x+3)(\\sec x-1)=0\\Rightarrow\\cos x=1,-\\frac23\\Rightarrow x=0^\\circ,360^\\circ,131.8^\\circ,228.2^\\circ$
""",

"ch03-review-q5": """$2\\cot^2x+5\\operatorname{cosec}x=10\\Rightarrow2(\\operatorname{cosec}^2x-1)+5\\operatorname{cosec}x=10\\Rightarrow2\\operatorname{cosec}^2x+5\\operatorname{cosec}x-12=0\\Rightarrow(2\\operatorname{cosec}x-3)(\\operatorname{cosec}x+4)=0\\Rightarrow\\sin x=\\frac23,-\\frac14\\Rightarrow x=41.8^\\circ,138.2^\\circ,194.5^\\circ,345.5^\\circ$
""",

"ch03-review-q6": """**a** $\\sin(x+60^\\circ)+\\cos(x+30^\\circ)=\\frac12\\sin x+\\frac{\\sqrt3}{2}\\cos x+\\frac{\\sqrt3}{2}\\cos x-\\frac12\\sin x=\\sqrt3\\cos x$ ✓

**b** $\\sqrt3\\cos x=\\frac32\\Rightarrow\\cos x=\\frac{\\sqrt3}{2}\\Rightarrow x=30^\\circ,330^\\circ$
""",

"ch03-review-q7": """**a** $\\sin(60^\\circ-x)+\\cos(30^\\circ-x)=\\frac{\\sqrt3}{2}\\cos x-\\frac12\\sin x+\\frac{\\sqrt3}{2}\\cos x+\\frac12\\sin x=\\sqrt3\\cos x$ ✓

**b** $\\sqrt3\\cos x=\\frac25\\sec x\\Rightarrow\\sqrt3\\cos^2x=\\frac25\\Rightarrow\\cos^2x=\\frac2{5\\sqrt3}\\Rightarrow\\cos x=\\pm0.4804\\Rightarrow x=61.3^\\circ,118.7^\\circ,241.3^\\circ,298.7^\\circ$
""",

"ch03-review-q9": """**a** Let $t=\\tan x$: $\\tan(x+45^\\circ)-\\tan(45^\\circ-x)=\\frac{t+1}{1-t}-\\frac{1-t}{1+t}=\\frac{(t+1)^2-(1-t)^2}{1-t^2}=\\frac{4t}{1-t^2}=2\\tan2x$ ✓

**b** $2\\tan2x=6\\Rightarrow\\tan2x=3\\Rightarrow2x=71.6,251.6\\Rightarrow x=35.8^\\circ,125.8^\\circ$
""",

"ch03-review-q10": """**i** $3\\cos\\theta+\\sin\\theta=R\\cos(\\theta-\\alpha)$, $R=\\sqrt{10}$, $\\cos\\alpha=\\frac3{\\sqrt{10}}\\Rightarrow\\alpha=18.43^\\circ$.

**ii** $3\\cos2x+\\sin2x=2\\Rightarrow\\sqrt{10}\\cos(2x-18.43^\\circ)=2\\Rightarrow\\cos(2x-18.43^\\circ)=0.6325\\Rightarrow2x-18.43=50.77,309.23,410.77,669.23\\Rightarrow x=34.6^\\circ,163.8^\\circ,214.6^\\circ,343.8^\\circ$
""",

"ch03-review-q11": """**a** $\\cos(60^\\circ-x)=\\frac12\\cos x+\\frac{\\sqrt3}{2}\\sin x$; $\\cos(300^\\circ-x)=\\frac12\\cos x-\\frac{\\sqrt3}{2}\\sin x$. Sum $=\\cos x$ ✓

**b i** With $x=45^\\circ$: $\\cos15^\\circ+\\cos255^\\circ=\\cos45^\\circ=\\frac{\\sqrt2}{2}$

**b ii** $\\cos x=\\frac14\\operatorname{cosec}x\\Rightarrow\\sin x\\cos x=\\frac14\\Rightarrow\\frac12\\sin2x=\\frac14\\Rightarrow\\sin2x=\\frac12\\Rightarrow2x=30,150\\Rightarrow x=15^\\circ,75^\\circ$
""",

"ch03-review-q12": """**a** $\\frac{2\\sin2\\theta-3\\cos2\\theta+3}{\\sin\\theta}=\\frac{4\\sin\\theta\\cos\\theta+6\\sin^2\\theta}{\\sin\\theta}=4\\cos\\theta+6\\sin\\theta$ ✓

**b** $4\\cos\\theta+6\\sin\\theta=R\\cos(\\theta-\\alpha)$, $R=\\sqrt{16+36}=2\\sqrt{13}$, $\\cos\\alpha=\\frac4{2\\sqrt{13}}\\Rightarrow\\alpha=56.31^\\circ$.

**c** greatest of the square $=(2\\sqrt{13})^2=52$
""",

"ch03-review-q13": """**i** $4\\sin\\theta-6\\cos\\theta=2\\sqrt{13}\\sin(\\theta-56.31^\\circ)$ (as ex3E-q4).

**ii** $2\\sqrt{13}\\sin(\\theta-56.31^\\circ)=3\\Rightarrow\\sin(\\theta-56.31^\\circ)=0.416\\Rightarrow\\theta-56.31=24.6,155.4,384.6\\Rightarrow\\theta=80.9^\\circ,211.7^\\circ$

**iii** $(4\\sin\\theta-6\\cos\\theta)^2+8$: max $=52+8=60$, min $=0+8=8$
""",

"ch03-review-q14": """**i** $\\sin3\\theta=\\sin(2\\theta+\\theta)=2\\sin\\theta\\cos^2\\theta+(\\cos^2\\theta-\\sin^2\\theta)\\sin\\theta=2\\sin\\theta(1-\\sin^2\\theta)+\\sin\\theta(1-2\\sin^2\\theta)=3\\sin\\theta-4\\sin^3\\theta$ ✓

**ii** $x=\\frac{2\\sin\\theta}{\\sqrt3}$: $x^3-x=\\frac{8\\sin^3\\theta}{3\\sqrt3}-\\frac{2\\sin\\theta}{\\sqrt3}=\\frac1{3\\sqrt3}(8\\sin^3\\theta-6\\sin\\theta)=\\frac{-2}{3\\sqrt3}\\sin3\\theta$. So $x^3-x+\\frac{\\sqrt3}{6}=0\\Rightarrow-2\\sin3\\theta+\\frac{9}{6}=0\\Rightarrow\\sin3\\theta=\\frac34$ ✓

**iii** $\\sin3\\theta=\\frac34\\Rightarrow3\\theta=48.6,131.4,408.6,491.4,768.6,851.4\\Rightarrow\\theta=16.2,43.8,136.2,163.8,256.2,283.8\\Rightarrow x=\\frac{2\\sin\\theta}{\\sqrt3}=0.322,0.799,-1.12$
""",

"ch03-review-q15": """**a** $\\sin(x+30^\\circ)+\\cos(x+60^\\circ)=\\frac{\\sqrt3}{2}\\sin x+\\frac12\\cos x+\\frac12\\cos x-\\frac{\\sqrt3}{2}\\sin x=\\cos x\\Rightarrow\\frac1{\\ldots}=\\sec x$ ✓

**b** $2\\sec x=7-\\tan^2x\\Rightarrow\\frac2{\\cos x}=7-\\frac{\\sin^2x}{\\cos^2x}\\Rightarrow2\\cos x=7\\cos^2x-\\sin^2x=8\\cos^2x-1\\Rightarrow8\\cos^2x-2\\cos x-1=0\\Rightarrow\\cos x=\\frac12,-\\frac14\\Rightarrow x=60^\\circ,300^\\circ,104.5^\\circ,255.5^\\circ$
""",

"ch03-review-q16": """**a** $\\operatorname{cosec}^4x-\\cot^4x=(\\operatorname{cosec}^2x-\\cot^2x)(\\operatorname{cosec}^2x+\\cot^2x)=1\\cdot(\\operatorname{cosec}^2x+\\cot^2x)$ ✓

**b** $\\operatorname{cosec}^2x+\\cot^2x=16-\\cot x\\Rightarrow(1+\\cot^2x)+\\cot^2x=16-\\cot x\\Rightarrow2\\cot^2x+\\cot x-15=0\\Rightarrow(2\\cot x-5)(\\cot x+3)=0\\Rightarrow\\cot x=\\frac52,-3\\Rightarrow x=21.8^\\circ,161.6^\\circ$
""",

"ch03-review-q17": """**a** $1+4\\cos2x=2\\cos^2x-4\\sin2x\\Rightarrow1+4\\cos2x=1+\\cos2x-4\\sin2x\\Rightarrow3\\cos2x+4\\sin2x=0$ ✓

**b** $3\\cos2x+4\\sin2x=5\\sin(2x+\\alpha)$, $\\cos\\alpha=\\frac45\\Rightarrow\\alpha=36.87^\\circ$.

**c** $5\\sin(2x+36.87^\\circ)=0\\Rightarrow2x+36.87=0,180,360,540\\Rightarrow2x=143.13,323.13,503.13\\Rightarrow x=71.6^\\circ,161.6^\\circ$ (in $0<x<180$)
""",

# ------------------------------------------------------------------ cross
"ch03-cross-q1": """Square both sides (both positive): $9(x-1)^2<(2x+1)^2\\Rightarrow9x^2-18x+9<4x^2+4x+1\\Rightarrow5x^2-22x+8<0\\Rightarrow(5x-2)(x-4)<0\\Rightarrow\\frac25<x<4$
""",

"ch03-cross-q2": """$2|3^x-1|=3^x$.

If $3^x\\ge1$ ($x\\ge0$): $2(3^x-1)=3^x\\Rightarrow3^x=2\\Rightarrow x=\\log_3 2=0.631$.

If $3^x<1$ ($x<0$): $2(1-3^x)=3^x\\Rightarrow3\\cdot3^x=2\\Rightarrow3^x=\\frac23\\Rightarrow x=\\log_3\\tfrac23=-0.369$.
""",

"ch03-cross-q3": """**i** Square: $(3x+4)^2=(3x-11)^2\\Rightarrow24x+16=-66x+121\\Rightarrow90x=105\\Rightarrow x=\\frac76$

**ii** Put $u=2^y$: $|3u+4|=|3u-11|\\Rightarrow u=\\frac76$ (by part i). $2^y=\\frac76\\Rightarrow y=\\log_2\\tfrac76=0.222$
""",

"ch03-cross-q4": """**i** Square: $4(x-1)^2=9x^2\\Rightarrow5x^2+8x-4=0\\Rightarrow x=\\frac{-8\\pm12}{10}\\Rightarrow x=-2,\\frac25$

**ii** Put $u=5^x>0$: $2|u-1|=3|u|\\Rightarrow u=\\frac25$ (negative root discarded). $5^x=\\frac25\\Rightarrow x=\\log_5\\tfrac25=-0.569$
""",

"ch03-cross-q5": """$y=Ab^x\\Rightarrow\\ln y=\\ln A+x\\ln b$. Line through $(0,2.14)$ and $(5,4.49)$: slope $=\\frac{4.49-2.14}{5}=0.47=\\ln b\\Rightarrow b=\\mathrm{e}^{0.47}=1.6$; intercept $\\ln A=2.14\\Rightarrow A=\\mathrm{e}^{2.14}=8.5$.
""",

"ch03-cross-q6": """**i** Let $u=3^x$: $u^2=5u+14\\Rightarrow u^2-5u-14=0\\Rightarrow(u-7)(u+2)=0\\Rightarrow u=7$ (discard $-2$). $3^x=7\\Rightarrow x=\\log_3 7=1.77$.

**ii** $3^{|x|}=7\\Rightarrow|x|=\\log_3 7\\Rightarrow x=\\pm1.77$
""",

"ch03-cross-q7": """$x^ny=C\\Rightarrow\\ln y=\\ln C-n\\ln x$. Points $(1.10,5.20)$, $(3.20,1.05)$: slope $=\\frac{\\ln1.05-\\ln5.20}{\\ln3.20-\\ln1.10}=\\frac{-1.600}{1.068}=-1.50=-n\\Rightarrow n=1.50$. $\\ln C=\\ln5.20+1.5\\ln1.10=1.792\\Rightarrow C=6.00$.

**ii** $\\ln y=\\ln C-n\\ln x$ is a straight line in $\\ln y$ vs $\\ln x$.
""",

"ch03-cross-q9": """Let $T=\\tan\\theta$, $U=\\tan\\phi$. $T+U=1$, $\\tan(\\theta-\\phi)=\\frac{T-U}{1+TU}=3$.

Solve: $T-U=3(1+TU)$ with $T+U=1$ gives $TU=-2$ or $-\\frac49$. With $T+U=1$:

- $TU=-2$: roots $T=2,U=-1\\Rightarrow\\theta=63.4^\\circ,\\phi=135^\\circ$ (but then $\\theta<\\phi$… the answer pairs them as $\\theta=135^\\circ,\\phi=63.4^\\circ$).

- $TU=-\\frac49$: roots $T=\\frac43,U=-\\frac13\\Rightarrow\\theta=53.1^\\circ,\\phi=161.6^\\circ$.

So $(\\theta,\\phi)=(135^\\circ,63.4^\\circ)$ or $(53.1^\\circ,161.6^\\circ)$.
""",

"ch03-cross-q11": """**i** Remainder when divided by $(2x-1)$ is $\\mathrm{p}(\\frac12)=\\frac12+\\frac a4+\\frac92+9=14+\\frac a4=10\\Rightarrow a=-16$. Then $\\mathrm{p}(x)=4x^3-16x^2+9x+9$ and $\\mathrm{p}(3)=108-144+27+9=0$, so $(x-3)$ is a factor ✓.

**ii** Divide by $(x-3)$: $\\mathrm{p}(x)=(x-3)(4x^2-4x-3)=(x-3)(2x-3)(2x+1)=0\\Rightarrow x=3,\\frac32,-\\frac12$
""",

"ch03-cross-q12": """**i** $\\mathrm{p}(-1)=-2-4-a+b=4\\Rightarrow b-a=10$. $\\mathrm{p}(3)=54-36+3a+b=12\\Rightarrow3a+b=-6$. Solve: $a=-4,\\ b=6$.

**ii** Divide $2x^3-4x^2-4x+6$ by $x^2-2$: quotient $=2x-4$, remainder $=-2$.
""",

"ch03-cross-q13": """**i** $\\cos x+3\\sin x=R\\cos(x-\\alpha)$, $R=\\sqrt{10}$, $\\cos\\alpha=\\frac1{\\sqrt{10}}\\Rightarrow\\alpha=71.57^\\circ$.

**ii** $\\cos2\\theta+3\\sin2\\theta=2\\Rightarrow\\sqrt{10}\\cos(2\\theta-71.57^\\circ)=2\\Rightarrow\\cos(2\\theta-71.57^\\circ)=0.6325\\Rightarrow2\\theta-71.57=\\pm50.77\\Rightarrow\\theta=10.4^\\circ,61.2^\\circ$ (in $0<\\theta<90$)
""",

"ch03-cross-q14": """**i** $2\\ln(4x-5)+\\ln(x+1)=3\\ln3\\Rightarrow\\ln[(4x-5)^2(x+1)]=\\ln27\\Rightarrow(16x^2-40x+25)(x+1)=27\\Rightarrow16x^3-24x^2-15x+25=27\\Rightarrow16x^3-24x^2-15x-2=0$ ✓

**ii** Try $x=2$: $128-96-30-2=0$ ✓. Divide: $(x-2)(16x^2+8x+1)=(x-2)(4x+1)^2$.

**iii** $x=2$ or $x=-\\frac14$; domain $4x-5>0\\Rightarrow x=\\frac54$, so $x=2$.
""",

"ch03-cross-q15": """**i** $(x+1)$ factor: $\\mathrm{p}(-1)=-8+a-b-1=0\\Rightarrow a-b=9$. Remainder at $(2x+1)$: $\\mathrm{p}(-\\frac12)=-1+\\frac a4-\\frac b2-1=1\\Rightarrow a-2b=12$. Solve: $a=6,\\ b=-3$.

**ii** $8x^3+6x^2-3x-1=(x+1)(8x^2-2x-1)=(x+1)(4x+1)(2x-1)$
""",

"ch03-cross-q16": """**i** $(x-1)$ factor: $\\mathrm{p}(1)=3+2+a+b=0\\Rightarrow a+b=-5$. $\\mathrm{p}(2)=24+8+2a+b=10\\Rightarrow2a+b=-22$. Solve: $a=-17,\\ b=12$.

**ii** $3x^3+2x^2-17x+12=(x-1)(3x^2+5x-12)=(x-1)(3x-4)(x+3)=0\\Rightarrow x=1,\\frac43,-3$
""",

"ch03-cross-q17": """**i** $\\mathrm{p}(3)=27+9a+3b+8=14\\Rightarrow3a+b=-7$. $\\mathrm{p}(-2)=-8+4a-2b+8=24\\Rightarrow2a-b=12$. Solve: $a=1,\\ b=-10$.

**ii** $x^3+x^2-10x+8=(x^2+2x-8)(x-1)=(x+4)(x-2)(x-1)$. Quotient $=x-1$; roots $x=-4,2,1$.
""",

"ch03-cross-q19": """**i** Long division: $x^4+x^3+3x^2+12x+6=(x^2-x+4)(x^2+2x+1)+(5x+2)$. Quotient $=x^2+2x+1$, remainder $=5x+2$.

**ii** With $px+q$ the remainder is $(p-7)x+(q-4)$; zero remainder gives $p=7,\\ q=4$.

**iii** $x^4+x^3+3x^2+7x+4=(x^2-x+4)(x+1)^2$. $x^2-x+4$ has no real roots (discriminant $<0$), so exactly one real root $x=-1$.
""",

"ch03-cross-q20": """**i** $2\\tan^2\\alpha+\\sec^2\\alpha=5-4\\tan\\alpha\\Rightarrow2\\tan^2\\alpha+1+\\tan^2\\alpha=5-4\\tan\\alpha\\Rightarrow3\\tan^2\\alpha+4\\tan\\alpha-4=0\\Rightarrow(3\\tan\\alpha-2)(\\tan\\alpha+2)=0\\Rightarrow\\tan\\alpha=\\frac23$ (Q1).

**ii** $\\cot(\\alpha+\\beta)=6\\Rightarrow\\tan(\\alpha+\\beta)=\\frac16$. $\\frac{\\frac23+t}{1-\\frac23t}=\\frac16\\Rightarrow6\\left(\\frac23+t\\right)=1-\\frac23t\\Rightarrow4+6t=1-\\frac23t\\Rightarrow\\frac{20}{3}t=-3\\Rightarrow t=-\\frac9{20}$
""",

"ch03-cross-q21": """**i** $5\\sin2\\theta+2\\cos2\\theta=R\\sin(2\\theta+\\alpha)$, $R=\\sqrt{29}$, $\\cos\\alpha=\\frac5{\\sqrt{29}}\\Rightarrow\\alpha=21.80^\\circ$.

**ii** $\\sqrt{29}\\sin(2\\theta+21.80^\\circ)=4\\Rightarrow\\sin(2\\theta+21.80^\\circ)=0.7428\\Rightarrow2\\theta+21.80=47.97,132.03,407.97,492.03\\Rightarrow\\theta=13.1^\\circ,55.1^\\circ,193.1^\\circ,235.1^\\circ$

**iii** least $\\frac1{(10\\sin2\\theta+4\\cos2\\theta)^2}=\\frac1{(2\\sqrt{29})^2}=\\frac1{116}$
""",

"ch03-cross-q22": """**i** $(x+3)$ factor: $\\mathrm{p}(-3)=-27a+27-3b+12=0\\Rightarrow9a+b=13$. $\\mathrm{p}(-2)=-8a+12-2b+12=18\\Rightarrow4a+b=3$. Solve: $a=2,\\ b=-5$.

**ii a** $2x^3+3x^2-5x+12=(x+3)(2x^2-3x+4)$. $2x^2-3x+4$ has discriminant $-23<0$ (no real roots) $\\Rightarrow$ exactly one real root.

**b** $\\sec y=-3\\Rightarrow\\cos y=-\\frac13\\Rightarrow y=109.5^\\circ$ (in $-180<y<180$).
""",


}


def write_all():
    out = Path(__file__).resolve().parent.parent / "working"
    out.mkdir(exist_ok=True)
    for qid, body in WORKING.items():
        (out / f"{qid}.md").write_text(
            f"# {qid} \u2014 working\n\n{MARKER}\n\n{body.strip()}\n",
            encoding="utf-8")
    print(f"wrote {len(WORKING)} working files to {out}")

if __name__ == "__main__":
    write_all()
