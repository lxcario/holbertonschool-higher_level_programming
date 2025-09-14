#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print()
    else:
        for i in matrix:
            for idx, j in enumerate(i):
                if idx < len(i) - 1:
                    print("{:d}".format(j), end=" ")
                else:
                    print("{:d}".format(j))
