#!/usr/bin/python3
"""Module containing load_from_json_file function"""
import json


def load_from_json_file(filename):
    """Function to create Object from JSON file"""

    # Opening and reading the file
    with open(filename, 'r', encoding='UTF-8') as file:
        read_data = file.read()

    # Making file object and returning
    return json.loads(read_data)
