from unittest import TestCase

from helpers import convert_first_index_to_str


class TestConvertFirstIndexToStr(TestCase):
    def test_convert_positive_integer(self):
        starting_tuple = (1, "hello")
        converted_tuple = convert_first_index_to_str(starting_tuple)

        self.assertEqual(('1', 'hello'), converted_tuple)

