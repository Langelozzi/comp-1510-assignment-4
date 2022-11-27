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
        "sword": None,
        "shield": None,
        "talisman": None
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


def main() -> None:
    test_character = make_character("Test")
    print_abilities(test_character)
    print(select_ability(test_character))


if __name__ == "__main__":
    main()
