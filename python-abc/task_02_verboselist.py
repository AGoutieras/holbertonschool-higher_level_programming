#!/usr/bin/python3
"""Extends the Python list class and prints a notification message"""


class VerboseList(list):
    """
    A subclass of Python's built-in list that prints a notification
    whenever items are added or removed.
    """
    def append(self, item):
        """Add an item to the list and print a notification."""
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, item):
        """Extend the list with multiple items and print a notification."""
        super().extend(item)
        print("Extended the list with [{}] items.".format(len(item)))

    def remove(self, item):
        """Remove an item from the list and print a notification."""
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=None):
        """Remove and return an item and print a notification."""
        item = self[-1] if index is None else self[index]
        print("Popped [{}] from the list.".format(item))
        if index is None:
            return super().pop()
        else:
            return super().pop(index)
