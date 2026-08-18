# Implementation

## 1. Overview

The mathematical estimator

$$
\hat{\pi}=4\frac{K}{N}
$$

is implemented using Python and NumPy.

The project contains two implementations:

- A naive Python implementation using explicit loops.
- A vectorized implementation using NumPy array operations.

Both implementations perform the same mathematical computation.

## 2. Random Number Generation

The simulation generates points uniformly from the unit square

$$
[0,1]^2.
$$

A NumPy random number generator is used to generate the coordinates.

The application exposes the random seed to the user through the Streamlit interface.

A fixed seed allows the same computational experiment to be reproduced.

For example, using the same seed and number of points produces the same sequence of pseudo-random values and therefore the same estimate.

## 3. Naive Implementation

The initial implementation processed points individually.

Conceptually, the algorithm is:

1. Generate an $x$ coordinate.
2. Generate a $y$ coordinate.
3. Determine whether the point satisfies

   $$
   x^2+y^2\leq1.
   $$

4. Increment the number of points inside the quarter circle.
5. Repeat for all $N$ points.
6. Calculate

   $$
   \hat{\pi}=4K/N.
   $$

This implementation directly mirrors the mathematical definition of the estimator.

## 4. Vectorized Implementation

The current implementation uses NumPy vectorization.

Instead of processing each point individually, arrays of coordinates are generated and mathematical operations are performed on the arrays.

The conceptual computation becomes:

$$
X^2+Y^2
$$

for all generated points simultaneously.

A Boolean condition identifies the points satisfying

$$
X^2+Y^2\leq1.
$$

The number of successful points is then used to calculate the estimator.

## 5. Why Vectorization?

The mathematical algorithm did not change when moving from the naive implementation to the vectorized implementation.

The difference is computational.

The naive implementation relies heavily on Python-level iteration, while the vectorized implementation delegates array operations to optimized numerical routines provided by NumPy.

The performance difference is investigated in the benchmark section.

## 6. Streamlit Interface

The Streamlit interface intentionally provides a small number of user-controlled parameters.

The user can select:

- A random seed.
- A predetermined number of points.

Restricting the number of available sample sizes keeps the application simple and makes it easier to compare experiments consistently.

The interface is intended primarily as an interactive demonstration of the underlying mathematical and computational method rather than as a general-purpose Monte Carlo library.