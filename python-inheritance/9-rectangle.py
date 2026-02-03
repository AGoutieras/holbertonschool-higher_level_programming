#!/usr/bin/python3
"""Define a base geometry class 'BaseGeometry'"""


class BaseGeometry:
    """Represents BaseGeometry"""
    def integer_validator(self, name, value):
        """Checks if value is an int and is greater than 0"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """Represents a rectangle"""
    def __init__(self, width, height):
        """Initialize rectangle with validated width and height"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return the string representation of the rectangle"""
        return f"[Rectangle] {self.__width}/{self.__height}"
