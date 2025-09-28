#!/usr/bin/python3
"""Module containing BaseGeometry class"""


class BaseGeometry:
    """Class for BaseGeometry"""

    def area(self):
        """Method to raise exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method to validate value"""

        # Checking if value is not an int
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        # Checking if value is not less or equal to 0
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
