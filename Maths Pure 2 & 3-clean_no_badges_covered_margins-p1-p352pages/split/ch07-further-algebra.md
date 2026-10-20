# Chapter 7: Further algebra

This chapter is for Pure Mathematics 3 students only.

In this chapter you will learn how to:

- recall an appropriate form for expressing rational functions in partial fractions, and carry out the decomposition, in cases where the denominator is no more complicated than:

- $(a x+b)(c x+d)(e x+f)$

- $(a x+b)(c x+d)^{2}$

- $(a x+b)\left(c x^{2}+d\right)$

- use the expansion of $(1+x)^{n}$, where $n$ is a rational number and $|x|<1$.

![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-165_573_1942_2202_136.jpg)

<a id="ch07-prerequisite"></a>
### PREREQUISITE KNOWLEDGE

| Where it comes from | What you should be able to do | Check your skills |
| :--- | :--- | :--- |
| Pure Mathematics 1 Coursebook, Chapter 6 | Equate coefficients of polynomials. | 1 Find the value of $A, B$ and $C$ for:<br>&#160;&#160;a $A x^{2}-3 x+C \equiv 6 x^{2}+B x-9$<br>&#160;&#160;b $(2-A) x^{2}+5 x+2 C \equiv 3 x^{2}-3 B x+8$<br> |
| Pure Mathematics 1 Coursebook, Chapter 6 | Expand $(a+b)^{n}$ where $n$ is a positive integer. | 2 Find the first 3 terms, in ascending powers of $x$, in the expansion of:<br><br>&#160;&#160;a $(1+2 x)^{7}$<br>&#160;&#160;b $(3-2 x)^{5}$<br> |
| Chapter 1 | Divide polynomials. | 3 Find the quotient and remainder when $x^{2}-8 x+4$ is divided by $x-3$. |

### Why do we study algebra?

At IGCSE / O Level we learnt how to add and subtract algebraic fractions. In this chapter we will learn how to do the 'reverse process'. This reverse process is often referred to as splitting a fraction into its partial fractions. In Mathematics it is often easier to deal with two or more simple fractions than it is to deal with one complicated fraction.

In the Pure Mathematics 1 Coursebook, Chapter 6, you learnt how to find the binomial expansion of $(a+b)^{n}$ for positive integer values of $n$. After working through this chapter you will be able to expand expressions of the form $(1+x)^{n}$ for values of $n$ that are not positive integers (providing $|x|<1$ ).

Combining your partial fraction and binomial expansion skills will enable you to obtain series expansions of complicated expressions such as $\frac{2 x-1}{2 x^{2}+3 x-20}$.

## 7.1 Improper algebraic fractions

A numerical improper fraction is defined as a fraction where the numerator $\geqslant$ the denominator. For example, $\frac{11}{5}$ is an improper fraction. This fraction can be expressed as $2+\frac{1}{5}$, which is the sum of a positive integer and a proper fraction.

So how do we define an algebraic improper fraction?

<a id="ch07-kp-7.1"></a>
#### KEY POINT 7.1

The algebraic fraction $\frac{\mathrm{P}(x)}{\mathrm{Q}(x)}$, where $\mathrm{P}(x)$ and $\mathrm{Q}(x)$ are polynomials in $x$, is said to be an algebraic improper fraction if the degree of $\mathrm{P}(x) \geqslant$ the degree of $\mathrm{Q}(x)$.

For example, the fraction $\frac{x^{3}-3 x^{2}+7}{x-2}$ is an improper algebraic fraction because the degree of the numerator (3) is greater than the degree of the denominator (1).

We can use long division to write the fraction $\frac{x^{3}-3 x^{2}+7}{x-2}$ as the sum of a polynomial and a proper algebraic fraction.

$$
\begin{align}
& x - 2 \longdiv { x ^ { 2 } - x - 2 } \\
& \frac{x^{3}-2 x^{2}+0 x+7}{-x^{2}+0 x} \\
& \frac{-x^{2}+2 x}{-2 x+7} \\
& \frac{-2 x+4}{3} \\
& \therefore \frac{x^{3}-3 x^{2}+7}{x-2}=x^{2}-x-2+\frac{3}{x-2}
\end{align}
$$

#### EXPLORE 7.1

**1** Discuss with your classmates which of the following are improper algebraic fractions.

![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-167_281_1112_1236_308.jpg)

**2** Write each improper fraction in question 1 as the sum of a polynomial and a proper fraction.

<a id="ch07-ex7A"></a>
### EXERCISE 7A

<a id="ch07-ex7A-q1"></a>
##### Question 1
Express each of the following improper fractions as the sum of a polynomial and a proper fraction.

**a** $\frac{8 x}{2 x-5}$

**b** $\frac{6 x+1}{3 x+2}$

**c** $\frac{4 x^{3}-3}{2 x+1}$

**d** $\frac{x^{3}+4 x^{2}+3 x-1}{x^{2}+2 x+3}$

**e** $\frac{7 x^{3}+2 x^{2}-5 x+1}{x^{2}-5}$

**f** $\frac{x^{4}+2 x^{2}-5}{x^{2}+1}$

<a id="ch07-ex7A-q2"></a>
##### Question 2
Given that $\frac{x^{3}+x^{2}-7}{x-3} \equiv A x^{2}+B x+C+\frac{D}{x-3}$, find the values of $A, B, C$ and $D$.

<a id="ch07-ex7A-q3"></a>
##### Question 3
Given that $\frac{x^{4}+5 x^{2}-1}{x+1} \equiv A x^{3}+B x^{2}+C x+D+\frac{E}{x+1}$, find the values of $A, B, C, D$ and $E$.

<a id="ch07-ex7A-q4"></a>
##### Question 4
Given that $\frac{2 x^{4}+3 x^{3}+4 x^{2}+5 x+6}{x^{3}+2 x} \equiv A x+B+\frac{C x+D}{x^{3}+2 x}$, find the values of $A, B, C$ and $D$.

## 7.2 Partial fractions

At IGCSE / O Level, we learnt how to add and subtract algebraic fractions. The following table shows three different cases for addition of algebraic fractions.

| Case 1 | Case 2 | Case 3 |
| :--- | :--- | :--- |
| $\begin{aligned} & \frac{5}{x+3}+\frac{4}{x-2} \\ & =\frac{5(x-2)+4(x+3)}{(x+3)(x-2)} \\ & =\frac{9 x+12}{(x+3)(x-2)} \end{aligned}$ | $\begin{aligned} & \frac{3}{x+1}+\frac{2}{(x+1)^{2}} \\ & =\frac{3(x+1)+2}{(x+1)^{2}} \\ & =\frac{3 x+5}{(x+1)^{2}} \end{aligned}$ | $\begin{aligned} & \frac{2}{x-1}+\frac{3}{x^{2}+5} \\ & =\frac{2\left(x^{2}+5\right)+3(x-1)}{(x-1)\left(x^{2}+5\right)} \\ & =\frac{2 x^{2}+3 x+7}{(x-1)\left(x^{2}+5\right)} \end{aligned}$ |
| Denominator in answer has: two distinct linear factors. | Denominator in answer has: one linear repeated factor. | Denominator in answer has: one linear factor and one quadratic factor. |

In this section we will learn how to do the reverse of this process. We will learn how to split (or decompose) a single algebraic fraction into two or more partial fractions.

### Case 1: Proper fraction where the denominator has distinct linear factors

If the denominator of a proper algebraic fraction has two distinct linear factors, the fraction can be split into partial fractions.

<a id="ch07-kp-7.2"></a>
#### KEY POINT 7.2

$$
\frac{p x+q}{(a x+b)(c x+d)} \equiv \frac{A}{a x+b}+\frac{B}{c x+d}
$$

This rule can be extended for 3 or more linear factors.

<a id="ch07-kp-7.3"></a>
#### KEY POINT 7.3

$$
\frac{p x+q}{(a x+b)(c x+d)(e x+f)} \equiv \frac{A}{a x+b}+\frac{B}{c x+d}+\frac{C}{e x+f}
$$

<a id="ch07-we-7.1"></a>
#### WORKED EXAMPLE 7.1

Express $\frac{2 x-13}{(2 x+1)(x-3)}$ in partial fractions.

Answer

$$
\begin{align}
\frac{2 x-13}{(2 x+1)(x-3)} & \equiv \frac{A}{2 x+1}+\frac{B}{x-3} \qquad \text { Multiply throughout by }(2 x+1)(x-3) . \\
2 x-13 & \equiv A(x-3)+B(2 x+1) \qquad \tag{1}
\end{align}
$$

Method 1: Choose appropriate values for $x$.

Let $x=3$ in equation (1):

$$
\begin{align}
2(3)-13 & =A(3-3)+B(6+1) \\
-7 & =7 B \\
B & =-1
\end{align}
$$

Let $x=-\frac{1}{2}$ in equation (1):

$$
\begin{align}
2\left(-\frac{1}{2}\right)-13 & =A\left(-\frac{1}{2}-3\right)+B(-1+1) \\
-14 & =-\frac{7}{2} A \\
A & =4
\end{align}
$$

$$
\therefore \frac{2 x-13}{(2 x+1)(x-3)} \equiv \frac{4}{2 x+1}-\frac{1}{x-3}
$$

Method 2: Equating coefficients.

$$
\begin{align}
& 2 x-13 \equiv A(x-3)+B(2 x+1) \\
& 2 x-13 \equiv(A+2 B) x-3 A+B
\end{align}
$$

$$
\begin{align}
& A+2 B=2-\qquad \tag{2} \\
& -3 A+B=-13 \tag{3} \\
& A=4, B=-1 \\
& \therefore \frac{2 x-13}{(2 x+1)(x-3)} \equiv \frac{4}{2 x+1}-\frac{1}{x-3}
\end{align}
$$

### Case 2: Proper fraction with repeated linear factor in the denominator

If the denominator has a repeated linear factor, the fraction can be split into partial fractions using the rule:

<a id="ch07-kp-7.4"></a>
#### KEY POINT 7.4

$$
\frac{p x+q}{(a x+b)^{2}} \equiv \frac{A}{a x+b}+\frac{B}{(a x+b)^{2}}
$$

<a id="ch07-we-7.2"></a>
#### WORKED EXAMPLE 7.2

Express $\frac{2 x-11}{(x-4)^{2}}$ in partial fractions.

Answer

$$
\begin{align}
\frac{2 x-11}{(x-4)^{2}} & \equiv \frac{A}{x-4}+\frac{B}{(x-4)^{2}} \\
2 x-11 & \equiv A(x-4)+B \tag{1}
\end{align}
$$

Let $x=4$ in equation (1):

$$
\begin{align}
2(4)-11 & =A(4-4)+B \\
B & =-3
\end{align}
$$

Let $x=0$ in equation (1):

$$
\begin{align}
2(0)-11 & =A(0-4)-3 \\
A & =2 \\
\therefore \frac{2 x-11}{(x-4)^{2}} & \equiv \frac{2}{x-4}-\frac{3}{(x-4)^{2}}
\end{align}
$$

<a id="ch07-we-7.3"></a>
#### WORKED EXAMPLE 7.3

Express $\frac{1-9 x-8 x^{2}}{(x-2)(2 x+3)^{2}}$ in partial fractions.

Answer

$$
\begin{align}
\frac{1-9 x-8 x^{2}}{(x-2)(2 x+3)^{2}} & \equiv \frac{A}{x-2}+\frac{B}{2 x+3}+\frac{C}{(2 x+3)^{2}} \qquad \infty \qquad \text { Multiply throughout by }(x-2)(2 x+3)^{2} . \\
1-9 x-8 x^{2} & \equiv A(2 x+3)^{2}+B(x-2)(2 x+3)+C(x-2) \qquad (1) \tag{1}
\end{align}
$$

Let $x=2$ in equation (1):

$$
\begin{align}
1-9(2)-8(2)^{2} & =A(4+3)^{2}+B(2-2)(4+3)+C(2-2) \\
-49 & =49 A \\
A & =-1
\end{align}
$$

Let $x=-\frac{3}{2}$ in equation (1):

$$
\begin{align}
1-9\left(-\frac{3}{2}\right)-8\left(-\frac{3}{2}\right)^{2} & =A(-3+3)^{2}+B\left(-\frac{3}{2}-2\right)(-3+3)+C\left(-\frac{3}{2}-2\right) \\
-\frac{7}{2} & =-\frac{7}{2} C \\
C & =1
\end{align}
$$

Let $x=0$ in equation (1):

$$
\begin{equation*} 1=9 A-6 B-2 C \tag{2} \end{equation*}
$$

Substitute $A=-1$ and $C=1$ in equation (2).

$$
\begin{align}
& B=-2 \\
& \therefore \frac{1-9 x-8 x^{2}}{(x-2)(2 x+3)^{2}} \equiv-\frac{1}{x-2}-\frac{2}{2 x+3}+\frac{1}{(2 x+3)^{2}}
\end{align}
$$

### Case 3: Proper fraction with a quadratic factor in the denominator that cannot be factorised

In this syllabus you will only be asked questions where the quadratic factor is of the form $c x^{2}+d$.

If the denominator of a proper algebraic fraction has a quadratic factor of the form $c x^{2}+d$ that cannot be factorised, the fraction can be split into partial fractions using the following rule.

<a id="ch07-kp-7.5"></a>
#### KEY POINT 7.5

$$
\frac{p x+q}{(a x+b)\left(c x^{2}+d\right)} \equiv \frac{A}{a x+b}+\frac{B x+C}{c x^{2}+d}
$$

<a id="ch07-we-7.4"></a>
#### WORKED EXAMPLE 7.4

Express $\frac{8+2 x-x^{2}}{(x-1)\left(x^{2}+2\right)}$ in partial fractions.

Answer

$$
\begin{align}
\frac{8+2 x-x^{2}}{(x-1)\left(x^{2}+2\right)} & \equiv \frac{A}{x-1}+\frac{B x+C}{x^{2}+2} \\
8+2 x-x^{2} & \equiv A\left(x^{2}+2\right)+B x(x-1)+C(x-1) \qquad \text { Multiply throughout by }(x-1)\left(x^{2}+2\right) \tag{1}
\end{align}
$$

Let $x=1$ in equation (1):

$$
\begin{align}
8+2(1)-(1)^{2} & =A\left(1^{2}+2\right)+B(1)(1-1)+C(1-1) \\
9 & =3 A \\
A & =3
\end{align}
$$

Let $x=0$ in equation (1):

$$
\begin{align}
8 & =6-C \\
C & =-2
\end{align}
$$

Let $x=-1$ in equation (1):

$$
\begin{align}
5 & =9+2 B+4 \\
B & =-4
\end{align}
$$

$$
\therefore \frac{8+2 x-x^{2}}{(x-1)\left(x^{2}+2\right)} \equiv \frac{3}{x-1}+\frac{-4 x-2}{x^{2}+2} \equiv \frac{3}{x-1}-\frac{4 x+2}{x^{2}+2}
$$

### Case 4: Improper fractions

If an algebraic fraction is improper we must first express it as the sum of a polynomial and a proper fraction and then split the proper fraction into partial fractions.

<a id="ch07-we-7.5"></a>
#### WORKED EXAMPLE 7.5

Express $\frac{2 x^{2}+5 x-11}{x^{2}+2 x-3}$ in partial fractions.

Answer

The fraction is improper. Hence it must first be written as the sum of a polynomial and a proper fraction.

$$
\begin{gathered} x ^ { 2 } + 2 x - 3 \longdiv { 2 x ^ { 2 } + 5 x - 1 1 } \\
\frac{2 x^{2}+4 x-6}{x-5} \\
\frac{2 x^{2}+5 x-11}{x^{2}+2 x-3} \equiv 2+\frac{x-5}{x^{2}+2 x-3} \end{gathered}
$$

Split the proper fraction $\frac{x-5}{x^{2}+2 x-3}$ into partial fractions:

$$
\begin{align}
\frac{x-5}{(x+3)(x-1)} & \equiv \frac{A}{x+3}+\frac{B}{x-1} \\
x-5 & \equiv A(x-1)+B(x+3) \qquad \text { Multiply throughout by }(x+3)(x-1)
\end{align}
$$

(1)

Let $x=1$ in equation (1):

$$
\begin{align}
-4 & =4 B \\
B & =-1
\end{align}
$$

Let $x=-3$ in equation (1):

$$
\begin{align}
-8= & -4 A \\
A= & 2 \\
\frac{x-5}{(x+3)(x-1)} & \equiv \frac{2}{x+3}-\frac{1}{x-1} \\
\therefore \frac{2 x^{2}+5 x-11}{x^{2}+2 x-3} & \equiv 2+\frac{2}{x+3}-\frac{1}{x-1}
\end{align}
$$

Application of partial fractions

Partial fractions can be used to help evaluate the sum of some sequences.

<a id="ch07-we-7.6"></a>
#### WORKED EXAMPLE 7.6

Given that the algebraic fraction $\frac{1}{x(x+1)}$ can be written in partial fractions as $\frac{1}{x}-\frac{1}{x+1}$, find the sum of the first $n$ terms of the series $\frac{1}{1 \times 2}+\frac{1}{2 \times 3}+\frac{1}{3 \times 4}+\frac{1}{4 \times 5}+$. Hence, state the sum to infinity.

Answer

$$
\begin{align}
S_{n} & =\frac{1}{1 \times 2}+\frac{1}{2 \times 3}+\frac{1}{3 \times 4}+\frac{1}{4 \times 5}+\qquad +\frac{1}{(n-1) n}+\frac{1}{n(n+1)} \\
& =\left(\frac{1}{1}-\frac{1}{2}\right)+\left(\frac{1}{2}-\frac{1}{3}\right)+\left(\frac{1}{3}-\frac{1}{4}\right)+\left(\frac{1}{4}-\frac{1}{5}\right)+\qquad +\left(\frac{1}{n-1}-\frac{1}{n}\right)+\left(\frac{1}{n}-\frac{1}{n+1}\right) \\
& =1-\frac{1}{n+1}
\end{align}
$$

$$
\begin{align}
& \text { As } n \rightarrow \infty, \frac{1}{n+1} \rightarrow 0 \\
& \therefore S_{\infty}=1
\end{align}
$$

#### DID YOU KNOW?

The series in Worked example 7.6 is called a telescoping series, because its partial sums only have a fixed number of terms after cancellation.

<a id="ch07-ex7B"></a>
### EXERCISE 7B

<a id="ch07-ex7B-q1"></a>
##### Question 1
Express the following proper fractions as partial fractions.

**a** $\frac{6 x-2}{(x-2)(x+3)}$

**b** $\frac{7 x+12}{2 x(x-4)}$

**c** $\frac{15 x+13}{(x-1)(3 x+1)}$

**d** $\frac{x-1}{(3 x-5)(x-3)}$

**e** $\frac{6 x^{2}+5 x-2}{x(x-1)(2 x+1)}$

**f** $\frac{11 x+12}{(2 x+3)(x+2)(x-3)}$

<a id="ch07-ex7B-q2"></a>
##### Question 2
Express the following proper fractions as partial fractions.

**a** $\frac{2 x}{(x+2)^{2}}$

**b** $\frac{11 x^{2}+14 x+5}{(2 x+1)(x+1)^{2}}$

**c** $\frac{x^{2}-2}{x(x-1)^{2}}$

**d** $\frac{36 x^{2}+2 x-4}{(2 x-3)(2 x+1)^{2}}$

**e** $\frac{3}{(x+2)(x-2)^{2}}$

**f** $\frac{3 x+4}{(x+2)(x-1)^{2}}$

<a id="ch07-ex7B-q3"></a>
##### Question 3
Express the following proper fractions as partial fractions.

**a** $\frac{2 x^{2}-3 x+2}{x\left(x^{2}+1\right)}$

**b** $\frac{3 x^{2}+4 x+17}{(2 x+1)\left(x^{2}+5\right)}$

**c** $\frac{2 x^{2}-6 x-9}{(3 x+5)\left(2 x^{2}+1\right)}$

**d** $-\frac{6 x^{2}-21 x+50}{(3 x-5)\left(2 x^{2}+5\right)}$

<a id="ch07-ex7B-q4"></a>
##### Question 4
Express the following improper fractions as partial fractions.

**a** $\frac{2 x^{2}+3 x+4}{(x-1)(x+2)}$

**b** $\frac{x^{2}+3}{x^{2}-4}$

**c** $\frac{22-17 x+21 x^{2}-4 x^{3}}{(x-4)\left(x^{2}+1\right)}$

**d** $\frac{4 x^{3}+x^{2}-16 x+7}{2 x^{3}-4 x^{2}+2 x}$

<a id="ch07-ex7B-q5"></a>
##### Question 5
Find the values of $A, B, C$ and $D$ such that $\frac{4 x^{3}-9 x^{2}+11 x-4}{x^{2}(2 x-1)} \equiv A+\frac{B}{x}+\frac{C}{x^{2}}+\frac{D}{2 x-1}$.

<a id="ch07-ex7B-q6"></a>
##### Question 6
**a** Factorise $2 x^{3}-3 x^{2}-3 x+2$ completely.

**b** Hence express $\frac{x^{2}-13 x-5}{2 x^{3}-3 x^{2}-3 x+2}$ in partial fractions.

<a id="ch07-ex7B-q7"></a>
##### Question 7
**a** Factorise $2 x^{3}-11 x^{2}+12 x+9$ completely.

**b** Hence express $\frac{24-x}{2 x^{3}-11 x^{2}+12 x+9}$ in partial fractions.

<a id="ch07-ex7B-q8"></a>
##### Question 8
The polynomial $\mathrm{p}(x)=2 x^{3}+5 x^{2}+a x+b$ is exactly divisible by $2 x+1$ and leaves a remainder of 9 when divided by $x+2$.

**a** Find the value of $a$ and the value of $b$.

**b** Factorise $\mathrm{p}(x)$ completely.

**c** Express $\frac{120}{\mathrm{p}(x)}$ in partial fractions.

<a id="ch07-ex7B-q9"></a>
##### Question 9
**a** Express $\frac{2}{x(x+2)}$ in partial fractions.

**b** Find an expression for the sum of the first $n$ terms of the series:

$$
\frac{2}{1 \times 3}+\frac{2}{2 \times 4}+\frac{2}{3 \times 5}+\frac{2}{4 \times 6}+\frac{2}{5 \times 7}+
$$

**c** Find the sum to infinity of this series.

<a id="ch07-ex7B-q10"></a>
##### Question 10
Investigate whether the series $\frac{1}{1 \times 2 \times 3}+\frac{1}{2 \times 3 \times 4}+\frac{1}{3 \times 4 \times 5}+\frac{1}{4 \times 5 \times 6}+$ is a telescoping series. If it is a telescoping series, find an expression for the sum of the first $n$ terms and the sum to infinity.

#### EXPLORE 7.2

There is another method that can be used to decompose a proper algebraic fraction where the denominator contains only distinct linear factors. This alternative method is called Heaviside's cover-up method. Find out more about this method and use it to express $\frac{4 x^{2}+15 x+29}{(x-2)(x+1)(x+3)}$ in partial fractions.

## 7.3 Binomial expansion of $(\mathbf{1}+\boldsymbol{x})^{\boldsymbol{n}}$ for values of $\boldsymbol{n}$ that are not positive integers

#### REWIND

In the Pure Mathematics 1 Coursebook, Chapter 6, we learnt that the binomial expansion of $(1+x)^{n}$, where $n$ is a positive integer is:

$$
(1+x)^{n}=\binom{n}{0}+\binom{n}{1} x+\binom{n}{2} x^{2}+\binom{n}{3} x^{3}+\qquad +\binom{n}{n} x^{n}
$$

and that this terminating series can also be written in the form:

$$
(1+x)^{n}=1+n x+\frac{n(n-1)}{2!} x^{2}+\frac{n(n-1)(n-2)}{3!} x^{3}+\qquad +x^{n} .
$$

The general binomial theorem can be used for any rational value of $n$. It states that:

<a id="ch07-kp-7.6"></a>
#### KEY POINT 7.6

$$
(1+x)^{n}=1+n x+\frac{n(n-1)}{2!} x^{2}+\frac{n(n-1)(n-2)}{3!} x^{3}+\qquad \text { where } n \text { is rational and }|x|<1
$$

There are two very important differences when $n$ is not a positive integer. These are:

- the series is infinite

- the expansion is only valid for $|x|<1$.

The proof of the general binomial theorem is beyond the scope of this course.

Consider, however, the following two examples where $n$ is not a positive integer $\left(n=-3\right.$ and $\left.n=\frac{1}{2}\right)$.

$$
\begin{align}
(1+x)^{-3} & =1+(-3) x+\frac{(-3)(-4)}{2!} x^{2}+\frac{(-3)(-4)(-5)}{3!} x^{3}+\frac{(-3)(-4)(-5)(-6)}{4!} x^{4}+\qquad \\
& =1-3 x+6 x^{2}-10 x^{3}+15 x^{4}+\qquad \\
(1+x)^{\frac{1}{2}} & =1+\left(\frac{1}{2}\right) x+\frac{\left(\frac{1}{2}\right)\left(-\frac{1}{2}\right)}{2!} x^{2}+\frac{\left(\frac{1}{2}\right)\left(-\frac{1}{2}\right)\left(-\frac{3}{2}\right)}{3!} x^{3}+\frac{\left(\frac{1}{2}\right)\left(-\frac{1}{2}\right)\left(-\frac{3}{2}\right)\left(-\frac{5}{2}\right)}{4!} x^{4}+\qquad \\
& =1+\frac{1}{2} x-\frac{1}{8} x^{2}+\frac{1}{16} x^{3}-\frac{5}{128} x^{4}+\qquad
\end{align}
$$

We can see that in each case the sequence of coefficients forms an infinite sequence.

When $|x|<1$, the binomial series converges and has a sum to infinity (in a similar way to a geometric series converging for $|r|<1$, where $r$ is the common ratio).

<a id="ch07-we-7.7"></a>
#### WORKED EXAMPLE 7.7

Expand $(1-3 x)^{-2}$ in ascending powers of $x$ up to and including the term in $x^{3}$, and state the range of values of $x$ for which the expansion is valid.

Answer

Use $n=-2$ and replace $x$ by $-3 x$ in the binomial formula:

$$
\begin{align}
(1-3 x)^{-2} & =1+(-2)(-3 x)+\frac{(-2)(-3)}{2!}(-3 x)^{2}+\frac{(-2)(-3)(-4)}{3!}(-3 x)^{3}+\qquad \\
& =1+6 x+27 x^{2}+108 x^{3}+\qquad
\end{align}
$$

Expansion is valid for $|-3 x|<1$

$$
\therefore|x|<\frac{1}{3} .
$$

<a id="ch07-we-7.8"></a>
#### WORKED EXAMPLE 7.8

Find the first four terms in the expansion of $\left(1+2 x^{2}\right)^{-4}$ and state the range of values of $x$ for which the expansion is valid.

Answer

Use $n=-4$ and replace $x$ by $2 x^{2}$ in the binomial formula:

$$
\begin{align}
\left(1+2 x^{2}\right)^{-4} & =1+(-4)\left(2 x^{2}\right)+\frac{(-4)(-5)}{2!}\left(2 x^{2}\right)^{2}+\frac{(-4)(-5)(-6)}{3!}\left(2 x^{2}\right)^{3}+\qquad \\
& =1-8 x^{2}+40 x^{4}-160 x^{6}+\qquad
\end{align}
$$

Expansion is valid for $\left|2 x^{2}\right|<1$

$$
\therefore|x|<\frac{1}{\sqrt{2}}
$$

<a id="ch07-we-7.9"></a>
#### WORKED EXAMPLE 7.9

Find the coefficient of $x^{3}$ in the expansion of $\frac{x-5}{1+2 x}$.

Answer

$$
\frac{x-5}{1+2 x}=(x-5)(1+2 x)^{-1}
$$

Use $n=-1$ and replace $x$ by $2 x$ in the binomial formula:

$$
\begin{align}
(1+2 x)^{-1} & =1+(-1)(2 x)+\frac{(-1)(-2)}{2!}(2 x)^{2}+\frac{(-1)(-2)(-3)}{3!}(2 x)^{3}+\qquad \\
& =1-2 x+4 x^{2}-8 x^{3}+\qquad
\end{align}
$$

$$
\begin{align}
(x-5)(1+2 x)^{-1} & =(x-5)\left(1-2 x+4 x^{2}-8 x^{3}+\qquad \right) \\
& =x\left(1-2 x+4 x^{2}-8 x^{3}\right)-5\left(1-2 x+4 x^{2}-8 x^{3}+\qquad \right)
\end{align}
$$

Term in $x^{3}$ is $x\left(4 x^{2}\right)+(-5)\left(-8 x^{3}\right)=44 x^{3}$.

∴ The coefficient of $x^{3}$ is 44.

<a id="ch07-ex7C"></a>
### EXERCISE 7C

<a id="ch07-ex7C-q1"></a>
##### Question 1
Expand the following, in ascending powers of $x$, up to and including the term in $x^{3}$. State the range of values of $x$ for which each expansion is valid.

**a** $(1+x)^{-2}$

**b** $(1+3 x)^{-1}$

**c** $(1-2 x)^{-4}$

**d** $\left(1+\frac{x}{2}\right)^{-3}$

**e** $\sqrt{1+2 x}$

**f** $\sqrt[3]{1-3 x}$

**g** $\frac{2}{(1-4 x)^{2}}$

**h** $\frac{1-3 x}{(1+2 x)^{3}}$

**i** $\frac{1+x}{\sqrt{1-2 x}}$

<a id="ch07-ex7C-q2"></a>
##### Question 2
Find the first 3 terms, in ascending powers of $x$, in the expansion of each of the following expressions. State the range of values of $x$ for which each expansion is valid.

**a** $\left(1+x^{2}\right)^{-3}$

**b** $\sqrt[3]{1-2 x^{2}}$

**c** $\left(\sqrt{1-4 x^{2}}\right)^{3}$

<a id="ch07-ex7C-q3"></a>
##### Question 3
Find the first 5 terms, in ascending powers of $x$, in the expansion of $\frac{2+3 x}{\sqrt{1-5 x^{2}}}$.

<a id="ch07-ex7C-q4"></a>
##### Question 4
Can the binomial expansion be used to expand each of these expressions?

**a** $(3 x-1)^{-2}$

**b** $\sqrt{2 x-1}$

Give reasons for your answers.

<a id="ch07-ex7C-q5"></a>
##### Question 5
Expand $(2 x-1)^{-3}$ in ascending powers of $x$, up to and including the term in $x^{3}$.

<a id="ch07-ex7C-q6"></a>
##### Question 6
Show that the expansion of $(1+x)^{\frac{1}{2}}$ is not valid when $x=3$.

<a id="ch07-ex7C-q7"></a>
##### Question 7
Given that $(1-3 x)^{-4}-(1+2 x)^{\frac{3}{2}} \approx 9 x+k x^{2}$ for small values of $x$, find the value of the constant $k$.

<a id="ch07-ex7C-q8"></a>
##### Question 8
Given that $\frac{a}{1-x}+\frac{b}{1+2 x} \approx-3+12 x$ for small values of $x$, find the value of $a$ and the value of $b$.

<a id="ch07-ex7C-q9"></a>
##### Question 9
When $(1+a x)^{-3}$, where $a$ is a positive constant, is expanded the coefficients of $x$ and $x^{2}$ are equal.

**a** Find the value of $a$.

**b** When $a$ has this value, obtain the first 5 terms in the expansion.

<a id="ch07-ex7C-q10"></a>
##### Question 10
When $(3-2 x)(1+a x)^{\frac{2}{3}}$ is expanded the coefficient of $x^{2}$ is -15. Find the two possible values of $a$.

<a id="ch07-ex7C-q11"></a>
##### Question 11
The first 3 terms in the expansion of $(1+a x)^{n}$ are $1-24 x+384 x^{2}$.

**a** Find the value of $a$ and the value of $n$.

**b** Hence find the term in $x^{3}$.

## 7.4 Binomial expansion of $(\boldsymbol{a}+\boldsymbol{x})^{\boldsymbol{n}}$ for values of $\boldsymbol{n}$ that are not positive integers

To expand $(a+x)^{n}$, where $n$ is not a positive integer, we take $a$ outside of the brackets:

$$
(a+x)^{n}=a^{n}\left(1+\frac{x}{a}\right)^{n}
$$

Hence the expression is:

<a id="ch07-kp-7.7"></a>
#### KEY POINT 7.7

$$
(a+x)^{n}=a^{n}\left[1+n\left(\frac{x}{a}\right)+\frac{n(n-1)}{2!}\left(\frac{x}{a}\right)^{2}+\frac{n(n-1)(n-2)}{3!}\left(\frac{x}{a}\right)^{3}+\qquad \right] \text { for }\left|\frac{x}{a}\right|<1
$$

<a id="ch07-we-7.10"></a>
#### WORKED EXAMPLE 7.10

Expand $(2+x)^{-3}$ in ascending powers of $x$, up to and including the term in $x^{3}$ and state the range of values of $x$ for which the expansion is valid.

Answer

$$
\begin{align}
(2+x)^{-3} & =(2)^{-3}\left(1+\frac{x}{2}\right)^{-3} \\
& =(2)^{-3}\left[1+(-3)\left(\frac{x}{2}\right)+\frac{(-3)(-4)}{2!}\left(\frac{x}{2}\right)^{2}+\frac{(-3)(-4)(-5)}{3!}\left(\frac{x}{2}\right)^{3}+\qquad \quad \text { for }\left|\frac{x}{2}\right|<1\right. \\
& =\frac{1}{8}\left[1-\frac{3}{2} x+\frac{3}{2} x^{2}-\frac{5}{4} x^{3}+\qquad \right] \\
& =\frac{1}{8}-\frac{3}{16} x+\frac{3}{16} x^{2}-\frac{5}{32} x^{3}+\qquad \quad \text { valid for }|x|<2
\end{align}
$$

<a id="ch07-we-7.11"></a>
#### WORKED EXAMPLE 7.11

Find the coefficient of $x^{2}$ in the expansion of $\frac{1-3 x}{\sqrt{4-x}}$.

Answer

$$
\begin{align}
\frac{1-3 x}{\sqrt{4-x}} & =(1-3 x)(4-x)^{-\frac{1}{2}} \\
& =(1-3 x)(4)^{-\frac{1}{2}}\left(1-\frac{x}{4}\right)^{-\frac{1}{2}} \qquad \text { Factor the } 4 \text { out of }(4-x)^{-\frac{1}{2}} . \\
& =\frac{1}{2}(1-3 x)\left[1+\left(-\frac{1}{2}\right)\left(-\frac{x}{4}\right)+\frac{\left(-\frac{1}{2}\right)\left(-\frac{3}{2}\right)}{2!}\left(-\frac{x}{4}\right)^{2}+\qquad \right] \\
& =\frac{1}{2}(1-3 x)\left[1+\frac{1}{8} x+\frac{3}{128} x^{2}+\qquad \right] \\
& =\frac{1}{2}\left[1+\frac{1}{8} x+\frac{3}{128} x^{2}+\qquad \right]-\frac{3}{2} x\left[1+\frac{1}{8} x+\frac{3}{128} x^{2}+\qquad \right]
\end{align}
$$

Coefficient of $x^{2}$ is $\frac{1}{2} \times \frac{3}{128}-\frac{3}{2} \times \frac{1}{8}=-\frac{45}{256}$

<a id="ch07-ex7D"></a>
### EXERCISE 7D

<a id="ch07-ex7D-q1"></a>
##### Question 1
Expand the following, in ascending powers of $x$, up to and including the term in $x^{3}$. State the range of values of $x$ for which each expansion is valid.

**a** $(2+x)^{-2}$

**b** $(5-2 x)^{-1}$

**c** $\sqrt{9-x}$

**d** $\sqrt[3]{3 x+8}$

**e** $\frac{4}{(3-x)^{3}}$

**f** $\frac{1+2 x}{(2 x-5)^{3}}$

<a id="ch07-ex7D-q2"></a>
##### Question 2
Find the first 3 terms, in ascending powers of $x$, in the expansion of each of the following expressions. State the range of values of $x$ for which each expansion is valid.

**a** $\left(2+x^{2}\right)^{-2}$

**b** $\sqrt[3]{8-3 x^{2}}$

**c** $\left(\sqrt{3-x^{2}}\right)^{5}$

<a id="ch07-ex7D-q3"></a>
##### Question 3
Expand $(1-2 x) \sqrt[3]{8-2 x}$ in ascending powers of $x$, up to and including the term in $x^{3}$.

<a id="ch07-ex7D-q4"></a>
##### Question 4
**a** Expand $(2-x)^{-1}$ and $(1+3 x)^{-2}$ giving the first 3 terms in each expansion.

**b** Use your answers to part a to find the first 3 terms in the expansion of $(2-x)^{-1}(1+3 x)^{-2}$, stating the range of values of $x$ for which this expansion is valid.

<a id="ch07-ex7D-q5"></a>
##### Question 5
The first 3 terms in the expansion of $(a-5 x)^{-2}$ are $\frac{1}{4}+\frac{5}{4} x+b x^{2}$.

Find the value of $a$, the value of $b$ and the term in $x^{3}$.

<a id="ch07-ex7D-q6"></a>
##### Question 6
In the expansion of $\sqrt{3+a x}$ where $a \neq 0$, the coefficient of the term in $x^{2}$ is 3 times the coefficient of the term in $x^{3}$. Find the value of $a$.

<a id="ch07-ex7D-q7"></a>
##### Question 7
**a** Find the first 4 terms in the expansion of $\left(1+\frac{2}{x}\right)^{-1}$, where $\left|\frac{2}{x}\right|<1$.

**b** Show that $\left(1+\frac{2}{x}\right)^{-1} \equiv \frac{x}{x+2} \equiv \frac{x}{2}\left(1+\frac{x}{2}\right)^{-1}$.

**c** Find the first 4 terms in the expansion of $\frac{x}{2}\left(1+\frac{x}{2}\right)^{-1}$, where $\left|\frac{x}{2}\right|<1$.

**d** Explain why your expansions are different.

#### EXPLORE 7.3

**1** Given that $\mathrm{f}(x)=\frac{1}{(1+x)(1+2 x)}$, discuss why $\mathrm{f}(x)$ can be written in each of the following ways:

![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-179_242_588_977_633.jpg)

**2** Use the binomial theorem to expand each of these three expressions in ascending powers of $x$, up to the term in $x^{3}$.

**3** Discuss with your classmates which method you would prefer if you were asked for:

a a linear approximation for $\mathrm{f}(x)$

b a quadratic approximation for $\mathrm{f}(x)$

c a cubic approximation for $\mathrm{f}(x)$.

## 7.5 Partial fractions and binomial expansions

One of the most common reasons for splitting a fraction into partial fractions is so that binomial expansions can be applied.

<a id="ch07-we-7.12"></a>
#### WORKED EXAMPLE 7.12

Given that $\mathrm{f}(x)=\frac{10 x+1}{(1-2 x)(1+x)}$, express f(x) in partial fractions and hence obtain the expansion of $\mathrm{f}(x)$ in ascending powers of $x$, up to and including the term in $x^{3}$. State the range of values of $x$ for which the expansion is valid.

Answer

$$
\begin{align}
\frac{10 x+1}{(1-2 x)(1+x)} & \equiv \frac{A}{1-2 x}+\frac{B}{1+x} \\
10 x+1 & \equiv A(1+x)+B(1-2 x) \tag{1}
\end{align}
$$

Multiply throughout by $(1-2 x)(1+x)$.

Let $x=-1$ in equation (1):

$$
\begin{align}
-9 & =3 B \\
B & =-3
\end{align}
$$

Let $x=\frac{1}{2}$ in equation (1):

$$
\begin{align}
6 & =\frac{3}{2} A \\
A & =4
\end{align}
$$

$$
\therefore \frac{10 x+1}{(1-2 x)(1+x)} \equiv \frac{4}{1-2 x}-\frac{3}{1+x} \equiv 4(1-2 x)^{-1}-3(1+x)^{-1}
$$

Expanding $(1-2 x)^{-1}$ gives:

$$
\begin{align}
(1-2 x)^{-1} & =1+(-1)(-2 x)+\frac{(-1)(-2)}{2!}(-2 x)^{2}+\frac{(-1)(-2)(-3)}{3!}(-2 x)^{3}+\qquad \\
& =1+2 x+4 x^{2}+8 x^{3}+\qquad \text { valid for }|-2 x|<1 \text { i.e. }-\frac{1}{2}<x<\frac{1}{2}
\end{align}
$$

Expanding $(1+x)^{-1}$ gives:

$$
\begin{align}
(1+x)^{-1} & =1+(-1) x+\frac{(-1)(-2)}{2!} x^{2}+\frac{(-1)(-2)(-3)}{3!} x^{3} \\
& =1-x+x^{2}-x^{3}+\qquad \quad \text { valid for }|x|<1 \quad \text { i.e. }-1<x<1
\end{align}
$$

$$
\begin{align}
\therefore \frac{10 x+1}{(1-2 x)(1+x)} & =4\left(1+2 x+4 x^{2}+8 x^{3}+\qquad \right)-3\left(1-x+x^{2}-x^{3}+\qquad \right) \\
& =1+11 x+13 x^{2}+35 x^{3}+\qquad
\end{align}
$$

The expansion is valid for the range of values of $x$ satisfying both $-\frac{1}{2}<x<\frac{1}{2}$ and $-1<x<1$

![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-180_140_568_1677_801.jpg)

Hence, the expansion is valid for $-\frac{1}{2}<x<\frac{1}{2}$.

<a id="ch07-ex7E"></a>
### EXERCISE 7E

<a id="ch07-ex7E-q1"></a>
##### Question 1
**a** Express $\frac{7 x-1}{(1-x)(1+2 x)}$ in partial fractions.

**b** Hence obtain the expansion of $\frac{7 x-1}{(1-x)(1+2 x)}$ in ascending powers of $x$, up to and including the term in $x^{3}$.

<a id="ch07-ex7E-q2"></a>
##### Question 2
**a** Express $\frac{5 x^{2}+x}{(1-x)^{2}(1-3 x)}$ in partial fractions.

**b** Hence obtain the expansion of $\frac{5 x^{2}+x}{(1-x)^{2}(1-3 x)}$ in ascending powers of $x$, up to and including the term in $x^{3}$.

<a id="ch07-ex7E-q3"></a>
##### Question 3
**a** Express $\frac{7 x^{2}+4 x+4}{(1-x)\left(2 x^{2}+1\right)}$ in partial fractions.

**b** Hence obtain the expansion of $\frac{7 x^{2}+4 x+4}{(1-x)\left(2 x^{2}+1\right)}$ in ascending powers of $x$, up to and including the term in $x^{3}$.

<a id="ch07-ex7E-q4"></a>
##### Question 4
**a** Express $\frac{19-7 x-6 x^{2}}{(2 x+1)(2-3 x)}$ in partial fractions.

**b** Hence obtain the coefficient of $x^{2}$ in the expansion of $\frac{19-7 x-6 x^{2}}{(2 x+1)(2-3 x)}$.

<a id="ch07-ex7E-q5"></a>
##### Question 5
**a** Express $\frac{21}{(x-4)(x+3)}$ in partial fractions.

**b** Hence obtain the expansion of $\frac{24}{(x-4)(x+3)}$ in ascending powers of $x$, up to and including the term in $x^{2}$.

<a id="ch07-ex7E-q6"></a>
##### Question 6
**a** Express $\frac{6 x^{2}-24 x+15}{(x+1)(x-2)^{2}}$ in partial fractions.

**b** Hence obtain the expansion of $\frac{6 x^{2}-24 x+15}{(x+1)(x-2)^{2}}$ in ascending powers of $x$, up to and including the term in $x^{2}$.

### Checklist of learning and understanding

Partial fractions

- Case 1: If the denominator of a proper algebraic fraction has two distinct linear factors, the fraction can be split into partial fractions using the rule $\frac{p x+q}{(a x+b)(c x+d)} \equiv \frac{A}{a x+b}+\frac{B}{c x+d}$

- Case 2: If the denominator of a proper algebraic fraction has a repeated linear factor, the fraction can be split into partial fractions using the rule $\frac{p x+q}{(a x+b)^{2}} \equiv \frac{A}{a x+b}+\frac{B}{(a x+b)^{2}}$

- Case 3: If the denominator of a proper algebraic fraction has a quadratic factor of the form $c x^{2}+d$ that cannot be factorised, the fraction can be split into partial fractions using the rule

$$
\frac{p x+q}{(a x+b)\left(c x^{2}+d\right)} \equiv \frac{A}{a x+b}+\frac{B x+C}{c x^{2}+d}
$$

- Case 4: If an algebraic fraction is improper we must first express it as the sum of a polynomial and a proper fraction and then split the proper fraction into partial fractions.

Binomial expansion of $(\mathbf{1}+\boldsymbol{x})^{\boldsymbol{n}}$ for values of $\boldsymbol{n}$ that are not positive integers

- $(1+x)^{n}=1+n x+\frac{n(n-1)}{2!} x^{2}+\frac{n(n-1)(n-2)}{3!} x^{3}+$ for $|x|<1$.

Binomial expansion of $(\mathbf{a}+\boldsymbol{x})^{\boldsymbol{n}}$ for values of $\boldsymbol{n}$ that are not positive integers

- $(a+x)^{n}=a^{n}\left[1+n\left(\frac{x}{a}\right)+\frac{n(n-1)}{2!}\left(\frac{x}{a}\right)^{2}+\frac{n(n-1)(n-2)}{3!}\left(\frac{x}{a}\right)^{3}+\qquad \right]$ for $\left|\frac{x}{a}\right|<1$.

<a id="ch07-review"></a>
### END-OF-CHAPTER REVIEW EXERCISE 7

<a id="ch07-review-q1"></a>
##### Question 1
Expand $(1-2 x)^{-4}$ in ascending powers of $x$, up to and including the term in $x^{3}$, simplifying the coefficients. `[4]`

<a id="ch07-review-q2"></a>
##### Question 2
Expand $\sqrt[3]{1-(6 x)}$ in ascending powers of $x$ up to and including the term in $x^{3}$, simplifying the coefficients. `[4]`

*Cambridge International A Level Mathematics 9709 Paper 31 Q1 June 2011*

<a id="ch07-review-q3"></a>
##### Question 3
Expand $(2-x)(1+2 x)^{-\frac{3}{2}}$ in ascending powers of $x$, up to and including the term in $x^{2}$, simplifying the coefficients. `[4]`

*Cambridge International A Level Mathematics 9709 Paper 31 Q2 November 2016*

<a id="ch07-review-q4"></a>
##### Question 4
Expand $\frac{1+3 x}{\sqrt{(1+2 x)}}$ in ascending powers of $x$ up to and including the term in $x^{2}$, simplifying the coefficients. `[4]`

*Cambridge International A Level Mathematics 9709 Paper 31 Q2 June 2013*

<a id="ch07-review-q5"></a>
##### Question 5
Expand $\frac{1}{\sqrt{1+3 x}}$ in ascending powers of $x$, up to and including the term in $x^{3}$, simplifying the coefficients. `[4]`

<a id="ch07-review-q6"></a>
##### Question 6
Expand $\frac{10}{(2-x)^{2}}$ in ascending powers of $x$, up to and including the term in $x^{2}$, simplifying the coefficients. `[4]`

<a id="ch07-review-q7"></a>
##### Question 7
Expand $\frac{1}{\sqrt{4-5 x}}$ in ascending powers of $x$, up to and including the term in $x^{2}$, simplifying the coefficients. `[4]`

<a id="ch07-review-q8"></a>
##### Question 8
Express $\frac{12}{x^{2}(2 x-3)}$ in the form $\frac{A}{x}+\frac{B}{x^{2}}+\frac{C}{2 x-3}$. `[4]`

<a id="ch07-review-q9"></a>
##### Question 9
Express $\frac{8 x^{2}+4 x+21}{(x+2)\left(x^{2}+5\right)}$ in the form $\frac{A}{x+2}+\frac{B x+C}{x^{2}+5}$. `[4]`

<a id="ch07-review-q10"></a>
##### Question 10
Express $\frac{7 x^{2}-3 x+2}{x\left(x^{2}+1\right)}$ in partial fractions. `[5]`

*Cambridge International A Level Mathematics 9709 Paper 31 Q3 June 2013*

<a id="ch07-review-q11"></a>
##### Question 11
Given that $\frac{9 x^{3}-11 x^{2}+8 x-4}{x^{2}(3 x-2)} \equiv A+\frac{B}{x}+\frac{C}{x^{2}}+\frac{D}{3 x-2}$, find the values of $A, B, C$ and $D$. `[5]`

<a id="ch07-review-q12"></a>
##### Question 12
Express $\frac{4 x^{2}-5 x+3}{(x+2)(2 x-1)}$ in partial fractions. `[5]`

<a id="ch07-review-q13"></a>
##### Question 13
Show that for small values of $x^{2},\left(1-2 x^{2}\right)^{-2}-\left(1+6 x^{2}\right)^{\frac{2}{3}} \approx k x^{4}$, where the value of the constant $k$ is to be determined. `[6]`

*Cambridge International A Level Mathematics 9709 Paper 31 Q3 June 2015*

<a id="ch07-review-q14"></a>
##### Question 14
Let $\mathrm{f}(x)=\frac{4 x^{2}+12}{(x+1)(x-3)^{2}}$.

**i** Express $\mathrm{f}(x)$ in partial fractions. `[5]`

**ii** Hence obtain the expansion of $\mathrm{f}(x)$ in ascending powers of $x$, up to and including the term in $x^{2}$. `[5]`

*Cambridge International A Level Mathematics 9709 Paper 31 Q8 June 2016*

<a id="ch07-review-q15"></a>
##### Question 15
Let $\mathrm{f}(x)=\frac{2 x^{2}-7 x-1}{(x-2)\left(x^{2}+3\right)}$.

**i** Express $\mathrm{f}(x)$ in partial fractions. `[5]`

**ii** Hence obtain the expansion of $\mathrm{f}(x)$ in ascending powers of $x$, up to and including the term in $x^{2}$. `[5]`

*Cambridge International A Level Mathematics 9709 Paper 31 Q7 November 2013*

<a id="ch07-review-q16"></a>
##### Question 16
Let $\mathrm{f}(x)=\frac{3 x}{(1+x)\left(1+2 x^{2}\right)}$.

**i** Express $\mathrm{f}(x)$ in partial fractions. `[5]`

**ii** Hence obtain the expansion of $\mathrm{f}(x)$ in ascending powers of $x$, up to and including the term in $x^{3}$. `[5]`

*Cambridge International A Level Mathematics 9709 Paper 31 Q8 November 2010*
