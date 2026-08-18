# Testing

## 1. Testing Philosophy

The test suite is designed to verify both the software behavior and important mathematical properties of the Monte Carlo estimator.

Tests are implemented using `pytest`.

The goal is not simply to verify that the program executes successfully, but to verify that the implementation satisfies properties expected from the mathematical model.

## 2. Estimator Bounds

The estimator is defined by

$$
\hat{\pi}=4\frac{K}{N}
$$

where

$$
0\leq K\leq N.
$$

Therefore,

$$
0\leq\hat{\pi}\leq4.
$$

The test suite verifies that generated estimates satisfy this bound.

This test checks a mathematical invariant rather than a specific numerical value.

## 3. Reproducibility

The simulation uses a user-provided random seed.

The test suite verifies that running the estimator with the same seed produces the same result.

Conceptually,

$$
\operatorname{estimate}(N,s)
=
\operatorname{estimate}(N,s)
$$

for the same number of points $N$ and seed $s$.

The test suite also verifies that changing the seed can produce a different computational result.

## 4. Edge Cases

The test suite includes cases designed to evaluate behavior near the boundaries of valid input.

Examples include:

- Small numbers of points.
- Different valid seeds.
- Boundary values for supported sample sizes.
- Invalid input where applicable.

These tests help ensure that the implementation behaves predictably outside of the typical demonstration cases.

## 5. Continuous Integration

The project uses a CI workflow to automatically execute the test suite when changes are pushed to the `main` branch.

The purpose of CI is to catch regressions automatically.

The development workflow is therefore:

```text
Modify code
    ↓
Commit changes
    ↓
Push to main
    ↓
CI executes pytest
    ↓
Tests pass or failure is reported