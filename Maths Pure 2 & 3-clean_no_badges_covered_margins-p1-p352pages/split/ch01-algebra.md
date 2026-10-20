# Chapter 1: Algebra

In this chapter you will learn how to:

- understand the meaning of $|x|$, sketch the graph of $y=|a x+b|$ and use relations such as $|a|=|b| \Leftrightarrow a^{2}=b^{2}$ and $|x-a|<b \Leftrightarrow a-b<x<a+b$ in the course of solving equations and inequalities

- divide a polynomial, of degree not exceeding 4, by a linear or quadratic polynomial, and identify the quotient and remainder (which may be zero)

- use the factor theorem and the remainder theorem.

![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-001_647_1943_2125_137.jpg)

<a id="ch01-prerequisite"></a>
### PREREQUISITE KNOWLEDGE

| Where it comes from | What you should be able to do | Check your skills |
| :--- | :--- | :--- |
| IGCSE $^{\circledR}$ / O Level Mathematics | Perform long division on numbers and find the remainder where necessary. | 1 Using long division, calculate:<br>&#160;&#160;a $4998 \div 14$<br>&#160;&#160;b $10287 \div 27$<br>&#160;&#160;c $4283 \div 32$<br> |
| IGCSE / O Level Mathematics | Sketch straight-line graphs. | 2 Sketch the graph of $y=2 x-5$. |

Why do we need to study algebra?

You have previously learnt the general formula, $x=\frac{-b \pm \sqrt{b^{2}-4 a c}}{2 a}$, for solving quadratic equations. Versions of this formula were known and used by the Babylonians nearly 4000 years ago.

It took until the 16th century for mathematicians to discover formulae for solving cubic equations, $a x^{3}+b x^{2}+c x+d=0$, and quartic equations, $a x^{4}+b x^{3}+c x^{2}+d x+e=0$. (These formulae are very complicated and there is insufficient space to include them here but you might wish to research them on the internet.)

Mathematicians then spent many years trying to discover a general formula for solving quintic equations, $a x^{5}+b x^{4}+c x^{3}+d x^{2}+e x+f=0$. Eventually, in 1824, a mathematician managed to prove that no general formula for this exists.

In this chapter you will develop skills for factorising and solving cubic and quartic equations. These types of equations have various applications in the real world. For example, cubic equations are used in thermodynamics and fluid mechanics to model the pressure/volume/temperature behaviour of gases and fluids.

You will also learn about a new type of function, called the modulus function.

## 1.1 The modulus function

The modulus of a number is the magnitude of the number without a sign attached.

The modulus of 3 is written $|3|$.

$$
|3|=3 \text { and }|-3|=3
$$

It is important to note that the modulus of any number (positive or negative) is always a positive number.

The modulus of a number is also called the absolute value.

The modulus of $x$, written as $|x|$, is defined as:

$$
|x|=\left\{\begin{array}{rll} x & \text { if } & x \geqslant 0 \\
-x & \text { if } & x<0 \end{array}\right.
$$

#### EXPLORE 1.1

You are given these eight statements:

$1|a+b|=|a|+|b|$

$2|a-b|=|a|-|b|$

$3|a b|=|a| \times|b|$

$4\left|\frac{a}{b}\right|=|a| \div|b|$, if $b \neq 0$

$5\left||a|^{2}=a^{2}\right.$

$6|a|^{n}=a^{n}$, where $n$ is a positive integer

$7|a+b| \leqslant|a|+|b|$

$8|a-b| \leqslant|a-c|+|c-b|$

You must decide whether a statement is

- If you think that a statement is either always true or never true, you must give a clear explanation to justify your answer.

- If you think that a statement is sometimes true you must give an example of when it is true and an example of when it is not true.

The statement $|x|=k$, where $k \geqslant 0$, means that $x=k$ or $x=-k$.

This property is used to solve equations that involve modulus functions.

If you are solving equations of the form $|a x+b|=k$, you can solve the equations using

$$
a x+b=k \quad \text { and } \quad a x+b=-k
$$

If you are solving harder equations of the form $|a x+b|=c x+d$, you can solve the equations using

$$
a x+b=c x+d \quad \text { and } \quad a x+b=-(c x+d)
$$

When solving these more complicated equations you must always check that your answers satisfy the original equation.

<a id="ch01-we-1.1"></a>
#### WORKED EXAMPLE 1.1

Solve:

**a** $|2 x-1|=3$

**b** $|x-4|=2 x+1$

Answer

**a**

$$
\begin{array}{rlrlrl} |2 x-1| & =3 & & & \\
2 x-1 & =3 & \text { or } & 2 x-1 & =-3 \\
2 x & =4 & & 2 x & =-2 \\
x & =2 & x & =-1 \end{array}
$$

CHECK: $|2 \times 2-1|=3 \checkmark$ and $|2 \times(-1)-1|=3 \checkmark$ The solution is: $x=-1$ or $x=2$

**b**

$$
\begin{align}
|x-4| & =2 x+1 & & \\
x-4 & =2 x+1 & \text { or } & x-4 \\
x & =-5 & & 3 x \\
& & x & =1
\end{align}
$$

CHECK: $|-5-4|=2 \times(-5)+1 \times$ and $|1-4|=2 \times 1+1 \checkmark$ The solution is: $x=1$

#### EXPLORE 1.2

Using $|a|^{2}=a^{2}$ you can write $a^{2}-b^{2}$ as $|a|^{2}-|b|^{2}$.

Using the difference of two squares you can now write:

$$
a^{2}-b^{2}=(|a|-|b|)(|a|+|b|)
$$

Using the previous statement, explain how these three important results can be obtained:

(The symbol ⇔ means 'is equivalent to'.)

- $|a|=|b| \Leftrightarrow a^{2}=b^{2}$

- $|a|>|b| \Leftrightarrow a^{2}>b^{2}$

- $|a|<|b| \Leftrightarrow a^{2}<b^{2}$, if $b \neq 0$.

Worked example 1.2 shows you how to solve equations of the form $|c x+d|=|e x+f|$.

<a id="ch01-kp-1.1"></a>
#### KEY POINT 1.1

To solve equations of the form $|c x+d|=|e x+f|$ we can use the rule:

$$
|a|=|b| \Leftrightarrow a^{2}=b^{2}
$$

<a id="ch01-we-1.2"></a>
#### WORKED EXAMPLE 1.2

Solve the equation $|3 x+4|=|x+5|$.

Answer

Method 1

$$
|3 x+4|=|x+5|
$$

$$
\begin{array}{rlrlrl} 3 x+4 & =x+5 & & \text { or } & 3 x+4 & =-(x+5) \\
2 x & =1 & \text { or } & 4 x & =-9 \\
x & =\frac{1}{2} & & x & =-\frac{9}{4} \end{array}
$$

CHECK: $\left|3 \times \frac{1}{2}+4\right|=\left|\frac{1}{2}+5\right| \quad \checkmark,\left|3 \times\left(-\frac{9}{4}\right)+4\right|=\left|-\frac{9}{4}+5\right| \quad \checkmark$ Solution is: $x=\frac{1}{2}$ or $x=-\frac{9}{4}$ Method 2

$$
\begin{align}
|3 x+4| & =|x+5| \\
(3 x+4)^{2} & =(x+5)^{2}
\end{align}
$$

$$
\begin{align}
9 x^{2}+24 x+16 & =x^{2}+10 x+25 \\
8 x^{2}+14 x-9 & =0
\end{align}
$$

$$
\begin{align}
(2 x-1)(4 x+9) & =0 \\
x=\frac{1}{2} \quad \text { or } \quad & x=-\frac{9}{4}
\end{align}
$$

<a id="ch01-we-1.3"></a>
#### WORKED EXAMPLE 1.3

Solve $|x+3|+|x+5|=10$.

Answer

$$
|x+3|+|x+5|=10 \quad \text { Subtract }|x+5| \text { from both sides. }
$$

$$
\begin{align}
|x+3| & =10-|x+5| \\
x+3 & =10-|x+5|--------- \text { (1) } \tag{1} \\
x+3 & =|x+5|-10 \qquad \text { Split the equation into two parts. } \tag{2}
\end{align}
$$

Using equation (1):

$$
\begin{align}
-7+x+|x+5| & =0 \\
|x+5| & =7-x
\end{align}
$$

$$
\begin{array}{rlrlrlrl} x+5 & =7-x & & \text { or } & & x+5 & =-(7-x) \\
2 x & =2 & \text { or } & 0 & =-12 & & & \\
x & =1 & & & & & & \\
2 x & & & & & & =-12 \text { is false. } \end{array}
$$

Using equation (2):

$$
\begin{align}
|x+5| & =x+13 \\
x+5 & =x+13 \text { or } x+5=-(x+13)
\end{align}
$$

$$
\begin{align}
0=8 \quad \text { or } \quad 2 x & =-18 \\
x & =-9
\end{align}
$$

The solution is $x=1$ or $x=-9$.

<a id="ch01-ex1A"></a>
### EXERCISE 1A

<a id="ch01-ex1A-q1"></a>
##### Question 1
Solve.

**a** $|4 x-3|=7$

**b** $|1-2 x|=5$

**c** $\left|\frac{3 x-2}{5}\right|=4$

**d** $\left|\frac{x}{3}+2\right|=3$

**e** $\left|\frac{x+2}{3}-\frac{2 x}{5}\right|=2$

**f** $|2 x+7|=3 x$

<a id="ch01-ex1A-q2"></a>
##### Question 2
Solve.

**a** $\left|\frac{2 x+1}{x-2}\right|=5$

**b** $\left|\frac{3 x-1}{x+5}\right|=1$

**c** $\left|2-\frac{x+2}{x-3}\right|=5$

**d** $|3 x-5|=x+1$

**e** $x+|x+4|=8$

**f** $8-|1-2 x|=x$

<a id="ch01-ex1A-q3"></a>
##### Question 3
Solve.

**a** $|2 x+1|=|x|$

**b** $|3-2 x|=|3 x|$

**c** $|2 x-5|=|1-x|$

**d** $|3 x+5|=|1+2 x|$

**e** $|x-5|=2|x+1|$

**f** $3|2 x-1|=\left|\frac{1}{2} x-3\right|$

<a id="ch01-ex1A-q4"></a>
##### Question 4
Solve.

**a** $\left|x^{2}-2\right|=7$

**b** $\left|5-x^{2}\right|=3-x$

**c** $\left|x^{2}+2 x\right|=x+2$

**d** $\left|x^{2}-3\right|=2 x+1$

**e** $\left|2 x^{2}-5 x\right|=4-x$

**f** $\left|x^{2}-7 x+6\right|=6-x$

<a id="ch01-ex1A-q5"></a>
##### Question 5
Solve the simultaneous equations.

**a**

$$
\begin{align}
& x+2 y=8 \\
& |x+2|+y=6
\end{align}
$$

**b**

$$
\begin{align}
& 3 x+y=0 \\
& y=\left|2 x^{2}-5\right|
\end{align}
$$

<a id="ch01-ex1A-q6"></a>
##### Question 6
Solve the equation $5|x-1|^{2}+9|x-1|-2=0$.

<a id="ch01-ex1A-q7"></a>
##### Question 7
**a** Solve the equation $x^{2}-5|x|+6=0$.

**b** Use graphing software to draw the graph of $y=x^{2}-5|x|+6$.

**c** Name the equation of the line of symmetry of the curve.

<a id="ch01-ex1A-q8"></a>
##### Question 8
Solve the equation $|2 x+1|+|2 x-1|=3$.

<a id="ch01-ex1A-q9"></a>
##### Question 9
Solve the equation $|3 x-2 y-11|+2 \sqrt{31-8 x+5 y}=0$.

## 1.2 Graphs of $\boldsymbol{y}=|\mathbf{f}(\boldsymbol{x})|$ where $\mathbf{f}(\boldsymbol{x})$ is linear

Consider drawing the graph of $y=|x|$.

First draw the line $y=x$.

Then reflect, in the $x$-axis, the part of the line that is below the $x$-axis.

![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-007_340_412_277_1624.jpg)

<a id="ch01-we-1.4"></a>
#### WORKED EXAMPLE 1.4

Sketch the graph of $y=\left|\frac{1}{2} x-1\right|$, showing the points where the graph meets the axes.

Use your graph to express $\left|\frac{1}{2} x-1\right|$ in an alternative form.

Answer

First sketch the graph of $y=\frac{1}{2} x-1$.

The line has gradient $\frac{1}{2}$ and

**a** $y$-intercept of -1 .

You then reflect in the $x$-axis the part of the line that is below the $x$-axis.

The graph shows that $\left|\frac{1}{2} x-1\right|$ can be written as:

$$
\left|\frac{1}{2} x-1\right|= \begin{cases}\frac{1}{2} x-1 & \text { if } x \geqslant 2 \\
-\left(\frac{1}{2} x-1\right) & \text { if } x<2\end{cases}
$$

![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-007_452_516_1036_1483.jpg)

In Worked example 1.1, we found that there were two roots, $x=-1$ and $x=2$, to the equation $|2 x-1|=3$.

These can also be found graphically by finding the $x$-coordinates of the points of intersection of the graphs of $y=|2 x-1|$ and $y=3$ as shown.

![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-007_388_411_1573_1619.jpg)

Also in Worked example 1.1, we found that there was only one root, $x=1$, to the equation $|x-4|=2 x+1$.

This root can be found graphically by finding the $x$-coordinates of the points of intersection of the graphs of $y=|x-4|$ and $y=2 x+1$ as shown.

![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-007_514_787_2024_1243.jpg)

<a id="ch01-ex1B"></a>
### EXERCISE 1B

<a id="ch01-ex1B-q1"></a>
##### Question 1
Sketch the graphs of each of the following functions showing the coordinates of the points where the graph meets the axes. Express each function in an alternative form.

**a** $y=|x+2|$

**b** $y=|3-x|$

**c** $y=\left|5-\frac{1}{2} x\right|$

<a id="ch01-ex1B-q2"></a>
##### Question 2
**a** Complete the table of values for $y=|x-3|+2$.

| $x$ | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| $y$ | 5 |  | 3 |  |  |  |  |

**b** Draw the graph of $y=|x-3|+2$ for $0 \leqslant x \leqslant 6$.

**c** Describe the transformation that maps the graph of $y=|x|$ onto the graph of $y=|x-3|+2$.

<a id="ch01-ex1B-q3"></a>
##### Question 3
Describe fully the transformation (or combination of transformations) that maps the graph of $y=|x|$ onto each of these functions.

**a** $y=|x+1|+2$

**b** $y=|x-5|-2$

**c** $y=2-|x|$

**d** $y=|2 x|-3$

**e** $y=1-|x+2|$

**f** $y=5-2|x|$

<a id="ch01-ex1B-q4"></a>
##### Question 4
Sketch the graphs of each of the functions in question 3. For each graph, state the coordinates of the vertex.

<a id="ch01-ex1B-q5"></a>
##### Question 5
$ \mathrm{f}(x)=|5-2 x|+3$ for $2 \leqslant x \leqslant 8$

Find the range of function f.

<a id="ch01-ex1B-q6"></a>
##### Question 6
**a** Sketch the graph of $y=2|x-2|+1$ for $-2<x<6$, showing the coordinates of the vertex and the $y$-intercept.

**b** On the same diagram, sketch the graph of $y=x+2$.

**c** Use your graph to solve the equation $2|x-2|+1=x+2$.

<a id="ch01-ex1B-q7"></a>
##### Question 7
**a** Sketch the graph of $y=|x-2|$ for $-3<x<6$, showing the coordinates of the vertex and the $y$-intercept.

**b** On the same diagram, sketch the graph of $y=|1-2 x|$.

**c** Use your graph to solve the equation $|x-2|=|1-2 x|$.

<a id="ch01-ex1B-q8"></a>
##### Question 8
**a** Sketch the graph of $y=|x+1|+|x-1|$.

**b** Use your graph to solve the equation $|x+1|+|x-1|=4$.

## 1.3 Solving modulus inequalities

Two useful properties that can be used when solving modulus inequalities are:

$$
|a| \leqslant b \Leftrightarrow-b \leqslant a \leqslant b \quad \text { and } \quad|a| \geqslant b \Leftrightarrow a \leqslant-b \quad \text { or } \quad a \geqslant b
$$

The following examples illustrate the different methods that can be used when solving modulus inequalities.

<a id="ch01-we-1.5"></a>
#### WORKED EXAMPLE 1.5

Solve $|2 x-5|<3$.

Answer

Method 1: Using algebra

$$
\begin{array}{r} |2 x-5|<3 \\
-3<2 x-5<3 \\
2<2 x<8 \\
1<x<4 \end{array}
$$

Method 2: Using a graph

The graphs of $y=|2 x-5|$ and $y=3$ intersect at the points $A$ and $B$.

$$
|2 x-5|=\left\{\begin{array}{cl} 2 x-5 & \text { if } x \geqslant 2 \frac{1}{2} \\
-(2 x-5) & \text { if } x<2 \frac{1}{2} \end{array}\right.
$$

At $A$, the line $y=-(2 x-5)$ intersects the line $y=3$.

$$
\begin{align}
-(2 x-5) & =3 \\
-2 x+5 & =3 \\
2 x & =2 \\
x & =1
\end{align}
$$

![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-009_448_462_845_1550.jpg)

At $B$, the line $y=2 x-5$ intersects the line $y=3$.

$$
\begin{array}{r} 2 x-5=3 \\
2 x=8 \\
x=4 \end{array}
$$

To solve the inequality $|2 x-5|<3$ you must find where the graph of the function $y=|2 x-5|$ is below the graph of $y=3$.

Hence, $1<x<4$.

<a id="ch01-we-1.6"></a>
#### WORKED EXAMPLE 1.6

Solve the inequality $|2 x-1| \geqslant|3-x|$.

Answer

Method 1: Using algebra

$$
\begin{align}
|2 x-1| & \geqslant|3-x| \\
(2 x-1)^{2} & \geqslant(3-x)^{2} \\
4 x^{2}-4 x+1 & \geqslant 9-6 x+x^{2} \\
3 x^{2}+2 x-8 & \geqslant 0
\end{align}
$$

$$
(3 x-4)(x+2) \geqslant 0
$$

$$
y=3 x^{2}+2 x-8
$$

Critical values are -2 and $\frac{4}{3}$.

Hence, $x \leqslant-2$ or $x \geqslant \frac{4}{3}$.

![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-010_214_393_315_1208.jpg)

Method 2: Using a graph

The graphs of $y=|2 x-1|$ and $y=|3-x|$ intersect at the points $A$ and $B$.

$$
\begin{align}
& |2 x-1|=\left\{\begin{array}{l} 2 x-1 \quad \text { if } x \geqslant \frac{1}{2} \\
-(2 x-1) \text { if } x<\frac{1}{2} \end{array}\right. \\
& |3-x|=|x-3|= \begin{cases}x-3 & \text { if } x \geqslant 3 \\
-(x-3) & \text { if } x<3\end{cases}
\end{align}
$$

At $A$, the line $y=-(2 x-1)$ intersects the line $y=-(x-3)$.

$$
\begin{align}
2 x-1 & =x-3 \\
x & =-2
\end{align}
$$

At $B$, the line $y=2 x-1$ intersects the line $y=-(x-3)$.

$$
\begin{align}
2 x-1 & =-(x-3) \\
3 x & =4 \\
x & =\frac{4}{3}
\end{align}
$$

To solve the inequality $|2 x-1| \geqslant|3-x|$ you must find where the graph of the function $y=|2 x-1|$ is above the graph of $y=|3-x|$.

Hence, $x \leqslant-2$ or $x \geqslant \frac{4}{3}$.

![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-010_632_780_1041_1174.jpg)

<a id="ch01-ex1C"></a>
### EXERCISE 1C

<a id="ch01-ex1C-q1"></a>
##### Question 1
![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-010_502_651_1879_331.jpg) The graphs of $y=|x-1|$ and $y=2|x-4|$ are shown on the grid.

Write down the solution to the inequality $|x-1|>2|x-4|$.

<a id="ch01-ex1C-q2"></a>
##### Question 2
**a** On the same axes, sketch the graphs of $y=|2 x-1|$ and $y=4-|x-1|$.

**b** Solve the inequality $|2 x-1|>4-|x-1|$.

<a id="ch01-ex1C-q3"></a>
##### Question 3
Solve. (You may use either an algebraic method or a graphical method.)

**a** $|2 x+1| \leqslant 3$

**b** $|2-x|<4$

**c** $|3 x-2| \geqslant 7$

<a id="ch01-ex1C-q4"></a>
##### Question 4
Solve. (You may use either an algebraic method or a graphical method.)

**a** $|2 x-5| \leqslant x-2$

**b** $|3+x|>4-2 x$

**c** $|x-7|-2 x \leqslant 4$

<a id="ch01-ex1C-q5"></a>
##### Question 5
Solve. (You may use either an algebraic method or a graphical method.)

**a** $|x+4|<|2 x|$

**b** $|2 x-5|>|3-x|$

**c** $|3 x-2| \leqslant|1-3 x|$

**d** $|x-1|>2|x-4|$

**e** $3|3-x| \geqslant|2 x-1|$

**f** $|3 x-5|<2|2-x|$

<a id="ch01-ex1C-q6"></a>
##### Question 6
Solve $|2 x+1|+|2 x-1|>5$.

## 1.4 Division of polynomials

A polynomial is an expression of the form

$$
a_{n} x^{n}+a_{n-1} x^{n-1}+a_{n-2} x^{n-2}+\qquad +a_{2} x^{2}+a_{1} x^{1}+a_{0}
$$

where:

- $x$ is a variable

- $n$ is a non-negative integer

- the coefficients $a_{n}, a_{n-1}, a_{n-2}, \qquad , a_{2}, a_{1}, a_{0}$ are constants

- $a_{n}$ is called the leading coefficient and $a_{n} \neq 0$

- $a_{0}$ is called the constant term.

The highest power of $x$ in the polynomial is called the degree of the polynomial.

For example, $5 x^{3}-6 x^{2}+2 x-6$ is a polynomial of degree 3.

In this section you will learn how to use long division to divide a polynomial by another polynomial. Alternative methods are possible, this is shown in Worked example 1.10.

#### DID YOU KNOW?

Polynomial functions can be used to predict the mass of an animal from its length.

![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-011_170_227_1743_1288.jpg)

<a id="ch01-we-1.7"></a>
#### WORKED EXAMPLE 1.7

Divide $x^{3}+2 x^{2}-11 x+6$ by $x-2$.

Answer

Step 1:

$$
\begin{align}
& x - 2 \longdiv { x ^ { 3 } + 2 x ^ { 2 } - 1 1 x + 6 } x^{2} \\
& \frac{x^{3}-2 x^{2}}{4 x^{2}}-11 x
\end{align}
$$

Divide the first term of the polynomial by $x$ : $x^{3} \div x=x^{2}$.

Multiply $(x-2)$ by $x^{2}: x^{2}(x-2)=x^{3}-2 x^{2}$.

Subtract: $\left(x^{3}+2 x^{2}\right)-\left(x^{3}-2 x^{2}\right)=4 x^{2}$.

Bring down the $-11 x$ from the next column.

Step 2: Repeat the process

$$
\begin{align}
x - 2 \longdiv { x ^ { 3 } + 2 x ^ { 2 } - 1 1 x + 6 } & \\
\frac{x^{3}-2 x^{2}}{4 x^{2}}-11 x & \text { Divide } 4 x^{2} \text { by } x: 4 x^{2} \div x=4 x . \\
\frac{4 x^{2}-8 x}{-3 x}+6 & \text { Multiply }(x-2) \text { by } 4 x: 4 x(x-2)=4 x^{2}-8 x . \\
\text { Subtract: }\left(4 x^{2}-11 x\right)-\left(4 x^{2}-8 x\right)=-3 x . & \text { Bring down the } 6 \text { from the next column } .
\end{align}
$$

Step 3: Repeat the process

$$
\begin{array}{lll} x - 2 \longdiv { x ^ { 3 } + 2 x ^ { 2 } - 1 1 x + 6 } & \\
\frac{x^{3}-2 x^{2}}{4 x^{2}-11 x} & & \text { Divide }-3 x \text { by } x:-3 x \div x=-3 . \\
\frac{4 x^{2}-8 x}{-3 x+6} & & \text { Multiply }(x-2) \text { by }-3:-3(x-2)=-3 x+6 . \\
& \text { Subtract: }(-3 x+6)-(-3 x+6)=0 . \end{array}
$$

Hence, $\left(x^{3}+2 x^{2}-11 x+6\right) \div(x-2)=x^{2}+4 x-3$.

Each part in the calculation in Worked example 1.7 has a special name:

$$
\left(x^{3}+2 x^{2}-11 x+6\right) \div(x-2)=\left(x^{2}+4 x-3\right)
$$

dividend divisor quotient

There was no remainder in this calculation so we say that $x-2$ is a factor of $x^{3}+2 x^{2}-11 x+6$.

<a id="ch01-we-1.8"></a>
#### WORKED EXAMPLE 1.8

Find the remainder when $2 x^{3}-x+52$ is divided by $x+3$.

Answer

There is no $x^{2}$ term in $2 x^{3}-x+52$ so we write it as $2 x^{3}+0 x^{2}-x+52$.

Step 1:

$$
\begin{gathered} x + 3 \longdiv { 2 x ^ { 3 } + 0 x ^ { 2 } - x + 5 2 } \\
\frac{2 x^{3}+6 x^{2}}{-6 x^{2}}-x \end{gathered}
$$

Divide the first term of the polynomial by $x$ : $2 x^{3} \div x=2 x^{2}$.

Multiply $(x+3)$ by $2 x^{2}: 2 x^{2}(x+3)=2 x^{3}+6 x^{2}$.

Subtract: $\left(2 x^{3}+0 x^{2}\right)-\left(2 x^{3}+6 x^{2}\right)=-6 x^{2}$.

Bring down the $-x$ from the next column.

Step 2: Repeat the process

$$
\begin{array}{r} 2 x^{2}-6 x \\
x + 3 \longdiv { 2 x ^ { 3 } + 0 x ^ { 2 } } - x + 5 2 \\
\frac{2 x^{3}+6 x^{2}}{-6 x^{2}}-x \\
\frac{-6 x^{2}-18 x}{17 x}+52 \end{array}
$$

Divide $-6 x^{2}$ by $x$ : $-6 x^{2} \div x=-6 x$.

Multiply $(x+3)$ by $-6 x:-6 x(x+3)=-6 x^{2}-18 x$.

Subtract: $\left(-6 x^{2}-x\right)-\left(-6 x^{2}-18 x\right)=17 x$.

Bring down the 52 from the next column.

Step 3: Repeat the process

$$
\begin{array}{r} 2 x^{2}-6 x+17 \\
x + 3 \longdiv { 2 x ^ { 3 } + 0 x ^ { 2 } - x + 5 2 } \\
\frac{2 x^{3}+6 x^{2}}{-6 x^{2}}-x \\
-6 x^{2}-18 x \\
\frac{17 x+52}{17 x+51} \end{array}
$$

Divide $17 x$ by $x: 17 x \div x=17$.

Multiply $(x+3)$ by 17: $17(x+3)=17 x+51$.

Subtract: $(17 x+52)-(17 x+51)=1$.

The remainder is 1.

The calculation in Worked example 1.8 can be written as:

$$
\left(2 x^{3}-x+52\right)=(x+3) \times\left(2 x^{2}-6 x+17\right)+1
$$

dividend divisor quotient remainder

<a id="ch01-kp-1.2"></a>
#### KEY POINT 1.2

The division algorithm for polynomials is:

dividend = divisor × quotient + remainder

<a id="ch01-ex1D"></a>
### EXERCISE 1D

<a id="ch01-ex1D-q1"></a>
##### Question 1
Simplify each of the following.

**a** $\left(x^{3}+5 x^{2}+5 x-2\right) \div(x+2)$

**b** $\left(x^{3}-8 x^{2}+22 x-21\right) \div(x-3)$

**c** $\left(3 x^{3}-7 x^{2}+6 x-2\right) \div(x-1)$

**d** $\left(2 x^{3}-3 x^{2}+8 x+5\right) \div(2 x+1)$

**e** $\left(5 x^{3}-13 x^{2}+10 x-8\right) \div(2-x)$

**f** $\left(6 x^{4}+13 x-19\right) \div(1-x)$

<a id="ch01-ex1D-q2"></a>
##### Question 2
Find the quotient and remainder for each of the following.

**a** $\left(x^{3}+2 x^{2}+5 x-4\right) \div(x+1)$

**b** $\left(6 x^{3}+7 x^{2}-6\right) \div(x-2)$

**c** $\left(8 x^{3}+x^{2}-2 x+1\right) \div(2 x-1)$

**d** $\left(2 x^{3}-9 x^{2}-9\right) \div(3-x)$

**e** $\left(x^{3}+5 x^{2}-3 x-1\right) \div\left(x^{2}+2 x+1\right)$

**f** $\left(5 x^{4}-2 x^{2}-13 x+8\right) \div\left(x^{2}+1\right)$

<a id="ch01-ex1D-q3"></a>
##### Question 3
Use algebraic division to show these two important factorisations.

**a** $x^{3}-y^{3}=(x-y)\left(x^{2}+x y+y^{2}\right)$

**b** $x^{3}+y^{3}=(x+y)\left(x^{2}-x y+y^{2}\right)$

<a id="ch01-ex1D-q4"></a>
##### Question 4
**a** Use algebraic division to show that $x-2$ is a factor of $2 x^{3}+7 x^{2}-43 x+42$.

**b** Hence, factorise $2 x^{3}+7 x^{2}-43 x+42$ completely.

<a id="ch01-ex1D-q5"></a>
##### Question 5
**a** Use algebraic division to show that $2 x+1$ is a factor of $12 x^{3}+16 x^{2}-3 x-4$.

**b** Hence, solve the equation $12 x^{3}+16 x^{2}-3 x-4=0$.

<a id="ch01-ex1D-q6"></a>
##### Question 6
**a** Use algebraic division to show that $x+1$ is a factor of $x^{3}-x^{2}+2 x+4$.

**b** Hence, show that there is only one real root for the equation $x^{3}-x^{2}+2 x+4=0$.

<a id="ch01-ex1D-q7"></a>
##### Question 7
The general formula for solving the quadratic equation $a x^{2}+b x+c=0$ is $x=\frac{-b \pm \sqrt{b^{2}-4 a c}}{2 a}$.

There is a general formula for solving a cubic equation. Find out more about this formula and use it to solve $2 x^{3}-5 x^{2}-28 x+15=0$.

## 1.5 The factor theorem

In Worked example 1.7 you found that $x^{3}+2 x^{2}-11 x+6$ is exactly divisible by $x-2$.

$$
\left(x^{3}+2 x^{2}-11 x+6\right) \div(x-2)=x^{2}+4 x-3
$$

This can also be written as:

$$
x^{3}+2 x^{2}-11 x+6=(x-2)\left(x^{2}+4 x-3\right)
$$

If a polynomial $\mathrm{P}(x)$ divides exactly by a linear factor $x-c$ to give the polynomial $\mathrm{Q}(x)$, then

$$
\mathrm{P}(x)=(x-c) \mathrm{Q}(x)
$$

Substituting $x=c$ into this formula gives $\mathrm{P}(c)=0$. This is known as the factor theorem.

<a id="ch01-kp-1.3"></a>
#### KEY POINT 1.3

If for a polynomial $\mathrm{P}(x), \mathrm{P}(c)=0$ then $x-c$ is a factor of $\mathrm{P}(x)$.

For example, when $x=2$,

$$
x^{3}+2 x^{2}-11 x+6=(2)^{3}+2(2)^{2}-11(2)+6=8+8-22+6=0
$$

Therefore $(x-2)$ is a factor of $x^{3}+2 x^{2}-11 x+6$.

The factor theorem can be extended to:

<a id="ch01-kp-1.4"></a>
#### KEY POINT 1.4

If for a polynomial $\mathrm{P}(x), \mathrm{P}\left(\frac{b}{a}\right)=0$ then $a x-b$ is a factor of $\mathrm{P}(x)$.

For example, when $x=\frac{2}{3}$,

$$
3 x^{3}-2 x^{2}-3 x+2=3\left(\frac{2}{3}\right)^{3}-2\left(\frac{2}{3}\right)^{2}-3\left(\frac{2}{3}\right)+2=\frac{8}{9}-\frac{8}{9}-2+2=0
$$

Hence $3 x-2$ is a factor of $3 x^{3}-2 x^{2}-3 x+2$.

<a id="ch01-we-1.9"></a>
#### WORKED EXAMPLE 1.9

Use the factor theorem to show that $x-3$ is a factor of $x^{3}+2 x^{2}-16 x+3$.

Answer

Let

$$
f(x)=x^{3}+2 x^{2}-16 x+3
$$

If $\mathrm{f}(3)=0$, then $(x-3)$ is a factor.

$$
\begin{align}
f(3) & =(3)^{3}+2(3)^{2}-16(3)+3 \\
& =27+18-48+3 \\
& =0
\end{align}
$$

Hence $x-3$ is a factor of $x^{3}+2 x^{2}-16 x+3$.

#### EXPLORE 1.3

A $x^{3}+x^{2}-3 x+1$

B $2 x^{3}+7 x^{2}+x-10$

C $3 x^{3}+7 x^{2}-4$

D $6 x^{3}+x^{2}-17 x+10$

E $6 x^{4}+x^{3}-8 x^{2}-x+2$

F $3 x^{3}+x^{2}-10 x-8$

Discuss with your classmates which of the expressions have:

$1 x-1$ as a factor

$2 x+2$ as a factor

$32 x-1$ as a factor.

<a id="ch01-we-1.10"></a>
#### WORKED EXAMPLE 1.10

**a** Given that $3 x^{2}+5 x-2$ is a factor of $3 x^{3}+17 x^{2}+a x+b$, find the value of $a$ and the value of $b$.

**b** Hence, factorise the polynomial completely.

Answer

**a** Let $\mathrm{f}(x)=3 x^{3}+17 x^{2}+a x+b$.

Factorising $3 x^{2}+5 x-2$ gives $(3 x-1)(x+2)$.

Hence, $3 x-1$ and $x+2$ are also factors of $\mathrm{f}(x)$.

Using the factor theorem, $\mathrm{f}\left(\frac{1}{3}\right)=0$ and $\mathrm{f}(-2)=0$.

$$
\begin{align}
f\left(\frac{1}{3}\right)=0 \text { gives } 3\left(\frac{1}{3}\right)^{3}+17\left(\frac{1}{3}\right)^{2}+a\left(\frac{1}{3}\right)+b & =0 \\
\frac{1}{9}+\frac{17}{9}+\frac{a}{3}+b & =0 \\
a+3 b & =-6 \tag{1}
\end{align}
$$

$$
\begin{align}
f(-2)=0 \text { gives } 3(-2)^{3}+17(-2)^{2}+a(-2)+b & =0 \\
-24+68-2 a+b & =0 \\
2 a-b & =44 \tag{2}
\end{align}
$$

(1) +3×(2) gives $7 a=126$

$$
a=18
$$

Substituting in (2) gives $b=-8$.

Hence, $a=18$ and $b=-8$.

**b** Method 1: Using long division

$$
\begin{array}{r} x+4 \\
3 x ^ { 2 } + 5 x - 2 \longdiv { 3 x ^ { 3 } + 1 7 x ^ { 2 } + 1 8 x - 8 } \\
\frac{3 x^{3}+5 x^{2}-2 x}{12 x^{2}+20 x-8} \\
\frac{12 x^{2}+20 x-8}{0} \end{array}
$$

Hence, $3 x^{3}+17 x^{2}+18 x-8=\left(3 x^{2}+5 x-2\right)(x+4)$

$$
=(3 x-1)(x+2)(x+4)
$$

Method 2: Equating coefficients

If $3 x^{2}+5 x-2$ is a factor, $3 x^{3}+17 x^{2}+18 x-8$ can be written as

$$
3 x^{3}+17 x^{2}+18 x-8=\left(3 x^{2}+5 x-2\right)(c x+d)
$$

coefficient of $x^{3}$ is 3, so $c=1$ since $3 \times 1=3 \quad$ constant term is -8 , so $d=4$ since $-2 \times 4=-8$

Hence, $3 x^{3}+17 x^{2}+18 x-8=(3 x-1)(x+2)(x+4)$

<a id="ch01-we-1.11"></a>
#### WORKED EXAMPLE 1.11

Solve $x^{3}+4 x^{2}-19 x+14=0$.

Answer

Let $\mathrm{f}(x)=x^{3}+4 x^{2}-19 x+14$.

The positive and negative factors of 14 are ±1, ±2, ±7 and ±14.

$\mathrm{f}(1)=(1)^{3}+4(1)^{2}-19(1)+14=0$, so $x-1$ is a factor of $\mathrm{f}(x)$.

The other factors of $\mathrm{f}(x)$ can be found by any of the following methods.

Method 1: Trial and error

$\mathrm{f}(2)=(2)^{3}+4(2)^{2}-19(2)+14=0$, so $x-2$ is a factor of $\mathrm{f}(x)$ $\mathrm{f}(-7)=(-7)^{3}+4(-7)^{2}-19(-7)+14=0$, so $x+7$ is a factor of $\mathrm{f}(x)$.

Hence, $\mathrm{f}(x)=(x-1)(x-2)(x+7)$.

Method 2: Long division

$$
\begin{array}{r} x^{2}+5 x-14 \\
x - 1 \longdiv { x ^ { 3 } + 4 x ^ { 2 } - 1 9 x + 1 4 } \\
\frac{x^{3}-x^{2}}{5 x^{2}-19 x} \\
\frac{5 x^{2}-5 x}{-14 x+14} \\
\frac{-14 x+14}{0} \end{array}
$$

Hence,

$$
\begin{align}
\mathrm{f}(x) & =(x-1)\left(x^{2}+5 x-14\right) \\
& =(x-1)(x-2)(x+7)
\end{align}
$$

Method 3: Equating coefficients

Since $x-1$ is a factor, $x^{3}+4 x^{2}-19 x+14$ can be written as:

$$
x^{3}+4 x^{2}-19 x+14=(x-1)\left(a x^{2}+b x+c\right)
$$

coefficient of $x^{3}$ is 1, so $a=1$ since $1 \times 1=1$

constant term is 14, so $c=-14$ since $-1 \times-14=14$

$$
x^{3}+4 x^{2}-19 x+14=(x-1)\left(x^{2}+b x-14\right)
$$

Equating the coefficients of $x^{2}$ gives $4=-1+b$, so $b=5$.

Hence,

$$
\begin{align}
\mathrm{f}(x) & =(x-1)\left(x^{2}+5 x-14\right) \\
& =(x-1)(x-2)(x+7)
\end{align}
$$

The solutions of the equation $x^{3}+4 x^{2}-19 x+14=0$ are: $x=1, x=2$ and $x=-7$.

<a id="ch01-ex1E"></a>
### EXERCISE 1E

<a id="ch01-ex1E-q1"></a>
##### Question 1
Use the factor theorem to show that $x+1$ is a factor of $x^{4}-3 x^{3}-4 x^{2}+5 x+5$.

<a id="ch01-ex1E-q2"></a>
##### Question 2
Use the factor theorem to show that $2 x-5$ is a factor of $2 x^{3}-7 x^{2}+9 x-10$.

<a id="ch01-ex1E-q3"></a>
##### Question 3
Given that $x+4$ is a factor of $x^{3}+a x^{2}-29 x+12$, find the value of $a$.

<a id="ch01-ex1E-q4"></a>
##### Question 4
Given that $x-3$ is a factor of $x^{3}+a x^{2}+b x-30$, express $a$ in terms of $b$.

<a id="ch01-ex1E-q5"></a>
##### Question 5
Given that $2 x^{2}+x-1$ is a factor of $2 x^{3}-x^{2}+a x+b$, find the value of $a$ and the value of $b$.

<a id="ch01-ex1E-q6"></a>
##### Question 6
Given that $x-3$ and $2 x+1$ are factors of $2 x^{3}+p x^{2}+(2 q-1) x+q$ :

**a** Find the value of $p$ and the value of $q$.

**b** Explain why $x+2$ is also a factor of the expression.

<a id="ch01-ex1E-q7"></a>
##### Question 7
It is given that $x+a$ is a factor of $x^{3}+4 x^{2}+7 a x+4 a$. Find the possible values of $a$.

<a id="ch01-ex1E-q8"></a>
##### Question 8
**a** It is given that $x+1$ is a common factor of $x^{3}+p x+q$ and $x^{3}+(1-p) x^{2}+19 x-2 q$. Find the value of $p$ and the value of $q$.

**b** When $p$ and $q$ have these values, factorise $x^{3}+p x+q$ and $x^{3}+(1-p) x^{2}+19 x-2 q$ completely.

<a id="ch01-ex1E-q9"></a>
##### Question 9
Given that $x-1$ and $x+2$ are factors of $x^{4}-x^{3}+p x^{2}-11 x+q$ :

**a** Find the value of $p$ and the value of $q$.

**b** When $p$ and $q$ have these values, factorise $x^{4}-x^{3}+p x^{2}-11 x+q$ completely.

<a id="ch01-ex1E-q10"></a>
##### Question 10
Solve.

**a** $x^{3}-5 x^{2}-4 x+20=0$

**b** $x^{3}+5 x^{2}-17 x-21=0$

**c** $2 x^{3}-5 x^{2}-13 x+30=0$

**d** $3 x^{3}+17 x^{2}+18 x-8=0$

**e** $x^{4}+2 x^{3}-7 x^{2}-8 x+12=0$

**f** $2 x^{4}-11 x^{3}+12 x^{2}+x-4=0$

<a id="ch01-ex1E-q11"></a>
##### Question 11
You are given that the equation $x^{3}+a x^{2}+b x+c=0$ has three real roots and that these roots are consecutive terms in an arithmetic progression. Show that $2 a^{3}+27 c=9 a b$.

<a id="ch01-ex1E-q12"></a>
##### Question 12
Find the set of values for $k$ for which the equation $3 x^{4}+4 x^{3}-12 x^{2}+k=0$ has four real roots.

## 1.6 The remainder theorem

Consider $\mathrm{f}(x)=2 x^{3}-5 x^{2}-2 x+12$.

Substituting $x=2$ in the polynomial gives $\mathrm{f}(2)=2(2)^{3}-5(2)^{2}-2(2)+12=4$.

When $2 x^{3}-5 x^{2}-2 x+12$ is divided by $x-2$, there is a remainder:

$$
\begin{array}{r} 2 x^{2}-x-4 \\
x - 2 \longdiv { 2 x ^ { 3 } - 5 x ^ { 2 } - 2 x + 1 2 } \\
\frac{2 x^{3}-4 x^{2}}{-x^{2}-2 x} \\
\frac{-x^{2}+2 x}{-4 x+12} \\
\frac{-4 x+8}{4} \end{array}
$$

The remainder is 4 . This is the same value as f(2).

$$
\begin{align}
& \mathrm{f}(x)=2 x^{3}-5 x^{2}-2 x+12 \text { can be written as: } \\
& \mathrm{f}(x)=(x-2)\left(2 x^{2}-x-4\right)+4
\end{align}
$$

In general:

If a polynomial $\mathrm{P}(x)$ is divided by $x-c$ to give the polynomial $\mathrm{Q}(x)$ and a remainder $R$, then:

$$
\mathrm{P}(x)=(x-c) \mathrm{Q}(x)+R
$$

Substituting $x=c$ into this formula gives $\mathrm{P}(c)=R$.

This leads to the remainder theorem.

<a id="ch01-kp-1.5"></a>
#### KEY POINT 1.5

The remainder theorem:

If a polynomial $\mathrm{P}(x)$ is divided by $x-c$, the remainder is $\mathrm{P}(c)$.

The remainder theorem can be extended to:

<a id="ch01-kp-1.6"></a>
#### KEY POINT 1.6

If a polynomial $\mathrm{P}(x)$ is divided by $a x-b$, the remainder is $\mathrm{P}\left(\frac{b}{a}\right)$.

<a id="ch01-we-1.12"></a>
#### WORKED EXAMPLE 1.12

Use the factor theorem to find the remainder when $4 x^{3}-2 x^{2}+5 x-8$ is divided by $x+1$.

Answer

Let $\mathrm{f}(x)=4 x^{3}-2 x^{2}+5 x-8$

$$
\begin{align}
\text { Remainder } & =f(-1) \\
& =4(-1)^{3}-2(-1)^{2}+5(-1)-8 \\
& =-4-2-5-8 \\
& =-19
\end{align}
$$

<a id="ch01-we-1.13"></a>
#### WORKED EXAMPLE 1.13

$$
f(x)=6 x^{3}+a x^{2}+b x-4
$$

When $\mathrm{f}(x)$ is divided by $x-1$, the remainder is 3.

When $\mathrm{f}(x)$ is divided by $3 x+2$, the remainder is -2 .

Find the value of $a$ and the value of $b$.

Answer

$$
f(x)=6 x^{3}+a x^{2}+b x-4
$$

When $\mathrm{f}(x)$ is divided by $x-1$ the remainder is 3, hence $\mathrm{f}(1)=3$.

$$
\begin{align}
6(1)^{3}+a(1)^{2}+b(1)-4 & =3 \\
a+b & =1 \tag{1}
\end{align}
$$

When $\mathrm{f}(x)$ is divided by $3 x+2$ the remainder is -2, hence $\mathrm{f}\left(-\frac{2}{3}\right)=-2$.

$$
\begin{align}
6\left(-\frac{2}{3}\right)^{3}+a\left(-\frac{2}{3}\right)^{2}+b\left(-\frac{2}{3}\right)-4 & =-2 \\
2 a-3 b & =17 \tag{2}
\end{align}
$$

$2 \times(1)-(2)$ gives $5 b=-15$

$$
b=-3
$$

Substituting $b=-3$ in equation (1) gives $a=4$.

$a=4$ and $b=-3$.

<a id="ch01-ex1F"></a>
### EXERCISE 1F

<a id="ch01-ex1F-q1"></a>
##### Question 1
Find the remainder when:

**a** $6 x^{3}+3 x^{2}-5 x+2$ is divided by $x-1$

**b** $x^{3}+x^{2}-11 x+12$ is divided by $x+4$

**c** $x^{4}+2 x^{3}-5 x^{2}-2 x+8$ is divided by $x+1$

**d** $4 x^{3}-x^{2}-18 x+1$ is divided by $2 x-1$

<a id="ch01-ex1F-q2"></a>
##### Question 2
**a** When $x^{3}-3 x^{2}+a x-7$ is divided by $x+2$, the remainder is -37. Find the value of $a$.

**b** When $9 x^{3}+b x-5$ is divided by $3 x+2$, the remainder is -13. Find the value of $b$.

<a id="ch01-ex1F-q3"></a>
##### Question 3
$ \mathrm{f}(x)=x^{3}+a x^{2}+b x-5$

$\mathrm{f}(x)$ has a factor of $x-1$ and leaves a remainder of -6 when divided by $x+1$.

Find the value of $a$ and the value of $b$.

<a id="ch01-ex1F-q4"></a>
##### Question 4
The polynomial $3 x^{3}+a x^{2}+b x+8$, where $a$ and $b$ are constants, is denoted by $\mathrm{f}(x)$. It is given that $x+2$ is a factor of $\mathrm{f}(x)$, and that when $\mathrm{f}(x)$ is divided by $x-1$ the remainder is 15. Find the value of $a$ and the value of $b$.

<a id="ch01-ex1F-q5"></a>
##### Question 5
The function $\mathrm{f}(x)=a x^{3}+7 x^{2}+b x-8$, where $a$ and $b$ are constants, is such that $2 x+1$ is a factor. The remainder when $\mathrm{f}(x)$ is divided by $x+1$ is 7 .

**a** Find the value of $a$ and the value of $b$.

**b** Factorise $\mathrm{f}(x)$ completely.

<a id="ch01-ex1F-q6"></a>
##### Question 6
The polynomial $x^{3}+6 x^{2}+p x-3$ leaves a remainder of $R$ when divided by $x+1$ and a remainder of $-10 R$ when divided by $x-3$.

**a** Find the value of $p$.

**b** Hence find the remainder when the expression is divided by $x-2$.

<a id="ch01-ex1F-q7"></a>
##### Question 7
The polynomial $x^{3}+a x^{2}+b x+2$, where $a$ and $b$ are constants, is denoted by $\mathrm{f}(x)$. It is given that $x-2$ is a factor of $\mathrm{f}(x)$, and that when $\mathrm{f}(x)$ is divided by $x+1$ the remainder is 21.

**a** Find the value of $a$ and the value of $b$.

**b** Solve the equation $\mathrm{f}(x)=0$, giving the roots in exact form.

<a id="ch01-ex1F-q8"></a>
##### Question 8
The polynomial $2 x^{3}+a x^{2}+b x+c$ is denoted by $\mathrm{f}(x)$. The roots of $\mathrm{f}(x)=0$ are -1, 2 and $k$. When $\mathrm{f}(x)$ is divided by $x-1$, the remainder is 6.

**a** Find the value of $k$.

**b** Find the remainder when $\mathrm{f}(x)$ is divided by $x+2$.

<a id="ch01-ex1F-q9"></a>
##### Question 9
$ \mathrm{P}(x)=2 x+4 x^{2}+6 x^{3}+\qquad +100 x^{50}$

Find the remainder when $\mathrm{P}(x)$ is divided by $(x-1)$.

<a id="ch01-ex1F-q10"></a>
##### Question 10
$ \mathrm{P}(x)=3(x+1)(x+2)(x+3)+a(x+1)(x+2)+b(x+1)+c$

It is given that when $\mathrm{P}(x)$ is divided by each of $x+1, x+2$ and $x+3$ the remainders are -2,2 and 10, respectively. Find the value of $a$, the value of $b$ and the value of $c$.

### Checklist of learning and understanding

The modulus function

- The modulus function $|x|$ is defined by:

$$
|x|=\left\{\begin{array}{r} x \text { if } x \geqslant 0 \\
-x \text { if } x<0 \end{array}\right.
$$

The division algorithm for polynomials

- $\mathrm{P}(x)=\mathrm{D}(x) \times \mathrm{Q}(x)+\mathrm{R}(x)$ dividend = divisor × quotient + remainder

The factor theorem

- If for a polynomial $\mathrm{P}(x), \mathrm{P}(c)=0$ then $x-c$ is a factor of $\mathrm{P}(x)$.

- If for a polynomial $\mathrm{P}(x), \mathrm{P}\left(\frac{b}{a}\right)=0$ then $a x-b$ is a factor of $\mathrm{P}(x)$.

The remainder theorem

- If a polynomial $\mathrm{P}(x)$ is divided by $x-c$, the remainder is $\mathrm{P}(c)$.

- If a polynomial $\mathrm{P}(x)$ is divided by $a x-b$, the remainder is $\mathrm{P}\left(\frac{b}{a}\right)$.

<a id="ch01-review"></a>
### END-OF-CHAPTER REVIEW EXERCISE 1

<a id="ch01-review-q1"></a>
##### Question 1
Solve the equation $|2 x-3|=|5 x+1|$. ..... `[3]`

<a id="ch01-review-q2"></a>
##### Question 2
Solve the inequality $|5 x-3| \geqslant 7$. ..... `[3]`

<a id="ch01-review-q3"></a>
##### Question 3
Solve the inequality $|2 x-3|<|2-x|$. ..... `[3]`

<a id="ch01-review-q4"></a>
##### Question 4
Solve the equation $\left|x^{2}-14\right|=11$. ..... `[4]`

<a id="ch01-review-q5"></a>
##### Question 5
The polynomial $a x^{3}-13 x^{2}-41 x-2 a$, where $a$ is a constant, is denoted by $\mathrm{p}(x)$.

**a** Given that $(x-4)$ is a factor of $\mathrm{p}(x)$, find the value of $a$. ..... `[2]`

**b** When $a$ has this value, factorise $\mathrm{p}(x)$ completely. ..... `[3]`

<a id="ch01-review-q6"></a>
##### Question 6
The polynomial $6 x^{3}-23 x^{2}-38 x+15$ is denoted by $\mathrm{f}(x)$.

**a** Show that $(x-5)$ is a factor of $\mathrm{f}(x)$ and hence factorise $\mathrm{f}(x)$ completely. ..... `[4]`

**b** Write down the roots of $\mathrm{f}(|x|)=0$. ..... `[1]`

<a id="ch01-review-q7"></a>
##### Question 7
The polynomial $x^{3}-5 x^{2}+a x+b$ is denoted by $\mathrm{f}(x)$. It is given that $(x+2)$ is a factor of $\mathrm{f}(x)$ and that when $\mathrm{f}(x)$ is divided by $(x-1)$ the remainder is -6. Find the value of $a$ and the value of $b$. ..... `[5]`

<a id="ch01-review-q8"></a>
##### Question 8
The polynomial $x^{3}-5 x^{2}+7 x-3$ is denoted by $\mathrm{p}(x)$.

**a** Find the quotient and remainder when $\mathrm{p}(x)$ is divided by $\left(x^{2}-2 x-1\right)$. ..... `[4]`

**b** Use the factor theorem to show that $(x-3)$ is a factor of $\mathrm{p}(x)$. ..... `[2]`

<a id="ch01-review-q9"></a>
##### Question 9
The polynomial $4 x^{4}+4 x^{3}-7 x^{2}-4 x+8$ is denoted by $\mathrm{p}(x)$.

**a** Find the quotient and remainder when $\mathrm{p}(x)$ is divided by $\left(x^{2}-1\right)$. ..... `[3]`

**b** Hence solve the equation $4 x^{4}+4 x^{3}-7 x^{2}-4 x+3=0$. ..... `[3]`

<a id="ch01-review-q10"></a>
##### Question 10
The polynomial $x^{4}-48 x^{2}-21 x-2$ is denoted by $\mathrm{f}(x)$.

**a** Find the value of the constant $k$ for which $\mathrm{f}(x)=\left(x^{2}+k x+2\right)\left(x^{2}-k x-1\right)$. ..... `[3]`

**b** Hence solve the equation $\mathrm{f}(x)=0$. Give your answers in exact form. ..... `[3]`

<a id="ch01-review-q11"></a>
##### Question 11
The polynomial $2 x^{4}+3 x^{3}-12 x^{2}-7 x+a$ is denoted by $\mathrm{p}(x)$.

**a** Given that $(2 x-1)$ is a factor of $\mathrm{p}(x)$, find the value of $a$. ..... `[2]`

**b** When $a$ has this value, verify that $(x+3)$ is also a factor of $\mathrm{p}(x)$ and hence factorise $\mathrm{p}(x)$ completely. ..... `[4]`

<a id="ch01-review-q12"></a>
##### Question 12
The polynomial $3 x^{3}+a x^{2}-36 x+20$ is denoted by $\mathrm{p}(x)$.

**a** Given that $(x-2)$ is a factor of $\mathrm{p}(x)$, find the value of $a$. ..... `[2]`

**b** When $a$ has this value, solve the equation $\mathrm{p}(x)=0$. ..... `[4]`

<a id="ch01-review-q13"></a>
##### Question 13
The polynomial $2 x^{3}+5 x^{2}-7 x+11$ is denoted by $\mathrm{f}(x)$.

**a** Find the remainder when $\mathrm{f}(x)$ is divided by $(x-2)$. ..... `[2]`

**b** Find the quotient and remainder when $\mathrm{f}(x)$ is divided by $\left(x^{2}-4 x+2\right)$. ..... `[4]`

<a id="ch01-review-q14"></a>
##### Question 14
The polynomial $a x^{3}+b x^{2}-x+12$ is denoted by $\mathrm{p}(x)$.

**a** Given that $(x-3)$ and $(x+1)$ are factors of $\mathrm{p}(x)$, find the value of $a$ and the value of $b$. ..... `[4]`

**b** When $a$ and $b$ take these values, find the other linear factor of $\mathrm{p}(x)$. ..... `[2]`

<a id="ch01-review-q15"></a>
##### Question 15
The polynomial $6 x^{3}+x^{2}+a x-10$, where $a$ is a constant, is denoted by $\mathrm{P}(x)$. It is given that when $\mathrm{P}(x)$ is divided by $(x+2)$ the remainder is -12.

**a** Find the value of $a$ and hence verify that $(2 x+1)$ is a factor of $\mathrm{P}(x)$. `[3]`

**b** When $a$ has this value, solve the equation $\mathrm{P}(x)=0$. `[4]`

<a id="ch01-review-q16"></a>
##### Question 16
The polynomial $2 x^{3}+a x^{2}+b x+6$ is denoted by $\mathrm{p}(x)$.

**a** Given that $(x+2)$ and $(x-3)$ are factors of $\mathrm{p}(x)$, find the value of $a$ and the value of $b$. `[4]`

**b** When $a$ and $b$ take these values, factorise $\mathrm{p}(x)$ completely. `[3]`

<a id="ch01-review-q17"></a>
##### Question 17
The polynomials $\mathrm{P}(x)$ and $\mathrm{Q}(x)$ are defined as:

$$
\mathrm{P}(x)=x^{3}+a x^{2}+b \text { and } \mathrm{Q}(x)=x^{3}+b x^{2}+a .
$$

It is given that $(x-2)$ is a factor of $\mathrm{P}(x)$ and that when $\mathrm{Q}(x)$ is divided by $(x+1)$ the remainder is -15.

**a** Find the value of $a$ and the value of $b$. `[5]`

**b** When $a$ and $b$ take these values, find the least possible value of $\mathrm{P}(x)-\mathrm{Q}(x)$ as $x$ varies. `[2]`

<a id="ch01-review-q18"></a>
##### Question 18
The polynomial $5 x^{3}-13 x^{2}+17 x-7$ is denoted by $\mathrm{p}(x)$.

**a** Find the quotient when $\mathrm{p}(x)$ is divided by $(x-1)$, and show that the remainder is 2. `[4]`

**b** Hence show that the polynomial $5 x^{3}-13 x^{2}+17 x-9$ has exactly one real root. `[3]`

<a id="ch01-review-q19"></a>
##### Question 19
The polynomial $4 x^{3}+k x^{2}-65 x+18$ is denoted by $\mathrm{f}(x)$.

**a** Given that $(x+2)$ is a factor of $\mathrm{f}(x)$, find the value of $k$. `[2]`

**b** When $k$ has this value, solve the equation $\mathrm{f}(x)=0$. `[4]`

**c** Write down the roots of $\mathrm{f}\left(x^{2}\right)=0$. `[1]`

<a id="ch01-review-q20"></a>
##### Question 20
The polynomial $2 x^{3}-5 x^{2}+a x+b$, where $a$ and $b$ are constants, is denoted by $\mathrm{f}(x)$. It is given that when $\mathrm{f}(x)$ is divided by $(x+2)$ the remainder is 8 and that when $\mathrm{f}(x)$ is divided by $(x-1)$ the remainder is 50.

**a** Find the value of $a$ and the value of $b$. `[5]`

**b** When $a$ and $b$ have these values, find the quotient and remainder when $\mathrm{f}(x)$ is divided by $x^{2}-x+2$. `[3]`

<a id="ch01-review-q21"></a>
##### Question 21
The polynomial $2 x^{3}-9 x^{2}+a x+b$, where $a$ and $b$ are constants, is denoted by $\mathrm{f}(x)$. It is given that ( $x+2$ ) is a factor of $\mathrm{f}(x)$, and that when $\mathrm{f}(x)$ is divided by ( $x+1$ ) the remainder is 30.

**a** Find the value of $a$ and the value of $b$. `[5]`

**b** When $a$ and $b$ have these values, solve the equation $\mathrm{f}(x)=0$. `[4]`

<a id="ch01-review-q22"></a>
##### Question 22
The polynomial $x^{3}+3 x^{2}+4 x+2$ is denoted by $\mathrm{f}(x)$.

**i** Find the quotient and remainder when $\mathrm{f}(x)$ is divided by $x^{2}+x-1$. `[4]`

**ii** Use the factor theorem to show that $(x+1)$ is a factor of $\mathrm{f}(x)$. `[2]`

<a id="ch01-review-q23"></a>
##### Question 23
The polynomial $4 x^{3}+a x^{2}+9 x+9$, where $a$ is a constant, is denoted by $\mathrm{p}(x)$. It is given that when $\mathrm{p}(x)$ is divided by $(2 x-1)$ the remainder is 10.

**i** Find the value of $a$ and hence verify that $(x-3)$ is a factor of $\mathrm{p}(x)$. `[3]`

**ii** When $a$ has this value, solve the equation $\mathrm{p}(x)=0$. `[4]`

*Cambridge International AS \& A Level Mathematics 9709 Paper 21 Q5 November 2011*

<a id="ch01-review-q24"></a>
##### Question 24
The polynomial $a x^{3}-5 x^{2}+b x+9$, where $a$ and $b$ are constants, is denoted by $\mathrm{p}(x)$. It is given that ( $2 x+3$ ) is a factor of $\mathrm{p}(x)$, and that when $\mathrm{p}(x)$ is divided by ( $x+1$ ) the remainder is 8 .

**i** Find the values of $a$ and $b$. `[5]`

**ii** When $a$ and $b$ have these values, factorise $\mathrm{p}(x)$ completely. `[3]`

*Cambridge International AS \& A Level Mathematics 9709 Paper 21 Q4 June 2013*

![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-025_1345_1940_3_136.jpg)
