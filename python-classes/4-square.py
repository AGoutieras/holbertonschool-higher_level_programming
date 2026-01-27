#!/usr/bin/python3
"""Defines a square."""


class Square:
    """Represents a square with a private size attribute.

    Attributes:
        __size (int): The size of the square (private).

    Properties:
        size (int): Getter and setter for the square's size with validation.
                     Must be an integer >= 0.

    Methods:
        area(): Returns the current square area.
    """
    def __init__(self, size=0):
        """
        Initializes a Square instance.

        Args:
            size (int, optional): The size of the square. Must be >= 0.
                                  Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """

        self.size = size

    @property
    def size(self):
        """
        Getter for the square's size.

        Returns:
            int: The current size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter for the square's size with validation.

        Args:
            value (int): The new size of the square. Must be >= 0.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        elif value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """
        Computes the area of the square.

        Returns:
            int: The area of the square (size squared).
        """
        return self.__size ** 2
