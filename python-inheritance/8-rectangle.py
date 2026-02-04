#!/usr/bin/python3
"""Define a base geometry class 'BaseGeometry'"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle"""
    def __init__(self, width, height):
        """Initialize rectangle with validated width and height"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
