import unittest

from by3_or_not_by3 import divisible_by_three


class TestDivisibleByThree(unittest.TestCase):

    def test_true(self):
        num = 8409
        self.assertTrue(divisible_by_three(num), True)

    def test_false(self):
        num = 100853
        self.assertFalse(divisible_by_three(num), False)


if __name__ == '__main__':
    unittest.main()