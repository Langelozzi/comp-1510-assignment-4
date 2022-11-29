from unittest import TestCase

from helpers import cleanse


class TestCleanse(TestCase):
    def test_cleanse_all_lower_case_no_whitespace(self):
        dirty_string = "hello world"
        clean_string = cleanse(dirty_string)

        self.assertEqual(dirty_string, clean_string)

    def test_cleanse_all_lower_case_mixed_whitespace(self):
        dirty_string = "\t  \n \n hello world    \t\t\t  \n "
        clean_string = cleanse(dirty_string)

        self.assertEqual("hello world", clean_string)

    def test_cleanse_mixed_case_no_whitespace(self):
        dirty_string = "hElLo wOrLD"
        clean_string = cleanse(dirty_string)

        self.assertEqual("hello world", clean_string)

    def test_cleanse_mixed_case_mixed_whitespace(self):
        dirty_string = "\t  \n \n hElLo wOrLD   \n "
        clean_string = cleanse(dirty_string)

        self.assertEqual("hello world", clean_string)

    def test_cleanse_all_upper_case_no_whitespace(self):
        dirty_string = "HELLO WORLD"
        clean_string = cleanse(dirty_string)

        self.assertEqual("hello world", clean_string)

    def test_cleanse_all_upper_case_mixed_whitespace(self):
        dirty_string = "\n   \t  \n       HELLO WORLD \t\t\n \n   \t  \n"
        clean_string = cleanse(dirty_string)

        self.assertEqual("hello world", clean_string)

    def test_cleanse_none_alphabetic_characters_mixed_whitespace(self):
        dirty_string = " \t   \n [1, 2, 3, 4] ('apple', True, False, None, 2.5) \n \t "
        clean_string = cleanse(dirty_string)

        self.assertEqual("[1, 2, 3, 4] ('apple', true, false, none, 2.5)", clean_string)

    def test_cleanse_only_whitespace(self):
        dirty_string = " \t   \n    \t \n \n\n \t     \n \t "
        clean_string = cleanse(dirty_string)

        self.assertEqual("", clean_string)

