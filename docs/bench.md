
### `benchmarks.md`

```md
# Performance Benchmarks

## 1. Purpose

The project compares the execution time of two implementations of the Monte Carlo estimator:

1. A naive Python loop implementation.
2. A vectorized NumPy implementation.

The mathematical algorithm is identical in both cases.

The purpose of the benchmark is to investigate how the computational implementation affects performance.

## 2. Experimental Setup

For each implementation, the estimator is evaluated using increasing numbers of generated points.

The execution time is measured for each input size.

The same general computational task is performed by both implementations so that their execution times can be compared.

## 3. Naive Implementation

The naive implementation processes individual points using Python-level iteration.

Its conceptual structure is:

```text
for each point:
    determine whether point is inside quarter circle
    update count