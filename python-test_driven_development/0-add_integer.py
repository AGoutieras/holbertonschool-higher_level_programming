#!/usr/bin/python3
"""
Computes the sum of two numbers as integers.

Prototype: def add_integer(a, b=98):
- Both a and b must be int or float; if not, raises a TypeError
  with the message 'a must be an integer' or 'b must be an integer'.
- If a or b are floats, they are first converted to integers.
- Returns an integer representing the sum of a and b.
- No external modules are required or allowed.
"""


def add_integer(a, b=98):
    """
    Calculates the sum of two numbers as integers.

    Parameters:
        a (int or float): The first value to add.
        b (int or float, optional): The second value to add (default is 98).

    Returns:
        int: The result of adding a and b as an integer.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
