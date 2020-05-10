import unittest

from duplicated_letters import duplicate_count


class TestDuplicatedLetters(unittest.TestCase):

    def test_case_a(self):
        string = ''
        self.assertEqual(duplicate_count(string), 0)

    def test_case_b(self):
        string = 'abcde'
        self.assertEqual(duplicate_count(string), 0)

    def test_case_c(self):
        string = 'abcdeaa'
        self.assertEqual(duplicate_count(string), 1)

    def test_case_d(self):
        string = 'abcdeaB'
        self.assertEqual(duplicate_count(string), 2)

    def test_case_e(self):
        string = 'Indivisibilities'
        self.assertEqual(duplicate_count(string), 2)

    def test_case_f(self):
        string = 'abcdefghijklmnopqrstuvwxyz'
        self.assertEqual(duplicate_count(string), 0)

    def test_case_g(self):
        string = 'abcdefghijklmnopqrstuvwxyz' + 'aaAb'
        self.assertEqual(duplicate_count(string), 2)

    def test_case_h(self):
        lowercase = 'abcdefghijklmnopqrstuvwxyz'
        uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.assertEqual(duplicate_count(lowercase+lowercase), 26)


if __name__ == '__main__':
    unittest.main()        