import unittest

from narcissistic import narcissistic


class TestNarcissistic(unittest.TestCase):
    
    def test_case_true(self):
        self.assertTrue(narcissistic(371))

    def test_case_false(self):
        self.assertFalse(narcissistic(122))


if __name__ == '__main__':
    unittest.main()