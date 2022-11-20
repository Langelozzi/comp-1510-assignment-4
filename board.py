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
import random


def some_func():
    print("Complete the challenge")


def make_board(rows, columns) -> dict:
    board = {
        (1, 0): {
            "description": "This is where you start lol",
            "challenge": some_func,
            "solved": False,
            "north": (1, 1),
            "east": None,
            "south": None,
            "west": None
        },
        (10, 11): {
            "description": "This is how you get to the boss fight",
            "solved": False,
            "north": None,
            "east": None,
            "south": (10, 10),
            "west": None
        }
    }

    # a list of tuples where tuple[0] = description of tile, tuple[1] = challenge for that tile as a function
    tile_details = [("desc1", some_func), ("desc2", some_func), ("desc3", some_func)]

    for x in range(1, columns + 1):
        for y in range(1, rows + 1):
            desc, challenge = random.choice(tile_details)

            board[(x, y)] = {
                "description": desc,
                "challenge": challenge,
                "solved": False,
                "north": (x, y+1),
                "east": (x+1, y),
                "south": (x, y-1),
                "west": (x-1, y)
            }

            if x == 1:
                board[(x, y)]["west"] = None
            if x == 10:
                board[(x, y)]["east"] = None
            if y == 1 and x != 1:
                board[(x, y)]["south"] = None
            if y == 10 and x != 10:
                board[(x, y)]["north"] = None

    return board


def main():
    rows = 10
    columns = 10

    board = make_board(rows, columns)
    print(board[(5, 5)])
    print(board[(5, 5)]["description"])
    board[(5, 5)]["challenge"]()


if __name__ == '__main__':
    main()
