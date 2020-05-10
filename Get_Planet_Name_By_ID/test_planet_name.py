import unittest

from planet_name import get_planet_name


class TestPlanetName(unittest.TestCase):

    def test_case_a(self):
        id = 2
        self.assertEqual(get_planet_name(id), 'Venus')

    def test_case_b(self):
        id = 6
        self.assertEqual(get_planet_name(id), 'Saturn')

    def test_case_c(self):
        id = 10
        self.assertEqual(get_planet_name(id), None)


if __name__ == '__main__':
    unittest.main()     