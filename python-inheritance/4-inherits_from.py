#!/usr/bin/python3
"""Module containing inherits_from func"""


def inherits_from(obj, a_class):
    """Function to check if the object is an instance of a class
    that inherited from the specified class"""
    return isinstance(obj, a_class) and type(obj) is not a_class
