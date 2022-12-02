"""
Functions to assist in the creation of the game.
"""


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


def print_user_options(options: list, option_title: str) -> None:
    """
    Print an enumerated and formatted list of options to stdout.

    The original options list does not get modified during execution.

    :param options: a list of enumerated options
    :param option_title: a string that will be the title of the printed options
    :precondition: options must be an enumerated list of options
    :precondition: option_title must be a string
    :postcondition: prints an enumerated and formatted list of options to stdout
    """
    print_in_color("\n{:<15}{}".format("Command", option_title), "blue")

    for number, option in options:
        print(f"{number:<15}{option}")


def get_user_choice(options: list, numeric: bool = False) -> str:
    """
    Return the user's selection of options.

    The original options list does not get modified during execution.

    :param options: a list of enumerated options
    :param numeric: a boolean representing if the returned string should be the command or the option. Default is False.
    :precondition: options must be an enumerated list of options
    :precondition: numeric must be a boolean. Default is False.
    :postcondition: returns the user's selected option or number as a string
    :return: the user's selected option or number as a string
    """
    options = list(map(convert_first_index_to_str, options))

    commands = [command for command, option in options]

    print_in_color(f"\nPlease choose an option:", "purple")

    user_choice = cleanse(input())
    while user_choice not in commands:
        print_in_color("That is not a valid choice. Take a closer look and try again.", "red")
        print_in_color(f"\nPlease choose an option?", "purple")
        user_choice = cleanse(input())

    # will return a string version of the numeric command
    if numeric:
        return user_choice

    return [option for number, option in options if number == user_choice][0]


def main() -> None:
    """
    Drive the program.
    """
    print("You are attempting to execute the helpers.py module.")
    print("Executing this module does not do anything.")


if __name__ == "__main__":
    main()
