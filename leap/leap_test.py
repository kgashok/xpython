try:
    from year import Year
except ImportError:
    raise SystemExit('Could not find year.py. Does it exist?')

import unittest


class YearTest(unittest.TestCase):
    def test_leap_year(self):
        self.assertTrue(Year(1996).is_leap_year())

    def test_non_leap_year(self):
        self.assertFalse(Year(1997).is_leap_year())

    def test_non_leap_even_year(self):
        self.assertFalse(Year(1998).is_leap_year())

    def test_century(self):
        self.assertFalse(Year(1900).is_leap_year())

    def test_exceptional_century(self):
        self.assertTrue(Year(2400).is_leap_year())

if __name__ == '__main__':
    unittest.main()

