import unittest
from topic3.more_functions import string_functions as sf


class MyTestCase(unittest.TestCase):
    def test_multiply_string(self):
        self.assertEqual("DanielDanielDanielDanielDanielDanielDaniel", sf.multiply_string('Daniel', 7))


if __name__ == '__main__':
    unittest.main()
