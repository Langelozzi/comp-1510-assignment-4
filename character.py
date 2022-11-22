

def make_character(name: str) -> dict:
    return {
        "name": name,
        "position": (1, 0),
        "hp": 100,
        "energy": 100,
        "level": 1,
        "abilities": {
            "fireball": 1,
            "heal": 1,
        },
        "inventory": ["map"]
    }


def move_character():
    pass


def is_alive(character: dict) -> bool:
    if character["hp"] <= 0:
        return False
    else:
        return True

