'''Using time function.'''

import time


def test_run():
    t1 = time.time()
    print('ML4T')
    t2 = time.time()
    print('Time of function: ', t2-t1)


if __name__ == '__main__':
    test_run()


