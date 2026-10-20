# Chapter 3: Trigonometry


In this chapter you will learn how to:

- understand the relationship of the secant, cosecant and cotangent functions to cosine, sine and tangent, and use properties and graphs of all six trigonometric functions for angles of any magnitude

- use trigonometrical identities for the simplification and exact evaluation of expressions and in the course of solving equations, and select an identity or identities appropriate to the context, showing familiarity in particular with the use of:

- $\sec ^{2} \theta=1+\tan ^{2} \theta$ and $\operatorname{cosec}^{2} \theta=1+\cot ^{2} \theta$

- the expansion of $\sin (A \pm B), \cos (A \pm B)$ and $\tan (A \pm B)$

- the formulae for $\sin 2 A, \cos 2 A$ and $\tan 2 A$

- the expression of $a \sin \theta+b \cos \theta$ in the forms $R \sin (\theta \pm \alpha)$ and $R \cos (\theta \pm \alpha)$.

<a id="ch03-prerequisite"></a>
### PREREQUISITE KNOWLEDGE

| Where it comes from | What you should be able to do | Check your skills |
| :--- | :--- | :--- |
| Pure Mathematics 1 Coursebook, Chapter 5 | Sketch graphs of the sine, cosine and tangent functions. | 1 Sketch the graphs of these functions for $0^{\circ} \leqslant x \leqslant 360^{\circ}$.<br>a $y=2 \sin x+1$<br>b $y=\tan \left(x-90^{\circ}\right)$<br>c $y=\cos \left(2 x+90^{\circ}\right)$<br> |
| Pure Mathematics 1 Coursebook, Chapter 5 | Find exact values of the sine, cosine and tangent of 30°, 45° and 60° and related angles. | 2 Find the exact values of:<br>a $\sin 120^{\circ}$<br>b $\cos 225^{\circ}$<br>c $\tan 150^{\circ}$<br> |
| Pure Mathematics 1 Coursebook, Chapter 5 | Solve trigonometric equations using the identities $\tan \theta \equiv \frac{\sin \theta}{\cos \theta}$ and $\sin ^{2} \theta+\cos ^{2} \theta \equiv 1$. | 3 Solve for $0^{\circ} \leqslant x \leqslant 360^{\circ}$.<br>a $5 \sin x=3 \cos x$<br>b $2 \cos ^{2} x-\sin x=1$<br> |

### Why do we study trigonometry?

In addition to the three main trigonometrical functions (sine, cosine and tangent) there are three more commonly used trigonometrical functions (cosecant, secant and cotangent) that we will learn about. These are sometimes referred to as the reciprocal trigonometrical functions.

We will also learn about the compound angle formulae, which form a basis for numerous important mathematical techniques. These techniques include solving equations, deriving further trigonometric identities, the addition of different sine and cosine functions and deriving rules for differentiating and integrating trigonometric functions, which we will cover later in this book.

As you know, scientists and engineers represent oscillations and waves using trigonometric functions. These functions also have further uses in navigation, engineering and physics.

## 3.1 The cosecant, secant and cotangent ratios

There are a total of six trigonometric ratios. You have already learnt about the ratios sine, cosine and tangent. In this section you will learn about the other three ratios, which are cosecant (cosec), secant (sec) and cotangent (cot).

<a id="ch03-kp-3.1"></a>
#### KEY POINT 3.1

The three reciprocal trigonometric ratios are defined as:

$$
\operatorname{cosec} \theta=\frac{1}{\sin \theta} \quad \sec \theta=\frac{1}{\cos \theta} \quad \cot \theta=\frac{1}{\tan \theta}\left(=\frac{\cos \theta}{\sin \theta}\right)
$$

Consider the right-angled triangle:

![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-053_224_330_2421_1060.jpg)

$$
\begin{array}{rlrl} \sin \theta & =\frac{y}{r} & \cos \theta & =\frac{x}{r} \\
\operatorname{cosec} \theta & =\frac{r}{y} & \sec \theta & =\frac{r}{x} \\
\cot \theta & =\frac{x}{y} \end{array}
$$

The following identities can be found from this triangle:

$$
\begin{align}
x^{2}+y^{2} & =r^{2} & & \text { Divide both sides by } x^{2} . \\
1+\left(\frac{y}{x}\right)^{2} & =\left(\frac{r}{x}\right)^{2} & & \text { Use } \frac{y}{x}=\tan \theta \text { and } \frac{r}{x}=\sec \theta . \\
1+\tan ^{2} \theta & \equiv \sec ^{2} \theta & &
\end{align}
$$

$$
\begin{array}{rlrl} x^{2}+y^{2} & =r^{2} & & \text { Divide both sides by } y^{2} . \\
\left(\frac{x}{y}\right)^{2}+1 & =\left(\frac{r}{y}\right)^{2} & \text { Use } \frac{x}{y}=\cot \theta \text { and } \frac{r}{y}=\operatorname{cosec} \theta . \\
\cot ^{2} \theta+1 & \equiv \operatorname{cosec}^{2} \theta & & \end{array}
$$

We will need these important identities to solve trigonometric equations later in this section.

<a id="ch03-kp-3.2"></a>
#### KEY POINT 3.2

$$
\begin{align}
& 1+\tan ^{2} \theta \equiv \sec ^{2} \theta \\
& \cot ^{2} \theta+1 \equiv \operatorname{cosec}^{2} \theta
\end{align}
$$

The graphs of $y=\sin \theta$ and $y=\operatorname{cosec} \theta$

![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-054_249_924_1444_181.jpg)

![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-054_563_700_1287_1294.jpg)

The function $y=\operatorname{cosec} \theta$ is the reciprocal of the function $y=\sin \theta$.

The function $y=\sin \theta$ is zero when $\theta=0^{\circ}, 180^{\circ}, 360^{\circ},$, this means that $y=\operatorname{cosec} \theta$ is not defined at each of these points because $\frac{1}{0}$ is not defined. Hence vertical asymptotes need to be drawn at each of these points.

The graphs of $\boldsymbol{y}=\boldsymbol{\operatorname { c o s }} \boldsymbol{\theta}$ and $\boldsymbol{y}=\boldsymbol{\operatorname { s e c }} \boldsymbol{\theta}$ We can find the graph of $y=\sec \theta$ in a similar way from the graph of $y=\cos \theta$.

![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-055_266_944_562_218.jpg)

![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-055_564_698_421_1328.jpg)

The graphs of $\boldsymbol{y}=\boldsymbol{\operatorname { t a n }} \boldsymbol{\theta}$ and $\boldsymbol{y}=\boldsymbol{\operatorname { c o t }} \boldsymbol{\theta}$ We can find the graph of $y=\cot \theta$ from the graph of $y=\tan \theta$.

![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-055_426_706_1173_222.jpg)

![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-055_422_697_1178_1326.jpg)

<a id="ch03-we-3.1"></a>
#### WORKED EXAMPLE 3.1

Find the exact value of $\operatorname{cosec} 240^{\circ}$.

Answer

$$
\begin{align}
\operatorname{cosec} 240^{\circ} & =\frac{1}{\sin 240^{\circ}} \\
& =\frac{1}{-\sin 60^{\circ}} \\
& =\frac{1}{-\frac{\sqrt{3}}{2}} \\
& =-\frac{2}{\sqrt{3}}
\end{align}
$$

![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-055_338_351_1921_1247.jpg)

<a id="ch03-we-3.2"></a>
#### WORKED EXAMPLE 3.2

Solve $\sec ^{2} x-\tan x-3=0$ for $0^{\circ} \leqslant x \leqslant 360^{\circ}$.

Answer

$$
\begin{align}
\sec ^{2} x-\tan x-3 & =0 \\
\tan x^{2} x-\tan x-2 & =0 \\
(\tan x-2)(\tan x+1) & =0 \\
\tan x=2 \text { or } \tan x & =-1 \\
\tan x=2 \Rightarrow x & =63.4^{\circ}(\text { calculator }) \\
\text { or } x & =63.4^{\circ}+180^{\circ}=243.4^{\circ} \\
\tan x=-1 \Rightarrow x & =-45^{\circ}(\text { not in required range }) \\
\text { or } x & =-45^{\circ}+180^{\circ}=135^{\circ} \\
\text { or } x & =135^{\circ}+180^{\circ}=315^{\circ}
\end{align}
$$

The values of $x$ are 63.4°, 135°, 243.4°, 315°.

Use $1+\tan ^{2} x \equiv \sec ^{2} x$.

Factorise.

![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-056_473_935_695_1042.jpg)

<a id="ch03-ex3A"></a>
### EXERCISE 3A

<a id="ch03-ex3A-q1"></a>
##### Question 1
Find the exact values of:

**a** $\sec 60^{\circ}$

**b** $\operatorname{cosec} 45^{\circ}$

**c** $\cot 120^{\circ}$

**d** $\sec 300^{\circ}$

**e** $\operatorname{cosec} 135^{\circ}$

**f** $\cot 330^{\circ}$

**g** $\sec 150^{\circ}$

**h** $\cot \left(-30^{\circ}\right)$.

<a id="ch03-ex3A-q2"></a>
##### Question 2
Find the exact values of:

**a** $\operatorname{cosec} \frac{\pi}{6}$

**b** $\cot \frac{\pi}{3}$

**c** $\sec \frac{\pi}{4}$

**d** $\cot \frac{2 \pi}{3}$

**e** $\sec \frac{5 \pi}{6}$

**f** $\operatorname{cosec} \frac{7 \pi}{4}$

**g** $\cot \frac{4 \pi}{3}$

**h** $\sec \left(-\frac{\pi}{6}\right)$.

<a id="ch03-ex3A-q3"></a>
##### Question 3
Solve each equation for $0^{\circ} \leqslant x \leqslant 360^{\circ}$.

**a** $\sec x=3$

**b** $\cot x=0.8$

**c** $\operatorname{cosec} x=-3$

**d** $3 \sec x-4=0$

<a id="ch03-ex3A-q4"></a>
##### Question 4
Solve each equation for $0 \leqslant x \leqslant 2 \pi$.

**a** $\operatorname{cosec} x=2$

**b** $\sec x=-1$

**c** $\cot x=2$

**d** $2 \cot x+5=0$

<a id="ch03-ex3A-q5"></a>
##### Question 5
Solve each equation for $0^{\circ} \leqslant x \leqslant 180^{\circ}$.

**a** $\operatorname{cosec} 2 x=1.2$

**b** $\sec 2 x=4$

**c** $\cot 2 x=1$

**d** $2 \sec 2 x=3$

<a id="ch03-ex3A-q6"></a>
##### Question 6
Solve each equation for the given domains.

**a** $\operatorname{cosec}\left(x-30^{\circ}\right)=2$ for $0^{\circ} \leqslant x \leqslant 360^{\circ}$

**b** $\sec \left(2 x+60^{\circ}\right)=-1.5$ for $0^{\circ} \leqslant x \leqslant 180^{\circ}$

**c** $\cot \left(x+\frac{\pi}{4}\right)=2$ for $0 \leqslant x \leqslant 2 \pi$

**d** $2 \operatorname{cosec}(2 x-1)=3$ for $-\pi \leqslant x \leqslant \pi$

<a id="ch03-ex3A-q7"></a>
##### Question 7
Solve each equation for $-180^{\circ} \leqslant x \leqslant 180^{\circ}$.

**a** $\operatorname{cosec}^{2} x=4$

**b** $\sec ^{2} x=9$

**c** $9 \cot ^{2} \frac{1}{2} x=4$

**d** $\sec x=\cos x$

**e** $\operatorname{cosec} x=\sec x$

**f** $2 \tan x=3 \operatorname{cosec} x$

<a id="ch03-ex3A-q8"></a>
##### Question 8
Solve each equation for $0^{\circ} \leqslant \theta \leqslant 360^{\circ}$.

**a** $2 \tan ^{2} \theta-1=\sec \theta$

**b** $3 \operatorname{cosec}^{2} \theta=13-\cot \theta$

**c** $2 \cot ^{2} \theta-\operatorname{cosec} \theta=13$

**d** $\operatorname{cosec} \theta+\cot \theta=2 \sin \theta$

**e** $\tan ^{2} \theta+3 \sec \theta=0$

**f** $\sqrt{3} \sec ^{2} \theta=\operatorname{cosec} \theta$

<a id="ch03-ex3A-q9"></a>
##### Question 9
Solve each equation for $0^{\circ} \leqslant \theta \leqslant 180^{\circ}$.

**a** $\sec \theta=3 \cos \theta-\tan \theta$

**b** $2 \sec ^{2} 2 \theta=3 \tan 2 \theta+1$

**c** $\sec ^{4} \theta+2=6 \tan ^{2} \theta$

**d** $2 \cot ^{2} 2 \theta+7 \operatorname{cosec} 2 \theta=2$

<a id="ch03-ex3A-q10"></a>
##### Question 10
Solve each equation for $0 \leqslant \theta \leqslant 2 \pi$.

**a** $\tan ^{2} \theta+3 \sec \theta+3=0$

**b** $3 \cot ^{2} \theta+5 \operatorname{cosec} \theta+1=0$

<a id="ch03-ex3A-q11"></a>
##### Question 11
**a** Sketch each of the following functions for the interval $0 \leqslant x \leqslant 2 \pi$.

**i** $y=1+\sec x$

**ii** $y=\cot 2 x$

**iii** $y=2 \operatorname{cosec}\left(x-\frac{\pi}{2}\right)$

**iv** $y=1-\sec x$

**v** $y=1+\operatorname{cosec} \frac{1}{2} x$

**vi** $y=\sec \left(2 x+\frac{\pi}{4}\right)$

**b** Write down the equation of each of the asymptotes for your graph for part a vi.

<a id="ch03-ex3A-q12"></a>
##### Question 12
Prove each of these identities.

**a** $\sin x+\cos x \cot x \equiv \operatorname{cosec} x$

**b** $\operatorname{cosec} x-\sin x \equiv \cos x \cot x$

**c** $\sec x \operatorname{cosec} x-\cot x \equiv \tan x$

**d** $(1+\sec x)(\operatorname{cosec} x-\cot x) \equiv \tan x$

<a id="ch03-ex3A-q13"></a>
##### Question 13
Prove each of these identities.

**a** $\frac{1}{\tan x+\cot x} \equiv \sin x \cos x$

**b** $\sec ^{2} x+\sec x \tan x \equiv \frac{1}{1-\sin x}$

**c** $\frac{1-\cos ^{2} x}{\sec ^{2} x-1} \equiv 1-\sin ^{2} x$

**d** $\frac{1+\tan ^{2} x}{\tan x} \equiv \sec x \operatorname{cosec} x$

**e** $\frac{\sin x}{1-\cos ^{2} x} \equiv \operatorname{cosec} x$

**f** $\frac{1+\sin x}{1-\sin x} \equiv(\tan x+\sec x)^{2}$

**g** $\frac{1}{1+\cos x}+\frac{1}{1-\cos x} \equiv 2 \operatorname{cosec}^{2} x$

**h** $\frac{\cos x}{1+\sin x}+\frac{\cos x}{1-\sin x} \equiv 2 \sec x$

<a id="ch03-ex3A-q14"></a>
##### Question 14
Solve each equation for $0^{\circ} \leqslant \theta \leqslant 180^{\circ}$.

**a** $6 \sec ^{3} \theta-5 \sec ^{2} \theta-8 \sec \theta+3=0$

**b** $2 \cot ^{3} \theta+3 \operatorname{cosec}^{2} \theta-8 \cot \theta=0$

## 3.2 Compound angle formulae

#### EXPLORE 3.1

**1** Sunita says that: $\sin (A+B)=\sin A+\sin B$

Use a calculator with $A=20^{\circ}$ and $B=50^{\circ}$ to prove that Sunita is wrong.

**2** The diagram shows $\triangle P Q R$.

![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-058_327_540_617_1124.jpg)

$R X$ is perpendicular to $P Q$.

$\angle A$ and $\angle B$ are acute angles.

$Q R=p, P R=q$ and $R X=h$.

**a** Write down an expression for $h$ in terms of:

**i** $q$ and $A$

**ii** $\quad p$ and $B$

**b** Using the formula area of triangle $=\frac{1}{2} a b \sin C$, we can write:

Area of $\Delta P Q R=\frac{1}{2} p q \sin (A+B)$.

Find an expression in terms of $p, q, A$ and $B$ for the area of:

**i** $\triangle P R X$

**ii** $\triangle Q R X$

**c** Use your expressions for the areas of triangles $P Q R, P R X$ and $Q R X$ to prove that:

$$
\sin (A+B) \equiv \sin A \cos B+\cos A \sin B
$$

**3** In the identity $\sin (A+B) \equiv \sin A \cos B+\cos A \sin B$, replace $B$ by $-B$ to show that:

$$
\sin (A-B) \equiv \sin A \cos B-\cos A \sin B
$$

**4** In the identity $\sin (A-B) \equiv \sin A \cos B-\cos A \sin B$, replace $A$ by ( $90^{\circ}-A$ ) to show that:

$$
\cos (A+B) \equiv \cos A \cos B-\sin A \sin B
$$

**5** In the identity $\cos (A+B) \equiv \cos A \cos B-\sin A \sin B$, replace $B$ by $-B$ to show that:

$$
\cos (A-B) \equiv \cos A \cos B+\sin A \sin B
$$

**6** By writing $\tan (A+B)$ as $\frac{\sin (A+B)}{\cos (A+B)}$ and $\tan (A-B)$ as $\frac{\sin (A-B)}{\cos (A-B)}$, show that:

$$
\tan (A+B) \equiv \frac{\tan A+\tan B}{1-\tan A \tan B} \text { and } \tan (A-B) \equiv \frac{\tan A-\tan B}{1+\tan A \tan B}
$$

<a id="ch03-kp-3.3"></a>
#### KEY POINT 3.3

Summarising, the six compound angle formulae are:

$$
\begin{align}
\sin (A+B) & \equiv \sin A \cos B+\cos A \sin B \\
\sin (A-B) & \equiv \sin A \cos B-\cos A \sin B \\
\cos (A+B) & \equiv \cos A \cos B-\sin A \sin B \\
\cos (A-B) & \equiv \cos A \cos B+\sin A \sin B \\
\tan (A+B) & \equiv \frac{\tan A+\tan B}{1-\tan A \tan B} \\
\tan (A-B) & \equiv \frac{\tan A-\tan B}{1+\tan A \tan B}
\end{align}
$$

<a id="ch03-we-3.3"></a>
#### WORKED EXAMPLE 3.3

Find the exact value of:

**a** $\sin 105^{\circ}$

**b** $\cos 42^{\circ} \cos 12^{\circ}+\sin 42^{\circ} \sin 12^{\circ}$

Answer

**a**

$$
\begin{align}
\sin 105^{\circ} & =\sin \left(60^{\circ}+45^{\circ}\right) \\
& =\sin 60^{\circ} \cos 45^{\circ}+\cos 60^{\circ} \sin 45^{\circ} \\
& =\left(\frac{\sqrt{3}}{2}\right)\left(\frac{1}{\sqrt{2}}\right)+\left(\frac{1}{2}\right)\left(\frac{1}{\sqrt{2}}\right) \\
& =\frac{\sqrt{3}+1}{2 \sqrt{2}}
\end{align}
$$

**b**

$$
\begin{align}
& \cos 42^{\circ} \cos 12^{\circ}+\sin 42^{\circ} \sin 12^{\circ} \\
& =\cos \left(42^{\circ}-12^{\circ}\right) \\
& =\cos 30^{\circ} \\
& =\frac{\sqrt{3}}{2}
\end{align}
$$

<a id="ch03-we-3.4"></a>
#### WORKED EXAMPLE 3.4

Given that $\sin A=\frac{4}{5}$ and $\cos B=\frac{5}{13}$, where $A$ is obtuse and $B$ is acute, find the value of:

**a** $\sin (A+B)$

**b** $\cos (A-B)$

**c** $\tan (A-B)$

Answer

![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-059_339_348_1629_263.jpg)

![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-059_337_350_1624_1232.jpg)

$\sin A=\frac{4}{5}, \cos A=-\frac{3}{5}, \tan A=-\frac{4}{3}$ $\sin B=\frac{12}{13}, \cos B=\frac{5}{13}, \tan B=\frac{12}{5}$

**a**

$$
\begin{align}
\sin (A+B) & =\sin A \cos B+\cos A \sin B \\
& =\left(\frac{4}{5}\right)\left(\frac{5}{13}\right)+\left(-\frac{3}{5}\right)\left(\frac{12}{13}\right) \\
& =-\frac{16}{65}
\end{align}
$$

**b**

$$
\begin{align}
\cos (A-B) & =\cos A \cos B+\sin A \sin B \\
& =\left(-\frac{3}{5}\right)\left(\frac{5}{13}\right)+\left(\frac{4}{5}\right)\left(\frac{12}{13}\right) \\
& =\frac{33}{65}
\end{align}
$$

**c** $\tan (A-B)=\frac{\tan A-\tan B}{1+\tan A \tan B}$

$$
\begin{align}
& =\frac{\left(-\frac{4}{3}\right)-\left(\frac{12}{5}\right)}{1+\left(-\frac{4}{3}\right)\left(\frac{12}{5}\right)} \\
& =\frac{56}{33}
\end{align}
$$

<a id="ch03-we-3.5"></a>
#### WORKED EXAMPLE 3.5

Solve the equation $\sin \left(60^{\circ}-x\right)=2 \sin x$ for $0^{\circ}<x<360^{\circ}$.

Answer

| $\sin \left(60^{\circ}-x\right)=2 \sin x$ | Expand $\sin \left(60^{\circ}-x\right)$. |
| :--- | :--- |
| $\sin 60^{\circ} \cos x-\cos 60^{\circ} \sin x=2 \sin x$ | Use $\sin 60^{\circ}=\frac{\sqrt{3}}{2}$ and $\cos 60^{\circ}=\frac{1}{2}$. |
| $\frac{\sqrt{3}}{2} \cos x-\frac{1}{2} \sin x=2 \sin x$ | Multiply both sides by 2. |
| $\sqrt{3} \cos x-\sin x=4 \sin x$ | Add $\sin x$ to both sides. |
| $\sqrt{3} \cos x=5 \sin x$ | Rearrange to find $\tan x$. |
| $\frac{\sqrt{3}}{5}=\tan x$ |  |
| $x=19.1^{\circ}$ or $x=180^{\circ}+19.1^{\circ}$ |  |

The values of $x$ are 19.1° and 199.1°.

<a id="ch03-ex3B"></a>
### EXERCISE 3B

<a id="ch03-ex3B-q1"></a>
##### Question 1
Expand and simplify $\cos \left(x+30^{\circ}\right)$.

<a id="ch03-ex3B-q2"></a>
##### Question 2
Without using a calculator, find the exact value of each of the following:

**a** $\sin 20^{\circ} \cos 70^{\circ}+\cos 20^{\circ} \sin 70^{\circ}$

**b** $\sin 172^{\circ} \cos 37^{\circ}-\cos 172^{\circ} \sin 37^{\circ}$

**c** $\cos 25^{\circ} \cos 35^{\circ}-\sin 25^{\circ} \sin 35^{\circ}$

**d** $\cos 99^{\circ} \cos 69^{\circ}+\sin 99^{\circ} \sin 69^{\circ}$

**e** $\frac{\tan 25^{\circ}+\tan 20^{\circ}}{1-\tan 25^{\circ} \tan 20^{\circ}}$

**f** $\frac{\tan 82^{\circ}-\tan 52^{\circ}}{1+\tan 82^{\circ} \tan 52^{\circ}}$

<a id="ch03-ex3B-q3"></a>
##### Question 3
Without using a calculator, find the exact value of:

**a** $\sin 75^{\circ}$

**b** $\tan 75^{\circ}$

**c** $\cos 105^{\circ}$

**d** $\tan \left(-15^{\circ}\right)$

**e** $\sin \frac{\pi}{12}$

**f** $\cos \frac{19 \pi}{12}$

**g** $\cot \frac{7 \pi}{12}$

**h** $\sin \frac{7 \pi}{12}$

<a id="ch03-ex3B-q4"></a>
##### Question 4
Given that $\cos x=\frac{4}{5}$ and that $0^{\circ}<x<90^{\circ}$, without using a calculator find the exact value of $\cos \left(x-60^{\circ}\right)$.

<a id="ch03-ex3B-q5"></a>
##### Question 5
Given that $\sin A=\frac{4}{5}$ and $\sin B=\frac{5}{13}$, where $A$ and $B$ are acute, show that $\sin (A+B)=\frac{63}{65}$.

<a id="ch03-ex3B-q6"></a>
##### Question 6
Given that $\sin A=\frac{12}{13}$ and $\sin B=\frac{3}{5}$, where $A$ is obtuse and $B$ is acute, find the value of:

**a** $\quad \sin (A+B)$

**b** $\cos (A-B)$

**c** $\tan (A+B)$

<a id="ch03-ex3B-q7"></a>
##### Question 7
Given that $\cos A=-\frac{4}{5}$ and $\sin B=-\frac{8}{17}$ and that $A$ and $B$ lie in the same quadrant, find the value of:

**a** $\sin (A+B)$

**b** $\cos (A+B)$

**c** $\tan (A-B)$

<a id="ch03-ex3B-q8"></a>
##### Question 8
Given that $\tan A=t$ and that $\tan (A-B)=2$, find $\tan B$ in terms of $t$.

<a id="ch03-ex3B-q9"></a>
##### Question 9
If $\cos (A-B)=3 \cos (A+B)$, find the exact value of $\tan A \tan B$.

<a id="ch03-ex3B-q10"></a>
##### Question 10
**a** Given that $8+\operatorname{cosec}^{2} \theta=6 \cot \theta$, find the value of $\tan \theta$.

**b** Hence find the exact value of $\tan \left(\theta+45^{\circ}\right)$.

<a id="ch03-ex3B-q11"></a>
##### Question 11
**a** Given that $x$ is acute and that $2 \sec ^{2} x+7 \tan x=17$, find the exact value of $\tan x$.

**b** Hence find the exact value of $\tan \left(225^{\circ}-x\right)$.

<a id="ch03-ex3B-q12"></a>
##### Question 12
**a** Show that the equation $\sin \left(x+30^{\circ}\right)=5 \cos \left(x-60^{\circ}\right)$ can be written in the form $\cot x=-\sqrt{3}$.

**b** Hence solve the equation $\sin \left(x+30^{\circ}\right)=5 \cos \left(x-60^{\circ}\right)$ for $-180^{\circ}<x<180^{\circ}$.

<a id="ch03-ex3B-q13"></a>
##### Question 13
Solve each equation for $0^{\circ} \leqslant x \leqslant 360^{\circ}$.

**a** $\cos \left(x+30^{\circ}\right)=2 \sin x$

**b** $\cos \left(x-60^{\circ}\right)=3 \cos x$

**c** $\quad \sin \left(30^{\circ}-x\right)=4 \sin x$

**d** $\cos \left(x+30^{\circ}\right)=2 \sin \left(x+60^{\circ}\right)$

<a id="ch03-ex3B-q14"></a>
##### Question 14
Solve each equation for $0^{\circ} \leqslant x \leqslant 180^{\circ}$.

**a** $2 \tan \left(60^{\circ}-x\right)=\tan x$

**b** $2 \tan \left(45^{\circ}-x\right)=3 \tan x$

**c** $\sin \left(x+60^{\circ}\right)=2 \cos \left(x+45^{\circ}\right)$

**d** $\sin \left(x-45^{\circ}\right)=2 \cos \left(x+60^{\circ}\right)$

**e** $\quad \tan \left(x+45^{\circ}\right)=6 \tan x$

**f** $\cos \left(x+225^{\circ}\right)=2 \sin \left(x-60^{\circ}\right)$

<a id="ch03-ex3B-q15"></a>
##### Question 15
Solve the equation $\tan \left(x-45^{\circ}\right)+\cot x=2$ for $0^{\circ} \leqslant x \leqslant 180^{\circ}$.

<a id="ch03-ex3B-q16"></a>
##### Question 16
Use the expansions of $\cos (5 x+x)$ and $\cos (5 x-x)$ to prove that $\cos 6 x+\cos 4 x \equiv 2 \cos 5 x \cos x$.

<a id="ch03-ex3B-q17"></a>
##### Question 17
Given that $\sin x+\sin y=p$ and $\cos x+\cos y=q$, find an expression for $\cos (x-y)$, in terms of $p$ and $q$.

## 3.3 Double angle formulae

We can use the compound angle formulae to derive three new identities.

Consider

$$
\sin (A+B) \equiv \sin A \cos B+\cos A \sin B
$$

If $B=A$,

$$
\begin{align}
\sin (A+A) & \equiv \sin A \cos A+\cos A \sin A \\
\therefore \sin 2 A & \equiv 2 \sin A \cos A
\end{align}
$$

Consider

$$
\cos (A+B) \equiv \cos A \cos B-\sin A \sin B
$$

If $B=A$,

$$
\begin{align}
\cos (A+A) & \equiv \cos A \cos A-\sin A \sin A \\
\therefore \cos 2 A & \equiv \cos ^{2} A-\sin ^{2} A
\end{align}
$$

Consider

$$
\tan (A+B) \equiv \frac{\tan A+\tan B}{1-\tan A \tan B}
$$

If $B=A$,

$$
\begin{align}
\tan (A+A) & \equiv \frac{\tan A+\tan A}{1-\tan A \tan A} \\
\therefore \tan 2 A & \equiv \frac{2 \tan A}{1-\tan ^{2} A}
\end{align}
$$

These three formulae are known as the double angle formulae. We can use the identity $\sin ^{2} A+\cos ^{2} A \equiv 1$ to write the identity $\cos 2 A \equiv \cos ^{2} A-\sin ^{2} A$ in two alternative forms:

Using $\sin ^{2} A \equiv 1-\cos ^{2} A$ gives: $\cos 2 A \equiv 2 \cos ^{2} A-1$ Using $\cos ^{2} A \equiv 1-\sin ^{2} A$ gives: $\cos 2 A \equiv 1-2 \sin ^{2} A$ Summarising, the double angle formulae are:

<a id="ch03-kp-3.4"></a>
#### KEY POINT 3.4

$$
\sin 2 A \equiv 2 \sin A \cos A
$$

$$
\begin{align}
\cos 2 A & \equiv \cos ^{2} A-\sin ^{2} A \quad \tan 2 A \equiv \frac{2 \tan A}{1-\tan ^{2} A} \\
& \equiv 2 \cos ^{2} A-1 \\
& \equiv 1-2 \sin ^{2} A
\end{align}
$$

<a id="ch03-we-3.6"></a>
#### WORKED EXAMPLE 3.6

Given that $\sin x=-\frac{3}{5}$ and that $180^{\circ}<x<270^{\circ}$, find the exact value of:

**a** $\sin 2 x$

**b** $\cos 2 x$

**c** $\tan \frac{x}{2}$

Answer

![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-062_340_350_1717_224.jpg)

From the diagram:

$\sin x=-\frac{3}{5}, \cos x=-\frac{4}{5}$ and $\tan x=\frac{3}{4}$

**a**

$$
\begin{align}
\sin 2 x & =2 \sin x \cos x \\
& =2\left(-\frac{3}{5}\right)\left(-\frac{4}{5}\right)=\frac{24}{25}
\end{align}
$$

**b**

$$
\begin{align}
\cos 2 x & =\cos ^{2} x-\sin ^{2} x \\
& =\left(-\frac{4}{5}\right)^{2}-\left(-\frac{3}{5}\right)^{2}=\frac{7}{25}
\end{align}
$$

**c** $\tan x=\frac{2 \tan \frac{x}{2}}{1-\tan ^{2} \frac{x}{2}}$ Use $2 A=x$ in the double angle formula.

$$
\begin{align}
& \frac{3}{4}=\frac{2 \tan \frac{x}{2}}{1-\tan ^{2} \frac{x}{2}} \\
& 3 \tan ^{2} \frac{x}{2}+8 \tan \frac{x}{2}-3=0 \\
& \left(3 \tan \frac{x}{2}-1\right)\left(\tan \frac{x}{2}+3\right)=0 \\
& \quad \tan \frac{x}{2}=\frac{1}{3} \text { or } \tan \frac{x}{2}=-3
\end{align}
$$

If $180^{\circ}<x<270^{\circ}$, then $90^{\circ}<\frac{x}{2}<135^{\circ}$, which means that $\frac{x}{2}$ is in the second quadrant.

$$
\therefore \tan \frac{x}{2}=-3
$$

<a id="ch03-we-3.7"></a>
#### WORKED EXAMPLE 3.7

Solve the equation $\sin 2 x=\sin x$ for $0^{\circ} \leqslant x \leqslant 360^{\circ}$.

Answer

| $\sin 2 x=\sin x$ | Use $\sin 2 x=2 \sin x \cos x$. |
| :--- | :--- |
| $2 \sin x \cos x=\sin x$ | Rearrange. |
| $2 \sin x \cos x-\sin x=0$ | Factorise. |

$$
\begin{align}
& \quad \sin x(2 \cos x-1)=0 \\
& \sin x=0 \text { or } \cos x=\frac{1}{2} \\
& \sin x=0 \Rightarrow x=0^{\circ}, 180^{\circ}, 360^{\circ} \\
& \cos x=\frac{1}{2} \Rightarrow x=60^{\circ} \\
& \text { or } x=360^{\circ}-60^{\circ}=300^{\circ} \\
& \text { The values of } x \text { are } 0^{\circ}, 60^{\circ}, 180^{\circ}, 300^{\circ}, 360^{\circ} .
\end{align}
$$

![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-063_424_819_1854_1149.jpg)

When solving equations involving $\cos 2 x$ it is important that we choose the most suitable expansion of $\cos 2 x$ for solving that particular equation.

<a id="ch03-we-3.8"></a>
#### WORKED EXAMPLE 3.8

Solve the equation $\cos 2 x+3 \sin x=2$ for $0 \leqslant x \leqslant 2 \pi$.

Answer

$\cos 2 x+3 \sin x=2 \qquad \cup$ Use $\cos 2 x=1-2 \sin ^{2} x$.

$1-2 \sin ^{2} x+3 \sin x=2$ Rearrange.

$2 \sin ^{2} x-3 \sin x+1=0$ Factorise.

$(2 \sin x-1)(\sin x-1)=0$

$\sin x=\frac{1}{2}$ or $\sin x=1$

$\sin x=\frac{1}{2} \Rightarrow x=\frac{\pi}{6}$

or $x=\pi-\frac{\pi}{6}=\frac{5 \pi}{6}$

$\sin x=1 \Rightarrow x=\frac{\pi}{2}$

![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-064_421_809_786_1112.jpg)

The values of $x$ are $\frac{\pi}{6}, \frac{\pi}{2}, \frac{5 \pi}{6}$.

<a id="ch03-ex3C"></a>
### EXERCISE 3C

<a id="ch03-ex3C-q1"></a>
##### Question 1
Express each of the following as a single trigonometric ratio.

**a** $2 \sin 28^{\circ} \cos 28^{\circ}$

**b** $2 \cos ^{2} 34^{\circ}-1$

**c** $\frac{2 \tan 17^{\circ}}{1-\tan ^{2} 17^{\circ}}$

<a id="ch03-ex3C-q2"></a>
##### Question 2
Given that $\tan x=\frac{4}{3}$, where $0^{\circ}<x<90^{\circ}$, find the exact value of:

**a** $\sin 2 x$

**b** $\cos 2 x$

**c** $\tan 2 x$

**d** $\tan 3 x$

<a id="ch03-ex3C-q3"></a>
##### Question 3
Given that $\cos 2 x=-\frac{527}{625}$ and that $0^{\circ}<x<90^{\circ}$, find the exact value of:

**a** $\sin 2 x$

**b** $\tan 2 x$

**c** $\cos x$

**d** $\tan x$

<a id="ch03-ex3C-q4"></a>
##### Question 4
Given that $\cos x=-\frac{3}{5}$ and that $90^{\circ}<x<180^{\circ}$, find the exact value of:

**a** $\sin 2 x$

**b** $\sin 4 x$

**c** $\tan 2 x$

**d** $\tan \frac{1}{2} x$

<a id="ch03-ex3C-q5"></a>
##### Question 5
Given that $3 \cos 2 x+17 \sin x=8$, find the exact value of $\sin x$.

<a id="ch03-ex3C-q6"></a>
##### Question 6
Solve each equation for $0^{\circ} \leqslant \theta \leqslant 360^{\circ}$.

**a** $2 \sin 2 \theta=\cos \theta$

**b** $2 \cos 2 \theta+3=4 \cos \theta$

**c** $2 \cos 2 \theta+1=\sin \theta$

<a id="ch03-ex3C-q7"></a>
##### Question 7
Solve each equation for $0^{\circ} \leqslant \theta \leqslant 180^{\circ}$.

**a** $2 \sin 2 \theta \tan \theta=1$

**b** $3 \cos 2 \theta+\cos \theta=2$

**c** $2 \operatorname{cosec} 2 \theta+2 \tan \theta=3 \sec \theta$

**d** $2 \tan 2 \theta=3 \cot \theta$

**e** $\tan 2 \theta=4 \cot \theta$

**f** $\cot 2 \theta+\cot \theta=3$

<a id="ch03-ex3C-q8"></a>
##### Question 8
Express $\cos ^{2} 2 x$ in terms of $\cos 4 x$.

<a id="ch03-ex3C-q9"></a>
##### Question 9
**a** Use the expansions of $\cos (2 x+x)$ to show that $\cos 3 x \equiv 4 \cos ^{3} x-3 \cos x$.

**b** Express $\sin 3 x$ in terms of $\sin x$.

<a id="ch03-ex3C-q10"></a>
##### Question 10
Solve $\tan 2 \theta+2 \tan \theta=3 \cot \theta$ for $0^{\circ} \leqslant \theta \leqslant 180^{\circ}$.

<a id="ch03-ex3C-q11"></a>
##### Question 11
**a** Prove that $\tan \theta+\cot \theta \equiv \frac{2}{\sin 2 \theta}$.

**b** Hence find the exact value of $\tan \frac{\pi}{12}+\cot \frac{\pi}{12}$.

<a id="ch03-ex3C-q12"></a>
##### Question 12
**a** Prove that $2 \operatorname{cosec} 2 \theta \tan \theta \equiv \sec ^{2} \theta$.

**b** Hence solve the equation $\operatorname{cosec} 2 \theta \tan \theta=2$ for $-\pi<\theta<\pi$.

<a id="ch03-ex3C-q13"></a>
##### Question 13
**a** Prove that $\cos 4 x+4 \cos 2 x \equiv 8 \cos ^{4} x-3$.

**b** Hence solve the equation $2 \cos 4 x+8 \cos 2 x=3$ for $-\pi \leqslant x \leqslant \pi$.

<a id="ch03-ex3C-q14"></a>
##### Question 14
**a** Show that $\theta=18^{\circ}$ is a root of the equation $\sin 3 \theta=\cos 2 \theta$.

**b** Express $\sin 3 \theta$ and $\cos 2 \theta$ in terms of $\sin \theta$.

**c** Hence show that $\sin 18^{\circ}$ is a root of the equation $4 x^{3}-2 x^{2}-3 x+1=0$.

**d** Hence find the exact value of $\sin 18^{\circ}$.

<a id="ch03-ex3C-q15"></a>
##### Question 15
Find the range of values of $\theta$ between 0 and $2 \pi$ for which $\cos 2 \theta>\cos \theta$.

<a id="ch03-ex3C-q16"></a>
##### Question 16
Solve the inequality $\cos 2 \theta-3 \sin \theta-2 \geqslant 0$ for $0^{\circ} \leqslant \theta \leqslant 360^{\circ}$.

<a id="ch03-ex3C-q17"></a>
##### Question 17
![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-065_234_485_1825_372.jpg)

Prove that $a=4 b \cos 2 x \cos x$.

<a id="ch03-ex3C-q18"></a>
##### Question 18
**a** Use the expansions of $\cos (2 x+x)$ and $\cos (2 x-x)$, to prove that:

$$
\cos 3 x+\cos x \equiv 2 \cos 2 x \cos x
$$

**b** Solve $\cos 3 x+\cos 2 x+\cos x>0$ for $0^{\circ}<x<360^{\circ}$.

<a id="ch03-ex3C-q19"></a>
##### Question 19
Solve the inequality $\cos 4 \theta+3 \cos 2 \theta+1<0$ for $0^{\circ} \leqslant \theta \leqslant 360^{\circ}$.

## 3.4 Further trigonometric identities

This section builds on our previous work by using the compound angle formulae and the double angle formulae to prove trigonometric identities.

<a id="ch03-we-3.9"></a>
#### WORKED EXAMPLE 3.9

Prove the identity $\tan 3 x \equiv \frac{3 \tan x-\tan ^{3} x}{1-3 \tan ^{2} x}$.

Answer

$$
\begin{align}
\mathrm{LHS} & \equiv \tan (2 x+x) \\
& \equiv \frac{\tan 2 x+\tan x}{1-\tan 2 x \tan x} \\
& \equiv \frac{\frac{2 \tan x}{1-\tan ^{2} x}+\tan x}{1-\tan x\left(\frac{2 \tan x}{1-\tan ^{2} x}\right)} \\
& \equiv \frac{2 \tan x+\tan x\left(1-\tan ^{2} x\right)}{1-\tan ^{2} x-2 \tan ^{2} x} \\
& \equiv \frac{3 \tan x-\tan ^{3} x}{1-3 \tan ^{2} x} \\
& \equiv \mathrm{RHS}
\end{align}
$$

<a id="ch03-we-3.10"></a>
#### WORKED EXAMPLE 3.10

Prove the identity $\frac{2 \sin (x-y)}{\cos (x-y)-\cos (x+y)} \equiv \cot y-\cot x$.

Answer

$$
\begin{align}
\mathrm{LHS} & \equiv \frac{2 \sin (x-y)}{\cos (x-y)-\cos (x+y)} \\
& \equiv \frac{2 \sin x \cos y-2 \cos x \sin y}{(\cos x \cos y+\sin x \sin y)-(\cos x \cos y-\sin x \sin y)} \qquad \text {. Simplify denominator. } \\
& \equiv \frac{2 \sin x \cos y-2 \cos x \sin y}{2 \sin x \sin y} \quad \text { Separate fractions. } \\
& \equiv \frac{2 \sin x \cos y}{2 \sin x \sin y}-\frac{2 \cos x \sin y}{2 \sin x \sin y} \\
& \equiv \frac{\cos y}{\sin y}-\frac{\cos x}{\sin x} \\
& \equiv \cot y-\cot x \\
& \equiv \text { RHS }
\end{align}
$$

#### EXPLORE 3.2

Odd one out

![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-067_521_1020_437_399.jpg)

Find the trigonometric expression that does not match the other six expressions.

Create as many expressions of your own to match the 'odd one out'.

(Your expressions must contain at least two different trigonometric ratios.) Compare your answers with your classmates.

<a id="ch03-ex3D"></a>
### EXERCISE 3D

<a id="ch03-ex3D-q1"></a>
##### Question 1
Prove each of these identities.

**a** $\tan A+\cot A \equiv 2 \operatorname{cosec} 2 A$

**b** $1-\tan ^{2} A \equiv \cos 2 A \sec ^{2} A$

**c** $\tan 2 A-\tan A \equiv \tan A \sec 2 A$

**d** $(\cos A+3 \sin A)^{2} \equiv 5-4 \cos 2 A+3 \sin 2 A$

**e** $\cot 2 A+\tan A \equiv \frac{1}{2} \operatorname{cosec} A \sec A$

**f** $\operatorname{cosec} 2 A+\cot 2 A \equiv \cot A$

**g** $\sec ^{2} A \operatorname{cosec}^{2} A \equiv 4 \operatorname{cosec}^{2} 2 A$

**h** $\sin (A+B) \sin (A-B) \equiv \sin ^{2} A-\sin ^{2} B$

<a id="ch03-ex3D-q2"></a>
##### Question 2
Prove each of these identities.

**a** $\frac{\sin A}{\cos B}+\frac{\cos A}{\sin B} \equiv \frac{2 \cos (A-B)}{\sin 2 B}$

**b** $\frac{\cos A+\sin A}{\cos A-\sin A} \equiv \sec 2 A+\tan 2 A$

**c** $\frac{1-\tan ^{2} A}{1+\tan ^{2} A} \equiv \cos 2 A$

**d** $\frac{\cos 2 A+\sin 2 A-1}{\cos 2 A-\sin 2 A+1} \equiv \tan A$

**e** $\frac{\sin 3 A+\sin A}{2 \sin 2 A} \equiv \cos A$

**f** $\frac{\cos 3 A-\sin 3 A}{1-2 \sin 2 A} \equiv \cos A+\sin A$

**g** $\frac{\cos 2 A+9 \cos A+5}{4+\cos A} \equiv 2 \cos A+1$

**h** $\frac{\cos ^{3} A-\sin ^{3} A}{\cos A-\sin A} \equiv \frac{2+\sin 2 A}{2}$

<a id="ch03-ex3D-q3"></a>
##### Question 3
Use the fact that $4 A=2 \times 2 A$ to show that:

**a** $\frac{\sin 4 A}{\sin A} \equiv 8 \cos ^{3} A-4 \cos A$

**b** $\cos 4 A+4 \cos 2 A \equiv 8 \cos ^{4} A-3$

<a id="ch03-ex3D-q4"></a>
##### Question 4
Prove the identity $8 \sin ^{2} x \cos ^{2} x \equiv 1-\cos 4 x$.

<a id="ch03-ex3D-q5"></a>
##### Question 5
Prove the identity $(2 \sin A+\cos A)^{2} \equiv \frac{1}{2}(4 \sin 2 A-3 \cos 2 A+5)$.

<a id="ch03-ex3D-q6"></a>
##### Question 6
Use the expansions of $\cos (3 x-x)$ and $\cos (3 x+x)$ to prove the identity:

$$
\cos 2 x-\cos 4 x \equiv 2 \sin 3 x \sin x
$$

## 3.5 Expressing $\boldsymbol{a} \boldsymbol{\operatorname { s i n }} \theta+\boldsymbol{b} \boldsymbol{\operatorname { c o s }} \theta$ in the form $\boldsymbol{R} \boldsymbol{\operatorname { s i n }}(\theta \pm \boldsymbol{\alpha})$ or $\boldsymbol{R} \boldsymbol{\operatorname { c o s }}(\theta \pm \boldsymbol{\alpha})$

In this section you will learn how to solve equations of the form $a \sin \theta+b \cos \theta=c$.

#### EXPLORE 3.3

Use graphing software to confirm that the graph of $y=3 \sin \theta+4 \cos \theta$ for $-90^{\circ} \leqslant \theta \leqslant 360^{\circ}$ is:

![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-068_255_653_627_757.jpg)

**1** What are the amplitude and period of this graph?

**2** Discuss with your classmates how this graph can be obtained by transforming the graph of:

**a** $y=\sin \theta$

**b** $y=\cos \theta$

**3** Use your knowledge of transformations of functions to write the function $y=3 \sin \theta+4 \cos \theta$ in the form:

**a** $y=R \sin (\theta+\alpha)$

**b** $R \sin (\theta+\beta)$

(You will need to use your graph to find the approximate values of $\alpha$ and $\beta$.)

The formula for replacing $a \sin \theta+b \cos \theta$ by $R \sin (\theta+\alpha)$ is derived as follows.

Let $a \sin \theta+b \cos \theta=R \sin (\theta+\alpha)$ where $R>0$ and $0^{\circ}<\alpha<90^{\circ}$.

$$
\begin{align}
R \sin (\theta+\alpha) & =R(\sin \theta \cos \alpha+\cos \theta \sin \alpha) \\
\therefore a \sin \theta+b \cos \theta & =R \sin \theta \cos \alpha+R \cos \theta \sin \alpha
\end{align}
$$

Equating coefficients of $\sin \theta: \quad R \cos \alpha=a$

(1)

Equating coefficients of $\cos \theta: \quad R \sin \alpha=b$

(2)

(2) ÷ (1): $\frac{\sin \alpha}{\cos \alpha}=\frac{b}{a} \Rightarrow \tan \alpha=\frac{b}{a}$ Squaring equations (1) and (2) and then adding gives:

$$
\begin{align}
a^{2}+b^{2} & =R^{2} \cos ^{2} \alpha+R^{2} \sin ^{2} \alpha \\
& =R^{2}\left(\cos ^{2} \alpha+\sin ^{2} \alpha\right) \\
& =R^{2}
\end{align}\quad \begin{array}{r} \text { Use } \cos ^{2} \alpha+\sin ^{2} \alpha=1 \end{array}
$$

Hence, $R=\sqrt{a^{2}+b^{2}}$

$\therefore a \sin \theta+b \cos \theta$ can be written as $R \sin (\theta+\alpha)$ where $R=\sqrt{a^{2}+b^{2}}$ and $\tan \alpha=\frac{b}{a}$

#### EXPLORE 3.4

Using a similar approach, show that:

$1 a \sin \theta-b \cos \theta \equiv R \sin (\theta-\alpha)$ where $R=\sqrt{a^{2}+b^{2}}$ and $\tan \alpha=\frac{b}{a}$ $2 a \cos \theta+b \sin \theta \equiv R \cos (\theta-\alpha)$ where $R=\sqrt{a^{2}+b^{2}}$ and $\tan \alpha=\frac{b}{a}$ $3 a \cos \theta-b \sin \theta \equiv R \cos (\theta+\alpha)$ where $R=\sqrt{a^{2}+b^{2}}$ and $\tan \alpha=\frac{b}{a}$

Summarising the results from Explore 3.4:

<a id="ch03-kp-3.5"></a>
#### KEY POINT 3.5

$a \sin \theta \pm b \cos \theta \equiv R \sin (\theta \pm \alpha)$ and $a \cos \theta \pm b \sin \theta \equiv R \cos (\theta \mp \alpha)$ where $R=\sqrt{a^{2}+b^{2}}, \tan \alpha=\frac{b}{a}$ and $0^{\circ}<\alpha<90^{\circ}$.

<a id="ch03-we-3.11"></a>
#### WORKED EXAMPLE 3.11

**a** Express $2 \sin \theta-3 \cos \theta$ in the form $R \sin (\theta-\alpha)$, where $R>0$ and $0^{\circ}<\alpha<90^{\circ}$.

Give the value of $\alpha$ correct to 2 decimal places.

**b** Hence solve the equation $2 \sin \theta-3 \cos \theta=\sqrt{2}$ for $0^{\circ}<\theta<360^{\circ}$.

Answer

**a**

$$
\begin{align}
2 \sin \theta-3 \cos \theta & =R \sin (\theta-\alpha) \\
\therefore 2 \sin \theta-3 \cos \theta & =R \sin \theta \cos \alpha-R \cos \theta \sin \alpha
\end{align}
$$

Equating coefficients of $\sin \theta: R \cos \alpha=2$

(1)

Equating coefficients of $\cos \theta: R \sin \alpha=3$

(2)

(2) $\div(1): \tan \alpha=\frac{3}{2} \Rightarrow \alpha=56.31^{\circ}$ Squaring equations (1) and (2) and then adding gives:

$$
3^{2}+2^{2}=R^{2} \Rightarrow R=\sqrt{13}
$$

$\therefore 2 \sin \theta-3 \cos \theta=\sqrt{13} \sin \left(\theta-56.31^{\circ}\right)$

**b**

$$
\begin{align}
2 \sin \theta-3 \cos \theta & =\sqrt{2} \\
\sqrt{13} \sin \left(\theta-56.31^{\circ}\right) & =\sqrt{2}
\end{align}
$$

$$
\sin \left(\theta-56.31^{\circ}\right)=\frac{\sqrt{2}}{\sqrt{13}}
$$

$$
\begin{align}
\theta-56.31^{\circ} & =23.09^{\circ}, 180^{\circ}-23.09^{\circ} \\
& =23.09^{\circ}, 156.91^{\circ} \\
\theta & =79.4^{\circ}, 213.2^{\circ}
\end{align}
$$

We can find the maximum and minimum values of the expression $a \sin \theta+b \cos \theta$ by writing the expression in the form $R \sin (\theta+\alpha)$.

From the Pure Mathematics Coursebook 1, Chapter 5, Section 5.4, we know that $-1 \leqslant \sin (\theta+\alpha) \leqslant 1$, hence $-R \leqslant R \sin (\theta+\alpha) \leqslant R$.

This can be summarised as:

<a id="ch03-kp-3.6"></a>
#### KEY POINT 3.6

The maximum value of $a \sin \theta+b \cos \theta$ is $\sqrt{a^{2}+b^{2}}$ and occurs when $\sin (\theta+\alpha)=1$.

The minimum value of $a \sin \theta+b \cos \theta$ is $-\sqrt{a^{2}+b^{2}}$ and occurs when $\sin (\theta+\alpha)=-1$.

<a id="ch03-we-3.12"></a>
#### WORKED EXAMPLE 3.12

Express $2 \cos \theta-\sin \theta$ in the form $R \cos (\theta+\alpha)$, where $R>0$ and $0^{\circ}<\alpha<90^{\circ}$.

Hence, find the maximum and minimum values of the expression $2 \cos \theta-\sin \theta$ and the values of $\theta$ in the interval $0^{\circ}<\theta<360^{\circ}$ for which these occur.

Answer

$$
\begin{align}
2 \cos \theta-\sin \theta & =R \cos (\theta+\alpha) \\
\therefore 2 \cos \theta-\sin \theta & =R \cos \theta \cos \alpha-R \sin \theta \sin \alpha
\end{align}
$$

Equating coefficients of $\cos \theta: R \cos \alpha=2$

(1)

Equating coefficients of $\sin \theta: R \sin \alpha=1$

(2)

(2) ÷ (1): $\tan \alpha=\frac{1}{2} \Rightarrow \alpha=26.57^{\circ}$

Squaring equations (1) and (2) and then adding gives:

$$
2^{2}+1^{2}=R^{2} \Rightarrow R=\sqrt{5}
$$

$\therefore 2 \cos \theta-\sin \theta=\sqrt{5} \cos \left(\theta+26.57^{\circ}\right)$ Maximum value is $\sqrt{2^{2}+(-1)^{2}}$ and occurs when $\cos \left(\theta+26.57^{\circ}\right)=1$

$$
\begin{align}
\theta+26.57^{\circ} & =360^{\circ} \\
\theta & =333.4^{\circ}
\end{align}
$$

Minimum value is $-\sqrt{2^{2}+(-1)^{2}}$ and occurs when $\cos \left(\theta+26.57^{\circ}\right)=-1$

$$
\begin{align}
\theta+26.57^{\circ} & =180^{\circ} \\
\theta & =153.4^{\circ}
\end{align}
$$

∴ Max value $=\sqrt{5}$ when $\theta=333.4^{\circ}$, min value $=-\sqrt{5}$ when $\theta=153.4^{\circ}$

#### DID YOU KNOW?

The French mathematician Joseph Fourier (1768-1830) found a way to represent any wave-like function as the sum (possibly infinite) of simple sine waves. The sum of sine functions is called

**a** Fourier series. These series can be applied to vibration problems. Fourier is also credited with discovering the greenhouse effect.

![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-070_148_885_2494_428.jpg)

<a id="ch03-ex3E"></a>
### EXERCISE 3E

<a id="ch03-ex3E-q1"></a>
##### Question 1
**a** Express $15 \sin \theta-8 \cos \theta$ in the form $R \sin (\theta-\alpha)$, where $R>0$ and $0^{\circ}<\alpha<90^{\circ}$. Give the value of $\alpha$ correct to 2 decimal places.

**b** Hence solve the equation $15 \sin \theta-8 \cos \theta=10$ for $0^{\circ}<\theta<360^{\circ}$.

<a id="ch03-ex3E-q2"></a>
##### Question 2
**a** Express $2 \cos \theta-3 \sin \theta$ in the form $R \cos (\theta+\alpha)$, where $R>0$ and $0^{\circ}<\alpha<90^{\circ}$. Give the exact value of $R$ and the value of $\alpha$ correct to 2 decimal places.

**b** Hence solve the equation $2 \cos \theta-3 \sin \theta=1.3$ for $0^{\circ}<\theta<360^{\circ}$.

<a id="ch03-ex3E-q3"></a>
##### Question 3
**a** Express $15 \sin \theta-8 \cos \theta$ in the form $R \sin (\theta-\alpha)$, where $R>0$ and $0^{\circ}<\alpha<90^{\circ}$. Give the value of $\alpha$ correct to 2 decimal places.

**b** Hence solve the equation $15 \sin \theta-8 \cos \theta=3$ for $0^{\circ}<\theta<360^{\circ}$.

**c** Find the greatest value of $30 \sin \theta-16 \cos \theta$ as $\theta$ varies.

<a id="ch03-ex3E-q4"></a>
##### Question 4
**a** Express $4 \sin \theta-6 \cos \theta$ in the form $R \sin (\theta-\alpha)$, where $R>0$ and $0^{\circ}<\alpha<90^{\circ}$. Give the exact value of $R$ and the value of $\alpha$ correct to 2 decimal places.

**b** Hence solve the equation $4 \sin \theta-6 \cos \theta=3$ for $0^{\circ}<\theta<180^{\circ}$.

**c** Find the greatest and least values of $(4 \sin \theta-6 \cos \theta)^{2}-3$ as $\theta$ varies.

<a id="ch03-ex3E-q5"></a>
##### Question 5
**a** Express $3 \sin \theta+4 \cos \theta$ in the form $R \sin (\theta+\alpha)$, where $R>0$ and $0^{\circ}<\alpha<90^{\circ}$. Give the value of $\alpha$ correct to 2 decimal places.

**b** Hence solve the equation $3 \sin \theta+4 \cos \theta=2$ for $0^{\circ}<\theta<360^{\circ}$.

**c** Find the least value of $3 \sin \theta+4 \cos \theta+3$ as $\theta$ varies.

<a id="ch03-ex3E-q6"></a>
##### Question 6
**a** Express $\cos \theta+\sqrt{3} \sin \theta$ in the form $R \cos (\theta-\alpha)$, where $R>0$ and $0<\alpha<\frac{\pi}{2}$. Give the exact values of $R$ and $\alpha$.

**b** Hence prove that $\frac{1}{(\cos \theta+\sqrt{3} \sin \theta)^{2}} \equiv \frac{1}{4} \sec ^{2}\left(\theta-\frac{\pi}{3}\right)$.

<a id="ch03-ex3E-q7"></a>
##### Question 7
**a** Express $8 \sin 2 \theta+4 \cos 2 \theta$ in the form $R \sin (2 \theta+\alpha)$, where $R>0$ and $0^{\circ}<\alpha<90^{\circ}$. Give the exact value of $R$ and the value of $\alpha$ correct to 2 decimal places.

**b** Hence solve the equation $8 \sin 2 \theta+4 \cos 2 \theta=3$ for $0^{\circ}<\theta<360^{\circ}$.

**c** Find the least value of $\frac{10}{(8 \sin 2 \theta+4 \cos 2 \theta)^{2}}$ as $\theta$ varies.

<a id="ch03-ex3E-q8"></a>
##### Question 8
**a** Express $\cos \theta-\sqrt{2} \sin \theta$ in the form $R \cos (\theta+\alpha)$, where $R>0$ and $0^{\circ}<\alpha<90^{\circ}$. Give the exact value of $R$ and the value of $\alpha$ correct to 2 decimal places.

**b** Hence solve the equation $\cos \theta-\sqrt{2} \sin \theta=-1$ for $0^{\circ}<\theta<360^{\circ}$.

**c** Find the least value of $\frac{1}{(\sqrt{2} \cos \theta-2 \sin \theta)^{2}}$ as $\theta$ varies.

<a id="ch03-ex3E-q9"></a>
##### Question 9
**a** Express $\cos \theta-\sin \theta$ in the form $R \cos (\theta+\alpha)$, where $R>0$ and $0<\alpha<\frac{\pi}{2}$.

Give the exact values of $R$ and $\alpha$.

**b** Show that one solution of the equation $\cos \theta-\sin \theta=\frac{1}{2} \sqrt{6}$ is $\theta=\frac{19 \pi}{12}$ and find the other solution in the interval $0<\theta<2 \pi$.

**c** State the set of values of $k$ for which the equation $\cos \theta-\sin \theta=k$ has any solutions.

<a id="ch03-ex3E-q10"></a>
##### Question 10
**a** Express $\sin \theta-3 \cos \theta$ in the form $R \sin (\theta-\alpha)$, where $R>0$ and $0^{\circ}<\alpha<90^{\circ}$.

Give the exact value of $R$ and the value of $\alpha$ correct to 2 decimal places.

**b** Hence solve the equation $\sin \theta-3 \cos \theta=-2$ for $0^{\circ}<\theta<360^{\circ}$.

**c** Find the greatest possible value of $1+\sin 2 \theta-3 \cos 2 \theta$ as $\theta$ varies and determine the smallest positive value of $\theta$ for which this greatest value occurs.

<a id="ch03-ex3E-q11"></a>
##### Question 11
**a** Express $\sqrt{5} \cos \theta+2 \sin \theta$ in the form $R \cos (\theta-\alpha)$, where $R>0$ and $0^{\circ}<\alpha<90^{\circ}$.

Give the value of $\alpha$ correct to 2 decimal places.

**b** Find the smallest positive angle $\theta$ that satisfies the equation $\sqrt{5} \cos \theta+2 \sin \theta=3$.

**c** Find the smallest positive angle $\theta$ that satisfies the equation $\sqrt{5} \cos \frac{1}{2} \theta+2 \sin \frac{1}{2} \theta=-1$.

<a id="ch03-ex3E-q12"></a>
##### Question 12
**a** Given that $3 \sec \theta+4 \operatorname{cosec} \theta=2 \operatorname{cosec} 2 \theta$, show that $3 \sin \theta+4 \cos \theta=1$.

**b** Express $3 \sin \theta+4 \cos \theta$ in the form $R \sin (\theta+\alpha)$, where $R>0$ and $0^{\circ}<\alpha<90^{\circ}$.

Give the value of $\alpha$ correct to 2 decimal places.

**c** Hence solve the equation $3 \sec \theta+4 \operatorname{cosec} \theta=2 \operatorname{cosec} 2 \theta$ for $0^{\circ}<\theta<360^{\circ}$.

<a id="ch03-ex3E-q13"></a>
##### Question 13
**a** Express $\sin \left(\theta+30^{\circ}\right)+\cos \theta$ in the form $R \sin (\theta+\alpha)$, where $R>0$ and $0^{\circ}<\alpha<90^{\circ}$.

Give the exact values of $R$ and $\alpha$.

**b** Hence solve the equation $\sin \left(\theta+30^{\circ}\right)+\cos \theta=1$ for $0^{\circ}<\theta<360^{\circ}$.

<a id="ch03-ex3E-q14"></a>
##### Question 14
**a** Find the maximum and minimum values of $7 \sin ^{2} \theta+9 \cos ^{2} \theta+4 \sin \theta \cos \theta+2$.

**b** Hence, or otherwise, solve the equation $7 \sin ^{2} \theta+9 \cos ^{2} \theta+4 \sin \theta \cos \theta=10$ for $0^{\circ}<\theta<360^{\circ}$.

### Checklist of learning and understanding

Cosecant, secant and cotangent

$$
\operatorname{cosec} \theta=\frac{1}{\sin \theta}
$$

$$
\sec \theta=\frac{1}{\cos \theta}
$$

$$
\cot \theta=\frac{1}{\tan \theta}
$$

![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-073_458_577_502_218.jpg)

![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-073_457_571_502_822.jpg)

![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-073_460_576_502_1421.jpg)

Trigonometric identities

- $1+\tan ^{2} x \equiv \sec ^{2} x$

- $1+\cot ^{2} x \equiv \operatorname{cosec}^{2} x$

Compound angle formula

- $\sin (A+B) \equiv \sin A \cos B+\cos A \sin B$

- $\sin (A-B) \equiv \sin A \cos B-\cos A \sin B$

- $\cos (A+B) \equiv \cos A \cos B-\sin A \sin B$

- $\cos (A-B) \equiv \cos A \cos B+\sin A \sin B$

- $\tan (A+B) \equiv \frac{\tan A+\tan B}{1-\tan A \tan B}$

- $\tan (A-B) \equiv \frac{\tan A-\tan B}{1+\tan A \tan B}$

Double angle formulae

- $\sin 2 A \equiv 2 \sin A \cos A$

-

$$
\begin{align}
\cos 2 A & \equiv \cos ^{2} A-\sin ^{2} A \\
& \equiv 1-2 \sin ^{2} A \\
& \equiv 2 \cos ^{2} A-1
\end{align}
$$

- $\tan 2 A \equiv \frac{2 \tan A}{1-\tan ^{2} A}$

Expressing $\boldsymbol{a} \boldsymbol{\operatorname { s i n }} \boldsymbol{\theta}+\boldsymbol{b} \boldsymbol{\operatorname { c o s }} \boldsymbol{\theta}$ in the form $\boldsymbol{R} \boldsymbol{\operatorname { s i n }}(\boldsymbol{\theta} \pm \boldsymbol{\alpha})$ or $\boldsymbol{R} \boldsymbol{\operatorname { c o s }}(\boldsymbol{\theta} \pm \boldsymbol{\alpha})$

- $a \sin \theta \pm b \cos \theta=R \sin (\theta \pm \alpha)$

- $a \cos \theta \pm b \sin \theta=R \cos (\theta \mp \alpha)$

where $R=\sqrt{a^{2}+b^{2}}$ and $\tan \alpha=\frac{b}{a}$

<a id="ch03-review"></a>
### END-OF-CHAPTER REVIEW EXERCISE 3

<a id="ch03-review-q1"></a>
##### Question 1
Sketch the graph of $y=3 \sec \left(2 x-90^{\circ}\right)$ for $0^{\circ}<x<180^{\circ}$. `[3]`

<a id="ch03-review-q2"></a>
##### Question 2
By expressing the equation $\operatorname{cosec} \theta=3 \sin \theta+\cot \theta$ in terms of $\cos \theta$ only, solve the equation for $0^{\circ}<\theta<180^{\circ}$. `[5]`

*Cambridge International A Level Mathematics 9709 Paper 31 Q3 June 2016*

<a id="ch03-review-q3"></a>
##### Question 3
Given that $\cos A=\frac{1}{4}$, where $270^{\circ}<A<360^{\circ}$, find the exact value of $\sin 2 A$. `[5]`

<a id="ch03-review-q4"></a>
##### Question 4
Solve the equation $2 \tan ^{2} x+\sec x=1$ for $0^{\circ} \leqslant x \leqslant 360^{\circ}$. `[6]`

<a id="ch03-review-q5"></a>
##### Question 5
Solve the equation $2 \cot ^{2} x+5 \operatorname{cosec} x=10$ for $0^{\circ}<x<360^{\circ}$. `[6]`

<a id="ch03-review-q6"></a>
##### Question 6
**a** Prove that $\sin \left(x+60^{\circ}\right)+\cos \left(x+30^{\circ}\right) \equiv \sqrt{3} \cos x$. `[3]`

**b** Hence solve the equation $\sin \left(x+60^{\circ}\right)+\cos \left(x+30^{\circ}\right)=\frac{3}{2}$ for $0^{\circ}<x<360^{\circ}$. `[3]`

<a id="ch03-review-q7"></a>
##### Question 7
**a** Prove that $\sin \left(60^{\circ}-x\right)+\cos \left(30^{\circ}-x\right) \equiv \sqrt{3} \cos x$. `[3]`

**b** Hence solve the equation $\sin \left(60^{\circ}-x\right)+\cos \left(30^{\circ}-x\right)=\frac{2}{5} \sec x$ for $0^{\circ}<x<360^{\circ}$. `[3]`

<a id="ch03-review-q8"></a>
##### Question 8
**i** Show that the equation $\tan \left(x+45^{\circ}\right)=6 \tan x$ can be written in the form $6 \tan ^{2} x-5 \tan x+1=0$.

**ii** Hence solve the equation $\tan \left(x+45^{\circ}\right)=6 \tan x$, for $0^{\circ}<x<180^{\circ}$. `[3]`

*Cambridge International AS \& A Level Mathematics 9709 Paper 21 Q3 June 2010*

<a id="ch03-review-q9"></a>
##### Question 9
**a** Prove that $\tan \left(x+45^{\circ}\right)-\tan \left(45^{\circ}-x\right) \equiv 2 \tan 2 x$. `[4]`

**b** Hence solve the equation $\tan \left(x+45^{\circ}\right)-\tan \left(45^{\circ}-x\right)=6$ for $0^{\circ}<x<180^{\circ}$. `[3]`

<a id="ch03-review-q10"></a>
##### Question 10
**i** Express $3 \cos \theta+\sin \theta$ in the form $R \cos (\theta-\alpha)$, where $R>0$ and $0^{\circ}<\alpha<90^{\circ}$, giving the exact value of $R$ and the value of $\alpha$ correct to 2 decimal places. `[3]`

**ii** Hence solve the equation $3 \cos 2 x+\sin 2 x=2$, giving all solutions in the interval $0^{\circ} \leqslant x \leqslant 360^{\circ}$. `[5]`

*Cambridge International AS \& A Level Mathematics 9709 Paper 21 Q7 November 2013*

<a id="ch03-review-q11"></a>
##### Question 11
**a** Prove that $\cos \left(60^{\circ}-x\right)+\cos \left(300^{\circ}-x\right) \equiv \cos x$. `[3]`

**b** Hence

i find the exact value of $\cos 15^{\circ}+\cos 255^{\circ}$ `[2]`

ii solve the equation $\cos \left(60^{\circ}-x\right)+\cos \left(300^{\circ}-x\right)=\frac{1}{4} \operatorname{cosec} x$ for $0^{\circ}<x<180^{\circ}$. `[3]`

<a id="ch03-review-q12"></a>
##### Question 12
**a** Prove the identity $\frac{2 \sin 2 \theta-3 \cos 2 \theta+3}{\sin \theta} \equiv 4 \cos \theta+6 \sin \theta$. `[3]`

**b** Express $4 \cos \theta+6 \sin \theta$ in the form $R \cos (\theta-\alpha)$, where $R>0$ and $0<\alpha<\frac{\pi}{2}$.

Give the exact value of $R$ and the value of $\alpha$ correct to 2 decimal places. `[4]`

**c** Write down the greatest value of $\left(\frac{2 \sin 2 \theta-3 \cos 2 \theta+3}{\sin \theta}\right)^{2}$. `[1]`

<a id="ch03-review-q13"></a>
##### Question 13
**i** Express $4 \sin \theta-6 \cos \theta$ in the form $R \sin (\theta-\alpha)$, where $R>0$ and $0^{\circ}<\alpha<90^{\circ}$.

Give the exact value of $R$ and the value of $\alpha$ correct to 2 decimal places. `[3]`

**ii** Solve the equation $4 \sin \theta-6 \cos \theta=3$ for $0^{\circ} \leqslant \theta \leqslant 360^{\circ}$. `[4]`

**iii** Find the greatest and least possible values of $(4 \sin \theta-6 \cos \theta)^{2}+8$ as $\theta$ varies. `[2]`

*Cambridge International AS \& A Level Mathematics 9709 Paper 21 Q8 June 2011*

<a id="ch03-review-q14"></a>
##### Question 14
**i** By first expanding $\sin (2 \theta+\theta)$, show that $\sin 3 \theta=3 \sin \theta-4 \sin ^{3} \theta$. `[4]`

**ii** Show that, after making the substitution $x=\frac{2 \sin \theta}{\sqrt{3}}$, the equation $x^{3}-x+\frac{1}{6} \sqrt{3}=0$ can be written in the form $\sin 3 \theta=\frac{3}{4}$. `[1]`

**iii** Hence solve the equation $x^{3}-x+\frac{1}{6} \sqrt{3}=0$, giving your answers correct to 3 significant figures. `[4]`

*Cambridge International A Level Mathematics 9709 Paper 31 Q8 November 2014*

<a id="ch03-review-q15"></a>
##### Question 15
**a** Prove the identity $\frac{1}{\sin \left(x+30^{\circ}\right)+\cos \left(x+60^{\circ}\right)} \equiv \sec x$. `[3]`

**b** Hence solve the equation $\frac{2}{\sin \left(x+30^{\circ}\right)+\cos \left(x+60^{\circ}\right)}=7-\tan ^{2} x$ for $0^{\circ}<x<360^{\circ}$. `[6]`

<a id="ch03-review-q16"></a>
##### Question 16
**a** Prove the identity $\operatorname{cosec}^{4} x-\cot ^{4} x \equiv \operatorname{cosec}^{2} x+\cot ^{2} x$. `[3]`

**b** Hence solve the equation $\operatorname{cosec}^{4} x-\cot ^{4} x=16-\cot x$ for $0^{\circ}<x<180^{\circ}$. `[6]`

<a id="ch03-review-q17"></a>
##### Question 17
The curves $C_{1}$ and $C_{2}$ have equations $y=1+4 \cos 2 x$ and $y=2 \cos ^{2} x-4 \sin 2 x$.

**a** Show that the $x$-coordinates of the points where $C_{1}$ and $C_{2}$ intersect satisfy the equation $3 \cos 2 x+4 \sin 2 x=0$. `[3]`

**b** Express $3 \cos 2 x+4 \sin 2 x$ in the form $R \sin (2 x+\alpha)$, where $R>0$ and $0^{\circ}<\alpha<90^{\circ}$. Give the exact value of $R$ and the value of $\alpha$ correct to 2 decimal places. `[3]`

**c** Hence find all the roots of the equation $3 \cos 2 x+4 \sin 2 x=0$ for $0^{\circ}<x<180^{\circ}$. `[3]`

<a id="ch03-cross"></a>
### CROSS-TOPIC REVIEW EXERCISE 1

<a id="ch03-cross-q1"></a>
##### Question 1
Find the set of values of $x$ satisfying the inequality $3|x-1|<|2 x+1|$. `[4]`

*Cambridge International A Level Mathematics 9709 Paper 31 Q1 November 2012*

<a id="ch03-cross-q2"></a>
##### Question 2
Solve the equation $2\left|3^{x}-1\right|=3^{x}$, giving your answers correct to 3 significant figures. `[4]`

*Cambridge International A Level Mathematics 9709 Paper 31 Q2 November 2013*

<a id="ch03-cross-q3"></a>
##### Question 3
**i** Solve the equation $|3 x+4|=|3 x-11|$. `[3]`

**ii** Hence, using logarithms, solve the equation $\left|3 \times 2^{y}+4\right|=\left|3 \times 2^{y}-11\right|$, giving the answer correct to 3 significant figures. `[2]`

*Cambridge International AS \& A Level Mathematics 9709 Paper 21 Q1 June 2015*

<a id="ch03-cross-q4"></a>
##### Question 4
**i** Solve the equation $2|x-1|=3|x|$. `[3]`

**ii** Hence solve the equation $2\left|5^{x}-1\right|=3\left|5^{x}\right|$, giving your answer correct to 3 significant figures. `[2]`

*Cambridge International A Level Mathematics 9709 Paper 31 Q1 June 2016*

<a id="ch03-cross-q5"></a>
##### Question 5
![](../images/6c997e27-652f-45af-9aa3-c3a1b39841c3-076_433_729_1214_782.jpg) The variables $x$ and $y$ satisfy the equation $y=A\left(b^{x}\right)$, where $A$ and $b$ are constants. The graph of $\ln y$ against $x$ is a straight line passing through the points (0, 2.14) and (5, 4.49), as shown in the diagram. Find the values of $A$ and $b$, correct to 1 decimal place. `[5]`

*Cambridge International AS \& A Level Mathematics 9709 Paper 21 Q2 June 2012*

<a id="ch03-cross-q6"></a>
##### Question 6
**i** It is given that $x$ satisfies the equation $3^{2 x}=5\left(3^{x}\right)+14$. Find the value of $3^{x}$ and, using logarithms, find the value of $x$ correct to 3 significant figures. `[4]`

**ii** Hence state the values of $x$ satisfying the equation $3^{|x|}=5\left(3^{|x|}\right)+14$. `[1]`

*Cambridge International AS \& A Level Mathematics 9709 Paper 21 Q1 November 2016*

<a id="ch03-cross-q7"></a>
##### Question 7
The variables $x$ and $y$ satisfy the equation $x^{n} y=C$, where $n$ and $C$ are constants.

When $x=1.10, y=5.20$, and when $x=3.20, y=1.05$.

**i** Find the values of $n$ and $C$. `[5]`

**ii** Explain why the graph of $\ln y$ against $\ln x$ is a straight line. `[1]`

*Cambridge International A Level Mathematics 9709 Paper 31 Q3 June 2010*

<a id="ch03-cross-q8"></a>
##### Question 8
Given that $3 \mathrm{e}^{x}+8 \mathrm{e}^{-x}=14$, find the possible values of $\mathrm{e}^{x}$ and hence solve the equation $3 \mathrm{e}^{x}+8 \mathrm{e}^{-x}=14$ correct to 3 significant figures. `[6]`

<a id="ch03-cross-q9"></a>
##### Question 9
The angles $\theta$ and $\phi$ lie between 0° and 180°, and are such that $\tan (\theta-\phi)=3$ and $\tan \theta+\tan \phi=1$. Find the possible values of $\theta$ and $\phi$. `[6]`

*Cambridge International A Level Mathematics 9709 Paper 31 Q3 November 2015*

<a id="ch03-cross-q10"></a>
##### Question 10
**i** Solve the equation $|4 x-1|=|x-3|$. `[3]`

**ii** Hence solve the equation $\left|4^{y+1}-1\right|=\left|4^{y}-3\right|$ correct to 3 significant figures. `[3]`

*Cambridge International A Level Mathematics 9709 Paper 31 Q4 June 2013*

<a id="ch03-cross-q11"></a>
##### Question 11
The polynomial $4 x^{3}+a x^{2}+9 x+9$, where $a$ is a constant, is denoted by $\mathrm{p}(x)$. It is given that when $\mathrm{p}(x)$ is divided by $(2 x-1)$ the remainder is 10.

**i** Find the value of $a$ and hence verify that $(x-3)$ is a factor of $\mathrm{p}(x)$. `[3]`

**ii** When $a$ has this value, solve the equation $\mathrm{p}(x)=0$. `[4]`

*Cambridge International AS \& A Level Mathematics 9709 Paper 21 Q5 November 2011*

<a id="ch03-cross-q12"></a>
##### Question 12
The polynomial $2 x^{3}-4 x^{2}+a x+b$, where $a$ and $b$ are constants, is denoted by $\mathrm{p}(x)$.

It is given that when $\mathrm{p}(x)$ is divided by ( $x+1$ ) the remainder is 4, and that when $\mathrm{p}(x)$ is divided by $(x-3)$ the remainder is 12.

**i** Find the values of $a$ and $b$. `[5]`

**ii** When $a$ and $b$ have these values, find the quotient and remainder when $\mathrm{p}(x)$ is divided by $\left(x^{2}-2\right)$. `[3]`

*Cambridge International AS \& A Level Mathematics 9709 Paper 21 Q7 November 2012*

<a id="ch03-cross-q13"></a>
##### Question 13
**i** Express $\cos x+3 \sin x$ in the form $R \cos (x-\alpha)$, where $R>0$ and $0^{\circ}<\alpha<90^{\circ}$, giving the exact value of $R$ and the value of $\alpha$ correct to 2 decimal places. `[3]`

**ii** Hence solve the equation $\cos 2 \theta+3 \sin 2 \theta=2$, for $0^{\circ}<\theta<90^{\circ}$. `[5]`

*Cambridge International A Level Mathematics 9709 Paper 31 Q6 November 2011*

<a id="ch03-cross-q14"></a>
##### Question 14
It is given that $2 \ln (4 x-5)+\ln (x+1)=3 \ln 3$.

**i** Show that $16 x^{3}-24 x^{2}-15 x-2=0$. `[3]`

**ii** By first using the factor theorem, factorise $16 x^{3}-24 x^{2}-15 x-2$ completely. `[4]`

**iii** Hence solve the equation $2 \ln (4 x-5)+\ln (x+1)=3 \ln 3$. `[1]`

*Cambridge International A Level Mathematics 9709 Paper 31 Q6 June 2014*

<a id="ch03-cross-q15"></a>
##### Question 15
The polynomial $8 x^{3}+a x^{2}+b x-1$, where $a$ and $b$ are constants, is denoted by $\mathrm{p}(x)$.

It is given that $(x+1)$ is a factor of $\mathrm{p}(x)$ and that when $\mathrm{p}(x)$ is divided by ( $2 x+1$ ) the remainder is 1.

**i** Find the values of $a$ and $b$. `[5]`

**ii** When $a$ and $b$ have these values, factorise $\mathrm{p}(x)$ completely. `[3]`

*Cambridge International A Level Mathematics 9709 Paper 31 Q6 November 2015*

<a id="ch03-cross-q16"></a>
##### Question 16
The polynomial $3 x^{3}+2 x^{2}+a x+b$, where $a$ and $b$ are constants, is denoted by $\mathrm{p}(x)$.

It is given that $(x-1)$ is a factor of $\mathrm{p}(x)$, and that when $\mathrm{p}(x)$ is divided by $(x-2)$ the remainder is 10.

**i** Find the values of $a$ and $b$. `[5]`

**ii** When $a$ and $b$ have these values, solve the equation $\mathrm{p}(x)=0$. `[4]`

*Cambridge International AS and A Level Mathematics 9709 Paper 21 Q7 November 2010*

<a id="ch03-cross-q17"></a>
##### Question 17
**i** The polynomial $x^{3}+a x^{2}+b x+8$, where $a$ and $b$ are constants, is denoted by $\mathrm{p}(x)$.

It is given that when $\mathrm{p}(x)$ is divided by ( $x-3$ ) the remainder is 14, and that when $\mathrm{p}(x)$ is divided by $(x+2)$ the remainder is 24. Find the values of $a$ and $b$. `[5]`

**ii** When $a$ and $b$ have these values, find the quotient when $\mathrm{p}(x)$ is divided by $x^{2}+2 x-8$ and hence solve the equation $\mathrm{p}(x)=0$. `[4]`

*Cambridge International AS \& A Level Mathematics 9709 Paper 21 Q4 November 2013*

<a id="ch03-cross-q18"></a>
##### Question 18
**i** Given that $(x+2)$ and $(x+3)$ are factors of $5 x^{3}+a x^{2}+b$, find the values of the constants $a$ and $b$. `[4]`

**ii** When $a$ and $b$ have these values, factorise $5 x^{3}+a x^{2}+b$ completely, and hence solve the equation $5^{3 y+1}+a \times 5^{2 y}+b=0$, giving any answers correct to 3 significant figures. `[5]`

*Cambridge International AS \& A Level Mathematics 9709 Paper 21 Q5 November 2014*

<a id="ch03-cross-q19"></a>
##### Question 19
**i** Find the quotient and remainder when $x^{4}+x^{3}+3 x^{2}+12 x+6$ is divided by $\left(x^{2}-x+4\right)$. `[4]`

**ii** It is given that, when $x^{4}+x^{3}+3 x^{2}+p x+q$ is divided by $\left(x^{2}-x+4\right)$, the remainder is zero. Find the values of the constants $p$ and $q$. `[2]`

**iii** When $p$ and $q$ have these values, show that there is exactly one real value of $x$ satisfying the equation $x^{4}+x^{3}+3 x^{2}+p x+q=0$ and state what that value is. `[3]`

*Cambridge International AS \& A Level Mathematics 9709 Paper 21 Q6 November 2015*

<a id="ch03-cross-q20"></a>
##### Question 20
The angle $\alpha$ lies between 0° and 90° and is such that $2 \tan ^{2} \alpha+\sec ^{2} \alpha=5-4 \tan \alpha$.

**i** Show that $3 \tan ^{2} \alpha+4 \tan \alpha-4=0$ and hence find the exact value of $\tan \alpha$. `[4]`

**ii** It is given that the angle $\beta$ is such that $\cot (\alpha+\beta)=6$. Without using a calculator, find the exact value of $\cot \beta$. `[5]`

*Cambridge International AS \& A Level Mathematics 9709 Paper 21 Q7 November 2014*

<a id="ch03-cross-q21"></a>
##### Question 21
**i** Express $5 \sin 2 \theta+2 \cos 2 \theta$ in the form $R \sin (2 \theta+\alpha)$, where $R>0$ and $0^{\circ}<\alpha<90^{\circ}$, giving the exact value of $R$ and the value of $\alpha$ correct to 2 decimal places.

Hence `[3]`

ii solve the equation $5 \sin 2 \theta+2 \cos 2 \theta=4$, giving all solutions in the interval $0^{\circ} \leqslant \theta \leqslant 360^{\circ}$, `[5]`

iii determine the least value of $\frac{1}{(10 \sin 2 \theta+4 \cos 2 \theta)^{2}}$ as $\theta$ varies. `[2]`

*Cambridge International AS \& A Level Mathematics 9709 Paper 21 Q7 June 2013*

<a id="ch03-cross-q22"></a>
##### Question 22
The polynomial $\mathrm{p}(x)$ is defined by $\mathrm{p}(x)=a x^{3}+3 x^{2}+b x+12$, where $a$ and $b$ are constants.

It is given that $(x+3)$ is a factor of $\mathrm{p}(x)$. It is also given that the remainder is 18 when $\mathrm{p}(x)$ is divided by $(x+2)$.

**i** Find the values of $a$ and $b$. `[5]`

**ii** When $a$ and $b$ have these values,

a show that the equation $\mathrm{p}(x)=0$ has exactly one real root, `[4]`

b solve the equation $\mathrm{p}(\sec y)=0$ for $-180^{\circ}<y<180^{\circ}$. `[3]`

*Cambridge International AS \& A Level Mathematics 9709 Paper 21 Q7 November 2016*
