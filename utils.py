import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import qmc

def estimate_pi(numPoints, rng):
     
    x=rng.random(numPoints)
    y=rng.random(numPoints)
    inside = (x*x + y*y) <= 1
    pi_hat = 4 *inside.mean()
    
    return round(pi_hat,5)

def estimate_pi_sobol(samples):
   sampler = qmc.Sobol(d=2, scramble=True, seed = np.random.randint(1e9))
   points = sampler.random(samples)

   x=points[:,0]
   y=points[:,1]
   inside = (x*x + y*y)<=1
   pi_hat = 4 * inside.mean()

   return round(pi_hat,5),points
    
def error(pi):
    return (f"Error = {abs(round(pi-np.pi,4))}"),abs(round(pi-np.pi,4))

def mean_estimates_and_error(samples,rng):

    estimates = np.empty(500)
    sobol_estimates = np.empty(500)
    errors = np.empty(500)
    sobol_errors = np.empty(500)
    y_converge = []
    ys_converge = []
    y_mae = []
    ys_mae = []
    pi = np.pi

    for num in samples:
        for i in range(500):
            pi_hat = estimate_pi(num,rng)
            sobol_pi_hat,points = estimate_pi_sobol(num)

            estimates[i] = pi_hat
            sobol_estimates[i] = sobol_pi_hat
            errors[i] = abs(pi_hat-pi)
            sobol_errors[i] = abs(sobol_pi_hat-pi)

        y_converge.append(estimates.mean())
        ys_converge.append(sobol_estimates.mean())
        y_mae.append(errors.mean())
        ys_mae.append(sobol_errors.mean())

    return y_converge,ys_converge,y_mae,ys_mae

def visualize_pi(n_points,pi,rng):
    x=rng.random(n_points)
    y=rng.random(n_points)
    inside = (x*x + y*y) <= 1
    
    
    
    fig, ax = plt.subplots(figsize=(6, 6))
    
    # Plot points inside the circle in blue, outside in red
    ax.scatter(x[inside], y[inside], color='dodgerblue', s=5, label='Inside')
    ax.scatter(x[~inside], y[~inside], color='tomato', s=5, label='Outside')
    
    # Add a visual boundary for the quarter-circle
    circle = plt.Circle((0, 0), 1, color='black', fill=False, linewidth=2)
    ax.add_patch(circle)
    
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.legend()
    ax.set_title(f"$\\pi$ ({pi}) Estimation with {n_points} points")
    return fig
    
def visualize_pi_sobol(pi,points):
    x=points[:,0]
    y=points[:,1]
    inside = (x*x + y*y )<= 1

    fig, ax = plt.subplots(figsize=(6,6))

    ax.scatter(x[inside], y[inside], color='dodgerblue', s=5, label='Inside')
    ax.scatter(x[~inside], y[~inside], color='tomato', s=5, label='Outside')
    
    # Add a visual boundary for the quarter-circle
    circle = plt.Circle((0, 0), 1, color='black', fill=False, linewidth=2)
    ax.add_patch(circle)
    
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.legend()
    ax.set_title(f"$\\pi$ ({pi}) Estimation with {len(points)} points")
    return fig


def visualize_convergence(xcoords,ycoords,yscoords):
    
    fig, ax = plt.subplots(figsize=(6,6))
    
    #Plot points to show convergence of Pi estimates
    ax.plot(xcoords,ycoords,color='dodgerblue',label='Mean Estimates')
    ax.plot(xcoords,yscoords,color='indigo',label='Mean Estimates(SOBOL)')
    
    #Add boundary for Pi
    ax.axhline(y=np.pi,color='tomato',linestyle='--',linewidth=1.5,label='Pi')

    ax.set_xscale("log")
    ax.set_xlim(10,1000000)
    ax.set_ylim(3.0,3.6)
    ax.margins(x=0.05)
    ax.legend()
    ax.set_title(f"Convergence Plot of Pi")
    return fig

def visualize_mae(xcoord,ycoord,yscoord):

    
    yt = [pow(xt,-0.5) for xt in xcoord]
    yst =[pow(xt,-1) for xt in xcoord]

    fig, ax = plt.subplots(figsize=(6,6))

    ax.plot(xcoord,ycoord,color="indigo",linestyle='-',linewidth=2,label='MAE')
    ax.plot(xcoord,yscoord,color="tomato",linestyle='-',linewidth=2,label="MAE (SOBOL)")
    ax.plot(xcoord,yt,color="black",linestyle='-.',linewidth=2,label='Theoretical Absolute Error')
    ax.plot(xcoord,yst,color="green",linestyle='-.',linewidth=2,label='Theoretical Absolute Error(SOBOL)')

    ax.margins(x=0.05)
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_ylim(1e-4,1e0)
    ax.set_xlim(10,100000)
    ax.legend()
    ax.set_title(f"Absolute Error vs Sample Size")
    return fig

def histogram(estimates,sobol_estimates,bins):

    fig,ax = plt.subplots(figsize=(6,6))
    ax.hist(estimates,bins=bins,alpha=0.6,density=True,color='dodgerblue',edgecolor='black',label='MC')
    ax.hist(sobol_estimates,bins=bins,alpha=0.6,density=True,color='tomato',edgecolor='black',label='SOBOL')
    ax.axvline(x=np.pi,color='black',linestyle='--',linewidth=1.5,label='Pi')
    ax.legend()
    ax.set_title(f"Comparison of Estimates: N=1000; Number of Samples = 100")
    return fig

def mse(estimates,mean,n_points):
    error = [(x-mean) for x in estimates]
    sq_error = [x**2 for x in error]
    sum = np.sum(sq_error)
    msqe=sum/n_points
    return round(msqe,5)

def mae(errors,n_points):
    sum = np.sum(errors)
    maer = sum/n_points
    return round(maer,5)

def descriptive_stats(estimates: np.array,errors: np.array):
    
    mean = estimates.mean()
    msqe= mse(estimates,mean,len(estimates))
    maer = mae(errors,len(errors))
    var = (estimates.std())**2
    sd = estimates.std()
    min_est=estimates.min()
    max_est=estimates.max()

    return round(mean,5), msqe,maer, round(var,5),round(sd,5),min_est, max_est

def repeated_sims(rng):
    estimates = np.empty(1000)
    sobol_estimates = np.empty(1000)
    errors = np.empty(1000)
    sobol_errors = np.empty(1000)
    pi = np.pi

    for i in range(1000):
        pi_hat = estimate_pi(1000,rng)
        pi_hat_sobol,points = estimate_pi_sobol(1000)
        err = abs(pi_hat-pi)
        sobol_error = abs(pi_hat_sobol-pi)

        estimates[i] = pi_hat
        errors[i] = err
        sobol_estimates[i] = pi_hat_sobol
        sobol_errors[i] = sobol_error


    fig = histogram(estimates,sobol_estimates,10)
    st.pyplot(fig)

    st.subheader("Results",text_alignment='center')
    mean,msqe,maer,var,sd,min_est,max_est = descriptive_stats(estimates,errors)
    sobol_mean,sobol_msqe,sobol_maer,sobol_var,sobol_sd,sobol_min_est,sobol_max_est = descriptive_stats(sobol_estimates,sobol_errors)

    col1, col2 = st.columns(2)
    with col1:
        st.metric("MC Mean Estimate",value=f"{mean}",delta=f"{np.pi}",border=True)
        st.metric("MC VAR",value=f"{var}",border=True)
        st.metric("MC STDEV",value=f"{sd}",border=True)

    with col2:
        st.metric("SOBOL Mean Estimate",value=f"{sobol_mean}",delta=f"{np.pi}",border=True)
        st.metric("SOBOL VAR",value=f"{sobol_var}",border=True)
        st.metric("SOBOL STDEV",value=f"{sobol_sd}",border=True)

    stats = {
        "Method":['Monte Carlo','SOBOL'],
        "Mean Estimate":[mean,sobol_mean],
        "Mean Squared Error":[msqe,sobol_msqe],
        "Mean Average Error":[maer,sobol_maer],
        "Variance":[var,sobol_var],
        "Standard Deviation":[sd,sobol_sd],
        "Min Estimate":[min_est,sobol_min_est],
        "Max Estimate":[max_est,sobol_max_est]
    }
    table1 = pd.DataFrame(stats)
    st.dataframe(table1)

def plots(samples,rng):
    
    
    y_converge,ys_converge,y_mae,ys_mae = mean_estimates_and_error(samples,rng)

       

    convergence_fig = visualize_convergence(samples,y_converge,ys_converge)
    st.pyplot(convergence_fig)
    error_fig = visualize_mae(samples,y_mae,ys_mae)
    st.pyplot(error_fig)

def estimation(selected_points,rng):
    pi = np.pi

    estimate = estimate_pi(selected_points,rng)
    err = abs(estimate-pi)

    estimate_sobol,points = estimate_pi_sobol(selected_points)
    err_sobol = abs(estimate_sobol-pi)

    col1,col2 = st.columns(2)

    with col1:
        st.metric("π",value=f"{estimate}",delta=f"{np.pi}",border=True)
        st.metric("Abs Error",value=f"{round(err,5)}",border=True)
        fig = visualize_pi(selected_points,estimate,rng)
        st.pyplot(fig)


    with col2:
        st.metric("π (SOBOL)",value=f"{estimate_sobol}",delta=f"{np.pi}",border=True)
        st.metric("Abs Error (SOBOL)",value=f"{round(err_sobol,5)}",border=True)
        fig_sobol = visualize_pi_sobol(estimate_sobol,points)
        st.pyplot(fig_sobol)

    st.subheader(f"How it works",text_alignment='center')
    st.write(
        "The Monte Carlo method uses random sampling to estimate π. We generate random points ina  unit square (0 to 1) on both axes" \
        "and check whether the poin falls within a quarter of the unit circle(radius=1)." \
        "The ratio of points within the quarter circle produces an estimate of the quarter circle's area" \
        "to the square's area. Thus multiplying by 4 gives us π.\n" \
        "A of Quarter Circle = πr^2/4 when radius = 1 \n" \
        "A of Unit Square =1" \
        "=> π = 4 * A of Quarter Circle = points inside/points outside")

    
       









