# 🎯 Monte Carlo Estimation of π (Interactive App)

This project is an interactive web application built with Streamlit that demonstrates how to estimate π using a Monte Carlo simulation. Users can experiment with different sample sizes and visually observe how the approximation improves as the number of random points increases.

---

## 🚀 Live Demo

*(Add your Streamlit link here after deployment)*

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

## 🧠 Features

* Select number of simulation points:

  * 10, 100, 1,000, 10,000, 100,000, 1,000,000
* Real-time estimation of π
* Error calculation vs true value of π
* Visual scatter plot:

  * Points inside the circle
  * Points outside the circle
* Clean and interactive UI powered by Streamlit

---

## 🛠️ Tech Stack

* Python
* NumPy
* Matplotlib
* Streamlit

---

## 📊 Example Output

* Estimated π value
* Absolute error from true π
* Visualization of random sampling and geometric boundary

---

## 🧪 How It Works

1. Generate `n` random points uniformly in the unit square

2. Compute distance from origin for each point

3. Count how many points lie inside the quarter circle

4. Estimate π using:

   π ≈ 4 × (inside / total)

5. Visualize results

---

## ▶️ Running Locally

Clone the repository:

```bash
git clone https://github.com/your-username/monte-carlo-pi.git
cd monte-carlo-pi
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the app:

```bash
streamlit run app.py
```

---

## 📈 Future Improvements

* Convergence plot (error vs number of points)
* Animation of point generation
* Log-scale visualization of error decay
* Extension to higher-dimensional Monte Carlo integration

---

## 🧩 Key Takeaways

This project demonstrates:

* Monte Carlo simulation techniques
* Numerical approximation methods
* Visualization of stochastic processes
* Building interactive data apps

---

## 👤 Author

Dominic Christopher
HBA Candidate | Data & Quantitative Analysis Enthusiast

---

## ⭐ Acknowledgements

Inspired by classical Monte Carlo methods used in physics, finance, and computational mathematics.
