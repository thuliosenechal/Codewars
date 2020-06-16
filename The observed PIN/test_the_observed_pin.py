import unittest

from the_observed_pin import get_pins


class TestPin(unittest.TestCase):
    
    def test_case_a(self):
        number = '8'
        result = ['5','7','8','9','0']
        self.assertEqual(get_pins(number), result)

    def test_case_b(self):
        number = '11'
        result = ['11', '12', '14', '21', '22', '24', '41', '42', '44']
        self.assertEqual(get_pins(number), result)


if __name__ == '__main__':
    unittest.main()
    