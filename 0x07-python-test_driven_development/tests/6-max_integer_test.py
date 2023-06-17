#!/usr/bin/python3
"""Unittest modul"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    ''' TestCase class '''

    def test_integer(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 2]), 3)
        self.assertEqual(max_integer([1]), 1)

    def test_ngative(self):
        self.assertEqual(max_integer([-1, -3, -4, -2]), -1)

    def test_floating_numbers(self):
        self.assertAlmostEqual(max_integer([-1.4, 3.6, 4.9, 2.212]), 4.9)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_no_argument(self):
        self.assertEqual(max_integer(), None)

    def test_string(self):
        self.assertEqual(max_integer("jghfhgjf"), "j")

    def test_not_iteratable(self):
        with self.assertRaises(TypeError):
            max_integer(1)

if __name__ == "__main__":
    unittest.main()
