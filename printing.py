def print_in_color(value, color: str, end: str = "\n"):
    colors = {
        "purple": '\033[95m',
        "blue": '\033[94m',
        "cyan": '\033[96m',
        "green": '\033[92m',
        "yellow": '\033[93m',
        "red": '\033[91m',
        "end_color": '\033[0m',
    }

    print(colors[color] + str(value) + colors["end_color"], end=end)


def print_board(x_coord, y_coord):
    #board = """
    # ---------------------------| |
    # | || || || || || || || || || |
    # | || || || || || || || || || |
    # | || || || || || || || || || |
    # | || || || || || || || || || |
    # | || || || || || || || || || |
    # | || || || || || || || || || |
    # | || || || || || || || || || |
    # | || || || || || || || || || |
    # | || || || || || || || || || |
    # | || || || || || || || || || |
    # | |---------------------------
    # """

    for y in range(11, -1, -1):
        for x in range(1, 11, 1):
            if (y == 11 and x != 10) or (y == 0 and x != 1):
                print('---', end="")
            elif y == y_coord and x == x_coord:
                print('|', end="")
                print_in_color("#", "purple", end="")
                print('|', end="")
            else:
                print('| |', end="")

        print()


print_board(1, 1)
