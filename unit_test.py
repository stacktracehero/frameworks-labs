import unittest
from math_operation import add_nums

class TestMathOperations(unittest.TestCase):
    def test_add_nums_positive(self):
        self.assertEqual(add_nums(2, 3), 5)

if __name__ == "__main__":
    unittest.main()
