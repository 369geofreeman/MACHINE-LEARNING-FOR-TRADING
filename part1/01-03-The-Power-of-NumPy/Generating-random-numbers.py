''' Generating random numbers '''

import numpy as np


def test_run():
    '''
    Genreate an array full of
    random numbers, uniformly samples from [0.0, 1.0]
    '''
    print(np.random.random((5, 4)))  # Pass in a size tuple
    print(np.random.rand(5, 4))  # function args (not a tuple)


def test_run2():
    '''Sampling from a normal distribution'''
    print(np.random.normal(size=(2, 3)))

    # Change mean to 50 and s.d. to 10
    print(np.random.normal(50, 10, size=(2, 3)))


def test_run3():
    np.random.randint(10)  # A single int from [0-10]
    np.random.randint(0, 10)  # Same as above specifying low-high explicit
    np.random.randint(0, 10, size=5)  # 5 randon ints as a 1D array
    np.random.randint(0, 10, size=(2, 3))  # 2x3 array of random ints


if __name__ == '__main__':
    test_run()
    test_run2()

