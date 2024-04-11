#!/usr/bin/python3
"""Unittests for max_integer([])."""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Class define unitests for the function max_integer"""

    def test_positive_integers(self):
        # Test case with a list of positive integers
        self.assertEqual(max_integer([3, 7, 2, 9, 1]), 9)

    def test_negative_integers(self):
        # Test case with a list of negative integers
        self.assertEqual(max_integer([-3, -7, -2, -9, -1]), -1)

    def test_mixed_integers(self):
        # Test case with a mix of positive and negative integers
        self.assertEqual(max_integer([-3, 7, -2, 9, -1]), 9)

    def test_ordered_list(self):
        """Test an ordered list of integers."""
        ordered = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered), 4)

    def test_unordered_list(self):
        """Test an unordered list of integers."""
        unordered = [1, 2, 4, 3]
        self.assertEqual(max_integer(unordered), 4)

    def test_single_integer(self):
        # Test case with a list containing a single integer
        self.assertEqual(max_integer([42]), 42)

    def test_floats(self):
        """Test a list of floats."""
        floats = [1.53, 6.33, -9.123, 15.2, 6.0]
        self.assertEqual(max_integer(floats), 15.2)

    def test_list_of_strings(self):
        """Test a list of strings."""
        strings = ["Brennan", "is", "my", "name"]
        self.assertEqual(max_integer(strings), "name")

    def test_empty_list(self):
        # Test case with an empty list
        self.assertIsNone(max_integer([]))


if __name__ == '__main__':
    unittest.main()
