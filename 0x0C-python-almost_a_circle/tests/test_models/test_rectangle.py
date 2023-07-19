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
        self.assertEqual(rect1.id, 29)

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


class TestRectangleExptions(unittest.TestCase):
    def test_instantiation(self):
        r = Rectangle(10, 20, 5, 10, 1)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 20)
        self.assertEqual(r.x, 5)
        self.assertEqual(r.y, 10)
        self.assertEqual(r.id, 1)

    def test_width_setter(self):
        r = Rectangle(10, 20)
        r.width = 15
        self.assertEqual(r.width, 15)
        with self.assertRaises(TypeError):
            r.width = "invalid"
        with self.assertRaises(ValueError):
            r.width = -5

    def test_height_setter(self):
        r = Rectangle(10, 20)
        r.height = 15
        self.assertEqual(r.height, 15)
        with self.assertRaises(TypeError):
            r.height = "invalid"
        with self.assertRaises(ValueError):
            r.height = -5

    def test_x_setter(self):
        r = Rectangle(10, 20)
        r.x = 15
        self.assertEqual(r.x, 15)
        with self.assertRaises(TypeError):
            r.x = "invalid"
        with self.assertRaises(ValueError):
            r.x = -5

    def test_y_setter(self):
        r = Rectangle(10, 20)
        r.y = 15
        self.assertEqual(r.y, 15)
        with self.assertRaises(TypeError):
            r.y = "invalid"
        with self.assertRaises(ValueError):
            r.y = -5

    def test_bad_width(self):
        with self.assertRaises(ValueError) as cm:
            r = Rectangle(-10, 20, 5, 10)
        self.assertEqual(str(cm.exception), "width must be > 0")

    def test_bad_height(self):
        with self.assertRaises(ValueError) as cm:
            r = Rectangle(10, -20, 5, 10)
        self.assertEqual(str(cm.exception), "height must be > 0")

    def test_bad_x(self):
        with self.assertRaises(ValueError) as cm:
            r = Rectangle(10, 20, -5, 10)
        self.assertEqual(str(cm.exception), "x must be >= 0")

    def test_bad_y(self):
        with self.assertRaises(ValueError) as cm:
            r = Rectangle(10, 20, 5, -10)
        self.assertEqual(str(cm.exception), "y must be >= 0")

    def test_type_error_width(self):
        with self.assertRaises(TypeError) as cm:
            r = Rectangle("10", 20, 5, 10)
        self.assertEqual(str(cm.exception), "width must be an integer")

    def test_type_error_height(self):
        with self.assertRaises(TypeError) as cm:
            r = Rectangle(10, "20", 5, 10)
        self.assertEqual(str(cm.exception), "height must be an integer")

    def test_type_error_x(self):
        with self.assertRaises(TypeError) as cm:
            r = Rectangle(10, 20, "5", 10)
        self.assertEqual(str(cm.exception), "x must be an integer")

    def test_type_error_y(self):
        with self.assertRaises(TypeError) as cm:
            r = Rectangle(10, 20, 5, "10")
        self.assertEqual(str(cm.exception), "y must be an integer")

    def test_negative_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-5, 2)

    def test_zero_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)

    def test_None_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 2)

    def test_str_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("Hello", 2)

    def test_float_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(2.5, 2)

    def test_complex_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(complex(4), 2)

    def test_list_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([1, 2, 3], 2)

    def test_dict_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({"a": 1, "b": 2, "c": 3}, 2)

    def test_bool_width(self):
        with self.assertRaises(ValueError) as cm:
            r = Rectangle(False, 10)
        self.assertEqual(str(cm.exception), "width must be > 0")

    def test_tuple_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle((1, 2, 3), 2)

    def test_set_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({1, 2, 3}, 2)

    def test_frozenset_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(frozenset({1, 2, 3}), 2)

    def test_inf_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('inf'), 2)

    def test_NaN_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('nan'), 2)

class RectangleOrderofInitializationTestCase(unittest.TestCase):
    """Unittests for testing Rectangle order of attribute initialization"""

    def test_width_before_height(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("input width", "input height")

    def test_width_before_x(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("input width", 2,"input x")

    def test_width_before_y(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("input width", 2, 3, "input Y")

    def test_height_before_x(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, "input height", "input x")

    def test_height_before_y(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, "input height", 3, "input Y")

    def test_x_before_y(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(5, 6, "input x", "input Y")

class Rectangle_YTestCase(unittest.TestCase):
    """Unittests for testing initialization of Rectangle y attribute."""

    def test_None_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, None)

    def test_str_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, "invalid")

    def test_float_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, 5.5)

    def test_complex_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, complex(5))

    def test_dict_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, {"a": 1, "b": 2})

    def test_list_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, [1, 2, 3])

    def test_set_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, {1, 2, 3})

    def test_tuple_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, (1, 2, 3))

    def test_frozenset_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, frozenset({1, 2, 3, 1}))

    def test_inf_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, float('inf'))

    def test_nan_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, float('nan'))

    def test_negative_y(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(3, 5, 0, -1)

class TestArea(unittest.TestCase):
    '''Area test'''

    def test_area_large(self):
        r = Rectangle(9999999999999, 999999999999999)
        self.assertEqual(9999999999998990000000000001, r.area())

    def test_area_changed_attributes(self):
        r = Rectangle(15, 10)
        r.width = 3
        r.height = 7
        self.assertEqual(21, r.area())

    def test_area_one_arg(self):
        r = Rectangle(2, 10)
        with self.assertRaises(TypeError):
            r.area(1)

    def test_area_int(self):
        r = Rectangle(10, 20)
        self.assertEqual(r.area(), 200)


if __name__ == '__main__':
    unittest.main()
