"""Fit a line to polynomial data points"""

import numpoy as np
import matplotlib.pyplot as plt
import scipy.optimize as spo


def error_poly(C, data):
    """Compute error between given polynomial and observed data

    Parameters
    ----------
    C: numpy.poly1d object or equivalent array representing polynomial coefficients
    data: 2d arraywhere each row  is a point (x, y)

    Returns error as a single real value
    """

    # Metric: Sum of squared Y-axis differences
    err = np.sum((data[:, 1] - np.polyval(C, data[:, 0])) ** 2)
    return err


def fit_poly(data, error_func, degree=3):
    """Fit a polynomial to given data, using supplied error function

    Parameters
    ----------
    data: 2D array where each row is a point (x, y)
    error_func: fucntion that computes the error between a polynomial and observed data

    Returns polynomial that minimises the error function
    """

    # Generate inital guess for polynomial model (all coeffs = 1)
    Cguess = np.poly1d(np.ones(degree + 1, dtype=np.float32))

    # Plot initial guess
    x = np.linspace(-5, 5, 21)
    plt.plot(x, np.polyval(Cguess, x), 'm--', linewidth=2.0, label="Inital Guess")

    # Call optimiser to minimise error functionresult
    result = spo.minimize(error_func, Cguess, args=(data,), method='SLSQP', options={'disp': True})
    return np.poly1d(result.x)  # Convert optimal results into a poly1d and return


