"""6. Zig Zag Conversion

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like
this: (you may want to display this pattern in a fixed font for better legibility)

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:
"""
import unittest


def convert(s, numRows):
    parsed = [[] for _ in range(numRows)]
    if numRows < 2:
        return s

    current_row = 0
    going_down = False

    for c in s:
        parsed[current_row].append(c)
        if current_row == 0 or current_row == (numRows - 1):
            going_down = not going_down
        current_row += 1 if going_down else -1

    return ''.join([c for row in parsed for c in row])


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