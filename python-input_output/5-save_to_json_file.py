#!/usr/bin/python3
"""Module containing save_to_json_file function"""
import json


def save_to_json_file(my_obj, filename):
    """Function to write an object to a JSON'ed text file"""

    with open(filename, 'w', encoding='UTF-8') as f:
        f.write(json.dumps(my_obj))
