#!/usr/bin/python3
"""Prints a text with 2 new lines after each '.', '?' or ':'."""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?' or ':'.

    Args:
        text (str): The text to print.

    Raises:
        TypeError: If text is not a string.

    Returns:
        None
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    line = ""
    for char in text:
        line += char
        if char in ".?:":
            print(line.strip())
            print()
            line = ""

    if line.strip():
        print(line.strip())
