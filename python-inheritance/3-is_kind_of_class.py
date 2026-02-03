#!/usr/bin/python3
"""Check if an object is an instance or inherited instance of a given class"""


def is_kind_of_class(obj, a_class):
    """Return True if obj is an instance or inherited instance of a_class"""
    if isinstance(obj, a_class):
        return True
    return False
