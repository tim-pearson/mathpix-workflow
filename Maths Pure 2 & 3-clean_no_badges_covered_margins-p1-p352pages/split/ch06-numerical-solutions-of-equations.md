# Chapter 6: Numerical solutions of equations

In this chapter you will learn how to:

- locate approximately a root of an equation, by means of graphical considerations and/or searching for a sign change

- understand the idea of, and use the notation for, a sequence of approximations that converges to a root of an equation

- understand how a given simple iterative formula of the form $x_{n+1}=\mathrm{F}\left(x_{n}\right)$ relates to the equation being solved, and use a given iteration, or an iteration based on a given rearrangement of an equation, to determine a root to a prescribed degree of accuracy.

![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-133_606_1942_2166_137.jpg)

<a id="ch06-prerequisite"></a>
### PREREQUISITE KNOWLEDGE

| Where it comes from | What you should be able to do | Check your skills |
| :--- | :--- | :--- |
| IGCSE / O Level Mathematics | Substitute numbers for letters in complicated formulae and algebraic expressions, including those involving logarithmic functions, exponential functions and major and minor trigonometric functions. | 1 Evaluate each of the following expressions when $x=1.5$.<br>a $\frac{2}{3}\left(x+\frac{1}{x^{2}}\right)$<br>b $100 \sin x-99 x$, ( $x$ in radians)<br>c $\mathrm{e}^{-x}$<br>d $\ln x+5$<br> |
| IGCSE / O Level Mathematics | Rearrange complicated formulae and equations. | 2 Rearrange each formula so that $x$ is the subject.<br>a $y=4 x^{2}+13$, given $x>0$<br>b $0=\frac{y-3 x+7}{w}$<br>c $3=\sqrt[3]{\frac{1+y}{x^{5}}}$<br> |
| Pure Mathematics 1 Coursebook, Chapters 1 and 2 | Understand the relationship between a graph and its associated algebraic equation, and use the relationship between points of intersection of graphs and solutions of equations. | 3 Show that the $x$-coordinates of the solutions to the simultaneous equations: $\begin{aligned} & y=x^{2}-6 x+10 \\ & y=x \end{aligned}$ <br> also satisfy the equation $x^{2}-7 x+10=0 .$ |
| Pure Mathematics 1 Coursebook, Chapter 1 | Know that the values of $x$ that make both sides of an equation equal are called the roots of the equation. <br> Also, the roots of $\mathrm{f}(x)=0$ are the $x$-intercepts on the graph of $y=\mathrm{f}(x) .$ | 4 Find the roots of the equation $x^{2}-7 x+10=0$. |
| IGCSE / O Level Mathematics Pure Mathematics 1 Coursebook, Chapter 5 | Sketch graphs of quadratic or cubic functions or the trigonometric functions sine, cosine, tangent. | 5 Sketch the graph, $y=\mathrm{f}(x)$, of each function.<br>a $\mathrm{f}(x)=x^{3}+1$<br>b $\mathrm{f}(x)=\cos 2 x-3$<br>c $\mathrm{f}(x)=4 x^{2}-16 x$<br> |
| Chapters 2 and 3 | Sketch graphs of exponential or logarithmic functions or the trigonometric functions cosecant, secant, cotangent. | 6 Sketch the graph, $y=\mathrm{g}(x)$, of each function.<br>a $\mathrm{g}(x)=\frac{\mathrm{e}^{x}}{2}$<br>b $\mathrm{g}(x)=\ln (x-1)$<br>c $\mathrm{g}(x)=\operatorname{cosec} x$<br> |

Why solve equations numerically?

You are used to solving equations using direct, algebraic methods such as factorising or using the quadratic formula.

You might be surprised to learn that not all equations can be solved using a direct, algebraic process.

Numerical methods are ways of calculating approximate solutions to equations. They are extremely powerful problem-solving tools and many are available. They are widely used in engineering, computing, finance and many other applications.

A well-programmed computer is quickly able to solve a complicated equation using a numerical method. So why do we need to understand how the method works?

Knowing how a numerical method works helps us to:

- understand when the results are likely to be reasonable

- understand how to use available software correctly

- select an appropriate method when choices are available

- write our own programs when we need to do so, if we have the programming skills!

To be a powerful problem-solving tool, the method must be used correctly. This might mean the method needs to work quickly or work to obtain a particular level of accuracy. When used incorrectly, numerical methods might be very slow or even fail to work, as we will see later in this chapter.

In this chapter we will focus on one numerical method, the numerical solution of an equation using an iterative formula.

## 6.1 Finding a starting point

As we will see throughout this chapter, a good starting point is very important.

We need a method to find an approximate solution to an equation first.

We might find this using, for example, a graphical approach or the change of sign approach.

For suitable functions, each of these approaches will produce two values: one above and one below the solution that we are finding.

<a id="ch06-we-6.1"></a>
#### WORKED EXAMPLE 6.1

By sketching graphs of $y=x^{3}$ and $y=4-x$, show that the equation $x^{3}+x-4=0$ has a root $\alpha$ between 1 and 2.

Answer

![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-135_522_799_2107_512.jpg)

There is one point of intersection and its $x$-coordinate is between 1 and 2.

At this point $x^{3}=4-x$.

This means that the equation $x^{3}=4-x$ has one root between 1 and 2.

Rearranging this equation gives $x^{3}+x-4=0$.

Hence $x^{3}+x-4=0$ has a root, $\alpha$, between 1 and 2.

<a id="ch06-we-6.2"></a>
#### WORKED EXAMPLE 6.2

Show, by calculation, that the equation $\mathrm{f}(x)=x^{5}+x-1=0$ has a root $\alpha$ between 0 and 1 .

Answer

| Find the value of $\alpha$ such that $\mathrm{f}(\alpha)=0$. | Why? Think about it and check the explanation that follows. |
| :--- | :--- |
| $\mathrm{f}(0)=0^{5}+0-1=-1$ | As $\alpha$ is between 0 and 1 , then $\mathrm{f}(0)$ might have the opposite sign to f(1). |
| :--- | :--- |
| $\mathrm{f}(1)=1^{5}+1-1=1$ |  |

The change of sign indicates the presence of a root, so $0<\alpha<1$.

This conclusion is important as it completes the argument.

To see why the change of sign method works in this case, look at the graph of $y=\mathrm{f}(x)$.

![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-136_467_604_1526_786.jpg)

Since it starts below the $x$-axis at $x=0$ and finishes above the $x$-axis at $x=1$, it must cross the $x$-axis somewhere in between, say at $x=\alpha$, where $0<\alpha<1$. So $\alpha$ is a root of the equation, that is, $\mathrm{f}(\alpha)=0$.

<a id="ch06-we-6.3"></a>
#### WORKED EXAMPLE 6.3

**a** By sketching a suitable pair of graphs, show that the equation $\cos x=2 x-1$ (where $x$ is in radians) has only one root for $0 \leqslant x \leqslant \frac{1}{2} \pi$.

**b** Verify by calculation that this root lies between $x=0.8$ and $x=0.9$.

Answer

**a** Draw the graphs of $y=\cos x$ and $y=2 x-1$ Why are these graphs suitable?

![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-137_515_626_749_415.jpg)

The graphs intersect once only and so the equation $\cos x=2 x-1$ has only one root for $0 \leqslant x \leqslant \frac{1}{2} \pi$.

**b** $\cos x=2 x-1$ so $\cos x-2 x+1=0$

Let $\mathrm{f}(x)=\cos x-2 x+1$ and so $\mathrm{f}(x)=0$ then

$$
\begin{align}
& f(0.8)=\cos 0.8-2(0.8)+1=0.0967 \qquad \\
& f(0.9)=\cos 0.9-2(0.9)+1=-0.1783 \qquad
\end{align}
$$

Change of sign indicates the presence of a root.

<a id="ch06-ex6A"></a>
### EXERCISE 6A

<a id="ch06-ex6A-q1"></a>
##### Question 1
**a** On the same axes, sketch the graphs of $y=\sqrt{1+x}$ and $y=x^{2}$.

**b** Using your answer to part a, explain why the equation $x^{2}-\sqrt{1+x}=0$ has two roots.

**c** Show, by calculation, that the smaller of these two roots lies between $x=-1$ and $x=0$.

<a id="ch06-ex6A-q2"></a>
##### Question 2
**a** By sketching graphs of $y=x^{3}+5 x^{2}$ and $y=5-2 x$, determine the number of real roots of the equation $x^{3}+5 x^{2}+2 x-5=0$.

**b** Verify by calculation that the largest root of $x^{3}+5 x^{2}+2 x-5=0$ lies between $x=0$ and $x=2$.

<a id="ch06-ex6A-q3"></a>
##### Question 3
The curve $y=x^{3}+5 x-1$ cuts the $x$-axis at the point $(\alpha, 0)$.

**a** By sketching the graph of $y=x^{3}$ and one other suitable graph, deduce that this is the only point where the curve $y=x^{3}+5 x-1$ cuts the $x$-axis.

**b** Using calculations, show that $0.1<\alpha<0.5$.

<a id="ch06-ex6A-q4"></a>
##### Question 4
**a** On the same axes, sketch the graphs of $y=\ln (x+1)$ and $y=3 x-4$.

**b** Hence deduce the number of roots of the equation $\ln (x+1)-3 x+4=0$.

<a id="ch06-ex6A-q5"></a>
##### Question 5
**a** By sketching graphs of $y=\mathrm{e}^{x}$ and $y=x+6$, determine the number of roots of the equation $\mathrm{e}^{x}-x-6=0$.

**b** Show, by calculation, that $\mathrm{e}^{x}-x-6=0$ has a root that lies between $x=2.0$ and $x=2.1$.

<a id="ch06-ex6A-q6"></a>
##### Question 6
**a** Show, by calculation, that $(x+2) \mathrm{e}^{5 x}=1$ has a root between $x=0$ and $x=-0.2$.

**b** Show, by sketching the graph of $y=\mathrm{e}^{5 x}$ and one other suitable graph, that this is the only root of this equation.

<a id="ch06-ex6A-q7"></a>
##### Question 7
**a** Show by calculation that the equation $\cos ^{-1} 2 x=1-x$ has a root $\alpha$, where $0.4 \leqslant \alpha \leqslant 0.5$.

**b** The diagram shows the graph of $y=\cos ^{-1} 2 x$ where $-0.5 \leqslant x \leqslant 0.5$.

![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-138_541_618_1044_378.jpg)

By drawing a suitable graph on a copy of the diagram, show that $\alpha$ is the only root of $\cos ^{-1} 2 x=1-x$ for $-0.5 \leqslant x \leqslant 0.5$.

<a id="ch06-ex6A-q8"></a>
##### Question 8
The curve with equation $y=\frac{\sin x}{2 x+3}$ where $x<-\frac{\pi}{2}$ intersects the line $y=1$ at the point $(\alpha, 1)$.

**a** By sketching the graph of $y=\sin x$ for $-2 \pi<x<-\frac{\pi}{2}$ radians and one other suitable graph, deduce that this is the only point where the curve $y=\frac{\sin x}{2 x+3}$ intersects the line $y=1$.

**b** Using calculations, show that $-2<\alpha<-1.9$.

<a id="ch06-ex6A-q9"></a>
##### Question 9
**a** By sketching a suitable pair of graphs, show that the equation $x^{3}+4 x=7 x+4$ has only one root for $0 \leqslant x \leqslant 5$.

**b** Verify by calculation that this root lies between $x=2$ and $x=3$.

<a id="ch06-ex6A-q10"></a>
##### Question 10
**a** Show graphically that the equation $2^{x}=x+4$ has exactly two roots.

**b** Show, by calculation, that the larger of the two roots is between 2.7 and 2.8.

<a id="ch06-ex6A-q11"></a>
##### Question 11
**a** By sketching two suitable graphs on the same diagram, show that the equation $\cot x=x^{2}$ has one root between 0 and $\frac{\pi}{2}$ radians.

**b** Show, by calculation, that this root, $\alpha$, lies between 0.8 and 1.

<a id="ch06-ex6A-q12"></a>
##### Question 12
**a** By sketching a suitable pair of graphs, deduce the number of roots of the equation $x=\tan 2 x$ for $0<x<2 \pi$.

**b** Verify, by calculation, that one of these roots, $\alpha$, lies between 2.1 and 2.2.

<a id="ch06-ex6A-q13"></a>
##### Question 13
**a** Show graphically that the equation $\operatorname{cosec} x=\sin x$ has exactly two roots for $0<x<2 \pi$.

**b** Use an algebraic method to find the value of the larger root correct to 3 significant figures.

<a id="ch06-ex6A-q14"></a>
##### Question 14
$ \mathrm{f}(x)=20 x^{3}+8 x^{2}-7 x-3$

a The equation $20 x^{3}+8 x^{2}-7 x-3=0$ has exactly two roots.

Without factorising the cubic equation, show, by calculation, that one of these roots is between 0.5 and 1.

b Show, by sketching the graph of $y=\mathrm{f}(x)$ for $-1 \leqslant x \leqslant 1$, that the smaller root is between -1 and 0.

**c** Explain why it is not necessary to use a numerical method to find the two solutions of this equation.

<a id="ch06-ex6A-q15"></a>
##### Question 15
A guitar tuning peg is in the shape of a cylinder with a hemisphere at one end.

![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-139_438_330_1180_1704.jpg)

The cylinder is 20 mm long and the whole peg is made from $800 \mathrm{~mm}^{3}$ of plastic.

The base radius of the cylinder is $r \mathrm{~mm}$.

**a** Show that $\pi r^{3}+30 \pi r^{2}-1200=0$.

**b** Show that the value of $r$ is between 3 mm and 4 mm.

#### EXPLORE 6.1

Anil is trying to find the roots of $\mathrm{f}(x)=|\tan x|=0$ between 0 and $2 \pi$ radians.

He states:

$\mathrm{f}(3.1)>0$ and $\mathrm{f}(3.2)>0$. There is no change of sign so there is no root of $|\tan x|=0$ between 3.1 and 3.2.

Mika states:

$y=|\tan x|$ and it meets the $x$-axis where $x=\pi$ radians so Anil has made a calculation error.

Discuss Anil and Mika's statements.

#### DID YOU KNOW?

Interestingly, cubic and quartic equations can be solved algebraically. This has been known since the 16th century and was shown by the Italian mathematicians Niccolò Fontana (Tartaglia) and Lodovico Ferrari. Quintic equations cannot be solved algebraically in general. This was shown by the Norwegian mathematician Niels Abel and the French mathematician Évariste Galois in the early 19th century.

## 6.2 Improving your solution

Once we have an approximate location for a solution, we can improve it.

One common way to do this is to use an iterative process, finding values that are closer and closer to $\alpha$, the root we are looking to find.

For example, we have shown, by calculation, that the equation $\mathrm{f}(x)=x^{5}+x-1=0$ has a root $\alpha$ between 0 and 1 . This is a reasonable starting point but probably not accurate enough if we wanted a solution to this equation in the real world. What if we needed to know the value correct to 1 significant figure? How could we find it?

Let us consider a rearrangement of $\mathrm{f}(x)=x^{5}+x-1=0$.

The root we are trying to find is a value of $x$, so rearranging $x^{5}+x-1=0$ into the form $x=\mathrm{F}(x)$ seems reasonable (in other words, $x=$ some function of $x$ ).

One possible rearrangement of this form is $x=\sqrt[5]{1-x}$.

As we already know that $0<\alpha<1$, a good starting point is $x=0.5$.

Now we can test our value to see how accurate it is. How?

- Work out the value of $\sqrt[5]{1-x}$ for the starting value.

$$
\sqrt[5]{1-0.5}=\sqrt[5]{0.5}=0.87055
$$

- Compare it with $x$.

| $x$ | $\mathbf{F}(\boldsymbol{x})=\sqrt[\mathbf{5}]{\mathbf{1}-\boldsymbol{x}}$ | Are $\boldsymbol{x}$ and $\mathbf{F}(\boldsymbol{x})$ the same correct to 1 significant figure? |
| :--- | :--- | :--- |
| 0.5 | 0.87055 ... | No |

- Are the values the same to the required number of significant figures or decimal places?

Yes - then use this value as the estimate for the root.

No - then find a more accurate value.

Look at the graphs of $y=x$ and $y=\sqrt[5]{1-x}$ on the same diagram.

![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-140_862_744_1802_178.jpg)

The graphs show that the values $x$ and $\mathrm{F}(x)$ are not very close together as the vertical distance between the line and curve is quite large.

How do we improve the accuracy of the estimate for the root?

We can see in the following diagram that $0.87055$ is a better approximation for the root $\alpha$ than 0.5.

Is 0.870 55... close enough?

![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-141_912_743_529_218.jpg)

The vertical distance between the line and curve is now smaller, so the values are converging.

Testing $x=0.87055$ gives $\sqrt[5]{1-x}=\sqrt[5]{1-0.87055} \qquad =0.66438$

| $x$ | $\mathbf{F}(\boldsymbol{x})=\sqrt[\mathbf{5}]{\mathbf{1}-\boldsymbol{x}}$ | Are $\boldsymbol{x}$ and $\mathbf{F}(\boldsymbol{x})$ the same correct to 1 significant figure? |
| :--- | :--- | :--- |
| 0.5 | 0.87055... | No |
| $0.87055$ | 0.66438... | No |

We can see that $0.66438$ is a better approximation of the root $\alpha$ than $0.87055$ because the values are closer together. Is 0.66438... close enough?

When we continue testing and comparing values, we find:

| $x$ | $\mathbf{F}(\boldsymbol{x})=\sqrt[\mathbf{5}]{\mathbf{1}-\boldsymbol{x}}$ | Are $\boldsymbol{x}$ and $\mathbf{F}(\boldsymbol{x})$ the same correct to 1 significant figure? |
| :--- | :--- | :--- |
| 0.66438... | 0.80383... | No |
| 0.80383... | 0.72197... | No |
| 0.72197... | 0.77413... | No |
| 0.77413... | 0.742 62... | No |
| 0.742 62... | 0.76227... | No |
| 0.76227... | 0.75026... | Yes |

Each test is called an iteration. Each iteration gives a value of $x$ that is closer to the actual value of the root than the previous value of $x$.

It seems as if the value of $\alpha$ is 0.8 correct to 1 significant figure.

This (enlarged) diagram shows what is happening with each new value.

![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-142_1437_1140_345_183.jpg)

Each value that comes from $\mathrm{F}(x)$ is used as the next value for $x$. The spiral is often called the cobweb pattern.

Summary

When trying to solve $\mathrm{f}(x)=0$, rearrange the equation to the form $x=\mathrm{F}(x)$.

When $\alpha$ is the value of $x$ such that $x=\mathrm{F}(x)$ then $\alpha$ is also a solution of $\mathrm{f}(x)=0$.

Subscript notation and formulae

In order to avoid unnecessary repetition and to make sure the process is recorded accurately, the method outlined is usually described using subscript notation.

The first approximation of the root is called $x_{1}$ (sometimes it is called $x_{0}$ ).

The next approximation of the root is called $x_{2}$, and so on.

A relationship such as $x=\mathrm{F}(x)$ where $\mathrm{F}(x)=\sqrt[5]{1-x}$ is the basis for an iterative formula:

$$
x_{n+1}=\mathrm{F}\left(x_{n}\right)=\sqrt[5]{1-x_{n}}
$$

Looking at the values we already have we can see how much easier this is to record:

| $\boldsymbol{x}_{\mathbf{1}}=\mathbf{0 . 5}$ | $\boldsymbol{x}_{\boldsymbol{n}+\mathbf{1}}=\mathbf{F}\left(\boldsymbol{x}_{\boldsymbol{n}}\right)=\sqrt[\mathbf{5}]{\mathbf{1}-\boldsymbol{x}_{\boldsymbol{n}}}$ | Are they the same correct to 1 significant figure? |
| :--- | :--- | :--- |
|  | $x_{2}=0.87055$ | No |
|  | $x_{3}=0.66438$ | No |
|  | $x_{4}=0.80383$ | No |
|  | $x_{5}=0.72197$ | No |
|  | $x_{6}=0.77413$ | No |
|  | $x_{7}=0.74262$ | No |
|  | $x_{8}=0.76227$ | No |
|  | $x_{9}=0.75026$ | Yes |

In this format we test the accuracy of the values by comparing each value of $x_{n}$ in the sequence with the previous value.

#### TIP

Does your calculator have an Ans key?

Using the Ans key reduces the number of key strokes needed to use an iterative process.

- Type the value for $x_{1}$ into your calculator and press .

$$
\text { e.g. } 0.5=
$$

- Type the formula into your calculator using Ans instead of $x_{n}$.

$$
\text { e.g. } \sqrt[5]{1-\text { Ans }}
$$

Now each time you press the calculator gives you the next value of $x_{n}$ generated (so $x_{2}, x_{3}, x_{4},$ ).

Try this now and check that you generate the values that are given in the table.

<a id="ch06-we-6.4"></a>
#### WORKED EXAMPLE 6.4

The equation $x^{2}+x-3=0$ has a negative root, $\alpha$.

**a** Show that this equation can be rearranged as $x=\frac{3}{x}-1$.

**b** Use the iterative formula $x_{n+1}=\frac{3}{x_{n}}-1$ with a starting value of $x_{1}=-2.5$ to find $\alpha$ correct to 2 decimal places. Give the result of each iteration to 4 decimal places, where appropriate.

Answer

**a**

$$
\begin{align}
& x^{2}+x-3=0 \\
& \frac{x^{2}}{x}+\frac{x}{x}-\frac{3}{x}=\frac{0}{x} \\
& x+1-\frac{3}{x}=0 \\
& x=\frac{3}{x}-1 \qquad \quad \text { Divide through by } x . \\
& \quad \text { Isolate } x .
\end{align}
$$

**b**

| $\boldsymbol{x}_{\mathbf{1}}=-\mathbf{2 . 5}$ | $\boldsymbol{x}_{\boldsymbol{n}+\mathbf{1}}=\frac{\mathbf{3}}{\boldsymbol{x}_{\boldsymbol{n}}}-\mathbf{1}$ | Are these the same correct to 2 decimal places? |
| :--- | :--- | :--- |
|  | $x_{2}=\frac{3}{-2.5}-1=-2.2$ | No |
|  | $x_{3}=\frac{3}{-2.2}-1=-2.3636$ | No |
|  | $x_{4}=-2.2692$ | No |
|  | $x_{5}=-2.3220$ | No |
|  | $x_{6}=-2.2920$ | No |
|  | $x_{7}=-2.3089$ | No |
|  | $x_{8}=-2.2993$ | No |
|  | $x_{9}=-2.3047$ | Yes |

The root seems to be $\alpha=-2.30$ to 2 decimal places.

We can prove this, using a change of sign test:

When $\alpha=-2.30$ then $-2.305<\alpha<-2.295$ and so

$$
\begin{align}
& f(-2.305)=(-2.305)^{2}+(-2.305)-3=0.00802 \qquad \\
& f(-2.295)=(-2.295)^{2}+(-2.295)-3=-0.0279 \qquad
\end{align}
$$

Change of sign indicates presence of root, therefore $\alpha=-2.30$, to 2 decimal places.

<a id="ch06-we-6.5"></a>
#### WORKED EXAMPLE 6.5

The equation $\mathrm{e}^{x}-1=2 x$ has a root $\alpha=0$.

**a** Show by calculation that this equation also has a root, $\beta$, such that $1<\beta<2$.

**b** Show that this equation can be rearranged as $x=\ln (2 x+1)$.

**c** Use an iteration process based on the equation in part b, with a suitable starting value, to find $\beta$ correct to 3 significant figures.

Give the result of each step of the process to 5 significant figures.

Answer

**a** Let $\mathrm{f}(x)=\mathrm{e}^{x}-1-2 x=0$ and look for a change of sign.

$$
\begin{align}
& f(1)=e-1-2=-0.2817 \qquad \\
& f(2)=e^{2}-1-2(2)=2.38905 \qquad
\end{align}
$$

Change of sign indicates presence of root.

**b** $\mathrm{e}^{x}-1=2 x$ Isolate e.

$$
\mathrm{e}^{x}=2 x+1
$$

Take logs to base e.

$$
x=\ln (2 x+1)
$$

✓

**c** A suitable iterative formula is $x_{n+1}=\ln \left(2 x_{n}+1\right)$ with a starting value of $x_{1}=1.5$.

(Any value between 1 and 2 would be an acceptable starting value.)

| $\boldsymbol{x}_{\mathbf{1}} \boldsymbol{=} \mathbf{1 . 5}$ | $\boldsymbol{x}_{\boldsymbol{n}+\mathbf{1}} \boldsymbol{=} \boldsymbol{\operatorname { l n }} \boldsymbol{(} \mathbf{2} \boldsymbol{x}_{\boldsymbol{n}} \boldsymbol{+} \mathbf{1} \boldsymbol{)}$ | Are these the same correct to 3 significant figures? |
| :--- | :--- | :--- |
|  | $x_{2}=\ln (2 \times 1.5+1)=1.38629 \qquad =1.3863$ | No |
|  | $x_{3}=\ln (2 \times 1.38629 \qquad +1)=1.32776 \qquad =1.3278$ | No |
|  | $x_{4}=1.29623 \qquad =1.2962$ | No |
|  | $x_{5}=1.27884 \qquad =1.2788$ | No |
|  | $x_{6}=1.26910 \qquad =1.2691$ | No |
|  | $x_{7}=1.26362 \qquad =1.2636$ | No |
|  | $x_{8}=1.26051 \qquad =1.2605$ | Yes |

The root seems to be $\beta=1.26$ correct to 3 significant figures.

We can prove this, using a change of sign test:

When $\beta=1.26$ then $1.255<\beta<1.265$ and so:

$$
\begin{align}
& f(1.255)=e^{1.255}-1-2(1.255)=-0.0021616 \qquad \\
& f(1.265)=e^{1.265}-1-2(1.265)=0.01309 \qquad
\end{align}
$$

Change of sign indicates presence of root, therefore $\beta=1.26$ correct to 3 significant figures.

You might notice that the pattern of convergence is different in this example. This is clear when you look at the graphs of $y=x$ and $y=\ln (2 x+1)$ on the same grid. The type of convergence shown in the graph on the right is often called a staircase pattern.

![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-145_614_1361_1923_448.jpg)

<a id="ch06-ex6B"></a>
### EXERCISE 6B

<a id="ch06-ex6B-q1"></a>
##### Question 1
The equation $x^{3}+5 x-7=0$ has a root $\alpha$ between 1 and 1.2.

The iterative formula $x_{n+1}=\frac{7-x_{n}^{3}}{5}$ can be used to find the value of $\alpha$.

**a** Using a starting value of $x_{1}=1.1$, find and write down, correct to 4 decimal places, the value of each of $x_{2}, x_{3}, x_{4}, x_{5}, x_{6}$.

**b** Write the value of $x_{6}$ correct to 2 decimal places and prove that this is the value of $\alpha$ correct to 2 decimal places.

<a id="ch06-ex6B-q2"></a>
##### Question 2
**a** Show that the equation $\ln (x+1)+2 x-4=0$ has a root $\alpha$ between $x=1$ and $x=2$.

**b** Use the iterative formula $x_{n+1}=\frac{4-\ln \left(x_{n}+1\right)}{2}$ with an initial value of $x_{1}=1.5$ to find the value of $\alpha$ correct to 3 decimal places.

<a id="ch06-ex6B-q3"></a>
##### Question 3
The equation $(x-0.5) \mathrm{e}^{3 x}=1$ has a root $\alpha$.

**a** Show, by sketching the graph of $y=\mathrm{e}^{3 x}$ and one other suitable graph, that $\alpha$ is the only root of this equation.

**b** Use the iterative formula $x_{n+1}=\mathrm{e}^{-3 x_{n}}+0.5$ with $x_{1}=0.5$ to find the value of $\alpha$ correct to 2 decimal places. Give the value of each of your iterations to 4 decimal places.

<a id="ch06-ex6B-q4"></a>
##### Question 4
**a** By sketching a suitable pair of graphs, show that the equation $x^{3}+10 x=x+5$ has only one root that lies between 0 and 1.

**b** Use the iterative formula $x_{n+1}=\frac{5-x_{n}^{3}}{9}$, with a suitable value for $x_{1}$, to find the value of this root correct to 4 decimal places. Give the result of each iteration to 6 decimal places.

<a id="ch06-ex6B-q5"></a>
##### Question 5
The equation $\cos ^{-1} 3 x=1-x$ has a root $\alpha$.

**a** Show, by calculation, that $\alpha$ is between $\frac{\pi}{15}$ and $\frac{\pi}{12}$.

**b** Show that the given equation can be rearranged into the form $x=\frac{1}{3} \cos (1-x)$.

**c** Using the iterative formula $x_{n+1}=\frac{1}{3} \cos \left(1-x_{n}\right)$ with a suitable starting value, $x_{1}$, find the value of $\alpha$ correct to 3 decimal places. Give the result of each iteration to 5 decimal places.

<a id="ch06-ex6B-q6"></a>
##### Question 6
The terms of a sequence with first term $x_{1}=1$ are defined by the iterative formula:

$$
x_{n+1}=\sqrt{\frac{5-2 x_{n}-x_{n}^{3}}{5}}
$$

The terms converge to the value $\alpha$.

**a** Use this formula to find the value of $\alpha$ correct to 2 decimal places. Give the value of each term you calculate to 4 decimal places.

**b** The value $\alpha$ is the root of an equation of the form $a x^{3}+b x^{2}+c x+d=0$, where $a, b, c$ and $d$ are integers. Find this equation.

<a id="ch06-ex6B-q7"></a>
##### Question 7
The equation $x^{4}-1-x=0$ has a root, $\alpha$, between $x=1$ and $x=2$.

**a** Show that $\alpha$ also satisfies the equation $x=\sqrt[4]{1+x}$.

**b** Write down an iterative formula based on the equation in part a.

**c** Use your iterative formula, with a starting value of $x_{1}=1.5$, to find $\alpha$ correct to 2 decimal places. Give the result of each iteration to 4 decimal places.

<a id="ch06-ex6B-q8"></a>
##### Question 8
The equation $\operatorname{cosec} x=x^{2}$ has a root, $\alpha$, between 1 and 2.

The equation can be rearranged either as $x=\sin ^{-1}\left(\frac{1}{x^{2}}\right)$ or $x=\sqrt{\frac{1}{\sin x}}$.

**a** Write down two possible iterative formulae, one based on each given rearrangement.

Use the starting value 1.5.

**b** Show that one of the formulae from part a fails to converge.

**c** Show that the other formula from part a converges to $\alpha$ and find the value of $\alpha$ correct to 3 decimal places. Give the result of each iteration to 5 decimal places.

<a id="ch06-ex6B-q9"></a>
##### Question 9
The terms of a sequence, defined by the iterative formula $x_{n+1}=\ln \left(x_{n}^{2}+4\right)$, converge to the value $\alpha$. The first term of the sequence is 2.

**a** Find the value of $\alpha$ correct to 2 decimal places. Give each term of the sequence you find to 4 decimal places.

**b** The value $\alpha$ is a root of an equation of the form $x^{2}=\mathrm{f}(x)$. Find this equation.

<a id="ch06-ex6B-q10"></a>
##### Question 10
The equation $\frac{\sin (x-1)}{2 x-3}+1=0$ has a root, $\alpha$, between $x=1$ and $x=1.4$.

**a** Show that $\alpha$ also satisfies the equation $x=\frac{3-\sin (x-1)}{2}$.

**b** Using an iterative formula based on the equation from part a, with a suitable starting value, find the value of $\alpha$ correct to 3 significant figures. Give the result of each iteration to 5 significant figures.

<a id="ch06-ex6B-q11"></a>
##### Question 11
The graphs of $y=\left(\frac{3}{2}\right)^{x}-1$ and $y=x$ intersect at the points $O(0,0)$ and $A$.

**a** Sketch these graphs on the same diagram.

**b** Using logarithms, find a suitable iterative formula that can be used to find the coordinates of the point $A$.

**c** Calculate the length of the line $O A$, giving your answer correct to 2 significant figures. Give the value of any iterations you calculate to a suitable number of significant figures.

<a id="ch06-ex6B-q12"></a>
##### Question 12
The diagram shows a container in the shape of a cone with a cylinder on top.

The height of the cylinder is 3 times its base radius, $r$.

The volume of the container must be $5500 \mathrm{~cm}^{3}$.

![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-147_423_383_1752_1639.jpg)

The base of the cone has a radius of $r \mathrm{~cm}$.

**a** Write down an expression for the height of the cone in terms of $r$.

**b** Show that $2 \pi r^{3}+11 \pi r^{2}-5500=0$.

**c** The equation in part b has a root, $\alpha$.

Show that $\alpha$ is also a root of the equation $r=\sqrt[3]{\frac{5500-11 \pi r^{2}}{2 \pi}}$.

**d** Using an iterative formula based on the equation in part c, and a starting value of 8, find the value of $\alpha$ correct to 3 decimal places. Give the value of each of your iterations to an appropriate degree of accuracy.

**e** Explain what information is given by your answer to part d, in the context of the question.

<a id="ch06-ex6B-q13"></a>
##### Question 13
The equation $x^{3}-7 x^{2}+1=0$ has two positive roots, $\alpha$ and $\beta$, which are such that $\alpha$ lies between 0 and 1 and $\beta$ lies between 6 and 7.

By deriving two suitable iterative formulae from the given equation, carry out suitable iterations to find the value of $\alpha$ and of $\beta$, giving each correct to 2 decimal places. Give the value of each of your iterations to 4 decimal places.

<a id="ch06-ex6B-q14"></a>
##### Question 14
**a** Show graphically that the equation $\cot x=\sin x$ has a root, $\alpha$, which is such that $0<\alpha<\frac{\pi}{2}$.

**b** Show that the equation in part a can be rearranged as $x=\sin ^{-1} \sqrt{\cos x}$.

**c** Using an iterative formula based on the equation in part b, with an initial value of 0.9, find the value of $\alpha$ correct to 2 decimal places. Give the value of each iteration to an appropriate number of decimal places.

**d** The equation given in part a can be rearranged in other ways.

Find an example of a formula, based on a different rearrangement of the equation given in part a, that also converges to the value of $\alpha$, with an initial value of 0.9 , in fewer iterations than the formula used in part c.

#### EXPLORE 6.2

You are going to explore why using rearrangements of equations into the form $x=\mathrm{F}(x)$ sometimes fails.

Possible causes of failure to consider are the starting value and the formula itself.

Discuss why formulae based on:

- $x=\sqrt[5]{1-x} \quad$ (the cobweb pattern)

- $x=\ln (2 x+1)$ (the staircase pattern)

each converged to a root.

Look at the equation $\mathrm{e}^{x}=3 x+1$ and some related graphs.

![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-148_509_404_1399_581.jpg)

![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-148_473_485_1436_1106.jpg)

Discuss the rearrangement $x=\frac{\mathrm{e}^{x}-1}{3}$.

Does this give a convergent iterative formula? Explain your answer.

Look at the equations in Exercise 6B.

Using one of the equations in questions 1 to 5 or 7 to 14, draw the graph of $y=x$ and the graph of a function $\mathrm{F}(x)$, where $x=\mathrm{F}(x)$ is a rearrangement of the equation given and for which $x=\mathrm{F}(x)$ will fail to converge.

Explain any similarities or differences between your example and the rearrangement $x=\frac{\mathrm{e}^{x}-1}{3}$.

## 6.3 Using iterative processes to solve problems involving other areas of mathematics

<a id="ch06-we-6.6"></a>
#### WORKED EXAMPLE 6.6

**a** Show that $\left(\frac{1+\cos x}{2 \sin x}\right)^{2}+\left(\frac{1-\cos x}{2 \sin x}\right)^{2}=\cot ^{2} x+\frac{1}{2}$.

**b** Hence, given that $\alpha$ is a root of the equation $\left(\frac{1+\cos x}{2 \sin x}\right)^{2}+\left(\frac{1-\cos x}{2 \sin x}\right)^{2}=x$, show that $\alpha$ is also a root of the equation $x=\tan ^{-1} \sqrt{\frac{2}{2 x-1}}$ for $0<x<\frac{\pi}{2}$.

**c** It is given that $\alpha$ is the only root of the equation $x=\tan ^{-1} \sqrt{\frac{2}{2 x-1}}$ for $0<x<\frac{\pi}{2}$. Verify by calculation that the value of $\alpha$ lies between 0.9 and 1.0.

**d** Using an iterative formula based on the equation in part c, find the value of $\alpha$ correct to 3 significant figures.

Answer

**a** $\left(\frac{1+\cos x}{2 \sin x}\right)^{2}+\left(\frac{1-\cos x}{2 \sin x}\right)^{2}$ Square.

$$
\begin{align}
& =\frac{1+2 \cos x+\cos ^{2} x}{4 \sin ^{2} x}+\frac{1-2 \cos x+\cos ^{2} x}{4 \sin ^{2} x} \\
& =\frac{2+2 \cos ^{2} x}{4 \sin ^{2} x} \\
& =\frac{1+\cos ^{2} x}{2 \sin ^{2} x} \\
& =\frac{1}{2 \sin ^{2} x}+\frac{\cos ^{2} x}{2 \sin ^{2} x} \\
& =\frac{\operatorname{cosec}^{2} x}{2}+\frac{\cot ^{2} x}{2} \text { Collect terms. } \\
& =\frac{1+\cot ^{2} x}{2}+\frac{\cot ^{2} x}{2} \\
& =\cot ^{2} x+\frac{1}{2}
\end{align}
$$

**b** $\cot ^{2} x+\frac{1}{2}=x$ Rearrange.

$$
\begin{align}
\cot ^{2} x & =x-\frac{1}{2} \\
\cot x & =\sqrt{x-\frac{1}{2}} \\
\frac{1}{\tan x} & =\sqrt{\frac{2 x-1}{2}} \\
\tan x & =\sqrt{\frac{2}{2 x-1}} \\
x & =\tan ^{-1} \sqrt{\frac{2}{2 x-1}}
\end{align}
$$

**c** Let $\mathrm{f}(x)=x-\tan ^{-1} \sqrt{\frac{2}{2 x-1}}$ and so $\mathrm{f}(x)=0$ then:

$$
\begin{align}
& f(0.9)=0.9-\tan ^{-1} \sqrt{\frac{2}{2(0.9)-1}}=-0.10685 \qquad \\
& f(1)=1-\tan ^{-1} \sqrt{\frac{2}{2(1)-1}}=0.44683 \qquad
\end{align}
$$

Change of sign indicates the presence of a root.

| $\boldsymbol{x}_{\mathbf{1}}=\mathbf{0 . 9 5}$ | $\boldsymbol{x}_{\boldsymbol{n}+\mathbf{1}}=\boldsymbol{\operatorname { t a n }}^{-\mathbf{1}} \sqrt{\frac{\mathbf{2}}{\mathbf{2} \boldsymbol{x}_{\boldsymbol{n}}-\mathbf{1}}}$ | Are they the same correct to 3 significant figures? |
| :--- | :--- | :--- |
|  | $x_{2}=\tan ^{-1} \sqrt{\frac{2}{2(0.95)-1}}=0.97992$ | No |
|  | $x_{3}=\tan ^{-1} \sqrt{\frac{2}{2(0.97992 \qquad )-1}}=0.96494$ | No |
|  | $x_{4}=0.97234$ | No |
|  | $x_{5}=0.96866$ | No |
|  | $x_{6}=0.97048$ | No |
|  | $x_{7}=0.96958$ | Yes |

$\alpha$ seems to be 0.970 correct to 3 significant figures.

We can prove this, using a change of sign test:

When $\alpha=0.970$ then $0.9695<\alpha<0.9705$ and so

$$
\begin{align}
& f(0.9695)=0.9695-\tan ^{-1} \sqrt{\frac{2}{2(0.9695)-1}}=-0.000571 \qquad \\
& f(0.9705)=0.9705-\tan ^{-1} \sqrt{\frac{2}{2(0.9705)-1}}=0.000924 \qquad
\end{align}
$$

Change of sign indicates presence of root.

Therefore $\alpha=0.970$ correct to 3 significant figures.

<a id="ch06-we-6.7"></a>
#### WORKED EXAMPLE 6.7

The diagram shows the design of a company logo, $A B C$.

![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-150_372_254_2097_1693.jpg)

$A B$ is an arc of a circle with centre $C$.

The area of the unshaded segment is to be the same as the area of the shaded triangle.

Angle $A C B$ is $\theta$ radians.

**a** Show that $\theta=2 \sin \theta$.

**b** Showing all your working, use an iterative formula based on the equation in part a, with an initial value of 1.85 , to find $\theta$ correct to 3 significant figures.

**c** Hence find the length of $A B$, given that $A C$ is 8 cm.

Answer

**a**

$$
\begin{align}
\frac{1}{2} r^{2} \sin \theta & =\frac{1}{2} r^{2}(\theta-\sin \theta) \\
\sin \theta & =\theta-\sin \theta \\
\theta & =2 \sin \theta
\end{align}
$$

Divide through by $\frac{1}{2} r^{2}$.

Add $\sin \theta$.

✓

**b**

| $\theta_{1}=1.85$ | $\theta_{n+1}=2 \sin \theta_{n}$ | Are they the same correct to 3 significant figures? |
| :--- | :--- | :--- |
|  | $\theta_{2}=2 \sin 1.85=1.92255$ | No |
|  | $\theta_{3}=2 \sin 1.92255 \qquad =1.87753$ | No |
|  | $\theta_{4}=1.90664$ | No |
|  | $\theta_{5}=1.88826$ | No |
|  | $\theta_{6}=1.90005$ | No |
|  | $\theta_{7}=1.89256$ | No |
|  | $\theta_{8}=1.89735$ | No |
|  | $\theta_{9}=1.89430$ | No |
|  | $\theta_{10}=1.89625$ | No |
|  | $\theta_{11}=1.89500$ | Yes |

$\theta$ seems to be 1.90 correct to 3 significant figures.

We can prove this, using a change of sign test with $\mathrm{f}(\theta)=\theta-2 \sin \theta=0$ :

When $\theta=1.90$ then $1.895<\theta<1.905$ and so

$$
\begin{align}
& f(1.895)=1.895-2 \sin 1.895=-0.000809 \qquad \\
& f(1.905)=1.905-2 \sin 1.905=0.01565 \qquad
\end{align}
$$

Change of sign indicates presence of root, therefore $\theta=1.90$ correct to 3 significant figures.

**c** Using trigonometry:

![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-152_440_318_364_320.jpg)

$$
\sin 0.95=\frac{0.5 A B}{8}
$$

$16 \sin 0.95=A B$

$A B=13.014 \qquad =13 \mathrm{~cm}$ (correct to 2 significant figures) Multiply by 16.

<a id="ch06-ex6C"></a>
### EXERCISE 6C

<a id="ch06-ex6C-q1"></a>
##### Question 1
The curve with equation $y=\frac{\mathrm{e}^{2 x}+x}{x^{3}}$ has a stationary point with $x$-coordinate lying between 1 and 2.

**a** Show that the $x$-coordinate of this stationary point satisfies the equation $x=\frac{3}{2}+\frac{x}{\mathrm{e}^{2 x}}$.

**b** Using a suitable iterative process based on the equation given in part a, find the value of the $x$-coordinate of this stationary point correct to 4 decimal places. Give each iteration to 6 decimal places.

<a id="ch06-ex6C-q2"></a>
##### Question 2
The parametric equations of a curve are $x=t^{2}+6, y=t^{4}-t^{3}-5 t$.

The curve has a stationary point for a value of $t$ that lies between 1 and 2.

**a** Show that the value of $t$ at this stationary point satisfies the equation

$$
t=\sqrt[3]{\frac{3 t^{2}+5}{4}}
$$

**b** Use an iterative process based on the equation in part a to find the value of $t$ correct to 3 decimal places. Show the result of each iteration to 6 decimal places.

**c** Hence find the coordinates of the stationary point, giving each coordinate correct to 1 significant figure.

<a id="ch06-ex6C-q3"></a>
##### Question 3
In the diagram, triangle $A B C$ is right-angled and angle $B A C$ is $\theta$ radians. The point $O$ is the mid point of $A C$ and $O C=r$. Angle $B O C$ is $2 \theta$ radians and $B O C$ is a sector of the circle with centre $O$. The area of triangle $A B C$ is 2 times the area of the shaded segment.

**a** Show that $\theta$ satisfies the equation $\sin 2 \theta=\theta$.

**b** This equation has one root in the interval $0<\theta<\frac{\pi}{2}$. Use the iterative formula $\theta_{n+1}=\sin 2 \theta_{n}$ to determine the root correct to 2 decimal places. Give the result of each iteration to 4 decimal places.

![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-152_365_675_2069_1319.jpg)

<a id="ch06-ex6C-q4"></a>
##### Question 4
The diagram shows the curve $y=x^{2} \cos 4 x$ for $0 \leqslant x \leqslant \frac{\pi}{8}$. The point $P$ is a maximum point.

**a** Show that the $x$-coordinate of $P$ satisfies the equation $4 x^{2} \tan 4 x=2 x$.

**b** Show also that the $x$-coordinate of $P$ satisfies the equation $x=\frac{1}{4} \tan ^{-1}\left(\frac{1}{2 x}\right)$.

**c** Using an iterative formula based on the equation in part b with initial value $x_{1}=0.3$ find the $x$-coordinate of $P$ correct to 2 decimal places. Give the result of each iteration to 4 decimal places.

![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-153_576_868_277_1168.jpg)

**d** Use integration by parts twice to find the exact area enclosed between the curve and the $x$-axis from 0 to $\frac{\pi}{8}$.

#### EXPLORE 6.3

The golden ratio

![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-153_271_399_1274_665.jpg)

![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-153_270_426_1277_1159.jpg)

When a rectangle with sides in the ratio $1: \phi(\mathrm{phi})$ can be cut into a square of side 1 and a smaller rectangle, also with sides in the ratio $1: \phi$, the original rectangle is called a golden rectangle and the ratio $1: \phi$ is called the golden ratio.

This means that $\frac{\phi-1}{1}=\frac{1}{\phi}$.

By using a suitable iterative formula based on this ratio, with a starting value of 1, find the value of $\phi$ correct to 5 significant figures.

Explore the link between the golden ratio and the sequence of Fibonacci numbers:

$$
1,1,2,3,5,8, \qquad ,
$$

#### DID YOU KNOW?

The relationship between the Fibonacci numbers and the golden ratio produces the golden spiral.

This can be seen in many natural settings, one of which is the spiralling pattern of the petals in a rose flower.

From a tight centre, petals flow outward in a spiral, growing wider and larger as they do so. Nature has made the best use of an incredible structure. This perfect arrangement of petals is why the small, compact rose bud grows into such a beautiful flower.

![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-153_460_332_2146_1258.jpg)

### Checklist of learning and understanding

- The process of finding a sequence of values that become closer and closer to a point of intersection of $y=x$ and $y=\mathrm{F}(x)$ is called an iterative process.

- Each time you generate a value of $x$ you carry out an iteration.

- When the point of intersection is at $x=\alpha$ and your iterations are values that are getting closer and closer to $\alpha$, you are converging to $\alpha$.

| - Start with $x_{1}$ | work out $\mathrm{F}\left(x_{1}\right)$. | Is it accurate enough? | Yes → Stop, No → |
| :--- | :--- | :--- | :--- |
| - Let $x_{2}=\mathrm{F}\left(x_{1}\right)$ | work out $\mathrm{F}\left(x_{2}\right)$. | Is it accurate enough? | Yes → Stop, No → |
| - Let $x_{3}=\mathrm{F}\left(x_{2}\right)$ | work out $\mathrm{F}\left(x_{3}\right)$. | Is it accurate enough? | Yes → Stop, No → |
| ⋮ |  |  |  |
| - Let $x_{n+1}=\mathrm{F}\left(x_{n}\right)$ | work out $\mathrm{F}\left(x_{n+1}\right)$. | Is it accurate enough? | Yes → Stop. |

- The relationship $x_{n+1}=\mathrm{F}\left(x_{n}\right)$ is called an iterative formula.

- The sequence of values of $x$ given by this formula are called $x_{1}, x_{2}, x_{3}, \qquad , x_{n}$.

- When the value found is accurate enough, then it is usually given a particular name such as $\alpha$.

- The success and speed of the iterative process depends on the function chosen for $\mathrm{F}\left(x_{n}\right)$ and the value chosen for $x_{1}$.

<a id="ch06-review"></a>
### END-OF-CHAPTER REVIEW EXERCISE 6

<a id="ch06-review-q1"></a>
##### Question 1
The terms of the sequence generated by the iterative formula $x_{n+1}=\frac{6}{7}\left(x_{n}+\frac{1}{x_{n}^{3}}\right)$ with initial value $x_{1}=1.5$, converge to $\alpha$.

**a** Use this formula to find $\alpha$ correct to 2 decimal places. Give the result of each iteration to an appropriate number of decimal places. `[3]`

**b** State an equation satisfied by $\alpha$, and hence find the exact value of $\alpha$. `[2]`

<a id="ch06-review-q2"></a>
##### Question 2
The equation $x^{3}+\frac{x}{2}-8=0$ has one real root, denoted by $\alpha$.

**a** Find, by calculation, the pair of consecutive integers between which $\alpha$ lies. `[2]`

**b** Show that, if a sequence of values given by the iterative formula $x_{n+1}=\sqrt{\frac{8}{x_{n}}-\frac{1}{2}}$ converges, then it converges to $\alpha$. `[2]`

**c** Use this iterative formula to determine $\alpha$ correct to 1 decimal place. Give the result of each iteration to 4 decimal places. `[3]`

<a id="ch06-review-q3"></a>
##### Question 3
**a** By sketching a suitable pair of graphs, show that the equation $\mathrm{e}^{2 x+1}=14-x^{3}$ has exactly one real root. `[3]`

**b** Show by calculation that this root lies between 0.5 and 1. `[2]`

**c** Show that this root also satisfies the equation $x=\frac{\ln \left(14-x^{3}\right)-1}{2}$. `[1]`

**d** Use an iteration process based on the equation in part c, with a suitable starting value, to find the root correct to 4 decimal places. Give the result of each step of the process to 6 decimal places. `[3]`

<a id="ch06-review-q4"></a>
##### Question 4
The sequence of values given by the iterative formula $x_{n+1}=\frac{x_{n}\left(1+\sec ^{2} x_{n}\right)-\tan x_{n}}{\sec ^{2} x_{n}-1}$ with initial value $x_{1}=1$, converges to $\alpha$.

**a** Use this formula to find $\alpha$ correct to 2 decimal places, showing the result of each iteration to 4 decimal places. `[3]`

**b** Show that $\alpha$ also satisfies the equation $\tan x-2 x=0$ where $1 \leqslant x<\frac{\pi}{2}$. `[2]`

<a id="ch06-review-q5"></a>
##### Question 5
The equation $\frac{\ln x^{2}-6}{2}=x-5$ has a root $\alpha$, such that $p<\alpha<q$, where $p$ and $q$ are consecutive integers.

**a** Show that $\alpha$ also satisfies the equation $x=\ln x+2$. `[1]`

**b** Find the value of $p$ and the value of $q$. `[2]`

**c** Use the iterative formula based on the equation in part a with starting value $x=p$, to find the value of $\alpha$ correct to 3 decimal places. `[3]`

**d** Hence find an approximate value of $y$ that satisfies the equation $5^{y}-2=y \ln 5$. `[2]`

<a id="ch06-review-q6"></a>
##### Question 6
**a** By sketching a suitable pair of graphs, show that the equation $7-x^{6}=\left|x^{2}-1\right|$ has exactly two real roots, $\alpha$ and $\beta$, where $\alpha$ is a positive constant. `[3]`

**b** Show that $\alpha$ satisfies the equation $x=\sqrt[5]{\frac{8}{x}-x}$. `[1]`

**c** Write down an iterative formula based on the equation in part a. Use this formula, with a suitable starting value, to find the value of $\alpha$ correct to 3 significant figures. Give the result of each iteration to 5 significant figures. `[3]`

**d** Hence write down the value of $\beta$ correct to 3 significant figures. `[1]`

<a id="ch06-review-q7"></a>
##### Question 7
It is given that $\int_{0}^{a}\left(\frac{1}{3 x+5}+2 \mathrm{e}^{6 x}\right) \mathrm{d} x=0.6$, where the constant $a>0$.

**a** Show that $a=\frac{1}{6} \ln \left(2.8+\ln \left(\frac{5}{3 a+5}\right)\right)$. `[4]`

**b** Use an iterative formula based on the equation in part a, with a starting value of $a=0.2$, to find the value of $a$ correct to 3 decimal places. Give the result of each iteration to an appropriate number of decimal places. `[3]`

<a id="ch06-review-q8"></a>
##### Question 8
A curve has parametric equations

$$
x=\frac{1}{t}, y=\sqrt{t+1}
$$

The point $P$ on the curve has parameter $p$. It is given that the gradient of the curve at $P$ is -0.4 .

**a** Show that $p=\frac{2 \sqrt{5}}{5}(p+1)^{\frac{1}{4}}$. `[3]`

**b** Use an iterative process based on the equation in part a to find the value of $p$ correct to 3 decimal places. Use a starting value of 1 and show the result of each iteration to 5 decimal places. `[3]`

<a id="ch06-review-q9"></a>
##### Question 9
In the diagram, $A, B$ and $C$ are points on the circumference of the circle with centre

![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-156_320_297_1193_1633.jpg)

$O$ and radius $r$. The shaded region, $A B C$, is a sector of the circle with centre $C$. Angle $O C A$ is equal to $\theta$ radians.

The area of the shaded region is equal to $\frac{3}{8}$ of the area of the circle.

**a** Show that $\theta=\cos ^{-1} \sqrt{\frac{3 \pi}{32 \theta}}$.

**b** Verify by calculation that $\theta$ lies between 0.8 and 1.2 radians. `[2]`

**c** Use the iterative formula $\theta_{n+1}=\cos ^{-1} \sqrt{\frac{3 \pi}{32 \theta_{n}}}$ to find the value of $\theta$ correct to 3 decimal places.

Give the result of each iteration to 5 decimal places. `[3]`

<a id="ch06-review-q10"></a>
##### Question 10
The functions f and g are defined, for $0 \leqslant x \leqslant \pi$, by $\mathrm{f}(x)=\mathrm{e}^{x-2}$ and

![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-156_471_535_1728_1386.jpg)

[4]

b Show that $q$ satisfies the equation $q=2+\ln (\sin q)$. `[1]`

c Given also that $1.5<q<2.5$, use the iterative formula $q_{n+1}=2+\ln \left(\sin q_{n}\right)$ to calculate $q$ correct to 2 decimal places, showing the result of each iteration to 4 decimal places. `[3]`

<a id="ch06-review-q11"></a>
##### Question 11
The equation $x=\cos x+\sin x$ has a root $\alpha$ that lies between 1 and 1.4.

**a** Show that $\alpha$ is also a root of the equation $x=\sqrt{2} \cos \left(x-\frac{\pi}{4}\right)$. `[3]`

**b** Using the iterative formula $x_{n+1}=\sqrt{2} \cos \left(x_{n}-\frac{\pi}{4}\right)$, find the value of $\alpha$, giving your answer correct to 2 decimal places. `[3]`

<a id="ch06-review-q12"></a>
##### Question 12
**a** By sketching each of the graphs of $y=\sec x$ and $y=\left(\frac{\pi}{2}-x\right)\left(\frac{\pi}{4}+x\right)$ for $-\frac{\pi}{2}<x \leqslant \frac{\pi}{2}$ on the same diagram, show that the equation $\sec x=\left(\frac{\pi}{2}-x\right)\left(\frac{\pi}{4}+x\right)$ has exactly two real roots in the interval $-\frac{\pi}{2}<x \leqslant \frac{\pi}{2}$. `[3]`

**b** Show that the equation $\sec x=\left(\frac{\pi}{2}-x\right)\left(\frac{\pi}{4}+x\right)$ can be written in the form

$$
x=\sqrt{\frac{2 \pi x+\pi^{2}-8 \sec x}{8}} .
$$

[1]

**c** The two real roots of the equation $\sec x=\left(\frac{\pi}{2}-x\right)\left(\frac{\pi}{4}+x\right)$ in the interval $-\frac{\pi}{2}<x \leqslant \frac{\pi}{2}$ are denoted $\alpha$ and $\beta$.

Verify by calculation that the smaller root, $\alpha$, is -0.21 correct to 2 decimal places. `[2]`

**d** Using an iterative formula based on the equation given in part b, with an initial value of 1, find the value of $\beta$ correct to 2 decimal places. Give the result of each iteration to 4 decimal places. `[3]`

#### FAST FORWARD

You need to have studied the skills in Chapter 8 before attempting questions 13 and 14.

**13** ![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-157_517_909_1386_752.jpg) The diagram shows part of the curve $y=\cos ^{3} x$, where $x$ is in radians. The shaded region between the curve, the axes and the line $x=\alpha$ is denoted by $R$. The area of $R$ is equal to 0.3.

**a** Using the substitution $u=\sin x$, find $\int_{0}^{\alpha} \cos ^{3} x \mathrm{~d} x$. Hence show that $\sin \alpha=\frac{0.9}{3-\sin ^{2} \alpha}$. `[6]`

**b** Use the iterative formula $\alpha_{n+1}=\sin ^{-1}\left(\frac{0.9}{3-\sin ^{2} \alpha_{n}}\right)$ with $\alpha_{1}=0.2$, to find the value of $\alpha$ correct to 3 significant figures. Give the result of each iteration to 5 significant figures. `[3]`

**14** It is given that $\int_{1}^{a} \ln x \mathrm{~d} x=5$, where $a$ is a constant greater than 1.

**a** Show that $a=\frac{4+a}{\ln a}$. `[5]`

**b** Use an iterative formula based on the equation in part a to find the value of $a$ correct to 3 decimal places. Use an initial value of 5 and give the result of each iteration to 5 decimal places. `[3]`

<a id="ch06-cross"></a>
### CROSS-TOPIC REVIEW EXERCISE 2

<a id="ch06-cross-q1"></a>
##### Question 1
The equation of a curve is $y=\frac{1+x}{1+2 x}$ for $x>-\frac{1}{2}$. Show that the gradient of the curve is always negative. `[3]`

*Cambridge International A Level Mathematics 9709 Paper 31 Q1 November 2013*

<a id="ch06-cross-q2"></a>
##### Question 2
![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-158_720_761_598_765.jpg) The diagram shows the part of the curve $y=\frac{1}{2} \tan 2 x$ for $0 \leqslant x \leqslant \frac{1}{2} \pi$. Find the $x$-coordinates of the points on this part of the curve at which the gradient is 4 . `[5]`

*Cambridge International AS \& A Level Mathematics 9709 Paper 21 Q3 November 2011*

<a id="ch06-cross-q3"></a>
##### Question 3
The parametric equations of a curve are $x=\ln (1-2 t), y=\frac{2}{t}$, for $t<0$.

**i** Show that $\frac{\mathrm{d} y}{\mathrm{~d} x}=\frac{1-2 t}{t^{2}}$. `[3]`

**ii** Find the exact coordinates of the only point on the curve at which the gradient is 3. `[3]`

*Cambridge International AS \& A Level Mathematics 9709 Paper 21 Q4 November 2012*

<a id="ch06-cross-q4"></a>
##### Question 4
The equation of a curve is $x^{2} y+y^{2}=6 x$.

**i** Show that $\frac{\mathrm{d} y}{\mathrm{~d} x}=\frac{6-2 x y}{x^{2}+2 y}$. `[4]`

**ii** Find the equation of the tangent to the curve at the point with coordinates (1, 2), giving your answer in the form $a x+b y+c=0$. `[3]`

*Cambridge International AS \& A Level Mathematics 9709 Paper 21 Q6 June 2010*

<a id="ch06-cross-q5"></a>
##### Question 5
**i** Use the trapezium rule with two intervals to estimate the value of $\int_{0}^{1} \frac{1}{6+2 \mathrm{e}^{x}} \mathrm{~d} x$, giving your answer correct to 2 decimal places. `[3]`

**ii** Find $\int \frac{\left(\mathrm{e}^{x}-2\right)^{2}}{\mathrm{e}^{2 x}} \mathrm{~d} x$. `[4]`

*Cambridge International AS \& A Level Mathematics 9709 Paper 21 Q6 November 2012*

<a id="ch06-cross-q6"></a>
##### Question 6
**i** By sketching a suitable pair of graphs, show that the equation $\ln x=4-\frac{1}{2} x$ has exactly one real root, $\alpha$. `[2]`

**ii** Verify by calculation that $4.5<\alpha<5.0$. `[2]`

**iii** Use an iterative formula $x_{n+1}=8-2 \ln x_{n}$ to find $\alpha$ correct to 2 decimal places. Give the result of each iteration to 4 decimal places. `[3]`

*Cambridge International AS \& A Level Mathematics 9709 Paper 21 Q4 November 2015*

<a id="ch06-cross-q7"></a>
##### Question 7
The parametric equations of a curve are $x=\frac{1}{\cos ^{3} t}, y=\tan ^{3} t$, where $0 \leqslant t<\frac{1}{2} \pi$.

**i** Show that $\frac{\mathrm{d} y}{\mathrm{~d} x}=\sin t$. `[4]`

**ii** Hence show that the equation of the tangent to the curve at the point with parameter $t$ is $y=x \sin t-\tan t$. `[3]`

*Cambridge International A Level Mathematics 9709 Paper 31 Q4 November 2014*

<a id="ch06-cross-q8"></a>
##### Question 8
It is given that the positive constant $a$ is such that $\int_{-a}^{a}\left(4 \mathrm{e}^{2 x}+5\right) \mathrm{d} x=100$.

**i** Show that $a=\frac{1}{2} \ln \left(50+\mathrm{e}^{-2 a}-5 a\right)$. `[4]`

**ii** Use the iterative formula $a_{n+1}=\frac{1}{2} \ln \left(50+\mathrm{e}^{-2 a_{n}}-5 a_{n}\right)$ to find $\alpha$ correct to 3 decimal places. Give the result of each iteration to 5 decimal places. `[3]`

*Cambridge International AS \& A Level Mathematics 9709 Paper 21 Q4 November 2016*

<a id="ch06-cross-q9"></a>
##### Question 9
The equation of a curve is $y=\mathrm{e}^{-2 x} \tan x$, for $0 \leqslant x<\frac{1}{2} \pi$.

**i** Obtain an expression for $\frac{\mathrm{d} y}{\mathrm{~d} x}$ and show that it can be written in the form $\mathrm{e}^{-2 x}(a+b \tan x)^{2}$, where $a$ and $b$ are constants. `[5]`

**ii** Explain why the gradient of the curve is never negative. `[1]`

**iii** Find the value of $x$ for which the gradient is least. `[1]`

*Cambridge International A Level Mathematics 9709 Paper 31 Q5 November 2015*

<a id="ch06-cross-q10"></a>
##### Question 10
**i** Prove that $\tan \theta+\cot \theta \equiv \frac{2}{\sin 2 \theta}$. `[3]`

**ii** Hence

a find the exact value of $\tan \frac{1}{8} \pi+\cot \frac{1}{8} \pi$, `[2]`

b evaluate $\int_{0}^{\frac{1}{2} \pi} \frac{6}{\tan \theta+\cot \theta} \mathrm{d} \theta$. `[3]`

*Cambridge International AS \& A Level Mathematics 9709 Paper 21 Q5 June 2014*

<a id="ch06-cross-q11"></a>
##### Question 11
The equation of a curve is $x y(x-6 y)=9 a^{3}$, where $a$ is a non-zero constant. Show that there is only one point on the curve at which the tangent is parallel to the $x$-axis, and find the coordinates of this point. `[7]`

*Cambridge International A Level Mathematics 9709 Paper 31 Q4 November 2016*

<a id="ch06-cross-q12"></a>
##### Question 12
The curve with equation $y=\frac{6}{x^{2}}$ intersects the line $y=x+1$ at the point $P$.

**i** Verify by calculation that the $x$-coordinate of $P$ lies between 1.4 and 1.6. `[2]`

**ii** Show that the $x$-coordinate of $P$ satisfies the equation $x=\sqrt{\left(\frac{6}{x+1}\right)}$. `[2]`

**iii** Use the iterative formula $x_{n+1}=\sqrt{\left(\frac{6}{x_{n}+1}\right)}$, with initial value $x_{1}=1.5$, to determine the $x$-coordinate of $P$ correct to 2 decimal places. Give the result of each iteration to 4 decimal places. `[3]`

*Cambridge International AS \& A Level Mathematics 9709 Paper 21 Q6 November 2010*

<a id="ch06-cross-q13"></a>
##### Question 13
The parametric equations of a curve are $x=\mathrm{e}^{2 t}, y=4 t \mathrm{e}^{t}$.

**i** Show that $\frac{\mathrm{d} y}{\mathrm{~d} x}=\frac{2(t+1)}{\mathrm{e}^{t}}$. `[4]`

**ii** Find the equation of the normal to the curve at the point where $t=0$. `[4]`

*Cambridge International AS \& A Level Mathematics 9709 Paper 21 Q5 June 2013*

<a id="ch06-cross-q14"></a>
##### Question 14
For each of the following curves, find the exact gradient at the point indicated:

**i** $y=3 \cos 2 x-5 \sin x$ at $\left(\frac{1}{6} \pi,-1\right)$, `[3]`

**ii** $\quad x^{3}+6 x y+y^{3}=21$ at (1, 2). `[5]`

*Cambridge International AS \& A Level Mathematics 9709 Paper 21 Q4 November 2014*

<a id="ch06-cross-q15"></a>
##### Question 15
**i** By differentiating $\frac{1}{\cos x}$, show that if $y=\sec x$ then $\frac{\mathrm{d} y}{\mathrm{~d} x}=\sec x \tan x$.

**ii** Show that $\frac{1}{\sec x-\tan x} \equiv \sec x+\tan x$. `[1]`

**iii** Deduce that $\frac{1}{(\sec x-\tan x)^{2}} \equiv 2 \sec ^{2} x-1+2 \sec x \tan x$. `[2]`

**iv** Hence show that $\int_{0}^{\frac{1}{4} \pi} \frac{1}{(\sec x-\tan x)^{2}} \mathrm{~d} x=\frac{1}{4}(8 \sqrt{2}-\pi)$. `[3]`

*Cambridge International A Level Mathematics 9709 Paper 31 Q5 November 2012*

<a id="ch06-cross-q16"></a>
##### Question 16
A curve is defined by the parametric equations $x=2 \tan \theta, y=3 \sin 2 \theta$, for $0 \leqslant \theta<\frac{1}{2} \pi$.

**i** Show that $\frac{\mathrm{d} y}{\mathrm{~d} x}=6 \cos ^{4} \theta-3 \cos ^{2} \theta$. `[4]`

**ii** Find the coordinates of the stationary point. `[3]`

**iii** Find the gradient of the curve at the point $\left(2 \sqrt{3}, \frac{3}{2} \sqrt{3}\right)$. `[2]`

*Cambridge International AS \& A Level Mathematics 9709 Paper 21 Q5 June 2016*

<a id="ch06-cross-q17"></a>
##### Question 17
![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-161_615_916_389_728.jpg) The diagram shows the curve $y=4 \mathrm{e}^{\frac{1}{2} x}-6 x+3$ and its minimum point $M$.

**i** Show that the $x$-coordinate of $M$ can be written in the form $\ln a$, where the value of $a$ is to be stated.

**ii** Find the exact value of the area of the region enclosed by the curve and the lines $x=0, x=2$ and $y=0$.

*Cambridge International AS \& A Level Mathematics 9709 Paper 21 Q5 June 2012*

<a id="ch06-cross-q18"></a>
##### Question 18
The equation of a curve is $x^{3}-3 x^{2} y+y^{3}=3$.

**i** Show that $\frac{\mathrm{d} y}{\mathrm{~d} x}=\frac{x^{2}-2 x y}{x^{2}-y^{2}}$. `[4]`

**ii** Find the coordinates of the points on the curve where the tangent is parallel to the $x$-axis. `[5]`

*Cambridge International A Level Mathematics 9709 Paper 31 Q7 June 2016*

<a id="ch06-cross-q19"></a>
##### Question 19
A curve has parametric equations $x=\frac{1}{(2 t+1)^{2}}, y=\sqrt{(t+2)}$

The point $P$ on the curve has parameter $p$ and it is given that the gradient of the curve at $P$ is -1.

**i** Show that $p=(p+2)^{\frac{1}{6}}-\frac{1}{2}$. `[6]`

**ii** Use an iterative process based on the equation in part i to find the value of $p$ correct to 3 decimal places. Use a starting value of 0.7 and show the result of each iteration to 5 decimal places. `[3]`

*Cambridge International AS \& A Level Mathematics 9709 Paper 21 Q6 June 2012*

<a id="ch06-cross-q20"></a>
##### Question 20
**i** Find

**a** $\int \frac{\mathrm{e}^{2 x}+6}{\mathrm{e}^{2 x}} \mathrm{~d} x$,

**b** $\int 3 \cos ^{2} x \mathrm{~d} x$.

ii Use the trapezium rule with 2 intervals to estimate the value of $\int_{1}^{2} \frac{6}{\ln (x+2)} \mathrm{d} x$, giving your answer correct to 2 decimal places. `[3]`

*Cambridge International AS \& A Level Mathematics 9709 Paper 21 Q6 November 2013*

<a id="ch06-cross-q21"></a>
##### Question 21
**i** By sketching a suitable pair of graphs, show that the equation $\mathrm{e}^{2 x}=14-x^{2}$ has exactly two real roots. `[3]`

**ii** Show by calculation that the positive root lies between 1.2 and 1.3. `[2]`

**iii** Show that this root also satisfies the equation $x=\frac{1}{2} \ln \left(14-x^{2}\right)$. `[1]`

**iv** Use an iteration process based on the equation in part iii, with a suitable starting value, to find the root correct to 2 decimal places. Give the result of each step of the process to 4 decimal places. `[3]`

*Cambridge International AS \& A Level Mathematics 9709 Paper 21 Q7 June 2011*

<a id="ch06-cross-q22"></a>
##### Question 22
**i** By sketching each of the graphs $y=\operatorname{cosec} x$ and $y=x(\pi-x)$ for $0<x<\pi$, show that the equation $\operatorname{cosec} x=x(\pi-x)$ has exactly two real roots in the interval for $0<x<\pi$. `[3]`

**ii** Show that the equation $\operatorname{cosec} x=x(\pi-x)$ can be written in the form $x=\frac{1+x^{2} \sin x}{\pi \sin x}$. `[2]`

**iii** The two real roots of the equation $\operatorname{cosec} x=x(\pi-x)$ in the interval $0<x<\pi$ are denoted by $\alpha$ and $\beta$, where $\alpha<\beta$.

**a** Use the iterative formula $x_{n+1}=\frac{1+x_{n}^{2} \sin x_{n}}{\pi \sin x_{n}}$ to find $\alpha$ correct to 2 decimal places. Give the result of each iteration to 4 decimal places. `[3]`

**b** Deduce the value of $\beta$ correct to 2 decimal places. `[1]`

*Cambridge International A Level Mathematics 9709 Paper 31 Q8 June 2014*

<a id="ch06-cross-q23"></a>
##### Question 23
![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-162_514_513_1439_887.jpg) The diagram shows part of the curve with parametric equations

$$
x=2 \ln (t+2), y=t^{3}+2 t+3 .
$$

**i** Find the gradient of the curve at the origin. `[5]`

**ii** At the point $P$ on the curve, the value of the parameter is $p$. It is given that the gradient of the curve at $P$ is $\frac{1}{2}$.

**a** Show that $p=\frac{1}{3 p^{2}+2}-2$. `[1]`

**b** By first using an iterative formula based on the equation in part a, determine the coordinates of the point $P$. Give the result of each iteration to 5 decimal places and each coordinate of $P$ correct to 2 decimal places. `[4]`

*Cambridge International A Level Mathematics 9709 Paper 31 Q10 June 2015*

<a id="ch06-cross-q24"></a>
##### Question 24
**i** Prove that $2 \operatorname{cosec} 2 \theta \tan \theta \equiv \sec ^{2} \theta$. `[3]`

**ii** Hence

a solve the equation $2 \operatorname{cosec} 2 \theta \tan \theta=5$ for $0<x<\pi$. `[3]`

b find the exact value of $\int_{0}^{\frac{1}{6} \pi} 2 \operatorname{cosec} 4 x \tan 2 x \mathrm{~d} x$. `[4]`

*Cambridge International AS \& A Level Mathematics 9709 Paper 21 Q6 June 2015*

<a id="ch06-cross-q25"></a>
##### Question 25
**i** Prove the identity $\cos 4 \theta+4 \cos 2 \theta \equiv 8 \cos ^{4} \theta-3$. `[4]`

**ii** Hence

a solve the equation $\cos 4 \theta+4 \cos 2 \theta=1$ for $-\frac{1}{2} \pi \leqslant \theta \leqslant \frac{1}{2} \pi$. `[3]`

b find the exact value of $\int_{0}^{\frac{1}{4} \pi} \cos ^{4} \theta \mathrm{~d} \theta$. `[3]`

*Cambridge International A Level Mathematics 9709 Paper 31 Q9 June 2011*

<a id="ch06-cross-q26"></a>
##### Question 26
**i** By first expanding $\cos (2 x+x)$, show that $\cos 3 x=4 \cos ^{3} x-3 \cos x$. `[5]`

**ii** Hence show that $\int_{0}^{\frac{1}{6} \pi}\left(2 \cos ^{3} x-\cos x\right) \mathrm{d} x=\frac{5}{12}$. `[5]`

*Cambridge International AS \& A Level Mathematics 9709 Paper 21 Q8 November 2011*

<a id="ch06-cross-q27"></a>
##### Question 27
![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-163_459_916_1625_731.jpg) The diagram shows the curve $y=10 \mathrm{e}^{-\frac{1}{2} x} \sin 4 x$ for $x \geqslant 0$. The stationary points are labeled $T_{1}, T_{2}, T_{3},$ as shown.

**i** Find the $x$-coordinates of $T_{1}$ and $T_{2}$, giving each $x$-coordinate correct to 3 decimal places. `[6]`

**ii** It is given that the $x$-coordinate of $T_{n}$ is greater than 25. Find the least possible value of $n$. `[4]`

*Cambridge International A Level Mathematics 9709 Paper 31 Q10 June 2014*

<a id="ch06-cross-q28"></a>
##### Question 28
The equation of a curve is $y=\frac{3 x^{2}}{x^{2}+4}$. At the point on the curve with positive $x$-coordinate $p$, the gradient of the curve is $\frac{1}{2}$.

**i** Show that $p=\sqrt{\left(\frac{48 p-16}{p^{2}+8}\right)}$. `[5]`

**ii** Show by calculation that $2<p<3$. `[2]`

**iii** Use an iterative formula based on the equation in part i to find the value of $p$ correct to 4 significant figures. Give the result of each iteration to 6 significant figures. `[3]`

*Cambridge International AS \& A Level Mathematics 9709 Paper 21 Q6 June 2016*

<a id="ch06-cross-q29"></a>
##### Question 29
**i** By differentiating $\frac{1}{\cos \theta}$, show that if $y=\sec \theta$ then $\frac{\mathrm{d} y}{\mathrm{~d} \theta}=\tan \theta \sec \theta$. `[3]`

**ii** Hence show that $\frac{\mathrm{d}^{2} y}{\mathrm{~d} \theta^{2}}=a \sec ^{3} \theta+b \sec \theta$, giving the values of $a$ and $b$. `[4]`

**iii** Find the exact value of $\int_{0}^{\frac{1}{4} \pi}\left(1+\tan ^{2} \theta-3 \sec \theta \tan \theta\right) \mathrm{d} \theta$. `[5]`

*Cambridge International AS \& A Level Mathematics 9709 Paper 21 Q8 November 2012*

![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-165_1344_1941_3_134.jpg)
