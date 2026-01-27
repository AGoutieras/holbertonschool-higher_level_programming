#!/usr/bin/python3
"""Defines a square."""


class Square:
    """
    Represents a square.

    Attributes:
        __size (int): The size of the square (private, >= 0).
        __position (tuple): The position of the square.

    Properties:
        size (int): Getter and setter for the size with validation.
        position (tuple): Getter and setter for the position with validation.

    Methods:
        area(): Returns the current area of the square.
        my_print(): Prints the square using '#' considering position.
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a Square instance.

        Args:
            size (int, optional): The size of the square.
            position (tuple, optional): The position (x, y) of the square.

        Raises:
            TypeError: If size is not an integer
                       or position is not a tuple of 2 positive integers.
            ValueError: If size is less than 0.
        """

        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        Getter for the square's position.

        Returns:
            tuple: The current position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter for the square's position with validation.

        Args:
            value (tuple): A tuple of 2 positive integers representing (x, y).

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")

        if not len(value) == 2:
            raise TypeError("position must be a tuple of 2 positive integers")

        if not all(isinstance(num, int) and num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """
        Computes the area of the square.

        Returns:
            int: The area of the square (size squared).
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square with the character '#' to stdout.

        If the size is 0, prints an empty line.
        The position attribute controls the horizontal and vertical offset.
        """
        if self.__size == 0:
            print()
            return

        for line in range(self.__position[1]):
            print()

        for line in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
