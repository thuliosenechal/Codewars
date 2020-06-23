import unittest
from generate_hashtag import generate_hashtag


class TestGenerateHashTag(unittest.TestCase):

    def test_case_a(self):
        s = 'Do We have A Hashtag'
        self.assertEqual(generate_hashtag(s), '#DoWeHaveAHashtag')

    def test_case_b(self):
        s = 'Codewars      '
        self.assertEqual(generate_hashtag(s), '#Codewars')

    def test_case_c(self):
        s = ''
        self.assertFalse(generate_hashtag(s))

    def test_case_d(self):
        s = 'Loooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo \
             ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo \
             oooooooooooooooooooooooooooooong Cat'
        self.assertEqual(generate_hashtag(s), False)


if __name__ == '__main__':
    unittest.main()
    