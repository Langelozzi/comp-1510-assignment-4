from unittest import TestCase
from character import leveled_up


class TestLeveledUp(TestCase):
    def test_leveled_up_xp_sixty_one_and_level_three(self):
        character_test = {"xp": 61, "level": 3}
        actual = leveled_up(character_test)
        expected = False
        self.assertFalse(expected, actual)

    def test_leveled_up_xp_sixty_and_level_three(self):
        character_test = {"xp": 60, "level": 3}
        actual = leveled_up(character_test)
        expected = False
        self.assertFalse(expected, actual)

    def test_leveled_up_xp_sixty_one_and_level_two(self):
        character_test = {"xp": 61, "level": 2}
        actual = leveled_up(character_test)
        expected = False
        self.assertFalse(expected, actual)

    def test_leveled_up_xp_fiftynine_and_level_two(self):
        character_test = {"xp": 59, "level": 2}
        actual = leveled_up(character_test)
        expected = True
        self.assertTrue(expected, actual)
