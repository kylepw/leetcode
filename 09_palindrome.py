"""9. Palindrome Number

Determine whether an integer is a palindrome. An integer is
a palindrome when it reads the same backward as forward.

"""
import unittest


def is_palindrome(i):
    pass


class TestIsPalindrome(unittest.TestCase):
    def setUp(self):
        self.data = {
            121: True,
            -121: False,
            10: False,
        }

    def test_is_palindrome(self):
        for arg, expected in self.data.items():
            self.assertEqual(is_palindrome(arg), expected)

if __name__ == "__main__":
    unittest.main()