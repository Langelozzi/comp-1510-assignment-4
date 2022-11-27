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
    print('+------------------------------------------------------------------+')
    print('|', end="")
    print_in_color('{:^66}'.format(character["name"]), "red", end="")
    print('|')
    print('+------------------------------------------------------------------+')

    print('{:<12}'.format("|"), end="")
    print_in_color('{:<20}'.format("Current Coordinates"), "blue", end="")
    print('{:<35}'.format(f": {character['position']}"), end="")
    print('|')

    print('{:<12}'.format("|"), end="")
    print_in_color('{:<20}'.format("Level"), "blue", end="")
    print('{:<35}'.format(f": {character['level']}"), end="")
    print('|')

    print('{:<12}'.format("|"), end="")
    print_in_color('{:<20}'.format("HP"), "blue", end="")
    print('{:<35}'.format(f": {character['current_hp']}/{character['max_hp']}"), end="")
    print('|')

    print('{:<12}'.format("|"), end="")
    print_in_color('{:<20}'.format("XP"), "blue", end="")
    print('{:<35}'.format(f": {character['xp']}/100"), end="")
    print('|')

    print('{:<12}'.format("|"), end="")
    print_in_color('{:<20}'.format("Sword"), "blue", end="")
    print('{:<35}'.format(f": {character['sword']}"), end="")
    print('|')

    print('{:<12}'.format("|"), end="")
    print_in_color('{:<20}'.format("Shield"), "blue", end="")
    print('{:<35}'.format(f": {character['shield']}"), end="")
    print('|')

    print('{:<12}'.format("|"), end="")
    print_in_color('{:<20}'.format("Talisman"), "blue", end="")
    try:
        print('{}'.format(f": {character['talisman']['name']} ("), end="")
        print_in_color(f"{'*' * character['talisman']['rarity']}", "yellow", end="")
        print("{:<17}".format(")"), end="")
    except TypeError:
        print('{:<35}'.format(f": {character['talisman']}"), end="")
    print('|')


def main() -> None:
    test_character = make_character("Sir charles")
    # print_abilities(test_character)
    # print(select_ability(test_character))
    show_stats(test_character)


if __name__ == "__main__":
    main()
