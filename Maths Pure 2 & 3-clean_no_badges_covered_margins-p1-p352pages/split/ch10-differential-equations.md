# Chapter 10: Differential equations
<a id="ch10-prerequisite"></a>
### PREREQUISITE KNOWLEDGE

| Where it comes from | What you should be able to do | Check your skills |
| :--- | :--- | :--- |
| IGCSE / O Level Mathematics | Express direct and inverse variation in algebraic terms and use this form of expression to find unknown quantities. | 1 The weight, $w$ newtons, of a sphere is directly proportional to the cube of its radius, $r \mathrm{~cm}$. When the radius of the sphere is 60 cm, its weight is 4320 newtons. Find an equation connecting $w$ and $r$. |
| IGCSE / O Level Mathematics | Understand and apply<br>- laws of indices<br>- laws of logarithms<br> | $2 \ln y-\ln (20-y)=\frac{x}{4}+\ln 3$ Find and simplify an expression for $y$ in terms of $x$.<br> |
| Chapter 5 | Integrate<br>- standard functions<br>- using substitution<br>- using parts<br> | 3 Find:<br>a $\int \frac{1}{3 x-1} \mathrm{~d} x$<br>b $\int \frac{\sin x}{\cos x} \mathrm{~d} x$<br>c $\int x \mathrm{e}^{-x} \mathrm{~d} x$.<br> |
| Chapter 8 | Decompose a compound fraction with denominator<br>- $(a x+b)(c x+d)(e x+f)$<br>- $(a x+b)(c x+d)^{2}$<br>- $(a x+b)\left(c x^{2}+d\right)$<br> <br> into its partial fractions and integrate the result. | 4 Find $\int \frac{2}{(x-2)(3 x+1)} \mathrm{d} x$. |
| Chapter 1 | Sketch graphs of standard functions e.g. involving $\ln \mathrm{f}(x)$ and $\mathrm{e}^{\mathrm{f}(x)}$ (including understanding end behaviour as $x \rightarrow \pm \infty$ ). | 5 a Sketch the graph of $y=\mathrm{e}^{x^{2}}$.<br>&#160;&#160;b $\frac{12 \mathrm{e}^{x}}{3+\mathrm{e}^{x}} \rightarrow k$ as $x \rightarrow \infty$. Find the value of the constant $k$.<br> |

### What is a differential equation?

An equation that has a derivative such as $\frac{\mathrm{d} y}{\mathrm{~d} x}$ or $\frac{\mathrm{d}^{2} y}{\mathrm{~d} x^{2}}$ as one of its terms is called a differential equation. When the equation has the first derivative $\frac{\mathrm{d} y}{\mathrm{~d} x}$ as one of its terms, it is called a first order differential equation. For example, the equation $\frac{\mathrm{d} y}{\mathrm{~d} x}=3 x^{2}$ is an alternative way of representing the relationship $y=x^{3}+C$, where $C$ is a constant.

To solve a differential equation, we integrate to find the direct relationship between $x$ and $y$, such as $y=x^{3}+C$. The direct equation $y=x^{3}+C$ is called the general solution of the differential equation $\frac{\mathrm{d} y}{\mathrm{~d} x}=3 x^{2}$. To find a particular solution, we must have further information that will enable us to find the value of $C$.

The solution of an algebraic equation is a number or set of numbers. The solution of a differential equation is a function.

In this chapter, we will learn the initial skills needed to master the solution of one type of first order differential equations. These simple skills will be the foundation for further study of this subject.

You might wonder about the usefulness of such seemingly abstract equations in the real world. In fact, differential equations are excellent mathematical models for many real-life situations and are essential to solve many problems. First order differential equations can model rates of change, in other words, the rate at which one quantity is increasing or decreasing with respect to another quantity. There are many examples in the physical world that can be modelled using such relationships. A few examples are the rate of increase of the number of bacteria in a culture, simple kinematics problems, the rate of decrease of the value of a car and the rate at which a hot liquid cools.

## 10.1 The technique of separating the variables

Solving a differential equation such as $\frac{\mathrm{d} y}{\mathrm{~d} x}=6(x+1)^{2}$ can be done using an anti-differentiation approach.

We know, from the Pure Mathematics 1 Coursebook, Chapter 9, that if we integrate both sides with respect to $x$, we have:

$$
\begin{align}
& \int \frac{\mathrm{d} y}{\mathrm{~d} x} \mathrm{~d} x=\int 6(x+1)^{2} \mathrm{~d} x \\
& y=\frac{6(x+1)^{3}}{3}+C \\
& y=2(x+1)^{3}+C
\end{align}
$$

Notice that the first line on the left-hand side is $\int \frac{\mathrm{d} y}{\mathrm{~d} x} \mathrm{~d} x=\int 6(x+1)^{2} \mathrm{~d} x$ and from anti-differentiation we can see that, if we integrate $\frac{\mathrm{d} y}{\mathrm{~d} x}$ with respect to $x$ we obtain an expression for $y$.

This means that $\int \frac{\mathrm{d} y}{\mathrm{~d} x} \mathrm{~d} x=$ is equivalent to $\int \mathrm{d} y=$, which is $y=$ This result is generally true.

<a id="ch10-kp-10.1"></a>
#### KEY POINT 10.1

Integrating an expression of the form $\mathrm{f}(y) \frac{\mathrm{d} y}{\mathrm{~d} x}$ with respect to $x$ is equivalent to integrating $\mathrm{f}(y)$ with respect to $y$.

Therefore $\int \mathrm{f}(y) \frac{\mathrm{d} y}{\mathrm{~d} x} \mathrm{~d} x$ is equivalent to $\int \mathrm{f}(y) \mathrm{d} y$.

The differential equation $\frac{\mathrm{d} y}{\mathrm{~d} x}=6(x+1)^{2}$ is easy to solve because $\frac{\mathrm{d} y}{\mathrm{~d} x}$ is equal to a function that we know how to integrate. This is not always the case.

How do we solve the differential equation $\frac{\mathrm{d} y}{\mathrm{~d} x}=x y$ when $y>0$ ?

As it is written, we cannot integrate both sides with respect to $x$ and find a solution.

Separating the variables in the expression $x y$ means that we are then able to integrate.

$$
\begin{align}
\frac{\mathrm{d} y}{\mathrm{~d} x} & =x y & & \text { Separate the variables } x \text { and } y . \\
\frac{1}{y} \frac{\mathrm{~d} y}{\mathrm{~d} x} & =x & & \text { Form integrals of both sides with respect to } x . \\
\int \frac{1}{y} \frac{\mathrm{~d} y}{\mathrm{~d} x} \mathrm{~d} x & =\int x \mathrm{~d} x & & \text { Integrate each side. } \\
\int \frac{1}{y} \mathrm{~d} y & =\int x \mathrm{~d} x & & \begin{array}{l} \text { The modulus of } y \text { is not required as } \\
\text { we know that } y>0 . \end{array} \\
\ln y+A & =\frac{x^{2}}{2}+B & & \begin{array}{l} \text { The constants of integration can be combined } \\
\text { as one term and we only need to write a } \\
\text { constant on one side. } \end{array} \\
y & =\mathrm{e}^{\frac{x^{2}}{2}+C} & & \begin{array}{l} \text { This is the general solution of the differential } \\
\text { equation as we do not know the value of the } \\
\text { arbitrary constant } C . \end{array}
\end{align}
$$

When we have further information, we can find the particular solution of the differential solution given by that information.

For example, solve $\frac{\mathrm{d} y}{\mathrm{~d} x}=x y$ given that $y=2$ when $x=0$.

Using this information:

$$
\begin{align}
& \ln y=\frac{x^{2}}{2}+C \text { and so } \ln 2=\frac{0^{2}}{2}+C, C=\ln 2 \\
& y=\mathrm{e}^{\frac{x^{2}}{2}+\ln 2} \\
& y=\mathrm{e}^{\frac{x^{2}}{2}} \times \mathrm{e}^{\ln 2} \quad \begin{array}{l} \text { This is the particular solution of the differential } \\
\text { equation. } \end{array} \\
& y=2 \mathrm{e}^{\frac{x^{2}}{2}} \quad \begin{array}{l} \text { Note that you often need to write your answer as } \\
\text { an expression for } y \text { in terms of } x . \text { This commonly } \\
\text { means using laws of indices or logarithms. } \end{array}
\end{align}
$$

By separating the variables we are rearranging the differential equation to the form

$$
\mathrm{f}(y) \frac{\mathrm{d} y}{\mathrm{~d} x}=\mathrm{g}(x) .
$$

$$
\begin{align}
\mathrm{f}(y) \frac{\mathrm{d} y}{\mathrm{~d} x} & =\mathrm{g}(x) & & \text { (Note: Other variables may be used such as } v \\
\int \mathrm{f}(y) \frac{\mathrm{d} y}{\mathrm{~d} x} \mathrm{~d} x & =\int \mathrm{g}(x) \mathrm{d} x & & \text { and } t .) \\
\int \mathrm{f}(y) \mathrm{d} y & =\int \mathrm{g}(x) \mathrm{d} x & &
\end{align}
$$

So, in the case where the derivative is $\frac{\mathrm{d} y}{\mathrm{~d} x}$ :

- form an expression in $x$ only on one side of the equation

- form an expression in $y \times \frac{\mathrm{d} y}{\mathrm{~d} x}$ on the other side of the equation.

This gives us a form of the equation that can be integrated on both sides, one side with respect to $x$ and the other side with respect to $y$.

<a id="ch10-we-10.1"></a>
#### WORKED EXAMPLE 10.1

The variables $x$ and $y$ satisfy the differential equation $\frac{\mathrm{d} y}{\mathrm{~d} x}=\frac{1+x}{2 y}$.

It is given that $y=3$ when $x=0$.

Solve the differential equation and obtain an expression for $y$ in terms of $x$.

Answer

Even though the question does not ask for it directly, you are expected to use the initial condition that you have been given to find a particular solution.

$$
\frac{\mathrm{d} y}{\mathrm{~d} x}=\frac{1+x}{2 y}
$$

Separate the variables $x$ and $y$.

Here we have moved the $2 y$. It was not essential to move the 2 , we could have moved the $y$ only. This would be just as valid as it would also give expressions that can be integrated.

$$
2 y \frac{\mathrm{~d} y}{\mathrm{~d} x}=1+x
$$

Form integrals of both sides with respect to $x$.

$$
\begin{align}
\int 2 y \frac{\mathrm{~d} y}{\mathrm{~d} x} \mathrm{~d} x & =\int(1+x) \mathrm{d} x \\
\int 2 y \mathrm{~d} y & =\int(1+x) \mathrm{d} x
\end{align}
$$

Integrate each side.

$$
y^{2}=x+\frac{x^{2}}{2}+C
$$

$$
y=3 \text { when } x=0 .
$$

$$
\begin{align}
9 & =0+\frac{0^{2}}{2}+C, \quad C=9 \\
y^{2} & =x+\frac{x^{2}}{2}+9 \\
y & =\left(x+\frac{x^{2}}{2}+9\right)^{\frac{1}{2}}
\end{align}
$$

You can check this by differentiating.

<a id="ch10-we-10.2"></a>
#### WORKED EXAMPLE 10.2

Find the general solution of the differential equation $\left(x^{2}+1\right) y^{3}+x^{2} \frac{\mathrm{~d} y}{\mathrm{~d} x}=0$.

Answer

$$
\begin{align}
& \left(x^{2}+1\right) y^{3}+x^{2} \frac{\mathrm{~d} y}{\mathrm{~d} x}=0 \\
& x^{2} \frac{\mathrm{~d} y}{\mathrm{~d} x}=-\left(x^{2}+1\right) y^{3} \\
& \frac{1}{y^{3}} \frac{\mathrm{~d} y}{\mathrm{~d} x}=-\frac{\left(x^{2}+1\right)}{x^{2}} * * \\
& \int y^{-3} \frac{\mathrm{~d} y}{\mathrm{~d} x} \mathrm{~d} x=\int\left(-x^{-2}-1\right) \mathrm{d} x \\
& \int y^{-3} \mathrm{~d} y=\int\left(-x^{-2}-1\right) \mathrm{d} x \\
& -\frac{1}{2 y^{2}}=\frac{1}{x}-x+C
\end{align}
$$

Is this the complete solution?

Earlier in the solution (at line **) we assumed that $y \neq 0$. However, when $y=0$, the original differential equation becomes $\frac{\mathrm{d} y}{\mathrm{~d} x}=\frac{0}{x^{2}}=0$. Since $y=0$ is the $x$-axis, it is true that its gradient is 0 at all points and so $y=0$ is also a solution of the differential equation and must be included for the general solution to be complete.

The complete general solution is, therefore, $-\frac{1}{2 y^{2}}=\frac{1}{x}-x+C$ or $y=0$.

In Worked example 10.2, we saw that, when rearranging to the form $\mathrm{f}(y) \frac{\mathrm{d} y}{\mathrm{~d} x}=\mathrm{g}(x)$, there are cases where $\mathrm{f}(y)$ is a function such as, for example, $\frac{1}{y^{3}}$. In these cases, a value (or values) of $y$ must be excluded for the separation of the variables to take place.

As a final step, when finding the general solution in these cases, we must check if the value (or values) we have excluded when separating the variables gives (or give) a valid solution of the original differential equation. When they do, we should include them.

<a id="ch10-we-10.3"></a>
#### WORKED EXAMPLE 10.3

It is given that, for $0<x<300, \frac{\mathrm{~d} x}{\mathrm{~d} t}=\frac{x(300-x)}{600}$ and $x=50$ when $t=0$. Find the particular solution of the differential equation, giving your answer as an expression for $x$ in terms of $t$.

Answer

$$
\frac{\mathrm{d} x}{\mathrm{~d} t}=\frac{x(300-x)}{600}
$$

Separate the variables. The derivative is with respect to $t$ and so the expression in $x$ needs to be moved to the left-hand side.

$$
\begin{align}
\frac{1}{x(300-x)} \frac{\mathrm{d} x}{\mathrm{~d} t} & =\frac{1}{600} \\
\int \frac{1}{x(300-x)} \frac{\mathrm{d} x}{\mathrm{~d} t} \mathrm{~d} t & =\frac{1}{600} \int \mathrm{~d} t \\
\int \frac{1}{x(300-x)} \mathrm{d} x & =\frac{1}{600} \int \mathrm{~d} t \\
\frac{1}{300} \int\left(\frac{1}{x}+\frac{1}{300-x}\right) \mathrm{d} x & =\frac{1}{600} \int \mathrm{~d} t \\
\frac{1}{300}(\ln x-\ln (300-x)) & =\frac{1}{600} t+C \\
\ln x-\ln (300-x) & =\frac{1}{2} t+C \\
\ln \frac{x}{300-x} & =\frac{1}{2} t+C \\
C & =\ln \frac{50}{300-x} \\
\frac{x}{300-x} & =\frac{1}{2} t+\ln 0.2 \\
\frac{x}{300-x} & =\mathrm{e}^{\frac{1}{2} t+\ln 0.2} \times \mathrm{e}^{\ln 0.2} \\
x & =0.2 \mathrm{e}^{\frac{1}{2} t}(300-x) \\
x+0.2 \mathrm{e}^{\frac{1}{2} t} x & =60 \mathrm{e}^{\frac{1}{2} t} \\
x\left(1+0.2 \mathrm{e}^{\frac{1}{2} t}\right) & =60 \mathrm{e}^{\frac{1}{2} t} \\
x & =\frac{60 \mathrm{e}^{\frac{1}{2} t}}{1+0.2 \mathrm{e}^{\frac{1}{2} t}}
\end{align}
$$

Form integrals of both sides with respect to $t$.

Note that it is simpler to leave the 600 on the right-hand side here.

Write the expression on the left in terms of its partial fractions.

Integrate each side.

The modulus signs are not required as we know that $0<x<300$.

$$
x=50 \text { when } t=0 .
$$

<a id="ch10-ex10A"></a>
### EXERCISE 10A

<a id="ch10-ex10A-q1"></a>
##### Question 1
Find the general solution of each of the following differential equations.

**a** $\frac{\mathrm{dy}}{\mathrm{d} x}=x^{3}-6$

**b** $\frac{\mathrm{d} A}{\mathrm{~d} r}=2 \pi r$

**c** $s^{2} \frac{\mathrm{~d} s}{\mathrm{~d} t}=\cos (t+5)$

**d** $V^{-1} \frac{\mathrm{~d} V}{\mathrm{~d} t}=2$

**e** $\frac{\mathrm{d} y}{\mathrm{~d} x}=\frac{y+1}{x}$

**f** $x+\sec x \sin y \frac{\mathrm{~d} y}{\mathrm{~d} x}=1$

<a id="ch10-ex10A-q2"></a>
##### Question 2
Find the particular solution for each of the following differential equations, using the values given.

**a** $\cos ^{2} x \frac{\mathrm{~d} y}{\mathrm{~d} x}=y$ given $y=5$ when $x=0$

**b** $x y \frac{\mathrm{~d} y}{\mathrm{~d} x}=\frac{x^{3}-x}{1-\sqrt{y}}$ given $y=4$ when $x=3$

<a id="ch10-ex10A-q3"></a>
##### Question 3
Given that $\frac{\mathrm{d} y}{\mathrm{~d} x}=\mathrm{e}^{x-y}$ and $y=\ln 2$ when $x=0$, obtain an expression for $y$ in terms of $x$.

<a id="ch10-ex10A-q4"></a>
##### Question 4
The gradient of a curve at the point $(x, y)$ is $5 y^{3} x$.

**a** Write down the differential equation satisfied by $y$.

**b** Given that the curve passes through the point $(1,1)$, find $y^{2}$ as a function of $x$.

<a id="ch10-ex10A-q5"></a>
##### Question 5
**a** Express $\frac{1}{(2-x)(x+1)}$ in the form $\frac{A}{2-x}+\frac{B}{x+1}$.

**b** The variables $x$ and $t$ satisfy the differential equation

$$
\frac{\mathrm{d} x}{\mathrm{~d} t}=(2-x)(x+1) .
$$

It is given that $t=0$ when $x=0$.

**i** Solve this differential equation and obtain an expression for $x$ in terms of $t$.

**ii** State what happens to the value of $x$ when $t$ becomes large.

<a id="ch10-ex10A-q6"></a>
##### Question 6
The variables $w$ and $t$ satisfy the differential equation

$$
\frac{\mathrm{d} w}{\mathrm{~d} t}=0.001(100-w)^{2} .
$$

Given that when $t=0 w=0$, show that the solution to the differential equation can be written in the form $w=100-\frac{1000}{t+10}$.

<a id="ch10-ex10A-q7"></a>
##### Question 7
Solve the differential equation $4 \frac{\mathrm{~d} x}{\mathrm{~d} t}=\left(3 x^{2}-x\right) \cos t$ given that $x=0.4$ when $t=0$. Give your answer as an expression for $x$ in terms of $t$.

<a id="ch10-ex10A-q8"></a>
##### Question 8
Find the general solution of the differential equation $x y \frac{\mathrm{~d} y}{\mathrm{~d} x}=\frac{x^{2}-1}{\mathrm{e}^{y+1}}$.

<a id="ch10-ex10A-q9"></a>
##### Question 9
Find the equation of the curve that satisfies the equation $\frac{\mathrm{d} y}{\mathrm{~d} x}=\frac{1+y^{2}}{4+x^{2}}$ and passes through the point $(0,1)$. Give your answer in the form $y=\mathrm{f}(x)$.

<a id="ch10-ex10A-q10"></a>
##### Question 10
Find the general solution of the equation $x^{3} \frac{\mathrm{~d} y}{\mathrm{~d} x}+2 y=1$.

<a id="ch10-ex10A-q11"></a>
##### Question 11
Solve the differential equation $\frac{\mathrm{d} x}{\mathrm{~d} t}=4 x \cos ^{2} t$ given that $x=1$ when $t=0$. Give your answer as an expression for $x$ in terms of $t$.

<a id="ch10-ex10A-q12"></a>
##### Question 12
**a** Use the substitution $u=t^{2}$ to find $\int t e^{t^{2}} \mathrm{~d} t$.

**b** Solve the differential equation $\frac{\mathrm{d} x}{\mathrm{~d} t}=\frac{t\left(e^{t^{2}}+5\right)}{x^{2}}$ given that $x=1$ when $t=0$.

<a id="ch10-ex10A-q13"></a>
##### Question 13
At a point with coordinates $(x, y)$ the gradient of a particular curve is directly proportional to $x y^{2}$. At a particular point $P$ with coordinates $(1,3)$ it is known that the gradient of this curve is 6 .

Find and simplify an expression for $y$ in terms of $x$.

<a id="ch10-ex10A-q14"></a>
##### Question 14
The variables $x$ and $t$ satisfy the differential equation

$$
\left(3 x+2 x^{3}\right) \frac{\mathrm{d} x}{\mathrm{~d} t}=k\left(3 x^{2}+x^{4}\right)
$$

for $x>0$ where $k$ is a constant. When $t=0, x=1$ and when $t=0.5, x=2$.

Solve the differential equation, finding the exact value of $k$, and show that $7^{2 t}=\frac{3 x^{2}+x^{4}}{4}$.

<a id="ch10-ex10A-q15"></a>
##### Question 15
**a** Use the substitution $u=\ln x$ to find $\int \frac{1}{x \ln x} \mathrm{~d} x$.

**b** Given that $x>0, y>0$, find the general solution of the differential equation $\ln x \frac{\mathrm{~d} y}{\mathrm{~d} x}=\frac{y}{x}$.

<a id="ch10-ex10A-q16"></a>
##### Question 16
A type of medicine that reacts to strong light can be used to treat some skin problems.

It is important that, after treatment with this type of medicine, the person stays out of bright light until the amount of medicine remaining in the skin is at a safe level.

Jonty is treated with a medicine of this type.

After the treatment, 65 mg remains in the treated area of skin.

The rate at which the medicine disappears from the treated area of Jonty's skin is modelled by the differential equation $\frac{\mathrm{d} m}{\mathrm{~d} t}=-0.05 m$, where $m$ is the amount of medicine, in milligrams, in the skin $t$ hours after the treatment.

Jonty is safe to go out in bright light when no more than 6 mg of the medicine remains in his skin.

How long must Jonty wait before he goes out in bright light?

#### EXPLORE 10.1

Newton's law of cooling or heating

Many differential equations arise from modelling natural laws and relationships. One example is Newton's law of cooling or heating:

The rate of change of temperature of an object is proportional to the difference in temperature of the object and its surroundings.

We define

$T$ as the temperature of the object

$t \quad$ as time

$T_{0}$ as the temperature of the object when $t=0$

$s$ as the constant temperature of the surroundings

$k$ as the constant of proportionality.

Discuss the following.

- Why it is necessary to define the variables and constants.

- Why the differential equation $\frac{\mathrm{d} T}{\mathrm{~d} t}=k(T-s), k>0$ is satisfied by $T$.

- Other possible correct ways to represent Newton's law of cooling or heating as a differential equation with this set of defined variables and constants.

- Why the general solution of the given form of the differential equation may be written as:

$$
|T-s|=A \mathrm{e}^{k t} \text { where } A=\mathrm{e}^{C} .
$$

- How many arbitrary constants there are in the general solution of any first order differential equation.

- Why the modulus in the general solution is required.

- How the general solution can be used to represent the temperature of an object cooling down or warming up.

## 10.2 Forming a differential equation from a problem

The key to forming a differential equation from a problem is the successful interpretation of the language used in the question.

For example, when you are given a problem such as:

The rate of increase of the number of bacteria in a dish is $k$ times the number of bacteria in the dish. The number of bacteria present in the dish at time $t$ is $x$...

Replacing the words the number of bacteria in a dish by $x$ the problem becomes:

> The rate of increase of $x$ is $k$ times $x$.

This rate of increase of $x$ is with respect to time, $t$, and is much easier to translate into a differential equation: $\frac{\mathrm{d} x}{\mathrm{~d} t}=k x$.

<a id="ch10-we-10.4"></a>
#### WORKED EXAMPLE 10.4

Velocity is defined to be the rate of change of displacement with respect to time.

The velocity of a particle at time $t$ seconds is inversely proportional to its displacement, $s$ metres, from an origin, $O$.

**a** Form a differential equation to represent this data.

**b** Initially, the particle has a displacement of 2 metres from $O$.

After 1 second, the particle has a displacement of 5 metres from $O$.

Solve the differential equation giving your answer in the form $t=\mathrm{f}(s)$.

**c** Find $t$ when the displacement of the particle from $O$ is 10 metres.

Answer

**a** The velocity of a particle at time $t$ seconds is inversely proportional to its displacement, $s$ metres, from the origin, $O$.

$$
v=\frac{\mathrm{d} s}{\mathrm{~d} t} \text { and so } \frac{\mathrm{d} s}{\mathrm{~d} t} \propto \frac{1}{s} \text {, which means that } \frac{\mathrm{d} s}{\mathrm{~d} t}=\frac{k}{s} \qquad \text { At the moment, you do not have enough }
$$

information to find the constant of proportionality, $k$

**b** $\frac{\mathrm{d} s}{\mathrm{~d} t}=\frac{k}{s}$. Separate the variables $s$ and $t$.

$s \frac{\mathrm{~d} s}{\mathrm{~d} t}=k \qquad _{~}$ Form integrals of both sides with respect to $t$.

$$
\begin{align}
& \int s \frac{\mathrm{~d} s}{\mathrm{~d} t} \mathrm{~d} t=\int k \mathrm{~d} t \\
& \int s \mathrm{~d} s=\int k \mathrm{~d} t \\
& \frac{s^{2}}{2}=k t+C \\
& C=2, \frac{s^{2}}{2}-k t+2 \\
& \frac{5^{2}}{2}=k+2, \quad k=10.5 \\
& \frac{s^{2}}{2}=\frac{21}{2} t+2 \\
& t=\frac{s^{2}-4}{21}
\end{align}
$$

**c** Find $t$ when $s=10$

$$
t=\frac{100-4}{21}=4.5714 \qquad =4.57 \text { seconds correct to } 3 \text { significant figures. }
$$

<a id="ch10-we-10.5"></a>
#### WORKED EXAMPLE 10.5

The population density, $P$, of a town can be modelled as a continuous variable.

In the year when records began:

- the population density, $P$, of the town was increasing at the rate of 0.5 people per hectare per year

- the population density of the town was 2 people per hectare.

It is suggested that, $t$ years after records began, the rate of increase of the population density is inversely proportional to the square of the population density.

**a** Form a differential equation to model this information.

**b** Solve the differential equation, giving your answer in the form $P=\mathrm{f}(t)$.

**c** The table shows the actual population density of the town, every 5 years for the first 20 years after records began.

| $\boldsymbol{t}$ | 5 | 10 | 15 | 20 |
| :--- | :--- | :--- | :--- | :--- |
| $P$ | 3.5 | 4 | 5.5 | 7 |

Comment on how good a fit the model is to the actual data in the longer term.

Answer

**a** The rate of increase of $P$ is inversely proportional to $P^{2}$ :

$$
\frac{\mathrm{d} P}{\mathrm{~d} t} \propto \frac{1}{P^{2}} \quad \frac{\mathrm{~d} P}{\mathrm{~d} t}=\frac{k}{P^{2}}
$$

When $t=0, \frac{\mathrm{~d} P}{\mathrm{~d} t}=0.5$ and $P=2$, therefore:

$$
\begin{array}{ll} \frac{\mathrm{d} P}{\mathrm{~d} t}=\frac{k}{P^{2}} & 0.5=\frac{k}{4}, k=2 \\
\frac{\mathrm{~d} P}{\mathrm{~d} t}=\frac{2}{P^{2}} & \end{array}
$$

**b** $\frac{\mathrm{d} P}{\mathrm{~d} t}=\frac{2}{P^{2}}$. Separate the variables $P$ and $t$.

$$
P^{2} \frac{\mathrm{~d} P}{\mathrm{~d} t}=2 \quad \text { Form integrals of both sides with respect to } t .
$$

$$
\begin{align}
& \int P^{2} \frac{\mathrm{~d} P}{\mathrm{~d} t} \mathrm{~d} t=\int 2 \mathrm{~d} t \\
& \int P^{2} \mathrm{~d} P=2 \int \mathrm{~d} t \\
& \qquad P \qquad \text { Integrate each side. } t=0, P=2
\end{align}
$$

$$
\begin{align}
\frac{P^{3}}{3} & =2 t+C \\
\frac{8}{3} & =C \\
\frac{P^{3}}{3} & =2 t+\frac{8}{3} \\
P^{3} & =6 t+8 \\
P & =\sqrt[3]{6 t+8}
\end{align}
$$

**c**

| $\boldsymbol{t}$ | 5 | 10 | 15 | 20 |
| :--- | :--- | :--- | :--- | :--- |
| $P$ | 3.5 | 4 | 5.5 | 7 |
| Model prediction (to 2 significant figures) | 3.4 | 4.1 | 4.6 | 5.0 |

In the longer term, the model is not a particularly good fit as the values it generates when time increases are under-estimates of the known data.

<a id="ch10-we-10.6"></a>
#### WORKED EXAMPLE 10.6

The value, $\$ V$, of a motorbike as it gets older can be modelled as a continuous variable.

A model is suggested to estimate the rate of decrease of the value of the motorbike. This model is that the value $V$ when the motorbike is $t$ months old decreases at a rate proportional to $V$.

**a** Write down a differential equation that is satisfied by $V$.

**b** The motorbike had a value of $\$ 10000$ when it was new.

Solve the differential equation, showing that $V=10000 \mathrm{e}^{-k t}$, where $k$ is a positive constant.

**c** After 3 years the motorbike has lost half of its value when new.

Find the value of the motorbike when it was 2 years old.

Answer

**a** The rate of decrease of $V$ is proportional to $V$.

$\frac{\mathrm{d} V}{\mathrm{~d} t} \propto V$ and so $\frac{\mathrm{d} V}{\mathrm{~d} t}=-k V$, where $k$ is a positive constant.

This describes exponential decay. The rate is decreasing and so the constant of proportionality is negative.

**b** $\quad \frac{\mathrm{d} V}{\mathrm{~d} t}=-k V$ Separate the variables $V$ and $t$.

$\frac{1}{V} \frac{\mathrm{~d} V}{\mathrm{~d} t}=-k$

Form integrals of both sides with respect to $t$.

$\int \frac{1}{V} \frac{\mathrm{~d} V}{\mathrm{~d} t} \mathrm{~d} t=\int-k \mathrm{~d} t$ $\int \frac{1}{V} \mathrm{~d} V=\int-k \mathrm{~d} t$ Integrate each side.

$\ln |V|=-k t+C$

$t=0, V=10000$

$\ln 10000=C$

For this particular solution, $V$ is positive and so the modulus is not required.

$\ln V=-k t+\ln 10000$

Write in the form $V=\mathrm{f}(t)$.

$V=\mathrm{e}^{-k t+\ln 10000}$

$V=\mathrm{e}^{-k t} \times \mathrm{e}^{\ln 10000}$

$V=10000 \mathrm{e}^{-k t}$

**c** $V=10000 \mathrm{e}^{-k t}$

$t=3, V=5000$

$5000=10000 \mathrm{e}^{-3 k}$

$\frac{5000}{10000}=\mathrm{e}^{-3 k}$

$\ln 0.5=-3 k$

$k=\frac{-\ln 0.5}{3}$

$V=10000 \mathrm{e}^{-2\left(\frac{-\ln 0.5}{3}\right)}$

$V=\$ 6299.605 \qquad =\$ 6300$

correct to 3 significant figures

<a id="ch10-ex10B"></a>
### EXERCISE 10B

<a id="ch10-ex10B-q1"></a>
##### Question 1
Write the following as differential equations. Do not solve the equations.

**a** For height $h$ and time $t$ :

The rate of decrease of the height of water in a tank is proportional to the square of the height.

**b** For number of infected cells $n$ and time $t$ :

The rate of increase of the number of infected cells in a body is proportional to the number of infected cells in the body at that time.

**c** For velocity $v$ and time $t$ :

The rate of decrease of the velocity of a particle moving in a fluid is proportional to the product of $v$ and $v+1$.

**d** For volume $V$ and time $t$ :

The rate at which oil is leaking from an engine is proportional to the volume of oil in the engine at that time.

**e** For cost $C$ and time $t$ :The rate at which the cost of an item increases is proportional to the cube of the cost at that time.

**f** For speed $v$ and time $t$ :

The rate of change of the speed of a skydiver just after he jumps out of a plane is inversely proportional to $\mathrm{e}^{\frac{t}{2}}$.

<a id="ch10-ex10B-q2"></a>
##### Question 2
A large tank is full of water. The tank starts to leak.

$t$ seconds after the tank starts to leak the depth of water in the tank is $x$ metres.

The rate of decrease of the depth of water is proportional to the square root of the depth of water.

**a** Write down a differential equation relating $x, t$ and a constant of proportionality.

**b** At the instant when water starts to leak from the tank, the depth of water is 6.25 metres. Given that 120 seconds after the tank starts to leak, the depth of water is 4 metres, solve the differential equation, expressing $t$ in terms of $x$.

**c** Find the time it takes for the depth of the water to halve.

<a id="ch10-ex10B-q3"></a>
##### Question 3
The cost of designing an aircraft, $\$ A$ per kilogram, at time $t$ years after 1950 can be modelled as a continuous variable. The rate of increase of $A$ is directly proportional to $A$.

**a** Write down a differential equation that is satisfied by $A$.

**b** In 1950, the cost of designing an aircraft was \$12 per kilogram. Show that $A=12 \mathrm{e}^{k t}$, where $k$ is a positive constant.

**c** After 25 years, the cost of designing an aircraft was \$48 per kilogram. Find the cost of designing an aircraft after 60 years.

<a id="ch10-ex10B-q4"></a>
##### Question 4
A liquid is heated so that its temperature is $x^{\circ} \mathrm{C}$ after $t$ seconds. It is given that the rate of increase of $x$ is proportional to $(100-x)$. The initial temperature of the liquid is 25°C.

**a** Form a differential equation relating $x, t$ and a constant of proportionality, $k$, to model this information.

**b** Solve the differential equation and obtain an expression for $x$ in terms of $t$ and $k$.

**c** After 180 seconds the temperature of the liquid is 85°C. Find the temperature of the liquid after 195 seconds.

**d** The model predicts that $x$ cannot exceed a certain temperature. Write down this maximum temperature.

<a id="ch10-ex10B-q5"></a>
##### Question 5
The diagram shows an inverted cone filled with liquid paint.

An artist cuts a small hole in the bottom of the cone and the liquid paint drips out at a rate of $16 \mathrm{~cm}^{3}$ per second. At time $t$ seconds after the hole is cut, the paint in the cone is an inverted cone of depth $h \mathrm{~cm}$.

**a** Show that $\frac{\mathrm{d} V}{\mathrm{~d} h}=\frac{4}{9} \pi h^{2}$.

**b** Hence find an expression for $\frac{\mathrm{d} h}{\mathrm{~d} t}$.

**c** Solve the differential equation in part b, giving $t$ in terms of $h$.

**d** Find the length of time it takes for the depth of the paint to fall to 7.5 cm.

<a id="ch10-ex10B-q6"></a>
##### Question 6
The size of a population, $P$, at time $t$ minutes is to be modelled as a continuous variable such that the rate of increase of $P$ is directly proportional to $P$.

**a** Write down a differential equation that is satisfied by $P$.

**b** The initial size of the population is $P_{0}$.

Show that $P=P_{0} \mathrm{e}^{k t}$, where $k$ is a positive constant.

**c** The size of the population is $1.5 P_{0}$ after 2 minutes.

Find when the population will be $3 P_{0}$.

<a id="ch10-ex10B-q7"></a>
##### Question 7
A ball in the shape of a sphere is being filled with air. After $t$ seconds, the radius of the ball is $r \mathrm{~cm}$. The rate of increase of the radius is inversely proportional to the square root of its radius. It is known that when $t=4$ the radius is increasing at the rate of $1.4 \mathrm{~cm} \mathrm{~s}^{-1}$ and $r=7.84$.

**a** Form a differential equation relating $r$ and $t$ to model this information.

**b** Solve the differential equation and obtain an expression for $r$ in terms of $t$.

**c** How much air was in the ball at the start?

<a id="ch10-ex10B-q8"></a>
##### Question 8
Maria makes a large dish of curry on Monday, ready for her family to eat on Tuesday. She needs to put the dish of curry in the refrigerator but must let it cool to room temperature, 18°C, first. The temperature of the curry is $94^{\circ} \mathrm{C}$ when it has finished cooking.

At 6 pm, Maria places the hot dish in a sink full of cold water and keeps the water at a constant temperature of 7°C by running the cold tap and stirring the dish from time to time. After 10 minutes, the temperature of the curry is 54°C.

![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-257_333_569_839_1455.jpg)

It is given that the rate at which the curry cools down is proportional to the difference between the temperature of the curry and the temperature of the water in the sink.

At what time can Maria put her dish of curry in the refrigerator?

<a id="ch10-ex10B-q9"></a>
##### Question 9
The half-life of a radioactive isotope is the amount of time it takes for half of the isotope in a sample to decay to its stable form.

Carbon-14 is a radioactive isotope that has a half-life of 5700 years.

It is given that the rate of decrease of the mass, $m$, of the carbon-14 in a sample is proportional to its mass.

A sample of carbon-14 has initial mass $m_{0}$. What fraction of the original amount of carbon-14 would be present in this sample after 2500 years?

<a id="ch10-ex10B-q10"></a>
##### Question 10
Anya carried out an experiment and discovered that the rate of growth of her hair was constant. At the start of her experiment, her hair was 20 cm long. After 20 weeks, her hair was 26 cm long. Form and solve a differential equation to find a direct relationship between time, $t$, and the length of Anya's hair, $L$.

<a id="ch10-ex10B-q11"></a>
##### Question 11
A bottle of water is taken out of a refrigerator. The temperature of the water in the bottle is 4°C. The bottle of water is taken outside to drink. The air temperature outside is constant at 24°C.

It is given that the rate at which the water in the bottle warms up is proportional to the difference in the air temperature outside and the temperature of the water in the bottle.

After 2 minutes the temperature of the water in the bottle is 11°C.

**a** How long does it take for the water to warm 20°C ?

**b** According to the model, what temperature will the water in the bottle eventually reach if the air temperature remains constant and the water is not drunk?

<a id="ch10-ex10B-q12"></a>
##### Question 12
The number of customers, $n$, of a food shop $t$ months after it opens for the first time can be modelled as a continuous variable. It is suggested that the number of customers is increasing at a rate that is proportional to the square root of $n$.

**a** Form and solve a differential equation relating $n$ and $t$ to model this information.

**b** Initially, $n=0$, and after 6 months the food shop has 3600 customers. Find how many complete months it takes for the number of customers to reach 6800.

**c** The food shop has a capacity of serving 14000 customers per month. Show that the model predicts the shop will have reached its capacity sometime in the 12th month.

<a id="ch10-ex10B-q13"></a>
##### Question 13
Doubling time is the length of time it takes for a quantity to double in size or value.

The number of bacteria in a liquid culture can be modelled as a continuous variable and grows at a rate proportional to the number of bacteria present. Initially, there are 5000 bacteria in the culture. After 3.5 hours there are a million bacteria.

**a** What is the doubling time of the bacteria in the culture?

**b** What assumption does the model make about the growth of the bacteria and how realistic is this assumption?

#### EXPLORE 10.2

Modelling growth

Many of the models we have been using have assumed exponential growth. This type of growth is unlimited as the rate of growth of a population is proportional to the size of the population at that time.

This means that $\frac{\mathrm{d} P}{\mathrm{~d} t}=k P$.

Is an exponential growth model appropriate for modelling the population of the planet Earth in the long term?

It is thought that the maximum capacity of the Earth is about 10 billion people.

In 1987, the population of the Earth was about 5 billion people and the growth rate of the population was about 1.84\%.

Some people think that the problem of the Earth's increasing population can be solved by sending some people to live on other planets, such as Mars. In 2031, the first people to live on Mars will launch into space. The environment on Mars is different to Earth and many challenges must be overcome. This will all take time.

When a population is modelled as growing exponentially at a constant rate of $r \%$ per year, it takes about $\frac{70}{r}$ years for the population to double.

- Use the data given so far to investigate whether going to live on Mars is a good solution to the population problem.

- Comment on any assumptions you have made in your investigation.

There is statistical evidence that the population of the Earth is not growing at a constant rate each year. In 2017, the growth rate had decreased to 1.11\% per year. The population needs resources to survive and so the growth rate has decreased as resources have decreased.

A different model, logistic growth, can be used when resources are limited. This model takes into account the changing growth rates of the population.

Here are sketch graphs of exponential and logistic growth models:

Exponential growth

![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-260_587_588_477_569.jpg)

Logistic growth

![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-260_578_587_1214_576.jpg)

For example, for a population of size $P$,

$$
\frac{\mathrm{d} P}{\mathrm{~d} t}=\frac{r P(k-P)}{k}
$$

where the constant $r$ is the maximum natural growth rate (birth rate - death rate) and the constant $k$ is the maximum capacity of the limited environment.

- Show that as time increases this model suggests that $P$ tends to $k$.

- Comment on the limitations of this model.

### Checklist of learning and understanding

General procedure to solve a differential equation using the technique of separating the variables

- Separate the variables $\mathrm{f}(y) \frac{\mathrm{d} y}{\mathrm{~d} x}=\mathrm{g}(x)$.

- Integrate both sides $\int \mathrm{f}(y) \frac{\mathrm{d} y}{\mathrm{~d} x} \mathrm{~d} x=\int \mathrm{g}(x) \mathrm{d} x$

$$
\int \mathrm{f}(y) \mathrm{d} y=\int \mathrm{g}(x) \mathrm{d} x .
$$

- Solve to find a general solution.

- Substitute any given conditions to find a particular solution.

- Check your answer by differentiating.

Other points to remember

- Take care with modulus signs in expressions such as $\ln |\mathrm{f}(x)|$.

- When finding a general solution, check to see if any values excluded when the variables are separated are possible solutions.

<a id="ch10-review"></a>
### END-OF-CHAPTER REVIEW EXERCISE 10

<a id="ch10-review-q1"></a>
##### Question 1
The variables $x$ and $y$ satisfy the differential equation

$$
\frac{\mathrm{d} y}{\mathrm{~d} x}=x^{2} \mathrm{e}^{y+2 x}
$$

and it is given that $y=0$ when $x=0$.

Solve the differential equation and obtain an expression for $y$ in terms of $x$. `[9]`

<a id="ch10-review-q2"></a>
##### Question 2
The number of birds, $x$, in a particular area of land is recorded every year for $t$ years. $x$ is to be modelled as a continuous variable. The rate of change of the number of birds over time is modelled by

$$
\frac{\mathrm{d} x}{\mathrm{~d} t}=\frac{x(2500-x)}{5000} .
$$

It is given that $x=500$ when $t=0$.

**a** Find an expression for $x$ in terms of $t$. `[9]`

**b** How many birds does the model suggest there will be in the long term? `[1]`

<a id="ch10-review-q3"></a>
##### Question 3
Given that $y=2$ when $x=0$, solve the differential equation

$$
y^{3} \frac{\mathrm{dy}}{\mathrm{~d} x}=1+y^{4}
$$

obtaining an expression for $y^{4}$ in terms of $x$. `[6]`

<a id="ch10-review-q4"></a>
##### Question 4
The gradient of a curve is such that, at the point $(x, y)$, the gradient of the curve is proportional to $x \sqrt{y}$. At the point $(3,4)$ the gradient of this curve is -5.

**a** Form and solve a differential equation to find the equation of this curve. `[7]`

**b** Find the gradient of the curve at the point $(-3,4)$. `[1]`

<a id="ch10-review-q5"></a>
##### Question 5
**a** Given that $x<5$, find $\int \frac{50}{(5-x)(10-x)} \mathrm{d} x$. `[3]`

**b** A chemical reaction takes place between two substances $A$ and $B$. When this happens, a third substance, $C$, is produced. After $t$ hours there are $5-x$ grams of $A$, there are $10-x$ grams of $B$ and there are $x$ grams of $C$ present. The rate of increase of $x$ is proportional to the product of $5-x$ and $10-x$. Initially, $x=0$ and the rate of increase of $x$ is 1 gram per hour.

**i** Show that $x$ and $t$ satisfy the differential equation $50 \frac{\mathrm{~d} x}{\mathrm{~d} t}=(5-x)(10-x)$. `[1]`

**ii** Solve this equation, giving $x$ in terms of $t$. `[6]`

**iii** According to the model, approximately how many grams of chemical $C$ are produced by the reaction? `[1]`

<a id="ch10-review-q6"></a>
##### Question 6
The variables $x$ and $y$ are related by the differential equation

$$
\frac{\mathrm{d} y}{\mathrm{~d} x}=\frac{x e^{x}}{5 y^{4}} .
$$

It is given that $y=4$ when $x=0$. Find a particular solution of the differential equation and hence find the value of $y$ when $x=3.5$. `[8]`

<a id="ch10-review-q7"></a>
##### Question 7
**a** Use the substitution $u=\sqrt{y^{4}-1}$ to find $\int \frac{y^{3}}{\sqrt{y^{4}-1}} \mathrm{~d} y$. `[1]`

**b** Given that $\frac{\mathrm{d} y}{\mathrm{~d} x}=\frac{(2 x+1) \sqrt{y^{4}-1}}{x y^{3}}, y=\sqrt{3}$ when $x=1$, find a relationship between $x$ and $y$. `[6]`

<a id="ch10-review-q8"></a>
##### Question 8
The height, $h$ metres, of a cherry tree is recorded every year for $t$ years after it is planted. It is thought that the height of the tree is increasing at a rate proportional to $8-h$. When the tree is planted it is 0.5 metres tall and after 5 years it is 2 metres tall.

**a** Form and solve a differential equation to model this information. Give your answer in the form $h=\mathrm{f}(t)$. `[6]`

**b** According to the model, what will the height of the cherry tree be when it is fully grown? `[1]`

<a id="ch10-review-q9"></a>
##### Question 9
The variables $x$ and $y$ satisfy the differential equation

$$
\frac{\mathrm{d} y}{\mathrm{~d} x}=\mathrm{e}^{3(x+y)} \text { and } y=0 \text { when } x=0 .
$$

Solve the differential equation and obtain an expression for $y$ in terms of $x$. `[6]`

<a id="ch10-review-q10"></a>
##### Question 10
At the start of a reaction, there are $x$ grams of chemical $X$ present. At time $t$ seconds after the start, the rate of decrease of $x$ is proportional to $x t$.

**a** Using $k$ as constant of proportionality, where $k>0$, form a differential equation to model this reaction rate. `[1]`

**b** Solve the differential equation obtaining a relation between $x, t$ and $k$. `[5]`

**c** Initially, there are 150 grams of chemical $X$ present and after 10 seconds this has decreased to 120 grams. Find the time after the start of the reaction when the amount of chemical $X$ has decreased to 1 gram. `[3]`

<a id="ch10-review-q11"></a>
##### Question 11
**a** Using partial fractions find $\int \frac{1}{P(5-P)} \mathrm{d} P$. `[4]`

**b** Given that $P=3$ when $t=0$, solve the differential equation $\frac{\mathrm{d} P}{\mathrm{~d} t}=P(5-P)$, obtaining an expression for $P$ in terms of $t$. `[4]`

**c** Describe what happens to $P$ when $t \rightarrow \infty$. `[1]`

<a id="ch10-review-q12"></a>
##### Question 12
The population of a country was 50 million in 2000 and 60 million in 2010. The rate of increase of the population is modelled by

$$
\frac{\mathrm{d} P}{\mathrm{~d} t}=\frac{k P(100-P)}{100}
$$

Use the model to predict the population of the country in 2025. `[7]`

<a id="ch10-review-q13"></a>
##### Question 13
**a** Use the substitution $u=x^{2}$ to find $\int x \sin x^{2} \mathrm{~d} x$. `[3]`

**b** Given that $\frac{\mathrm{d} y}{\mathrm{~d} x}=\frac{x \sin x^{2}}{y}, y=-1$ when $x=0$, find a relationship between $x$ and $y$. `[5]`

<a id="ch10-review-q14"></a>
##### Question 14
Solve the differential equation

$$
\frac{\mathrm{d} y}{\mathrm{~d} x}=\frac{\tan x}{\mathrm{e}^{3 y}}
$$

given that $x=0$ when $y=0$. Give your answer in the form $y=\mathrm{f}(x)$. `[6]`

<a id="ch10-review-q15"></a>
##### Question 15
There are 2000 mice in a field. At time $t$ hours, $x$ mice are infected with a disease. The rate of increase of the number of mice infected is proportional to the product of the number of mice infected and the number of mice not infected. Initially 500 mice are infected and the disease is spreading at a rate of 50 mice per hour.

**a** Form and solve a differential equation to model this data. Give your answer in the form $t=\mathrm{f}(x)$. `[7]`

**b** Find how long it takes for 1900 mice to be infected. `[1]`

<a id="ch10-review-q16"></a>
##### Question 16
The variables $x$ and $y$ are related by the differential equation

$$
x \frac{\mathrm{~d} y}{\mathrm{~d} x}=1-y^{2} .
$$

When $x=2, y=0$. Solve the differential equation, obtaining an expression for $y$ in terms of $x$. `[8]`

*Cambridge International A Level Mathematics 9709 Paper 31 Q6 November 2012*

<a id="ch10-review-q17"></a>
##### Question 17
The variables $x$ and $\theta$ satisfy the differential equation

$$
\frac{\mathrm{d} x}{\mathrm{~d} \theta}=(x+2) \sin ^{2} 2 \theta,
$$

and it is given that $x=0$ when $\theta=0$. Solve the differential equation and calculate the value of $x$ when $\theta=\frac{1}{4} \pi$, giving your answer correct to 3 significant figures. `[9]`

*Cambridge International A Level Mathematics 9709 Paper 31 Q8 November 2015*

![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-265_1346_1941_4_136.jpg)
