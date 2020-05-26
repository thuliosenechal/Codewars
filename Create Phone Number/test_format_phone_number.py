import unittest

from format_phone_number import create_phone_number


class TestFormatPhoneNumber(unittest.TestCase):

    def test_case_a(self):
        lista = [5, 0, 5, 1, 8, 2, 7, 4, 2, 7]
        self.assertEqual(create_phone_number(lista), '(505) 182-7427')

    def test_case_b(self):
        lista = [4, 9, 4, 4, 6, 1, 8, 6, 3, 1]
        self.assertEqual(create_phone_number(lista), '(494) 461-8631')


if __name__ == '__main__':
    unittest.main()
