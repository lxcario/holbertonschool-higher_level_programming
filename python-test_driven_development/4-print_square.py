#!/usr/bin/python3
"""Module containing print_square function"""


def print_square(size):
    """Function to print a square"""

    # Checking if size is not an integer
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    # Checking if size is not greater or equal to 0
    if size < 0:
        raise ValueError("size must be >= 0")

    # Printing the square
    for i in range(size):
        print(size * "#")
