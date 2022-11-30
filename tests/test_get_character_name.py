from unittest import TestCase
from unittest.mock import patch

from character import get_character_name


class TestGetCharacterName(TestCase):
    @patch('builtins.input', side_effect=["chris"])
    def test_get_character_name_no_spaces(self, mock_input):
        actual = get_character_name()
        expected = 'chris'
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["Lord of Python Christopher Thompson"])
    def test_get_character_name_with_spaces(self, mock_input):
        actual = get_character_name()
        expected = 'Lord of Python Christopher Thompson'
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=[""])
    def test_get_character_name_empty_string(self, mock_input):
        actual = get_character_name()
        expected = ''
        self.assertEqual(expected, actual)


