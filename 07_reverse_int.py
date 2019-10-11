"""7. Reverse Integer

Given a 32-bit signed integer, reverse digits of an integer.

Input: 123
Output: 321

Input: -123
Output: -321

Input: 120
Output: 21

Note:
Assume we are dealing with an environment which could only store integers
within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose
of this problem, assume that your function returns 0 when the reversed
integer overflows.
"""
import unittest


def reverse(x: int) -> int:
    pass


class TestReverse(unittest.TestCase):
    def setUp(self):
        self.data = {
            123: 321,
            -456: -654,
            120: 21,
        }

    def test_reverse(self):
        for x, expected in self.data.items():
            self.assertEqual(reverse(x), expected)


if __name__ == "__main__":
    unittest.main()