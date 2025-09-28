#!/usr/bin/python3
"""Module containing is_kind_of_class func"""


def is_kind_of_class(obj, a_class):
    """Function to check if obj is instance of given class
    or inherited class"""
    return isinstance(obj, a_class)
