"""
tests/test_estimate_pi1000.py

Unit tests for the test_estimate_pi1000 function
"""

import numpy as np
from utils import estimate_pi_1000
from scipy.stats import qmc

#Basic Correctness Tests
def test_estimate_pi1000_correctness():
    points = np.array(
        [
            [
                [
                    [0.0,0.0],
                    [1.0,0.9],
                    [1.0,0.0],
                    [1.0,1.0]
                ]
            ]
        ]
    )

    pi_hat,err=estimate_pi_1000(points,4)

    assert pi_hat == 2.0 
    assert err == abs(2.0-np.pi) 

#Shape Tests
def test_estimate_pi1000_shape():
    rng = np.random.default_rng(12345)

    points = rng.uniform(low=0.0,high=1.0,size=(1,1000,100,2))
    pi_hat,err = estimate_pi_1000(points,100)
    assert pi_hat.shape == (1,1000)
    assert err.shape==(1,1000)

#Mathematical Tests
def test_estimate_pi1000_range():
    rng = np.random.default_rng(12345)
    
    points = rng.uniform(low=0.0,high=1.0,size=(1,1000,100,2))
    pi_hat,err = estimate_pi_1000(points,100)

    assert np.all((pi_hat>=0) & (pi_hat<=4))
    assert np.all(err>=0)

    
#Edge Tests
def test_estimate_pi1000_one_point():
    rng = np.random.default_rng(12345)
    sampler = qmc.Sobol(d=2,scramble=True,seed=12345)
    points = rng.uniform(low=0.0,high=1.0,size=(1,1000,1,2))
    points_qmc_raw = sampler.random(1*1000)
    points_qmc = points_qmc_raw.reshape(1,1000,1,2)

    pi_hat,_ = estimate_pi_1000(points,1)
    pi_hat_qmc,_ = estimate_pi_1000(points_qmc,1)

    assert np.all((pi_hat==0)|(pi_hat==4))
    assert np.all((pi_hat_qmc==0)|(pi_hat_qmc==4))


def test_estiamte_pi1000_all_inside():
    points = np.array(
        [
            [
                [
                    [0.0,0.0],
                    [0.1,0.1],
                    [0.0,0.1],
                    [0.2,0.3]
                ]
            ]
        ]
    )

    pi_hat,err = estimate_pi_1000(points,4)

    assert pi_hat == 4
    assert err == abs(4-np.pi)

def test_estimate_pi_1000all_outside():
    points = np.array(
        [
            [
                [
                    [1.0,1.0],
                    [0.9,1.0],
                    [1.0,0.9],
                    [1.0,1.0]
                ]
            ]
        ]
    )

    pi_hat,err = estimate_pi_1000(points,4)

    assert pi_hat == 0
    assert err == abs(0-np.pi)