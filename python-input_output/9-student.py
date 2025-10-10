#!/usr/bin/python3
"""Module containing Student class"""


class Student:
    """The Student class"""

    def __init__(self, first_name, last_name, age):
        """Initialization of the class instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Method to retrieve dict of the class"""
        return self.__dict__
