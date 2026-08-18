"""
tests/test_estimators.py
Unit testing 


"""
import numpy as np
from utils import estimate_pi

#Mathematical Tests
def test_estimate_pi_range():
    rng = np.random.default_rng(12345)
    points_to_generate = [5,10,15]

    for points in points_to_generate:
        pi_hat,_,_=estimate_pi(points,rng)

        assert 0 <= pi_hat <= 4

#Randomness Tests
def test_estimate_pi_reproducibility():
    rng1 = np.random.default_rng(12345)
    rng2 = np.random.default_rng(12345)

    pi1,x1,y1 = estimate_pi(10,rng1)
    pi2,x2,y2 = estimate_pi(10,rng2)
    
    assert pi1 == pi2
    np.testing.assert_array_equal(x1,x2)
    np.testing.assert_array_equal(y1,y2)    

def test_estimate_pi_sobol_diff_seeds():
    rng1 = np.random.default_rng(12345)
    rng2 = np.random.default_rng(54321)

    pi1,x1,y1 = estimate_pi(10,rng1)
    pi2,x2,y2 = estimate_pi(10,rng2)
    
    assert not np.array_equal(x1,x2)
    assert not np.array_equal(y1,y2)