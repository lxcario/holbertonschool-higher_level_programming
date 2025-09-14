#!/usr/bin/python3
"""Module for function of adding integer"""


def add_integer(a, b=98):
    """Adding integers function"""

    # Checking if a and b are float or int
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Casting to int if a and b is floating
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    # Return sum of a and b
    return a + b
