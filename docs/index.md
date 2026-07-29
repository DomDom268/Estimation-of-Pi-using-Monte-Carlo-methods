# Monte Carlo Estimation of π

This project is an interactive web application built with Streamlit that demonstrates how to estimate π using a Monte Carlo simulation. Users can experiment with different sample sizes and visually observe how the approximation improves as the number of random points increases.

---

## 🚀 Live Demo

*Streamlit deployment coming soon*

---

## 📌 Overview

The Monte Carlo method estimates π by randomly generating points inside a unit square and measuring how many fall inside a quarter circle.

Since:

* Area of quarter circle = π/4
* Area of square = 1

We can estimate:

π ≈ 4 × (points inside circle / total points)

This app allows users to explore this concept interactively.

---

## ❓Why Monte Carlo

Monte Carlo simulations and integration are an integral part of various technical fields such as scientific computing, finance (risk management) and bayesian machine learning
as it provides a trivial way to approximate possible deterministic events using randomness. As a prospective mathematics graduate student, I was interested in utilizig this
numerical method as I find fascinating how geometry and stochastics could be used to approximate such a pivotal mathematical figure in Pi.

## 🧠 Features

* Select number of simulation points:

  * 10, 100, 1,000, 10,000, 100,000, 1,000,000
* Real-time estimation of π
* Error calculation vs true value of π
* Visual scatter plot:

  * Points inside the circle
  * Points outside the circle
* Visual convergence plot:
  * Estimation of pi at different number of samples
  * Numpy Pi reference boundary
* Visual Absolute Error line plot:
  * Absolute error of each estimate at different number of samples
* Histogram plot:
  * Shows distribution of estimates after running experiment 1000 times
  * Shows Central Limit Theorem in action as the ratio mimics a Bernoulli distribution(0-inside circle;1-outside cirlce)
  * Shows descriptive statistics(mean, min,max, std dev,mse)
* Clean and interactive UI powered by Streamlit


---

## 🛠️ Tech Stack

* Python
* NumPy
* Matplotlib
* Streamlit

---