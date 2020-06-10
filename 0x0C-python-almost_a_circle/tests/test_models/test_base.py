from models.base import Base
from models.rectangle import Rectangle
import json
import unittest

class TestBase(unittest.TestCase):
    def test_base1(self):
        x = Base()
        self.assertEqual(x.id, 1)

    def test_base2(self):
        x1 = Base(20)
        self.assertEqual(x1.id, 20)

    def test_base3(self):
        x2 = Base()
        self.assertEqual(x2.id, 2)

    
