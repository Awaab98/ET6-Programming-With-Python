import unittest
from math_operations import add, subtract

class TestMathOperations(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(add(2, 3), 5)  # Test case 1
        self.assertEqual(add(-1, 1), 0)  # Test case 2

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)  # Test case 1
        self.assertEqual(subtract(0, 5), -5)  # Test case 2

if __name__ == '__main__':
    unittest.main()
