from unittest import TestCase
from character import is_alive


class TestIsAlive(TestCase):

    def test_is_alive_positive_hp(self):
        actual = is_alive({"current_hp": 1})
        expected = True
        self.assertTrue(expected, actual)

    def test_is_alive_zero_hp(self):
        actual = is_alive({"current_hp": 0})
        expected = False
        self.assertFalse(expected, actual)

    def test_is_alive_negative_hp(self):
        actual = is_alive({"current_hp": -1})
        expected = False
        self.assertFalse(expected, actual)
