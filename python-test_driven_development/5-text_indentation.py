#!/usr/bin/python3
"""Prints a text with 2 new lines after each '.', '?' or ':'."""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?', or ':'.

    Args:
        text (str): The text to print.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    index = 0
    length = len(text)

    while index < length and text[index] == ' ':
        index += 1

    while index < length:
        char = text[index]
        print(char, end="")

        if char == "\n" or char in ".?:":
            if char in ".?:":
                print("\n")

            index += 1

            while index < length and text[index] == ' ':
                index += 1
            continue

        index += 1
