#!/usr/bin/python3
"""Check if an object is exactly an instance of a given class"""


def is_same_class(obj, a_class):
    """
    Return True if obj is an instance of a_class

    Args:
        obj (any): The object to check.
        a_class (type): The class to compare the object against.

    Returns:
        bool: True if obj is exactly an instance of a_class, False otherwise.
    """
    if type(obj) == a_class:
        return True
    return False
