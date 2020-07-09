import unittest

from permutations import permutations


class TestPermutation(unittest.TestCase):

    def test_case_a(self):
        string = 'ab'
        self.assertEqual(permutations(string), ['ab', 'ba'])

    def test_case_b(self):
        string = 'aabb'
        self.assertEqual(permutations(string), ['aabb', 'abab', 'abba', 
                                                'baab', 'baba', 'bbaa'])


if __name__ == '__main__':
    unittest.main()
