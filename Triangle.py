"""
A skeleton template for the Triangle class in Week 2: Coding Exercises.
"""

import math


class Triangle:
    """
    A class representing a triangle.

    Parameters
    ----------
    lengthSide1: (int, float)
        The length of the first side.
    lengthSide2: (int, float)
        The length of the second side.
    lengthSide3: (int, float)
        The length of the third side.
    """

    def __init__(self, lengthSide1, lengthSide2, lengthSide3):
        self.side1 = lengthSide1
        self.side2 = lengthSide2
        self.side3 = lengthSide3

        # run test to check if triangle is valid
        if not self.testIfValidTriangle():
            raise ValueError(
                "A triangle with sides ({}, {}, {}) is not valid".format(
                    self.side1, self.side2, self.side3,
                )
            )

    def __str__(self):
        return "Triangle (sides {}, {}, {})".format(self.side1, self.side2, self.side3)

    def testIfValidTriangle(self):
        test = True
        a = self.side1
        b = self.side2
        c = self.side3
        # Carry out checks that this is a triangle
        if not (a > 0 and b > 0 and c > 0):
            test = False
        if not ((a + b) > c and (b + c) > a and (a + c) > b):
            test = False
        return test

    def calcTriangleArea(self):
        # Return area of the triangle
        a = self.side1
        b = self.side2
        c = self.side3
        s = (a + b + c) / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        return area


sides = [1.0, 2.0, 3.0]
try:
    t = Triangle(*sides)
except ValueError as e:
    print(e)