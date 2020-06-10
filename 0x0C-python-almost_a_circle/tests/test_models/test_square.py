#!/usr/bin/python3
from models.base import Base
from models.square import Square
import unittest

"""
testing
"""


class TestSquare(unittest.TestCase):
    """
    Testing class
    """
    def test_square(self):
        x = Base()
        self.assertEqual(x.id, 5)

    def test_square2(self):
        x1 = Base(20)
        self.assertEqual(x1.id, 20)

    def test_square3(self):
        x2 = Base()
        self.assertEqual(x2.id, 6)
