"""
A skeleton template for the Quadratic class in Week 2: Coding Exercises.
"""

import math
from numpy import poly1d


class Quadratic:
    """
    A class representing a quadratic.

    It has three variables representing the coefficients of a quadratic of the
    form

    ax^2 + bx + c,

    where a, b, and c, are real constants.

    The discriminant = b^2 - 4ac.

    If b^2 - 4ac < 0 the solutions are complex and will not be calculated.
    if b^2 - 4ac = 0 then there is one real root give by -b/2a
    If b^2 - 4ac > 0 then there are two real solutions.

    Parameters
    ----------
    a: (int, float)
        The coefficient of the x^2 term.
    b: (int, float)
        The coefficient of the x term.
    c: (int, float)
        The constant term (i.e., the coefficient of  the x^0 = 1 term).
    """

    def __init__(self, a, b, c):
        # The checks below make sure the coefficients are real numbers.
        if not isinstance(a, (int, float)):
            raise ValueError('Coefficient a is not a number')
        if not isinstance(b, (int, float)):
            raise ValueError('Coefficient b is not a number')
        if not isinstance(c, (int, float)):
            raise ValueError('Coefficient c is not a number')

        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return "Q(x) = {} x^2 + {} x + {}".format(self.a, self.b, self.c)

    def discriminant(self):
        # Replace the line below with the correct calculation of the discriminant
        disc = self.b ** 2 - 4 * self.a * self.c
        return disc

    def numberOfRoots(self):
        if self.discriminant() > 0:
            number = 2
        elif self.discriminant() == 0:
            number = 1
        else:
            number = 0
        # Use flow-control to set the number of roots

        return number

    def roots(self):
        root_number = self.numberOfRoots()
        discriminant = self.discriminant()
        # add code below thats calculates and returns the root(s)
        if root_number == 2:
            root_1 = (-self.b + discriminant ** 0.5) / (2 * self.a)
            root_2 = (-self.b - discriminant ** 0.5) / (2 * self.a)
            rootValues = (root_1, root_2)
        elif root_number == 1:
            rootValues = (-self.b + discriminant ** 0.5) / (2 * self.a)
        else:
            rootValues = None

        return rootValues

    @staticmethod
    def solveRoots(coefficients):
        if len(coefficients) != 3:
            print('Not a quadratic, you need three coefficients')
            return None

        for x in coefficients:
            if not isinstance(x, (int, float)):
                print('Not a quadratic, the coefficients need to be numbers')
                return None

        q = Quadratic(coefficients[0], coefficients[1], coefficients[2])
        return q.roots()


q = Quadratic(1.0, -7.0, 4.0)
roots = q.roots()
sortedRoots = sorted(roots)  # sort output for consistency
print("Number of roots: {0}\n"
      "Root type is {1}\n"
      "Roots are ({2:.3f}, {3:.3f})".format(
    q.numberOfRoots(),
    type(roots),
    sortedRoots[0],
    sortedRoots[1])
)
