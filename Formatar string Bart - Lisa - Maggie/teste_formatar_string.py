import unittest

from formatar_string import namelist


class TestFormatString(unittest.TestCase):

    def test_case_a(self):
        list_name = [{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'},{'name': 'Homer'},{'name': 'Marge'}]
        self.assertEqual(namelist(list_name), 'Bart, Lisa, Maggie, Homer & Marge')
        
    def test_case_b(self):
        list_name = [{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'}]
        self.assertEqual(namelist(list_name), 'Bart, Lisa & Maggie')

    def test_case_c(self):
        list_name = [{'name': 'Bart'},{'name': 'Lisa'}]
        self.assertEqual(namelist(list_name), 'Bart & Lisa')

    def test_case_d(self):
        list_name = [{'name': 'Bart'}]
        self.assertEqual(namelist(list_name), 'Bart')

    def test_case_e(self):
        list_name = []
        self.assertEqual(namelist(list_name), '')


if __name__ == '__main__':
    unittest.main()        