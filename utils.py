import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import qmc

num_trials=1000

@st.cache_data
def generate_xy(seed:int,numPoints: int):
    """
    Generates numPoints randomly uniformed points to be used to estimate pi

    Parameters:
    seed(int): User selected seed
    numPoints(int): Number of points to be generated

    Returns:
    x(np.ndarray): List of x points
    y(np.ndarray): List of y points
    """
    rng = np.random.default_rng(seed)

    x=rng.random(numPoints)
    y=rng.random(numPoints)

    return x,y

@st.cache_data
def generate_sobol_points(seed:int,numPoints:int):
    """
    Generates numPoints sobol sequenced points to be used to estimate pi

    Parameters:
    seed(int): User selected seed
    numPoints(int): Number of points to be generated

    Returns:
    points(np.ndarray): List of points generated
    """

    sampler = qmc.Sobol(d=2,scramble=True,seed=seed)
    points = sampler.random(numPoints)

    return points

def estimate_pi(x,y):
    """
    Calculates an estimate of pi using MC methods

    Parameters:
    x(np.ndarray): List of x points
    y(np.ndarray): List of y points
    

    Returns:
    pi_hat(flaot):Estimate of Pi
    
    """

    inside = (x*x + y*y) <= 1
    pi_hat = 4 *inside.mean()
    
    return round(pi_hat,5)

def estimate_pi_sobol(points):
   """
   Calculates an estimate of pi using QMC methods of SOBOL

   Parameters:
   points(np.ndarray): List of points generated

   Returns:
   pi_hat: Pi estimate
   
   """

   x=points[:,0]
   y=points[:,1]
   inside = (x*x + y*y)<=1
   pi_hat = 4 * inside.mean()

   return round(pi_hat,5)
    
def visualize_pi(numPoints,pi,x,y):
    """
    Visualizes MC pi estimate

    Parameter:
    pi(float): Estimate
    numPoints(int): Number of points to be generated
    x(np.darray): List of x coordinates generated
    y(np.darray): List of y coordinates generated

    Returns: 
    fig: matplotlib figure
    """
    
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
    ax.set_title(f"$\\pi$ ({pi}) Estimation with {numPoints} points")
    return fig
    
def visualize_pi_sobol(pi,points):
    """
    Visualizes QMC pi estimate

    Parameter:
    pi(float): Estimate
    points(int):Points geenrated by sampler

    Returns: 
    fig: matplotlib figure
    """
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

def mse(estimates,mean,numPoints):
    """
    Helper function to calculate mean squared error for descriptive stats function

    Parameters:
    estimates(np.darray): List of pi estimates
    mean(float): Average of the estimates
    numPoints(int): Number of points to be generated

    Returns:
    msqe(float): Mean Sqaured Error
    """
    error = [(x-mean) for x in estimates]
    sq_error = [x**2 for x in error]
    sum = np.sum(sq_error)
    msqe=sum/numPoints
    return round(msqe,5)

def mae(errors,numPoints):
    """
    Helper function to calculate mean absolute error for descriptive stats function

    Parameters"
    errors(np.darray):List of errors 
    n_points(int):number of points generated

    Returns:
    maer(float): Mean Absolute Error
    """
    sum = np.sum(errors)
    maer = sum/numPoints
    return round(maer,5)

def descriptive_stats(estimates: np.array,errors: np.array):
    """
    Calculates the mean, mean squared error, mean absolue error,
    variance,standad deviation ,max and min for the list of pi estimates
    
    Parameters:
    estimates(np.darray): A 1D array containing the estimates of pi
    errors(np.darray): A 1D array containing the errors of the estimates

    Returns:
    mean(float): average pi estimate
    msqe(float): mean squared error of the estimates
    maer(float):mean absolute error of the estimates
    var(float): variance of the pi estimates
    sd(float): standard deviation of the pi estimates
    min_est(float):minimum pi estimate
    max_est(float): maximum pi estimate
    """
    mean = estimates.mean()
    msqe= mse(estimates,mean,len(estimates))
    maer = mae(errors,len(errors))
    var = (estimates.std())**2
    sd = estimates.std()
    min_est=estimates.min()
    max_est=estimates.max()

    return round(mean,5), msqe,maer, round(var,5),round(sd,5),min_est, max_est

def estimation(selected_points,seed):
    """
    Estimates and visualizes pi using selected_points points generated 

    Parameters:
    selected_points(int): the number of points to be generated selected by the user
    rng: customr andom generator

    Returns:
    streamlit metric with the pi estimate and mae along with two figures
    """
    pi = np.pi

    x,y = generate_xy(seed,selected_points)
    pi_mc = estimate_pi(x,y)
    err = abs(pi_mc-pi)

    points = generate_sobol_points(seed,selected_points)
    pi_qmc = estimate_pi_sobol(points)
    err_sobol = abs(pi_qmc-pi)

    col1,col2 = st.columns(2)

    with col1:
        st.metric("π",value=f"{pi_mc}",delta=f"{np.pi}",border=True)
        st.metric("Abs Error",value=f"{round(err,5)}",border=True)
        fig = visualize_pi(selected_points,pi_mc,x,y)
        st.pyplot(fig)


    with col2:
        st.metric("π (SOBOL)",value=f"{pi_qmc}",delta=f"{np.pi}",border=True)
        st.metric("Abs Error (SOBOL)",value=f"{round(err_sobol,5)}",border=True)
        fig_sobol = visualize_pi_sobol(pi_qmc,points)
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

def estimate_pi_1000(points,numPoints):
    """
    Estimates pi using Monte Carlo methods for different number of points generated
    and for 1000 simulations

    Parameters:
    points(np.darray): 4D array containing the points generated for each simulation
    numPoints(int): The number of points generated

    Returns:
    pi_estimates(np.darray): A 2D matrix containing the estimate of pi for each simulation
    abs_errors(np.darray): A 2D matrix containing the absolute error for each pi estimate for each simulation
    """
    pi=np.pi
    x = points[...,0]
    y = points[...,1]
    inside_circle = (x**2+y**2)<=1

    #Calculate the estimate of pi
    pi_estimates = 4 * (np.sum(inside_circle,axis=2))/numPoints
    abs_errors = abs(pi_estimates-pi)

    return pi_estimates,abs_errors

def simulations(rng,points):
    """
    Estimates the average pi estimate at different number of points generated using Monte Carlo Methods

    Parameters:
    rng: A custom random generater 
    points:(np.darray): A 1D array containing the number of points to be generated

    Returns:
    mean(np.darray): A 1D array containing the mean pi estimate for each number of points generated in points
    mae(np.darray): A 1D array containing the mean absolute error for each number of points generated in points
    """
    mean = np.empty(len(points))
    mae = np.empty(len(points))

    #Loop through simulation with different number of points
    for i,num in zip(range(len(points)),points):
        shape=(1,num_trials,num,2)

        #Create 4D matrix to host points for each trial in 2D array
        point = rng.uniform(low=0.0,high=1.0,size=shape)

        #Call estimate_pi to receive mask
        est,err = estimate_pi_1000(point,num)


        #Update metric list
        mean[i] = round(np.mean(est),4)
        mae[i] = round(np.mean(err),4)

    return mean,mae

def qmc_simulations(sampler,points):
    """
    Estimates the average pi estimate and absolute error at different number of points generated using quasi-Monte Carlo methods(SOBOL)

    Parameters:
    sampler: A custom qmc sampler from scipy.stats.qmc
    points:(np.darray): A 1D array containing the number of points to be generated

    Returns:
    mean(np.darray): A 1D array containing the mean pi estimate for each number of points generated in points
    mae(np.darray): A 1D array containing the mean absolute error for each number of points generated in points
    """
    
    mean = np.empty(len(points))
    mae = np.empty(len(points))

    #Loop through simulation with different number of points
    for i,num in zip(range(len(points)),points):
        shape=(1,num_trials,num,2)
        total_points = num_trials*num

        #Create 2D array with sobol random points
        raw_point = sampler.random(n=total_points)

        #Reshape point array to a 4D matrix
        point = raw_point.reshape(shape)

        #Call estimate_pi
        est,err = estimate_pi_1000(point,num)

        #Update metrics
        mean[i] = round(np.mean(est),4)
        mae[i] = round(np.mean(err),4)

    return mean,mae

def pi_convergence(mc_estimates,qmc_estimates,points):
    """
    Generates a convergence plot for the estimation of pi 

    Parameters:
    mc_estimates(np.darray):A 1D array containing the estimates of pi using monte carlo methods
    qmc_estimates(np.darray): A 1D array containing the estimates of pi usign qmc methods
    points(np.darray): 1D array containing the options for the number of points generated

    Returns:
    fig: A matplotlib figure
    """

    x_coords = points
    ymc_coords = mc_estimates
    yqmc_coords = qmc_estimates

    #Create figure
    fig,ax = plt.subplots(figsize=(10,10))

    #Plot Points
    ax.plot(x_coords,ymc_coords,color='dodgerblue',label='Mean MC Estimates')
    ax.plot(x_coords,yqmc_coords,color='tomato',label='Mean QMC Estimates')

    #Add boundary line for pi
    ax.axhline(y=np.pi,color='black',linestyle='--',linewidth=3,label='Pi')

    #Customize figure
    ax.set_xscale("log")
    ax.set_xlim(10,100000)
    ax.set_xlabel("Points Generated")
    ax.set_ylim(3.13,3.16)
    ax.set_ylabel("Pi Estimate")
    ax.margins(x=0.05)
    ax.legend()
    ax.set_title('Convergence Plot of Pi')

    return fig

def mae_convergence(mc_errors,qmc_errors,points):
    """
    Generates a convergence plot for the estimation of pi 

    Parameters:
    mc_estimates(np.darray):A 1D array containing the estimates of pi using monte carlo methods
    qmc_estimates(np.darray): A 1D array containing the estimates of pi usign qmc methods
    points(np.darray): 1D array containing the options for the number of points generated

    Returns:
    fig: A matplotlib figure
    """
    x_coords = points
    ymc_coords = mc_errors
    yqmc_coords = qmc_errors

    ymc_theory = [pow(x,-0.5) for x in points]
    yqmc_theory= [pow(x,-1) for x in points]

    #Create figure
    fig,ax = plt.subplots(figsize=(10,7))

    #Plot Points
    ax.plot(x_coords,ymc_coords,color='dodgerblue',label='MC MAE')
    ax.plot(x_coords,yqmc_coords,color='tomato',label='QMC MAE')

    #Plot theoretical decay
    ax.plot(x_coords,ymc_theory,color="dodgerblue",linestyle="--",linewidth=3,label="MC Theoretical")
    ax.plot(x_coords,yqmc_theory,color="tomato",linestyle="--",linewidth=3,label="QMC Theoretical")


    #Customize figure
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlim(10,100000)
    ax.set_xlabel("Points Generated")
    ax.set_ylim(1e-5,1e0)
    ax.set_ylabel("Pi Estimate")
    ax.margins(x=0.05)
    ax.legend()
    ax.set_title('Convergence Plot of MAE')

    return fig

def histogram2(rng,sampler,numPoints):
    """
    Creates histogram to plot distribution of pi estimates for 1000 simulations at num_points points generated and 
    compare between methods

    Parameters:
    rng: custom random generator
    sampler: custom qmc sampler from scipy.stats.qmc
    num_points(int): number of points to be generated

    Returns:
    fig: matplotlib figure
    """
    
    #Create figure
    fig,ax = plt.subplots(figsize=(6,6))

   #Create 4D matrix to host points for each trial in 2D array
    shape=(1,num_trials,numPoints,2)
    total_points = num_trials*numPoints
    mc_point = rng.uniform(low=0.0,high=1.0,size=shape)
    qmc_raw = sampler.random(n=total_points)
    qmc_point=qmc_raw.reshape(shape)

    #Call estimate_pi for mc methods
    mc_est,_ = estimate_pi_1000(mc_point,numPoints)
    pi_est = mc_est.ravel()

    #Call estimate_pi for qmc methods
    qmc_est,_ = estimate_pi_1000(qmc_point,numPoints)
    pi_qmc = qmc_est.ravel()


    #Plot histogram
    ax.hist(pi_est,bins=10,alpha=0.6,density=True,color='tomato',edgecolor='black',label=f'{numPoints} points(MC)')
    ax.hist(pi_qmc,bins=10,alpha=0.6,density=True,color='dodgerblue',edgecolor='black',label=f'{numPoints} points(QMC)')

    #Customize figure
    ax.axvline(x=np.pi,color='black',linestyle='--',linewidth=1.5,label='Pi')
    ax.legend()
    ax.set_title(f"Comparison of Estimates: N={numPoints}; Number of Sims=1000")
    return fig







