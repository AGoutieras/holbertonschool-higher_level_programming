#!/usr/bin/python3
"""Prints the full name in the format 'My name is <first_name> <last_name>'."""


def say_my_name(first_name, last_name=""):
    """
    Prints the full name in the format 'My name is <first_name> <last_name>'.

    Args:
        first_name (str): The first name to print.
        last_name (str, optional): The last name to print.

    Raises:
        TypeError: If first_name is not a string.
        TypeError: If last_name is not a string.

    Returns:
        None
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
