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


def cleanse(text: str) -> str:
    """
    Convert text to lower case and strip whitespace from both sides.

    The original string is not modified as string are immutable, instead a new string is created and returned.

    :param text: a string
    :precondition: text must be a string
    :postcondition: returns text converted to lowercase and stripped of whitespace on both sides, as a new string
    :return: text converted to lowercase and stripped of whitespace on both sides, as a new string

    >>> cleanse("  ApPle     \t")
    'apple'
    >>> cleanse(' RUN AWAY NOW  ')
    'run away now'
    """
    return text.lower().strip()


def convert_first_index_to_str(iterable: tuple) -> tuple:
    """
    Convert the first index of a tuple to a string.

    The original tuple is not modified, a new tuple is created and returned.

    :param iterable: a tuple of length greater than 1
    :precondition: iterable must be a tuple of length greater than 1
    :postcondition: returns a new tuple with the first index of iterable converted to a string
    :return: a new tuple with the first index of iterable converted to a string

    >>> convert_first_index_to_str((1, "abc"))
    ('1', 'abc')
    >>> convert_first_index_to_str((1, 2, 3, 4, 5, 6))
    ('1', 2, 3, 4, 5, 6)
    >>> convert_first_index_to_str((['a', 1, True], [2, 'b', False]))
    ("['a', 1, True]", [2, 'b', False])
    """
    new_iterable = [element for element in iterable]
    new_iterable[0] = str(new_iterable[0])

    return tuple(new_iterable)


def get_user_choice(board: dict, character: dict) -> str:
    """
    Print possible choices and return the user's selected choice.

    The board and character dictionaries are not modified.

    :param board: a dictionary in the form of our game board with all proper keys
    :param character: a dictionary in the form of our game character with at least keys "position" and "name"
    :precondition: board must be a dictionary in the form of our game board
    :precondition: character must be a dictionary in the form of our game character with at least keys "position" and
    "name"
    :postcondition: prints the possible choices and returns the user selected choice as a string
    :return: the user selected choice as a string
    """
    current_room = board[character["position"]]
    possible_directions = [direction for direction, coord in current_room["directions"].items() if coord is not None]

    options = [('q', "quit"), ('s', "show stats")]
    options += list(enumerate(possible_directions, start=1))

    options = list(map(convert_first_index_to_str, options))
    commands = [command for command, option in options]

    print_in_color("\n{:<15}Option".format("Command"), "blue")

    for number, direction in options:
        print(f"{number:<15}{direction}")

    print_in_color(f"\n{character['name']}, which direction would you like to advance in?", "purple")

    user_choice = cleanse(input())
    while user_choice not in commands:
        print_in_color("That is not a valid choice, try again.", "red")
        print_in_color(f"\n{character['name']}, which direction would you like to advance in?", "purple")
        user_choice = cleanse(input())

    return [direction for number, direction in options if number == user_choice][0]
