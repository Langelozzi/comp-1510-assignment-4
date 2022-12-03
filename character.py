"""
Contains functions related to the game characters attributes and state.
"""

from helpers import print_in_color, print_user_options, get_user_choice


def get_character_name() -> str:
    """
    Return the input from the user.

    :postcondition: returns the string value of what the user entered into stdin
    :return: the input from the user, as a string
    """
    print_in_color("Please enter a name for your character..", "purple")
    return input()


def make_character(name: str) -> dict:
    """
    Generate and return a dictionary representing a game character.

    :param name: the name of the character, as a string
    :precondition: name must be a string
    :postcondition: returns a newly created character dictionary with the proper name
    :return: a newly created character dictionary with the proper name

    >>> make_character("Chris")
    {'name': 'Chris', 'position': (1, 1), 'max_hp': 100, 'current_hp': 100, 'xp': 0, 'damage': 20, 'level': 1, 'abilities': ['Fireball'], 'staff': None, 'armour': None}
    >>> make_character("N3p7un3")
    {'name': 'N3p7un3', 'position': (1, 1), 'max_hp': 100, 'current_hp': 100, 'xp': 0, 'damage': 20, 'level': 1, 'abilities': ['Fireball'], 'staff': None, 'armour': None}
    """
    return {
        "name": name,
        "position": (1, 1),
        "max_hp": 100,
        "current_hp": 100,
        "xp": 0,
        "damage": 20,
        "level": 1,
        "abilities": ["Fireball"],
        "staff": None,
        "armour": None
    }


def choose_direction(board: dict, character: dict) -> str:
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

    print_user_options(options, "Option")

    return get_user_choice(options)


def move_character(direction: str, board: dict, character: dict) -> None:
    """
    Modify the character coordinates accordingly based on the direction. Original character is modified, board is not.

    :param direction: one of the following strings in lowercase: "north", "east", "south", "west"
    :param board: a dictionary in the form of our game board with all proper keys
    :param character: a dictionary in the form of our game character with at least the key "position"
    :precondition: direction must be one of the following strings in lowercase: "north", "east", "south", "west"
    :precondition: board must be a dictionary in the form of our game board
    :precondition: character must be a dictionary in the form of our game character with at least the key "position"
    :postcondition: changes the character position according to the direction they moved
    """
    current_room = board[character["position"]]
    character["position"] = current_room["directions"][direction]


def is_alive(character: dict) -> bool:
    """
    Determine if the character is still alive or not. Does not modify the character dictionary.

    :param character: a character in dictionary form
    :precondition: character must be a dictionary in the form of our game character with at least the key "current_hp"
    :postcondition: Returns True if character is alive, False otherwise
    :return: True if character is alive, False otherwise

    >>> character1 = {"current_hp": 1}
    >>> is_alive(character1)
    True
    >>> character2 = {"current_hp": 0}
    >>> is_alive(character2)
    False
    """
    if character["current_hp"] <= 0:
        return False
    else:
        return True


def leveled_up(character: dict) -> bool:
    """
    Determines if the character has leveled up. Does not modify the character dictionary.

    :param character: a character in dictionary form
    :precondition: character must be a dictionary in the form of our game character with at least the keys "xp" and
    "level"
    :postcondition: returns True if the character leveled up, otherwise False
    :return: True if the character leveled up, otherwise False

    >>> character1 = {"xp": 60, "level": 2}
    >>> leveled_up(character1)
    True
    >>> character2 = {"xp": 59, "level": 2}
    >>> leveled_up(character2)
    False
    >>> character3 = {"xp": 61, "level": 3}
    >>> leveled_up(character3)
    False
    """
    return True if (character['xp'] >= 60) and (character['level'] < 3) else False


def level_up_sequence(character: dict) -> None:
    """
    Increase character level, reset xp to 0 and print ascii art. Modifies the original character dictionary.

    :param character: a character in dictionary form
    :precondition: character must be a dictionary in the form of our game character with at least the keys "xp" and
    "level"
    :postcondition: increases the character level, resets xp to 0 and prints ascii art.
    """
    character["level"] += 1
    character["xp"] = 0
    print_in_color("""
                          _                              _     _    _           _                                                             
                         | |                            | |   | |  | |         | |                                                            
                         | |        ___  __   __   ___  | |   | |  | |  _ __   | |                                                            
                         | |       / _ \ \ \ / /  / _ \ | |   | |  | | | '_ \  | |                                      
                         | |____  |  __/  \ V /  |  __/ | |   | |__| | | |_) | |_|                                      
                         |______|  \___|   \_/    \___| |_|    \____/  | .__/  (_)                                      
                                                                       | |                                                                    
                                                                       |_|                                                                    
                                     \U0001F386 Congrats you leveled up \U0001F386 	                
    """, "yellow")
    print_in_color("You feel stronger, your veins are coursing with denser magic and your mana shield has "
                   "strengthened!", "yellow")


def died(character: dict) -> None:
    """
    Resets character position to start and character level to 1 as if they just started the game.

    All items and abilities are retained. Ascii art gets printed. Modifies the original character dictionary.

    :param character: a character in dictionary form
    :precondition: character must be a dictionary in the form of our game character with at least the keys "xp",
    "level", "position" and "current_hp"
    :postcondition: Resets character position to start and character level to 1
    """
    character["position"] = (1, 1)
    character["xp"] = 0
    character["level"] = 1
    character["current_hp"] = 100

    print_in_color("""
                         __     __                    _____    _              _                                     
                         \ \   / /                   |  __ \  (_)            | |                                    
                          \ \_/ /    ___    _   _    | |  | |  _    ___    __| |                                    
                           \   /    / _ \  | | | |   | |  | | | |  / _ \  / _` |                                    
                            | |    | (_) | | |_| |   | |__| | | | |  __/ | (_| |                                    
                            |_|     \___/   \__,_|   |_____/  |_|  \___|  \__,_|                                    
                                      \U00002620 Rip, you died. Skill issue. \U00002620                                                  
    """, "red")


def show_stats(character: dict) -> None:
    """
    Print the character's statistics formatted to stdout. Does not modify the character dictionary.

    :param character: a character in dictionary form
    :precondition: character must be a dictionary in the form of our game character with all proper keys
    :postcondition: prints the character's statistics formatted to stdout
    """
    print('+----------------------------------------------------------------------------------+')
    print('|', end="")
    print_in_color('{:^82}'.format(character["name"]), "red", end="")
    print('|')
    print('+----------------------------------------------------------------------------------+')

    general_stats = [
        ("Current Coordinates", character['position']),
        ("Level", character['level']),
        ("HP", f"{round(character['current_hp'])}/{character['max_hp']}"),
    ]
    xp_stat = ("XP (to next level)", f"{round(character['xp'])}/60") if character["level"] < 3 \
        else ("XP (to next level)", "Max")
    general_stats.append(xp_stat)

    for title, stat in general_stats:
        print('{:<18}'.format("|"), end="")
        print_in_color(f"{title:<20}", "blue", end="")
        print("{:<45}".format(f": [ {stat} ]"), end="")
        print('|')

    print('+----------------------------------------------------------------------------------+')

    inventory_stats = (
        ("Staff", "staff"),
        ("Armour", "armour")
    )
    for item, key in inventory_stats:
        print('{:<18}'.format("|"), end="")
        print_in_color(f"{item:<20}", "blue", end="")
        try:
            print('{:<54}'.format(f": [ {character[key]['name']} (\033[93m{'*' * character[key]['rarity']}\033[0m) ]"),
                  end="")
        except TypeError:
            print('{:<45}'.format(f": None"), end="")
        print('|')

    print('+----------------------------------------------------------------------------------+')

    print('{:<18}'.format("|"), end="")
    print_in_color("{:<20}".format("Abilities"), "blue", end="")
    print("{:<45}".format(f": [ {character['abilities'][0]} ]"), end="")
    print('|')

    for ability in character['abilities'][1:]:
        print('{:<38}'.format("|"), end="")
        print("{:<45}".format(f"  [ {ability} ]"), end="")
        print('|')

    print('+----------------------------------------------------------------------------------+')


def main() -> None:
    """
    Drive the program.
    """
    print("You are attempting to execute the character.py module.")
    print("Executing this module does not do anything.")


if __name__ == "__main__":
    main()
