#!/usr/bin/python3
"""
adds two numbers as integers
"""


def add_integer(a, b=98):
    """
    Adds two integers (or floats casted to int).

    a and b must be integers or floats; floats are casted to integers.
    Returns the sum as an integer.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + (b)
