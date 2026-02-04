#!/usr/bin/python3
"""Check if an object is an inherited instance of a given class"""


def inherits_from(obj, a_class):
    """Check if an object is an inherited instance of a given class"""
    return False if type(obj) is a_class else issubclass(type(obj), a_class)
