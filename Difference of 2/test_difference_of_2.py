import unittest

from difference_of_2 import twos_difference


class TestDifferenceOfTwo(unittest.TestCase):

    def test_case_a(self):
        lista = [1, 2, 3, 4]
        self.assertEqual(twos_difference(lista), [(1, 3), (2, 4)])

    def test_case_b(self):
        lista = [1, 23, 3, 4, 7]
        self.assertEqual(twos_difference(lista), [(1, 3)])

    def test_case_c(self):
        lista = [4, 3, 1, 5, 6]
        self.assertEqual(twos_difference(lista), [(1, 3), (3, 5), (4, 6)])

if __name__ == '__main__':
    unittest.main()