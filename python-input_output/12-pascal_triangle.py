#!/usr/bin/python3
"""Module containing pascal_triangle func"""


def pascal_triangle(n):
    """Function to return Pascal's triangle"""
    # Checking n <= 0 case
    if n <= 0:
        return []

    # Creating the triangle lists
    final = [[1]]
    for i in range(1, n):
        new_list = []
        for index in range(i + 1):
            if index != 0 and index != i:
                new_list.append(final[i - 1][index - 1] + final[i - 1][index])
            else:
                new_list.append(1)
        final.append(new_list)
    return final
