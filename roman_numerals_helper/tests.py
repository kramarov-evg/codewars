import unittest
import os
from roman_numerals_helper import RomanNumerals as RN


class Tests(unittest.TestCase):

    def test_from_roman(self):
        path_to_data = os.path.join(os.curdir, 'roman_numerals_helper', '__test_data_roman__.txt')
        with open(path_to_data, 'r') as test_data:
            for data in enumerate(test_data, 1):
                self.assertEqual(RN.from_roman(data[1].strip()), data[0],
                                 msg="{} should result in {}".format(data[0], data[1].strip()))

    def test_to_roman(self):
        path_to_data = os.path.join(os.curdir, 'roman_numerals_helper', '__test_data_roman__.txt')
        with open(path_to_data, 'r') as test_data:
            for data in enumerate(test_data, 1):
                self.assertEqual(RN.to_roman(data[0]), data[1].strip(),
                                 msg="{} should result in {}".format(data[1].strip(), data[0]))


if __name__ == "__main__":
    unittest.main(verbosity=2)
