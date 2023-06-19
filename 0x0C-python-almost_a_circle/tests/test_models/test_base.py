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


if __name__ == '__main__':
    unittest.main()
