import os


def print_in_color(value, color: str, end: str = "\n") -> None:
    """
    Print value to stdout in a specific color with a specific ending.

    :param value: a python object of any type that will be printed to stdout
    :param color: the name of the color you want to print in, as one of the following strings: "purple", "blue",
    "cyan", "green", "yellow", "red"
    :param end: a string representing the last characters to be printed. Default value is "\n".
    :precondition: value must be a python object of any type
    :precondition: color must be one of the following strings: "purple", "blue", "cyan", "green", "yellow", "red"
    :precondition: end must be a string
    :postcondition: prints value to stdout in the color specified with the ending specified

    >>> print_in_color("Hello World", "blue")
    \033[94mHello World\033[0m
    """
    colors = {
        "purple": '\033[95m',
        "blue": '\033[94m',
        "cyan": '\033[96m',
        "green": '\033[92m',
        "yellow": '\033[93m',
        "red": '\033[91m',
        "end_color": '\033[0m',
    }

    print(colors[color.lower()] + str(value) + colors["end_color"], end=end)


def print_board(rows, columns, coords: tuple):
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


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
