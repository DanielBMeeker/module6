import unittest
from topic4.more_functions import validate_input_in_functions as vf


class MyTestCase(unittest.TestCase):
    def test_score_input_test_name(self):
        self.assertEqual("Python: 0", vf.score_input('Python'))

    def test_score_input_test_score_valid(self):
        self.assertEqual("Python: 98", vf.score_input('Python', 98))

    def test_score_input_test_score_below_range(self):
        self.assertRaises(ValueError, vf.score_input('Python', -5))

    def test_score_input_test_score_above_range(self):
        self.assertRaises(ValueError, vf.score_input('Python', 115))

    def test_score_input_test_score_non_numeric(self):
        self.assertRaises(ValueError, vf.score_input('Python', 'Ten'))


if __name__ == '__main__':
    unittest.main()
