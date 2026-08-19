# Monte Carlo Estimation of π

## Overview

This project implements a Monte Carlo method for estimating the value of $\pi$ using uniformly distributed random points.

The project was developed to explore the relationship between mathematical theory, numerical computation, software implementation, and empirical performance.

The application provides an interactive Streamlit interface where users can:

- Select a random seed.
- Select a predetermined number of points.
- Run the Monte Carlo simulation.
- Compare between Monte Carlo and Quasi Monte Carlo Methods
- View the resulting estimate of $\pi$.
- View the convergence of estimates towards $\pi$
- View the convergence of the absolute error of estimates against the theoretical decay
- View distribution plots for the estimates of $\pi$

The project also includes an automated test suite and performance benchmarks comparing a naive Python implementation with a vectorized NumPy implementation.

## Mathematical Approach

The estimator is based on the ratio between the area of a quarter circle and the area of its enclosing unit square.

For a point $(x,y)$ uniformly distributed on $[0,1]^2$, the point lies inside the quarter circle when

$$
x^2+y^2 \leq 1.
$$

If $N$ points are generated and $K$ points fall inside the quarter circle, then the estimate is

$$
\hat{\pi}=4\frac{K}{N}.
$$

A more detailed derivation is provided in the [Mathematical Foundation](mathematics.md) section.

## Computational Approach

Two implementations were developed:

1. An inital naive implementation using Python loops.
2. A vectorized implementation using NumPy operations.

The mathematical estimator is identical in both implementations. The primary difference is how the computation is performed.

The performance of the two implementations is evaluated using benchmarks. [Benchmarks](benchmark.md)

## Project Goals

The primary goals of this project are to:

- Implement a Monte Carlo estimator for $\pi$.
- Understand the mathematical basis of the estimator.
- Investigate convergence and estimation error.
- Compare Monte Carlo and Quasi Monte Carlo methods
- Compare naive and vectorized implementations.
- Develop reproducible computational experiments.
- Practice automated testing with `pytest`.
- Integrate automated testing into a CI pipeline.
- Document both mathematical and software design decisions.

## Documentation

- [Mathematical Foundation](mathematics.md)
- [Implementation](implementation.md)
- [Testing](test.md)
- [Benchmarks](bench.md)