#!/usr/bin/python3
"""Defines a rectangle class with width and height attributes."""


class Rectangle:
    """Represents a rectangle with width and height.

    Attributes:
        width (int): The width of the rectangle (must be >= 0).
        height (int): The height of the rectangle (must be >= 0).
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): Optional, width of the rectangle (default 0).
            height (int): Optional, height of the rectangle (default 0).
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Get or set the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width, ensuring it is an int >= 0."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        elif value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """Get or set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height, ensuring it is an int >= 0."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        elif value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the rectangle with the greater area, or rect_1 if equal.

        Raises:
            TypeError: If rect_1 or rect_2 is not a Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1

        else:
            return rect_2

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """
        Return the perimeter of the rectangle.

        If width or height is 0, returns 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__width * 2 + self.__height * 2

    def __str__(self):
        """
        Return a string representation of the rectangle using '#' characters.

        Each line contains 'width' number of '#' characters, and the total
        number of lines is 'height'.
        If width or height is 0, returns an empty string.
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        lines = []

        for line in range(self.__height):
            lines.append(str(self.print_symbol) * self.__width)

        return f"\n".join(lines)

    def __repr__(self):
        """
        Return a string representation of the rectangle
        that can be used to recreate a new instance with eval().
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Prints a message on deletion"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
