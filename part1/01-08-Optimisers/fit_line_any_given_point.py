'''Fit a line to given set of data points using optimisation'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as spo


def err(line, data):  # error function
    '''Compute error between given line model and observed data.

    Parameters
    ----------

    line: tuple/list/array (C0, C1) where C0 is slope and C1 is Y intercept
    data: 2d array where each row is a point (x, y)

    returns error as single real value
    '''

    # Metric: Sum od squared Y-axis differences
    err = np.sum((data[:, 1] - (line[0] * data[:, 0] + line[1])) ** 2)
    return err


def fit_line(data, err_func):
    """Fit line to given data, using  a supplied error function

    Parameters
    ----------
    data: 2D array where each row is a point (X0, Y)
    err_func: function that computes the error between the observed data and the line

    returns line that minimises the rror function
    """

    # Generate initial guess for line model
    l = np.float32([0, np.mean(data[:, 1])])  # Slope = 0, intercept = mean(y values)

    # plot initial guess
    x_ends = np.float32([-5, 5])
    plt.plot(x_ends, l[0] * x_ends + l[1], 'm--', linewidth=2.0, label="Initial Guess")

    # Call optimiser to minimise error function
    result = spo.minimize(err_func, l, args=(data,), method='SLSQP', options={'disp': True})

    return result.x



def test_run():
    # Define original line
    l_orig = np.float32([4, 2])
    print("Original line: C0 = {}, C1 = {}".format(l_orig[0], l_orig[1]))

    Xorig = np.linspace(0, 10, 21)
    Yorig = l_orig[0] * Xorig + l_orig[1]
    plt.plot(Xorig, Yorig, 'b--', linewidth=2.0, label='Original line')

    # Generate noisy data points
    noise_sigma = 3.0
    noise = np.random.normal(0, noise_sigma, Yorig.shape)
    data = np.asarray([Xorig, Yorig + noise]).T
    plt.plot(data[:, 0], data[:, 1], 'go', label='Data points')

    # try to fit a line to this data
    l_fit = fit_line(data, err)
    print("Fited line: C0 = {}, C1 = {}".format(l_fit[0], l_fit[1]))
    plt.plot(data[:, 0], l_fit[0] * data[:, 0] + l_fit[1], 'r--', linewidth=2.0, label='Fited Line')

    # Add a legend and show plot
    plt.legend()
    plt.show()


if __name__ == "__main__":
    test_run()



