#!/usr/bin/python3
"""Define a base geometry class 'BaseGeometry'"""


class BaseGeometry:
    """Represents BaseGeometry"""
    def area(self):
        """Not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Checks if value is an int and is greater than 0"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
