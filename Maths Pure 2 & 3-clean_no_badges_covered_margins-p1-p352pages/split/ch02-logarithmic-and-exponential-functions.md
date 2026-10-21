# Chapter 2: Logarithmic and exponential functions

In this chapter you will learn how to:

- understand the relationship between logarithms and indices, and use the laws of logarithms (excluding change of base)

- understand the definition and properties of $\mathrm{e}^{x}$ and $\ln x$, including their relationship as inverse functions and their graphs

- use logarithms to solve equations and inequalities in which the unknown appears in indices

- use logarithms to transform a given relationship to linear form, and hence determine unknown constants by considering the gradient and/or intercept.

<a id="ch02-prerequisite"></a>
### PREREQUISITE KNOWLEDGE

| Where it comes from | What you should be able to do | Check your skills |
| :--- | :--- | :--- |
| IGCSE / O Level Mathematics | Use and interpret positive, negative, fractional and zero indices. | 1 Evaluate.<br>&#160;&#160;a $5^{-2}$<br>&#160;&#160;b $8^{\frac{2}{3}}$<br>&#160;&#160;c $7^{0}$<br>2 Solve $32^{x}=2$.<br> |
| IGCSE / O Level Mathematics | Use the rules of indices. | 3 Simplify.<br>&#160;&#160;a $3 x^{-4} \times \frac{2}{3} x^{\frac{1}{2}}$<br>&#160;&#160;b $\frac{2}{5} x^{\frac{1}{2}} \div 2 x^{-2}$<br>&#160;&#160;c $\left(\frac{2 x^{5}}{3}\right)^{3}$<br> |

What is a logarithm?

At IGCSE / O Level we learnt how to solve some simple exponential equations. For example, $32^{x}=2$ can be solved by first writing 32 as a power of 2. In this chapter we will learn how to solve more difficult exponential equations such as $a^{x}=b$ where there is no obvious way of writing the numbers $a$ and $b$ in index form with the same base number. In order to be able to do this we will first learn about a new type of function called the logarithmic function. A logarithmic function is the inverse of an exponential function.

At IGCSE / O Level we learnt about exponential growth and decay and its applications to numerous real-life problems such as investments and population sizes. Logarithmic functions also have real-life applications such as the amount of energy released during an earthquake (the Richter scale). One of the most fascinating occurrences of logarithms in nature is that of the logarithmic spiral that can be observed in a nautilus shell. We also see logarithmic spiral shapes in spiral galaxies, and in plants such as sunflowers.

2.1 Logarithms to base 10

Consider the exponential function $\mathrm{f}(x)=10^{x}$.

To solve the equation $10^{x}=6$, we could make an estimate by noting that $10^{0}=1$ and $10^{1}=10$, hence $0<x<1$. We could then try values of $x$ between 0 and 1 to find a more accurate value for $x$.

The graph of $y=10^{x}$ could also be used to give a more accurate value for $x$ when $10^{x}=6$.

![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-026_287_631_2319_554.jpg)

From the graph, $x \approx 0.78$.

There is, however, a function that gives the value of $x$ directly:

If $10^{x}=6$ then $x=\log _{10} 6$.

$\log _{10} 6$ is read as ' $\log 6$ to base 10'.

log is short for logarithm.

On a calculator, for logs to the base 10, we use the log or lg key.

So if $10^{x}=6$

then

$$
\begin{align}
& x=\log _{10} 6 \\
& x=0.778 \text { to } 3 \text { significant figures. }
\end{align}
$$

<a id="ch02-kp-2.1"></a>
#### KEY POINT 2.1

The rule for base 10 is:

If $y=10^{x}$ then $x=\log _{10} y$

This rule can be described in words as:

$\log _{10} y$ is the power that 10 must be raised to in order to obtain $y$.

For example, $\log _{10} 100=2$ since $100=10^{2}$.

$y=10^{x}$ and $y=\log _{10} x$ are inverse functions.

We say that $y=10^{x} \Leftrightarrow x=\log _{10} y$.

This is read as: $y=10^{x}$ is equivalent to saying that $x=\log _{10} y$.

#### EXPLORE 2.1

**1** Discuss with your classmates why each of these two statements is true.

$$
\left.\log _{10} 10^{x}=x \text { for } x \in \mathbb{R}\right) \quad\left(10^{\log _{10} x}=x \text { for } x>0\right.
$$

**2** **a** Discuss with your classmates why each of these two statements is true.

$$
\left.\log _{10} 10=1\right) \quad\left(\log _{10} 1=0\right.
$$

**b** Discuss what the missing numbers should be in this table of values, giving reasons for your answers.

| $\boldsymbol{\operatorname { l o g }}_{\mathbf{1 0}} \mathbf{0 . 0 1}$ | $\boldsymbol{\operatorname { l o g }}_{\mathbf{1 0}} \mathbf{0 . 1}$ | $\boldsymbol{\operatorname { l o g }}_{\mathbf{1 0}} \mathbf{1}$ | $\boldsymbol{\operatorname { l o g }}_{\mathbf{1 0}} \mathbf{1 0}$ | $\boldsymbol{\operatorname { l o g }}_{\mathbf{1 0}} \mathbf{1 0 0}$ | $\boldsymbol{\operatorname { l o g }}_{\mathbf{1 0}} \mathbf{1 0 0 0}$ |
| :--- | :--- | :--- | :--- | :--- | :--- |
| ..... | ..... | 0 | 1 | ..... | ..... |

![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-027_350_366_1115_1669.jpg)

<a id="ch02-we-2.1"></a>
#### WORKED EXAMPLE 2.1

**a** Convert $10^{x}=58$ to logarithmic form.

**b** Solve $10^{x}=58$ giving your answer correct to 3 significant figures.

Answer

**a** Method 1

$$
10^{x}=58
$$

Step 1: Identify the base and index ⟶ base $=10$, index $=x$

Step 2: Start to write in $\log$ form $\longrightarrow x=\log _{10}$ ?

Step 3: Complete the $\log$ form $\longrightarrow x=\log _{10} 58$

$$
10^{x}=58 \Leftrightarrow x=\log _{10} 58
$$

Method 2

$$
10^{x}=58
$$

$$
\begin{align}
\log _{10} 10^{x} & =\log _{10} 58 \\
x & =\log _{10} 58
\end{align}
$$

**b**

$$
\begin{align}
10^{x} & =58 \\
x & =\log _{10} 58 \\
x & \approx 1.76
\end{align}
$$

<a id="ch02-we-2.2"></a>
#### WORKED EXAMPLE 2.2

**a** Convert $\log _{10} x=3.5$ to exponential form.

**b** Solve $\log _{10} x=3.5$ giving your answer correct to 3 significant figures.

Answer

**a** Method 1

$$
\log _{10} x=3.5
$$

Step 1: Identify the base and index ⟶ base = 10 , index = 3.5

Step 2: Start to write in exponential form $\longrightarrow 10^{3.5}=$ ?

Step 3: Complete the exponential form ⟶ X = $10^{3.5}$ $\log _{10} x=3.5 \Leftrightarrow x=10^{3.5}$

Method 2

$$
\begin{align}
\log _{10} x & =3.5 \\
10^{\log _{10} x} & =10^{3.5} \\
x & =10^{3.5}
\end{align}
$$

Write each side as an exponent of 10.

Use $10^{\log _{10} x}=x$.

**b**

$$
\begin{align}
\log _{10} x & =3.5 \\
x & =10^{3.5} \\
x & \approx 3160
\end{align}
$$

<a id="ch02-we-2.3"></a>
#### WORKED EXAMPLE 2.3

Find the value of:

**a** $\quad \log _{10} 10000$

**b** $\quad \log _{10} 0.0001$

**c** $\quad \log _{10} 1000 \sqrt{10}$.

Answer

**a**

$$
\begin{align}
\log _{10} 10000 & =\log _{10} 10^{4} \\
& =4
\end{align}
$$

**b**

$$
\begin{align}
\log _{10} 0.0001 & =\log _{10} 10^{-4} \\
& =-4
\end{align}
$$

**c**

$$
\begin{align}
\log _{10} 1000 \sqrt{10} & =\log _{10} 10^{3.5} \qquad Q \frac{W r i t e}{} 1000 \sqrt{10} \text { as a power of } 10 . \\
& =3.5
\end{align}
$$

<a id="ch02-ex2A"></a>
### EXERCISE 2A

<a id="ch02-ex2A-q1"></a>
##### Question 1
Convert from exponential form to logarithmic form.

**a** $\quad 10^{2}=100$

**b** $\quad 10^{x}=200$

**c** $\quad 10^{x}=0.05$

<a id="ch02-ex2A-q2"></a>
##### Question 2
Solve each of these equations, giving your answers correct to 3 significant figures.

**a** $10^{x}=52$

**b** $10^{x}=250$

**c** $\quad 10^{x}=0.48$

<a id="ch02-ex2A-q3"></a>
##### Question 3
Convert from logarithmic form to exponential form.

**a** $\quad \log _{10} 10000=4$

**b** $\quad \log _{10} x=1.2$

**c** $\quad \log _{10} x=-0.6$

<a id="ch02-ex2A-q4"></a>
##### Question 4
Solve each of these equations, giving your answers correct to 3 significant figures.

**a** $\quad \log _{10} x=1.88$

**b** $\log _{10} x=2.76$

**c** $\quad \log _{10} x=-1.4$

<a id="ch02-ex2A-q5"></a>
##### Question 4
Without using a calculator, find the value of:

**a** $\quad \log _{10}100$
**b** $\quad \log _{10}0.0001$
**c** $\quad \log _{10}(10 \sqrt{10})$
**d** $\quad \log _{10}(\sqrt[3]{10})$
**e** $\quad \log _{10}(100 \sqrt[3]{10})$
**f** $\quad \log _{10}\left( \frac{100}{\sqrt{1000}} \right)$



<a id="ch02-ex2A-q6"></a>
##### Question 6
Given that the function f is defined as f : $x \mapsto 10^{x}-3$ for $x \in \mathbb{R}$, find an expression for $\mathrm{f}^{-1}(x)$.

<a id="ch02-ex2A-q7"></a>
##### Question 7
Given that $p$ and $q$ are positive and that $4\left(\log _{10} p\right)^{2}+2\left(\log _{10} q\right)^{2}=9$, find the greatest possible value of $p$.

## 2.2 Logarithms to base $\boldsymbol{a}$

In the last section you learnt about logarithms to the base of 10.

The same principles can be applied to define logarithms in other bases.

<a id="ch02-kp-2.2"></a>
#### KEY POINT 2.2

If $y=a^{x}$ then $x=\log _{a} y$

$$
\begin{array}{ll} \log _{a} a=1 & \log _{a} 1=0 \\
\log _{a} a^{x}=x & a^{\log _{a} x}=x \end{array}
$$

The conditions for $\log _{a} x$ to be defined are:

- $a>0$ and $a \neq 1$

- $x>0$

We say that $y=a^{x} \Leftrightarrow x=\log _{a} y$.

<a id="ch02-we-2.4"></a>
#### WORKED EXAMPLE 2.4

Convert $5^{3}=125$ to logarithmic form.

Answer

Method 1

$$
5^{3}=125
$$

Step 1: Identify the base and index ⟶ base = 5, index = 3

Step 2: Start to write in $\log$ form $\longrightarrow 3=\log _{5}$ ?

Step 3: Complete the $\log$ form $\quad \longrightarrow \quad 3=\log _{5} 125$

$$
5^{3}=125 \Leftrightarrow 3=\log _{5} 125
$$

Method 2

$$
5^{3}=125
$$

$$
\begin{align}
\log _{5} 5^{3} & =\log _{5} 125 \\
3 & =\log _{5} 125
\end{align}
$$

<a id="ch02-we-2.5"></a>
#### WORKED EXAMPLE 2.5

Convert $\log _{3} x=2.5$ to exponential form.

Answer

Method 1

$$
\log _{3} x=2.5
$$

Step 1: Identify the base and index $\longrightarrow \quad$ base $=3$, index $=2.5$ Step 2: Start to write in exponential form $\longrightarrow 3^{2.5}=$ ?

Step 3: Complete the exponential form $\longrightarrow 3^{2.5}=x$

$$
\log _{3} x=2.5 \Leftrightarrow 3^{2.5}=x
$$

Method 2

$$
\begin{align}
\log _{3} x & =2.5 \\
3^{\log _{3} x} & =3^{2.5} \\
x & =3^{2.5}
\end{align}
$$

<a id="ch02-we-2.6"></a>
#### WORKED EXAMPLE 2.6

Find the value of:

**a** $\log _{2} 16$

**b** $\quad \log _{3} \frac{1}{9}$

Answer

**a**

$$
\begin{align}
\log _{2} 16 & =\log _{2} 2^{4} \\
& =4
\end{align}
$$

**b**

$$
\begin{align}
\log _{3} \frac{1}{9} & =\log _{3} 3^{-2} \\
& =-2
\end{align}
$$

<a id="ch02-we-2.7"></a>
#### WORKED EXAMPLE 2.7

Simplify $\log _{x}\left(\frac{\sqrt[3]{x}}{x}\right)$.

Answer

$$
\begin{align}
\log _{x}\left(\frac{\sqrt[3]{x}}{x}\right) & =\log _{x}\left(x^{-\frac{2}{3}}\right) \\
& =-\frac{2}{3}
\end{align}
$$

<a id="ch02-ex2B"></a>
### EXERCISE 2B

<a id="ch02-ex2B-q1"></a>
##### Question 1
Convert from exponential form to logarithmic form.

**a** $5^{2}=25$

**b** $2^{4}=16$

**c** $\quad 3^{-5}=\frac{1}{243}$

**d** $\quad 2^{-10}=\frac{1}{1024}$

**e** $8^{x}=15$

**f** $\quad x^{y}=6$

**g** $a^{b}=c$

**h** $x^{5 y}=7$

<a id="ch02-ex2B-q2"></a>
##### Question 2
Convert from logarithmic form to exponential form.

**a** $\log _{2} 8=3$

**b** $\quad \log _{3} 81=4$

**c** $\quad \log _{8} 1=0$

**d** $\quad \log _{16} 4=\frac{1}{2}$

**e** $\log _{8} 2=\frac{1}{3}$

**f** $\log _{2} y=4$

**g** $\log _{a} 1=0$

**h** $\log _{x} 5=y$

<a id="ch02-ex2B-q3"></a>
##### Question 3
Solve.

**a** $\log _{2} x=3$

**b** $\log _{3} x=2$

**c** $\quad \log _{4} x=0$

**d** $\quad \log _{x} 49=2$

<a id="ch02-ex2B-q4"></a>
##### Question 4
Solve.

**a** $\log _{3}(x+5)=2$

**b** $\quad \log _{2}(3 x-1)=5$

**c** $\quad \log _{y}(7-2 x)=0$

<a id="ch02-ex2B-q5"></a>
##### Question 5
Find the value of:

**a** $\log _{3} 27$

**b** $\quad \log _{6} 36$

**c** $\log _{4} 2$

**d** $\quad \log _{2} 0.125$

**e** $\quad \log _{4}\left(\frac{1}{16}\right)$

**f** $\quad \log _{5}(5 \sqrt{5})$

**g** $\quad \log _{3}\left(\frac{\sqrt{3}}{3}\right)$

**h** $\quad \log _{7}\left(\frac{\sqrt[3]{7}}{7}\right)^{2}$

<a id="ch02-ex2B-q6"></a>
##### Question 6
Simplify.

**a** $\log _{x} x^{3}$

**b** $\log _{x} \sqrt[3]{x}$

**c** $\log _{x}\left(x^{2} \sqrt{x}\right)$

**d** $\quad \log _{x} \frac{1}{x^{4}}$

**e** $\quad \log _{x}\left(\frac{1}{x^{3}}\right)^{2}$

**f** $\quad \log _{x}\left(\sqrt{x^{5}}\right)$

**g** $\log _{x}\left(\frac{x}{\sqrt[3]{x}}\right)$

**h** $\quad \log _{x}\left(\frac{x^{2}}{\sqrt{x}}\right)^{3}$

<a id="ch02-ex2B-q7"></a>
##### Question 7
Given that the function f is defined as f : $x \mapsto 1+\log _{2}(x-3)$ for $x \in \mathbb{R}, x>3$, find an expression for $\mathrm{f}^{-1}(x)$.

<a id="ch02-ex2B-q8"></a>
##### Question 8
Solve.

**a** $\log _{2}\left(\log _{3} x\right)=-1$

**b** $\log _{4} 2^{3-5 x}=x^{2}$

<a id="ch02-ex2B-q9"></a>
##### Question 9

$$
\left(\log _{3} 9\right)
$$

$$
\log _{2} 8
$$

$$
\log _{3} 20
$$

$$
\log _{3} 4
$$

$$
\log _{2} 2
$$

$$
\log _{4} 3
$$

$$
\log _{2} 3
$$

Without using a calculator, arrange these logarithms in ascending order.

Add some more logarithms of your own in the correct position in your ordered list.

#### EXPLORE 2.2

**1** Prya and Hamish are asked what they think $\log _{10} 12+\log _{10} 4$ simplifies to.

Prya says that:

$$
\log _{10} 12+\log _{10} 4=\log _{10}(12+4)=\log _{10} 16
$$

Hamish says that: $\log _{10} 12+\log _{10} 4=\log _{10}(12 \times 4)=\log _{10} 48$

Use a calculator to see who is correct and check that their rule works for other pairs of numbers.

**2** Can you predict what $\log _{10} 12-\log _{10} 4$ simplifies to?

Use a calculator to check that you have predicted correctly and check for other pairs of numbers.

## 2.3 The laws of logarithms

If $x$ and $y$ are both positive and $a>0$ and $a \neq 1$, then the following laws of logarithms can be used.

<a id="ch02-kp-2.3"></a>
#### KEY POINT 2.3

| Multiplication law | Division law | Power law |
| :--- | :--- | :--- |
| $\log _{a}(x y)=\log _{a} x+\log _{a} y$ | $\log _{a}\left(\frac{x}{y}\right)=\log _{a} x-\log _{a} y$ | $\log _{a}(x)^{m}=m \log _{a} x$ |

Proofs:

| Multiplication law | Division law | Power law |
| :--- | :--- | :--- |
| $\begin{aligned} & \log _{a}(x y) \\ & =\log _{a}\left(a^{\log _{a} x} \times a^{\log _{a} y}\right) \\ & =\log _{a}\left(a^{\log _{a} x+\log _{a} y}\right) \\ & =\log _{a} x+\log _{a} y \end{aligned}$ | $\begin{aligned} & \log _{a}\left(\frac{x}{y}\right) \\ & =\log _{a}\left(\frac{a^{\log _{a} x}}{a^{\log _{a} y}}\right) \\ & =\log _{a}\left(a^{\log _{a} x-\log _{a} y}\right) \\ & =\log _{a} x-\log _{a} y \end{aligned}$ | $\begin{aligned} & \log _{a}(x)^{m} \\ & =\log _{a}\left(\left(a^{\log _{a} x}\right)^{m}\right) \\ & =\log _{a}\left(a^{m \log _{a} x}\right) \\ & =m \log _{a} x \end{aligned}$ |

$$
\text { Using the power law, }\begin{align}
\log _{a}\left(\frac{1}{x}\right) & =\log _{a} x^{-1} \\
& =-\log _{a} x
\end{align}
$$

Another useful rule to remember:

<a id="ch02-kp-2.4"></a>
#### KEY POINT 2.4

$$
\log _{a}\left(\frac{1}{x}\right)=-\log _{a} x
$$

<a id="ch02-we-2.8"></a>
#### WORKED EXAMPLE 2.8

Use the laws of logarithms to simplify these expressions.

**a** $\log _{2} 3+\log _{2} 5$

**b** $\log _{3} 8-\log _{3} 4$

**c** $2 \log _{5} 2+\log _{5} 3$

Answer

**a**

$$
\begin{gathered} \log _{2} 3+\log _{2} 5 \\
=\log _{2}(3 \times 5) \\
=\log _{2} 15 \end{gathered}
$$

**b**

$$
\begin{gathered} \log _{3} 8-\log _{3} 4 \\
=\log _{3}\left(\frac{8}{4}\right) \\
=\log _{3} 2 \end{gathered}
$$

**c**

$$
\begin{align}
& 2 \log _{5} 2+\log _{5} 3 \\
& =\log _{5} 2^{2}+\log _{5} 3 \\
& =\log _{5}(4 \times 3) \\
& =\log _{5} 12
\end{align}
$$

<a id="ch02-we-2.9"></a>
#### WORKED EXAMPLE 2.9

Given that $\log _{4} p=x$ and $\log _{4} q=y$, express in terms of $x$ and/or $y$

**a** $\log _{4} p^{5}-\log _{4} q^{2}$

**b** $\log _{4} \sqrt{p}+5 \log _{4} \sqrt[3]{q}$

**c** $\quad \log _{4}\left(\frac{64}{p}\right)$.

Answer

**a**

$$
\begin{align}
& \log _{4} p^{5}-\log _{4} q^{2} \\
& =5 \log _{4} p-2 \log _{4} q \\
& =5 x-2 y
\end{align}
$$

**b**

$$
\begin{align}
& \log _{4} \sqrt{p}+5 \log _{4} \sqrt[3]{q} \\
& =\frac{1}{2} \log _{4} p+\frac{5}{3} \log _{4} q \\
& =\frac{1}{2} x+\frac{5}{3} y
\end{align}
$$

**c**

$$
\begin{align}
& \log _{4}\left(\frac{64}{p}\right) \\
& =\log _{4} 4^{3}-\log _{4} p \\
& =3-x
\end{align}
$$

<a id="ch02-ex2C"></a>
### EXERCISE 2C

<a id="ch02-ex2C-q1"></a>
##### Question 1
Write as a single logarithm.

**a** $\log _{2} 7+\log _{2} 11$

**b** $\log _{6} 20-\log _{6} 4$

**c** $3 \log _{5} 2-\log _{5} 4$

**d** $2 \log _{3} 8-5 \log _{3} 2$

**e** $1+2 \log _{2} 3$

**f** $2-\log _{4} 2$

<a id="ch02-ex2C-q2"></a>
##### Question 2
Write as a single logarithm, then simplify your answer.

**a** $\log _{2} 40-\log _{2} 5$

**b** $\log _{6} 20+\log _{6} 5$

**c** $\quad \log _{2} 60-\log _{2} 5$

<a id="ch02-ex2C-q3"></a>
##### Question 3
Simplify.

**a** $3 \log _{5} 2+\frac{1}{2} \log _{5} 36-\log _{5} 12$

**b** $\frac{1}{2} \log _{3} 8+\frac{1}{2} \log _{3} 18-1$

<a id="ch02-ex2C-q4"></a>
##### Question 4
Express 8 and 0.25 as powers of 2 and hence simplify $\frac{\log _{5} 8}{\log _{5} 0.25}$.

<a id="ch02-ex2C-q5"></a>
##### Question 5
Simplify.

**a** $\frac{\log _{2} 27}{\log _{2} 3}$

**b** $\frac{\log _{3} 128}{\log _{3} 16}$

**c** $\frac{\log _{3} 25}{\log _{3} 0.04}$

**d** $\frac{\log _{5} 1000}{\log _{5} 0.01}$

<a id="ch02-ex2C-q6"></a>
##### Question 6
Given that $\log _{8} y=\log _{8}(x-2)-2 \log _{8} x$, express $y$ in terms of $x$.

<a id="ch02-ex2C-q7"></a>
##### Question 7
Given that $\log _{3}(z-1)-\log _{3} z=1+3 \log _{3} y$, express $z$ in terms of $y$.

<a id="ch02-ex2C-q8"></a>
##### Question 8
Given that $y=\log _{5} x$, find in terms of $y$ :

**a** $x$

**b** $\log _{5}(25 x)$

**c** $\quad \log _{5}\left(\frac{x \sqrt{x}}{125}\right)$

**d** $\log _{x} 125$

<a id="ch02-ex2C-q9"></a>
##### Question 9
Given that $x=\log _{4} p$ and $y=\log _{4} q$, express in terms of $x$ and/or $y$ :

**a** $\quad \log _{4}(64 p)$

**b** $\quad \log _{4}\left(\frac{2}{q}\right)$

**c** $p q$

**d** $\quad \log _{4} p^{2}-\log _{4}(4 \sqrt{q})$

<a id="ch02-ex2C-q10"></a>
##### Question 10
Given that $\log _{a} x=7$ and $\log _{a} y=4$, find the value of:

**a** $\quad \log _{a}\left(\frac{x}{y}\right)$

**b** $\log _{a}\left(\frac{\sqrt{x}}{y^{2}}\right)$

**c** $\log _{a}\left(x^{2} \sqrt{y}\right)$

**d** $\quad \log _{a}\left(\frac{y}{\sqrt[3]{x}}\right)$.

<a id="ch02-ex2C-q11"></a>
##### Question 11
![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-035_604_720_1435_371.jpg) The number in the rectangle on the side of the triangle is the sum of the numbers at the adjacent vertices.

For example, $x+y=-\log _{2} 5$.

Find the value of $x$, the value of $y$ and the value of $z$.

## 2.4 Solving logarithmic equations

We have already learnt how to solve simple logarithmic equations. In this section we will learn how to solve more complicated equations.

Since $\log _{a} x$ only exists for $x>0$ and for $a>0$ and $a \neq 1$, it is essential when solving equations involving logs that all roots are checked in the original equation.

<a id="ch02-we-2.10"></a>
#### WORKED EXAMPLE 2.10

Solve:

**a** $2 \log _{8}(x+2)=\log _{8}(2 x+19)$

**b** $4 \log _{x} 2-\log _{x} 4=2$

Answer

**a** $2 \log _{8}(x+2)=\log _{8}(2 x+19)$ Use the power law.

$$
\begin{align}
\log _{8}(x+2)^{2} & =\log _{8}(2 x+19) \\
(x+2)^{2} & =2 x+19 \\
x^{2}+4 x+4 & =2 x+19 \\
x^{2}+2 x-15 & =0 \\
(x-3)(x+5) & =0 \\
x=3 \text { or } x & =-5
\end{align}
$$

Check when $x=3: 2 \log _{8}(x+2)=2 \log _{8} 5=\log _{8} 25$ is defined

$$
\log _{8}(2 x+19)=\log _{8} 25 \text { is defined. }
$$

So $x=3$ is a solution, since both sides of the equation are defined and equivalent in value.

Check when $x=-5: 2 \log _{8}(x+2)=2 \log _{8}(-3)$ is not defined.

So $x=-5$ is not a solution of the original equation.

Hence, the solution is $x=3$

**b** $4 \log _{x} 2-\log _{x} 4=2$ Use the power law.

$$
\begin{align}
\log _{x} 2^{4}-\log _{x} 2^{2} & =2 \\
\log _{x} 2^{4-2} & =2 \\
\log _{x} 2^{2} & =2 \\
\log _{x} 4 & =2 \\
x^{2} & =4 \\
x & = \pm 2
\end{align}
$$

Since logarithms only exist for positive bases, $x=-2$ is not a solution.

Check when $x=2$ :

$$
\begin{align}
4 \log _{2} 2-\log _{2} 4 & =4-2 \log _{2} 2 \\
& =4-2 \\
& =2
\end{align}
$$

So $x=2$ satisfies the original equation.

Hence, the solution is $x=2$

<a id="ch02-ex2D"></a>
### EXERCISE 2D

<a id="ch02-ex2D-q1"></a>
##### Question 1
Solve.

**a** $\log _{5} x+\log _{5} 3=\log _{5} 30$

**b** $\quad \log _{3} 4 x-\log _{3} 2=\log _{3} 7$

**c** $\quad \log _{2}(2-x)+\log _{2} 9=2 \log _{2} 8$

**d** $\log _{10}(x-4)=2 \log _{10} 5+\log _{10} 2$

<a id="ch02-ex2D-q2"></a>
##### Question 2
Solve.

**a** $\log _{10}(2 x+9)-\log _{10} 5=1$

**b** $\quad \log _{3} 2 x-\log _{3}(x-1)=2$

**c** $\quad \log _{2}(5-2 x)=3+\log _{2}(x+1)$

**d** $\quad \log _{5}(2 x-3)+2 \log _{5} 2=1+\log _{5}(3-2 x)$

<a id="ch02-ex2D-q3"></a>
##### Question 3
Solve.

**a** $\log _{2} x+\log _{2}(x-1)=\log _{2} 20$

**b** $\log _{5}(x-2)+\log _{5}(x-5)=\log _{5} 4 x$

**c** $2 \log _{3} x-\log _{3}(x-2)=2$

**d** $3+2 \log _{2} x=\log _{2}(3-10 x)$

<a id="ch02-ex2D-q4"></a>
##### Question 4
Solve.

**a** $\log _{x} 40-\log _{x} 5=1$

**b** $\log _{x} 36+\log _{x} 4=2$

**c** $\log _{x} 25-2 \log _{x} 3=2$

**d** $2 \log _{x} 32=3+2 \log _{x} 4$

<a id="ch02-ex2D-q5"></a>
##### Question 5
Solve.

**a** $\left(\log _{2} x\right)^{2}-8 \log _{2} x+15=0$

**b** $\left(\log _{10} x\right)^{2}-\log _{10}\left(x^{2}\right)=3$

**c** $\left(\log _{5} x\right)^{2}+\log _{5}\left(x^{3}\right)=10$

**d** $4\left(\log _{2} x\right)^{2}-2 \log _{2}\left(x^{2}\right)=3$

<a id="ch02-ex2D-q6"></a>
##### Question 6
Solve the simultaneous equations.

**a** $x y=81$

$$
\log _{x} y=3
$$

c $\quad \log _{4}(x-y)=2 \log _{4} x$

$$
\log _{4}(x+y+9)=0
$$

**b**

$$
\begin{align}
& 4^{x}=2^{y} \\
& 3 \log _{10} y=\log _{10} x+\log _{10} 2
\end{align}
$$

d

$$
\begin{align}
& \log _{10} x=2 \log _{10} y \\
& \log _{10}(2 x-17 y)=2
\end{align}
$$

<a id="ch02-ex2D-q7"></a>
##### Question 7
Given that $\log _{10}\left(x^{2} y\right)=4$ and $\log _{10}\left(\frac{x^{4}}{y^{3}}\right)=18$, find the value of $\log _{10} x$ and of $\log _{10} y$.

## 2.5 Solving exponential equations

At IGCSE / O Level you learnt how to solve exponential equations whose terms could be converted to the same base. In this section you will learn how to solve exponential equations whose terms cannot be converted to the same base.

<a id="ch02-we-2.11"></a>
#### WORKED EXAMPLE 2.11

Solve, giving your answers correct to 3 significant figures.

**a** $5^{2 x+1}=7$

**b** $3^{2 x}=4^{x+5}$

Answer

**a**

$$
\begin{align}
5^{2 x+1} & =7 \\
\log 5^{2 x+1} & =\log 7 \\
(2 x+1) \log 5 & =\log 7 \\
2 x \log 5+\log 5 & =\log 7
\end{align}
$$

**b**

$$
\begin{align}
3^{2 x} & =4^{x+5} \\
\log 3^{2 x} & =\log 4^{x+5} \\
2 x \log 3 & =(x+5) \log 4 \\
2 x \log 3 & =x \log 4+5 \log 4
\end{align}
$$

$$
x(2 \log 3-\log 4)=5 \log 4
$$

$$
\begin{align}
& x=\frac{5 \log 4}{2 \log 3-\log 4} \\
& x=8.55 \text { to } 3 \text { significant figures. }
\end{align}
$$

<a id="ch02-we-2.12"></a>
#### WORKED EXAMPLE 2.12

Solve the equation $2\left(3^{2 x}\right)+7\left(3^{x}\right)=15$, giving your answers correct to 3 significant figures.

Answer

$$
\begin{align}
2\left(3^{2 x}\right)+7\left(3^{x}\right)-15 & =0 \\
2 y^{2}+7 y-15 & =0 \\
(2 y-3)(y+5) & =0 \\
y=1.5 \text { or } y & =-5
\end{align}
$$

When $y=1.5$

$$
3^{x}=1.5 \quad \text { Take logs of both sides } .
$$

$$
\begin{align}
x \log 3 & =\log 1.5 \\
x & =\frac{\log 1.5}{\log 3}=0.369 \qquad
\end{align}
$$

When $y=-5$

$3^{x}=-5$

There are no solutions to this equation since $3^{x}$ is always positive.

Hence, the solution is $x=0.369$ to 3 significant figures.

<a id="ch02-ex2E"></a>
### EXERCISE 2E

<a id="ch02-ex2E-q1"></a>
##### Question 1
Solve, giving your answers correct to 3 significant figures.

**a** $5^{x}=18$

**b** $2^{x}=35$

**c** $3^{2 x}=8$

**d** $2^{x+1}=25$

**e** $3^{2 x-5}=20$

**f** $3^{x}=2^{x+1}$

**g** $5^{x+3}=7^{4-3 x}$

**h** $4^{1-3 x}=3^{x-2}$

**i** $2^{x}=2\left(5^{x}\right)$

**j** $4^{x}=7\left(3^{x}\right)$

**k** $2^{x+1}=3\left(5^{x}\right)$

**l** $5\left(2^{x-3}\right)=4\left(3^{x+4}\right)$

<a id="ch02-ex2E-q2"></a>
##### Question 2
**a** Show that $2^{x+1}+6\left(2^{x-1}\right)=12$ can be written as $2\left(2^{x}\right)+3\left(2^{x}\right)=12$.

**b** Hence solve the equation $2^{x+1}+6\left(2^{x-1}\right)=12$, giving your answer correct to 3 significant figures.

<a id="ch02-ex2E-q3"></a>
##### Question 3
Solve, giving your answers correct to 3 significant figures.

**a** $2^{x+2}+2^{x}=2^{2}$

**b** $3^{x+1}=3^{x-1}+3^{2}$

**c** $2^{x+1}+5\left(2^{x-1}\right)=2^{4}$

**d** $5^{x}+5^{3}=5^{x+2}$

**e** $4^{x-1}=4^{x}-4^{3}$

**f** $3^{x+1}-2\left(3^{x-2}\right)=5$

<a id="ch02-ex2E-q4"></a>
##### Question 4
Use the substitution $y=2^{x}$ to solve the equation $2^{2 x}+32=12\left(2^{x}\right)$.

<a id="ch02-ex2E-q5"></a>
##### Question 5
Solve, giving your answers correct to 3 significant figures.

**a** $5^{2 x}-5\left(5^{x}\right)+6=0$

**b** $2^{2 x}+5=6 \times 2^{x}$

**c** $3^{2 x}=6 \times 3^{x}+7$

**d** $4^{2 x}+27=12\left(4^{x}\right)$

<a id="ch02-ex2E-q6"></a>
##### Question 6
Use the substitution $u=2^{x}$ to solve the equation $2^{2 x}-5\left(2^{x+1}\right)+24=0$.

<a id="ch02-ex2E-q7"></a>
##### Question 7
Solve, giving your answers correct to 3 significant figures.

**a** $2^{2 x}-2^{x+1}-35=0$

**b** $3^{2 x}-3^{x+1}=10$

**c** $2\left(5^{x+1}\right)-5^{2 x}=16$

**d** $4^{2 x+1}=17\left(4^{x}\right)-15$

<a id="ch02-ex2E-q8"></a>
##### Question 8
Solve, giving your answers correct to 3 significant figures.

**a** $4^{x}+2^{x}-12=0$

**b** $3\left(16^{x}\right)-10\left(4^{x}\right)+3=0$

**c** $4^{x}+15=4\left(2^{x+1}\right)$

**d** $2\left(9^{x}\right)=3^{x+1}+27$

<a id="ch02-ex2E-q9"></a>
##### Question 9
For each of the following equations find the value of $\frac{x}{y}$ correct to 3 significant figures.

**a** $3^{x}=7^{y}$

**b** $7^{x}=(2.7)^{y}$

**c** $4^{2 x}=3^{5 y}$

<a id="ch02-ex2E-q10"></a>
##### Question 10
Solve the equation $x^{2.5}=20 x^{1.25}$, giving your answers in exact form.

<a id="ch02-ex2E-q11"></a>
##### Question 11
Solve, giving your answers correct to 3 significant figures.

**a** $\left|4^{x}-8\right|=2$

**b** $\left|2\left(3^{x}\right)-4\right|=8$

**c** $3\left|2^{x}-5\right|=2^{x}$

**d** $\left|3^{x}+4\right|=\left|3^{x}-9\right|$

**e** $\left|5\left(2^{x}\right)+3\right|=\left|5\left(2^{x}\right)-10\right|$

**f** $\left|2^{x+2}+1\right|=\left|2^{x}+12\right|$

**g** $3^{|x|}=6\left(3^{|x|}\right)+16$

**h** $\quad 4^{|x|}=5\left(2^{|x|}\right)+14$

<a id="ch02-ex2E-q12"></a>
##### Question 12
Given that $2^{4 x+1} \times 3^{2-x}=8^{x} \times 3^{5-2 x}$, find the value of:

**a** $6^{x}$

**b** $x$

<a id="ch02-ex2E-q13"></a>
##### Question 13
Solve the equation $8\left(8^{x-1}-1\right)=7\left(4^{x}-2^{x+1}\right)$.

## 2.6 Solving exponential inequalities

To solve inequalities such as $2^{x}>3$ we take the logarithm of both sides of the inequality. We can take logarithms to any base but care must be taken with the inequality symbol when doing so.

- If the base of the logarithm is greater than 1 then the inequality symbol remains the same.

- If the base of the logarithm is between 0 and 1 then the inequality symbol must be reversed.

This is because $y=\log _{a} x$ is an increasing function if $a>1$ and it is a decreasing function when $0<a<1$.

Hence, when taking logarithms to base 10 of both sides of an inequality the inequality symbol is unchanged.

It is also important to remember that if we divide both sides of an inequality by a negative number then the inequality symbol must be reversed.

<a id="ch02-we-2.13"></a>
#### WORKED EXAMPLE 2.13

Solve the inequality $0.6^{x}<0.7$, giving your answer in terms of base 10 logarithms.

Answer

| $0.6^{x}<0.7$ | Take logs to base 10 of both sides, inequality symbol is unchanged. |
| :--- | :--- |
| $\log 0.6^{x}<\log 0.7$ | Use the power rule for logs. |
| $x \log 0.6<\log 0.7$ | Divide both sides by $\log _{10}$ 0.6. |
| $x>\frac{\log 0.7}{\log 0.6}$ $x>0.698 \text { (correct to } 3 \text { significant figures) }$ | $\log 0.6$ is negative so the inequality symbol is reversed. |

<a id="ch02-we-2.14"></a>
#### WORKED EXAMPLE 2.14

Solve the inequality $4 \times 3^{2 x-1}>5$, giving your answer in terms of base 10 logarithms.

Answer

| $4 \times 3^{2 x-1}>5$ | Divide both sides by 4 . |
| :--- | :--- |
| $3^{2 x-1}>\frac{5}{4}$ | Take logs to base 10 of both sides and use the power rule. |
| $(2 x-1) \log 3>\log \frac{5}{4}$ | Expand brackets. |
| $(2 \log 3) x-\log 3>\log \frac{5}{4}$ | Rearrange. |
| $\begin{aligned} & x>\frac{\log \frac{5}{4}+\log 3}{2 \log 3} \\ & x>\frac{\log \frac{15}{4}}{\log 9} \end{aligned}$ | Simplify. |

<a id="ch02-ex2F"></a>
### EXERCISE 2F

<a id="ch02-ex2F-q1"></a>
##### Question 1
Solve the inequalities, giving your answer in terms of base 10 logarithms.

**a** $2^{x}<5$

**b** $5^{x} \geqslant 7$

**c** $\left(\frac{2}{3}\right)^{x}>3$

**d** $0.8^{x}<0.3$

<a id="ch02-ex2F-q2"></a>
##### Question 2
Solve the inequalities, giving your answer in terms of base 10 logarithms.

**a** $8^{5-x}<10$

**b** $3^{2 x+5}>20$

**c** $2 \times 5^{2 x+1} \leqslant 3$

**d** $7 \times\left(\frac{5}{6}\right)^{3-x}>4$

<a id="ch02-ex2F-q3"></a>
##### Question 3
Solve $5^{x^{2}}>2^{x}$, giving your answer in terms of logarithms.

<a id="ch02-ex2F-q4"></a>
##### Question 4
Prove that the solution to the inequality $3^{2x -1} \times 2 ^{1 - 3x} \ge 5$ is $x \ge \frac{\log(\frac{15}{2})}{\log\left(\frac{9}{8}\right)}$.

<a id="ch02-ex2F-q5"></a>
##### Question 5
In this question you are not allowed to use a calculator.

You are given that $\log _{10} 4=0.60206$ correct to 5 decimal places and that $10^{0.206}<2$.

**a** Find the number of digits in the number $4^{100}$.

**b** Find the first digit in the number $4^{100}$.

## 2.7 Natural logarithms

There is another type of logarithm to a special base called e.

The number e is an irrational number and $\mathrm{e} \approx 2.718$.

The function $y=\mathrm{e}^{x}$ is called the natural exponential function.

Logarithms to the base of e are called natural logarithms.

$\ln x$ is used to represent $\log _{\mathrm{e}} x$.

<a id="ch02-kp-2.5"></a>
#### KEY POINT 2.5

If $y=\mathrm{e}^{x}$ then $x=\ln y$

![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-042_353_358_917_181.jpg)

The curve $y=\ln x$ is the reflection of $y=\mathrm{e}^{x}$ in the line $y=x$.

$y=\ln x$ and $y=\mathrm{e}^{x}$ are inverse functions.

All the rules of logarithms that we have learnt so far also apply for natural logarithms.

We say that $y=\mathrm{e}^{x} \Leftrightarrow x=\log _{\mathrm{e}} y$. DID YOU KNOW?

![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-042_440_363_1675_184.jpg)

The Scottish mathematician John Napier (1550-1617) is credited with the discovery of logarithms. His original studies involved logarithms to the base of $\frac{1}{\mathrm{e}}$.

#### DID YOU KNOW?

The number e is also known as Euler's number. It is named after Leonhard Euler (1707-1783), who devised the following formula for calculating the value of e:

$$
e=1+\frac{1}{1}+\frac{1}{1 \times 2}+\frac{1}{1 \times 2 \times 3}+\frac{1}{1 \times 2 \times 3 \times 4}+\frac{1}{1 \times 2 \times 3 \times 4 \times 5}+
$$

<a id="ch02-ex2G"></a>
### EXERCISE 2G

<a id="ch02-ex2G-q1"></a>
##### Question 1
Use a calculator to evaluate correct to 3 significant figures:

**a** $\mathrm{e}^{3}$

**b** $\mathrm{e}^{2.7}$

**c** $\mathrm{e}^{0.8}$

**d** $\mathrm{e}^{-2}$

<a id="ch02-ex2G-q2"></a>
##### Question 2
Use a calculator to evaluate correct to 3 significant figures:

**a** $\ln 3$

**b** $\ln 1.4$

**c** $\ln 0.9$

**d** $\ln 0.15$

<a id="ch02-ex2G-q3"></a>
##### Question 3
Without using a calculator, find the value of:

**a** $\mathrm{e}^{\ln 2}$

**b** $\mathrm{e}^{\frac{1}{2} \ln 9}$

**c** $5 \mathrm{e}^{\ln 6}$

**d** $\mathrm{e}^{-\ln \frac{1}{2}}$

<a id="ch02-ex2G-q4"></a>
##### Question 4
Solve.

**a** $\mathrm{e}^{\ln x}=5$

**b** $\quad \ln \mathrm{e}^{x}=15$

**c** $\mathrm{e}^{3 \ln x}=64$

**d** $\quad \mathrm{e}^{-\ln x}=3$

<a id="ch02-ex2G-q5"></a>
##### Question 5
Solve, giving your answers correct to 3 significant figures.

**a** $\mathrm{e}^{x}=18$

**b** $\mathrm{e}^{2 x}=25$

**c** $\mathrm{e}^{x+1}=8$

**d** $\mathrm{e}^{2 x-3}=16$

<a id="ch02-ex2G-q6"></a>
##### Question 6
Solve, giving your answers in terms of natural logarithms.

**a** $\mathrm{e}^{x}=13$

**b** $\quad \mathrm{e}^{3 x}=7$

**c** $\mathrm{e}^{2 x-1}=6$

**d** $\mathrm{e}^{\frac{1}{2} x+3}=4$

<a id="ch02-ex2G-q7"></a>
##### Question 7
Solve, giving your answers in terms of natural logarithms.

**a** $\mathrm{e}^{x}>10$

**b** $\mathrm{e}^{5 x-2} \leqslant 35$

**c** $5 \times \mathrm{e}^{2 x+3}<1$

<a id="ch02-ex2G-q8"></a>
##### Question 8
Solve, giving your answers correct to 3 significant figures.

**a** $\ln x=5$

**b** $\ln x=-4$

**c** $\ln (x-2)=6$

**d** $\quad \ln (2 x+1)=-2$

<a id="ch02-ex2G-q9"></a>
##### Question 9
Solve, giving your answers correct to 3 significant figures.

**a** $\quad \ln \left(3-x^{2}\right)=2 \ln x$

**b** $2 \ln (x+2)-\ln x=\ln (2 x-1)$

**c** $2 \ln (x+1)=\ln (2 x+3)$

**d** $\ln (2 x+1)=2 \ln x+\ln 5$

**e** $\quad \ln (x+2)-\ln x=1$

**f** $\ln \left(2+x^{2}\right)=1+2 \ln x$

<a id="ch02-ex2G-q10"></a>
##### Question 10
Express $y$ in terms of $x$ for each of these equations.

**a** $2 \ln (y+1)-\ln y=\ln (x+y)$

**b** $\ln (y+2)-\ln y=1+2 \ln x$

<a id="ch02-ex2G-q11"></a>
##### Question 11
Solve, giving your answers in exact form.

**a** $\mathrm{e}^{2 x}+2 \mathrm{e}^{x}-15=0$

**b** $\mathrm{e}^{2 x}-5 \mathrm{e}^{x}+6=0$

**c** $6 \mathrm{e}^{2 x}-13 \mathrm{e}^{x}-5=0$

**d** $\mathrm{e}^{x}-21 \mathrm{e}^{-x}=4$

<a id="ch02-ex2G-q12"></a>
##### Question 12
Given that the function f is defined as $\mathrm{f}: x \mapsto 5 \mathrm{e}^{x}+2$ for $x \in \mathbb{R}$, find an expression for $\mathrm{f}^{-1}(x)$.

<a id="ch02-ex2G-q13"></a>
##### Question 13
Solve $2 \ln \left(3-\mathrm{e}^{2 x}\right)=1$, giving your answer correct to 3 significant figures.

<a id="ch02-ex2G-q14"></a>
##### Question 14
Solve the simultaneous equations, giving your answers in exact form.

**a**

$$
\begin{align}
& 2 \ln x+\ln y=1+\ln 5 \\
& \ln 10 x-\ln y=2+\ln 2
\end{align}
$$

**b**

$$
\begin{align}
& \mathrm{e}^{3 x+4 y}=2 \mathrm{e}^{2 x-y} \\
& \mathrm{e}^{2 x+y}=8 \mathrm{e}^{x+6 y}
\end{align}
$$

<a id="ch02-ex2G-q15"></a>
##### Question 15
Solve $\ln (2 x+1) \leqslant \ln (x+4)$.

### 2．8 Transforming a relationship to linear form

When we collect experimental data for two variables we often wish to find a mathematical relationship connecting the variables．When the data plots on a graph lie on a straight line the relationship can be easily found using the equation $y=m x+c$ ， where $m$ is the gradient and $c$ is the $y$－intercept．It is more common，however，for the data plots to lie on a curve．

Logarithms can be used to convert some curves into straight lines．

This is the case for relationships of the form $y=k x^{n}$ and $y=k\left(a^{x}\right)$ where $k, a$ and $n$ are constants．

Logarithms to any base can be used but it is more usual to use those that are most commonly available on calculators，which are natural logarithms or logarithms to the base 10.

<a id="ch02-we-2.15"></a>
#### WORKED EXAMPLE 2.15

Convert $y=a \mathrm{e}^{b x}$ ，where $a$ and $b$ are constants，into the form $Y=m X+c$ ．

Answer

$$
y=a \mathrm{e}^{b x}
$$

Taking natural logarithms of both sides gives：

$$
\begin{align}
& \ln y=\ln \left(a \mathrm{e}^{b x}\right) \\
& \ln y=\ln a+\ln \mathrm{e}^{b x} \\
& \ln y=\ln a+b x \\
& \ln y=b x+\ln a
\end{align}
$$

Now compare $\ln y=b x+\ln a$ with $Y=m X+c$ ：

$$
\begin{align}
& \underline{\ln y}=b \text { (X) }+\ln a \\
& \stackrel{\text { 十个 }}{\text { 十 }} \stackrel{\triangle}{\text { 十 }} \\
& Y=m X+c
\end{align}
$$

The non－linear equation $y=a \mathrm{e}^{b x}$ becomes the linear equation：

$$
Y=m X+c \text {, where } Y=\ln y, X=x, \quad m=b \text { and } c=\ln a
$$

It is important to note：

－The variables $X$ and $Y$ in $Y=m X+c$ must contain only the original variables $x$ and $y$ ． （They must not contain the unknown constants $a$ and $b$ ．） －The constants $m$ and $c$ must contain only the original unknown constants $a$ and $b$ ．（They must not contain the variables $x$ and $y$ ．）

<a id="ch02-we-2.16"></a>
#### WORKED EXAMPLE 2.16

The variables $x$ and $y$ satisfy the equation $y=a\left(\mathrm{e}^{-b x^{2}}\right)$ ，where $a$ and $b$ are constants．The graph of $\ln y$ against $x^{2}$ is a straight line passing through the points（0．55，0．84）and（1．72，0．26）as shown in the diagram．

Find the value of $a$ and the value of $b$ correct to 2 decimal places．

![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-044_336_449_2306_1494.jpg)

Answer

$$
y=a \times \mathrm{e}^{-b x^{2}}
$$

Taking natural logarithms of both sides gives:

$$
\begin{align}
& \ln y=\ln \left(a \times \mathrm{e}^{-b x^{2}}\right) \\
& \ln y=\ln a+\ln \mathrm{e}^{-b x^{2}} \\
& \ln y=\ln a-b x^{2} \\
& \ln y=-b x^{2}+\ln a
\end{align}
$$

Now compare $\ln y=-b x^{2}+\ln a$ with $Y=m X+c$ :

$$
\begin{align}
\ln y & =-b\left(x^{2}\right)+\ln a \\
\stackrel{\boldsymbol{\Upsilon}}{\boldsymbol{\uparrow}} \stackrel{-}{\boldsymbol{\Upsilon}} & +\stackrel{\boldsymbol{\Upsilon}}{\boldsymbol{\uparrow}} \\
Y & =m X+c
\end{align}
$$

Gradient $=m=\frac{0.26-0.84}{1.72-0.55}=-0.4957$

$\therefore b=0.50$ to 2 decimal places

Using $Y=m X+c, X=0.55, Y=0.84$ and $m=-0.4957$

$$
\begin{align}
0.84 & =-0.4957 \qquad \times 0.55+c \\
c & =1.1126 \qquad \\
\therefore \ln a & =1.1126 \qquad \\
a & =\mathrm{e}^{1.1126 }
\end{align}
$$

Hence $a=3.04$ and $b=0.50$ to 2 decimal places.

<a id="ch02-we-2.17"></a>
#### WORKED EXAMPLE 2.17

| $x$ | 5 | 10 | 20 | 40 | 80 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| $y$ | 2593 | 1596 | 983 | 605 | 372 |

The table shows experimental values of the variables $x$ and $y$.

**a** By plotting a suitable straight-line graph, show that $x$ and $y$ are related by the equation $y=k \times x^{n}$, where $k$ and $n$ are constants.

**b** Use your graph to estimate the value of $k$ and the value of $n$.

Answer

**a**

$$
\begin{align}
y & =k \times x^{n} \\
\ln y & =\ln \left(k \times x^{n}\right) \\
\ln y & =\ln k+\ln x^{n} \\
\ln y & =n \ln x+\ln k
\end{align}
$$

Now compare $\ln y=n \ln x+\ln k$ with $Y=m X+c$ :

$$
\ln y=n(\ln x)+\ln k
$$

$$
\stackrel{\uparrow}{Y}=\stackrel{\uparrow}{m} \stackrel{\uparrow}{X}+\stackrel{\uparrow}{c}
$$

Hence the graph of $\ln y$ against $\ln x$ needs to be drawn where:

- gradient $=n$

- intercept on vertical axis $=\ln k$

Table of values is

| $\boldsymbol{\operatorname { l n }} \boldsymbol{x}$ | 1.61 | 2.30 | 3.00 | 3.69 | 4.38 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| $\ln y$ | 7.86 | 7.38 | 6.89 | 6.41 | 5.92 |

![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-046_521_566_926_770.jpg)

The points form an approximate straight line, so $x$ and $y$ are related by the equation $y=k \times x^{n}$.

**b** $n=$ gradient $\approx \frac{5.92-7.86}{4.38-1.61} \approx-0.70$ to 2 significant figures.

ln $k=$ intercept on vertical axis

$$
\begin{align}
\ln k & \approx 9 \\
k & \approx \mathrm{e}^{9} \\
k & \approx 8100 \text { to } 2 \text { significant figures. }
\end{align}
$$

#### DID YOU KNOW?

![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-046_302_401_2124_181.jpg)

The distributions of a diverse range of natural and man-made phenomena approximately follow the power law $y=a x^{b}$. These include the size of craters on the moon, avalanches, species extinction, body mass, income and populations of cities.

<a id="ch02-ex2H"></a>
### EXERCISE 2H

<a id="ch02-ex2H-q1"></a>
##### Question 1
Given that $a$ and $b$ are constants, use logarithms to change each of these non-linear equations into the form $Y=m X+c$. State what the variables $X$ and $Y$ and the constants $m$ and $c$ represent. (Note: there might be more than one method to do this.)

**a** $y=\mathrm{e}^{a x+b}$

**b** $y=10^{a x-b}$

**c** $y=a\left(x^{-b}\right)$

**d** $y=a\left(b^{x}\right)$

**e** $a=\mathrm{e}^{x^{2}+b y}$

**f** $x^{a} y^{b}=8$

**g** $\quad x a^{y}=b$

**h** $y=a\left(\mathrm{e}^{-b x}\right)$

<a id="ch02-ex2H-q2"></a>
##### Question 2
The variables $x$ and $y$ satisfy the equation $y=a \times x^{n}$, where $a$ and $n$ are constants. The graph of $\ln y$ against $\ln x$ is a straight line passing through the points (0.31, 4.02) and (1.83, 3.22) as shown in the diagram. Find the value of $a$ and the value of $n$ correct to 2 significant figures.

![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-047_343_419_697_1596.jpg)

<a id="ch02-ex2H-q3"></a>
##### Question 3
The variables $x$ and $y$ satisfy the equation $y=k \times \mathrm{e}^{n(x-2)}$, where $k$ and $n$ are constants. The graph of $\ln y$ against $x$ is a straight line passing through the points $(1,1.84)$ and (7, 4.33) as shown in the diagram. Find the value of $k$ and the value of $n$ correct to 2 significant figures.

![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-047_354_381_1057_1596.jpg)

<a id="ch02-ex2H-q4"></a>
##### Question 4
Variables $x$ and $y$ are related so that, when $\log _{10} y$ is plotted on the vertical axis and $x$ is plotted on the horizontal axis, a straight-line graph passing through the points $(2,5)$ and $(6,11)$ is obtained.

**a** Express $\log _{10} y$ in terms of $x$.

**b** Express $y$ in terms of $x$, giving your answer in the form $y=a \times 10^{b x}$.

<a id="ch02-ex2H-q5"></a>
##### Question 5
Variables $x$ and $y$ are related so that, when $\ln y$ is plotted on the vertical axis and $\ln x$ is plotted on the horizontal axis, a straight-line graph passing through the points $(2,4)$ and $(5,13)$ is obtained.

**a** Express $\ln y$ in terms of $x$.

**b** Express $y$ in terms of $x$.

<a id="ch02-ex2H-q6"></a>
##### Question 6
The variables $x$ and $y$ satisfy the equation $5^{2 y}=3^{2 x+1}$. By taking natural logarithms, show that the graph of $\ln y$ against $\ln x$ is a straight line, and find the exact value of the gradient of this line and state the coordinates of the point at which the line cuts the $y$-axis.

<a id="ch02-ex2H-q7"></a>
##### Question 7
The mass, $m$ grams, of a radioactive substance is given by the formula $m=m_{0} \mathrm{e}^{-k t}$, where $t$ is the time in days after the mass was first recorded and $m_{0}$ and $k$ are constants.

The table below shows experimental values of $t$ and $m$.

| $t$ | 10 | 20 | 30 | 40 | 50 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| $m$ | 40.9 | 33.5 | 27.4 | 22.5 | 18.4 |

**a** Draw the graph of $\ln m$ against $t$.

**b** Use your graph to estimate the value of $m_{0}$ and $k$.

**c** The half-life of a radioactive substance is the time it takes to decay to half of its original mass. Find the half-life of this radioactive substance.

<a id="ch02-ex2H-q8"></a>
##### Question 8
The temperature, $T^{\circ} \mathrm{C}$, of a hot drink, $t$ minutes after it is made, can be modelled by the equation $T=25+k \mathrm{e}^{-n t}$, where $k$ and $n$ are constants. The table below shows experimental values of $t$ and $T$.

| $t$ | 2 | 4 | 6 | 8 | 10 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| $T$ | 63.3 | 57.7 | 52.8 | 48.7 | 45.2 |

**a** Convert the equation to a form suitable for drawing a straight-line graph.

**b** Draw the straight-line graph and use it to estimate the value of $k$ and $n$.

**c** Estimate:

i the initial temperature of the drink

ii the time taken for the temperature to reach $28^{\circ} \mathrm{C}$ iii the room temperature.

### Checklist of learning and understanding

The rules of logarithms

- If $y=a^{x}$ then $x=\log _{a} y$.

- $\log _{a} a=1, \log _{a} 1=0, \log _{a} a^{x}=x, a^{\log _{a} x}=x$

- Product rule: $\log _{a}(x y)=\log _{a} x+\log _{a} y$

- Division rule: $\log _{a}\left(\frac{x}{y}\right)=\log _{a} x-\log _{a} y$

- Power rule: $\log _{a}(x)^{m}=m \log _{a} x$

- Special case of power rule: $\log _{a}\left(\frac{1}{x}\right)=-\log _{a} x$

Natural logarithms

- Logarithms to the base of e are called natural logarithms.

- $\mathrm{e} \approx 2.718$

- $\ln x$ is used to represent $\log _{\mathrm{e}} x$.

- If $y=\mathrm{e}^{x}$ then $x=\ln y$.

- All the rules of logarithms apply for natural logarithms.

![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-049_353_357_883_1218.jpg)

Transforming a relationship to linear form

- Logarithms can be used to convert relationships of the form $y=k x^{n}$ and $y=k\left(a^{x}\right)$, where $k, a$ and $n$ are constants, into straight lines of the form $Y=m X+c$, where $X$ and $Y$ are functions of $x$ and of $y$.

<a id="ch02-review"></a>
### END-OF-CHAPTER REVIEW EXERCISE 2

<a id="ch02-review-q1"></a>
##### Question 1
Solve the inequality $2^{x}>7$, giving your answer in terms of logarithms. `[2]`

<a id="ch02-review-q2"></a>
##### Question 2
Given that $\ln p=2 \ln q-\ln (3+q)$ and that $q>0$, express $p$ in terms of $q$ not involving logarithms. `[3]`

<a id="ch02-review-q3"></a>
##### Question 3
Solve the inequality $3 \times 2^{3 x+2}<8$, giving your answer in terms of logarithms. `[4]`

<a id="ch02-review-q4"></a>
##### Question 4
Use logarithms to solve the equation

$$
5^{x+3}=7^{x-1}
$$

giving the answer correct to 3 significant figures. `[4]`

*Cambridge International AS \& A Level Mathematics 9709 Paper 21 Q1 November 2015*

<a id="ch02-review-q5"></a>
##### Question 5
Solve the equation $6\left(4^{x}\right)-11\left(2^{x}\right)+4=0$, giving your answers for $x$ in terms of logarithms where appropriate. `[5]`

<a id="ch02-review-q6"></a>
##### Question 6
Solve the equation $\ln (5 x+4)=2 \ln x+\ln 6$. `[5]`

<a id="ch02-review-q7"></a>
##### Question 7
![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-050_360_684_1028_822.jpg) The variables $x$ and $y$ satisfy the equation $y=K x^{m}$, where $K$ and $m$ are constants. The graph of $\ln y$ against $\ln x$ is a straight line passing through the points (0, 2.0) and (6, 10.2), as shown in the diagram. Find the values of $K$ and $m$, correct to 2 decimal places. `[5]`

*Cambridge International AS \& A Level Mathematics 9709 Paper 21 Q3 June 2011*

<a id="ch02-review-q8"></a>
##### Question 8
**i** Given that $y=2^{x}$, show that the equation

$$
2^{x}+3\left(2^{-x}\right)=4
$$

can be written in the form

$$
y^{2}-4 y+3=0 .
$$

[3]

**ii** Hence solve the equation

$$
2^{x}+3\left(2^{-x}\right)=4,
$$

giving the values of $x$ correct to 3 significant figures where appropriate. `[3]`

*Cambridge International AS \& A Level Mathematics 9709 Paper 21 Q5 June 2010*

<a id="ch02-review-q9"></a>
##### Question 9
Given that $(1.2)^{x}=6^{y}$, use logarithms to find the value of $\frac{x}{y}$ correct to 3 significant figures. `[3]`

<a id="ch02-review-q10"></a>
##### Question 10
The polynomial $\mathrm{f}(x)$ is defined by

$$
f(x)=12 x^{3}+25 x^{2}-4 x-12 .
$$

**i** Show that $\mathrm{f}(-2)=0$ and factorise $\mathrm{f}(x)$ completely. `[4]`

**ii** Given that $12 \times 27^{y}+25 \times 9^{y}-4 \times 3^{y}-12=0$, state the value of $3^{y}$ and hence find $y$ correct to 3 significant figures. `[3]`

<a id="ch02-review-q11"></a>
##### Question 11
Solve the equation $\left|4-2^{x}\right|=10$, giving your answer correct to 3 significant figures. `[3]`

*Cambridge International A Level Mathematics 9709 Paper 31 Q1 June 2012*

<a id="ch02-review-q12"></a>
##### Question 12
Use logarithms to solve the equation $\mathrm{e}^{x}=3^{x-2}$, giving your answer correct to 3 decimal places. `[3]`

*Cambridge International A Level Mathematics 9709 Paper 31 Q1 November 2014*

<a id="ch02-review-q13"></a>
##### Question 13
Using the substitution $u=3^{x}$, solve the equation $3^{x}+3^{2 x}=3^{3 x}$ giving your answer correct to 3 significant figures. `[5]`

*Cambridge International A Level Mathematics 9709 Paper 31 Q2 November 2015*

<a id="ch02-review-q14"></a>
##### Question 14
The variables $x$ and $y$ satisfy the equation $5^{y}=3^{2 x-4}$.

**a** By taking natural logarithms, show that the graph of $y$ against $x$ is a straight line and find the exact value of the gradient of this line. `[3]`

**b** This line intersects the $x$-axis at $P$ and the $y$-axis at $Q$. Find the exact coordinates of the midpoint of $P Q$. `[3]`

<a id="ch02-review-q15"></a>
##### Question 15
![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-051_361_426_1121_995.jpg) The variables $x$ and $y$ satisfy the equation $y=K\left(b^{x}\right)$, where $K$ and $b$ are constants. The graph of $\ln y$ against $x$ is a straight line passing through the points (2.3,1.7) and (3.1,2.1), as shown in the diagram. Find the values of $K$ and $b$, correct to 2 decimal places. `[6]`
