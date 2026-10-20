# Chapter 8: Further calculus

This chapter is for Pure Mathematics 3 students only.

In this chapter you will learn how to:

- use the derivative of $\tan ^{-1} x$

- extend the ideas of 'reverse differentiation' to include the integration of $\frac{1}{x^{2}+a^{2}}$

- recognise an integrand of the form $\frac{k \mathrm{f}^{\prime}(x)}{\mathrm{f}(x)}$, and integrate such functions

- use a given substitution to simplify and evaluate either a definite or an indefinite integral

- integrate rational functions by means of decomposition into partial fractions

- recognise when an integrand can usefully be regarded as a product, and use integration by parts.

<a id="ch08-prerequisite"></a>
### PREREQUISITE KNOWLEDGE

| Where it comes from | What you should be able to do | Check your skills |
| :--- | :--- | :--- |
| Chapter 4 | Differentiate $\mathrm{e}^{x}, \ln x, \sin x, \cos x$ and $\tan x$. | 1 Differentiate with respect to $x$.<br>a $\sin 3 x$<br>b $\mathrm{e}^{x^{2}+1}$<br>c $\quad \ln (5 x-3)$<br>d $\tan 2 x-5 \cos x$<br> |
| Chapter 5 | Integrate $\mathrm{e}^{a x+b}, \frac{1}{a x+b}, \sin (a x+b)$, $\cos (a x+b)$ and $\sec ^{2}(a x+b)$ and use trigonometrical relationships in carrying out integration. | 2 Find each of these integrals.<br>a $\int \mathrm{e}^{5 x+1} \mathrm{~d} x$<br>b $\int \sin ^{2} 2 x \mathrm{~d} x$<br>c $\int \frac{5}{3 x-2} \mathrm{~d} x$<br>d $\quad \int \sec ^{2}(3 x) \mathrm{d} x$<br> |
| Chapter 7 | Express rational functions as partial fractions. | 3 Express in partial fractions.<br>a $\frac{2 x}{(x-1)(x+3)}$<br>b $\frac{4 x^{2}-6}{x\left(x^{2}+2\right)}$<br>c $\frac{5}{x(x-1)^{2}}$<br>d $\frac{3 x^{2}-3 x-3}{x^{2}-x-2}$<br> |

### Why do we study calculus?

This chapter will further extend your knowledge and skills in differentiation and integration.

In particular, we will learn about integration by substitution and integration by parts, which can be considered as the 'reverse process' of the chain rule and the product rule for differentiation that we learnt about earlier in this course. These new rules will enable you to integrate many more functions than you could previously.

The skills that we learn in this chapter will be very important when studying Chapter 10. Chapter 10 is about solving differential equations, many of which model real-life situations.

Integration by parts plays a major role in engineering and its application is often found in problems including electric circuits, heat transfer, vibrations, structures, fluid mechanics, air pollution, electromagnetics and digital signal processing.

## 8.1 Derivative of $\boldsymbol{\operatorname { t a n }}^{-\mathbf{1}} \boldsymbol{x}$

The function $y=\tan ^{-1} x$ can be written as:

$$
\begin{align}
\tan y & =x & & \text { Differentiate both sides with respect to } x . \\
\sec ^{2} y \frac{\mathrm{~d} y}{\mathrm{~d} x} & =1 & & \\
\frac{\mathrm{~d} y}{\mathrm{~d} x} & =\frac{1}{\sec ^{2} y} & & \text { Use } \sec ^{2} y=1+\tan ^{2} y . \\
\frac{\mathrm{d} y}{\mathrm{~d} x} & =\frac{1}{1+\tan ^{2} y} & & \text { Use } \tan y=x . \\
\frac{\mathrm{d} y}{\mathrm{~d} x} & =\frac{1}{1+x^{2}} & &
\end{align}
$$

<a id="ch08-kp-8.1"></a>
#### KEY POINT 8.1

$$
\frac{\mathrm{d}}{\mathrm{~d} x}\left(\tan ^{-1} x\right)=\frac{1}{x^{2}+1}
$$

<a id="ch08-we-8.1"></a>
#### WORKED EXAMPLE 8.1

Differentiate with respect to $x$.

**a** $\tan ^{-1} 3 x$

**b** $\tan ^{-1} \sqrt{x}$

**c** $\tan ^{-1}\left(\frac{x}{x-2}\right)$

Answer

**a**

$$
\begin{align}
\frac{\mathrm{d}}{\mathrm{~d} x}\left(\tan ^{-1} 3 x\right) & =\frac{1}{(3 x)^{2}+1} \times 3 \\
& =\frac{3}{9 x^{2}+1}
\end{align}
$$

**b**

$$
\begin{align}
\frac{\mathrm{d}}{\mathrm{~d} x}\left(\tan ^{-1} \sqrt{x}\right) & =\frac{1}{(\sqrt{x})^{2}+1} \times \frac{1}{2} x^{-\frac{1}{2}} \\
& =\frac{1}{x+1} \times \frac{1}{2 \sqrt{x}} \\
& =\frac{1}{2 \sqrt{x}(x+1)}
\end{align}
$$

**c** $\frac{\mathrm{d}}{\mathrm{d} x}\left[\tan ^{-1}\left(\frac{x}{x-2}\right)\right]=\frac{1}{\left(\frac{x}{x-2}\right)^{2}+1} \times \frac{\mathrm{d}}{\mathrm{d} x}\left(\frac{x}{x-2}\right)$ Chain rule and quotient rule.

$$
\begin{align}
& =\frac{(x-2)^{2}}{x^{2}+(x-2)^{2}} \times \frac{(x-2)(1)-(x)(1)}{(x-2)^{2}} \qquad \text { Simplify. } \\
& =\frac{-2}{2 x^{2}-4 x+4} \\
& =\frac{-1}{x^{2}-2 x+2}
\end{align}
$$

<a id="ch08-ex8A"></a>
### EXERCISE 8A

<a id="ch08-ex8A-q1"></a>
##### Question 1
Differentiate with respect to $x$.

**a** $\tan ^{-1} 2 x$

**b** $\tan ^{-1} 5 x$

**c** $\tan ^{-1} \frac{x}{3}$

**d** $\tan ^{-1}(x-1)$

**e** $\tan ^{-1} x^{2}$

**f** $\tan ^{-1}\left(\frac{2 x}{x+1}\right)$

<a id="ch08-ex8A-q2"></a>
##### Question 2
Differentiate with respect to $x$.

**a** $x \tan ^{-1} x$

**b** $\frac{\tan ^{-1} 2 x}{x}$

**c** $\mathrm{e}^{x} \tan ^{-1} x$

<a id="ch08-ex8A-q3"></a>
##### Question 3
Find the equation of the tangent to the curve $y=\tan ^{-1}\left(\frac{x}{2}\right)$ at the point where $x=2$.

<a id="ch08-ex8A-q4"></a>
##### Question 4
Show that the tangent to the curve $y=\tan ^{-1} x$ at the point where $x=-1$ is perpendicular to the normal to the curve at the point where $x=1$. Find the $x$-coordinate of the point where this tangent and normal intersect.

## 8.2 Integration of $\frac{\mathbf{1}}{\boldsymbol{x}^{\mathbf{2}}+\boldsymbol{a}^{\mathbf{2}}}$

Since integration is the reverse process of differentiation we can say that:

<a id="ch08-kp-8.2"></a>
#### KEY POINT 8.2

$$
\int \frac{1}{x^{2}+1} \mathrm{~d} x=\tan ^{-1} x+c
$$

This can be extended to:

$$
\int \frac{1}{x^{2}+a^{2}} \mathrm{~d} x=\frac{1}{a} \tan ^{-1} \frac{x}{a}+c
$$

<a id="ch08-we-8.2"></a>
#### WORKED EXAMPLE 8.2

Find $\int \frac{1}{x^{2}+25} \mathrm{~d} x$.

Answer

$$
\int \frac{1}{x^{2}+25} \mathrm{~d} x=\frac{1}{5} \tan ^{-1} \frac{x}{5}+c
$$

<a id="ch08-we-8.3"></a>
#### WORKED EXAMPLE 8.3

Find $\int \frac{1}{2 x^{2}+3} \mathrm{~d} x$.

Answer

$$
\begin{align}
\int \frac{1}{2 x^{2}+3} \mathrm{~d} x & =\frac{1}{2} \int \frac{1}{x^{2}+\frac{3}{2}} \mathrm{~d} x \\
& =\frac{1}{2} \times \sqrt{\frac{2}{3}} \tan ^{-1}\left(\frac{x}{\sqrt{\frac{3}{2}}}\right)+c \\
& =\frac{1}{2} \sqrt{\frac{2}{3}} \tan ^{-1}\left(\sqrt{\frac{2}{3}} x\right)+c
\end{align}
$$

<a id="ch08-we-8.4"></a>
#### WORKED EXAMPLE 8.4

Find the exact value of $\int_{0}^{2} \frac{1}{x^{2}+4} \mathrm{~d} x$.

Answer

$$
\begin{align}
\int_{0}^{2} \frac{1}{x^{2}+4} \mathrm{~d} x & =\left[\frac{1}{2} \tan ^{-1} \frac{x}{2}\right]_{0}^{2} \\
& =\left(\frac{1}{2} \tan ^{-1} 1\right)-\left(\frac{1}{2} \tan ^{-1} 0\right) \\
& =\left(\frac{1}{2} \times \frac{\pi}{4}\right)-\left(\frac{1}{2} \times 0\right) \\
& =\frac{\pi}{8}
\end{align}
$$

<a id="ch08-ex8B"></a>
### EXERCISE 8B

<a id="ch08-ex8B-q1"></a>
##### Question 1
Find the following integrals.

**a** $\int \frac{1}{x^{2}+9} \mathrm{~d} x$

**b** $\int \frac{1}{16+x^{2}} \mathrm{~d} x$

**c** $\int \frac{1}{4 x^{2}+1} \mathrm{~d} x$

**d** $\quad \int \frac{1}{9 x^{2}+16} \mathrm{~d} x$

**e** $\int \frac{1}{4 x^{2}+3} \mathrm{~d} x$

**f** $\quad \int \frac{1}{2+3 x^{2}} \mathrm{~d} x$

<a id="ch08-ex8B-q2"></a>
##### Question 2
Find the exact value of each of these integrals.

**a** $\int_{0}^{3} \frac{1}{x^{2}+9} \mathrm{~d} x$

**b** $\int_{0}^{\frac{1}{2}} \frac{2}{4 x^{2}+1} \mathrm{~d} x$

**c** $\int_{-\sqrt{2}}^{\sqrt{2}} \frac{1}{3 x^{2}+2} \mathrm{~d} x$

<a id="ch08-ex8B-q3"></a>
##### Question 3
The diagram shows part of the curve $y=\frac{2}{\sqrt{x^{2}+1}}$. Find the exact value of the volume of the solid formed when the shaded region is rotated completely about the $x$-axis.

![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-188_276_537_2281_1455.jpg)

## 8.3 Integration of $\frac{\boldsymbol{k} \mathbf{f}^{\prime}(\boldsymbol{x})}{\mathbf{f}(\boldsymbol{x})}$

Since integration is the reverse process of differentiation and $\ln x$ only exists for $x>0$, we can say that:

<a id="ch08-kp-8.3"></a>
#### KEY POINT 8.3

$$
\int \frac{\mathrm{f}^{\prime}(x)}{\mathrm{f}(x)} \mathrm{d} x=\ln |\mathrm{f}(x)|+c
$$

This can be extended to:

$$
\int \frac{k \mathrm{f}^{\prime}(x)}{\mathrm{f}(x)} \mathrm{d} x=k \ln |\mathrm{f}(x)|+c
$$

<a id="ch08-we-8.5"></a>
#### WORKED EXAMPLE 8.5

Find $\int \frac{2 x}{x^{2}+3} \mathrm{~d} x$.

Answer

If $\mathrm{f}(x)=x^{2}+3$ then $\mathrm{f}^{\prime}(x)=2 x$.

$$
\therefore \int \frac{2 x}{x^{2}+3} \mathrm{~d} x=\ln \left|x^{2}+3\right|+c
$$

<a id="ch08-we-8.6"></a>
#### WORKED EXAMPLE 8.6

Find $\int \tan 3 x \mathrm{~d} x$.

Answer

$$
\int \tan 3 x d x=\int \frac{\sin 3 x}{\cos 3 x} d x
$$

If $\mathrm{f}(x)=\cos 3 x$ then $\mathrm{f}^{\prime}(x)=-3 \sin 3 x$.

$$
\begin{align}
\int \tan 3 x \mathrm{~d} x & =-\frac{1}{3} \int \frac{-3 \sin 3 x}{\cos 3 x} \mathrm{~d} x \\
& =-\frac{1}{3} \ln |\cos 3 x|+c
\end{align}
$$

<a id="ch08-we-8.7"></a>
#### WORKED EXAMPLE 8.7

Find $\int \frac{3 x^{2}+5 x}{2 x^{3}+5 x^{2}} \mathrm{~d} x$.

Answer

If $\mathrm{f}(x)=2 x^{3}+5 x^{2}$ then $\mathrm{f}^{\prime}(x)=6 x^{2}+10 x$.

$$
\begin{align}
\int \frac{3 x^{2}+5 x}{2 x^{3}+5 x^{2}} \mathrm{~d} x & =\frac{1}{2} \int \frac{6 x^{2}+10 x}{2 x^{3}+5 x^{2}} \mathrm{~d} x \\
& =\frac{1}{2} \ln \left|2 x^{3}+5 x^{2}\right|+c
\end{align}
$$

<a id="ch08-we-8.8"></a>
#### WORKED EXAMPLE 8.8

Find $\int_{0}^{1} \frac{2 \mathrm{e}^{x}}{1+\mathrm{e}^{x}} \mathrm{~d} x$

Answer

If $\mathrm{f}(x)=1+\mathrm{e}^{x}$ then $\mathrm{f}^{\prime}(x)=\mathrm{e}^{x}$.

$$
\begin{align}
\int_{0}^{1} \frac{2 \mathrm{e}^{x}}{1+\mathrm{e}^{x}} \mathrm{~d} x & =2 \int_{0}^{1} \frac{\mathrm{e}^{x}}{1+\mathrm{e}^{x}} \mathrm{~d} x \\
& =\left[2 \ln \left|1+\mathrm{e}^{x}\right|\right]_{0}^{1} \\
& =2 \ln (1+\mathrm{e})-2 \ln 2 \\
& =2 \ln \left(\frac{1+\mathrm{e}}{2}\right)
\end{align}
$$

<a id="ch08-ex8C"></a>
### EXERCISE 8C

<a id="ch08-ex8C-q1"></a>
##### Question 1
Find the following integrals.

**a** $\int \frac{6 x^{2}}{x^{3}-1} \mathrm{~d} x$

**b** $\int \frac{\cos x}{1+\sin x} \mathrm{~d} x$

**c** $\int \frac{4 x-10}{x^{2}-5 x+1} \mathrm{~d} x$

**d** $\int \cot x \mathrm{~d} x$

**e** $\int \frac{x}{2-x^{2}} \mathrm{~d} x$

**f** $\quad \int \frac{\sec ^{2} x}{1+\tan x} \mathrm{~d} x$

<a id="ch08-ex8C-q2"></a>
##### Question 2
Find the exact value of each of these integrals.

**a** $\int_{\frac{1}{6} \pi}^{\frac{1}{4} \pi} \tan x \mathrm{~d} x$

**b** $\int_{0}^{2} \frac{3 x^{2}}{x^{3}+2} \mathrm{~d} x$

**c** $\quad \int_{0}^{\ln 2} \frac{\mathrm{e}^{2 x}}{1+\mathrm{e}^{2 x}} \mathrm{~d} x$

**d** $\quad \int_{1}^{2} \frac{x+1}{x^{2}+2 x-1} \mathrm{~d} x$

**e** $\quad \int_{\frac{1}{6} \pi}^{\frac{1}{4} \pi} \cot x \mathrm{~d} x$

**f** $\quad \int_{0}^{1} \frac{2 x+3}{(x+1)(x+2)} \mathrm{d} x$

<a id="ch08-ex8C-q3"></a>
##### Question 3
Show that $\int \frac{\mathrm{e}^{x}+\mathrm{e}^{-x}}{\mathrm{e}^{x}-\mathrm{e}^{-x}} \mathrm{~d} x=\ln \left(1-\mathrm{e}^{2 x}\right)-x+c$.

<a id="ch08-ex8C-q4"></a>
##### Question 4
Show that $\int_{\frac{1}{3} \pi}^{\frac{1}{4} \pi} \frac{\sin x \cos x}{1-2 \cos 2 x} \mathrm{~d} x=-\frac{1}{8} \ln 2$.

<a id="ch08-ex8C-q5"></a>
##### Question 5

![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-191_273_522_278_379.jpg)

The diagram shows part of the curve $y=\frac{4 x}{x^{2}+1}$. Find the exact value of $p$ for which the shaded region has an area of 4 .

## 8.4 Integration by substitution

Integration by substitution can be considered as the reverse process of differentiation by the chain rule.

This method is used when a simple substitution can be applied that will transform a difficult integral into an easier integral. The integral must be completely rewritten in terms of the new variable.

<a id="ch08-we-8.9"></a>
#### WORKED EXAMPLE 8.9

Use the substitution $u=2 x+1$ to find $\int 4 x \sqrt{2 x+1} \mathrm{~d} x$.

Answer

$$
\begin{align}
& u=2 x+1 \Rightarrow x=\frac{u-1}{2} \\
& u=2 x+1 \Rightarrow \frac{\mathrm{~d} u}{\mathrm{~d} x}=2 \Rightarrow \mathrm{~d} x=\frac{\mathrm{d} u}{2}
\end{align}
$$

$$
\begin{align}
\int 4 x \sqrt{2 x+1} \mathrm{~d} x & =\int 4\left(\frac{u-1}{2}\right) \sqrt{u} \frac{\mathrm{~d} u}{2} \\
& =\int\left(u^{\frac{3}{2}}-u^{\frac{1}{2}}\right) \mathrm{d} u \qquad \text { Sewrite the integral in terms of } u \text { and simplify. } \\
& =\frac{2}{5} u^{\frac{5}{2}}-\frac{2}{3} u^{\frac{3}{2}}+c \\
& =\frac{2}{5}(2 x+1)^{\frac{5}{2}}-\frac{2}{3}(2 x+1)^{\frac{3}{2}}+c
\end{align}
$$

<a id="ch08-we-8.10"></a>
#### WORKED EXAMPLE 8.10

Use the substitution $x=2 \tan u$ to find $\int \frac{8}{x^{2}+4} \mathrm{~d} x$.

Answer

$$
\begin{align}
x=2 \tan u & \Rightarrow x^{2}=4 \tan ^{2} u \\
x=2 \tan u & \Rightarrow \frac{\mathrm{~d} x}{\mathrm{~d} u}=2 \sec ^{2} u \Rightarrow \mathrm{~d} x=2 \sec ^{2} u \mathrm{~d} u \\
\int \frac{8}{x^{2}+4} \mathrm{~d} x & =\int\left(\frac{8}{4 \tan ^{2} u+4}\right) 2 \sec ^{2} u \mathrm{~d} u \quad \text { Rewrite the integral in terms of } u \text { and simplify. } \\
& =\int \frac{16 \sec ^{2} u}{4 \tan ^{2} u+4} \mathrm{~d} u \quad \text { Se } \tan ^{2} u+1 \equiv \sec ^{2} u . \\
& =\int \frac{16 \sec ^{2} u}{4 \sec ^{2} u} \mathrm{~d} u \quad \text { Simplify. } \\
& =\int 4 \mathrm{~d} u \\
& =4 u+c \\
& =4 \tan ^{-1}\left(\frac{x}{2}\right)+c
\end{align}
$$

<a id="ch08-we-8.11"></a>
#### WORKED EXAMPLE 8.11

Use the substitution $u=\sin x$ to find $\int \sin ^{2} 2 x \cos x \mathrm{~d} x$.

Answer

$$
\begin{align}
u=\sin x \Rightarrow \sin ^{2} 2 x & =(2 \sin x \cos x)^{2} \\
& =4 \sin ^{2} x \cos ^{2} x \\
& =4 u^{2}(1-u)^{2} \\
u=\sin x \Rightarrow \frac{\mathrm{~d} u}{\mathrm{~d} x}= & \cos x \Rightarrow \mathrm{~d} x=\frac{\mathrm{d} u}{\cos x}
\end{align}
$$

$$
\begin{align}
\int \sin ^{2} 2 x \cos x \mathrm{~d} x & =\int \sin ^{2} 2 x \cos x \frac{\mathrm{~d} u}{\cos x} \quad \text { Replace } \mathrm{d} x \text { by } \frac{\mathrm{d} u}{\cos x} \text { and simplify. } \\
& =\int \sin ^{2} 2 x \mathrm{~d} u \\
& =\int\left(4 u^{2}-4 u^{4}\right) \mathrm{d} u \qquad \text { Replace } \sin ^{2} 2 x \text { by } 4 u^{2}-4 u^{4} . \\
& =\frac{4}{3} u^{3}-\frac{4}{5} u^{5}+c \qquad \text { Integrate with respect to } u . \\
& =\frac{4}{3} \sin ^{3} x-\frac{4}{5} \sin ^{5} x+c \quad \text { Rewrite in terms of } x .
\end{align}
$$

<a id="ch08-we-8.12"></a>
#### WORKED EXAMPLE 8.12

Use the substitution $u=x+1$ to find $\int_{0}^{3} \frac{x}{\sqrt{x+1}} \mathrm{~d} x$.

Answer

$$
\begin{align}
& u=x+1 \Rightarrow x=u-1 \\
& u=x+1 \Rightarrow \frac{\mathrm{~d} u}{\mathrm{~d} x}=1 \Rightarrow \mathrm{~d} x=\mathrm{d} u
\end{align}
$$

Find the new limits for $u$ :

$$
\begin{align}
& x=3 \Rightarrow u=3+1=4 \\
& x=0 \Rightarrow u=0+1=1
\end{align}
$$

$$
\begin{align}
\int_{x=0}^{x=3} \frac{x}{\sqrt{x+1}} \mathrm{~d} x & =\int_{u=1}^{u=4} \frac{u-1}{\sqrt{u}} \mathrm{~d} u \\
& =\int_{1}^{4}\left(u^{\frac{1}{2}}-u^{-\frac{1}{2}}\right) \mathrm{d} u \qquad \text { Write the integral in terms of } u \text { and simplify } \\
& =\left[\frac{2}{3} u^{\frac{3}{2}}-2 u^{\frac{1}{2}}\right]_{1}^{4} \\
& =\left(\frac{16}{3}-4\right)-\left(\frac{2}{3}-2\right) \\
& =\frac{8}{3}
\end{align}
$$

<a id="ch08-ex8D"></a>
### EXERCISE 8D

<a id="ch08-ex8D-q1"></a>
##### Question 1
Given that $I=\int \frac{x}{\sqrt{x^{2}-3}} \mathrm{~d} x$, use the substitution $u=x^{2}-3$ to show that $I=\frac{1}{2} \int \frac{1}{\sqrt{u}} \mathrm{~d} u$. Hence find $I$.

<a id="ch08-ex8D-q2"></a>
##### Question 2
Find these integrals, using the given substitution.

**a** $\int \frac{x}{(x+2)^{4}} \mathrm{~d} x, u=x+2$

**b** $\int x \sqrt{1-2 x^{2}} \mathrm{~d} x, u=1-2 x^{2}$

**c** $\int \cos x \sin ^{5} x \mathrm{~d} x, u=\sin x$

**d** $\int \mathrm{e}^{x} \sqrt{\mathrm{e}^{x}+2} \mathrm{~d} x, u=\mathrm{e}^{x}+2$

**e** $\int \frac{5 x}{5 x+1} \mathrm{~d} x, u=5 x+1$

**f** $\quad \int x \sqrt{3 x-1} \mathrm{~d} x, u=3 x-1$

<a id="ch08-ex8D-q3"></a>
##### Question 3
Given that $I=\int_{0}^{1} \frac{x^{2}}{\sqrt{1-x^{2}}} \mathrm{~d} x$, use the substitution $x=\sin \theta$ to show that $I=\int_{0}^{\frac{1}{2} \pi} \sin ^{2} \theta \mathrm{~d} \theta$. Hence find the exact value of $I$.

<a id="ch08-ex8D-q4"></a>
##### Question 4
Find the exact value of each of these integrals.

**a** $\int_{0}^{\frac{1}{2} \pi} \cos ^{3} x \mathrm{~d} x, u=\sin x$

**b** $\int_{0}^{4} \frac{\sqrt{x}}{3-\sqrt{x}} \mathrm{~d} x, u=3-\sqrt{x}$

**c** $\int_{1}^{2} \frac{3}{x(2-\sqrt{x})} \mathrm{d} x, u=\sqrt{x}$

**d** $\quad \int_{0}^{\sqrt{\pi}} 2 x \cos \left(\frac{x^{2}}{4}\right) \mathrm{d} x, u=\cos \left(\frac{x^{2}}{4}\right)$

**e** $\int_{\frac{1}{6} \pi}^{\frac{1}{3} \pi} \sec ^{2} x \tan ^{3} x \mathrm{~d} x, u=\tan x$

**f** $\int_{-2}^{2} \frac{5}{\left(x^{2}+4\right)^{2}} \mathrm{~d} x, x=2 \tan \theta$

**g** $\int_{0}^{1} \frac{x^{2}}{\sqrt{4-x^{2}}}, x=2 \cos \theta$

**h** $\int_{0}^{2} \sqrt{x(2-x)} \mathrm{d} x, x=2 \sin ^{2} \theta$

<a id="ch08-ex8D-q5"></a>
##### Question 5
Use the substitution $u=x-2$ to find the exact value of $\int_{1}^{2} \frac{4}{1+(x-2)^{2}} \mathrm{~d} x$.

<a id="ch08-ex8D-q6"></a>
##### Question 6
The diagram shows part of the curve $y=2 \sin ^{2} x \cos ^{3} x$. Using the substitution $u=\sin x$, find the exact area of the shaded region.

![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-194_275_512_649_1484.jpg)

<a id="ch08-ex8D-q7"></a>
##### Question 7
The diagram shows part of the curve $y=\frac{\ln x}{\sqrt{x}}$. Using the substitution $u=\ln x$, find the exact value of the volume of the solid formed when the shaded region is rotated completely about the $x$-axis.

![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-194_281_504_941_1482.jpg)

<a id="ch08-ex8D-q8"></a>
##### Question 8
The diagram shows part of the curve $y=3 \mathrm{e}^{\cos x} \sin x$. The curve has rotational symmetry of order 2 about the origin. Using the substitution $u=\cos x$, find the exact value of the total area bounded by the curve and the $x$-axis between $x=-\pi$ and $x=\pi$.

![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-194_292_616_1236_1377.jpg)

## 8.5 The use of partial fractions in integration

#### EXPLORE 8.1

Consider $\int \frac{2}{x^{2}-1} \mathrm{~d} x$.

Try using some of the integration techniques that you have learnt so far to find this integral and discuss what happens with your classmates.

In the integral $\int \frac{2}{x^{2}-1} \mathrm{~d} x$, the denominator $x^{2}-1$ can be factorised to $(x-1)(x+1)$.

Hence the fraction $\frac{2}{x^{2}-1}$ can be split into partial fractions.

$$
\begin{align}
\frac{2}{x^{2}-1} & \equiv \frac{A}{x-1}+\frac{B}{x+1} \quad \text { Multiply throughout by }(x-1)(x+1) \\
2 & \equiv A(x+1)+B(x-1) \text {...... (1) } \tag{1}
\end{align}
$$

Let $x=1$ in equation (1):

$$
\begin{align}
& 2=2 A \\
& A=1
\end{align}
$$

Let $x=-1$ in equation (1):

$$
\begin{align}
2 & =-2 B \\
B & =-1 \\
\therefore \frac{2}{x^{2}-1} & \equiv \frac{1}{x-1}-\frac{1}{x+1}
\end{align}
$$

Hence

$$
\begin{align}
\int \frac{2}{x^{2}-1} \mathrm{~d} x & =\int\left(\frac{1}{x-1}-\frac{1}{x+1}\right) \mathrm{d} x \\
& =\ln |x-1|-\ln |x+1|+c \\
& =\ln \left|\frac{x-1}{x+1}\right|+c
\end{align}
$$

<a id="ch08-we-8.13"></a>
#### WORKED EXAMPLE 8.13

Find $\int \frac{3-x}{(x+1)\left(x^{2}+3\right)} \mathrm{d} x$.

Answer

First split into partial fractions.

$$
\begin{align}
\frac{3-x}{(x+1)\left(x^{2}+3\right)} & \equiv \frac{A}{x+1}+\frac{B x+C}{x^{2}+3} \\
3-x & \equiv A\left(x^{2}+3\right)+B x(x+1)+C(x+1)
\end{align}
$$

Let $x=-1 \quad 4=4 A \quad \Rightarrow A=1$

Let $x=0 \quad 3=3 A+C \quad \Rightarrow C=0$

Let $x=1 \quad 2=4 A+2 B+2 C \quad \Rightarrow B=-1$

$$
\begin{align}
\therefore \int \frac{3-x}{(x+1)\left(x^{2}+3\right)} \mathrm{d} x & =\int\left(\frac{1}{x+1}-\frac{x}{x^{2}+3}\right) \mathrm{d} x \\
& =\int \frac{1}{x+1} \mathrm{~d} x-\frac{1}{2} \int \frac{2 x}{x^{2}+3} \mathrm{~d} x \\
& =\ln |x+1|-\frac{1}{2} \ln \left|x^{2}+3\right|+c
\end{align}
$$

<a id="ch08-we-8.14"></a>
#### WORKED EXAMPLE 8.14

Find $\int \frac{9}{(x+2)(x-1)^{2}} \mathrm{~d} x$.

Answer

First split into partial fractions.

$$
\begin{align}
\frac{9}{(x+2)(x-1)^{2}} & \equiv \frac{A}{x+2}+\frac{B}{x-1}+\frac{C}{(x-1)^{2}} \\
9 & \equiv A(x-1)^{2}+B(x+2)(x-1)+C(x+2)
\end{align}
$$

$$
\begin{align}
& \text { Let } x=1 \quad \begin{array}{ll} 9=3 C & \Rightarrow C=3 \\
\text { Let } x=-2 & 9=9 A \end{array} \quad \begin{array}{l} x=A=1 \\
9=A-2 B+2 C \quad \\
\therefore \int \frac{9}{(x+2)(x-1)^{2}} \mathrm{~d} x=\int\left(\frac{1}{x+2}-\frac{1}{x-1}+\frac{3}{(x-1)^{2}}\right) \mathrm{d} x \\
\quad=\int\left(\frac{1}{x+2}-\frac{1}{x-1}+3(x-1)^{-2}\right) \mathrm{d} x \\
\quad=\ln |x+2|-\ln |x-1|-3(x-1)^{-1}+c \\
\quad=\ln \left|\frac{x+2}{x-1}\right|-\frac{3}{x-1}+c \end{array}
\end{align}
$$

<a id="ch08-ex8E"></a>
### EXERCISE 8E

<a id="ch08-ex8E-q1"></a>
##### Question 1
Find each of these integrals.

**a** $\int \frac{1}{x(2-x)} \mathrm{d} x$

**b** $\int \frac{2 x-5}{(x+2)(x-1)} \mathrm{d} x$

**c** $\int \frac{2(4 x-9)}{(2 x+1)(x-5)} \mathrm{d} x$

**d** $\quad \int \frac{x^{2}+2 x-5}{(x-3)\left(x^{2}+1\right)} \mathrm{d} x$

**e** $\int \frac{6 x^{2}-19 x+20}{(x+1)(x-2)^{2}} \mathrm{~d} x$

**f** $\quad \int \frac{2 x^{2}+4 x-21}{(x-1)(x+4)} \mathrm{d} x$

<a id="ch08-ex8E-q2"></a>
##### Question 2
Evaluate each of these integrals.

**a** $\int_{1}^{2} \frac{5 x+13}{(x+2)(x+3)} \mathrm{d} x$

**b** $\int_{0}^{2} \frac{4 x+5}{(2 x+1)(x+2)} \mathrm{d} x$

**c** $\quad \int_{1}^{2} \frac{4-3 x}{(2 x-1)(x+2)} \mathrm{d} x$

**d** $\int_{-1}^{1} \frac{3 x^{2}+x}{(x-2)\left(x^{2}+1\right)} \mathrm{d} x$

**e** $\int_{0}^{1} \frac{x^{2}+x+2}{(x+1)\left(1+x^{2}\right)} \mathrm{d} x$

**f** $\quad \int_{-2}^{0} \frac{8}{(2-x)\left(4+x^{2}\right)} \mathrm{d} x$

**g** $\int_{2}^{3} \frac{1-x-2 x^{2}}{x^{2}(1-x)} \mathrm{d} x$

**h** $\int_{0}^{1} \frac{1-2 x}{(2 x+1)(x+1)^{2}} \mathrm{~d} x$

**i** $\int_{1}^{2} \frac{8 x^{2}-3 x-2}{4 x^{3}-3 x+1} \mathrm{~d} x$

<a id="ch08-ex8E-q3"></a>
##### Question 3
By first dividing the numerator by the denominator, evaluate each of these integrals.

**a** $\int_{2}^{3} \frac{x^{2}+2 x+3}{(x-1)(x+2)} \mathrm{d} x$

**b** $\int_{1}^{3} \frac{2 x^{2}+5 x+1}{(x+1)(x+2)} \mathrm{d} x$

**c** $\int_{1}^{2} \frac{4 x^{2}+2 x-5}{(x+1)(2 x-1)} \mathrm{d} x$

<a id="ch08-ex8E-q4"></a>
##### Question 4
Show that $\int_{2 \sqrt{2}}^{3 \sqrt{2}} \frac{x+3 \sqrt{2}}{x^{2}-2} \mathrm{~d} x=\ln 3$.

<a id="ch08-ex8E-q5"></a>
##### Question 5
Show that $\int_{0}^{\frac{1}{2} \pi} \frac{\cos x}{9-\sin ^{2} x} \mathrm{~d} x=\frac{1}{6} \ln 2$.

<a id="ch08-ex8E-q6"></a>
##### Question 6
Show that $\int_{0}^{\ln 2} \frac{\mathrm{e}^{2 x}}{\left(1+\mathrm{e}^{x}\right)\left(2 \mathrm{e}^{x}+1\right)} \mathrm{d} x=\frac{1}{2} \ln \frac{27}{20}$.

## 8.6 Integration by parts

Consider $\int x \mathrm{e}^{2 x} \mathrm{~d} x$. The function to be integrated is clearly the product of two simpler functions $x$ and $\mathrm{e}^{2 x}$. If we try using a substitution to simplify the integral we will find that it does not help. To integrate this function we require a new technique.

Integrating both sides of the equation for the product rule for differentiation with respect to $x$ and using the fact that integration is the reverse process of differentiation we can say that:

$$
u v=\int u \frac{\mathrm{~d} v}{\mathrm{~d} x} \mathrm{~d} x+\int v \frac{\mathrm{~d} u}{\mathrm{~d} x} \mathrm{~d} x
$$

Rearranging gives the formula for integration by parts:

<a id="ch08-kp-8.4"></a>
#### KEY POINT 8.4

$$
\int u \frac{\mathrm{~d} v}{\mathrm{~d} x} \mathrm{~d} x=u v-\int v \frac{\mathrm{~d} u}{\mathrm{~d} x} \mathrm{~d} x
$$

The following Worked examples show how to use this formula.

<a id="ch08-we-8.15"></a>
#### WORKED EXAMPLE 8.15

Find $\int x \mathrm{e}^{2 x} \mathrm{~d} x$.

Answer

$$
\begin{align}
& u=x \quad \Rightarrow \quad \frac{\mathrm{~d} u}{\mathrm{~d} x}=1 \\
& \frac{\mathrm{~d} v}{\mathrm{~d} x}=\mathrm{e}^{2 x} \Rightarrow \quad v=\frac{1}{2} \mathrm{e}^{2 x}
\end{align}
$$

Substitute into $\int u \frac{\mathrm{~d} v}{\mathrm{~d} x} \mathrm{~d} x=u v-\int v \frac{\mathrm{~d} u}{\mathrm{~d} x} \mathrm{~d} x$ :

$$
\begin{align}
\int x \mathrm{e}^{2 x} \mathrm{~d} x & =\frac{1}{2} x \mathrm{e}^{2 x}-\int \frac{1}{2} \mathrm{e}^{2 x} \mathrm{~d} x \\
& =\frac{1}{2} x \mathrm{e}^{2 x}-\frac{1}{4} \mathrm{e}^{2 x}+c
\end{align}
$$

It is important to choose our values for $u$ and $\frac{\mathrm{d} v}{\mathrm{~d} x}$ carefully.

Consider trying to find $\int x \ln x \mathrm{~d} x$. If we let $u=x$ and $\frac{\mathrm{d} v}{\mathrm{~d} x}=\ln x$, then finding $\frac{\mathrm{d} u}{\mathrm{~d} x}$ is easy but we do not know how to integrate $\ln x$ to find $v$. Hence we must let $u=\ln x$ and $\frac{\mathrm{d} v}{\mathrm{~d} x}=x$. This is demonstrated in Worked example 8.16.

<a id="ch08-we-8.16"></a>
#### WORKED EXAMPLE 8.16

Find $\int x \ln x \mathrm{~d} x$.

Answer

$$
\begin{array}{ll} u=\ln x \Rightarrow & \frac{\mathrm{~d} u}{\mathrm{~d} x}=\frac{1}{x} \\
\frac{\mathrm{~d} v}{\mathrm{~d} x}=x \Rightarrow & v=\frac{1}{2} x^{2} \end{array}
$$

Substitute into $\int u \frac{\mathrm{~d} v}{\mathrm{~d} x} \mathrm{~d} x=u v-\int v \frac{\mathrm{~d} u}{\mathrm{~d} x} \mathrm{~d} x$ :

$$
\begin{align}
\int x \ln x \mathrm{~d} x & =\frac{1}{2} x^{2} \ln x-\int \frac{1}{2} x^{2} \cdot \frac{1}{x} \mathrm{~d} x \\
& =\frac{1}{2} x^{2} \ln x-\int \frac{1}{2} x \mathrm{~d} x \\
& =\frac{1}{2} x^{2} \ln x-\frac{1}{4} x^{2}+c
\end{align}
$$

<a id="ch08-we-8.17"></a>
#### WORKED EXAMPLE 8.17

Find $\int \ln x \mathrm{~d} x$.

Answer

First write $\int \ln x \mathrm{~d} x$ as $\int 1 \cdot \ln x \mathrm{~d} x$.

$$
u=\ln x \Rightarrow \quad \frac{\mathrm{~d} u}{\mathrm{~d} x}=\frac{1}{x}
$$

$$
\frac{\mathrm{d} v}{\mathrm{~d} x}=1 \Rightarrow \quad v=x
$$

Substitute into $\int u \frac{\mathrm{~d} v}{\mathrm{~d} x} \mathrm{~d} x=u v-\int v \frac{\mathrm{~d} u}{\mathrm{~d} x} \mathrm{~d} x$ :

$$
\begin{align}
\int \ln x \mathrm{~d} x & =x \ln x-\int \frac{1}{x} \cdot x \mathrm{~d} x \\
& =x \ln x-\int 1 \mathrm{~d} x \\
& =x \ln x-x+c
\end{align}
$$

Sometimes we might need to use integration by parts more than once to integrate a function.

<a id="ch08-we-8.18"></a>
#### WORKED EXAMPLE 8.18

Find $\int x^{2} \sin x \mathrm{~d} x$.

Answer

$$
\begin{array}{cl} u=x^{2} & \Rightarrow \frac{\mathrm{~d} u}{\mathrm{~d} x}=2 x \\
\frac{\mathrm{~d} v}{\mathrm{~d} x}=\sin x & \Rightarrow v=-\cos x \end{array}
$$

Substitute into $\int u \frac{\mathrm{~d} v}{\mathrm{~d} x} \mathrm{~d} x=u v-\int v \frac{\mathrm{~d} u}{\mathrm{~d} x} \mathrm{~d} x$

$$
\begin{align}
\int x^{2} \sin x \mathrm{~d} x & =-x^{2} \cos x-\int-2 x \cos x \mathrm{~d} x \\
& =-x^{2} \cos x+\int 2 x \cos x \mathrm{~d} x
\end{align}
$$

Use integration by parts a second time to find $\int 2 x \cos x \mathrm{~d} x$

$$
\begin{array}{cl} u=2 x & \Rightarrow \frac{\mathrm{~d} u}{\mathrm{~d} x}=2 \\
\frac{\mathrm{~d} v}{\mathrm{~d} x}=\cos x & \Rightarrow v=\sin x \end{array}
$$

Substitute into $\int u \frac{\mathrm{~d} v}{\mathrm{~d} x} \mathrm{~d} x=u v-\int v \frac{\mathrm{~d} u}{\mathrm{~d} x} \mathrm{~d} x$

$$
\begin{align}
\int 2 x \cos x \mathrm{~d} x & =2 x \sin x-\int 2 \sin x \mathrm{~d} x \\
& =2 x \sin x+2 \cos x+c
\end{align}
$$

Substituting in (1) gives:

$$
\int x^{2} \sin x d x=-x^{2} \cos x+2 x \sin x+2 \cos x+c
$$

<a id="ch08-we-8.19"></a>
#### WORKED EXAMPLE 8.19

Given that $I=\int \frac{\ln x}{x} \mathrm{~d} x$, use integration by parts to show that $I=\frac{1}{2}(\ln x)^{2}+c$.

Answer

$$
\begin{align}
u=\ln x & \Rightarrow \frac{\mathrm{~d} u}{\mathrm{~d} x}=\frac{1}{x} \\
\frac{\mathrm{~d} v}{\mathrm{~d} x}=\frac{1}{x} & \Rightarrow v=\ln x
\end{align}
$$

Substitute into $\int u \frac{\mathrm{~d} v}{\mathrm{~d} x} \mathrm{~d} x=u v-\int v \frac{\mathrm{~d} u}{\mathrm{~d} x} \mathrm{~d} x$

$$
\begin{align}
I & =(\ln x)^{2}-\int \frac{\ln x}{x} \mathrm{~d} x \qquad \mathrm{C}^{2} \qquad \text { Rearrange. } \\
2 I & =(\ln x)^{2}+k \\
I & =\frac{1}{2}(\ln x)^{2}+\frac{k}{2} \\
\therefore I & =\frac{1}{2}(\ln x)^{2}+c
\end{align}
$$

<a id="ch08-we-8.20"></a>
#### WORKED EXAMPLE 8.20

Find the exact value of $\int_{0}^{\frac{1}{2} \pi} 4 x \sin 2 x \mathrm{~d} x$.

Answer

$$
\begin{array}{cl} u=4 x & \Rightarrow \frac{\mathrm{~d} u}{\mathrm{~d} x}=4 \\
\frac{\mathrm{~d} v}{\mathrm{~d} x}=\sin 2 x & \Rightarrow v=-\frac{1}{2} \cos 2 x \end{array}
$$

Substitute into $\int u \frac{\mathrm{~d} v}{\mathrm{~d} x} \mathrm{~d} x=u v-\int v \frac{\mathrm{~d} u}{\mathrm{~d} x} \mathrm{~d} x$

$$
\begin{align}
\int 4 x \sin 2 x \mathrm{~d} x & =-2 x \cos 2 x+\int 2 \cos 2 x \mathrm{~d} x \\
& =-2 x \cos 2 x+\sin 2 x+c
\end{align}
$$

$$
\begin{align}
\therefore \int_{0}^{\frac{1}{2} \pi} 4 x \sin 2 x \mathrm{~d} x & =[-2 x \cos 2 x+\sin 2 x]_{0}^{\frac{1}{2} \pi} \\
& =(-\pi \cos \pi+\sin \pi)-(0+\sin 0) \\
& =\pi
\end{align}
$$

<a id="ch08-ex8F"></a>
### EXERCISE 8F

<a id="ch08-ex8F-q1"></a>
##### Question 1
Find each of these integrals.

**a** $\int 3 x \mathrm{e}^{x} \mathrm{~d} x$

**b** $\int x \cos x \mathrm{~d} x$

**c** $\int x \ln 2 x \mathrm{~d} x$

**d** $\int x \sin 2 x \mathrm{~d} x$

**e** $\int x^{3} \ln x \mathrm{~d} x$

**f** $\quad \int \frac{\ln x}{\sqrt{x}} \mathrm{~d} x$

<a id="ch08-ex8F-q2"></a>
##### Question 2
Evaluate each of these integrals.

**a** $\int_{0}^{\frac{1}{6} \pi} x \cos 3 x \mathrm{~d} x$

**b** $\int_{1}^{2} x \ln 2 x \mathrm{~d} x$

**c** $\quad \int_{0}^{1} x \mathrm{e}^{2 x} \mathrm{~d} x$

**d** $\quad \int_{1}^{3} \ln x \mathrm{~d} x$

**e** $\quad \int_{0}^{1}(2-x) \mathrm{e}^{-3 x} \mathrm{~d} x$

**f** $\quad \int_{-\frac{1}{5}}^{0}\left(1-3 x \mathrm{e}^{-5 x}\right) \mathrm{d} x$

<a id="ch08-ex8F-q3"></a>
##### Question 3
Use integration by parts twice to find the exact value of each of these integrals.

**a** $\int_{1}^{2}(\ln x)^{2} \mathrm{~d} x$

**b** $\int_{0}^{\frac{1}{4} \pi} x^{2} \cos 2 x \mathrm{~d} x$

**c** $\int_{0}^{\pi} x^{2} \sin x \mathrm{~d} x$

**d** $\quad \int_{0}^{\mathrm{e}} x(\ln x)^{2} \mathrm{~d} x$

**e** $\quad \int_{-\infty}^{0} x^{2} \mathrm{e}^{x} \mathrm{~d} x$

**f** $\quad \int_{0}^{\pi} \mathrm{e}^{x} \sin x \mathrm{~d} x$

<a id="ch08-ex8F-q4"></a>
##### Question 4
Find the exact value of the area for each of these shaded regions.

**a**

![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-201_374_673_606_424.jpg)

c

![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-201_320_596_1028_423.jpg)

**b**

![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-201_333_601_605_1332.jpg)

d

![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-201_275_574_1028_1332.jpg)

<a id="ch08-ex8F-q5"></a>
##### Question 5

![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-201_263_547_1393_369.jpg)

The diagram shows the curve $y=\mathrm{e}^{-x} \sqrt{x+2}$. Find the exact value of the volume of the solid formed when the shaded region is rotated completely about the $x$-axis.

## 8.7 Further integration

Some integrals can be found using different integration techniques.

The activities in Explore 8.2 look at why our answers to an indefinite integral might 'appear' to be different when using different integration techniques when they are actually equivalent.

#### EXPLORE 8.2

**1** Nadia and Richard are asked to find $\int x(x-2)^{7} \mathrm{~d} x$.

Nadia uses the substitution $u=x-2$ and her answer is: $\frac{1}{9}(x-2)^{9}+\frac{1}{4}(x-2)^{8}+c$ Richard uses integration by parts and his answer is: $\quad \frac{1}{8} x(x-2)^{8}-\frac{1}{72}(x-2)^{9}+c$

Use each of their methods to show that they are both correct and then use algebra to explain why their answers are equivalent.

**2** **a** Find $\int \frac{4 x+1}{2 x^{2}+x-1} \mathrm{~d} x$ using:

i the substitution $u=2 x^{2}+x-1$

ii partial fractions.

**b** Suggest another method for finding $\int \frac{4 x+1}{2 x^{2}+x-1} \mathrm{~d} x$.

**c** Use algebra to show that your two answers to part a are equivalent.

Explore 8.3 is designed to make you think about the different integration techniques that might be available to you for a particular integral.

This activity expects you to be able to recognise the appropriate substitution to use when integrating by substitution.

#### EXPLORE 8.3

Discuss with your classmates which integration methods can be used to find each of these integrals.

![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-202_364_1680_1151_274.jpg)

Find each integral.

### Checklist of learning and understanding

Integrating $\frac{\boldsymbol{k} \mathbf{f}^{\prime}(\boldsymbol{x})}{\mathbf{f}(\boldsymbol{x})}$

- $\int \frac{k \mathrm{f}^{\prime}(x)}{\mathrm{f}(x)} \mathrm{d} x=k \ln |\mathrm{f}(x)|+c$

Integration by substitution

- Substitutions can sometimes be used to simplify the form of a function so that its integral can be easily recognised. When using a substitution, we must ensure that the integral is completely rewritten in terms of the new variable before integrating.

Integrating rational functions

- Some rational functions can be split into partial fractions that can then be integrated.

Integration by parts

- $\int u \frac{\mathrm{~d} v}{\mathrm{~d} x} \mathrm{~d} x=u v-\int v \frac{\mathrm{~d} u}{\mathrm{~d} x} \mathrm{~d} x$

<a id="ch08-review"></a>
### END-OF-CHAPTER REVIEW EXERCISE 8
<a id="ch08-review-q1"></a>
##### Question 1
Find the exact value of $\int_{0}^{\frac{1}{2}} x \mathrm{e}^{-2 x} \mathrm{~d} x$. `[5]`

*Cambridge International A Level Mathematics 9709 Paper 31 Q2 June 2016*

<a id="ch08-review-q2"></a>
##### Question 2
Find the exact value of $\int_{1}^{4} \frac{\ln x}{\sqrt{x}} \mathrm{~d} x$. `[5]`

*Cambridge International A Level Mathematics 9709 Paper 31 Q3 November 2013*

<a id="ch08-review-q3"></a>
##### Question 3
Use the substitution $u=1+3 \tan x$ to find the exact value of $\int_{0}^{\frac{1}{4} \pi} \frac{\sqrt{(1+3 \tan x)}}{\cos ^{2} x} \mathrm{~d} x$ `[5]`

*Cambridge International A Level Mathematics 9709 Paper 31 Q2 June 2014*

<a id="ch08-review-q4"></a>
##### Question 4
**i** Prove that $\cot \theta+\tan \theta \equiv 2 \operatorname{cosec} 2 \theta$. `[3]`

**ii** Hence show that $\int_{\frac{1}{6} \pi}^{\frac{1}{3} \pi} \operatorname{cosec} 2 \theta \mathrm{~d} \theta=\frac{1}{2} \ln 3$. `[4]`

*Cambridge International A Level Mathematics 9709 Paper 31 Q5 November 2013*

<a id="ch08-review-q5"></a>
##### Question 5
Let $I=\int_{0}^{1} \frac{x^{2}}{\sqrt{\left(4-x^{2}\right)}} \mathrm{d} x$.

**i** Using the substitution $x=2 \sin \theta$, show that $I=\int_{0}^{\frac{1}{6} \pi} 4 \sin ^{2} \theta \mathrm{~d} \theta$. `[3]`

**ii** Hence find the exact value of $I$. `[4]`

*Cambridge International A Level Mathematics 9709 Paper 31 Q5 November 2010*

<a id="ch08-review-q6"></a>
##### Question 6
The integral $I$ is defined by $I=\int_{0}^{2} 4 t^{3} \ln \left(t^{2}+1\right) \mathrm{d} t$.

**i** Use the substitution $x=t^{2}+1$ to show that $I=\int_{1}^{5}(2 x-2) \ln x \mathrm{~d} x$. `[3]`

**ii** Hence find the exact value of $I$. `[5]`

*Cambridge International A Level Mathematics 9709 Paper 31 Q7 June 2011*

<a id="ch08-review-q7"></a>
##### Question 7
**i** Express $\frac{2}{(x+1)(x+3)}$ in partial fractions. `[2]`

**ii** Using your answer to part i, show that $\left(\frac{2}{(x+1)(x+3)}\right)^{2} \equiv \frac{1}{(x+1)^{2}}-\frac{1}{x+1}+\frac{1}{x+3}+\frac{1}{(x+3)^{2}}$. `[2]`

**iii** Hence show that $\int_{0}^{1} \frac{4}{(x+1)^{2}(x+3)^{2}} \mathrm{~d} x=\frac{7}{12}-\ln \frac{3}{2}$. `[5]`

*Cambridge International A Level Mathematics 9709 Paper 31 Q8 June 2010*

<a id="ch08-review-q8"></a>
##### Question 8
**a** Find $\int\left(4+\tan ^{2} 2 x\right) \mathrm{d} x$. `[3]`

**b** Find the exact value of $\int_{\frac{1}{4} \pi}^{\frac{1}{2} \pi} \frac{\sin \left(x+\frac{1}{6} \pi\right)}{\sin x} \mathrm{~d} x$. `[5]`

*Cambridge International A Level Mathematics 9709 Paper 31 Q5 June 2015*

<a id="ch08-review-q9"></a>
##### Question 9
**i** Prove the identity $\tan 2 \theta-\tan \theta \equiv \tan \theta \sec 2 \theta$. `[4]`

**ii** Hence show that $\int_{0}^{\frac{1}{6} \pi} \tan \theta \sec 2 \theta \mathrm{~d} \theta=\frac{1}{2} \ln \frac{3}{2}$. `[4]`

*Cambridge International A Level Mathematics 9709 Paper 31 Q5 November 2016*

<a id="ch08-review-q10"></a>
##### Question 10
![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-204_298_515_600_883.jpg) The diagram shows part of the curve $y=\left(2 x-x^{2}\right) \mathrm{e}^{\frac{1}{2} x}$ and its maximum point $M$.

**i** Find the exact $x$-coordinate of $M$. `[4]`

**ii** Find the exact value of the area of the shaded region bounded by the curve and the positive $x$-axis. `[5]`

*Cambridge International A Level Mathematics 9709 Paper 31 Q7 November 2016*

<a id="ch08-review-q11"></a>
##### Question 11
By first expressing $\frac{4 x^{2}+5 x+3}{2 x^{2}+5 x+2}$ in partial fractions, show that $\int_{0}^{4} \frac{4 x^{2}+5 x+3}{2 x^{2}+5 x+2} \mathrm{~d} x=8-\ln 9$. `[10]`

*Cambridge International A Level Mathematics 9709 Paper 31 Q9 June 2012*

<a id="ch08-review-q12"></a>
##### Question 12
![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-204_358_548_1378_864.jpg) The diagram shows the curve $y=x^{3} \ln x$ and its minimum point $M$.

**i** Find the exact coordinates of $M$. `[5]`

**ii** Find the exact area of the shaded region bounded by the curve, the $x$-axis and the line $x=2$. `[5]`

*Cambridge International A Level Mathematics 9709 Paper 31 Q9 November 2010*

<a id="ch08-review-q13"></a>
##### Question 13
![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-204_277_629_2013_814.jpg) The diagram shows the curve $y=\frac{x^{2}}{1+x^{3}}$ for $x \geqslant 0$, and its maximum point $M$. The shaded region $R$ is enclosed by the curve, the $x$-axis and the lines $x=1$ and $x=p$.

**i** Find the exact value of the $x$-coordinate of $M$. `[4]`

**ii** Calculate the value of $p$ for which the area of $R$ is equal to 1 . Give your answer correct to 3 significant figures. `[6]`

<a id="ch08-cross"></a>
### CROSS-TOPIC REVIEW EXERCISE 3

This exercise is for Pure Mathematics 3 students only.

<a id="ch08-cross-q1"></a>
##### Question 1
Expand $(1-3 x)^{-5}$ in ascending powers of $x$, up to and including the term in $x^{3}$. `[3]`

<a id="ch08-cross-q2"></a>
##### Question 2
Evaluate $\int_{0}^{1} \frac{1}{3 x^{2}+1} \mathrm{~d} x$. `[3]`

<a id="ch08-cross-q3"></a>
##### Question 3
Expand $\frac{32}{(x+2)^{3}}$ in ascending powers of $x$, up to and including the term in $x^{3}$. `[4]`

<a id="ch08-cross-q4"></a>
##### Question 4
Expand $\frac{1}{\sqrt{4-2 x}}$ in ascending powers of $x$, up to and including the term in $x^{2}$. `[4]`

<a id="ch08-cross-q5"></a>
##### Question 5
Evaluate $\int_{0}^{\frac{1}{2} \pi} x^{2} \sin x \mathrm{~d} x$. `[5]`

<a id="ch08-cross-q6"></a>
##### Question 6
Expand $\sqrt{\frac{1+2 x}{1-x}}$ in ascending powers of $x$, up to and including the term in $x^{3}$. `[5]`

<a id="ch08-cross-q7"></a>
##### Question 7
Show that $\int_{0}^{1}(x+2) \mathrm{e}^{-2 x} \mathrm{~d} x=\frac{5}{4}-\frac{7}{4 \mathrm{e}^{2}}$. `[5]`

<a id="ch08-cross-q8"></a>
##### Question 8
**i** Expand $\frac{1}{\sqrt{(1-4 x)}}$ in ascending powers of $x$, up to and including the term in $x^{2}$, simplifying the coefficients. `[3]`

**ii** Hence find the coefficient of $x^{2}$ in the expansion of $\frac{1+2 x}{\sqrt{(4-16 x)}}$. `[2]`

*Cambridge International A Level Mathematics 9709 Paper 31 Q2 June 2012*

<a id="ch08-cross-q9"></a>
##### Question 9
When $(1+a x)^{-2}$, where $a$ is a positive constant, is expanded in ascending powers of $x$, the coefficients of $x$ and $x^{3}$ are equal.

**i** Find the exact value of $a$. `[4]`

**ii** When $a$ has this value, obtain the expansion up to and including the term in $x^{2}$, simplifying the coefficients. `[3]`

*Cambridge International A Level Mathematics 9709 Paper 31 Q4 November 2012*

<a id="ch08-cross-q10"></a>
##### Question 10
![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-205_286_524_1983_920.jpg) The diagram shows the curve $y=8 \sin \frac{1}{2} x-\tan \frac{1}{2} x$ for $0 \leqslant x<\pi$. The $x$-coordinate of the maximum point is $\alpha$ and the shaded region is enclosed by the curve and the lines $x=\alpha$ and $y=0$.

**i** Show that $\alpha=\frac{2}{3} \pi$. `[3]`

**ii** Find the exact value of the area of the shaded region. `[4]`

*Cambridge International A Level Mathematics 9709 Paper 31 Q5 June 2012*

<a id="ch08-cross-q11"></a>
##### Question 11
Show that $\int_{0}^{5} \frac{5-3 x}{(x+1)(3 x+1)} \mathrm{d} x=4 \ln \frac{4}{3}$. `[7]`

<a id="ch08-cross-q12"></a>
##### Question 12
Let $I=\int_{0}^{\frac{1}{2}} \frac{4 x^{2}}{\sqrt{1-x^{2}}} \mathrm{~d} x$.

**a** Using the substitution $x=\sin \theta$, show that $I=\int_{0}^{\frac{\pi}{6}} 4 \sin ^{2} \theta \mathrm{~d} \theta$. `[3]`

**b** Hence show that $I=\frac{\pi}{3}-\frac{\sqrt{3}}{2}$. `[4]`

<a id="ch08-cross-q13"></a>
##### Question 13
It is given that $\int_{1}^{a} x \ln x \mathrm{~d} x=30$, where $a>1$.

**a** Show that $a=\sqrt{\frac{119}{2 \ln a-1}}$. `[5]`

**b** Use the iterative formula $a_{n+1}=\sqrt{\frac{119}{2 \ln a_{n}-1}}$ to determine the value of $a$ correct to 2 decimal places. Give the result of each iteration correct to 4 decimal places. `[3]`

<a id="ch08-cross-q14"></a>
##### Question 14
![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-206_298_557_1151_867.jpg) The diagram shows the curve $y=x^{2} \mathrm{e}^{2-x}$ and its maximum point $M$.

**i** Show that the $x$-coordinate of $M$ is 2. `[3]`

**ii** Find the exact value of $\int_{0}^{2} x^{2} \mathrm{e}^{2-x} \mathrm{~d} x$. `[6]`

*Cambridge International A Level Mathematics 9709 Paper 31 Q9 June 2015*

<a id="ch08-cross-q15"></a>
##### Question 15
Let $\mathrm{f}(x)=\frac{12+8 x-x^{2}}{(2-x)\left(4+x^{2}\right)}$.

**i** Express f(x) in the form $\frac{A}{2-x}+\frac{B x+C}{4+x^{2}}$. `[4]`

**ii** Show that $\int_{0}^{1} \mathrm{f}(x) \mathrm{d} x=\ln \left(\frac{25}{2}\right)$. `[5]`

*Cambridge International A Level Mathematics 9709 Paper 31 Q8 November 2011*

<a id="ch08-cross-q16"></a>
##### Question 16
It is given that $\int_{1}^{a} \ln (2 x) \mathrm{d} x=1$, where $a>1$.

**i** Show that $a=\frac{1}{2} \exp \left(1+\frac{\ln 2}{a}\right)$, where $\exp (x)$ denotes $\mathrm{e}^{x}$. `[6]`

**ii** Use the iterative formula $a_{n+1}=\frac{1}{2} \exp \left(1+\frac{\ln 2}{a_{n}}\right)$ to determine the value of $a$ correct to 2 decimal places. Give the result of each iteration to 4 decimal places. `[3]`

*Cambridge International A Level Mathematics 9709 Paper 31 Q6 November 2014*

<a id="ch08-cross-q17"></a>
##### Question 17
**i** Express $\frac{4+12 x+x^{2}}{(3-x)(1+2 x)^{2}}$ in partial fractions. `[5]`

**ii** Hence obtain the expansion of $\frac{4+12 x+x^{2}}{(3-x)(1+2 x)^{2}}$ in ascending powers of $x$, up to and including the term in $x^{2}$. `[5]`

*Cambridge International A Level Mathematics 9709 Paper 31 Q9 June 2014*

<a id="ch08-cross-q18"></a>
##### Question 18
Let $\mathrm{f}(x)=\frac{x^{2}-8 x+9}{(1-x)(2-x)^{2}}$.

**i** Express $\mathrm{f}(x)$ in partial fractions. `[5]`

**ii** Hence obtain the expansion of $\mathrm{f}(x)$ in ascending powers of $x$, up to and including the term in $x^{2}$. `[5]`

*Cambridge International A Level Mathematics 9709 Paper 31 Q9 November 2014*

<a id="ch08-cross-q19"></a>
##### Question 19
Let $\mathrm{f}(x)=\frac{5 x-2}{(x-1)\left(2 x^{2}-1\right)}$.

**a** Express f( $x$ ) in partial fractions. `[5]`

**b** Hence obtain the expansion of $\mathrm{f}(x)$ in ascending powers of $x$, up to and including the term in $x^{3}$. `[5]`

<a id="ch08-cross-q20"></a>
##### Question 20
**a** Given that $\frac{x^{3}-2}{x^{2}(2 x-1)} \equiv A+\frac{B}{x}+\frac{C}{x^{2}}+\frac{D}{2 x-1}$, find the values of the constants $A, B, C$ and $D$.

**b** Hence show that $\int_{1}^{2} \frac{x^{3}-2}{x^{2}(2 x-1)} \mathrm{d} x=\frac{3}{2}-2 \ln \frac{9}{4}+\frac{1}{4} \ln 3$.

<a id="ch08-cross-q21"></a>
##### Question 21

![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-207_393_575_1578_904.jpg)

The diagram shows the curve $y=x^{2} \ln x$ and its minimum point $M$.

**i** Find the exact values of the coordinates of $M$. `[5]`

**ii** Find the exact value of the area of the shaded region bounded by the curve, the $x$-axis and the line $x=\mathrm{e}$. `[5]`

*Cambridge International A Level Mathematics 9709 Paper 31 Q9 November 2011*

<a id="ch08-cross-q22"></a>
##### Question 22
**i** Show that $\int_{2}^{4} 4 x \ln x \mathrm{~d} x=56 \ln 2-12$. `[5]`

**ii** Use the substitution $u=\sin 4 x$ to find the exact value of $\int_{0}^{\frac{1}{24} \pi} \cos ^{3} 4 x \mathrm{~d} x$. `[5]`

<a id="ch08-cross-q23"></a>
##### Question 23
**i** Express $4 \cos \theta+3 \sin \theta$ in the form $R \cos (\theta-\alpha)$, where $R>0$ and $0<\alpha<\frac{1}{2} \pi$. Give the value of $\alpha$ correct to 4 decimal places. `[3]`

**ii** Hence

a solve the equation $4 \cos \theta+3 \sin \theta=2$ for $0<\theta<2 \pi$, `[4]`

b find $\int \frac{50}{(4 \cos \theta+3 \sin \theta)^{2}} \mathrm{~d} \theta$. `[3]`

![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-209_437_529_850_931.jpg)
