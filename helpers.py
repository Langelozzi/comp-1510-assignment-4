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


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def cleanse(text: str) -> str:
    return text.lower().strip()


def get_user_choice() -> str:
    print_in_color("Which direction wouldst thee liketh to traverse?", "purple")
    return cleanse(input())
