#!/usr/bin/python3
'''test Module'''
from models.base import Base
import unittest


class TestBase(unittest.TestCase):
    '''test Base class'''

    def test_id(self):
        base1 = Base(12)
        base2 = Base(24)
        self.assertEqual(base1.id, 12)
        self.assertEqual(base2.id, 24)

    def test_no_args(self):
        base1 = Base()
        base2 = Base()
        self.assertEqual(base1.id, base2.id - 1)

    def test_None_id(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_unique_id(self):
        self.assertEqual(12, Base(12).id)

    def test_nb_instances_after_unique_id(self):
        b1 = Base()
        b2 = Base(12)
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 1)

    def test_id_public(self):
        b = Base(12)
        b.id = 9
        self.assertEqual(9, b.id)

    def test_nb_instances_private(self):
        with self.assertRaises(AttributeError):
            print(Base(12).__nb_intances)

    def test_float_id(self):
        self.assertEqual(3.5, Base(3.5).id)

    def test_str_id(self):
        self.assertEqual("str", Base("str").id)

    def test_complex_id(self):
        self.assertEqual(complex(7), Base(complex(7)).id)

    def test_list_id(self):
        self.assertEqual([1, 2, 3], Base([1, 2, 3]).id)

    def test_dict_id(self):
        self.assertEqual({"a": 1, "b": 2, "c": 3},
                         Base({"a": 1, "b": 2, "c": 3}).id)

    def test_tuple_id(self):
        self.assertEqual((1, 2), Base((1, 2)).id)

    def test_bool_id(self):
        self.assertEqual(True, Base(True).id)

    def test_set_id(self):
        self.assertEqual({1, 2, 3}, Base({1, 2, 3}).id)

    def test_frozenset_id(self):
        self.assertEqual(frozenset({1, 2, 3}), Base(frozenset({1, 2, 3})).id)

    def test_inf_id(self):
        self.assertEqual(float('inf'), Base(float('inf')).id)

    # def test_NaN_id(self):
        # self.assertEqual(math.isnan(float('nan')),
        # math.isnan(Base(float('nan')).id))

    def test_two_args(self):
        with self.assertRaises(TypeError):
            Base(1, 2)


if __name__ == '__main__':
    unittest.main()
