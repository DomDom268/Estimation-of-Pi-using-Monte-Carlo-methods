"""
tests/test_estimate_sobol.py

Unity test for the estimate_pi_sobol function
"""
import numpy as np
from scipy.stats import qmc
from utils import estimate_pi_sobol

#Mathematical Tests
def test_estimate_pi_sobol_range():
    seed = 12345
    points_to_generate = [5,10,15]

    for points in points_to_generate:
        pi_hat,_=estimate_pi_sobol(points,seed)

        assert 0 <= pi_hat <= 4

#Randomness Tests
def test_estimate_pi_sobol_reproducibility():
    seed = 12345

    pi1,points1 = estimate_pi_sobol(1000,seed)
    pi2,points2 = estimate_pi_sobol(1000,seed)

    assert pi1 == pi2
    np.testing.assert_array_equal(points1,points2)    

def test_estimate_pi_sobol_diff_seeds():
    seed1 = 12345
    seed2 = 54321

    p1,points1 = estimate_pi_sobol(1000,seed1)
    p1,points2 = estimate_pi_sobol(1000,seed2)

    assert not np.array_equal(points1,points2)
