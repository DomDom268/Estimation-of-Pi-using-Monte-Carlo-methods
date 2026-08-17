import streamlit as st
import numpy as np
import pandas as pd
import utils as u
import vector as v
from scipy.stats import qmc





st.title("Monte Carlo Estimation of π")

#User input for seed 
seed = st.sidebar.number_input("Insert a Seed",min_value=0,max_value=1000000,value=None,step=1)
rng = np.random.default_rng(seed=seed)
sampler = qmc.Sobol(d=2,scramble=True,seed=seed)

points = [10,100,1000,10000,100000]
selected_points = st.sidebar.radio(
    "Select number of points generated",
    points,
    horizontal=False
)

if st.sidebar.button(f"Estimate Pi with {selected_points} generated"):
    u.estimation(selected_points,rng)
    

if st.sidebar.button("Plot convergence of average estimate for 1000 simulations"):
    mc_est,mc_err = u.simulations(rng,points)
    qmc_est,qmc_err = u.qmc_simulations(sampler,points)

    convergence_fig = v.pi_convergence(mc_est,qmc_est,points)
    st.pyplot(convergence_fig)

if st.sidebar.button("Plot convergence of mae for 1000 simulations"):
    mc_est,mc_err = u.simulations(rng,points)
    qmc_est,qmc_err = u.qmc_simulations(sampler,points)

    mae_fig = u.mae_convergence(mc_err,qmc_err,points)
    st.pyplot(mae_fig)

if st.sidebar.button(f"Plot distribution of estimates over 1000 simulations for {selected_points} generated"):
    fig = u.histogram2(rng,sampler,selected_points)
    st.pyplot(fig)



    



