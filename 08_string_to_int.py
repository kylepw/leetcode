"""8. String to Integer

Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary
until the first non-whitespace character is found. Then, starting from
this character, takes an optional initial plus or minus sign followed
by as many numerical digits as possible, and interprets them as a
numerical value.

The string can contain additional characters after those that form the
integral number, which are ignored and have no effect on the behavior
of this function.

If the first sequence of non-whitespace characters in str is not a
valid integral number, or if no such sequence exists because either
str is empty or it contains only whitespace characters, no conversion
is performed.

If no valid conversion could be performed, a zero value is returned.

Note:

Only the space character ' ' is considered as whitespace character.
Assume we are dealing with an environment which could only store
integers within the 32-bit signed integer range: [−231,  231 − 1]. If
the numerical value is out of the range of representable values,
INT_MAX (231 − 1) or INT_MIN (−231) is returned.
"""
import unittest


def my_atoi(s):
    if len(s) < 1:
        return 0
    s = list(s.strip())
    if not str.isdigit(s[0]) and s[0] not in ('-', '+'):
        return 0
    is_neg = True if s[0] == '-' else False
    if s[0] in ('-', '+'):
        del s[0]
    i = x = 0
    while x < len(s) and str.isdigit(s[x]):
        i = i * 10 + ord(s[x]) - ord('0')
        x += 1
    if x < 1:
        # No numbers
        return 0
    if i > 2**31 - 1:
        if is_neg:
            return -2**31
        return 2**31 - 1
    return -i if is_neg else i


class TestMyAtoi(unittest.TestCase):
    def setUp(self):
        self.data = {
            '+1': 1,
            '42': 42,
            '   -42': -42,
            '4193 with words': 4193,
            'words and 987': 0,
            '-91283472332': -2147483648,
        }

    def test_my_atoi(self):
        for arg, expected in self.data.items():
            self.assertEqual(my_atoi(arg), expected)


if __name__ == "__main__":
    unittest.main()