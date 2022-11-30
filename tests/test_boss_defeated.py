from unittest import TestCase

from board import boss_defeated


class TestBossDefeated(TestCase):
    def test_boss_defeated(self):
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

        self.assertTrue(boss_defeated(board))

    def test_boss_not_defeated(self):
        board = {
            (10, 11): {
                "description": "God-King Thompson, the God Slayer",
                "action": None,
                "solved": False,
                "directions": {
                    "north": None,
                    "east": None,
                    "south": (10, 10),
                    "west": None
                }
            }
        }

        self.assertFalse(boss_defeated(board))
