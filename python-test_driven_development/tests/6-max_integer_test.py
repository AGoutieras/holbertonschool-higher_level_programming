#!/usr/bin/python3
"""
Unittests for the function max_integer(list=[]).

This module contains tests for the max_integer function which returns
the largest integer (or float) in a list. It checks for positive numbers,
negative numbers, floats, empty lists, single-element lists,
and other edge cases.

Usage:
    python3 -m unittest tests.6-max_integer_test
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function."""

    def test_only_positives(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_only_negatives(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_positives_and_negatives(self):
        self.assertEqual(max_integer([1, -2, 3, -4]), 3)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_one_element(self):
        self.assertEqual(max_integer([1]), 1)

    def test_two_elements(self):
        self.assertEqual(max_integer([1, 2]), 2)

    def test_same_elements(self):
        self.assertEqual(max_integer([7, 7, 7, 7]), 7)

    def test_zero(self):
        self.assertEqual(max_integer([0, 1, 2, 3]), 3)

    def test_only_zero(self):
        self.assertEqual(max_integer([0, 0, 0, 0]), 0)

    def test_large_ints(self):
        self.assertEqual(max_integer([10e6, 10e7, 10e8, 10e9]), 10e9)

    def test_float(self):
        self.assertEqual(max_integer([1.5, 6.3, 8.6, 10.59]), 10.59)
