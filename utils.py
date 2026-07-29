import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
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

   return round(pi_hat,5)
    
def error(pi):
    return (f"Error = {abs(round(pi-np.pi,4))}"),abs(round(pi-np.pi,4))

def visualize_pi(n_points,pi,rng):
    x=rng.random(n_points)
    y=rng.random(n_points)
    inside = (x*x + y*y) <= 1
    
    
    
    fig, ax = plt.subplots(figsize=(6, 6))
    
    # Plot points inside the circle in blue, outside in red
    ax.scatter(x[inside], y[inside], color='dodgerblue', s=5, label='Inside')
    scatter = ax.scatter(x[~inside], y[~inside], color='tomato', s=5, label='Outside')
    
    # Add a visual boundary for the quarter-circle
    circle = plt.Circle((0, 0), 1, color='black', fill=False, linewidth=2)
    ax.add_patch(circle)
    
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.legend()
    ax.set_title(f"$\\pi$ ({pi}) Estimation with {n_points} points")
    return fig

def convergence(samples,rng):
    estimates =[]
    errors=[]
    estimates_sobol = []
    errors_sobol=[]

    #Create a list of estimates and errors for each sample size
    for idx in samples:
        pi_hat = estimate_pi(idx,rng)
        estimates.append(pi_hat)
        err_message,err = error(pi_hat)
        errors.append(err)

        pi_sobol = estimate_pi_sobol(idx)
        estimates_sobol.append(pi_sobol)
        err_sobol_message, err_sobol = error(pi_sobol)
        errors_sobol.append(err_sobol)


    estimate_coords = list(zip(samples,estimates))
    error_coords = list(zip(samples,errors))
    estimate_sobol_coords = list(zip(samples,estimates_sobol))
    error_sobol_coords = list(zip(samples,errors_sobol))

    return estimate_coords, error_coords, estimate_sobol_coords,error_sobol_coords

def visualize_convergence(coords,coords_sobol):
    #Separate coordinates
    x = [x for x,y in coords]
    y = [y for x,y in coords]

    xs=[x for x,y in coords_sobol]
    ys=[y for x,y in coords_sobol]

    # x,y = zip(*coords)
    # x = np.array(x,dtype=float)
    # y = np.array(y, dtype=float)

    fig, ax = plt.subplots(figsize=(6,6))
    
    #Plot points to show convergence of Pi estimates
    ax.plot(x,y,color='dodgerblue',label='Pi Estimates')
    ax.plot(xs,ys,color='indigo',label='Pi Estimates(SOBOL)')
    
    #Add boundary for Pi
    ax.axhline(y=np.pi,color='tomato',linestyle='--',linewidth=1.5,label='Pi')

    ax.set_xscale("log")
    ax.set_xlim(10,1000000)
    ax.set_ylim(3.0,3.6)
    ax.margins(x=0.05)
    ax.legend()
    ax.set_title(f"Convergence Plot of Pi")
    return fig

def visualize_error(coords,coords_sobol):
    x=[x for x,y in coords]
    y=[y for x,y in coords]

    xs=[x for x,y in coords_sobol]
    ys=[y for x,y in coords_sobol]

    yt = [pow(xt,-0.5) for xt in x]
    yst =[pow(xt,-1) for xt in x]

    fig, ax = plt.subplots(figsize=(6,6))

    ax.plot(x,y,color="indigo",linestyle='-',linewidth=2,label='Absolute Error')
    ax.plot(xs,ys,color="orange",linestyle='-',linewidth=2,label='Absolute Error(SOBOL)')
    ax.plot(x,yt,color="black",linestyle='-.',linewidth=2,label='Theoretical Absolute Error')
    ax.plot(x,yst,color="green",linestyle='-.',linewidth=2,label='Theoretical Absolute Error(SOBOL)')

    ax.margins(x=0.05)
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_ylim(1e-4,1e0)
    ax.set_xlim(10,1000000)
    ax.legend()
    ax.set_title(f"Absolute Error vs Sample Size")
    return fig

def histogram(estimates,sobol_estimates,bins):

    fig,ax = plt.subplots(figsize=(6,6))
    ax.hist(estimates,bins=bins,alpha=0.6,density=True,color='dodgerblue',edgecolor='black',label='MC')
    ax.hist(sobol_estimates,bins=bins,alpha=0.6,density=True,color='tomato',edgecolor='black',label='SOBOL')
    ax.axvline(x=np.pi,color='tomato',linestyle='-',linewidth=1.5,label='Pi')
    ax.legend()
    ax.set_title(f"Comparison of Estimates: N=1000; Number of Samples = 100")
    return fig

def std_dev(estimates, mean,n_points):
    deviations = [(x-mean)**2 for x in estimates]
    sum = np.sum(deviations)
    var = np.sqrt(sum/(n_points-1))
    return round(var,5)

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

def descriptive_stats(estimates,errors):
    
    mean = sum(estimates)/len(estimates)
    msqe= mse(estimates,mean,len(estimates))
    maer = mae(errors,len(errors))
    sd=std_dev(estimates,mean,len(estimates))
    min_est=min(estimates)
    max_est=max(estimates)

    return round(mean,5), msqe,maer, sd,min_est, max_est


