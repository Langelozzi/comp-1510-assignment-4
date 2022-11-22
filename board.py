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
from printing import print_in_color


def test_challenge():
    print("this is a test challenge")


def make_board(rows, columns) -> dict:
    board = {
        (1, 0): {
            "description": "This is where you start lol",
            "action": test_challenge,
            "solved": False,
            "north": (1, 1),
            "east": None,
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

    # a list of tuples where tuple[0] = description of tile, tuple[1] = challenge for that tile as a function

    # for x in range(1, columns + 1):
    #     for y in range(1, rows + 1):
    #         board[(x, y)] = {
    #             "description": # function from challenge.py,
    #             "action": # function from challenge.py,
    #             "solved": False,
    #             "north": (x, y+1),
    #             "east": (x+1, y),
    #             "south": (x, y-1),
    #             "west": (x-1, y)
    #         }
    #
    #         if x == 1:
    #             board[(x, y)]["west"] = None
    #         if x == 10:
    #             board[(x, y)]["east"] = None
    #         if y == 1 and x != 1:
    #             board[(x, y)]["south"] = None
    #         if y == 10 and x != 10:
    #             board[(x, y)]["north"] = None

    return board


def describe_current_location(board: dict, current_position: tuple) -> None:
    print_in_color(board[current_position]["description"], "cyan")


def is_valid_move(direction: str, board: dict, current_position: tuple) -> bool:
    if board[current_position][direction] is None:
        return False
    else:
        return True


def main():
    rows = 10
    columns = 10

    board = make_board(rows, columns)
    describe_current_location(board, (1, 0))


if __name__ == '__main__':
    main()
