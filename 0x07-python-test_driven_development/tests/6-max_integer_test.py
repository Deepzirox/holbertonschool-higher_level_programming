import unittest
"""[Unittest for max_integer]
"""
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """[Test for max integet function]

    Arguments:
        unittest {[testing]} -- module for use unittest.testcases
    """
    def test_results(self):
        """[test_results]
        """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([0]), 0)

    def test_fails(self):
        """[test_fails]
        """
        self.assertRaises(TypeError, max_integer, 123)
        self.assertRaises(TypeError, max_integer, True)
