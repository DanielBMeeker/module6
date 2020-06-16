import unittest
from topic4.more_functions import validate_input_in_functions as vf


class MyTestCase(unittest.TestCase):
    def test_score_input_test_name(self):
        self.assertEqual("Python: 0", vf.score_input('Python'))


if __name__ == '__main__':
    unittest.main()
