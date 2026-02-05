#!/usr/bin/python3
"""Define a base geometry class 'BaseGeometry'"""


class BaseGeometry:
    """Represents BaseGeometry"""
    def area(self):
        """Not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Checks if value is an int and is greater than 0"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
