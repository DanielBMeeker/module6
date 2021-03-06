"""
Program: test_valid_input_in_functions
Author: Daniel Meeker
Date: 6/17/2020

This program defines and tests a function to validate input that is
used as a parameter of the function.
"""
import unittest
from topic4.more_functions import validate_input_in_functions as vf


class MyTestCase(unittest.TestCase):
    def test_score_input_test_name(self):
        self.assertEqual("Python: 0", vf.score_input('Python'))

    def test_score_input_test_score_valid(self):
        self.assertEqual("Python: 98", vf.score_input('Python', 98))

    def test_score_input_test_score_below_range(self):
        with self.assertRaises(ValueError):
            vf.score_input('Python', -5)

    def test_score_input_test_score_above_range(self):
        with self.assertRaises(ValueError):
            vf.score_input('Python', 115)

    def test_score_input_test_score_non_numeric(self):
        with self.assertRaises(ValueError):
            vf.score_input('Python', 'Ten')

    def test_score_input_invalid_message(self):
        with self.assertRaises(ValueError):
            vf.score_input('Python', '110', 'Score too high')


if __name__ == '__main__':
    unittest.main()
