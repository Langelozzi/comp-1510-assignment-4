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
from helpers import print_in_color


def test_challenge():
    print("this is a test challenge")


def make_board(rows, columns) -> dict:
    board = {
        (1, 1): {
            "north": (1, 2),
            "east": (2, 1),
            "south": None,
            "west": None
        },
        (10, 11): {
            "description": "This is how you get to the boss fight",
            "action": test_challenge,
            "solved": False,
            "north": None,
            "east": None,
            "south": (10, 10),
            "west": None
        }
    }

    for x in range(1, columns + 1):
        for y in range(1, rows + 1):
            board[(x, y)] = {
                "description": "This is a generic spot",  # function from challenge.py
                "action": test_challenge,  # function from challenge.py
                "solved": False,
                "north": (x, y+1),
                "east": (x+1, y),
                "south": (x, y-1),
                "west": (x-1, y)
            }
            if x == 1 and y == 1:
                continue
            if x == 1:
                board[(x, y)]["west"] = None
            if x == 10:
                board[(x, y)]["east"] = None
            if y == 1 and x != 1:
                board[(x, y)]["south"] = None
            if y == 10 and x != 10:
                board[(x, y)]["north"] = None

    return board


def print_board(rows, columns, coords: tuple):
    x_pos, y_pos = coords

    for y_coord in range(columns + 1, -1, -1):
        for x_coord in range(1, rows + 1, 1):
            if (y_coord == 11 and x_coord != 10) or (y_coord == 0 and x_coord != 1):
                print_in_color('---', "green", end="")
            elif y_coord == y_pos and x_coord == x_pos:
                print_in_color('|', "green", end="")
                print_in_color("#", "purple", end="")
                print_in_color('|', "green", end="")
            else:
                print_in_color('| |', "green", end="")

        print()


def describe_current_location(board: dict, character: dict) -> None:
    current_position = character["position"]
    print_in_color(board[current_position]["description"], "cyan")


def is_valid_move(direction: str, board: dict, character: dict) -> bool:
    current_position = character["position"]
    if board[current_position][direction] is None:
        return False
    else:
        return True


def main():
    rows = 10
    columns = 10

    board = make_board(rows, columns)


if __name__ == '__main__':
    main()
