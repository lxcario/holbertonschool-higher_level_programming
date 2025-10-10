#!/usr/bin/python3
"""Module containing write_file function"""


def write_file(filename="", text=""):
    """The write_file function"""

    # Opening and writing to the file
    with open(filename, 'w', encoding='UTF-8') as f:
        return f.write(text)
