# Array Attributes

import numpy as np


def test_run():
    a = np.random.random((5, 4))  # 5x4 array of random numbers
    print(a)
    print(a.shape)
    print(a.shape[0])
    print(a.shape[1])

    # Number of all elements in array

    print(a.size)

    # Access the data type of the elements in the array
    print(a.dtype)


if __name__ == '__main__':
    test_run()

