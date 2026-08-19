"""
tests/test_estimate_sobol.py

Unity test for the estimate_pi_sobol function
"""
import numpy as np
from scipy.stats import qmc
from utils import generate_sobol_points,estimate_pi_sobol

#Mathematical Tests
def test_estimate_pi_sobol_range():
    seed = 12345
    points_to_generate = [5,10,15]

    for points in points_to_generate:
        coords = generate_sobol_points(seed,points)
        pi_hat=estimate_pi_sobol(coords)

        assert 0 <= pi_hat <= 4

#Randomness Tests
def test_estimate_pi_sobol_reproducibility():
    seed = 12345

    points1 = generate_sobol_points(seed,1000)
    points2 = generate_sobol_points(seed,1000)

    pi1 = estimate_pi_sobol(points1)
    pi2 = estimate_pi_sobol(points2)

    assert pi1 == pi2
    np.testing.assert_array_equal(points1,points2)    

def test_estimate_pi_sobol_diff_seeds():
    seed1 = 12345
    seed2 = 54321

    points1 = generate_sobol_points(seed1,1000)
    points2 = generate_sobol_points(seed2,1000)


    assert not np.array_equal(points1,points2)
