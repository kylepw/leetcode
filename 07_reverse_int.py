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

def reverse(x):
    rev = 0
    while x > 0:
        pop = x % 10
        x //= 10
        rev = rev * 10 + pop
    return rev

def reverse_num(x):
    if x > 2**31 - 1 or x < -2**31:
        return 0
    if -10 < x < 10:
        return x
    reversed_x = str(x)[::-1]
    if reversed_x.startswith('0'):
        i = 0
        while reversed_x[i] == '0':
            i += 1
        reversed_x = reversed_x[i:]
    if reversed_x.endswith('-'):
        reversed_x = '-' + reversed_x[:-1]
    result = int(reversed_x)
    if result > 2**31 - 1 or result < -2**31:
        return 0
    return int(reversed_x)


class TestReverse(unittest.TestCase):
    def setUp(self):
        self.data = {
            123: 321,
            -456: -654,
            120: 21,
        }

    def test_reverse_num(self):
        for x, expected in self.data.items():
            self.assertEqual(reverse_num(x), expected)

    def test_reverse(self):
        for x, expected in self.data.items():
            self.assertEqual(reverse(x), expected)


if __name__ == "__main__":
    unittest.main()