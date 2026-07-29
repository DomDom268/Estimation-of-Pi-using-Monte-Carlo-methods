import streamlit as st
import numpy as np
import utils as u





st.title("Monte Carlo Estimation of π")

#User input for seed 
seed = st.sidebar.number_input("Insert a Seed",min_value=0,max_value=1000000,value=None,step=1)
rng = np.random.default_rng(seed=seed)

points = [10,100,1000,10000,100000,1000000]
selected_points = st.sidebar.radio(
    "Select number of poitns generated",
    points,
    horizontal=False
)

if st.sidebar.button("Run Simulation"):
    estimate = u.estimate_pi(selected_points,rng)
    err_message,err = u.error(estimate)

    estimate_sobol = u.estimate_pi_sobol(selected_points)
    err_message_sobol,err_sobol = u.error(estimate_sobol)

    st.subheader(f"Estimated π: {round(estimate, 6)}")
    st.write(f"{err_message}")

    fig = u.visualize_pi(selected_points,estimate,rng)
    st.pyplot(fig)

    st.subheader(f"How it works",text_alignment='center')
    st.write(
        "The Monte Carlo method uses random sampling to estimate π. We generate random points ina  unit square (0 to 1) on both axes" \
        "and check whether the poin falls within a quarter of the unit circle(radius=1)." \
        "The ratio of points within the quarter circle produces an estimate of the quarter circle's area" \
        "to the square's area. Thus multiplying by 4 gives us π.\n" \
        "A of Quarter Circle = πr^2/4 when radius = 1 \n" \
        "A of Unit Square =1" \
        "=> π = 4 * A of Quarter Circle = points inside/points outside")

    st.subheader(f"Estimated π using SOBOL Sequence: {round(estimate_sobol, 6)}")
    st.write(f"{err_message_sobol}")
    
    fig_sobol = u.visualize_pi(selected_points,estimate_sobol,rng)
    st.pyplot(fig_sobol)
    
if st.sidebar.button("Plot Convergence"):

    convergence_coords,error_coords,convergence_coords_sobol,error_coords_sobol = u.convergence(points,rng)
    fig = u.visualize_convergence(convergence_coords,convergence_coords_sobol)
    st.pyplot(fig)

if st.sidebar.button("Plot Absolute Error"):

    convergence_coords,error_coords,convergence_coords_sobol,error_coords_sobol = u.convergence(points,rng)
    fig = u.visualize_error(error_coords,error_coords_sobol)
    st.pyplot(fig)

if st.sidebar.button("Run 1000 Repeated Simulations"):
    estimates = []
    sobol_estimates = []

    for i in range(1000):
        estimates.append(u.estimate_pi(10000,rng))
        sobol_estimates.append(u.estimate_pi_sobol(10000))

    fig = u.histogram(estimates,10)
    st.pyplot(fig)

    mean,msqe,sd,min_est,max_est = u.descriptive_stats(estimates)

    st.subheader(f"Mean= {mean}") 
    st.subheader(f"Mean Squared Error: {msqe}")
    st.subheader(f"Standard Deviation: {sd}")
    st.subheader(f"Min:{min_est}")
    st.subheader(f"Max:{max_est}")

    st.subheader("SOBOL Results",text_alignment='center')
    #SOBOL 
    sobol_fig = u.histogram(sobol_estimates,10)
    st.pyplot(sobol_fig)
    
    sobol_mean,sobol_msqe,sobol_sd,sobol_min_est,sobol_max_est = u.descriptive_stats(sobol_estimates)

    st.subheader(f"Mean= {sobol_mean}") 
    st.subheader(f"Mean Squared Error: {sobol_msqe}")
    st.subheader(f"Standard Deviation: {sobol_sd}")
    st.subheader(f"Min:{sobol_min_est}")
    st.subheader(f"Max:{sobol_max_est}")


    



