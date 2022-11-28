"""
---------------------------| |
| || || || || || || || || || |
| || || || || || || || || || |
| || || || || || || || || || |
| || || || || || || || || || |
| || || || || || || || || || |
| || || || || || || || || || |
| || || || || || || || || || |
| || || || || || || || || || |
| || || || || || || || || || |
| || || || || || || || || || |
| |---------------------------
"""
import itertools

from helpers import print_in_color
from actions import get_generic_actions, get_generic_room_description, \
    royal_mage_angelozzi, lord_commander_ymir, god_king_thompson


def test_challenge():
    print("this is a test challenge")


def make_board(rows, columns) -> dict:
    board = {
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
        },
        (4, 4): {
            "description": "Royal Mage Angelozzi, Left Wing of Alyndelle",
            "action": royal_mage_angelozzi(),
            "solved": False,
            "directions": {
                "north": (4, 5),
                "east": (5, 4),
                "south": (4, 3),
                "west": (3, 4)
            }
        },
        (7, 7): {
            "description": "Lord-Commander Ymir, Right Wing of Alyndelle",
            "action": lord_commander_ymir(),
            "solved": False,
            "directions": {
                "north": (7, 8),
                "east": (8, 7),
                "south": (7, 6),
                "west": (6, 7)
            }
        },
        (10, 11): {
            "description": "God-King Thompson, the God Slayer",
            "action": god_king_thompson(),
            "solved": False,
            "directions": {
                "north": None,
                "east": None,
                "south": (10, 10),
                "west": None
            }
        }
    }

    actions = itertools.cycle(get_generic_actions())

    for x_coord in range(1, columns + 1):
        for y_coord in range(1, rows + 1):
            if (x_coord == 1 and y_coord == 1) or \
                    (x_coord == 10 and y_coord == 11) or \
                    (x_coord == 4 and y_coord == 4) or \
                    (x_coord == 7 and y_coord == 7):
                continue

            board[(x_coord, y_coord)] = {
                "description": get_generic_room_description(),
                "action": next(actions),
                "solved": False,
                "directions": {
                    "north": (x_coord, y_coord + 1),
                    "east": (x_coord + 1, y_coord),
                    "south": (x_coord, y_coord - 1),
                    "west": (x_coord - 1, y_coord)
                }
            }

            if x_coord == 1:
                board[(x_coord, y_coord)]["directions"]["west"] = None
            if x_coord == rows:
                board[(x_coord, y_coord)]["directions"]["east"] = None
            if y_coord == 1 and x_coord != 1:
                board[(x_coord, y_coord)]["directions"]["south"] = None
            if y_coord == columns and x_coord != rows:
                board[(x_coord, y_coord)]["directions"]["north"] = None

    return board


def print_board(board: dict, rows: int, columns: int, coords: tuple, boss_1_coords: tuple, boss_2_coords: tuple):
    x_pos, y_pos = coords
    boss_1_x, boss_1_y = boss_1_coords
    boss_2_x, boss_2_y = boss_2_coords
    final_boss_x, final_boss_y = (10, 11)

    print()
    for y_coord in range(columns + 1, -1, -1):
        for x_coord in range(1, rows + 1, 1):
            if y_coord == y_pos and x_coord == x_pos:
                print_in_color('|', "green", end="")
                print_in_color("#", "purple", end="")
                print_in_color('|', "green", end="")

            elif (y_coord == 0 and x_coord == 1) or ((x_coord, y_coord) in board.keys()) and \
                    (board[(x_coord, y_coord)]["solved"]):
                print_in_color('| |', "green", end="")

            elif (y_coord == boss_1_y and x_coord == boss_1_x) or (y_coord == boss_2_y and x_coord == boss_2_x):
                print_in_color('|', "green", end="")
                print_in_color("%", "red", end="")
                print_in_color('|', "green", end="")

            elif (y_coord == final_boss_y) and (x_coord == final_boss_x):
                print_in_color('|', "green", end="")
                print_in_color("&", "red", end="")
                print_in_color('|', "green", end="")

            elif (y_coord == 11 and x_coord != 10) or (y_coord == 0 and x_coord != 1):
                print_in_color('---', "green", end="")

            else:
                print_in_color('|?|', "green", end="")

        print()


def describe_current_location(board: dict, character: dict) -> None:
    current_position = character["position"]
    print_in_color(board[current_position]["description"], "cyan")


def is_valid_move(direction: str, board: dict, character: dict) -> bool:
    current_position = character["position"]
    try:
        if board[current_position]["directions"][direction] is not None:
            return True
    except KeyError:
        return False
    else:
        return False


def boss_defeated(board: dict) -> bool:
    return True if board[(10, 11)]['solved'] else False


def main():
    rows = 10
    columns = 10

    board = make_board(rows, columns)


if __name__ == '__main__':
    main()
