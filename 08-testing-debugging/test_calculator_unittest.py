"""Tests using the standard library's unittest module."""

import unittest
from calculator import add, divide, is_palindrome

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)

    def test_divide_by_zero_raises(self):
        with self.assertRaises(ValueError):
            divide(10, 0)

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome("A man a plan a canal Panama".replace(" ", "")))
        self.assertFalse(is_palindrome("hello"))


if __name__ == "__main__":
    unittest.main()
