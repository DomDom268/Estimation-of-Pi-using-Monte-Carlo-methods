"""
tests/test_estimators.py
Unit testing 


"""
import numpy as np
from utils import generate_xy,estimate_pi

#Mathematical Tests
def test_estimate_pi_range():
    seed=12345

    points_to_generate = [5,10,15]

    for points in points_to_generate:
        x,y=generate_xy(seed,points)
        pi_hat=estimate_pi(x,y)

        assert 0 <= pi_hat <= 4

#Randomness Tests
def test_estimate_pi_reproducibility():
    seed1 = 12345
    seed2 = 12345

    x1,y1= generate_xy(seed1,10)
    x2,y2=generate_xy(seed2,10)

    pi1 = estimate_pi(x1,y1)
    pi2 = estimate_pi(x2,y2)

    assert pi1==pi2
    np.testing.assert_equal(x1,x2)
    np.testing.assert_equal(y1,y2)


def test_estimate_pi_sobol_diff_seeds():
    seed1 = 12345
    seed2 = 54321

    x1,y1= generate_xy(seed1,10)
    x2,y2=generate_xy(seed2,10)
    
    
    assert not np.array_equal(x1,x2)
    assert not np.array_equal(y1,y2)