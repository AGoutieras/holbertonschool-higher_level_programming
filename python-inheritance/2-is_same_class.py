#!/usr/bin/python3
"""Check if an object is exactly an instance of a given class"""


def is_same_class(obj, a_class):
    """Return True if obj is an istance of a_class"""
    return type(obj) == a_class
