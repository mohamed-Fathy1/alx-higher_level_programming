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

if __name__ == '__main__':
    unittest.main()
