from helpers import print_in_color, cleanse


def get_character_name() -> str:
    print_in_color("Please enter a name for your character..", "purple")
    return input()


def make_character(name: str) -> dict:
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


def move_character(direction: str, board: dict, character: dict) -> None:
    current_room = board[character["position"]]
    character["position"] = current_room["directions"][direction]


def is_alive(character: dict) -> bool:
    if character["current_hp"] <= 0:
        return False
    else:
        return True


def print_abilities(character: dict) -> None:
    print_in_color("{:<15}Ability".format("Command"), "blue")
    ability_options = list(enumerate(character["abilities"], start=1))

    for number, ability in ability_options:
        print(f"{number:<15}{ability}")


def select_ability(character: dict) -> tuple:
    ability_options = list(enumerate(character["abilities"], start=1))

    print_in_color("\nWhich ability would you like to use?", "purple")

    user_choice = cleanse(input())
    while (not user_choice.isnumeric()) or (int(user_choice) not in list(range(1, len(ability_options) + 1))):
        print_in_color("\nThat wasn't one of the options! Take a closer look and try again.", "red")
        print_in_color("Which ability would you like to use?", "purple")
        user_choice = cleanse(input())

    return [ability for number, ability in ability_options if number == int(user_choice)][0]


def show_stats(character: dict) -> None:
    print('+----------------------------------------------------------------------------------+')
    print('|', end="")
    print_in_color('{:^82}'.format(character["name"]), "red", end="")
    print('|')
    print('+----------------------------------------------------------------------------------+')

    general_stats = (
        ("Current Coordinates", character['position']),
        ("Level", character['level']),
        ("HP", f"{character['current_hp']}/{character['max_hp']}"),
        ("XP (to next level)", f"{character['xp']}/100"),
        ("Ability Power", character['damage'])
    )
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
    test_character = make_character("Sir charles")
    # print_abilities(test_character)
    # print(select_ability(test_character))
    show_stats(test_character)


if __name__ == "__main__":
    main()
