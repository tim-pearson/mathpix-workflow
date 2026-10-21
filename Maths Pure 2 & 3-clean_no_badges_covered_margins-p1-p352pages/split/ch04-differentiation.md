# Chapter 4: Differentiation

In this chapter you will learn how to:

- differentiate products and quotients

- use the derivatives of $\mathrm{e}^{x}, \ln x, \sin x, \cos x, \tan x$, together with constant multiples, sums, differences and composites

- find and use the first derivative of a function, which is defined parametrically or implicitly.

<a id="ch04-prerequisite"></a>
### PREREQUISITE KNOWLEDGE

| Where it comes from | What you should be able to do | Check your skills |
| :--- | :--- | :--- |
| Pure Mathematics 1 Coursebook, Chapter 7 | Differentiate $x^{n}$ together with constant multiples, sums and differences. | 1 Differentiate with respect to $x$.<br>&#160;&#160;a $y=5 x^{3}-\frac{3}{x^{2}}+2 \sqrt{x}$<br>&#160;&#160;b $y=\frac{x^{8}-4 x^{5}+x^{2}}{2 x^{3}}$<br> |
| Pure Mathematics 1 Coursebook, Chapter 7 | Differentiate composite functions using the chain rule. | 2 Differentiate with respect to $x$.<br>&#160;&#160;a $(3 x-5)^{4}$<br>&#160;&#160;b $\frac{4}{\sqrt{1-2 x}}$<br> |
| Pure Mathematics 1 Coursebook, Chapter 7 | Find tangents and normals to curves. | 3 Find the equation of the normal to the curve $y=x^{3}-5 x^{2}+2 x-1$ at the point (1, -3). |
| Pure Mathematics 1 Coursebook, Chapter 8 | Find stationary points on curves and determine their nature. | 4 Find the stationary points on the curve $y=x^{3}-3 x^{2}+2$ and determine their nature. |

### Why do we study differentiation?

In this chapter we will learn how to differentiate the product and the quotient of two simple functions. We will also learn how to find and use the derivatives of exponential, logarithmic and trigonometric functions.

All of the functions that we have differentiated so far have been of the form $y=\mathrm{f}(x)$. In this chapter we will also learn how to differentiate functions that cannot be written in the form $y=\mathrm{f}(x)$. For example, the function $y^{2}+2 x y=4$.

Lastly, we will learn how to find and use the derivative of a function where the variables $x$ and $y$ are given as a function of a third variable.

Although these topics might seem like they are just for Pure Mathematics problems, differentiation is used for calculations to do with quantum mechanics and field theories in Physics.

## 4.1 The product rule

The function $y=(x+1)^{4}(3 x-2)^{3}$ can be considered as the product of two separate functions:

$$
y=u v \text { where } u=(x+1)^{4} \text { and } v=(3 x-2)^{3}
$$

To differentiate the product of two functions we can use the product rule.

<a id="ch04-kp-4.1"></a>
#### KEY POINT 4.1

The product rule is:

$$
\frac{\mathrm{d}}{\mathrm{~d} x}(u v)=u \frac{\mathrm{~d} v}{\mathrm{~d} x}+v \frac{\mathrm{~d} u}{\mathrm{~d} x}
$$

Some people find it easier to remember this rule as:

'(first function × derivative of second function) + (second function × derivative of first function)' So for $y=(x+1)^{4}(3 x-2)^{3}$,

$$
\begin{align}
\frac{\mathrm{d} y}{\mathrm{~d} x} & =\underbrace{(x+1)^{4}}_{\text {first }} \underbrace{\frac{\mathrm{d}}{\mathrm{~d} x}(3 x-2)^{3}}_{\text {differentiate second }}+\underbrace{(3 x-2)^{3}}_{\text {second }} \underbrace{\frac{\mathrm{d}}{\mathrm{~d} x}(x+1)^{4}}_{\text {differentiate first }} \\
& =(x+1)^{4} \times 9(3 x-2)^{2}+(3 x-2)^{3} \times 4(x+1)^{3} \\
& =(x+1)^{3}(3 x-2)^{2}[9(x+1)+4(3 x-2)] \\
& =(x+1)^{3}(3 x-2)^{2}(21 x+1)
\end{align}
$$

### The product rule from first principles

Consider the function $y=u v$ where $u$ and $v$ are functions of $x$.

A small increase $\delta x$ in $x$ leads to corresponding small increases $\delta y, \delta u$ and $\delta v$ in $y, u$ and $v$.

$$
\begin{array}{rlrl} y+\delta y & =(u+\delta u)(v+\delta v) & & \text { Expand brackets and replace } y \text { with } u v . \\
u v+\delta y & =u v+u \delta v+v \delta u+\delta u \delta v & & \text { Subtract } u v \text { from both sides. } \\
\delta y & =u \delta v+v \delta u+\delta u \delta v & & \text { Divide both sides by } \delta x . \\
\frac{\delta y}{\delta x} & =u \frac{\delta v}{\delta x}+v \frac{\delta u}{\delta x}+\delta u \frac{\delta v}{\delta x}----------(1) \tag{1} \end{array}
$$

As $\delta x \rightarrow 0$, then so do $\delta y, \delta u$ and $\delta v$ and

$$
\frac{\delta y}{\delta x} \rightarrow \frac{\mathrm{~d} y}{\mathrm{~d} x}, \frac{\delta u}{\delta x} \rightarrow \frac{\mathrm{~d} u}{\mathrm{~d} x} \text { and } \frac{\delta v}{\delta x} \rightarrow \frac{\mathrm{~d} v}{\mathrm{~d} x} .
$$

Equation (1) becomes:

$$
\begin{align}
\frac{\mathrm{d} y}{\mathrm{~d} x} & =u \frac{\mathrm{~d} v}{\mathrm{~d} x}+v \frac{\mathrm{~d} u}{\mathrm{~d} x}+0 \frac{\mathrm{~d} v}{\mathrm{~d} x} \\
\therefore \frac{\mathrm{~d} y}{\mathrm{~d} x} & =u \frac{\mathrm{~d} v}{\mathrm{~d} x}+v \frac{\mathrm{~d} u}{\mathrm{~d} x}
\end{align}
$$

<a id="ch04-we-4.1"></a>
#### WORKED EXAMPLE 4.1

Find $\frac{\mathrm{d} y}{\mathrm{~d} x}$ when $y=(2 x-1) \sqrt{4 x+5}$.

Answer

$$
\begin{align}
y & =(2 x-1)(4 x+5)^{\frac{1}{2}} \\
\frac{\mathrm{~d} y}{\mathrm{~d} x} & =\underbrace{(2 x-1)}_{\text {first }} \underbrace{\frac{\mathrm{d}}{\mathrm{~d} x}\left[(4 x+5)^{\frac{1}{2}}\right]}_{\text {differentiate second }}+\underbrace{(4 x+5)^{\frac{1}{2}}}_{\text {second }} \underbrace{\frac{\mathrm{d}}{\mathrm{~d} x}(2 x-1)}_{\text {differentiate first }}
\end{align}
$$

$$
\begin{align}
& =(2 x-1) \underbrace{\left[\frac{1}{2}(4 x+5)^{-\frac{1}{2}}(4)\right]}_{\text {Chain rule. }}+(\sqrt{4 x+5})(2) \\
& =\frac{2(2 x-1)}{\sqrt{4 x+5}}+2 \sqrt{4 x+5} \\
& =\frac{2(2 x-1)+2(4 x+5)}{\sqrt{4 x+5}} \\
& =\frac{12 x+8}{\sqrt{4 x+5}}
\end{align}
$$

<a id="ch04-we-4.2"></a>
#### WORKED EXAMPLE 4.2

Find the $x$-coordinate of the points on the curve $y=(2 x-3)^{2}(x+5)^{3}$ where the gradient is 0.

Answer

$$
\begin{align}
y & =(2 x-3)^{2}(x+5)^{3} \\
\frac{\mathrm{~d} y}{\mathrm{~d} x} & =\underbrace{(2 x-3)^{2}}_{\text {first }} \underbrace{\frac{\mathrm{d}}{\mathrm{~d} x}\left[(x+5)^{3}\right]}_{\text {differentiate second }}+\underbrace{(x+5)^{3}}_{\text {second }} \underbrace{\frac{\mathrm{d}}{\mathrm{~d} x}\left[(2 x-3)^{2}\right]}_{\text {differentiate first }} \\
& =(2 x-3)^{2} \underbrace{\left[3(x+5)^{2}(1)\right]}_{\text {Chain rule }}+(x+5)^{3} \underbrace{\left[2(2 x-3)^{1}(2)\right]}_{\text {Chain rule }} \\
& =3(2 x-3)^{2}(x+5)^{2}+4(2 x-3)(x+5)^{3} \qquad \text {. Factorise. } \\
& =(2 x-3)(x+5)^{2}[3(2 x-3)+4(x+5)] \qquad \text { Simplify. } \\
& =(2 x-3)(x+5)^{2}(10 x+11)
\end{align}
$$

$$
\frac{\mathrm{d} y}{\mathrm{~d} x}=0 \text { when }(2 x-3)(x+5)^{2}(10 x+11)=0
$$

$$
\begin{array}{rlrlrl} 2 x-3 & =0 & x+5 & =0 & 10 x+11 & =0 \\
x & =\frac{3}{2} & x & =-5 & x & =-1.1 \end{array}
$$

<a id="ch04-ex4A"></a>
### EXERCISE 4A

<a id="ch04-ex4A-q1"></a>
##### Question 1
Use the product rule to differentiate each of the following with respect to $x$ :

**a** $x(x-2)^{5}$

**b** $5 x(2 x+1)^{3}$

**c** $x \sqrt{x+2}$

**d** $(x-1) \sqrt{x+5}$

**e** $x^{3} \sqrt{2 x-1}$

**f** $\sqrt{x}\left(x^{2}+2\right)^{3}$

**g** $(x-3)^{2}(x+2)^{5}$

**h** $(2 x-1)^{5}(3 x+4)^{4}$

**i** $(2 x-5)\left(3 x^{2}+1\right)^{2}$

<a id="ch04-ex4A-q2"></a>
##### Question 2
Find the gradient of the curve $y=x^{2} \sqrt{x+4}$ at the point (-3, 9).

<a id="ch04-ex4A-q3"></a>
##### Question 3
Find the equation of the tangent to the curve $y=(2-x)^{3}(x+1)^{4}$ at the point where $x=1$.

<a id="ch04-ex4A-q4"></a>
##### Question 4
Find the gradient of the tangent to the curve $y=(x+2)(x-1)^{3}$ at the point where the curve meets the $y$-axis.

<a id="ch04-ex4A-q5"></a>
##### Question 5
Find the $x$-coordinate of the points on the curve $y=(3-x)^{3}(x+1)^{2}$ where the gradient is zero.

<a id="ch04-ex4A-q6"></a>
##### Question 6
Find the $x$-coordinate of the point on the curve $y=(x+2) \sqrt{1-2 x}$ where the gradient is zero.

<a id="ch04-ex4A-q7"></a>
##### Question 7
**a** Sketch the curve $y=(x-1)^{2}(5-2 x)+3$.

**b** The curve $y=(x-1)^{2}(5-2 x)+3$ has stationary points at $A$ and $B$. The straight line through $A$ and $B$ cuts the axes at $P$ and $Q$. Find the area of the triangle $P O Q$.

## 4.2 The quotient rule

We can differentiate the function $y=\frac{x^{2}-5}{2 x+1}$ by writing the function in the form $y=\left(x^{2}-5\right)(2 x+1)^{-1}$ and then by applying the product rule.

Alternatively, we can consider $y=\frac{x^{2}-5}{2 x+1}$ as the division (quotient) of two separate functions:

$$
y=\frac{u}{v} \text { where } u=x^{2}-5 \text { and } v=2 x+1 .
$$

To differentiate the quotient of two functions we can use the quotient rule.

<a id="ch04-kp-4.2"></a>
#### KEY POINT 4.2

The quotient rule is:

$$
\frac{\mathrm{d}}{\mathrm{~d} x}\left(\frac{u}{v}\right)=\frac{v \frac{\mathrm{~d} u}{\mathrm{~d} x}-u \frac{\mathrm{~d} v}{\mathrm{~d} x}}{v^{2}}
$$

Some people find it easier to remember this rule as

$$
\frac{(\text { denominator } \times \text { derivative of numerator })-(\text { numerator } \times \text { derivative of denominator })}{(\text { denominator })^{2}}
$$

### The quotient rule from first principles

Consider the function $y=\frac{u}{v}$ where $u$ and $v$ are functions of $x$.

A small increase $\delta x$ in $x$ leads to corresponding small increases $\delta y, \delta u$ and $\delta v$ in $y, u$ and $v$.

$$
\begin{align}
y+\delta y & =\frac{u+\delta u}{v+\delta v} & & \text { Subtract } y \text { from both sides. } \\
\delta y & =\frac{u+\delta u}{v+\delta v}-y & & \text { Replace } y \text { with } \frac{u}{v} . \\
\delta y & =\frac{u+\delta u}{v+\delta v}-\frac{u}{v} & & \text { Combine fractions. } \\
\delta y & =\frac{v(u+\delta u)-u(v+\delta v)}{v(v+\delta v)} & & \text { Expand brackets and simplify. } \\
\delta y & =\frac{v \delta u-u \delta v}{v^{2}+v \delta v} & & \text { Divide both sides by } \delta x . \\
\frac{\delta y}{\delta x} & =\frac{v \frac{\delta u}{\delta x}-u \frac{\delta v}{v^{2}+v \delta v}}{} & & \tag{1}
\end{align}
$$

As $\delta x \rightarrow 0$, then so do $\delta y, \delta u$ and $\delta v$ and $\frac{\delta y}{\delta x} \rightarrow \frac{\mathrm{~d} y}{\mathrm{~d} x}, \frac{\delta u}{\delta x} \rightarrow \frac{\mathrm{~d} u}{\mathrm{~d} x}$ and $\frac{\delta v}{\delta x} \rightarrow \frac{\mathrm{~d} v}{\mathrm{~d} x}$.

Equation (1) becomes

$$
\frac{\mathrm{d}}{\mathrm{~d} x}\left(\frac{u}{v}\right)=\frac{v \frac{\mathrm{~d} u}{\mathrm{~d} x}-u \frac{\mathrm{~d} v}{\mathrm{~d} x}}{v^{2}}
$$

<a id="ch04-we-4.3"></a>
#### WORKED EXAMPLE 4.3

Find the derivative of $y=\frac{x^{2}-5}{2 x+1}$.

Answer

$$
y=\frac{x^{2}-5}{2 x+1}
$$

$$
\begin{align}
\frac{\mathrm{d} y}{\mathrm{~d} x} & =\frac{\overbrace{(2 x+1)}^{\text {denominator }} \times \overbrace{\frac{\mathrm{d}}{\mathrm{~d} x}\left(x^{2}-5\right)}^{\text {differentiate numerator }}-\left(x^{2}-5\right) \times \overbrace{\frac{\mathrm{d}}{\mathrm{~d} x}(2 x+1)}^{\text {numerator }}}{\underbrace{(2 x+1)^{2}}_{\text {denominator squared }}} \\
& =\frac{(2 x+1)(2 x)-\left(x^{2}-5\right)(2)}{(2 x+1)^{2}} \\
& =\frac{4 x^{2}+2 x-2 x^{2}+10}{(2 x+1)^{2}} \\
& =\frac{2\left(x^{2}+x+5\right)}{(2 x+1)^{2}}
\end{align}
$$

<a id="ch04-we-4.4"></a>
#### WORKED EXAMPLE 4.4

Find the derivative of $y=\frac{(x+2)^{3}}{\sqrt{x-1}}$.

Answer

$$
y=\frac{(x+2)^{3}}{\sqrt{x-1}}
$$

$$
\begin{align}
\frac{\mathrm{d} y}{\mathrm{~d} x} & =\frac{\overbrace{\sqrt{x-1}}^{\text {denominator }} \times \overbrace{\frac{\mathrm{d}}{\mathrm{~d} x}\left[(x+2)^{3}\right]}^{\text {differentiate numerator }}-(x+2)^{3}}{\underbrace{(\sqrt{x-1})^{2}}_{\text {denominator squared }} \times \overbrace{\frac{\mathrm{d}}{\mathrm{~d} x}[\sqrt{x-1}]}^{\text {numerator }}} \\
& =\frac{(\sqrt{x-1})\left[3(x+2)^{2}(1)\right]-(x+2)^{3}\left[\frac{1}{2}(x-1)^{-\frac{1}{2}}(1)\right]}{x-1} \\
& =\frac{3(x+2)^{2} \sqrt{x-1}-\frac{(x+2)^{3}}{2 \sqrt{x-1}}}{x-1} \\
& =\frac{6(x+2)^{2}(x-1)-(x+2)^{3}}{2(x-1) \sqrt{x-1}} \\
& =\frac{(x+2)^{2}[6(x-1)-(x+2)]}{2(x-1)^{\frac{3}{2}}} \\
& =\frac{(x+2)^{2}(5 x-8)}{2(x-1)^{\frac{3}{2}}}
\end{align}
$$

#### EXPLORE 4.1

In Worked examples 4.3 and 4.4 we differentiated the functions $y=\frac{x^{2}-5}{2 x+1}$ and $y=\frac{(x+2)^{3}}{\sqrt{x-1}}$ using the quotient rule. Now write each of these functions as a product, such as $y=\left(x^{2}-5\right)(2 x+1)^{-1}$, and then use the product rule to differentiate them.

Do you obtain the same answers?

Discuss with your classmates which method you prefer for functions such as these: the quotient rule or the product rule.

<a id="ch04-ex4B"></a>
### EXERCISE 4B

<a id="ch04-ex4B-q1"></a>
##### Question 1
Use the quotient rule to differentiate each of the following with respect to $x$ :

**a** $\frac{2 x+3}{x-4}$

**b** $\frac{3 x-5}{2-x}$

**c** $\frac{x^{2}-3}{2 x-1}$

**d** $\frac{3 x+1}{2-5 x}$

**e** $\frac{1-2 x^{2}}{(x+4)^{2}}$

**f** $\frac{5 x^{4}}{\left(x^{2}-1\right)^{2}}$

**g** $\frac{3 x^{2}-7 x}{x^{2}+2 x+5}$

**h** $\frac{(x+4)^{2}}{\left(x^{2}+1\right)^{3}}$

<a id="ch04-ex4B-q2"></a>
##### Question 2
Find the gradient of the curve $y=\frac{x-5}{x+4}$ at the point $\left(2,-\frac{1}{2}\right)$.

<a id="ch04-ex4B-q3"></a>
##### Question 3
Find the coordinates of the points on the curve $y=\frac{(x-1)^{2}}{2 x+5}$ where the tangent is parallel to the $x$-axis.

<a id="ch04-ex4B-q4"></a>
##### Question 4
Find the coordinates of the points on the curve $y=\frac{1-2 x}{x-5}$ at which the gradient is 1.

<a id="ch04-ex4B-q5"></a>
##### Question 5
Find the equation of the tangent of the curve $y=\frac{x-4}{2 x+1}$ at the point where the curve crosses the $y$-axis.

<a id="ch04-ex4B-q6"></a>
##### Question 6
Differentiate with respect to $x$ :

**a** $\frac{\sqrt{x}}{5 x-1}$

**b** $\frac{x-1}{\sqrt{2 x+3}}$

**c** $\frac{3-x^{2}}{\sqrt{x^{2}-1}}$

**d** $\frac{5(x-1)^{3}}{\sqrt{x+2}}$

<a id="ch04-ex4B-q7"></a>
##### Question 7
Find the $x$-coordinate of the point on the curve $y=\frac{x+1}{\sqrt{x-1}}$ where the gradient is 0 .

<a id="ch04-ex4B-q8"></a>
##### Question 8
Find the equation of the normal to the curve $y=\frac{x^{2}+1}{\sqrt{x+2}}$ at the point (-1, 2).

<a id="ch04-ex4B-q9"></a>
##### Question 9
The line $2 x-2 y=5$ intersects the curve $2 x^{2} y-x^{2}-26 y-35=0$ at three points.

**a** Find the $x$-coordinates of the points of intersection.

**b** Find the gradient of the curve at each of the points of intersection.

## 4.3 Derivatives of exponential functions

### The derivative of $\mathbf{e}^{\boldsymbol{x}}$

In Chapter 2, we learnt about the natural exponential function $\mathrm{f}(x)=\mathrm{e}^{x}$. This function has a very special property. If we use graphing software to draw the graph of $\mathrm{f}(x)=\mathrm{e}^{x}$ together with the graph of its gradient function we find that the two curves are identical.

<a id="ch04-kp-4.3"></a>
#### KEY POINT 4.3

Hence, we have the rule:

$$
\frac{\mathrm{d}}{\mathrm{~d} x}\left(\mathrm{e}^{x}\right)=\mathrm{e}^{x}
$$

An explanation of how this rule can be obtained is as follows.

Consider the function $\mathrm{f}(x)=\mathrm{e}^{x}$ and two points whose $x$-coordinates are $x$ and $x+\delta x$ where $\delta x$ is a small increase in $x$.

![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-088_246_466_464_637.jpg)

$$
\frac{\mathrm{d} y}{\mathrm{~d} x}=\lim _{\delta x \rightarrow 0} \frac{\mathrm{f}(x+\delta x)-\mathrm{f}(x)}{(x+\delta x)-x}=\lim _{\delta x \rightarrow 0} \frac{\mathrm{e}^{x+\delta x}-\mathrm{e}^{x}}{\delta x}=\lim _{\delta x \rightarrow 0} \frac{\mathrm{e}^{x}\left(\mathrm{e}^{\delta x}-1\right)}{\delta x}
$$

Now consider $\frac{\mathrm{e}^{\delta x}-1}{\delta x}$ for small values of $\delta x$.

| $\delta x$ | 0.1 | 0.01 | 0.001 | 0.0001 |
| :--- | :--- | :--- | :--- | :--- |
| $\frac{\mathrm{e}^{\delta x}-1}{\delta x}$ | 1.051709 | 1.005017 | 1.000500 | 1.000050 |

From the table, we can see that as $\delta x \rightarrow 0, \frac{\mathrm{e}^{\delta x}-1}{\delta x} \rightarrow 1$.

$$
\therefore \frac{\mathrm{d} y}{\mathrm{~d} x}=\mathrm{e}^{x}
$$

The derivative of $\mathbf{e}^{\mathbf{f}(x)}$

Consider the function $y=\mathrm{e}^{\mathrm{f}(x)}$.

Let $y=\mathrm{e}^{u} \quad$ where $\quad u=\mathrm{f}(x)$

$$
\frac{\mathrm{d} y}{\mathrm{~d} u}=\mathrm{e}^{u} \quad \frac{\mathrm{~d} u}{\mathrm{~d} x}=\mathrm{f}^{\prime}(x)
$$

Using the chain rule:

$$
\begin{align}
\frac{\mathrm{d} y}{\mathrm{~d} x} & =\frac{\mathrm{d} y}{\mathrm{~d} u} \times \frac{\mathrm{d} u}{\mathrm{~d} x} \\
& =\mathrm{e}^{u} \times \mathrm{f}^{\prime}(x) \\
& =\mathrm{f}^{\prime}(x) \times \mathrm{e}^{\mathrm{f}(x)} \\
\frac{\mathrm{d}}{\mathrm{~d} x}\left[\mathrm{e}^{\mathrm{f}(x)}\right] & =\mathrm{f}^{\prime}(x) \times \mathrm{e}^{\mathrm{f}(x)}
\end{align}
$$

<a id="ch04-kp-4.4"></a>
#### KEY POINT 4.4

In particular,

$$
\frac{\mathrm{d}}{\mathrm{~d} x}\left[\mathrm{e}^{a x+b}\right]=a \mathrm{e}^{a x+b}
$$

<a id="ch04-we-4.5"></a>
#### WORKED EXAMPLE 4.5

Differentiate with respect to $x$.

**a** $\mathrm{e}^{2 x}$

**b** $x \mathrm{e}^{-5 x}$

**c** $\frac{\mathrm{e}^{3 x}}{x^{2}}$

Answer

**a** $\frac{\mathrm{d}}{\mathrm{d} x}\left(\mathrm{e}^{2 x}\right)=\underbrace{2}_{\text {differentiate index }} \times \underbrace{\mathrm{e}^{2 x}}_{\text {original function }}=2 \mathrm{e}^{2 x}$

**b**

$$
\begin{align}
\frac{\mathrm{d}}{\mathrm{~d} x}\left(x \mathrm{e}^{-5 x}\right) & =x \times \frac{\mathrm{d}}{\mathrm{~d} x}\left(\mathrm{e}^{-5 x}\right)+\mathrm{e}^{-5 x} \times \frac{\mathrm{d}}{\mathrm{~d} x}(x) \qquad \text { Product rule. } \\
& =x \times\left(-5 \mathrm{e}^{-5 x}\right)+\mathrm{e}^{-5 x} \times(1) \\
& =-5 x \mathrm{e}^{-5 x}+\mathrm{e}^{-5 x} \\
& =\mathrm{e}^{-5 x}(1-5 x)
\end{align}
$$

**c**

$$
\begin{align}
\frac{\mathrm{d}}{\mathrm{~d} x}\left(\frac{\mathrm{e}^{3 x}}{x^{2}}\right) & =\frac{x^{2} \times \frac{\mathrm{d}}{\mathrm{~d} x}\left(\mathrm{e}^{3 x}\right)-\mathrm{e}^{3 x} \times \frac{\mathrm{d}}{\mathrm{~d} x}\left(x^{2}\right)}{x^{4}} \\
& =\frac{x^{2} \times 3 \mathrm{e}^{3 x}-\mathrm{e}^{3 x} \times 2 x}{x^{4}} \\
& =\frac{\mathrm{e}^{3 x}(3 x-2)}{x^{3}}
\end{align}
$$

<a id="ch04-we-4.6"></a>
#### WORKED EXAMPLE 4.6

The equation of a curve is $y=\mathrm{e}^{2 x}-9 \mathrm{e}^{x}+7 x$. Find the exact value of the $x$-coordinate at each of the stationary points and determine the nature of each stationary point.

Answer

$$
\begin{align}
y & =\mathrm{e}^{2 x}-9 \mathrm{e}^{x}+7 x \\
\frac{\mathrm{~d} y}{\mathrm{~d} x} & =2 \mathrm{e}^{2 x}-9 \mathrm{e}^{x}+7 \\
\frac{\mathrm{~d}^{2} y}{\mathrm{~d} x^{2}} & =4 \mathrm{e}^{2 x}-9 \mathrm{e}^{x}
\end{align}
$$

Stationary points occur when $\frac{\mathrm{d} y}{\mathrm{~d} x}=0$.

$$
\begin{align}
2 \mathrm{e}^{2 x}-9 \mathrm{e}^{x}+7 & =0 \\
\left(2 \mathrm{e}^{x}-7\right)\left(\mathrm{e}^{x}-1\right) & =0 \\
\left(2 \mathrm{e}^{x}-7\right)=0 \text { or }\left(\mathrm{e}^{x}-1\right) & =0 \\
\mathrm{e}^{x}=\frac{7}{2} \text { or } \mathrm{e}^{x} & =1 \\
x=\ln \left(\frac{7}{2}\right) \text { or } x & =0
\end{align}
$$

Factorise.

When $x=0, \frac{\mathrm{~d}^{2} y}{\mathrm{~d} x^{2}}$ is negative ⇒ maximum point.

When $x=\ln \left(\frac{7}{2}\right), \frac{\mathrm{d}^{2} y}{\mathrm{~d} x^{2}}$ is positive ⇒ minimum point.

<a id="ch04-ex4C"></a>
### EXERCISE 4C

<a id="ch04-ex4C-q1"></a>
##### Question 1
Differentiate with respect to $x$.

**a** $\mathrm{e}^{5 x}$

**b** $\mathrm{e}^{-4 x}$

**c** $2 \mathrm{e}^{6 x}$

**d** $3 \mathrm{e}^{-5 x}$

**e** $4 \mathrm{e}^{\frac{x}{2}}$

**f** $\mathrm{e}^{2 x-7}$

**g** $\mathrm{e}^{x^{2}-3}$

**h** $2 x+3 \mathrm{e}^{\sqrt{x}}$

**i** $5 \sqrt{\mathrm{e}^{x}}-\frac{1}{\mathrm{e}^{2 x}}$

**j** $2\left(\mathrm{e}^{3 x}-1\right)$

**k** $\frac{3 \mathrm{e}^{2 x}+\mathrm{e}^{-2 x}}{2}$

**l** $5\left(\mathrm{e}^{x^{2}}-2 x\right)$

<a id="ch04-ex4C-q2"></a>
##### Question 2
**a** Sketch the graph of the function $y=1-\mathrm{e}^{2-x}$.

**b** Find the equation of the normal to the curve $y=1-\mathrm{e}^{2-x}$ at the point where $y=0$.

<a id="ch04-ex4C-q3"></a>
##### Question 3
The mass, $m$ grams, of a radioactive substance remaining $t$ years after a given time, is given by the formula $m=300 \mathrm{e}^{-0.00012 t}$. Find the rate at which the mass is decreasing when $t=2000$.

<a id="ch04-ex4C-q4"></a>
##### Question 4
Differentiate with respect to $x$.

**a** $x \mathrm{e}^{x}$

**b** $x^{2} \mathrm{e}^{3 x}$

**c** $5 x \mathrm{e}^{-2 x}$

**d** $2 \sqrt{x} \mathrm{e}^{x}$

**e** $\frac{\mathrm{e}^{6 x}}{x}$

**f** $\frac{\mathrm{e}^{-2 x}}{\sqrt{x}}$

**g** $\frac{\mathrm{e}^{x}-1}{\mathrm{e}^{x}+2}$

**h** $x \mathrm{e}^{3 x}+\frac{\mathrm{e}^{6 x}}{2}$

**i** $\frac{x^{2} \mathrm{e}^{x}-x}{\mathrm{e}^{x}+2}$

<a id="ch04-ex4C-q5"></a>
##### Question 5
Find the gradient of the curve $y=\frac{8}{5+\mathrm{e}^{2 x}}$ at the point where $x=0$.

<a id="ch04-ex4C-q6"></a>
##### Question 6
Find the exact coordinates of the stationary point on the curve $y=x \mathrm{e}^{x}$.

<a id="ch04-ex4C-q7"></a>
##### Question 7
The curve $y=2 \mathrm{e}^{2 x}+\mathrm{e}^{-x}$ cuts the $y$-axis at the point $P$. Find the equation of the tangent to the curve at the point $P$ and state the coordinates of the point where this tangent cuts the $x$-axis.

<a id="ch04-ex4C-q8"></a>
##### Question 8
Find the exact coordinates of the stationary point on the curve $y=(x-4) \mathrm{e}^{x}$ and determine its nature.

<a id="ch04-ex4C-q9"></a>
##### Question 9
Find the exact coordinates of the stationary point on the curve $y=\frac{\mathrm{e}^{2 x}}{x^{2}}$ and determine its nature.

<a id="ch04-ex4C-q10"></a>
##### Question 10
The equation of a curve is $y=x^{2} \mathrm{e}^{-x}$.

**a** Find the $x$-coordinates of the stationary points of the curve and determine the nature of these stationary points.

**b** Show that the equation of the normal to the curve at the point where $x=1$ is $\mathrm{e}^{2} x+\mathrm{e} y=1+\mathrm{e}^{2}$.

<a id="ch04-ex4C-q11"></a>
##### Question 11
Find the exact value of the $x$-coordinates of the points on the curve $y=x^{2} \mathrm{e}^{-2 x}$ at which $\frac{\mathrm{d}^{2} y}{\mathrm{~d} x^{2}}=0$.

<a id="ch04-ex4C-q12"></a>
##### Question 12
Find the coordinates of the stationary point on the curve $y=\frac{\mathrm{e}^{2 x-1}}{x}$.

<a id="ch04-ex4C-q13"></a>
##### Question 13
By writing 2 as $\mathrm{e}^{\ln 2}$, prove that $\frac{\mathrm{d}}{\mathrm{d} x}\left(2^{x}\right)=2^{x} \ln 2$.

<a id="ch04-ex4C-q14"></a>
##### Question 14
The equation of a curve is $y=x\left(3^{x}\right)$.

Find the exact value of the gradient of the tangent to the curve at the point where $x=1$.

## 4.4 Derivatives of natural logarithmic functions

#### EXPLORE 4.2

![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-091_592_740_1122_539.jpg)

Here is a sketch of the graph of $y=\ln x$. Can you sketch a graph of its derivative (gradient function)? Discuss your sketch with your classmates.

Now sketch the graphs using graphing software. Can you suggest a formula for the derivative of $\ln x$ ? (It might be helpful to look at the coordinates of some of the points on the graph of the derivative.)

### The derivative of $\boldsymbol{\operatorname { l n }} \boldsymbol{x}$

In Chapter 2, you learnt that if $y=\ln x$, then $\mathrm{e}^{y}=x$.

In Section 4.3, you learnt that if $y=\mathrm{e}^{x}$, then $\frac{\mathrm{d} y}{\mathrm{~d} x}=\mathrm{e}^{x}$.

Using these two results we can find the rule for differentiating $\ln x$.

$$
\begin{align}
y & =\ln x & & \\
\mathrm{e}^{y} & =x & & \text { Differentiate both sides with respect to } y . \\
\mathrm{e}^{y} & =\frac{\mathrm{d} x}{\mathrm{~d} y} & & \text { Rearrange and replace } \mathrm{e}^{y} \text { by } x . \\
\frac{\mathrm{d} y}{\mathrm{~d} x} & =\frac{1}{x} & &
\end{align}
$$

<a id="ch04-kp-4.5"></a>
#### KEY POINT 4.5

$$
\frac{\mathrm{d}}{\mathrm{~d} x}(\ln x)=\frac{1}{x}
$$

The derivative of $\boldsymbol{\operatorname { l n }} \mathbf{f}(\boldsymbol{x})$ Consider the function $y=\ln \mathrm{f}(x)$.

Let $y=\ln u \quad$ where $\quad u=\mathrm{f}(x)$

$$
\frac{\mathrm{d} y}{\mathrm{~d} u}=\frac{1}{u} \quad \frac{\mathrm{~d} u}{\mathrm{~d} x}=\mathrm{f}^{\prime}(x)
$$

Using the chain rule:

$$
\text { ule: }\begin{align}
\frac{\mathrm{d} y}{\mathrm{~d} x} & =\frac{\mathrm{d} y}{\mathrm{~d} u} \times \frac{\mathrm{d} u}{\mathrm{~d} x} \\
& =\frac{1}{u} \times \mathrm{f}^{\prime}(x) \\
& =\frac{\mathrm{f}^{\prime}(x)}{\mathrm{f}(x)} \\
\frac{\mathrm{d}}{\mathrm{~d} x}[\ln \mathrm{f}(x)] & =\frac{\mathrm{f}^{\prime}(x)}{\mathrm{f}(x)}
\end{align}
$$

<a id="ch04-kp-4.6"></a>
#### KEY POINT 4.6

In particular,

$$
\frac{\mathrm{d}}{\mathrm{~d} x}[\ln (a x+b)]=\frac{a}{a x+b}
$$

<a id="ch04-we-4.7"></a>
#### WORKED EXAMPLE 4.7

Differentiate with respect to $x$.

**a** $\ln 2 x$

**b** $\ln (4 x-3)$

**c** $\quad \ln \sqrt{5-x}$

Answer

**a**

$$
\begin{align}
\frac{\mathrm{d}}{\mathrm{~d} x}(\ln 2 x) & =\frac{2}{2 x} \\
& =\frac{1}{x}
\end{align}
$$

**b** $\frac{\mathrm{d}}{\mathrm{d} x}[\ln (4 x-3)]=\frac{4}{4 x-3}$ 'Inside' differentiated.

'Inside'

**c** Method 1:

$$
\begin{align}
\frac{\mathrm{d}}{\mathrm{~d} x}[\ln \sqrt{5-x}] & =\frac{\frac{1}{2}(5-x)^{-\frac{1}{2}}(-1)}{\sqrt{5-x}} \\
& =-\frac{1}{2(5-x)}
\end{align}
$$

Method 2: using the rules of logarithms before differentiating.

$$
\begin{align}
\frac{\mathrm{d}}{\mathrm{~d} x}[\ln \sqrt{5-x}] & =\frac{\mathrm{d}}{\mathrm{~d} x}\left[\ln (5-x)^{\frac{1}{2}}\right] \\
& =\frac{\mathrm{d}}{\mathrm{~d} x}\left[\frac{1}{2} \ln (5-x)\right] \\
& =\frac{1}{2} \times \frac{\mathrm{d}}{\mathrm{~d} x}[\ln (5-x)] \\
& =\frac{1}{2} \times \frac{-1}{5-x} \\
& =-\frac{1}{2(5-x)}
\end{align}
$$

<a id="ch04-we-4.8"></a>
#### WORKED EXAMPLE 4.8

Differentiate with respect to $x$.

**a** $2 x^{4} \ln 5 x$

**b** $\frac{\ln 2 x}{x^{3}}$

Answer

**a**

$$
\begin{align}
\frac{\mathrm{d}}{\mathrm{~d} x}\left(2 x^{4} \ln 5 x\right) & =2 x^{4} \times \frac{\mathrm{d}}{\mathrm{~d} x}(\ln 5 x)+\ln 5 x \times \frac{\mathrm{d}}{\mathrm{~d} x}\left(2 x^{4}\right) \qquad \text { Product rule. } \\
& =2 x^{4} \times \frac{5}{5 x}+\ln 5 x \times 8 x^{3} \\
& =2 x^{3}+8 x^{3} \ln 5 x
\end{align}
$$

**b**

$$
\begin{align}
\frac{\mathrm{d}}{\mathrm{~d} x}\left(\frac{\ln 2 x}{x^{3}}\right) & =\frac{x^{3} \times \frac{\mathrm{d}}{\mathrm{~d} x}(\ln 2 x)-\ln 2 x \times \frac{\mathrm{d}}{\mathrm{~d} x}\left(x^{3}\right)}{\left(x^{3}\right)^{2}} \quad \because \quad \text { Quotient rule. } \\
& =\frac{x^{3} \times \frac{2}{2 x}-\ln 2 x \times 3 x^{2}}{x^{6}} \\
& =\frac{x^{2}-3 x^{2} \ln 2 x}{x^{6}} \\
& =\frac{1-3 \ln 2 x}{x^{4}}
\end{align}
$$

<a id="ch04-ex4D"></a>
### EXERCISE 4D

<a id="ch04-ex4D-q1"></a>
##### Question 1
Differentiate with respect to $x$.

**a** $\ln 3 x$

**b** $\ln 7 x$

**c** $\ln (2 x+1)$

**d** $5+\ln \left(x^{2}+1\right)$

**e** $\ln (2 x-1)^{2}$

**f** $\ln \sqrt{x-3}$

**g** $\ln (x+3)^{5}$

**h** $3 x+\ln \left(\frac{2}{x}\right)$

**i** $5 x+\ln \left(\frac{2}{1-2 x}\right)$

**j** $\quad \ln (\ln x)$

**k** $\ln (2-\sqrt{x})^{2}$

**l** $\ln (5 x+\ln x)$

<a id="ch04-ex4D-q2"></a>
##### Question 2
The answers to question 1 parts a and b are the same. Why is this the case? How many different ways can you justify this?

<a id="ch04-ex4D-q3"></a>
##### Question 3
Differentiate with respect to $x$.

**a** $x \ln x$

**b** $2 x^{3} \ln x$

**c** $x \ln (2 x+1)$

**d** $3 x \ln 2 x$

**e** $\quad x \ln (\ln x)$

**f** $\frac{\ln 5 x}{x}$

**g** $\frac{2}{\ln x}$

**h** $\frac{\ln (3 x-2)}{x}$

**i** $\frac{\ln (2 x+1)}{4 x-1}$

<a id="ch04-ex4D-q4"></a>
##### Question 4
**a** Sketch the graph of the function $y=\ln (2 x-3)$.

**b** Find the gradient of the curve $y=\ln (2 x-3)$ at the point where $x=5$.

<a id="ch04-ex4D-q5"></a>
##### Question 5
Find the gradient of the curve $y=\mathrm{e}^{2 x}-5 \ln (2 x+1)$ at the point where $x=0$.

<a id="ch04-ex4D-q6"></a>
##### Question 6
A curve has equation $y=x^{2} \ln 5 x$.

Find the value of $\frac{\mathrm{d} y}{\mathrm{~d} x}$ and $\frac{\mathrm{d}^{2} y}{\mathrm{~d} x^{2}}$ at the point where $x=2$.

<a id="ch04-ex4D-q7"></a>
##### Question 7
The equation of a curve is $y=x^{2} \ln x$. Find the exact coordinates of the stationary point on this curve and determine whether it is a maximum or a minimum point.

<a id="ch04-ex4D-q8"></a>
##### Question 8
The equation of a curve is $y=\frac{\ln x}{x}$. Find the exact coordinates of the stationary point on this curve and determine whether it is a maximum or a minimum point.

<a id="ch04-ex4D-q9"></a>
##### Question 9
Find the equation of the tangent to the curve $y=\ln (5 x-4)$ at the point where $x=1$.

<a id="ch04-ex4D-q10"></a>
##### Question 10
Use the laws of logarithms to help differentiate these expressions with respect to $x$.

**a** $\ln \sqrt{5 x-1}$

**b** $\quad \ln \left(\frac{1}{3 x+2}\right)$

**c** $\ln \left[x(x+1)^{5}\right]$

**d** $\quad \ln \left(\frac{2 x+3}{x-1}\right)$

**e** $\ln \left(\frac{1-3 x}{x^{2}}\right)$

**f** $\ln \left[\frac{x(x-2)}{x+4}\right]$

**g** $\ln \left[\frac{3-x}{(x+4)(x-1)}\right]$

**h** $\quad \ln \left[\frac{8}{(x+1)^{2}(x-2)}\right]$

**i** $\ln \left[\frac{(x+2)(2 x-1)}{x(x+5)}\right]$

<a id="ch04-ex4D-q11"></a>
##### Question 11
Find $\frac{\mathrm{d} y}{\mathrm{~d} x}$, in terms of $x$, for each of the following.

**a** $\mathrm{e}^{y}=2 x^{2}-1$

**b** $\mathrm{e}^{y}=3 x^{3}+2 x$

**c** $\mathrm{e}^{y}=(x+1)(x-5)$

#### TIP

Take the natural logarithm of both sides of the equation before differentiating.

<a id="ch04-ex4D-q12"></a>
##### Question 11
A curve has equation $x=\frac{1}{5}\left[\mathrm{e}^{y(2 x-3)}+4\right]$. Find the value of $\frac{\mathrm{d} y}{\mathrm{~d} x}$ when $x=1$.

## 4.5 Derivatives of trigonometric functions

#### EXPLORE 4.3

Graphing software has been used to draw the graphs of $y=\sin x$ and $y=\cos x$ for $0 \leqslant x \leqslant 2 \pi$ together with their gradient (derived) functions.

![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-095_302_641_901_259.jpg)

![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-095_300_636_904_912.jpg)

Discuss with your classmates why, for the function $y=\sin x$, you would expect the graph of the gradient function to have this shape. Do the same for the graph of $y=\cos x$.

Can you suggest how to complete the following formulae?

$$
\frac{\mathrm{d}}{\mathrm{~d} x}(\sin x)=\quad \frac{\mathrm{d}}{\mathrm{~d} x}(\cos x)=
$$

The derivative of $\boldsymbol{\operatorname { s i n }} \boldsymbol{x}$ Consider the function $\mathrm{f}(x)=\sin x$, where $x$ is measured in radians, and two points whose $x$-coordinates are $x$ and $x+\delta x$ where $\delta x$ is a small increase in $x$.

![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-095_264_610_1815_263.jpg)

$$
\begin{align}
\frac{\mathrm{d} y}{\mathrm{~d} x} & =\lim _{\delta x \rightarrow 0} \frac{\mathrm{f}(x+\delta x)-\mathrm{f}(x)}{(x+\delta x)-x} & & \\
& =\lim _{\delta x \rightarrow 0} \frac{\sin (x+\delta x)-\sin x}{\delta x} & & \text { Expand } \sin (x+\delta x) \\
& =\lim _{\delta x \rightarrow 0} \frac{\sin x \cos \delta x+\cos x \sin \delta x-\sin x}{\delta x} & & \text { As } \delta x \rightarrow 0, \cos \delta x \rightarrow 1 \\
& =\cos x & & \text { and } \sin \delta x \rightarrow \delta x .
\end{align}
$$

<a id="ch04-kp-4.7"></a>
#### KEY POINT 4.7

$$
\frac{\mathrm{d}}{\mathrm{~d} x}(\sin x)=\cos x
$$

Similarly, we can show that

$$
\frac{\mathrm{d}}{\mathrm{~d} x}(\cos x)=-\sin x
$$

We can find the derivative of $\tan x$ using these two results together with the quotient rule.

$$
\begin{align}
\frac{\mathrm{d}}{\mathrm{~d} x}(\tan x) & =\frac{\mathrm{d}}{\mathrm{~d} x}\left(\frac{\sin x}{\cos x}\right) & & \text { Use the quotient rule. } \\
& =\frac{\cos x \times \frac{\mathrm{d}}{\mathrm{~d} x}(\sin x)-\sin x \times \frac{\mathrm{d}}{\mathrm{~d} x}(\cos x)}{(\cos x)^{2}} & & \\
& =\frac{\cos x \times \cos x-\sin x \times(-\sin x)}{\cos ^{2} x} & & \\
& =\frac{\cos ^{2} x+\sin ^{2} x}{\cos ^{2} x} & & \text { Use } \cos ^{2} x+\sin ^{2} x=1 . \\
& =\frac{1}{\cos ^{2} x} & & \text { Use } \frac{1}{\cos x}=\sec x . \\
& =\sec ^{2} x & &
\end{align}
$$

<a id="ch04-kp-4.8"></a>
#### KEY POINT 4.8

$$
\frac{\mathrm{d}}{\mathrm{~d} x}(\tan x)=\sec ^{2} x
$$

<a id="ch04-we-4.9"></a>
#### WORKED EXAMPLE 4.9

Differentiate with respect to $x$.

**a** $2 \sin x$

**b** $x \cos x$

**c** $\frac{\tan x}{x^{2}}$

**d** $(3+2 \sin x)^{5}$

Answer

**a**

$$
\begin{align}
\frac{\mathrm{d}}{\mathrm{~d} x}(2 \sin x) & =2 \frac{\mathrm{~d}}{\mathrm{~d} x}(\sin x) \\
& =2 \cos x
\end{align}
$$

**b**

$$
\begin{align}
\frac{\mathrm{d}}{\mathrm{~d} x}(x \cos x) & =x \times \frac{\mathrm{d}}{\mathrm{~d} x}(\cos x)+\cos x \times \frac{\mathrm{d}}{\mathrm{~d} x}(x) \\
& =-x \sin x+\cos x
\end{align}
$$

**c**

$$
\begin{align}
\frac{\mathrm{d}}{\mathrm{~d} x}\left(\frac{\tan x}{x^{2}}\right) & =\frac{x^{2} \times \frac{\mathrm{d}}{\mathrm{~d} x}(\tan x)-\tan x \times \frac{\mathrm{d}}{\mathrm{~d} x}\left(x^{2}\right)}{x^{4}} \\
& =\frac{x^{2} \times \sec ^{2} x-\tan x \times 2 x}{x^{4}} \\
& =\frac{x \sec ^{2} x-2 \tan x}{x^{3}}
\end{align}
$$

**d**

$$
\begin{align}
\frac{\mathrm{d}}{\mathrm{~d} x}\left[(3+2 \sin x)^{5}\right] & =5(3+2 \sin x)^{4} \times 2 \cos x \\
& =10 \cos x(3+2 \sin x)^{4}
\end{align}
$$

Derivatives of $\boldsymbol{\operatorname { s i n }}(\boldsymbol{a} \boldsymbol{x}+\boldsymbol{b}), \boldsymbol{\operatorname { c o s }}(\boldsymbol{a} \boldsymbol{x}+\boldsymbol{b})$ and $\boldsymbol{\operatorname { t a n }}(\boldsymbol{a} \boldsymbol{x}+\boldsymbol{b})$ Consider the function $y=\sin (a x+b)$ where $x$ is measured in radians.

Let

$$
\begin{align}
y & =\sin u & \text { where } & u \\
\frac{\mathrm{~d} y}{\mathrm{~d} u} & =\cos u & \frac{\mathrm{~d} u}{\mathrm{~d} x} & =a
\end{align}
$$

Using the chain rule:

$$
\begin{align}
\frac{\mathrm{d} y}{\mathrm{~d} x} & =\frac{\mathrm{d} y}{\mathrm{~d} u} \times \frac{\mathrm{d} u}{\mathrm{~d} x} \\
& =\cos u \times a \\
& =a \cos (a x+b)
\end{align}
$$

<a id="ch04-kp-4.9"></a>
#### KEY POINT 4.9

$$
\frac{\mathrm{d}}{\mathrm{~d} x}[\sin (a x+b)]=a \cos (a x+b)
$$

Similarly, it can be shown that:

$$
\begin{align}
& \frac{\mathrm{d}}{\mathrm{~d} x}[\cos (a x+b)]=-a \sin (a x+b) \\
& \frac{\mathrm{d}}{\mathrm{~d} x}[\tan (a x+b)]=a \sec ^{2}(a x+b)
\end{align}
$$

<a id="ch04-we-4.10"></a>
#### WORKED EXAMPLE 4.10

Differentiate with respect to $x$.

**a** $2 \sin 3 x$

**b** $4 x \tan 2 x$

**c** $\frac{\cos \left(2 x-\frac{\pi}{4}\right)}{x^{2}}$

**d** $(3-2 \cos 5 x)^{4}$

Answer

**a**

$$
\begin{align}
\frac{\mathrm{d}}{\mathrm{~d} x}(2 \sin 3 x) & =2 \frac{\mathrm{~d}}{\mathrm{~d} x}(\sin 3 x) \\
& =2 \times \cos 3 x \times(3) \\
& =6 \cos 3 x
\end{align}
$$

**b**

$$
\begin{align}
\frac{\mathrm{d}}{\mathrm{~d} x}(4 x \tan 2 x) & =4 x \times \frac{\mathrm{d}}{\mathrm{~d} x}(\tan 2 x)+\tan 2 x \times \frac{\mathrm{d}}{\mathrm{~d} x}(4 x) \\
& =4 x \times \sec ^{2} 2 x(2)+\tan 2 x \times(4) \\
& =8 x \sec ^{2} 2 x+4 \tan 2 x
\end{align}
$$

Product rule.

**c**

$$
\frac{\mathrm{d}}{\mathrm{~d} x}\left[\frac{\cos \left(2 x-\frac{\pi}{4}\right)}{x^{2}}\right]=\frac{x^{2} \times \frac{\mathrm{d}}{\mathrm{~d} x}\left[\cos \left(2 x-\frac{\pi}{4}\right)\right]-\cos \left(2 x-\frac{\pi}{4}\right) \times \frac{\mathrm{d}}{\mathrm{~d} x}\left[x^{2}\right]}{\left(x^{2}\right)^{2}} \qquad \text { Quotient rule. }
$$

$$
\begin{align}
& =\frac{-2 x^{2} \sin \left(2 x-\frac{\pi}{4}\right)-2 x \cos \left(2 x-\frac{\pi}{4}\right)}{x^{4}} \\
& =\frac{-2 x \sin \left(2 x-\frac{\pi}{4}\right)-2 \cos \left(2 x-\frac{\pi}{4}\right)}{x^{3}}
\end{align}
$$

**d**

$$
\begin{align}
\frac{\mathrm{d}}{\mathrm{~d} x}\left[(3-2 \cos 5 x)^{4}\right] & =4(3-2 \cos 5 x)^{3} \times 10 \sin 5 x \\
& =40 \sin 5 x(3-2 \cos 5 x)^{3}
\end{align}
$$

Chain rule.

<a id="ch04-ex4E"></a>
### EXERCISE 4E

<a id="ch04-ex4E-q1"></a>
##### Question 1
Differentiate with respect to $x$.

**a** $2+\sin x$

**b** $2 \sin x+3 \cos x$

**c** $2 \cos x-\tan x$

**d** $3 \sin 2 x$

**e** $4 \tan 5 x$

**f** $2 \cos 3 x-\sin 2 x$

**g** $\tan (3 x+2)$

**h** $\sin \left(2 x+\frac{\pi}{3}\right)$

**i** $2 \cos \left(3 x-\frac{\pi}{6}\right)$

<a id="ch04-ex4E-q2"></a>
##### Question 2
Differentiate with respect to $x$.

**a** $\sin ^{3} x$

**b** $5 \cos ^{2} 3 x$

**c** $\sin ^{2} x-2 \cos x$

**d** $(3-\cos x)^{4}$

**e** $2 \sin ^{3}\left(2 x+\frac{\pi}{6}\right)$

**f** $3 \cos ^{4} x+2 \tan ^{2}\left(2 x-\frac{\pi}{4}\right)$

<a id="ch04-ex4E-q3"></a>
##### Question 3
Differentiate with respect to $x$.

**a** $x \sin x$

**b** $5 x \cos 3 x$

**c** $x^{2} \tan x$

**d** $x \cos ^{3} 2 x$

**e** $\frac{5}{\cos 3 x}$

**f** $\frac{x}{\cos x}$

**g** $\frac{\tan x}{x}$

**h** $\frac{\sin x}{2+\cos x}$

**i** $\frac{\sin x}{3 x-1}$

**j** $\frac{1}{\sin ^{3} 2 x}$

**k** $\frac{3 x}{\sin 2 x}$

**l** $\frac{\sin x+\cos x}{\sin x-\cos x}$

<a id="ch04-ex4E-q4"></a>
##### Question 4
Differentiate with respect to $x$.

**a** $\mathrm{e}^{\sin x}$

**b** $\mathrm{e}^{\cos 2 x}$

**c** $\mathrm{e}^{\tan 3 x}$

**d** $\mathrm{e}^{(\sin x-\cos x)}$

**e** $\mathrm{e}^{x} \cos x$

**f** $\mathrm{e}^{x} \sin 2 x$

**g** $\mathrm{e}^{x}(2 \cos x-\sin x)$

**h** $x^{3} \mathrm{e}^{\cos x}$

**i** $\quad \ln (\cos x)$

**j** $x \ln (\sin x)$

**k** $\frac{\cos 2 x}{\mathrm{e}^{2 x+1}}$

**l** $\frac{x \sin 2 x}{\mathrm{e}^{2 x}}$

<a id="ch04-ex4E-q5"></a>
##### Question 5
Find the gradient of the curve $y=3 \sin 2 x-5 \tan x$ at the point where $x=0$.

<a id="ch04-ex4E-q6"></a>
##### Question 6
Find the exact value of the gradient of the curve $y=2 \sin 3 x-4 \cos x$ at the point $\left(\frac{\pi}{3},-2\right)$.

<a id="ch04-ex4E-q7"></a>
##### Question 7
Given that $y=\sin ^{2} x$ for $0 \leqslant x \leqslant \pi$, find the exact values of the $x$-coordinates of the points on the curve where the gradient is $\frac{\sqrt{3}}{2}$.

<a id="ch04-ex4E-q8"></a>
##### Question 8
Prove that the gradient of the curve $y=\frac{5}{2-\tan x}$ is always positive.

<a id="ch04-ex4E-q9"></a>
##### Question 9
**a** By writing $\sec x$ as $\frac{1}{\cos x}$, find $\frac{\mathrm{d}}{\mathrm{d} x}(\sec x)$.

**b** By writing $\operatorname{cosec} x$ as $\frac{1}{\sin x}$, find $\frac{\mathrm{d}}{\mathrm{d} x}(\operatorname{cosec} x)$.

**c** By writing $\cot x$ as $\frac{\cos x}{\sin x}$, find $\frac{\mathrm{d}}{\mathrm{d} x}(\cot x)$.

<a id="ch04-ex4E-q10"></a>
##### Question 10
Prove that the normal to the curve $y=x \sin x$ at the point $P\left(\frac{\pi}{2}, \frac{\pi}{2}\right)$ intersects the $x$-axis at the point $(\pi, 0)$.

<a id="ch04-ex4E-q11"></a>
##### Question 11
The equation of a curve is $y=5 \sin 3 x-2 \cos x$. Find the equation of the tangent to the curve at the point $\left(\frac{\pi}{3},-1\right)$. Give the answer in the form $y=m x+c$, where the values of $m$ and $c$ are correct to 3 significant figures.

<a id="ch04-ex4E-q12"></a>
##### Question 12
A curve has equation $y=3 \cos 2 x+4 \sin 2 x+1$ for $0 \leqslant x \leqslant \pi$. Find the $x$-coordinates of the stationary points of the curve, giving your answer correct to 3 significant figures.

<a id="ch04-ex4E-q13"></a>
##### Question 13
A curve has equation $y=\mathrm{e}^{x} \cos x$ for $0 \leqslant x \leqslant \frac{\pi}{2}$. Find the exact value of the $x$-coordinate of the stationary point of the curve and determine the nature of this stationary point.

<a id="ch04-ex4E-q14"></a>
##### Question 14
A curve has equation $y=\frac{\sin 2 x}{\mathrm{e}^{2 x}}$ for $0 \leqslant x \leqslant \frac{\pi}{2}$. Find the exact value for the $x$-coordinate of the stationary point of this curve.

<a id="ch04-ex4E-q15"></a>
##### Question 15
A curve has equation $y=\frac{\mathrm{e}^{3 x}}{\sin 3 x}$ for $0<x<\frac{\pi}{2}$. Find the exact value for the $x$-coordinate of the stationary point of this curve and determine the nature of this point.

<a id="ch04-ex4E-q16"></a>
##### Question 16
A curve has equation $y=\sin 2 x-x$ for $0 \leqslant x \leqslant 2 \pi$. Find the $x$-coordinates of the stationary points of the curve, and determine the nature of these stationary points.

<a id="ch04-ex4E-q17"></a>
##### Question 17
A curve has equation $y=\tan x \cos 2 x$ for $0 \leqslant x<\frac{\pi}{2}$. Find the $x$-coordinate of the stationary point on the curve giving your answer correct to 3 significant figures.

## 4.6 Implicit differentiation

All the functions that we have differentiated so far have been of the form $y=\mathrm{f}(x)$. These are called explicit functions as $y$ is given explicitly in terms of $x$. However, many functions cannot be expressed in this form, for example $x^{3}+5 x y+y^{3}=16$.

When a function is given as an equation connecting $x$ and $y$, where $y$ is not the subject, it is called an implicit function.

The chain rule $\left(\frac{\mathrm{d} y}{\mathrm{~d} x}=\frac{\mathrm{d} y}{\mathrm{~d} u} \times \frac{\mathrm{d} u}{\mathrm{~d} x}\right)$ and the product rule $\left(\frac{\mathrm{d}}{\mathrm{d} x}(u v)=u \frac{\mathrm{~d} v}{\mathrm{~d} x}+v \frac{\mathrm{~d} u}{\mathrm{~d} x}\right)$ are used extensively to differentiate implicit functions.

This is illustrated in the following Worked examples.

<a id="ch04-we-4.11"></a>
#### WORKED EXAMPLE 4.11

Differentiate each of these expressions with respect to $x$.

**a** $y^{3}$

**b** $4 x^{2} y^{5}$

**c** $x^{3}+5 x y$

Answer

**a**

$$
\begin{align}
\frac{\mathrm{d}}{\mathrm{~d} x}\left(y^{3}\right) & =\frac{\mathrm{d}}{\mathrm{~d} y}\left(y^{3}\right) \times \frac{\mathrm{d} y}{\mathrm{~d} x} \\
& =3 y^{2} \frac{\mathrm{~d} y}{\mathrm{~d} x}
\end{align}
$$

Chain rule.

**b**

$$
\begin{align}
\frac{\mathrm{d}}{\mathrm{~d} x}\left(4 x^{2} y^{5}\right) & =4 x^{2} \frac{\mathrm{~d}}{\mathrm{~d} x}\left(y^{5}\right)+y^{5} \frac{\mathrm{~d}}{\mathrm{~d} x}\left(4 x^{2}\right) \qquad \text { Product rule. } \\
& =4 x^{2} \frac{\mathrm{~d}}{\mathrm{~d} x}\left(y^{5}\right)+8 x y^{5} \qquad \text { Chain rule: } \frac{\mathrm{d}}{\mathrm{~d} x}\left(y^{5}\right)=5 y^{4} \frac{\mathrm{~d} y}{\mathrm{~d} x} . \\
& =20 x^{2} y^{4} \frac{\mathrm{~d} y}{\mathrm{~d} x}+8 x y^{5}
\end{align}
$$

**c**

$$
\begin{align}
\frac{\mathrm{d}}{\mathrm{~d} x}\left(x^{3}+5 x y\right) & =\frac{\mathrm{d}}{\mathrm{~d} x}\left(x^{3}\right)+\frac{\mathrm{d}}{\mathrm{~d} x}(5 x y) \\
& =3 x^{2}+5 x \frac{\mathrm{~d}}{\mathrm{~d} x}(y)+y \frac{\mathrm{~d}}{\mathrm{~d} x}(5 x) \\
& =3 x^{2}+5 x \frac{\mathrm{~d} y}{\mathrm{~d} x}+5 y
\end{align}
$$

<a id="ch04-we-4.12"></a>
#### WORKED EXAMPLE 4.12

Find $\frac{\mathrm{d} y}{\mathrm{~d} x}$ for the curve $x^{3}+y^{3}=4 x y$. Hence find the gradient of the curve at the point (2, 2).

Answer

$$
\begin{align}
x^{3}+y^{3} & =4 x y \\
\frac{\mathrm{~d}}{\mathrm{~d} x}\left(x^{3}\right)+\frac{\mathrm{d}}{\mathrm{~d} x}\left(y^{3}\right) & =\frac{\mathrm{d}}{\mathrm{~d} x}(4 x y) \\
3 x^{2}+\frac{\mathrm{d}}{\mathrm{~d} y}\left(y^{3}\right) \times \frac{\mathrm{d} y}{\mathrm{~d} x} & =4 x \frac{\mathrm{~d}}{\mathrm{~d} x}(y)+y \frac{\mathrm{~d}}{\mathrm{~d} x}(4 x) \qquad \text { Differentiate with respect to } x . \\
3 x^{2}+3 y^{2} \frac{\mathrm{~d} y}{\mathrm{~d} x} & =4 x \frac{\mathrm{~d} y}{\mathrm{~d} x}+4 y \\
3 y^{2} \frac{\mathrm{~d} y}{\mathrm{~d} x}-4 x \frac{\mathrm{~d} y}{\mathrm{~d} x} & =4 y-3 x^{2} \\
\left(3 y^{2}-4 x\right) \frac{\mathrm{d} y}{\mathrm{~d} x} & =4 y-3 x^{2} \\
\frac{\mathrm{~d} y}{\mathrm{~d} x} & =\frac{4 y-3 x^{2}}{3 y^{2}-4 x}
\end{align}
$$

When $x=2$ and $y=2$,

$$
\frac{\mathrm{d} y}{\mathrm{~d} x}=\frac{4(2)-3(2)^{2}}{3(2)^{2}-4(2)}=-1
$$

Gradient of the curve at the point $(2,2)$ is -1.

<a id="ch04-we-4.13"></a>
#### WORKED EXAMPLE 4.13

The equation of a curve is $3 x^{2}+2 x y+y^{2}=6$. Find the coordinates of the two stationary points on the curve.

Answer

$$
\begin{align}
& 3 x^{2}+2 x y+y^{2}=6 \\
& \text { Differentiate with respect to } x \text {. } \\
& \frac{\mathrm{d}}{\mathrm{~d} x}\left(3 x^{2}\right)+\frac{\mathrm{d}}{\mathrm{~d} x}(2 x y)+\frac{\mathrm{d}}{\mathrm{~d} x}\left(y^{2}\right)=\frac{\mathrm{d}}{\mathrm{~d} x}(6) \\
& \text { Use product rule for } \frac{\mathrm{d}}{\mathrm{~d} x}(2 x y) \text {. } \\
& 6 x+2 x \frac{\mathrm{~d}}{\mathrm{~d} x}(y)+y \frac{\mathrm{~d}}{\mathrm{~d} x}(2 x)+\frac{\mathrm{d}}{\mathrm{~d} x}\left(y^{2}\right)=0 \\
& \text { Use chain rule for } \frac{\mathrm{d}}{\mathrm{~d} x}\left(y^{2}\right) \text {. } \\
& 6 x+2 x \frac{\mathrm{~d} y}{\mathrm{~d} x}+2 y+2 y \frac{\mathrm{~d} y}{\mathrm{~d} x}=0 \\
& \text { Divide by } 2 \text { and rearrange. } \\
& x \frac{\mathrm{~d} y}{\mathrm{~d} x}+y \frac{\mathrm{~d} y}{\mathrm{~d} x}=-y-3 x \\
& \text { Factorise. } \\
& (x+y) \frac{\mathrm{d} y}{\mathrm{~d} x}=-y-3 x \\
& \text { Rearrange. } \\
& \frac{\mathrm{d} y}{\mathrm{~d} x}=\frac{-y-3 x}{x+y}
\end{align}
$$

Stationary points occur when

$$
\begin{align}
\frac{\mathrm{d} y}{\mathrm{~d} x} & =0 . \\
-y-3 x & =0 \\
y & =-3 x
\end{align}
$$

Substituting $y=-3 x$ into the equation of the curve gives:

$$
\begin{align}
3 x^{2}+2 x(-3 x)+(-3 x)^{2} & =6 \\
6 x^{2} & =6 \\
x & = \pm 1
\end{align}
$$

The stationary points are (-1, 3) and (1, -3).

<a id="ch04-ex4F"></a>
### EXERCISE 4F

<a id="ch04-ex4F-q1"></a>
##### Question 1
Differentiate each expression with respect to $x$.

**a** $y^{5}$

**b** $x^{3}+2 y^{2}$

**c** $5 x^{2}+\ln y$

**d** $2+\sin y$

**e** $6 x^{2} y^{3}$

**f** $y^{2}+x y$

**g** $x^{3}-7 x y+y^{3}$

**h** $x \sin y+y \cos x$

**i** $x^{3} \ln y$

**j** $x \cos 2 y$

**k** $5 y+\mathrm{e}^{x} \sin y$

**l** $2 x \mathrm{e}^{\cos y}$

<a id="ch04-ex4F-q2"></a>
##### Question 2
Find $\frac{\mathrm{d} y}{\mathrm{~d} x}$ for each of these functions.

**a** $x^{3}+2 x y+y^{3}=10$

**b** $x^{2} y+y^{2}=5 x$

**c** $2 x^{2}+5 x y+y^{2}=8$

**d** $x \ln y=2 x+5$

**e** $2 \mathrm{e}^{x} y+\mathrm{e}^{2 x} y^{3}=10$

**f** $\quad \ln (x y)=4-y^{2}$

**g** $x y^{3}=2 \ln y$

**h** $\ln x-2 \ln y+5 x y=3$

<a id="ch04-ex4F-q3"></a>
##### Question 3
Find the gradient of the curve $x^{2}+3 x y-5 y+y^{3}=22$ at the point $(1,3)$.

<a id="ch04-ex4F-q4"></a>
##### Question 4
Find the gradient of the curve $2 x^{3}-4 x y+y^{3}=16$ at the point where the curve crosses the $x$-axis.

<a id="ch04-ex4F-q5"></a>
##### Question 5
A curve has equation $2 x^{2}+3 y^{2}-2 x+4 y=4$. Find the equation of the tangent to the curve at the point (1, -2).

<a id="ch04-ex4F-q6"></a>
##### Question 6
The equation of a curve is $4 x^{2} y+8 \ln x+2 \ln y=4$. Find the equation of the normal to the curve at the point (1, 1).

<a id="ch04-ex4F-q7"></a>
##### Question 7
The equation of a curve is $5 x^{2}+2 x y+2 y^{2}=45$.

**a** Given that there are two points on the curve where the tangent is parallel to the $x$-axis, show by differentiation that, at these points, $y=-5 x$.

**b** Hence find the coordinates of the two points.

<a id="ch04-ex4F-q8"></a>
##### Question 8
The equation of a curve is $y^{2}-4 x y-x^{2}=20$.

**a** Find the coordinates of the two points on the curve where $x=4$.

**b** Show that at one of these points the tangent to the curve is parallel to the $x$-axis.

**c** Find the equation of the tangent to the curve at the other point.

<a id="ch04-ex4F-q9"></a>
##### Question 9
The equation of a curve is $y^{3}-12 x y+16=0$.

**a** Show that the curve has no stationary points.

**b** Find the coordinates of the point on the curve where the tangent is parallel to the $y$-axis.

<a id="ch04-ex4F-q10"></a>
##### Question 10
Find the gradient of the curve $5 \mathrm{e}^{x} y^{2}+2 \mathrm{e}^{x} y=88$ at the point $(0,4)$.

<a id="ch04-ex4F-q11"></a>
##### Question 11
The equation of a curve is $x^{2}-4 x+6 y+2 y^{2}=12$. Find the coordinates of the two points on the curve at which the gradient is $\frac{4}{3}$.

<a id="ch04-ex4F-q12"></a>
##### Question 12
The equation of a curve is $2 x+y \ln x=4 y$. Find the equation of the tangent to the curve at the point with coordinates $\left(1, \frac{1}{2}\right)$.

<a id="ch04-ex4F-q13"></a>
##### Question 13
The equation of a curve is $y=x^{x}$. Find the exact value of the $x$-coordinate of the stationary point on this curve.

<a id="ch04-ex4F-q14"></a>
##### Question 14
Find the stationary points on the curve $x^{2}-x y+y^{2}=48$. By finding $\frac{\mathrm{d}^{2} y}{\mathrm{~d} x^{2}}$ determine the nature of each of these stationary points.

## 4.7 Parametric differentiation

Sometimes variables $x$ and $y$ are given as a function of a third variable $t$.

For example, $x=1+4 \sin t$ and $y=2 \cos t$.

The variable $t$ is called a parameter and the two equations are called the parametric equations of the curve.

We can find the curve given by the parametric equations $x=1+4 \sin t, y=2 \cos t$ for $0 \leqslant t \leqslant 2 \pi$ by finding the values of $x$ and $y$ for particular values of $t$.

| $t$ | 0 | $\frac{1}{4} \pi$ | $\frac{1}{2} \pi$ | $\frac{3}{4} \pi$ | $\pi$ | $\frac{5}{4} \pi$ | $\frac{3}{2} \pi$ | $\frac{7}{4} \pi$ | $2 \pi$ |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| $x$ | 1 | 3.83 | 5 | 3.83 | 1 | -1.83 | -3 | -1.83 | 1 |
| $y$ | 2 | 1.41 | 0 | -1.41 | -2 | -1.41 | 0 | 1.41 | 2 |

Plotting the coordinates on a grid gives the following graph.

![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-103_436_701_1034_570.jpg)

#### EXPLORE 4.4

**1** Use tables of values for $t, x$ and $y$ to sketch each of the following curves. Use graphing software to check your answers.

**a** $x=t^{3}, \quad y=t^{2}$

**b** $x=t^{2}, \quad y=t^{3}-t$

**c** $x=t+\frac{1}{t}, y=t-\frac{1}{t}$

**2** Use graphing software to draw the curves given by these parametric equations.

**a** $x=\sin t, \quad y=\sin 2 t$

**b** $x=\sin 2 t, \quad y=\sin 3 t$

**c** $x=\sin 4 t, \quad y=\sin 3 t$

**3** The curves in question 2 are called Lissajous curves. Use the internet to find out more about these curves. (A Lissajous curve is shown at the start of this chapter.)

When a curve is given in parametric form, in terms of the parameter $t$, we can use the chain rule to find $\frac{\mathrm{d} y}{\mathrm{~d} x}$ in terms of $t$.

<a id="ch04-we-4.14"></a>
#### WORKED EXAMPLE 4.14

The parametric equations of a curve are $x=t^{2}, y=5-2 t$.

**a** Find $\frac{\mathrm{d} y}{\mathrm{~d} x}$ in terms of the parameter $t$.

**b** Find the equation of the tangent to the curve at the point where $t=2$.

Answer

**a**

$$
\begin{array}{ll} x=t^{2} & \Rightarrow \frac{\mathrm{~d} x}{\mathrm{~d} t}=2 t \\
y=5-2 t & \Rightarrow \frac{\mathrm{~d} y}{\mathrm{~d} t}=-2 \end{array}
$$

$$
\begin{align}
\frac{\mathrm{d} y}{\mathrm{~d} x} & =\frac{\mathrm{d} y}{\mathrm{~d} t} \times \frac{\mathrm{d} t}{\mathrm{~d} x} \\
& =-2 \times \frac{1}{2 t} \\
& =-\frac{1}{t}
\end{align}
$$

**b** When $t=2$, gradient $=-\frac{1}{2}, x=4$ and $y=1$.

Using $y-y_{1}=m\left(x-x_{1}\right)$

$$
\begin{align}
y-1 & =-\frac{1}{2}(x-4) \\
y & =-\frac{1}{2} x+3
\end{align}
$$

<a id="ch04-we-4.15"></a>
#### WORKED EXAMPLE 4.15

The parametric equations of a curve are $x=1+2 \sin ^{2} \theta, y=4 \tan \theta$ for $\frac{\pi}{2}<\theta<\frac{3 \pi}{2}$.

**a** Find $\frac{\mathrm{d} y}{\mathrm{~d} x}$ in terms of the parameter $\theta$.

**b** Find the coordinates of the point on the curve where the tangent is parallel to the $y$-axis.

Answer

**a**

$$
\begin{array}{ll} x=1+2 \sin ^{2} \theta & \Rightarrow \frac{\mathrm{~d} x}{\mathrm{~d} \theta}=4 \sin \theta \cos \theta \\
y=4 \tan \theta \quad \Rightarrow \frac{\mathrm{~d} y}{\mathrm{~d} \theta}=4 \sec ^{2} \theta=\frac{4}{\cos ^{2} \theta} \end{array}
$$

$$
\begin{align}
\frac{d y}{d x} & =\frac{d y}{d \theta} \times \frac{d \theta}{d x} \\
& =\frac{4}{\cos ^{2} \theta} \times \frac{1}{4 \sin \theta \cos \theta} \\
& =\frac{1}{\sin \theta \cos ^{3} \theta}
\end{align}
$$

**b** Tangent is parallel to the $y$-axis when:

$$
\begin{align}
\sin \theta \cos ^{3} \theta & =0 \\
\sin \theta=0 \text { or } \cos \theta & =0 \\
\sin \theta=0 \Rightarrow \theta & =\pi \Rightarrow(1,0)
\end{align}
$$

There are no solutions to $\cos \theta=0$ in the range $\frac{\pi}{2}<\theta<\frac{3 \pi}{2}$.

∴ The point where the tangent is parallel to the $y$-axis is $(1,0)$.

<a id="ch04-ex4G"></a>
### EXERCISE 4G

<a id="ch04-ex4G-q1"></a>
##### Question 1
For each of the following parametric equations, find $\frac{\mathrm{d} y}{\mathrm{~d} x}$ in terms of the given parameter.

**a** $x=2 t^{3}, y=t^{2}-5$

c $x=2 \theta-\sin 2 \theta, y=2-\cos 2 \theta$

e $x=1+\tan \theta, y=\cos \theta$

g $x=1+2 \sin ^{2} \theta, y=4 \tan \theta$

**i** $x=\mathrm{e}^{2 t}, y=t^{3} \mathrm{e}^{t}+1$

k $x=\ln (1-t), y=\frac{5}{t}$

**b** $x=2+\sin 2 \theta, y=4 \theta+2 \cos 2 \theta$

d $x=3 \tan \theta, y=2 \sin 2 \theta$

f $x=\cos 2 \theta-\cos \theta, y=\sin ^{2} \theta$

h $x=2+\mathrm{e}^{-t}, y=\mathrm{e}^{t}-\mathrm{e}^{-t}$

j $x=2 \ln (t+3), y=4 \mathrm{e}^{t}$

l $x=1+\sqrt{t}, y=2 \ln t$

<a id="ch04-ex4G-q2"></a>
##### Question 2
The parametric equations of a curve are $x=3 t, y=t^{3}+4 t^{2}-3 t$. Find the two values of $t$ for which the curve has gradient 0.

<a id="ch04-ex4G-q3"></a>
##### Question 3
The parametric equations of a curve are $x=2 \sin \theta, y=1-3 \cos 2 \theta$. Find the exact gradient of the curve at the point where $\theta=\frac{\pi}{3}$.

<a id="ch04-ex4G-q4"></a>
##### Question 4
The parametric equations of a curve are $x=2+\ln (t-1), y=t+\frac{4}{t}$ for $t>1$. Find the coordinates of the only point on the curve at which the gradient is equal to 0 .

<a id="ch04-ex4G-q5"></a>
##### Question 5
The parametric equations of a curve are $x=\mathrm{e}^{2 t}, y=1+2 t \mathrm{e}^{t}$. Find the equation of the normal to the curve at the point where $t=0$.

<a id="ch04-ex4G-q6"></a>
##### Question 6
The parametric equations of a curve are $x=\mathrm{e}^{2 t}, y=t^{2} \mathrm{e}^{-t}-1$.

**a** Show that $\frac{\mathrm{d} y}{\mathrm{~d} x}=\frac{t(2-t)}{2 \mathrm{e}^{3 t}}$.

**b** Show that the tangent to the curve at the point $(1,-1)$ is parallel to the $x$-axis and find the exact coordinates of the other point on the curve at which the tangent is parallel to the $x$-axis.

<a id="ch04-ex4G-q7"></a>
##### Question 7
A curve is defined by the parametric equations $x=\tan \theta, y=2 \sin 2 \theta$, for $0<\theta<\frac{\pi}{2}$.

**a** Show that $\frac{\mathrm{d} y}{\mathrm{~d} x}=4 \cos ^{2} \theta\left(2 \cos ^{2} \theta-1\right)$.

**b** Hence, find the coordinates of the stationary point.

<a id="ch04-ex4G-q8"></a>
##### Question 8
The parametric equations of a curve are $x=t+4 \ln t, \quad y=t+\frac{9}{t}$, for $t>0$.

**a** Show that $\frac{\mathrm{d} y}{\mathrm{~d} x}=\frac{t^{2}-9}{t^{2}+4 t}$.

**b** The curve has one stationary point. Find the $y$-coordinate of this point and determine whether it is a maximum or a minimum point.

<a id="ch04-ex4G-q9"></a>
##### Question 9
The parametric equations of a curve are $x=1+2 \sin ^{2} \theta, y=1+2 \tan \theta$. Find the equation of the normal to the curve at the point where $\theta=\frac{\pi}{4}$.

<a id="ch04-ex4G-q10"></a>
##### Question 10
The parametric equations of a curve are $x=2 \sin \theta+\cos 2 \theta, \quad y=1+\cos 2 \theta$, for $0 \leqslant \theta \leqslant \frac{\pi}{2}$.

**a** Show that $\frac{\mathrm{d} y}{\mathrm{~d} x}=\frac{2 \sin \theta}{2 \sin \theta-1}$.

**b** Find the coordinates of the point on the curve where the tangent is parallel to the $x$-axis.

**c** Show that the tangent to the curve at the point $\left(\frac{3}{2}, \frac{3}{2}\right)$ is parallel to the $y$-axis.

<a id="ch04-ex4G-q11"></a>
##### Question 11
The parametric equations of a curve are $x=\ln (\tan t), y=2 \sin 2 t$, for $0<t<\frac{\pi}{2}$.

**a** Show that $\frac{\mathrm{d} y}{\mathrm{~d} x}=\sin 4 t$.

**b** Hence show that at the point where $x=0$ the tangent is parallel to the $x$-axis.

### Checklist of learning and understanding

Product rule

- $\frac{\mathrm{d}}{\mathrm{d} x}(u v)=u \frac{\mathrm{~d} v}{\mathrm{~d} x}+v \frac{\mathrm{~d} u}{\mathrm{~d} x}$

Quotient rule

- $\frac{\mathrm{d}}{\mathrm{d} x}\left(\frac{u}{v}\right)=\frac{v \frac{\mathrm{~d} u}{\mathrm{~d} x}-u \frac{\mathrm{~d} v}{\mathrm{~d} x}}{v^{2}}$

Exponential functions

- $\frac{\mathrm{d}}{\mathrm{d} x}\left(\mathrm{e}^{x}\right)=\mathrm{e}^{x} \quad \frac{\mathrm{~d}}{\mathrm{~d} x}\left[\mathrm{e}^{a x+b}\right]=a \mathrm{e}^{a x+b} \quad \frac{\mathrm{~d}}{\mathrm{~d} x}\left[\mathrm{e}^{\mathrm{f}(x)}\right]=\mathrm{f}^{\prime}(x) \times \mathrm{e}^{\mathrm{f}(x)}$

Logarithmic functions

- $\frac{\mathrm{d}}{\mathrm{d} x}(\ln x)=\frac{1}{x} \quad \frac{\mathrm{~d}}{\mathrm{~d} x}[\ln (a x+b)]=\frac{a}{a x+b} \quad \frac{\mathrm{~d}}{\mathrm{~d} x}[\ln (\mathrm{f}(x))]=\frac{\mathrm{f}^{\prime}(x)}{\mathrm{f}(x)}$

Trigonometric functions

- $\left.\frac{\mathrm{d}}{\mathrm{d} x}(\sin x)=\cos x \mathrm{~d} x \mathrm{~s}(a x+b)\right]=a \cos (a x+b)$

- $\frac{\mathrm{d}}{\mathrm{d} x}(\cos x)=-\sin x \quad \frac{\mathrm{~d}}{\mathrm{~d} x}[\cos (a x+b)]=-a \sin (a x+b)$

- $\left.\frac{\mathrm{d}}{\mathrm{d} x}(\tan x)=\sec ^{2} x \mathrm{~d} x \mathrm{tan}(a x+b)\right]=a \sec ^{2}(a x+b)$

<a id="ch04-review"></a>
### END-OF-CHAPTER REVIEW EXERCISE 4

<a id="ch04-review-q1"></a>
##### Question 1
The parametric equations of a curve are

$$
x=1+\ln (t-2), y=t+\frac{9}{t}, \text { for } t>2 .
$$

**i** Show that $\frac{\mathrm{d} y}{\mathrm{~d} x}=\frac{\left(t^{2}-9\right)(t-2)}{t^{2}}$. `[3]`

**ii** Find the coordinates of the only point on the curve at which the gradient is equal to 0. `[3]`

*Cambridge International AS \& A Level Mathematics 9709 Paper 21 Q4 November 2010*

<a id="ch04-review-q2"></a>
##### Question 2
Find the value of $\frac{\mathrm{d} y}{\mathrm{~d} x}$ when $x=4$ in each of the following cases:

**i** $y=x \ln (x-3)$, `[4]`

**ii** $y=\frac{x-1}{x+1}$. `[3]`

*Cambridge International AS \& A Level Mathematics 9709 Paper 21 Q5 June 2011*

<a id="ch04-review-q3"></a>
##### Question 3
The parametric equations of a curve are $x=\mathrm{e}^{3 t}, y=t^{2} \mathrm{e}^{t}+3$.

**i** Show that $\frac{\mathrm{d} y}{\mathrm{~d} x}=\frac{t(t+2)}{3 \mathrm{e}^{2 t}}$. `[4]`

**ii** Show that the tangent to the curve at the point $(1,3)$ is parallel to the $x$-axis. `[2]`

**iii** Find the exact coordinates of the other point on the curve at which the tangent is parallel to the $x$-axis. `[2]`

*Cambridge International AS \& A Level Mathematics 9709 Paper 21 Q7 November 2011*

<a id="ch04-review-q4"></a>
##### Question 4
Find the gradient of each of the following curves at the point for which $x=0$.

**i** $y=3 \sin x+\tan 2 x$ `[3]`

**ii** $y=\frac{6}{1+\mathrm{e}^{2 x}}$ `[3]`

*Cambridge International AS \& A Level Mathematics 9709 Paper 21 Q2 June 2014*

<a id="ch04-review-q5"></a>
##### Question 5
The equation of a curve is $2 x^{2}+3 x y+y^{2}=3$.

**i** Find the equation of the tangent to the curve at the point (2, -1), giving your answer in the form $a x+b y+c=0$, where $a, b$ and $c$ are integers. `[6]`

**ii** Show that the curve has no stationary points. `[4]`

*Cambridge International AS \& A Level Mathematics 9709 Paper 21 Q7 June 2014*

<a id="ch04-review-q6"></a>
##### Question 6
The equation of a curve is $y^{3}+4 x y=16$.

**i** Show that $\frac{\mathrm{d} y}{\mathrm{~d} x}=-\frac{4 y}{3 y^{2}+4 x}$. `[4]`

**ii** Show that the curve has no stationary points. `[2]`

**iii** Find the coordinates of the point on the curve where the tangent is parallel to the $y$-axis. `[4]`

*Cambridge International AS \& A Level Mathematics 9709 Paper 21 Q7 June 2015*

<a id="ch04-review-q7"></a>
##### Question 7
The equation of a curve is $y=6 \sin x-2 \cos 2 x$.

Find the equation of the tangent to the curve at the point $\left(\frac{1}{6} \pi, 2\right)$. Give the answer in the form $y=m x+c$, where the values of $m$ and $c$ are correct to 3 significant figures. `[5]`

*Cambridge International AS \& A Level Mathematics 9709 Paper 21 Q3 June 2015*

<a id="ch04-review-q8"></a>
##### Question 8
![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-109_416_532_390_861.jpg) The parametric equations of a curve are $x=6 \sin ^{2} t, y=2 \sin 2 t+3 \cos 2 t$, for $0 \leqslant t<\pi$. The curve crosses the $x$-axis at the points $B$ and $D$ and the stationary points are $A$ and $C$, as shown in the diagram.

**i** Show that $\frac{\mathrm{d} y}{\mathrm{~d} x}=\frac{2}{3} \cot 2 t-1$. `[5]`

**ii** Find the values of $t$ at $A$ and $C$, giving each answer correct to 3 decimal places. `[3]`

**iii** Find the value of the gradient of the curve at $B$. `[3]`

##

*Cambridge International AS \& A Level Mathematics 9709 Paper 21 Q7 November 2015*

<a id="ch04-review-q9"></a>
##### Question 9
The equation of a curve is $3 x^{2}+4 x y+y^{2}=24$. Find the equation of the normal to the curve at the point (1, 3), giving your answer in the form $a x+b y+c=0$ where $a, b$ and $c$ are integers. `[8]`

##

*Cambridge International AS \& A Level Mathematics 9709 Paper 21 Q6 November 2016*

<a id="ch04-review-q10"></a>
##### Question 10
![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-109_436_633_1481_810.jpg) The diagram shows the curve $y=\sqrt{\left(\frac{1-x}{1+x}\right)}$.

**i** By first differentiating $\frac{1-x}{1+x}$, obtain an expression for $\frac{\mathrm{d} y}{\mathrm{~d} x}$ in terms of $x$. Hence show that the gradient of the normal to the curve at the point $(x, y)$ is $(1+x) \sqrt{\left(1-x^{2}\right)}$. `[5]`

**ii** The gradient of the normal to the curve has its maximum value at the point $P$ shown in the diagram. Find, by differentiation, the $x$-coordinate of $P$. `[4]`

<a id="ch04-review-q11"></a>
##### Question 11
The parametric equations of a curve are $x=3\left(1+\sin ^{2} t\right), y=2 \cos ^{3} t$.

Find $\frac{\mathrm{d} y}{\mathrm{~d} x}$ in terms of $t$, simplifying your answer as far as possible. `[5]`

*Cambridge International A Level Mathematics 9709 Paper 31 Q2 November 2011*

<a id="ch04-review-q12"></a>
##### Question 12
The equation of a curve is $\ln (x y)-y^{3}=1$.

**i** Show that $\frac{\mathrm{d} y}{\mathrm{~d} x}=\frac{y}{x\left(3 y^{3}-1\right)}$. `[4]`

**ii** Find the coordinates of the point where the tangent to the curve is parallel to the $y$-axis, giving each coordinate correct to 3 significant figures. `[4]`

*Cambridge International A Level Mathematics 9709 Paper 31 Q7 November 2012*

<a id="ch04-review-q13"></a>
##### Question 13
The curve with equation $6 \mathrm{e}^{2 x}+k \mathrm{e}^{y}+\mathrm{e}^{2 y}=c$, where $k$ and $c$ are constants, passes through the point $P$ with coordinates $(\ln 3, \ln 2)$.

**i** Show that $58+2 k=c$. `[2]`

**ii** Given also that the gradient of the curve at $P$ is -6, find the values of $k$ and $c$. `[5]`

*Cambridge International A Level Mathematics 9709 Paper 31 Q5 June 2011*

![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-111_2770_1944_3_136.jpg)
