#!/usr/bin/python3
"""Module containing text_indentation function"""


def text_indentation(text):
    """Function printing text with two blank lines after each of ?, : and ."""

    # Checking if text is a string
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Changing the text for signs
    for char in ".:?":
        text = text.replace(char, char + "\n\n")

    # Printing the text
    print("\n".join(line.strip() for line in text.split("\n")), end="")
