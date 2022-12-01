from unittest import TestCase
from character import move_character


class TestMoveCharacter(TestCase):

    def test_move_character_north(self):
        board_test = {
            (0, 0): {
                "directions": {
                    "north": (0, 1),
                    "east": (1, 0),
                    "south": None,
                    "west": None
                }
            }
        }

        character_test = {"position": (0, 0)}

        move_character("north", board_test, character_test)
        actual = character_test["position"]
        expected = (0, 1)
        self.assertEqual(expected, actual)

    def test_move_character_east(self):
        board_test = {
            (0, 0): {
                "directions": {
                    "north": (0, 1),
                    "east": (1, 0),
                    "south": None,
                    "west": None
                }
            }
        }

        character_test = {"position": (0, 0)}

        move_character("east", board_test, character_test)
        actual = character_test["position"]
        expected = (1, 0)
        self.assertEqual(expected, actual)

    def test_move_character_south(self):
        board_test = {
            (10, 10): {
                "directions": {
                    "north": None,
                    "east": None,
                    "south": (10, 9),
                    "west": (9, 10)
                }
            }
        }

        character_test = {"position": (10, 10)}

        move_character("south", board_test, character_test)
        actual = character_test["position"]
        expected = (10, 9)
        self.assertEqual(expected, actual)

    def test_move_character_west(self):
        board_test = {
            (10, 10): {
                "directions": {
                    "north": None,
                    "east": None,
                    "south": (10, 9),
                    "west": (9, 10)
                }
            }
        }

        character_test = {"position": (10, 10)}

        move_character("west", board_test, character_test)
        actual = character_test["position"]
        expected = (9, 10)
        self.assertEqual(expected, actual)