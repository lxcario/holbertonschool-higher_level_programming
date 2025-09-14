#!/usr/bin/python3
"""Module containing matrix_divided func"""


def matrix_divided(matrix, div):
    """Function for dividing all the elements of matrix"""

    # Checking if matrix is a list and its elements is lists containing ints
    if not all(isinstance(matrix, list)
               and all(isinstance(num, (int, float))
                       for num in row) for row in matrix):
        raise TypeError("matrix must be a matrix "
                        "(list of lists) of integers/floats")

    # Checking if all rows containing same number of elements
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Checking if div is not a float or int
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Checking if div is 0
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Dividing elements
    new_matrix = []
    for row in matrix:
        new_row = []
        for element in row:
            new_row.append(round(element / div, 2))
        new_matrix.append(new_row)

    # Return new matrix
    return new_matrix
