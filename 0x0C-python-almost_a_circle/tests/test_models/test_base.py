#!/usr/bin/python3
'''test Module'''
from models.base import Base
import unittest


class TestBase(unittest.TestCase):
    '''test Base class'''

    def setUp(self) -> None:
        '''run on every test fuction call'''
        self.base2 = Base()
        self.base1 = Base(12)
        self.base3 = Base()
        self.base4 = Base()
        self.base5 = Base()

    def test_id(self):
        '''test id'''
        self.assertEqual(self.base2.id, 1)
        self.assertEqual(self.base1.id, 12)
        self.assertEqual(self.base3.id, 2)
        self.assertEqual(self.base4.id, 3)
        self.assertEqual(self.base5.id, 4)
