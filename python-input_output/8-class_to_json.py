#!/usr/bin/python3
"""Module containing class_to_json function"""


def class_to_json(obj):
    """Function returning dict of a class"""
    return obj.__dict__
