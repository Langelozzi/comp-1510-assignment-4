from unittest import TestCase

from board import is_valid_move
from character import make_character


class TestIsValidMove(TestCase):
    def setUp(self) -> None:
        self.board = {
            (1, 1): {
                "description": "Looks like you have come back to the start, try the opposite direction of the cell",
                "action": None,
                "solved": True,
                "directions": {
                    "north": (1, 2),
                    "east": (2, 1),
                    "south": None,
                    "west": None
                }
            }
        }

    def test_valid_move(self):
        character = make_character("Test Character")
        character['position'] = (1, 1)

        valid_move = 'north'

        self.assertTrue(is_valid_move(valid_move, self.board, character))

    def test_invalid_move(self):
        character = make_character("Test Character")
        character['position'] = (1, 1)

        invalid_move = 'west'

        self.assertFalse(is_valid_move(invalid_move, self.board, character))
