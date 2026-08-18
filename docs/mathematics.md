# Mathematical Foundation

## 1. Geometric Interpretation

The Monte Carlo estimator for $\pi$ is based on the area of a quarter circle with radius $1$.

The area of a full circle is

$$
A=\pi r^2.
$$

For $r=1$,

$$
A=\pi.
$$

Therefore, the area of a quarter circle is

$$
A_{\text{quarter}}=\frac{\pi}{4}.
$$

Consider the unit square

$$
[0,1]\times[0,1].
$$

Its area is

$$
A_{\text{square}}=1.
$$

The probability that a uniformly distributed point $(X,Y)$ in the unit square falls inside the quarter circle is therefore

$$
P(X^2+Y^2\leq1)
=
\frac{\pi/4}{1}
=
\frac{\pi}{4}.
$$

This relationship allows $\pi$ to be estimated using randomly generated points.

## 2. Monte Carlo Estimator

Suppose that $N$ independent points

$$
(X_1,Y_1),\ldots,(X_N,Y_N)
$$

are generated uniformly from the unit square.

Define the indicator variable

$$
I_i =
\begin{cases}
1, & X_i^2+Y_i^2\leq1,\\
0, & X_i^2+Y_i^2>1.
\end{cases}
$$

The number of points inside the quarter circle is

$$
K=\sum_{i=1}^{N}I_i.
$$

The proportion of points inside the quarter circle is therefore

$$
\frac{K}{N}.
$$

Since this proportion estimates $\pi/4$, the Monte Carlo estimator for $\pi$ is

$$
\boxed{
\hat{\pi}=4\frac{K}{N}
}
$$

or equivalently,

$$
\hat{\pi}
=
\frac{4}{N}
\sum_{i=1}^{N}I_i.
$$

## 3. Expected Value

Since each $I_i$ is a Bernoulli random variable with

$$
p=P(X_i^2+Y_i^2\leq1)=\frac{\pi}{4},
$$

we have

$$
E[I_i]=\frac{\pi}{4}.
$$

Therefore,

$$
E[\hat{\pi}]
=
E\left[
\frac{4}{N}
\sum_{i=1}^{N}I_i
\right].
$$

By linearity of expectation,

$$
E[\hat{\pi}]
=
\frac{4}{N}
\sum_{i=1}^{N}E[I_i].
$$

Thus,

$$
E[\hat{\pi}]
=
\frac{4}{N}
\left(
N\frac{\pi}{4}
\right)
=
\pi.
$$

Therefore,

$$
\boxed{E[\hat{\pi}]=\pi}
$$

and the estimator is unbiased.

## 4. Convergence

By the Law of Large Numbers,

$$
\frac{1}{N}\sum_{i=1}^{N}I_i
\rightarrow
E[I_i]
=
\frac{\pi}{4}
$$

as $N\rightarrow\infty$.

Consequently,

$$
\hat{\pi}
=
4\frac{1}{N}
\sum_{i=1}^{N}I_i
\rightarrow
\pi.
$$

Thus, increasing the number of samples causes the Monte Carlo estimate to converge toward $\pi$.

However, convergence does not imply that every individual estimate becomes progressively closer to $\pi$. Because the method is stochastic, individual estimates may fluctuate.

## 5. Variance and Error

Because $I_i$ is Bernoulli with

$$
p=\frac{\pi}{4},
$$

its variance is

$$
\operatorname{Var}(I_i)
=
p(1-p).
$$

Therefore,

$$
\operatorname{Var}(\hat{\pi})
=
\frac{16}{N}
p(1-p).
$$

Substituting $p=\pi/4$ gives

$$
\operatorname{Var}(\hat{\pi})
=
\frac{16}{N}
\frac{\pi}{4}
\left(1-\frac{\pi}{4}\right).
$$

Simplifying,

$$
\boxed{
\operatorname{Var}(\hat{\pi})
=
\frac{4\pi}{N}
\left(1-\frac{\pi}{4}\right)
}
$$

and therefore the standard deviation satisfies

$$
\operatorname{SD}(\hat{\pi})
=
\sqrt{
\frac{4\pi}{N}
\left(1-\frac{\pi}{4}\right)
}.
$$

The important computational consequence is that the standard error decreases at a rate proportional to

$$
\frac{1}{\sqrt{N}}.
$$

Therefore, substantially more samples are required to obtain additional digits of accuracy.

## 6. Estimator Bounds

The number of points inside the quarter circle satisfies

$$
0\leq K\leq N.
$$

Therefore,

$$
0\leq\frac{K}{N}\leq1.
$$

Multiplying by $4$ gives

$$
0\leq\hat{\pi}\leq4.
$$

This provides a simple mathematical invariant that can be verified through automated testing.

## 7. Limitations

Although the estimator converges to $\pi$, Monte Carlo methods have relatively slow convergence.

The standard error decreases according to

$$
O(N^{-1/2}).
$$

Consequently, reducing the error by a factor of $10$ generally requires approximately $100$ times as many samples.

The method is therefore useful for demonstrating probabilistic numerical computation, but it is not an efficient method for computing many digits of $\pi$.