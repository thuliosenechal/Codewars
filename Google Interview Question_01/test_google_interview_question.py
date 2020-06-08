import unittest

from google_interview_question import get_strings


class TestGetStrings(unittest.TestCase):

    def test_case_a(self):
        city = 'Chicago'
        self.assertEqual(get_strings(city), "c:**,h:*,i:*,a:*,g:*,o:*")

    def test_case_b(self):
        city = 'Bangkok'
        self.assertEqual(get_strings(city), "b:*,a:*,n:*,g:*,k:**,o:*")

    def test_case_c(self):
        city = 'Las Vegas'
        self.assertEqual(get_strings(city), "l:*,a:**,s:**,v:*,e:*,g:*")


if __name__ == '__main__':
    unittest.main()