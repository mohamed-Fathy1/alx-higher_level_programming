#!/usr/bin/python3
'''testfrom models.rectangle import Rectangle Module'''
from models.base import Base
from models.rectangle import Rectangle
import unittest


class TestRectangle(unittest.TestCase):
    '''test from models.rectangle import Rectangle class'''

    def test_is_an_instance(self):
        self.assertIsInstance(Rectangle(5, 10), Base)

    def test_width_getter(self):
        rect1 = Rectangle(8, 5)
        self.assertEqual(rect1.width, 8)

    def test_width_setter(self):
        rect1 = Rectangle(8, 5)
        rect1.width = 10
        self.assertEqual(rect1.width, 10)

    def test_height_getter(self):
        rect1 = Rectangle(8, 5)
        self.assertEqual(rect1.height, 5)

    def test_height_setter(self):
        rect1 = Rectangle(8, 5)
        rect1.height = 10
        self.assertEqual(rect1.height, 10)

    def test_defult(self):
        rect1 = Rectangle(8, 5)
        self.assertEqual(rect1.width, 8)
        self.assertEqual(rect1.height, 5)
        self.assertEqual(rect1.x, 0)
        self.assertEqual(rect1.y, 0)
        self.assertEqual(rect1.id, 7)

    def test_id(self):
        rect1 = Rectangle(8, 5, id=12)
        self.assertEqual(rect1.id, 12)

    def test_x_getter(self):
        r = Rectangle(10, 20, 5, 10)
        self.assertEqual(r.x, 5)

    def test_x_setter(self):
        r = Rectangle(10, 20, 5, 10)
        r.x = 15
        self.assertEqual(r.x, 15)

    def test_y_getter(self):
        r = Rectangle(10, 20, 5, 10)
        self.assertEqual(r.y, 10)

    def test_y_setter(self):
        r = Rectangle(10, 20, 5, 10)
        r.y = 15
        self.assertEqual(r.y, 15)

    def test_named_arg(self):
        r = Rectangle(10, 20, 5, 10, id=10)
        self.assertEqual(r.id, 10)

    def test_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_three_args(self):
        r1 = Rectangle(2, 2, 4)
        r2 = Rectangle(4, 4, 2)
        self.assertEqual(r1.id, r2.id - 1)

    def test_four_args(self):
        r1 = Rectangle(1, 2, 3, 4)
        r2 = Rectangle(4, 3, 2, 1)
        self.assertEqual(r1.id, r2.id - 1)

    def test_five_args(self):
        self.assertEqual(7, Rectangle(10, 2, 0, 0, 7).id)

    def test_more_than_five_args(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)


if __name__ == '__main__':
    unittest.main()
