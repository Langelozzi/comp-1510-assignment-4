from unittest import TestCase
from character import move_character


class TestMoveCharacter(TestCase):
    board = {
        (10, 11): {
            "description": "God-King Thompson, the God Slayer",
            "action": None,
            "solved": True,
            "directions": {
                "north": None,
                "east": None,
                "south": (10, 10),
                "west": None
            }
        }
    }

    character_test = {"position": (1, 1)}

    def test_move_character_north(self):

        actual = move_character('north')
        expected = 
        self.fail()
