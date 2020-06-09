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

    def test_base4(self):
        res1 = [{'height': 4, 'width': 10, 'id': 89}, {'height': 7, 'width': 1, 'id': 7}]
        list_input = [
        {'id': 89, 'width': 10, 'height': 4}, 
        {'id': 7, 'width': 1, 'height': 7}
    ]
    json_list_input = Rectangle.to_json_string(list_input)
    list_output = Rectangle.from_json_string(json_list_input)
    self.assertEqual(res1, list_input)

'''
Recangle info
-----------------
order: width, height, x=0, y=0, id=None
return {
            "x" : self.x,
            "y" : self.y,
            "id" : self.id,
            "height" : self.height,
            "width" : self.width
        }
'''
