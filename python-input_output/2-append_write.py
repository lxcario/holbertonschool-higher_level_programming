#!/usr/bin/python3
"""Module containing append_file function"""


def append_write(filename="", text=""):
    """The append_file function"""

    # Opening and appending to the file
    with open(filename, 'a', encoding='UTF-8') as f:
        return f.write(text)
