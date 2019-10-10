"""6. Zig Zag Conversion

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like
this: (you may want to display this pattern in a fixed font for better legibility)

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:
"""
import unittest


def convert(s, numRows):
    parsed = [[] for _ in range(numRows)]

    counter = i = j = 0
    while i < len(s):
        if j >= len(parsed):
            j = 0
        if counter == numRows:
            counter = -1
            diagonal_row = numRows - 2
            while i < len(s) and diagonal_row > 0:
                parsed[diagonal_row].append(s[i])
                diagonal_row -= 1
                i += 1
            j = 0
        else:
            parsed[j].append(s[i])
            j += 1
            i += 1
        counter += 1
    return ''.join([item for row in parsed for item in row])


class TestConvert(unittest.TestCase):
    def setUp(self):
        self.data = {
            ('PAYPALISHIRING', 3): 'PAHNAPLSIIGYIR',
            ('PAYPALISHIRING', 4): 'PINALSIGYAHRPI',
        }

    def test_convert(self):
        for args, expected in self.data.items():
            self.assertEqual(convert(*args), expected)


if __name__ == "__main__":
    unittest.main()