"""
Program: test_string_functions.py
Author: Daniel Meeker
Date: 6/15/2020

This program defines and tests a function to multiply strings.
"""
import unittest
from topic3.more_functions import string_functions as sf


class MyTestCase(unittest.TestCase):
    def test_multiply_string(self):
        self.assertEqual("DanielDanielDanielDanielDanielDanielDaniel", sf.multiply_string('Daniel', 7))


if __name__ == '__main__':
    unittest.main()
