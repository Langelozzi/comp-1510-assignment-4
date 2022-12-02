"""
Contains functions related to the creation and state of the game board.
"""
import itertools

from helpers import print_in_color
from actions import get_generic_actions, get_generic_room_description, \
    royal_mage_angelozzi, lord_commander_ymir, god_king_thompson


def make_board(rows, columns) -> dict:
    """
    Generate coordinate for all actions, room descriptions and determines

    :param rows: a positive integer
    :param columns: a positive integer
    :precondition: rows must be a positive non-zero integer
    :precondition: columns must be a positive non-zero integer
    :postcondition: return a dictionary called board that contain game relevant information
                    for every tile in the game
    :return: a dictionary called board that contain game relevant information for every tile in the game
    """
    board = {
        (1, 1): {
            "description": "\nLooks like you have come back to the start, try the opposite direction of the cell",
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
            "description": "\nRoyal Mage Angelozzi, Left Wing of Alyndelle",
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
            "description": "\nLord-Commander Ymir, Right Wing of Alyndelle",
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
            "description": "\nGod-King Thompson, the God Slayer",
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
    """
    Print a game board indicating the map border, uncleared rooms, sub-bosses and a final boss.
    
    The size is determined by the parameter that is passed through this function.

    The board dictionary is not modified during execution.

    :param board: a dictionary in the form of our game board with at least the key "solved"
    :param rows: a positive integer
    :param columns: a positive integer
    :param coords: a tuple of positive non-zero integers
    :param boss_1_coords: a tuple of positive non-zero integers which is determined in the main game function
    :param boss_2_coords: a tuple of positive non-zero integers which is determined in the main game function
    :precondition: board must be a dictionary in the form of our game board with at least the key "solved"
    :precondition: rows must be a positive non-zero integer
    :precondition: columns must be a positive non-zero integer
    :precondition: coords must be a tuple of positive non-zero integers
    :precondition: boss_1_coords must be a tuple of positive non-zero integers
    :precondition: boss_2_coords must be a tuple of positive non-zero integers
    :postcondition: print a game board indicating the map border, uncleared rooms, sub-bosses and a final boss
    """
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
                print_in_color("X", "red", end="")
                print_in_color('|', "green", end="")

            elif (y_coord == final_boss_y) and (x_coord == final_boss_x):
                print_in_color('|', "green", end="")
                print_in_color("\U0001F451", "red", end="")
                print_in_color('|', "green", end="")

            elif (y_coord == 11 and x_coord != 10) or (y_coord == 0 and x_coord != 1):
                print_in_color('---', "green", end="")

            else:
                print_in_color('|?|', "green", end="")

        print()


def describe_current_location(board: dict, character: dict) -> None:
    """
    Print the description of the room that the player is currently in.

    :param board: a dictionary in the form of our game board
    :param character: a dictionary in the form of our game character with at least the key "position"
    :precondition: board must be a dictionary in the form of our game board
    :precondition: character must be a dictionary in the form of our game character with at least the key "position"
    :postcondition: prints the content of the key "description" from board dictionary
    :postcondition: parameters passed through this function will remain unchanged
    """
    current_position = character["position"]
    print_in_color(board[current_position]["description"], "cyan")


def is_valid_move(direction: str, board: dict, character: dict) -> bool:
    """
    Determine if the user input for player movement is valid.

    :param direction: one of the following strings in lowercase: "north", "east", "south", "west"
    :param board: a dictionary in the form of our game board with all proper keys
    :param character: a dictionary in the form of our game character with at least the key "position"
    :precondition: board must be a dictionary in the form of our game
    :precondition: direction must be the following strings in lowercase: "north", "east", "south", "west"
    :precondition: character must be a dictionary in the form of our game character with at least the key "position"
    :postcondition: return True if an x or y coordinates of a next move exists; else False
    :postcondition: parameters passed through this function will remain unchanged
    :return: True if an x or y coordinates of a next move exists; else False if the next coordinate has
             None value
    """
    current_position = character["position"]
    try:
        if board[current_position]["directions"][direction] is not None:
            return True
    except KeyError:
        return False
    else:
        return False


def boss_defeated(board: dict) -> bool:
    """
    Determine if the final boss is defeated.

    Read through a dictionary of a module to determine if the final boss is defeated.
    Return True if it is; else False.

    :param board: a dictionary in the form of our game board with all proper keys
    :precondition: board must be a dictionary in the form of our game board with
                   at least the key "solved"
    :postcondition: return True if a value tied to the 'solved' key in board is
                    True; else False
    :postcondition: board is unchanged
    :return: True if a value tied to the 'solved' key in board[(10,11)] is True; else False

    >>> test_board = { (10, 11): {"description": "God-King Thompson, the God Slayer", "action": god_king_thompson(), "solved": False, "directions": {"north": None, "east": None, "south": (10, 10), "west": None} } }
    >>> boss_defeated(test_board)
    False
    """
    return True if board[(10, 11)]['solved'] else False


def main():
    """
    Drive the Program.
    """
    print("You are attempting to execute the board.py module.")
    print("Executing this module does not do anything.")


if __name__ == '__main__':
    main()
