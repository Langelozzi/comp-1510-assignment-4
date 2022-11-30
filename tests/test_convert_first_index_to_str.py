from unittest import TestCase

from helpers import convert_first_index_to_str


class TestConvertFirstIndexToStr(TestCase):
    def test_convert_positive_integer(self):
        starting_tuple = (1, "hello")
        converted_tuple = convert_first_index_to_str(starting_tuple)

        self.assertEqual(('1', 'hello'), converted_tuple)

    def test_convert_negative_integer(self):
        starting_tuple = (-1, "hello")
        converted_tuple = convert_first_index_to_str(starting_tuple)

        self.assertEqual(('-1', 'hello'), converted_tuple)

    def test_convert_zero_integer(self):
        starting_tuple = (0, "hello")
        converted_tuple = convert_first_index_to_str(starting_tuple)

        self.assertEqual(('0', 'hello'), converted_tuple)

    def test_convert_positive_float(self):
        starting_tuple = (435.67, "hello")
        converted_tuple = convert_first_index_to_str(starting_tuple)

        self.assertEqual(('435.67', 'hello'), converted_tuple)

    def test_convert_negative_float(self):
        starting_tuple = (-435.67, "hello")
        converted_tuple = convert_first_index_to_str(starting_tuple)

        self.assertEqual(('-435.67', 'hello'), converted_tuple)

    def test_convert_string(self):
        starting_tuple = ("Chris", "hello")
        converted_tuple = convert_first_index_to_str(starting_tuple)

        self.assertEqual(('Chris', 'hello'), converted_tuple)

    def test_convert_list(self):
        starting_tuple = ([1, 2, "apple", True], "hello")
        converted_tuple = convert_first_index_to_str(starting_tuple)

        self.assertEqual(("[1, 2, 'apple', True]", 'hello'), converted_tuple)

    def test_convert_tuple(self):
        starting_tuple = ((1, 2, "apple", True), "hello")
        converted_tuple = convert_first_index_to_str(starting_tuple)

        self.assertEqual(("(1, 2, 'apple', True)", 'hello'), converted_tuple)

    def test_convert_dictionary(self):
        starting_tuple = ({1: "run"}, "hello")
        converted_tuple = convert_first_index_to_str(starting_tuple)

        self.assertEqual(("{1: 'run'}", 'hello'), converted_tuple)

    def test_convert_boolean(self):
        starting_tuple = (True, "hello")
        converted_tuple = convert_first_index_to_str(starting_tuple)

        self.assertEqual(('True', 'hello'), converted_tuple)

    def test_convert_long_tuple(self):
        starting_tuple = (True, "hello", 4, [1, 2, 3], False, 9.4, 90, 'tree')
        converted_tuple = convert_first_index_to_str(starting_tuple)

        self.assertEqual(('True', 'hello', 4, [1, 2, 3], False, 9.4, 90, 'tree'), converted_tuple)

