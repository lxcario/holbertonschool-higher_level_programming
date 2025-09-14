#!/usr/bin/python3
"""
This module provides a function for adding two numbers.
"""


def add_integer(a, b=98):
    """Adds two numbers, casting them to integers first.

    Args:
        a (int or float): The first number.
        b (int or float): The second number, with a default value of 98.

    Raises:
        TypeError: If 'a' or 'b' are not integers or floats.

    Returns:
        int: The sum of a and b as an integer.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)

