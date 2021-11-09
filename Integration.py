import math
import numpy


class Integration:
    """
    Class to setup an integration instance with an associated function.

    Parameters
    ----------
    function: callable
        The function to be integrated.
    method: int
        An integer defining the integration method to use: 1 is trapezium rule,
        2 is left rectangle rule, 3 is centre rectangle. Default it to use the
        trapezium rule.
    eps: float
        A value defining the absolute precision of the integration.
    """

    def __init__(self, function, method=1, eps=1e-5):
        self.setFunction(function)
        self.setEPS(eps)
        self.setMethod(method)

    def __repr__(self):
        return "I(method {}, function {}, eps {})".format(
            self.integrationMethod.__name__,
            self.functionToBeIntegrated.__name__,
            self.eps
        )

    def setFunction(self, function):
        if not callable(function):
            raise TypeError("You have not supplied a valid function")
        self.functionToBeIntegrated = function

    def setMethod(self, method):
        if method == 1:
            self.integrationMethod = self.trapz
        elif method == 2:
            self.integrationMethod = self.lrect
        elif method == 3:
            self.integrationMethod = self.crect
        else:
            raise ValueError(
                "Unrecognised integration method. Method must be 1 "
                "(trapezoid), 2 (left rectangle), or 3 (centre rectangle)."
            )

    def setEPS(self, eps):
        if eps <= 0:
            raise ValueError("Precision must be a positive number")
        self.eps = eps

    def evaluate(self, a, b):
        """
        Evaluate the integral between the ranges a and b.

        Parameters
        ----------
        a: (int, float)
            The lower bound of the integral.
        b: (int, float)
            The upper bound of the integral.

        Return
        ------
        float:
            The result of the integral.
        """

        if a >= b:
            raise ValueError(
                "The lower bound is greater than or equal to the upper bound"
            )

        my_function = self.functionToBeIntegrated
        i = 1
        similar_enough = False

        while not similar_enough:
            print(i)
            y_1 = self.integrationMethod(a, b, i * 100 * i, my_function)
            y_2 = self.integrationMethod(a, b, i * 100 * (i + 1), my_function)

            i += 1

            if math.isclose(y_1, y_2, rel_tol=self.eps):
                similar_enough = True

        result = y_2
        return result

    @staticmethod
    def lrect(a, b, N, f):

        h = (b - a) / N  # "height"
        sum = 0
        for i in range(0, N):
            x_i = a + h * (i)
            sum += h * f(x_i)

        return sum

    @staticmethod
    def crect(a, b, N, f):

        h = (b - a) / N  # "height"
        sum = 0
        for i in range(1, N + 1):
            x_i = a + h * (i - 0.5)
            sum += h * f(x_i)

        return sum

    @staticmethod
    def trapz(a, b, N, f):
        """
        Trapezium method of numerical integration.

        Parameters
        ----------
        a: (int, float)
            The lower bound of integral
        b: (int, float)
            The upper bound of integral
        N: int
            The number of intervals to use.
        f: callable
            The function to be integrated.
        """

        h = (b - a) / N  # height
        sum = 0

        for i in range(2, N + 1):
            x_i = a + (h * (i - 1))
            sum += f(x_i)

        integral_result = h * ((0.5 * f(a)) + (0.5 * f(b)) + sum)

        return integral_result


def straight_line(x):
    m = 2.0
    c = 2.0
    return m * x + c


from scipy.integrate import quad


def test_function(x):
    return math.exp(-x) * x ** 5


myIntegral = Integration(test_function)
a = 0  # lower bound
b = 1  # upper bound

print(myIntegral.evaluate(a, b))

myIntegral.setEPS(1e-8)
print(myIntegral.evaluate(a, b))

myIntegral.setMethod(2)
print(myIntegral.evaluate(a, b))
