import numpy as np
import matplotlib.pyplot as plt


def quadratic(x, c0, c1, c2):
    """
    A function defining a quadratic equation.

    Parameters
    ----------
    x: (list, array)
        A set of values at which the function is evaluated.
    c0: float
        The coefficient of the x^0 term
    c1: float
        The coefficient of the x^1 term
    c2: float
        The coefficient of the x^2 term

    Returns
    -------
    y: array
        The function evaluated at x.
    """

    xs = np.array(x)  # make sure x is an array
    return c0 + c1 * xs + c2 * xs ** 2


np.random.seed(42)  # set seed for reproducible random data

# values to set up quadratic
n = 20  # number of data points
x = np.linspace(-10, 10, n)  # points at which to evaluate the function
coeffs = [-7.6, 3.4, 1.7]  # quadratic coefficients

# create data: quadratic + Gaussian noise with zero mean and standard deviation of 20
data = quadratic(x, coeffs[0], coeffs[1], coeffs[2]) + np.random.normal(0.0, 20.0, n)

c = np.polyfit(x, data, 2)
best_fit = (c[0] * x **2) + (c[1] * x) + c[2]

plt.scatter(x, data, marker="o", color="r", label="data")
plt.plot(x, best_fit, color="k", label="Best fit")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()

plt.show()
