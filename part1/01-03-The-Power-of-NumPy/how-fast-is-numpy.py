# How Fast is Numpy


import numpy as np
import time


def how_long(func, *args):
    '''Execute functionwith given arguments, and meaure execution time'''
    t1 = time.time()
    result = func(*args) # all args are passes as is
    t2 = time.time()
    return result, t2-t1


def manual_mean(arr):
    '''Comput all the elements in a 2d array'''
    s = 0
    for i in range(arr.shape[0]):
        for j in range(arr.shape[1]):
            s = s+arr[i, j]
    return s / arr.size


def numpy_mean(arr):
    '''Comput mean average using numpy'''
    return arr.mean()


def test_run():
    '''Function called by Test Run'''
    nd1 = np.random.random((1000, 1000))  # Use a large array

    # Time two functions, retrieving results and execution times
    res_manual, t_manual = how_long(manual_mean, nd1)
    res_numpy, t_numpy = how_long(numpy_mean, nd1)
    print('Manual: {}  vs. Numpy: {}'.format(res_manual, res_numpy))

    # Make sure both give the same answer (up to tyhe same precision)
    assert abs(res_manual - res_numpy) <= 10e-6, "Results aren't equal."

    # Conmpute speedup
    speedup = t_manual / t_numpy
    print("Numpy mean is:", speedup, "faster than maual for loops.")


if __name__ == '__main__':
    test_run()

