# Operations on arrays

import numpy as np


def test_run():
    np.random.seed(693)
    a = np.random.randint(0, 10, size=(5, 4))
    print('Array:\n', a)

    # sum of all the elements in the array
    print('Print sum of all elements:', a.sum())

    # Itterate over rows to compute sum of the columns**
    print('Sum of column: ', a.sum(axis=0))

    # Itterate over columns to compute sum of the rows**
    print('Sum of rows: ', a.sum(axis=1))

    # Statistics : min, max, mean (across rows, cols and overall)
    print('Minimum of each column: ', a.min(axis=0))
    print('Maximum of each row: ', a.max(axis=1))
    print('Mean of all elements: ', a.mean())


if __name__ == '__main__':
    test_run()
