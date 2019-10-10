"""5. Longest Palindromic Substring

Given a string s, find the longest palindromic substring in s. You may assume
that the maximum length of s is 1000.

"""
from collections import defaultdict
import unittest


def is_palindrome(s):
    low = 0
    high = len(s) - 1
    while low < high:
        if s[low] != s[high]:
            return False
        low += 1
        high -= 1
    return True


def longestPalindrome(s: str) -> str:
    if len(s) == 1:
        return s
    s1 = s[::-1]
    if s == s1:
        longest = s
    else:
        longest = ''
        for i in range(len(s)):
            i1 = s1.find(s[i])
            j, j1 = i, i1
            while i1 >= 0:
                sub = []
                while j < len(s) and j1 < len(s1) and s[j] == s1[j1]:
                    sub.append(s[j])
                    j += 1
                    j1 += 1
                sub = ''.join(sub)
                longest = longest if len(longest) > len(sub) else sub
                i1 = s1.find(s[i], i1 + 1)
    return longest


class TestlongestPalindrome(unittest.TestCase):
    def setUp(self):
        self.data = {
            'babad': 'aba',
            'cbbd': 'bb',
            'bb': 'bb',
        }

    def test_longest_palindrome(self):
        for arg, result in self.data.items():
            self.assertEqual(longestPalindrome(arg), result)


if __name__ == "__main__":
    unittest.main()