# Benchmarking Execution Time

## Overview

This project benchmarks two implementations of the Monte Carlo estimator for \( \pi \):

1. **Naive implementation** — generates random points and checks each point individually using Python loops.
2. **Vectorized implementation** — performs the same computation using NumPy array operations.

The purpose of the benchmark is to demonstrate the performance benefit of vectorization while confirming that both implementations perform the same mathematical computation.

The benchmark measures *execution time* and *speedup ratio* for a set number of points generated
---

## Mathematical Problem

The estimator samples points uniformly from the unit square

$$
[0,1]^2.
$$

A point \( (x,y) \) is inside the quarter circle when

$$
x^2 + y^2 \leq 1.
$$

The area of the quarter circle is

$$
\frac{\pi}{4}.
$$

Therefore, if \(N\) points are generated and \(N_{\text{inside}}\) fall inside the quarter circle, the Monte Carlo estimate is

$$
\hat{\pi}
=
4\frac{N_{\text{inside}}}{N}.
$$

Both implementations use this same estimator. The benchmark therefore focuses on the computational cost of evaluating it rather than comparing different mathematical methods.

---

## Implementations

### Naive Implementation

The naive implementation processes the generated points one at a time.

Conceptually, for each point:

1. Initate trial
2. Generate \(x\) and \(y\).
2. Compute \(x^2+y^2\).
3. Determine whether the point is inside the quarter circle.
4. Increment the count if it is inside.
5. Compute the final estimate.
6. Append list of estimates
7. Initate next trial and repeat 2-6 for all trials
8. Calculate average estimate

This approach is straightforward and closely resembles the mathematical description of the algorithm.

Its main disadvantage is that the individual operations are performed through Python-level iteration.

### Vectorized Implementation

The vectorized implementation generates all points for every trial simultaneously as a matrix with shape (1,numTrials,numPoints,2).

Then the inside-circle mask is applied to all points simultaenously which creates a boolen array of shape (1,numTrials,numPoints).

The complete list of estimates is then calculated all at once.


For example, the inside-circle condition can be evaluated as

$$
x^2+y^2 \leq 1
$$

for all sampled points simultaneously.

NumPy performs these operations using optimized compiled code, avoiding the overhead of repeatedly executing the same operations in a Python loop.

---

## Benchmark Methodology

The benchmark should be run under the same environment for both implementations.

For each sample size:

1. Generate the same number of random points.
2. Run the naive implementation.
3. Run the vectorized implementation.
4. Record the execution time.
5. Repeat the measurement when appropriate to reduce the influence of temporary system load.
6. Compare the resulting execution times.

A fixed random seed can be used when reproducibility of the generated sample is important.

The benchmark is intended primarily as a **performance comparison**, so the exact estimate of \( \pi \) is secondary to the execution time.

---

## Metrics

The primary metric is **execution time**, measured in seconds.

For an input of \(N\) points, define

$$
T_{\text{naive}}(N)
$$

as the execution time of the naive implementation and

$$
T_{\text{vectorized}}(N)
$$

as the execution time of the vectorized implementation.

The speedup of the vectorized implementation can then be expressed as

$$
S(N)
=
\frac{T_{\text{naive}}(N)}
{T_{\text{vectorized}}(N)}.
$$

A value of \(S(N)=5\), for example, means that the vectorized implementation completed the benchmark approximately five times faster.

---

## Expected Results

Both implementations should have approximately the same computational behavior with respect to the number of points:

$$
T(N)=O(N).
$$

The important difference is the constant factor associated with how the work is performed.

The naive implementation performs the repeated operations through Python iteration, while the vectorized implementation delegates bulk numerical operations to NumPy.

Consequently, the vectorized implementation is expected to become increasingly advantageous as the number of generated points increases.

Small inputs may show a smaller difference because fixed overhead can represent a larger fraction of the total execution time.

---

## Example Results

|Method|Execution Time|Speedup|
|:------|:------|:------|
|Naive Loops|0.1792s|1.0x|
|Vectorized MC|0.0072s|24.8x|
|Vectorized QMC|0.0156s|11.5x|

---

## Interpreting the Benchmark

The benchmark should not be interpreted as showing that vectorization changes the underlying Monte Carlo algorithm.

Both implementations perform the same mathematical procedure:

$$
\hat{\pi}
=
4\frac{N_{\text{inside}}}{N}.
$$

The performance improvement comes from **how the computation is implemented**.

This provides a useful example of the distinction between:

- **Algorithmic complexity** — both implementations are \(O(N)\).
- **Implementation efficiency** — vectorized numerical operations can have substantially lower constant overhead than Python-level loops.

This distinction is important when implementing computational mathematics algorithms in Python.

---

## Reproducibility

The project accepts a user-defined random seed. Using the same seed and sample size allows the random-number generation process to be reproduced.

The test suite verifies seed reproducibility separately from the performance benchmark.

Benchmark results themselves may vary between runs because of:

- CPU load
- operating-system scheduling
- Python and NumPy versions
- hardware differences
- background processes
- memory/cache effects

Therefore, benchmark results should be interpreted as measurements for a particular computational environment rather than universal execution times.

---

## Relationship to Testing

Performance benchmarks are separate from correctness tests.

The test suite verifies properties such as:

- estimates are within the valid range \( [0,4] \);
- the same seed produces reproducible results;
- the estimator behaves consistently for supported inputs.

The benchmark instead asks:

> How efficiently can the implementation perform the computation?

Keeping these concerns separate makes the project easier to maintain and prevents performance measurements from being treated as correctness tests.

---

## Reproducing the Benchmark

The benchmark can be run using the project's benchmark script or notebook.

When reporting results, include the computational environment when possible:

- Python version
- NumPy version
- operating system
- CPU
- sample sizes
- number of repetitions
- random seed, if applicable

This information makes it easier to reproduce and interpret the measurements.

---

## Limitations

These benchmarks measure the implementations used in this project and should not be interpreted as a general comparison of all Monte Carlo implementations.

In particular, execution time can change substantially depending on:

- the random-number generator;
- the NumPy version;
- the processor;
- memory availability;
- whether random-number generation is included in the timing;
- the number of repetitions;
- the benchmarking methodology.

The benchmark also does not measure statistical convergence. Convergence and estimation error are separate mathematical properties of the Monte Carlo method.

---

## Summary

The benchmark demonstrates a central computational-mathematics lesson:

> Two implementations can have the same mathematical algorithm and the same asymptotic complexity while having very different practical execution times.

For this project, both the naive and vectorized implementations use the same Monte Carlo estimator, but vectorization reduces Python-level iteration and allows NumPy to perform bulk numerical operations efficiently.

The benchmark therefore serves as both a performance study and an example of translating a mathematical algorithm into multiple computational implementations.
