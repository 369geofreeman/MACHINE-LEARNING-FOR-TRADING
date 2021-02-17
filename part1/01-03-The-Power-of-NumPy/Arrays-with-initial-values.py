# Creating numpy arrays

import numpy as np


def test_run():
    '''Empty array'''
    print(np.empty(5))
    print(np.empty((5, 4, 3)))


def test_run2():
    print(np.ones((5, 4)))
    print(np.ones(6))


if __name__ == '__main__':
    test_run2()


