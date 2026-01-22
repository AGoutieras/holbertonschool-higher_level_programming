#!/usr/bin/python3
"""Divides all elements of a matrix by a number."""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a number.

    Args:
        matrix (list of lists of int/float): The matrix to be divided.
        div (int or float): The number by which to divide the matrix elements.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats.
        TypeError: If each row of the matrix does not have the same size.
        TypeError: If div is not a number.
        ZeroDivisionError: If div is 0.

    Returns:
        list of lists of float: A new matrix with all elements divided by div,
                                rounded to 2 decimal places.
    """
    if (not isinstance(matrix, list) or
            not all(isinstance(row, list) for row in matrix)):
        raise TypeError
        ("matrix must be a matrix (list of lists) of integers/floats")

    if (not all(all(isinstance(elem, (int, float)) for elem in row)
                for row in matrix)):
        raise TypeError
        ("matrix must be a matrix (list of lists) of integers/floats")

    if len(set(len(row) for row in matrix)) > 1:
        raise TypeError
        ("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError
        ("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(elem / div, 2) for elem in row] for row in matrix]
    return new_matrix
