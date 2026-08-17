import streamlit as st
import numpy as np
import utils as u
from scipy.stats import qmc
import matplotlib.pyplot as plt


num_trials = 1000


def estimate_pi_1000(points,num_points):
    """
    Estimates pi using Monte Carlo methods for different number of points generated
    and for 1000 simulations

    Parameters:
    points(np.darray): 4D array containing the points generated for each simulation
    num_points(int): The number of points generated

    Returns:
    pi_estimates(np.darray): A 3D matrix containing the estimate of pi for each simulation
    abs_errors(np.darray): A 3D matrix containing the absolute error for each pi estimate for each simulation
    """
    pi=np.pi
    x = points[...,0]
    y = points[...,1]
    inside_circle = (x**2+y**2)<=1

    #Calculate the estimate of pi
    pi_estimates = 4 * (np.sum(inside_circle,axis=2))/num_points
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
    fig,ax = plt.subplots(figsize=(10,7))

    #Plot Points
    ax.plot(x_coords,ymc_coords,color='dodgerblue',label='Mean MC Estimates')
    ax.plot(x_coords,yqmc_coords,color='tomato',label='Mean QMC Estimates')

    #Add boundary line for pi
    ax.axhline(y=np.pi,color='black',linestyle='--',linewidth=3,label='Pi')

    #Customize figure
    ax.set_xscale("log")
    ax.set_xlim(10,100000)
    ax.set_ylim(3.13,3.16)
    ax.margins(x=0.05)
    ax.legend()
    ax.set_title('Convergence Plot of Pi')

    return fig


def mae_convergence(mc_erros,qmc_erros,points):
    """
    Generates a convergence plot for the estimation of pi 

    Parameters:
    mc_estimates(np.darray):A 1D array containing the estimates of pi using monte carlo methods
    qmc_estimates(np.darray): A 1D array containing the estimates of pi usign qmc methods
    points(np.darray): 1D array containing the options for the number of points generated

    Returns:
    fig: A matplotlib figure
    """
    





