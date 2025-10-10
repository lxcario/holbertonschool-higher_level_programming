#!/usr/bin/python3
"""Module containing read_file function"""


def read_file(filename=""):
    """The read_file function"""

    # Opening and reading the file
    with open(filename, 'r', encoding='UTF-8') as f:
        read_data = f.read()
        print(read_data, end="")
