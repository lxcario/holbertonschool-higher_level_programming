#!/usr/bin/python3
"""
Module 1-my_list
Defines the MyList class, which inherits from list.
"""


class MyList(list):
    """
    Inherits from the built-in list class and provides a method
    to print the list elements sorted in ascending order.
    """

    def print_sorted(self):
        """
        Prints the list, sorted in ascending order.
        The original list object is not modified.
        """
        # The built-in sorted() function is used to return a new sorted list.
        # This ensures the original list (self) remains unchanged.
        print(sorted(self))
