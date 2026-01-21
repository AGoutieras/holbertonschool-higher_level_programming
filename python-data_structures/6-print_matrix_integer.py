#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None

    for row in matrix:
        for elem in row:
            print("{:d}".format(elem), end=" ")
        print()
