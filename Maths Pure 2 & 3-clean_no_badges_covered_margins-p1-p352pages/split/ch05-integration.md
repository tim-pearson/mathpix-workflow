# Chapter 5: Integration
<a id="ch05-prerequisite"></a>
### PREREQUISITE KNOWLEDGE

| Where it comes from | What you should be able to do | Check your skills |
| :--- | :--- | :--- |
| Chapter 4 | Differentiate standard functions. | 1 Find $\frac{\mathrm{d} y}{\mathrm{~d} x}$ when:<br>&#160;&#160;a $y=3 \sin 2 x-5 \cos x$<br>&#160;&#160;b $y=\mathrm{e}^{5 x-2}$<br>&#160;&#160;c $y=\ln (2 x+1)$<br> |
| Chapter 4 | Use standard trigonometric relationships to prove trigonometric identities. | 2 Prove that $\cos 4 x+4 \cos 2 x \equiv 8 \cos ^{4} x-3 .$ |

### Why do we study integration?

In this chapter we will learn how to integrate exponential, logarithmic and trigonometrical functions and how to apply integration to solve problems.

It is important that you have a good grasp of the work covered in Chapter 3 on trigonometry, as you will be expected to know and use the trigonometrical relationships when solving integration problems.

Lastly, we will learn how to find an estimate for $\int_{a}^{b} \mathrm{f}(x) \mathrm{d} x$ using a numerical method. This is used when we are not able to find the value of $\int_{a}^{b} \mathrm{f}(x) \mathrm{d} x$ using an algebraic method.

## 5.1 Integration of exponential functions

Since integration is the reverse process of differentiation, the rules for integrating exponential functions are:

<a id="ch05-kp-5.1"></a>
#### KEY POINT 5.1

$$
\int \mathrm{e}^{x} \mathrm{~d} x=\mathrm{e}^{x}+c \quad \int \mathrm{e}^{a x+b} \mathrm{~d} x=\frac{1}{a} \mathrm{e}^{a x+b}+c
$$

<a id="ch05-we-5.1"></a>
#### WORKED EXAMPLE 5.1

Find:

**a** $\int \mathrm{e}^{3 x} \mathrm{~d} x$

**b** $\int \mathrm{e}^{-2 x} \mathrm{~d} x$

**c** $\int \mathrm{e}^{5 x-4} \mathrm{~d} x$

Answer

**a** $\int \mathrm{e}^{3 x} \mathrm{~d} x=\frac{1}{3} \mathrm{e}^{3 x}+c$

**b** $\int \mathrm{e}^{-2 x} \mathrm{~d} x=\frac{1}{-2} \mathrm{e}^{-2 x}+c$ $=-\frac{1}{2} \mathrm{e}^{-2 x}+c$

**c** $\int \mathrm{e}^{5 x-4} \mathrm{~d} x=\frac{1}{5} \mathrm{e}^{5 x-4}+c$

<a id="ch05-we-5.2"></a>
#### WORKED EXAMPLE 5.2

Evaluate $\int_{1}^{2} 9 \mathrm{e}^{3 x-1} \mathrm{~d} x$.

Answer

$$
\begin{align}
\int_{1}^{2} 9 \mathrm{e}^{3 x-1} \mathrm{~d} x & =\left[\frac{9}{3} \mathrm{e}^{3 x-1}\right]_{1}^{2} \\
& =\left(3 \mathrm{e}^{5}\right)-\left(3 \mathrm{e}^{2}\right) \\
& =3 \mathrm{e}^{2}\left(\mathrm{e}^{3}-1\right)
\end{align}
$$

<a id="ch05-we-5.3"></a>
#### WORKED EXAMPLE 5.3

![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-113_274_392_1007_263.jpg)

Find the area of the shaded region.

Answer

$$
\begin{align}
\text { Area } & =\int_{1}^{2}\left(x^{2}+\mathrm{e}^{-2 x}\right) \mathrm{d} x \\
& =\left[\frac{x^{3}}{3}-\frac{1}{2} \mathrm{e}^{-2 x}\right]_{1}^{2} \\
& =\left(\frac{8}{3}-\frac{1}{2} \mathrm{e}^{-4}\right)-\left(\frac{1}{3}-\frac{1}{2} \mathrm{e}^{-2}\right) \\
& =\frac{7}{3}+\frac{1}{2} \mathrm{e}^{-2}-\frac{1}{2} \mathrm{e}^{-4} \\
& \approx 2.39 \text { units }^{2}
\end{align}
$$

<a id="ch05-ex5A"></a>
### EXERCISE 5A

<a id="ch05-ex5A-q1"></a>
##### Question 1
Find:

**a** $\int \mathrm{e}^{2 x} \mathrm{~d} x$

**b** $\int \mathrm{e}^{-4 x} \mathrm{~d} x$

**c** $\int 6 \mathrm{e}^{3 x} \mathrm{~d} x$

**d** $\int 4 \mathrm{e}^{\frac{1}{2} x} \mathrm{~d} x$

**e** $\int 2 \mathrm{e}^{-x} \mathrm{~d} x$

**f** $\quad \int \mathrm{e}^{2 x+4} \mathrm{~d} x$

**g** $\int \mathrm{e}^{3 x-1} \mathrm{~d} x$

**h** $\int 6 \mathrm{e}^{2-3 x} \mathrm{~d} x$

**i** $\quad \int 2 \mathrm{e}^{8 x-3} \mathrm{~d} x$

<a id="ch05-ex5A-q2"></a>
##### Question 2
Find:

**a** $\int \mathrm{e}^{-x}\left(1+\mathrm{e}^{x}\right) \mathrm{d} x$

**b** $\quad \int 5 \mathrm{e}^{x}\left(2+\mathrm{e}^{3 x}\right) \mathrm{d} x$

**c** $\int\left(\mathrm{e}^{2 x}-1\right)^{2} \mathrm{~d} x$

**d** $\int \frac{4+\mathrm{e}^{2 x}}{\mathrm{e}^{2 x}} \mathrm{~d} x$

**e** $\int \frac{8-\mathrm{e}^{x}}{2 \mathrm{e}^{2 x}} \mathrm{~d} x$

**f** $\quad \int \frac{\left(\mathrm{e}^{x}-2\right)^{2}}{\mathrm{e}^{2 x}} \mathrm{~d} x$

<a id="ch05-ex5A-q3"></a>
##### Question 3
Evaluate:

**a** $\int_{0}^{2} \mathrm{e}^{3 x} \mathrm{~d} x$

**b** $\int_{0}^{\frac{1}{2}} \mathrm{e}^{4 x} \mathrm{~d} x$

**c** $\int_{0}^{\ln 2} 5 \mathrm{e}^{-2 x} \mathrm{~d} x$

**d** $\int_{0}^{3} \mathrm{e}^{1+2 x} \mathrm{~d} x$

**e** $\int_{0}^{1} \frac{8}{\mathrm{e}^{2 x-1}} \mathrm{~d} x$

**f** $\quad \int_{0}^{1}\left(\mathrm{e}^{x}+1\right)^{2} \mathrm{~d} x$

**g** $\quad \int_{0}^{1}\left(\mathrm{e}^{x}+\mathrm{e}^{2 x}\right)^{2} \mathrm{~d} x$

**h** $\quad \int_{0}^{1}\left(2 \mathrm{e}^{x}-\frac{5}{\mathrm{e}^{x}}\right)^{2} \mathrm{~d} x$

**i** $\quad \int_{0}^{2} \frac{\left(\mathrm{e}^{x}+1\right)^{2}}{\mathrm{e}^{2 x}} \mathrm{~d} x$

<a id="ch05-ex5A-q4"></a>
##### Question 4
A curve is such that $\frac{\mathrm{d} y}{\mathrm{~d} x}=6 \mathrm{e}^{2 x}+2 \mathrm{e}^{-x}$. Given that the curve passes through the point (0, 2), find the equation of the curve.

<a id="ch05-ex5A-q5"></a>
##### Question 5
A curve is such that $\frac{\mathrm{d}^{2} y}{\mathrm{~d} x^{2}}=20 \mathrm{e}^{-2 x}$. Given that $\frac{\mathrm{d} y}{\mathrm{~d} x}=-8$ when $x=0$ and that the curve passes through the point $\left(1, \frac{5}{\mathrm{e}^{2}}\right)$, find the equation of the curve.

<a id="ch05-ex5A-q6"></a>
##### Question 6
Find the exact area of the region bounded by the curve $y=1+\mathrm{e}^{2 x-5}$, the $x$-axis and the lines $x=1$ and $x=3$.

<a id="ch05-ex5A-q7"></a>
##### Question 7
![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-114_288_367_1490_330.jpg)

Find the exact area of the shaded region.

<a id="ch05-ex5A-q8"></a>
##### Question 8
**a** Show that $\frac{\mathrm{d}}{\mathrm{d} x}\left(x \mathrm{e}^{x}-\mathrm{e}^{x}\right)=x \mathrm{e}^{x}$.

**b** ![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-114_320_620_1988_383.jpg)

Use your result from part a to evaluate the area of the shaded region.

<a id="ch05-ex5A-q9"></a>
##### Question 9
**a** Find $\int_{0}^{a}\left(4 \mathrm{e}^{-2 x}+5 \mathrm{e}^{-x}\right) \mathrm{d} x$, where $a$ is a positive constant.

**b** Hence find the value of $\int_{0}^{\infty}\left(4 \mathrm{e}^{-2 x}+5 \mathrm{e}^{-x}\right) \mathrm{d} x$.

<a id="ch05-ex5A-q10"></a>
##### Question 10
![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-115_283_400_278_371.jpg) The diagram shows the curve $y=2 \mathrm{e}^{x}+8 \mathrm{e}^{-x}-7$ and its minimum point $M$.

Find the area of the shaded region.

<a id="ch05-ex5A-q11"></a>
##### Question 11
![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-115_248_398_719_371.jpg) The diagram shows the graph of $y=\mathrm{e}^{x}$. The points $(\ln 2,2)$ and $(\ln 3,3)$ lie on the curve.

**a** Find the value of $\int_{\ln 2}^{\ln 3} \mathrm{e}^{x} \mathrm{~d} x$.

**b** Hence show that $\int_{2}^{3} \ln y \mathrm{~d} y=\ln \left(\frac{27}{4 \mathrm{e}}\right)$.

## 5.2 Integration of $\frac{\mathbf{1}}{\boldsymbol{a} \boldsymbol{x}+\boldsymbol{b}}$

Since integration is the reverse process of differentiation, the rules for integration are:

<a id="ch05-kp-5.2"></a>
#### KEY POINT 5.2

$$
\int \frac{1}{x} \mathrm{~d} x=\ln x+c, x>0 \quad \int \frac{1}{a x+b} \mathrm{~d} x=\frac{1}{a} \ln (a x+b)+c, a x+b>0
$$

<a id="ch05-we-5.4"></a>
#### WORKED EXAMPLE 5.4

Find each of these integrals and state the values of $x$ for which the integral is valid.

**a** $\int \frac{2}{x} \mathrm{~d} x$

**b** $\int \frac{4}{2 x+1} \mathrm{~d} x$

**c** $\int \frac{6}{2-3 x} \mathrm{~d} x$

Answer

**a**

$$
\begin{align}
\int \frac{2}{x} \mathrm{~d} x & =2 \int \frac{1}{x} \mathrm{~d} x \\
& =2 \ln x+c, x>0
\end{align}
$$

**b**

$$
\begin{align}
\int \frac{4}{2 x+1} \mathrm{~d} x & =4 \int \frac{1}{2 x+1} \mathrm{~d} x \\
& =4\left(\frac{1}{2}\right) \ln (2 x+1)+c \\
& =2 \ln (2 x+1)+c, x>-\frac{1}{2}
\end{align}
$$

#### REWIND

In Chapter 4, we learnt the following rules for differentiating logarithmic functions:

$$
\begin{align}
& \frac{\mathrm{d}}{\mathrm{~d} x}(\ln x)=\frac{1}{x}, x>0 \\
& \frac{\mathrm{~d}}{\mathrm{~d} x}[\ln (a x+b)]= \\
& \frac{a}{a x+b}, a x+b>0
\end{align}
$$

It is important to remember that $\ln x$ is only defined for $x>0$.

c

$$
\begin{align}
\int \frac{6}{2-3 x} \mathrm{~d} x & =6 \int \frac{1}{2-3 x} \mathrm{~d} x \\
& =6\left(\frac{1}{-3}\right) \ln (2-3 x)+c \qquad \text { Valid for } 2-3 x>0 . \\
& =-2 \ln (2-3 x)+c, x<\frac{2}{3}
\end{align}
$$

#### EXPLORE 5.1

Fiona is asked to find $\int x^{-1} \mathrm{~d} x$.

She tries to use the formula $\int x^{n} \mathrm{~d} x=\frac{1}{n+1} x^{n+1}+c$ to obtain her answer.

Fiona is also asked to find $\int(2 x+3)^{-1} \mathrm{~d} x$.

She tries to use the formula $\int(a x+b)^{n} \mathrm{~d} x=\frac{1}{a(n+1)}(a x+b)^{n+1}+c$ to obtain her answer.

Discuss with your classmates why Fiona's methods do not work.

#### EXPLORE 5.2

Rafiu and Fausat are asked to find $\int \frac{1}{2(3 x+1)} \mathrm{d} x$.

Rafiu writes: $\int \frac{1}{2(3 \mathrm{x}+1)} \mathrm{dx}=\int \frac{1}{6 \mathrm{x}+2} \mathrm{dx}$

$$
=\frac{1}{6} \ln (6 x+2)+c
$$

Fausat writes: $\int \frac{1}{2(3 x+1)} d x=\frac{1}{2} \int \frac{1}{3 x+1} d x$

$$
\begin{align}
& =\left(\frac{1}{2}\right)\left(\frac{1}{3}\right) \ln (3 x+1)+c \\
& =\frac{1}{6} \ln (3 x+1)+c
\end{align}
$$

Decide who is correct and discuss the reasons for your decision with your classmates.

Consider the integrals $\int_{2}^{3} \frac{1}{x} \mathrm{~d} x$ and $\int_{-3}^{-2} \frac{1}{x} \mathrm{~d} x$.

From the symmetry properties of the graph of $y=\frac{1}{x}$ we can see that the shaded areas that represent the two integrals are equal in magnitude. However, one of the areas is below the $x$-axis, which suggests that $\int_{-3}^{-2} \frac{1}{x} \mathrm{~d} x=-\int_{2}^{3} \frac{1}{x} \mathrm{~d} x$.

![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-116_322_454_2219_1543.jpg)

Evaluating $\int_{2}^{3} \frac{1}{x} \mathrm{~d} x$ gives:

$$
\int_{2}^{3} \frac{1}{x} \mathrm{~d} x=[\ln x]_{2}^{3}=\ln 3-\ln 2=\ln \frac{3}{2}
$$

This implies that $\int_{-3}^{-2} \frac{1}{x} \mathrm{~d} x=-\ln \frac{3}{2}=\ln \frac{2}{3}$.

If we try using integration to find the value of $\int_{-3}^{-2} \frac{1}{x} \mathrm{~d} x$ we obtain:

$$
\int_{-3}^{-2} \frac{1}{x} \mathrm{~d} x=[\ln x]_{-3}^{-2}=\ln (-2)-\ln (-3)=\ln \frac{2}{3}
$$

There is, however, a problem with this calculation in that $\ln x$ is only defined for $x>0$ so $\ln (-2)$ and $\ln (-3)$ do not actually exist.

Hence for $x<0$, we say that $\int \frac{1}{x} \mathrm{~d} x=\ln |x|+c$.

In conclusion, the integration formulae are written as:

<a id="ch05-kp-5.3"></a>
#### KEY POINT 5.3

$$
\int \frac{1}{x} \mathrm{~d} x=\ln |x|+c \quad \int \frac{1}{a x+b} \mathrm{~d} x=\frac{1}{a} \ln |a x+b|+c
$$

<a id="ch05-we-5.5"></a>
#### WORKED EXAMPLE 5.5

Find the value of $\int_{2}^{3} \frac{6}{2-3 x} \mathrm{~d} x$.

Answer

$$
\begin{align}
\int_{2}^{3} \frac{6}{2-3 x} \mathrm{~d} x & =\left[\left(\frac{6}{-3}\right) \ln |2-3 x|\right]_{2}^{3} \qquad \text { Substitute limits. } \\
& =(-2 \ln 7)-(-2 \ln 4) \\
& =-2 \ln 7+2 \ln 4 \\
& =2 \ln \frac{4}{7}
\end{align}
$$

<a id="ch05-ex5B"></a>
### EXERCISE 5B

<a id="ch05-ex5B-q1"></a>
##### Question 1
Find:

**a** $\int \frac{6}{x} \mathrm{~d} x$

**b** $\int \frac{1}{2 x} \mathrm{~d} x$

**c** $\int \frac{1}{3 x+1} \mathrm{~d} x$

**d** $\quad \int \frac{6}{2 x-5} \mathrm{~d} x$

**e** $\quad \int \frac{5}{2-3 x} \mathrm{~d} x$

**f** $\quad \int \frac{3}{2(5 x-1)} \mathrm{d} x$

<a id="ch05-ex5B-q2"></a>
##### Question 2
Evaluate:

**a** $\int_{0}^{5} \frac{1}{x+2} \mathrm{~d} x$

**b** $\quad \int_{1}^{4} \frac{1}{2 x+1} \mathrm{~d} x$

**c** $\int_{-1}^{4} \frac{3}{2 x+5} \mathrm{~d} x$

**d** $\quad \int_{2}^{4} \frac{2}{4 x+1} \mathrm{~d} x$

**e** $\int_{0}^{2} \frac{3}{2 x-7} \mathrm{~d} x$

**f** $\quad \int_{2}^{3} \frac{4}{3-2 x} \mathrm{~d} x$

<a id="ch05-ex5B-q3"></a>
##### Question 3
Evaluate:

**a** $\int_{4}^{10}\left(2+\frac{5}{3 x-2}\right) \mathrm{d} x$

**b** $\int_{1}^{3}\left(\frac{3}{x}-\frac{4}{2 x-1}\right) \mathrm{d} x$

**c** $\int_{-1}^{3}\left(2 x-1+\frac{4}{2 x+3}\right) \mathrm{d} x$

<a id="ch05-ex5B-q4"></a>
##### Question 4
**a** Given that $\frac{4 x}{2 x-1} \equiv 2+\frac{A}{2 x-1}$, find the value of the constant $A$.

**b** Hence show that $\int_{1}^{5} \frac{4 x}{2 x-1} \mathrm{~d} x=8+\ln 9$.

<a id="ch05-ex5B-q5"></a>
##### Question 5
**a** Find the quotient and remainder when $6 x^{2}+5 x$ is divided by $2 x-5$.

**b** Hence show that $\int_{0}^{1} \frac{6 x^{2}+5 x}{2 x-5} \mathrm{~d} x=\frac{23}{2}-25 \ln \left(\frac{5}{3}\right)$.

<a id="ch05-ex5B-q6"></a>
##### Question 6
A curve is such that $\frac{\mathrm{d} y}{\mathrm{~d} x}=2 x+\frac{3}{x+\mathrm{e}}$.

Given that the curve passes through the point $\left(\mathrm{e}, \mathrm{e}^{2}\right)$, find the equation of the curve.

<a id="ch05-ex5B-q7"></a>
##### Question 7
![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-118_277_411_1363_330.jpg) The diagram shows part of the curve $y=\frac{2}{x+3}$. Given that the shaded region has area 4, find the value of $k$.

<a id="ch05-ex5B-q8"></a>
##### Question 8
The points $P(1,-2)$ and $Q(2, k)$ lie on the curve for which $\frac{\mathrm{d} y}{\mathrm{~d} x}=3-\frac{2}{x}$. The tangents to the curve at the points $P$ and $Q$ intersect at the point $R$. Find the coordinates of $R$.

## 5.3 Integration of $\boldsymbol{\operatorname { s i n }}(\boldsymbol{a} \boldsymbol{x}+\boldsymbol{b}), \boldsymbol{\operatorname { c o s }}(\boldsymbol{a} \boldsymbol{x}+\boldsymbol{b})$ and $\boldsymbol{\operatorname { s e c }}^{\mathbf{2}}(\boldsymbol{a} \boldsymbol{x}+\boldsymbol{b})$

In Chapter 4, we learnt how to differentiate some trigonometric functions:

$$
\begin{array}{ll} \frac{\mathrm{d}}{\mathrm{~d} x}(\sin x)=\cos x & \frac{\mathrm{~d}}{\mathrm{~d} x}[\sin (a x+b)]=a \cos (a x+b) \\
\frac{\mathrm{d}}{\mathrm{~d} x}(\cos x)=-\sin x & \frac{\mathrm{~d}}{\mathrm{~d} x}[\cos (a x+b)]=-a \sin (a x+b) \\
\frac{\mathrm{d}}{\mathrm{~d} x}(\tan x)=\sec ^{2} x & \frac{\mathrm{~d}}{\mathrm{~d} x}[\tan (a x+b)]=a \sec ^{2}(a x+b) \end{array}
$$

<a id="ch05-kp-5.4"></a>
#### KEY POINT 5.4

Since integration is the reverse process of differentiation, the rules for integrating are:

$$
\begin{array}{ll} \int \cos x d x=\sin x+c & \int \cos (a x+b) d x=\frac{1}{a} \sin (a x+b)+c \\
\int \sin x d x=-\cos x+c & \int \sin (a x+b) d x=-\frac{1}{a} \cos (a x+b)+c \\
\int \sec ^{2} x d x=\tan x+c & \int \sec ^{2}(a x+b) d x=\frac{1}{a} \tan (a x+b)+c \end{array}
$$

<a id="ch05-we-5.6"></a>
#### WORKED EXAMPLE 5.6

Find:

**a** $\int \sin 2 x \mathrm{~d} x$

**b** $\int \cos 3 x \mathrm{~d} x$

**c** $\int 4 \sec ^{2} \frac{x}{2} \mathrm{~d} x$

Answer

**a** $\int \sin 2 x \mathrm{~d} x=-\frac{1}{2} \cos 2 x+c$

**b** $\int \cos 3 x \mathrm{~d} x=\frac{1}{3} \sin 3 x+c$

**c** $\int 4 \sec ^{2} \frac{x}{2} \mathrm{~d} x=4 \int \sec ^{2} \frac{x}{2} \mathrm{~d} x$

$$
\begin{align}
& =4 \times\left(2 \tan \frac{x}{2}\right)+c \\
& =8 \tan \frac{x}{2}+c
\end{align}
$$

<a id="ch05-we-5.7"></a>
#### WORKED EXAMPLE 5.7

Find the exact value of $\int_{0}^{\frac{\pi}{4}}(3-2 \sin 2 x) \mathrm{d} x$.

Answer

$$
\begin{align}
\int_{0}^{\frac{\pi}{4}}(3-2 \sin 2 x) \mathrm{d} x & =\left[3 x+\frac{2}{2} \cos 2 x\right]_{0}^{\frac{\pi}{4}} \\
& =\left(\frac{3 \pi}{4}+\cos \frac{\pi}{2}\right)-(0+\cos 0) \\
& =\left(\frac{3 \pi}{4}+0\right)-(0+1) \\
& =\frac{3 \pi}{4}-1
\end{align}
$$

<a id="ch05-ex5C"></a>
### EXERCISE 5C

<a id="ch05-ex5C-q1"></a>
##### Question 1
Find:

**a** $\int \sin 3 x \mathrm{~d} x$

**b** $\int \cos 4 x \mathrm{~d} x$

**c** $\int \sin \frac{x}{2} \mathrm{~d} x$

**d** $\int 3 \sin 2 x \mathrm{~d} x$

**e** $\int 5 \cos 3 x \mathrm{~d} x$

**f** $\int \sec ^{2} 2 x \mathrm{~d} x$

**g** $\int 2 \cos (1-5 x) \mathrm{d} x$

**h** $\int 3 \sin (2 x+1) \mathrm{d} x$

**i** $\int 2 \sec ^{2}(5 x-2) \mathrm{d} x$

<a id="ch05-ex5C-q2"></a>
##### Question 2
Evaluate:

**a** $\int_{0}^{\frac{1}{6} \pi} \cos 4 x \mathrm{~d} x$

**b** $\int_{0}^{\frac{2}{3} \pi} \sin \left(\frac{1}{2} x\right) \mathrm{d} x$

**c** $\int_{0}^{\frac{1}{6} \pi} \sec ^{2} 2 x \mathrm{~d} x$

**d** $\int_{0}^{\frac{1}{2} \pi}(\sin 2 x+\cos x) \mathrm{d} x$

**e** $\int_{0}^{\frac{1}{6} \pi}(\cos 2 x+\sin x) \mathrm{d} x$

**f** $\int_{-\frac{1}{4} \pi}^{\frac{1}{4} \pi}\left(5-2 \sec ^{2} x\right) \mathrm{d} x$

<a id="ch05-ex5C-q3"></a>
##### Question 3
**a** Find $\frac{\mathrm{d}}{\mathrm{d} x}(x \sin x+\cos x)$.

**b** Hence find the exact value of $\int_{0}^{\frac{1}{3} \pi} x \cos x \mathrm{~d} x$.

<a id="ch05-ex5C-q4"></a>
##### Question 4
A curve is such that $\frac{\mathrm{d} y}{\mathrm{~d} x}=1-3 \sin 2 x$.

Given that the curve passes through the point $\left(\frac{\pi}{4}, 0\right)$, find the equation of the curve.

<a id="ch05-ex5C-q5"></a>
##### Question 5
A curve is such that $\frac{\mathrm{d}^{2} y}{\mathrm{~d} x^{2}}=-12 \sin 2 x-2 \cos x$.

Given that $\frac{\mathrm{d} y}{\mathrm{~d} x}=4$ when $x=0$ and that the curve passes through the point $\left(\frac{\pi}{2},-3\right)$, find the equation of the curve.

<a id="ch05-ex5C-q6"></a>
##### Question 6
The point $\left(\frac{\pi}{2}, 5\right)$ lies on the curve for which $\frac{\mathrm{d} y}{\mathrm{~d} x}=4 \sin \left(2 x-\frac{\pi}{2}\right)$.

**a** Find the equation of the curve.

**b** Find the equation of the normal to the curve at the point where $x=\frac{\pi}{3}$.

<a id="ch05-ex5C-q7"></a>
##### Question 7
![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-120_235_410_2138_329.jpg) The diagram shows part of the curve $y=1+\sqrt{3} \sin 2 x+\cos 2 x$. Find the exact value of the area of the shaded region.

<a id="ch05-ex5C-q8"></a>
##### Question 8
![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-121_278_506_271_370.jpg) The diagram shows part of the curve $y=3 \sin 2 x+6 \sin x$ and its maximum point $M$.

Find the exact area of the shaded region.

<a id="ch05-ex5C-q9"></a>
##### Question 9
![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-121_399_510_731_371.jpg) The diagram shows part of the graph of $y=\sin x$. The points $\left(\frac{\pi}{6}, \frac{1}{2}\right)$ and $\left(\frac{\pi}{3}, \frac{\sqrt{3}}{2}\right)$ lie on the curve.

**a** Find the exact value of $\int_{\frac{\pi}{6}}^{\frac{\pi}{3}} \sin x \mathrm{~d} x$.

**b** Hence show that $\int_{\frac{1}{2}}^{\frac{\sqrt{3}}{2}}\left(\sin ^{-1} y\right) \mathrm{d} y=\frac{\pi}{12}(2 \sqrt{3}-1)-\frac{\sqrt{3}-1}{2}$.

<a id="ch05-ex5C-q10"></a>
##### Question 10
![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-121_411_523_1530_371.jpg) The diagram shows part of the graph of $y=\cos x$. The points $\left(\frac{\pi}{4}, \frac{\sqrt{2}}{2}\right)$ and $\left(\frac{\pi}{3}, \frac{1}{2}\right)$ lie on the curve.

**a** Find the exact value of $\int_{\frac{\pi}{4}}^{\frac{\pi}{3}} \cos x \mathrm{~d} x$.

**b** Hence show that $\int_{\frac{1}{2}}^{\frac{\sqrt{2}}{2}}\left(\cos ^{-1} y\right) \mathrm{d} y=\frac{\pi}{24}(3 \sqrt{2}-4)+\frac{\sqrt{3}-\sqrt{2}}{2}$.

## 5.4 Further integration of trigonometric functions

Sometimes, when it is not immediately obvious how to integrate a trigonometric function, we can use trigonometric identities to rewrite the function in a form that we can then integrate.

To integrate $\sin ^{2} x$ and $\cos ^{2} x$ we must use the double angle identities:

$$
\cos 2 x \equiv 1-2 \sin ^{2} x \text { and } \cos 2 x \equiv 2 \cos ^{2} x-1
$$

Rearranging these two identities gives:

$$
\sin ^{2} x \equiv \frac{1}{2}(1-\cos 2 x) \text { and } \cos ^{2} x \equiv \frac{1}{2}(1+\cos 2 x)
$$

<a id="ch05-we-5.8"></a>
#### WORKED EXAMPLE 5.8

Find:

**a** $\int \sin ^{2} x \mathrm{~d} x$

**b** $\int 3 \cos ^{2} 2 x \mathrm{~d} x$

Answer

**a**

$$
\begin{align}
\int \sin ^{2} x \mathrm{~d} x & =\frac{1}{2} \int(1-\cos 2 x) \mathrm{d} x \\
& =\frac{1}{2}\left(x-\frac{1}{2} \sin 2 x\right)+c \\
& =\frac{1}{2} x-\frac{1}{4} \sin 2 x+c
\end{align}
$$

**b**

$$
\begin{align}
\int 3 \cos ^{2} 2 x \mathrm{~d} x & =\frac{3}{2} \int(1+\cos 4 x) \mathrm{d} x \\
& =\frac{3}{2}\left(x+\frac{1}{4} \sin 4 x\right)+c \\
& =\frac{3}{2} x+\frac{3}{8} \sin 4 x+c
\end{align}
$$

<a id="ch05-we-5.9"></a>
#### WORKED EXAMPLE 5.9

Find $\int \sin ^{4} x \mathrm{~d} x$.

Answer

$$
\begin{align}
\sin ^{4} x & =\left(\sin ^{2} x\right)^{2} \\
& =\left[\frac{1}{2}(1-\cos 2 x)\right]^{2} \\
& =\frac{1}{4}\left(1-2 \cos 2 x+\cos ^{2} 2 x\right) \qquad \text { Use }^{2} \sin ^{2} x \equiv \frac{1}{2}(1-\cos 2 x) \\
& =\frac{1}{4}\left(1-2 \cos 2 x+\frac{1}{2}+\frac{1}{2} \cos 4 x\right) \\
& =\frac{3}{8}-\frac{1}{2} \cos 2 x+\frac{1}{8} \cos 4 x
\end{align}
$$

$$
\begin{align}
\int \sin ^{4} x \mathrm{~d} x & =\int\left(\frac{3}{8}-\frac{1}{2} \cos 2 x+\frac{1}{8} \cos 4 x\right) \mathrm{d} x \\
& =\frac{3}{8} x-\frac{1}{4} \sin 2 x+\frac{1}{32} \sin 4 x+c
\end{align}
$$

To integrate $\tan ^{2} x$ we use the identity $1+\tan ^{2} x \equiv \sec ^{2} x$.

Rearranging this identity gives $\tan ^{2} x \equiv \sec ^{2} x-1$.

<a id="ch05-we-5.10"></a>
#### WORKED EXAMPLE 5.10

Find the exact value of $\int_{0}^{\frac{\pi}{4}} 5 \tan ^{2} x \mathrm{~d} x$.

Answer

$$
\begin{align}
\int_{0}^{\frac{\pi}{4}} 5 \tan ^{2} x \mathrm{~d} x & =\int_{0}^{\frac{\pi}{4}}\left(5 \sec ^{2} x-5\right) \mathrm{d} x \\
& =[5 \tan x-5 x]_{0}^{\frac{\pi}{4}} \\
& =\left(5-\frac{5 \pi}{4}\right)-(0-0) \\
& =5-\frac{5 \pi}{4}
\end{align}
$$

Worked example 5.11 uses the principle that integration is the reverse process of differentiation.

<a id="ch05-we-5.11"></a>
#### WORKED EXAMPLE 5.11

**a** Show that if $y=\sec x$ then $\frac{\mathrm{d} y}{\mathrm{~d} x}=\tan x \sec x$.

**b** Hence find the exact value of $\int_{0}^{\frac{1}{4} \pi}(\cos 2 x+5 \tan x \sec x) \mathrm{d} x$.

Answer

**a**

$$
\begin{align}
y & =\frac{1}{\cos x} \\
\frac{\mathrm{~d} y}{\mathrm{~d} x} & =\frac{(\cos x)(0)-(1)(-\sin x)}{\cos ^{2} x} \\
& =\frac{\sin x}{\cos ^{2} x} \\
& =\tan x \sec x
\end{align}
$$

**b** $\int_{0}^{\frac{1}{4} \pi}(\cos 2 x+5 \tan x \sec x) \mathrm{d} x$ Use $\int \tan x \sec x \mathrm{~d} x=\sec x$.

$$
\begin{align}
& =\left[\frac{1}{2} \sin 2 x+5 \sec x\right]_{0}^{\frac{1}{4} \pi} \\
& =\left(\frac{1}{2}+5 \sqrt{2}\right)-(0+5) \\
& =5 \sqrt{2}-\frac{9}{2}
\end{align}
$$

<a id="ch05-we-5.12"></a>
#### WORKED EXAMPLE 5.12

**a** Prove that $2 \operatorname{cosec} 2 x \tan x \equiv \sec ^{2} x$.

**b** Hence find the exact value of $\int_{-\frac{1}{3} \pi}^{\frac{1}{3} \pi}(5+\operatorname{cosec} 2 x \tan x) \mathrm{d} x$.

Answer

**a**

$$
\begin{align}
2 \operatorname{cosec} 2 x \tan x & \equiv \frac{2 \tan x}{\sin 2 x} \\
& \equiv \frac{2 \sin x}{(2 \sin x \cos x) \cos x} \qquad \infty \qquad \text { Use } \tan x=\frac{\sin x}{\cos x} \text { and } \\
& \equiv \frac{1}{\cos ^{2} x} \\
& \equiv \sec ^{2} x
\end{align}
$$

**b**

$$
\begin{align}
\int_{-\frac{1}{3} \pi}^{\frac{1}{3} \pi}(5+\operatorname{cosec} 2 x \tan x) \mathrm{d} x & =\int_{-\frac{1}{3} \pi}^{\frac{1}{3} \pi}\left(5+\frac{1}{2} \sec ^{2} x\right) \mathrm{d} x \qquad \text { Use part a. } \\
& =\left[5 x+\frac{1}{2} \tan x\right]_{-\frac{1}{3} \pi}^{\frac{1}{3} \pi} \qquad \text { Simplify. } \\
& =\left(\frac{5 \pi}{3}+\frac{\sqrt{3}}{2}\right)-\left(-\frac{5 \pi}{3}-\frac{\sqrt{3}}{2}\right) \\
& =\frac{10 \pi}{3}+\sqrt{3}
\end{align}
$$

<a id="ch05-we-5.13"></a>
#### WORKED EXAMPLE 5.13

**a** Use the expansions of $\cos (3 x-x)$ and $\cos (3 x+x)$ to show that:

$$
\cos 2 x-\cos 4 x \equiv 2 \sin 3 x \sin x
$$

**b** Hence show that $\int_{0}^{\frac{1}{4} \pi} \sin 3 x \sin x \mathrm{~d} x=\frac{1}{4}$.

Answer

**a**

$$
\begin{align}
\cos 2 x-\cos 4 x & \equiv \cos (3 x-x)-\cos (3 x+x) \\
& \equiv(\cos 3 x \cos x+\sin 3 x \sin x)-(\cos 3 x \cos x-\sin 3 x \sin x) \\
& \equiv 2 \sin 3 x \sin x
\end{align}
$$

**b**

$$
\begin{align}
\int_{0}^{\frac{1}{4} \pi} \sin 3 x \sin x \mathrm{~d} x & =\frac{1}{2} \int_{0}^{\frac{1}{4} \pi}(\cos 2 x-\cos 4 x) \mathrm{d} x \\
& =\frac{1}{2}\left[\frac{1}{2} \sin 2 x-\frac{1}{4} \sin 4 x\right]_{0}^{\frac{1}{4} \pi} \qquad \text { Use part a. } \\
& =\frac{1}{2}\left[\left(\frac{1}{2}-0\right)-(0-0)\right] \\
& =\frac{1}{4}
\end{align}
$$

<a id="ch05-ex5D"></a>
### EXERCISE 5D

<a id="ch05-ex5D-q1"></a>
##### Question 1
Find:

**a** $\int 3 \cos ^{2} x \mathrm{~d} x$

**b** $\int 4 \cos ^{2}\left(\frac{x}{2}\right) \mathrm{d} x$

**c** $\int \sin ^{2} 3 x \mathrm{~d} x$

**d** $\int 2 \tan ^{2} x \mathrm{~d} x$

**e** $\int 6 \tan ^{2}(3 x) \mathrm{d} x$

**f** $\int \cos ^{4} x \mathrm{~d} x$

<a id="ch05-ex5D-q2"></a>
##### Question 2
Find the value of:

**a** $\int_{0}^{\frac{1}{3} \pi} \sin ^{2} x \mathrm{~d} x$

**b** $\quad \int_{\frac{1}{6} \pi}^{\frac{1}{3} \pi} 3 \tan ^{2} x \mathrm{~d} x$

**c** $\int_{0}^{\frac{1}{3} \pi} \cos ^{2} x \mathrm{~d} x$

**d** $\quad \int_{0}^{\frac{1}{8} \pi} \cos ^{2} 2 x \mathrm{~d} x$

**e** $\quad \int_{0}^{\frac{1}{6} \pi} 4 \sin ^{2} x \mathrm{~d} x$

**f** $\int_{0}^{\frac{1}{6} \pi} \tan ^{2} 2 x \mathrm{~d} x$

<a id="ch05-ex5D-q3"></a>
##### Question 3
Find the value of:

**a** $\int_{0}^{\frac{1}{6} \pi}\left(\cos ^{2} x-\frac{1}{\cos ^{2} x}\right) \mathrm{d} x$

**b** $\int_{0}^{\frac{1}{6} \pi}\left(\cos ^{2} x+\sin 2 x\right) \mathrm{d} x$

**c** $\int_{0}^{\frac{1}{4} \pi}(2 \sin x+\cos x)^{2} \mathrm{~d} x$

**d** $\int_{0}^{\frac{1}{3} \pi}(\cos x-3 \sin x)^{2} \mathrm{~d} x$

**e** $\quad \int_{0}^{\frac{1}{6} \pi} \frac{1+\cos ^{4} x}{\cos ^{2} x} \mathrm{~d} x$

**f** $\int_{0}^{\frac{1}{6} \pi} \frac{5}{1+\cos 4 x} \mathrm{~d} x$

<a id="ch05-ex5D-q4"></a>
##### Question 4
**a** By differentiating $\frac{\cos x}{\sin x}$, show that if $y=\cot x$ then $\frac{\mathrm{d} y}{\mathrm{~d} x}=-\operatorname{cosec}^{2} x$.

**b** Hence, show that $\int_{\frac{1}{6} \pi}^{\frac{1}{4} \pi} \operatorname{cosec}^{2} 2 x \mathrm{~d} x=\frac{\sqrt{3}}{6}$.

<a id="ch05-ex5D-q5"></a>
##### Question 5
**a** Show that $\tan x+\cot x \equiv \frac{2}{\sin 2 x}$.

**b** Hence show that $\int_{\frac{1}{3} \pi}^{\frac{1}{2} \pi} \frac{8}{\tan x+\cot x} \mathrm{~d} x=1$.

<a id="ch05-ex5D-q6"></a>
##### Question 6
**a** Use the expansions of $\sin (5 x+2 x)$ and $\sin (5 x-2 x)$ to show that:

$$
\sin 7 x+\sin 3 x \equiv 2 \sin 5 x \cos 2 x
$$

**b** Hence show that $\int_{\frac{1}{6} \pi}^{\frac{1}{3} \pi} 2 \sin 5 x \cos 2 x \mathrm{~d} x=\frac{11-3 \sqrt{3}}{42}$.

<a id="ch05-ex5D-q7"></a>
##### Question 7
**a** Show that $\sin 3 x \equiv 3 \sin x-4 \sin ^{3} x$.

**b** Hence show that $\int_{0}^{\frac{1}{3} \pi} 2 \sin ^{3} x \mathrm{~d} x=\frac{5}{12}$.

<a id="ch05-ex5D-q8"></a>
##### Question 8
**a** Show that $\cos 3 x \equiv 4 \cos ^{3} x-3 \cos x$.

**b** Hence show that $\int_{0}^{\frac{1}{6} \pi}\left(4 \cos ^{3} x+2 \cos x\right) \mathrm{d} x=\frac{17}{6}$.

<a id="ch05-ex5D-q9"></a>
##### Question 9
The diagram shows part of the curve $y=\cos x+2 \sin x$. Find the exact volume of the solid formed when the shaded region is rotated through $360^{\circ}$ about the $x$-axis.

![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-126_295_401_277_1594.jpg)

<a id="ch05-ex5D-q10"></a>
##### Question 10
**a** Show that $\sec ^{2} x+\sec x \tan x \equiv \frac{1}{1-\sin x}$.

**b** Show that if $y=\sec x$ then $\frac{\mathrm{d} y}{\mathrm{~d} x}=\sec x \tan x$.

**c** Hence show that $\int_{0}^{\frac{1}{6} \pi} \frac{4}{1-\sin 2 x} \mathrm{~d} x=2(1+\sqrt{3})$.

## 5.5 The trapezium rule

We already know that the area, $A$, under the curve $y=\mathrm{f}(x)$ between $x=a$ and $x=b$

![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-126_332_383_986_1612.jpg)

can be found by evaluating $\int_{a}^{b} \mathrm{f}(x) \mathrm{d} x$. Sometimes we might not be able to find the value of $\int_{a}^{b} \mathrm{f}(x) \mathrm{d} x$ by the integration methods that we have covered so far or maybe the function cannot be integrated algebraically.

In these situations an approximate answer can be found using a numerical method called the trapezium rule.

This numerical method involves splitting the area under the curve $y=\mathrm{f}(x)$ between $x=a$ and $x=b$ into equal width strips.

![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-126_307_790_1523_469.jpg)

The area of each trapezium-shaped strip can be found using the formula:

$$
\text { area }=\frac{1}{2}(\text { sum of parallel sides }) \times \text { width }
$$

The sum of the areas of all the strips gives an approximate value for the area under the curve and hence an approximate value for $\int_{a}^{b} \mathrm{f}(x) \mathrm{d} x$.

For the previous diagram, there are 6 strips, each of width $h$, where $h=\frac{b-a}{6}$ and the length of the vertical edges (ordinates) of the strips are $y_{0}, y_{1}, y_{2}, y_{3}, y_{4}, y_{5}$ and $y_{6}$.

The sum of the areas of the trapezium-shaped strips is:

$$
\begin{align}
& \frac{h}{2}\left(y_{0}+y_{1}\right)+\frac{h}{2}\left(y_{1}+y_{2}\right)+\frac{h}{2}\left(y_{2}+y_{3}\right)+\frac{h}{2}\left(y_{3}+y_{4}\right)+\frac{h}{2}\left(y_{4}+y_{5}\right)+\frac{h}{2}\left(y_{5}+y_{6}\right) \\
& =\frac{h}{2}\left[y_{0}+y_{6}+2\left(y_{1}+y_{2}+y_{3}+y_{4}+y_{5}\right)\right]
\end{align}
$$

When there are $n$ strips and the ordinates are $y_{0}, y_{1}, y_{2}, y_{3}, \qquad , y_{n-1}, y_{n}$ then the sum of the areas of the strips is:

$$
\frac{h}{2}\left(y_{0}+y_{1}\right)+\frac{h}{2}\left(y_{1}+y_{2}\right)+\frac{h}{2}\left(y_{2}+y_{3}\right)+\qquad +\frac{h}{2}\left(y_{n-2}+y_{n-1}\right)+\frac{h}{2}\left(y_{n-1}+y_{n}\right)
$$

Hence we can find an approximate value for $\int_{a}^{b} \mathrm{f}(x) \mathrm{d} x$ using:

<a id="ch05-kp-5.5"></a>
#### KEY POINT 5.5

$$
\int_{a}^{b} \mathrm{f}(x) \mathrm{d} x \approx \frac{h}{2}\left[y_{0}+y_{n}+2\left(y_{1}+y_{2}+y_{3}+\qquad +y_{n-1}\right)\right] \text { where } h=\frac{b-a}{n} \text {. }
$$

An easy way to remember this rule in terms of the ordinates is:

$$
\int_{a}^{b} \mathrm{f}(x) \mathrm{d} x \approx \text { half width of strip × (first }+ \text { last }+ \text { twice the sum of all the others). }
$$

<a id="ch05-we-5.14"></a>
#### WORKED EXAMPLE 5.14

The diagram shows the curve $y=x-2 \ln x$.

Use the trapezium rule with 2 intervals to estimate the shaded area, giving your answer correct to 2 decimal places. State, with a reason, whether the trapezium rule gives an under-estimate or an over-estimate of the true value.

![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-127_328_455_1150_1119.jpg)

Answer

$$
a=0.5, b=3.5 \text { and } h=1.5
$$

![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-127_303_456_1624_468.jpg)

| $\boldsymbol{x}$ | 0.5 | 2 | 3.5 |
| :--- | :--- | :--- | :--- |
| $y$ | 1.8863 | 0.6137 | 0.9945 |
|  | $y_{0}$ | $y_{1}$ | $y_{2}$ |

$$
\begin{align}
\text { Area } & \approx \frac{h}{2}\left[y_{0}+y_{2}+2 y_{1}\right] \\
& \approx \frac{1.5}{2}[1.8863+0.9945+2 \times 0.6137] \\
& \approx 3.08115 \qquad \\
& \approx 3.08 \text { (to } 2 \text { decimal places) }
\end{align}
$$

It can be seen from the diagram that this is an over-estimate since the top edges of the strips all lie above the curve.

<a id="ch05-we-5.15"></a>
#### WORKED EXAMPLE 5.15

The diagram shows the curve $y=2 \sqrt{4 x-x^{2}}$.

Use the trapezium rule with 4 intervals to estimate the value of $\int_{0}^{4} 2 \sqrt{4 x-x^{2}} \mathrm{~d} x$ giving your answer correct to 2 decimal places. State, with a reason, whether the trapezium rule gives an under-estimate or an over-estimate of the true value.

Answer

$$
a=0, b=4 \text { and } h=1
$$

| $\boldsymbol{x}$ | 0 | 1 | 2 | 3 | 4 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| $y$ | 0 | $2 \sqrt{3}$ | 4 | $2 \sqrt{3}$ | 0 |
|  | $y_{0}$ | $y_{1}$ | $y_{2}$ | $y_{3}$ | $y_{4}$ |

![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-128_219_468_859_1056.jpg)

$$
\begin{align}
\int_{0}^{4} 2 \sqrt{4 x-x^{2}} \mathrm{~d} x & \approx \frac{h}{2}\left[y_{0}+y_{4}+2\left(y_{1}+y_{2}+y_{3}\right)\right] \\
& \approx \frac{1}{2}[0+0+2(2 \sqrt{3}+4+2 \sqrt{3})] \\
& \approx 4 \sqrt{3}+4 \\
& \approx 10.93 \text { (to } 2 \text { decimal places) }
\end{align}
$$

It can be seen from the diagram that this is an under-estimate since the top edges of the strips all lie below the curve.

Worked example 5.14 involves a 'concave' curve and the diagram shows that the trapezium rule gives an over-estimate for the area.

Worked example 5.15 involves a 'convex' curve and the diagram shows that the trapezium rule gives an under-estimate for the area.

If a curve is partially convex and partially concave over the required interval it is not so easy to predict whether the trapezium rule will give an under-estimate or an over-estimate for the area.

The more strips that are used, the more accurate the estimate will be.

<a id="ch05-ex5E"></a>
### EXERCISE 5E

<a id="ch05-ex5E-q1"></a>
##### Question 1
Use the trapezium rule with 2 intervals to estimate the value of each of these definite integrals. Give your answers correct to 2 decimal places.

**a** $\int_{2}^{4} \sqrt{x^{2}-2} \mathrm{~d} x$

**b** $\int_{0}^{2}\left|\mathrm{e}^{x}-12\right| \mathrm{d} x$

**c** $\int_{0}^{4} \frac{2}{3+\mathrm{e}^{x}} \mathrm{~d} x$

**d** $\int_{1}^{7} \frac{2}{\ln (x+5)} \mathrm{d} x$

**e** $\int_{0}^{\frac{1}{3} \pi} \frac{1}{2+\tan x} \mathrm{~d} x$

**f** $\quad \int_{2}^{12} \log _{10} x \mathrm{~d} x$

![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-128_218_469_395_1071.jpg)

| $\boldsymbol{x}$ | 0 | 1 | 2 | 3 | 4 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| $y$ | 0 | $2 \sqrt{3}$ | 4 | $2 \sqrt{3}$ | 0 |
|  | $y_{0}$ | $y_{1}$ | $y_{2}$ | $y_{3}$ | $y_{4}$ |

#### DID YOU KNOW?

If you double the number of strips in a trapezium rule approximation, the error reduces to approximately one quarter the previous error.

**2** ![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-129_201_378_278_370.jpg) The diagram shows part of the curve $y=x^{2} \mathrm{e}^{-x}$. Use the trapezium rule with 4 intervals to estimate the value of $\int_{1}^{5} x^{2} \mathrm{e}^{-x} \mathrm{~d} x$, giving your answer correct to 2 decimal places.

**3** **a** Use the trapezium rule with 6 intervals to estimate the value of $\int_{\frac{1}{4} \pi}^{\frac{7}{4} \pi} \operatorname{cosec}\left(\frac{1}{2} x\right) \mathrm{d} x$, giving your answer correct to 2 decimal places.

**b** Use a sketch of the graph of $y=\operatorname{cosec}\left(\frac{1}{2} x\right)$ for $0 \leqslant x \leqslant 2 \pi$, to explain whether the trapezium rule gives an under-estimate or an over-estimate of the true value of $\int_{\frac{1}{4} \pi}^{\frac{7}{4} \pi} \operatorname{cosec}\left(\frac{1}{2} x\right) \mathrm{d} x$.

**4** ![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-129_338_403_1230_372.jpg) The diagram shows the curve $y=\mathrm{e}^{x} \cos x$ for $0 \leqslant x \leqslant \frac{1}{2} \pi$. Use the trapezium rule with 3 intervals to estimate the value of $\int_{0}^{\frac{1}{2} \pi} \mathrm{e}^{x} \cos x \mathrm{~d} x$, giving your answer correct to 2 decimal places. State, with a reason, whether the trapezium rule gives an under-estimate or an over-estimate of the true value of $\int_{0}^{\frac{1}{2} \pi} \mathrm{e}^{x} \cos x \mathrm{~d} x$.

**5** ![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-129_257_499_1963_369.jpg) The diagram shows part of the curve $y=\frac{\mathrm{e}^{x}}{2 x}$. Use the trapezium rule with 4 intervals to estimate the area of the shaded region, giving your answer correct to 2 decimal places.

State, with a reason, whether the trapezium rule gives an under-estimate or an over-estimate of the true value of the shaded area.

### Checklist of learning and understanding

Integration formulae

- $\int \mathrm{e}^{x} \mathrm{~d} x=\mathrm{e}^{x}+c$ $\int \mathrm{e}^{a x+b} \mathrm{~d} x=\frac{1}{a} \mathrm{e}^{a x+b}+c$

- $\int \frac{1}{x} \mathrm{~d} x=\ln |x|+c$ $\int \frac{1}{a x+b} \mathrm{~d} x=\frac{1}{a} \ln |a x+b|+c$

- $\int \cos x \mathrm{~d} x=\sin x+c$ $\int \cos (a x+b) \mathrm{d} x=\frac{1}{a} \sin (a x+b)+c$

- $\int \sin x \mathrm{~d} x=-\cos x+c$ $\int \sin (a x+b) \mathrm{d} x=-\frac{1}{a} \cos (a x+b)+c$

- $\int \sec ^{2} x \mathrm{~d} x=\tan x+c$ $\int \sec ^{2}(a x+b) \mathrm{d} x=\frac{1}{a} \tan (a x+b)+c$

The trapezium rule

- The trapezium rule can be used to find an approximate value for $\int_{a}^{b} \mathrm{f}(x) \mathrm{d} x$. If the region under the curve is divided into $n$ strips each of width $h$, then:

$$
\int_{a}^{b} \mathrm{f}(x) \mathrm{d} x \approx \frac{h}{2}\left[y_{0}+y_{n}+2\left(y_{1}+y_{2}+y_{3}+\qquad +y_{n-1}\right)\right] \text { where } h=\frac{b-a}{n} \text {. }
$$

<a id="ch05-review"></a>
### END-OF-CHAPTER REVIEW EXERCISE 5

<a id="ch05-review-q1"></a>
##### Question 1
Show that $\int_{\frac{1}{6} \pi}^{\frac{1}{3} \pi}\left(1+2 \tan ^{2} x\right) \mathrm{d} x=\frac{4 \sqrt{3}}{3}-\frac{\pi}{6}$. `[4]`

<a id="ch05-review-q2"></a>
##### Question 2
Find the exact value of $\int_{-4}^{-2}\left(\frac{4}{1-2 x}-2 x\right) \mathrm{d} x$, giving your answer in the form $a+\ln \left(\frac{b}{c}\right)$, where $a, b$ and $c$ are integers. `[4]`

<a id="ch05-review-q3"></a>
##### Question 3
![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-131_283_559_726_834.jpg) The diagram shows part of the curve $y=2-x^{2} \ln (x+1)$. The shaded region $R$ is bounded by the curve and by the lines $x=0, x=1$ and $y=0$. Use the trapezium rule with 4 intervals to estimate the area of $R$ giving your answer correct to 2 decimal places. State, with a reason, whether the trapezium rule gives an under-estimate or an over-estimate of the true value of the area of $R$. `[4]`

<a id="ch05-review-q4"></a>
##### Question 4
Find the exact value of $\int_{0}^{\frac{1}{6} \pi}(\cos 3 x-\sin 2 x) \mathrm{d} x$. `[5]`

<a id="ch05-review-q5"></a>
##### Question 5
Show that $\int_{0}^{1}\left(3 \mathrm{e}^{x}-2\right)^{2} \mathrm{~d} x=\frac{9}{2} \mathrm{e}^{2}-12 \mathrm{e}+\frac{23}{2}$. `[5]`

<a id="ch05-review-q6"></a>
##### Question 6
**a** Find $\int_{0}^{k}\left(5 \mathrm{e}^{-2 x}+2 \mathrm{e}^{-3 x}\right) \mathrm{d} x$, where $k$ is a positive constant. `[4]`

**b** Hence find the exact value of $\int_{0}^{\infty}\left(5 \mathrm{e}^{-2 x}+2 \mathrm{e}^{-3 x}\right) \mathrm{d} x$. `[1]`

<a id="ch05-review-q7"></a>
##### Question 7
Show that $\int_{2}^{4} \frac{3}{5 x+1} \mathrm{~d} x=\frac{3}{5} \ln \frac{21}{11}$. `[5]`

<a id="ch05-review-q8"></a>
##### Question 8
**a** Find the value of the constant $A$ such that $\frac{8 x}{2 x+5} \equiv 4+\frac{A}{2 x+5}$. `[2]`

**b** Hence show that $\int_{1}^{3} \frac{8 x}{2 x+5} \mathrm{~d} x=8-10 \ln \frac{11}{7}$. `[5]`

<a id="ch05-review-q9"></a>
##### Question 9
**i** Show that $12 \sin ^{2} x \cos ^{2} x \equiv \frac{3}{2}(1-\cos 4 x)$. `[3]`

**ii** Hence show that $\int_{\frac{1}{4} \pi}^{\frac{1}{3} \pi} 12 \sin ^{2} x \cos ^{2} x \mathrm{~d} x=\frac{\pi}{8}+\frac{3 \sqrt{3}}{16}$. `[3]`

##

*Cambridge International AS \& A Level Mathematics 9709 Paper 21 Q3 June 2013*

<a id="ch05-review-q10"></a>
##### Question 10
**a** Find $\int 4 \mathrm{e}^{x}\left(3+\mathrm{e}^{2 x}\right) \mathrm{d} x$. `[3]`

**b** Show that $\int_{-\frac{1}{4} \pi}^{\frac{1}{4} \pi}\left(3+2 \tan ^{2} \theta\right) \mathrm{d} \theta=\frac{1}{2}(8+\pi)$. `[4]`

<a id="ch05-review-q11"></a>
##### Question 11
**i** Show that $(2 \sin x+\cos x)^{2}$ can be written in the form $\frac{5}{2}+2 \sin 2 x-\frac{3}{2} \cos 2 x$. `[5]`

**ii** Hence find the exact value of $\int_{0}^{\frac{1}{4} \pi}(2 \sin x+\cos x)^{2} \mathrm{~d} x$. `[4]`

*Cambridge International AS \& A Level Mathematics 9709 Paper 21 Q7 June 2012*

<a id="ch05-review-q12"></a>
##### Question 12
**i** By differentiating $\frac{\cos x}{\sin x}$, show that if $y=\cot x$ then $\frac{\mathrm{d} y}{\mathrm{~d} x}=-\operatorname{cosec}^{2} x$. `[3]`

**ii** By expressing $\cot ^{2} x$ in terms of $\operatorname{cosec}^{2} x$ and using the result of part i, show that $\int_{\frac{1}{4} \pi}^{\frac{1}{2} \pi} \cot ^{2} x \mathrm{~d} x=1-\frac{1}{4} \pi$. `[4]`

**iii** Express $\cos 2 x$ in terms of $\sin ^{2} x$ and hence show that $\frac{1}{1-\cos 2 x}$ can be expressed as $\frac{1}{2} \operatorname{cosec}^{2} x$. Hence, using the result of part i, find $\int \frac{1}{1-\cos 2 x} \mathrm{~d} x$. `[3]`

*Cambridge International AS \& A Level Mathematics 9709 Paper 21 Q8 June 2010*

<a id="ch05-review-q13"></a>
##### Question 13
**i** Find $\int \frac{1+\cos ^{4} 2 x}{\cos ^{2} 2 x} \mathrm{~d} x$. `[3]`

**ii** Without using a calculator, find the exact value of $\int_{4}^{14}\left(2+\frac{6}{3 x-2}\right) \mathrm{d} x$, giving your answer in the form $\ln \left(a \mathrm{e}^{b}\right)$, where $a$ and $b$ are integers. `[5]`

*Cambridge International AS \& A Level Mathematics 9709 Paper 21 Q7 June 2016*

<a id="ch05-review-q14"></a>
##### Question 14
![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-132_324_461_1576_806.jpg)

The diagram shows the curve $y=x \sin x$, for $0 \leqslant x \leqslant \pi$. The point $Q\left(\frac{1}{2} \pi, \frac{1}{2} \pi\right)$ lies on the curve.

**i** Show that the normal to the curve at Q passes through the point $(\pi, 0)$. `[5]`

**ii** Find $\frac{\mathrm{d}}{\mathrm{d} x}(\sin x-x \cos x)$. `[2]`

**iii** Hence evaluate $\int_{0}^{\frac{1}{2} \pi} x \sin x \mathrm{~d} x$. `[3]`

*Cambridge International AS \& A Level Mathematics 9709 Paper 21 Q8 November 2010*

<a id="ch05-review-q15"></a>
##### Question 15
**i** Using the expansion of $\cos (3 x-x)$ and $\cos (3 x+x)$, prove that $\frac{1}{2}(\cos 2 x-\cos 4 x) \equiv \sin 3 x \sin x$. `[3]`

**ii** Hence show that $\int_{\frac{1}{6} \pi}^{\frac{1}{3} \pi} \sin 3 x \sin x \mathrm{~d} x=\frac{1}{8} \sqrt{3}$. `[3]`

![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-133_1344_1941_4_137.jpg)
