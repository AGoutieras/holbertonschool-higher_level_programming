#!/usr/bin/python3
"""Extends the built-in iterator obtained from the iter function."""


class CountedIterator:
    """
    An iterator that wraps any iterable
    and counts how many items have been iterated over.
    """

    def __init__(self, iterable):
        """Initialize the CountedIterator with an iterable."""

        self.iterator = iter(iterable)
        self.count = 0

    def get_count(self):
        """Return the number of items iterated so far"""

        return self.count

    def __iter__(self):
        """Return the iterator object itself."""

        return self

    def __next__(self):
        """Fetch the next item from the iterator and increment the count."""
        item = next(self.iterator)
        self.count += 1
        return item
