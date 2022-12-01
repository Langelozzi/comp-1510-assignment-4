from unittest import TestCase
from character import make_character


class TestMakeCharacter(TestCase):
    def test_make_character_empty_string(self):
        actual = make_character("")
        expected = {'name': '', 'position': (1, 1), 'max_hp': 100, 'current_hp': 100, 'xp': 0, 'damage': 20, 'level': 1,
                    'abilities': ['Fireball'], 'staff': None, 'armour': None}
        self.assertEqual(expected, actual)

    def test_make_character_alphabetical(self):
        actual = make_character("Chris")
        expected = {'name': 'Chris', 'position': (1, 1), 'max_hp': 100, 'current_hp': 100, 'xp': 0, 'damage': 20,
                    'level': 1, 'abilities': ['Fireball'], 'staff': None, 'armour': None}
        self.assertEqual(expected, actual)

    def test_make_character_numerical(self):
        actual = make_character("1234")
        expected = {'name': '1234', 'position': (1, 1), 'max_hp': 100, 'current_hp': 100, 'xp': 0, 'damage': 20,
                    'level': 1, 'abilities': ['Fireball'], 'staff': None, 'armour': None}
        self.assertEqual(expected, actual)

    def test_make_character_alphanumerical(self):
        actual = make_character("N3p7un3")
        expected = {'name': 'N3p7un3', 'position': (1, 1), 'max_hp': 100, 'current_hp': 100, 'xp': 0, 'damage': 20,
                    'level': 1, 'abilities': ['Fireball'], 'staff': None, 'armour': None}
        self.assertEqual(expected, actual)
