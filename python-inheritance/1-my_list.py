#!/usr/bin/python3
"""
Define an inherited list class MyList
"""


class MyList(list):
    """
    Inherit from list and add a print_sorted method
    """
    def print_sorted(self):
        """
        Print the list in ascending order
        """
        print(sorted(self))
