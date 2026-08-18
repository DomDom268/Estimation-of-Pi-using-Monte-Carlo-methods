"""
benchmark.py

Compares execution speed between Naive for loops, NumPy vectorization(MC and QMC)

"""

import time
import numpy as np
from scipy.stats import qmc


def naive_estimator(numTrials:int, numPoints:int)->np.ndarray:
    """Original Naive Loop based estimator"""

    estimates=[]
    rng = np.random.default_rng(seed=42)

    for _ in range(numTrials):
        inside_circle = 0
        for _ in range(numPoints):
            x=rng.random()
            y=rng.random()
            if x**2 + y**2 <=1:
                inside_circle+=1
        estimates.append(4*inside_circle/numPoints)

    return np.array(estimates)

def vectorized_estimator(numTrials:int,numPoints:int)->np.ndarray:
    """Optimized vectorized estimator using uniform prng"""

    shape=(1,numTrials,numPoints,2)
    rng = np.random.default_rng(seed=42)

    points = np.random.uniform(low=0.0,high=1.0,size=shape)
    inside_circle = (points[...,0]**2+points[...,1]**2)<=1

    return 4*np.sum(inside_circle,axis=2)/numPoints


def vectorized_qmc_estimator(numTrials:int,numPoints:int)->np.ndarray:
    """Optimized vectorized estimator using sobol sequencing"""

    shape = (1,numTrials,numPoints,2)
    total_points = numTrials*numPoints

    sampler = qmc.Sobol(d=2,scramble=True,seed=42)
    raw_points = sampler.random(n=total_points)
    points = raw_points.reshape(shape)

    inside_circle = (points[...,0]**2+points[...,1]**2)<=1

    return 4*np.sum(inside_circle,axis=2)/numPoints

def run_bench():
    numTrials=8
    numPoints=2**16

    methods={
        "Naive Loops":naive_estimator,
        "Vectorized MC":vectorized_estimator,
        "Vectorized QMC":vectorized_qmc_estimator
    }

    results={}

    print(f"Starting benchmarks: {numTrials} trials with {numPoints} points")

    for name,func in methods.items():
        start_time=time.perf_counter()
        estimates=func(numTrials,numPoints)
        end_time=time.perf_counter()

        #Calculate duration
        duration = end_time-start_time

        results[name] = {"time":duration,"speedup":1.0}

    #Calculate performance speedup
    baseline_time = results['Naive Loops']['time']
    for name in results:
        results[name]["speedup"]= baseline_time/results[name]['time']

    #Print results
    print("|Method|Execution Time|Speedup|")
    print("|:------|:------|:------|")
    for name,metrics in results.items():
        print(
            f"|{name}"
            f"|{metrics['time']:.4f}s"
            f"|{metrics['speedup']:.1f}x|"
        )

run_bench()
