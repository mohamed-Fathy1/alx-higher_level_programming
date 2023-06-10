#!/usr/bin/python3
"""Unittest modul"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_list_length(self):
        """test"""
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer(()), None)
        self.assertEqual(max_integer('a'), 'a')
        self.assertRaises(TypeError, max_integer, (5))
        self.assertEqual(max_integer(''), None)
        self.assertEqual(max_integer([5]), 5)

    def test_higher_list_dimensions(self):
        """test function"""
        self.assertEqual(max_integer([[[8, 2], [2], []], [[4], [5]], [[6]]]),
                         [[8, 2], [2], []])
        self.assertEqual(max_integer([{5, 4}, {6, 3, 1}, {20}]), {4, 5})
        self.assertEqual(max_integer([[5, 4, 1], [6, 3], []]), [6, 3])
        self.assertEqual(max_integer([(5, 4, 1), (6, 3), ()]), (6, 3))
        self.assertEqual(max_integer([[[1, 2], [2], []], [[4], [5]], [[6]]]),
                         [[6]])
        self.assertEqual(max_integer(['azzz', 'byy', 'cx']), 'cx')

    def test_first_list_dimension_type(self):
        """test """
        self.assertEqual(max_integer(['a', 'b']), 'b')
        self.assertRaises(TypeError, max_integer, [3, 'a'])
        self.assertEqual(max_integer([-1, -.5, False]), False)
        self.assertEqual(max_integer([5, .544, True]), 5)
        self.assertEqual(max_integer([3, 5.0]), 5.0)
        self.assertEqual(max_integer([3, -5.3456]), 3)

    def test_list_type(self):
        """Test function"""
        self.assertRaises(TypeError, max_integer, 5)
        self.assertRaises(TypeError, max_integer, True)
        self.assertEqual(max_integer((3, 5)), 5)
        self.assertEqual(max_integer('actg'), 't')
        self.assertRaises(TypeError, max_integer, {3, 5})
        self.assertEqual(max_integer([3, 5]), 5)

if __name__ == '__main__':
    unittest.main()
