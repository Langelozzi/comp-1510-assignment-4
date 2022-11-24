from helpers import print_in_color, cleanse


def get_character_name() -> str:
    print_in_color("Please enter a name for your character..", "purple")
    return input()


def make_character(name: str) -> dict:
    return {
        "name": name,
        "position": (1, 1),
        "hp": 100,
        "xp": 0,
        "energy": 100,
        "level": 1,
        "abilities": {
            "fireball": 1,
            "heal": 1,
        },
        "inventory": ["map"]
    }


def move_character(direction: str, board: dict, character: dict) -> None:
    current_room = board[character["position"]]
    character["position"] = current_room["directions"][direction]


def is_alive(character: dict) -> bool:
    if character["hp"] <= 0:
        return False
    else:
        return True


def use_ability(character: dict) -> str:
    print_in_color("{:<15}{:<15}Level".format("Command", "Ability"), "blue")
    ability_options = list(enumerate(character["abilities"].items(), start=1))

    for number, ability in ability_options:
        ability_description, ability_level = ability

        print(f"{number:<15}{ability_description:<15}{ability_level}")

    print_in_color("\nWhich ability would you like to use?", "purple")

    user_choice = cleanse(input())

    return [ability for number, ability in ability_options if number == int(user_choice)][0]


def main() -> None:
    test_character = make_character("Test")
    use_ability(test_character)


if __name__ == "__main__":
    main()
