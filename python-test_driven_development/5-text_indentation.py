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

    separators = ".?:"
    i = 0
    length = len(text)
    line = ""

    while i < length:
        char = text[i]
        line += char
        if char in separators:
            print(line.strip(), end="\n\n")
            line = ""
        i += 1

    if line.strip():
        print(line.strip())
