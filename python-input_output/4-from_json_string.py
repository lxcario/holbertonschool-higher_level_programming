#!/usr/bin/python3
"""Module containing from_json_string function"""
import json


def from_json_string(my_str):
    """Function to return obj representation of JSON"""
    return json.loads(my_str)
