# 10 basic challenges which can be mob fights or puzzles
# 3 sub boss fights
# 1 final boss fights
import itertools

from helpers import cleanse, print_in_color
from character import make_character, print_abilities, select_ability

import random
import time
import json


def opening_dialogue() -> None:
    # intro_one = "During the Reign of Gold, the continent of Aleyndell were prosperous. The Golden Capital of  \n" \
    #             "Astera were at the pinnacle of its reign, their prowess told to match the power of gods. \n"
    #
    # intro_two = "However, power such as these often corrupts, and the God King of Aleyndelle were no different. His\n"
    #             " arrogance lead him to enslaving an angel to extract their power to truly transcend the realm of \n"
    #             "humanhood. His greed and transgression angered the Gods leading the world into the Age of Strife.\n"
    #             "The gods eventually slayed the King and as punishment, snuff out the flame of humanity, casting \n"
    #             "the humanity into darkness...\n"
    #
    # intro_three = "Someone...please defeat the God King Angelozzi and rekindle the fire of humanity.\n"
    #
    # intro_four = "▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n" \
    #              "▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n" \
    #              "▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒\n" \
    #              "▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒\n" \
    #              "▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒\n" \
    #              "▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄░░▒▒▒▒▒\n" \
    #              "▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██▌░░▒▒▒▒\n" \
    #              "▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░▄▄███▀░░░░▒▒▒\n" \
    #              "▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░█████░▄█░░░░▒▒\n" \
    #              "▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░▄████████▀░░░░▒▒\n" \
    #              "▒▒░░░░░░░░░░░░░░░░░░░░░░░░▄█████████░░░░░░░▒\n" \
    #              "▒░░░░░░░░░░░░░░░░░░░░░░░░░░▄███████▌░░░░░░░▒\n" \
    #              "▒░░░░░░░░░░░░░░░░░░░░░░░░▄█████████░░░░░░░░▒\n" \
    #              "▒░░░░░░░░░░░░░░░░░░░░░▄███████████▌░░░░░░░░▒\n" \
    #              "▒░░░░░░░░░░░░░░░▄▄▄▄██████████████▌░░░░░░░░▒\n" \
    #              "▒░░░░░░░░░░░▄▄███████████████████▌░░░░░░░░░▒\n" \
    #              "▒░░░░░░░░░▄██████████████████████▌░░░░░░░░░▒\n" \
    #              "▒░░░░░░░░████████████████████████░░░░░░░░░░▒\n" \
    #              "▒█░░░░░▐██████████▌░▀▀███████████░░░░░░░░░░▒\n" \
    #              "▐██░░░▄██████████▌░░░░░░░░░▀██▐█▌░░░░░░░░░▒▒\n" \
    #              "▒██████░█████████░░░░░░░░░░░▐█▐█▌░░░░░░░░░▒▒\n" \
    #              "▒▒▀▀▀▀░░░██████▀░░░░░░░░░░░░▐█▐█▌░░░░░░░░▒▒▒\n" \
    #              "▒▒▒▒▒░░░░▐█████▌░░░░░░░░░░░░▐█▐█▌░░░░░░░▒▒▒▒\n" \
    #              "▒▒▒▒▒▒░░░░███▀██░░░░░░░░░░░░░█░█▌░░░░░░▒▒▒▒▒\n" \
    #              "▒▒▒▒▒▒▒▒░▐██░░░██░░░░░░░░▄▄████████▄▒▒▒▒▒▒▒▒\n" \
    #              "▒▒▒▒▒▒▒▒▒██▌░░░░█▄░░░░░░▄███████████████████\n" \
    #              "▒▒▒▒▒▒▒▒▒▐██▒▒░░░██▄▄███████████████████████\n" \
    #              "▒▒▒▒▒▒▒▒▒▒▐██▒▒▄████████████████████████████\n" \
    #              "▒▒▒▒▒▒▒▒▒▒▄▄████████████████████████████████\n" \
    #              "████████████████████████████████████████████\n"

    print_in_color("...\n", "cyan")
    time.sleep(3)
    print_in_color(
        "During the Reign of Gold, the continent of Aleyndell were prosperous. The Golden Capital of  \n"
        "Astera were at the pinnacle of its reign, their prowess told to match the power of gods. \n", "cyan")
    time.sleep(3)
    print_in_color(
        "However, power such as these often corrupts, and the God King of Aleyndelle were no different. His \n"
        "arrogance lead him to enslaving an angel to extract their power to truly transcend the realm of \n"
        "humanhood. His greed and transgression angered the Gods leading the world into the Age of Strife.\n"
        "The gods eventually slayed the King and as punishment, snuff out the flame of humanity, casting \n"
        " humanity into darkness...\n", "cyan")
    time.sleep(10)
    # print_in_color(
    #     "Gods proclaimed. 'The flame \n", "cyan")
    # time.sleep(3)
    print_in_color(
        "Someone...please defeat the God King Angelozzi and rekindle the fire of humanity.\n", "cyan")
    time.sleep(3)
    print_in_color(
        "▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n"
        "▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n"
        "▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒\n"
        "▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒\n"
        "▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒\n"
        "▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄░░▒▒▒▒▒\n"
        "▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██▌░░▒▒▒▒\n"
        "▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░▄▄███▀░░░░▒▒▒\n"
        "▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░█████░▄█░░░░▒▒\n"
        "▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░▄████████▀░░░░▒▒\n"
        "▒▒░░░░░░░░░░░░░░░░░░░░░░░░▄█████████░░░░░░░▒\n"
        "▒░░░░░░░░░░░░░░░░░░░░░░░░░░▄███████▌░░░░░░░▒\n"
        "▒░░░░░░░░░░░░░░░░░░░░░░░░▄█████████░░░░░░░░▒\n"
        "▒░░░░░░░░░░░░░░░░░░░░░▄███████████▌░░░░░░░░▒\n"
        "▒░░░░░░░░░░░░░░░▄▄▄▄██████████████▌░░░░░░░░▒\n"
        "▒░░░░░░░░░░░▄▄███████████████████▌░░░░░░░░░▒\n"
        "▒░░░░░░░░░▄██████████████████████▌░░░░░░░░░▒\n"
        "▒░░░░░░░░████████████████████████░░░░░░░░░░▒\n"
        "▒█░░░░░▐██████████▌░▀▀███████████░░░░░░░░░░▒\n"
        "▐██░░░▄██████████▌░░░░░░░░░▀██▐█▌░░░░░░░░░▒▒\n"
        "▒██████░█████████░░░░░░░░░░░▐█▐█▌░░░░░░░░░▒▒\n"
        "▒▒▀▀▀▀░░░██████▀░░░░░░░░░░░░▐█▐█▌░░░░░░░░▒▒▒\n"
        "▒▒▒▒▒░░░░▐█████▌░░░░░░░░░░░░▐█▐█▌░░░░░░░▒▒▒▒\n"
        "▒▒▒▒▒▒░░░░███▀██░░░░░░░░░░░░░█░█▌░░░░░░▒▒▒▒▒\n"
        "▒▒▒▒▒▒▒▒░▐██░░░██░░░░░░░░▄▄████████▄▒▒▒▒▒▒▒▒\n"
        "▒▒▒▒▒▒▒▒▒██▌░░░░█▄░░░░░░▄███████████████████\n"
        "▒▒▒▒▒▒▒▒▒▐██▒▒░░░██▄▄███████████████████████\n"
        "▒▒▒▒▒▒▒▒▒▒▐██▒▒▄████████████████████████████\n"
        "▒▒▒▒▒▒▒▒▒▒▄▄████████████████████████████████\n"
        "████████████████████████████████████████████\n", "cyan")
    print_in_color(
        " _______  _______ _________ _______  _          _______  _______    _______ _________ _______  _______ \n"
        "(  ____ )(  ____ \\__   __/(  ____ \( (    /|  (  ___  )(  ____ \  (  ____ \\__   __/(  ____ )(  ____  \ \n"
        "| (    )|| (    \/   ) (   | (    \/|  \  ( |  | (   ) || (    \/  | (    \/   ) (   | (    )|| (    \/ \n"
        "| (____)|| (__       | |   | |      |   \ | |  | |   | || (__      | (__       | |   | (____)|| (__     \n"
        "|     __)|  __)      | |   | | ____ | (\ \) |  | |   | ||  __)     |  __)      | |   |     __)|  __)    \n"
        "| (\ (   | (         | |   | | \_  )| | \   |  | |   | || (        | (         | |   | (\ (   | (       \n"
        "| ) \ \__| (____/\___) (___| (___) || )  \  |  | (___) || )        | )      ___) (___| ) \ \__| (____/\ \n"
        "|/   \__/(_______/\_______/(_______)|/    )_)  (_______)|/         |/       \_______/|/   \__/(_______/ \n"
        , "cyan")
    time.sleep(3)


def cell_description() -> None:
    part_one = "You wake to the sound of metal against stone.\n" \
               "You lift you head from the floor and as your eyes adjust to the darkness you start to scan your " \
               "surroundings..\n"

    part_two = "You are in a small cell, metal bars straight ahead; cobblestone lines the rest of the room\n" \
               "You can feel the damp air in your breath, and hear the slow drop of water against the stone floor\n" \
               "You sense a darkness weighing in your chest and a cold breeze stroke down your spine\n" \
               "From down the hall you see a shadow as it rounds the corner east, you catch a glimpse of a metal " \
               "foot..\n"

    part_three = "The last thing you can remember is when gods descended on Alyndelle and took our flame of humanity\n" \
                 "The whole town was there..\n" \
                 "There was lightning, darkness. It blanketed the sky; low and heavy causing a sense of confusion\n" \
                 "You turn to your left to see the royal knights yelling and tearing at their heads..\n" \
                 "As they glance up you see a glow of deep red, shining from the slits of their helmets\n" \
                 "You tried to scream but fear restrained your voice,\n" \
                 "And then nothing..\n"

    part_four = "As you bring yourself back to the cell, to the present, you feel your heart beat speed up, " \
                "as the feeling of entrapment sets in.. " \
                "but not for long\n" \
                "The metal door of the cell creaks open, revealing a clear stone path to the hall where the shadow " \
                "walked\n" \
                "You lift yourself to your feet from the cobblestone floor and contemplate your options\n" \
                "The curiosity twists in your cut and pulls you north..\n" \
                "You are now following the shadowy figure north down the dungeon hall...\n"

    part_five = "As you approach the end of the hall, you feel a stronger wind against you skin\n" \
                "At the end of the hall, the room opens to a small room, arched doorways to your north and east\n" \
                "Another chill propagates along your spine, as you make your choice..\n"

    print_in_color("**CLANK**\n", "cyan")
    time.sleep(3)
    print_in_color(part_one, "cyan")
    time.sleep(8)
    print_in_color(part_two, "cyan")
    time.sleep(15)
    print_in_color(part_three, "cyan")
    time.sleep(15)
    print_in_color(part_four, "cyan")
    time.sleep(12)
    print_in_color(part_five, "cyan")
    time.sleep(8)


def spider_web_blockade(character: dict) -> None:
    print_in_color("You pause once in the room. You see that all of the archways are blocked off with layers upon \n"
                   "layers of spider webs. You need some way to clear the archways before you can proceed.", "cyan")
    print_in_color("You might be able to use one of your abilities to clear the webs!\n", "cyan")

    print_abilities(character)

    ability_used = select_ability(character)
    while ability_used[0] != "Fireball":
        print_in_color(f"I don't think {ability_used[0]} will work here, try a different one.", "red")
        ability_used = select_ability(character)

    print_in_color("Nice work! You were able to clear out all of those webs with your Fireball!", "cyan")

    character["xp"] += 12

    print_in_color(f"[{character['name']} | xp: +12]", "yellow")


def empty_room(character: dict) -> None:
    print_in_color("You stop in the center of the room. It appears empty, but you hear a voice whispering..", "cyan")
    print_in_color(f"{character['name']}, keep walking if you know what's good for you!", "cyan")
    print_in_color("You hastily make your decision..", "cyan")


def generate_enemy_battle(enemy: dict):
    def fight(character: dict) -> None:
        print_in_color(f"Both you and the {enemy['name']} step forward, and prepare for a battle..\n", "cyan")

        while (character["current_hp"] > 0) and (enemy["current_hp"] > 0):
            print_abilities(character)
            chosen_ability = select_ability(character)

            print_in_color(f"Your {chosen_ability} hits the {enemy['name']}", "cyan")
            # enemy health will decrease by character damage * character level * (1 + (0.1 * sword rarity))
            try:
                damage_given = character["damage"] * character["level"] * (1 + (0.2 * character["sword"]["rarity"]))
            except TypeError:
                damage_given = character["damage"] * character["level"]
            enemy["current_hp"] -= damage_given

            print_in_color(f"But the {enemy['name']}'s attack lands successfully as well", "cyan")
            # character health with decrease by 10 * (1 + (0.2 * enemy level))
            damage_taken = 10 * (1 + (0.2 * enemy["level"]))
            character["current_hp"] -= damage_taken

            print_in_color(f"[{character['name']} | hp: {character['current_hp']}/{character['max_hp']}]", "yellow")
            print(f"[{enemy['name']} | hp: {enemy['current_hp']}/{enemy['max_hp']}]")

        if (enemy["current_hp"] <= 0) and (character["current_hp"] > 0):
            print_in_color(f"\nCongratulations! You have defeated the {enemy['name']}", "cyan")

            earned_xp = 12 * enemy["level"]
            character["xp"] += earned_xp

            print_in_color(f"[{character['name']} | xp: +{earned_xp}]", "yellow")

    def enemy_battle(character: dict):
        print_in_color(f"Out of the corner of your eye you see a {enemy['name']} appear!\n", "cyan")

        if character["level"] < enemy["level"]:
            print_in_color(f"\nThis enemies level is greater than yours, you might want to weigh your options before "
                           f"you make your decision\n", "red")

        print_in_color("{:<15}Choice".format("Command"), "blue")

        options = list(enumerate(["Fight", "Flee"], start=1))
        for number, option in options:
            print(f"{number:<15}{option}")

        print_in_color("\nWhat would you like to do?", "purple")

        decision = cleanse(input())
        while (not decision.isnumeric()) or (int(decision) not in list(range(1, len(options) + 1))):
            print_in_color("\nThat wasn't one of the options! Take a closer look and try again.", "red")
            print_in_color("\nWhat would you like to do?", "purple")
            decision = cleanse(input())

        if int(decision) == 1:
            fight(character)
        else:
            print_in_color(f"\nAs you turn to flee the {enemy['name']} says:", "cyan")
            print("I should have guessed. You do seem like a cowardly creature. I will be here if you wish "
                  "to return with a bit more courage..")

    return enemy_battle


def generate_riddle(riddle_data: dict):
    def riddle_success(character: dict) -> None:
        print_in_color(f"\nCongratulations {character['name']}, you are not as dumb as I thought for a creature such "
                       f"as yourself.", "green")

        character["xp"] += 15
        print_in_color(f"[{character['name']} | xp: +15]", "yellow")

        print_in_color(f"To appreciate your success, I give you two options: try your luck at possibly earning a "
                       f"new ability, or except the gift of maximum health", "green")

        success_options = list(enumerate(["Try my luck at a new ability", "Refill HP to max"], start=1))

        print_in_color("\n{:<15}Choice".format("Command"), "blue")

        for number, option in success_options:
            print(f"{number:<15}{option}")

        print_in_color("\nPlease choose an option:", "purple")

        user_choice = cleanse(input())
        while (not user_choice.isnumeric()) or (int(user_choice) not in list(range(1, len(success_options) + 1))):
            print_in_color("\nThat wasn't one of the options! Take a closer look and try again.", "red")
            print_in_color("Please choose an option:", "purple")
            user_choice = cleanse(input())

        if int(user_choice) == 1:
            gets_new_ability = random.choice([True, False])
            new_ability = riddle_data["ability"]
            if (
                    gets_new_ability and
                    new_ability is not None and
                    new_ability not in character["abilities"]
            ):
                character["abilities"].append(new_ability)
                print(f"\nYou got lucky! I am feeling generous and will grant you a new ability. You can now use "
                      f"{new_ability}")
                print_in_color(f"[{character['name']} | abilities: +'{new_ability}']", "yellow")
            else:
                print("\nOh no, looks like you lost the coin flip, you will not be getting a new ability.")
        else:
            difference = character["max_hp"] - character["current_hp"]
            character["current_hp"] = character["max_hp"]
            print_in_color(f"[{character['name']} | xp: +{difference}]", "yellow")

    def riddle(character: dict) -> None:
        print_in_color("As you enter a dark, candle-lit room; you notice a mysterious potion placed by your feet.\n"
                       "You picked it up out of curiosity, but it started to shake violently.", "cyan")
        print_in_color("***POOF***", "cyan")
        print_in_color("Through the thick purple smoke, a Phantom Imp appears, with unnaturally wide smile, \n"
                       "and in a high-pitch crackle, speaks:", "cyan")
        time.sleep(8)

        print_in_color(
            "            _.----._     _.---.\n"
            "         .-'        `-.-'      `.\n"
            "       .'                 .:''':.`.\n"
            "     .'        .:'''':. .' .----.  `.\n"
            " .-./        .' .----.    /  .-. \   `.\n"
            "/.-.           /  .-. \   \ ' O ' |    \ \n"
            "||        `.   | ' O '/    \ `-' /     |\n"
            "|| (        \   \ `-'/      `-.__     / `.\n"
            " \`-'        )   .-'  --         )        `.\n"
            "  `-'     _.'   (            _.-'    _/\    \ \n"
            "     `.       /\_ `-.____..-'     .-' _/    / \n"
            "       `.     \_ `-._         _.-'_.-'   .' \n"
            "         `--.._ `-._ `-.__..-'_.-'     .' \n"
            "       .-'     `-._ `--.__..-'  _.----'`. \n"
            "      /            `---.......-' _     \ \ \n"
            "     /                          ( `-._.-` ) \n"
            "    /  /     _                  .-    _.-' \n"
            "   (  `-._.-' )                (_   .'    \ \n"
            "    `-._      -.               (_.-'       |\n"
            "        `.     _)                   __..---'\n"
            "       |  `-._) ''...__ .-. __...'''__..---'\n"
            "        \      '''...__((=))__...'''      /\n"
            "         |              `-'             .'\n"
            "         \                             /\n"
            "          |                           |\n"
            "          \     \    \      /    /   /\n"
            "           `. \               /     /\n"
            "             `.    \   \   /   /   /\n"
            "               `--.._   ` '  _.--'\n"
            "                      [====]\n"
            "                       )  (\n"
            "                    .-'    '-.\n"
            "                   |          |\n"
            "                   | .------. |\n"
            "                   | |  LGB | |\n"
            "                   | '------' |\n"
            "                   |          |\n"
            "                   '----------'\n", "green")

        print(f"Oh {character['name']}, you foolish creature, how dare you interrupt my slumber. For your transgression"
              f" you must prove your intellect to me with a riddle if you want me to spare your life..\n")
        time.sleep(5)
        print_in_color(riddle_data["question"], "purple")

        print_in_color("\n{:<15}Response".format("Command"), "blue")
        options = list(enumerate(riddle_data["options"], start=1))

        for number, option in options:
            print(f"{number:<15}{option}")

        print_in_color("\nYou have one chance to guess the answer or you will be punished.\nPlease choose the correct "
                       "answer to this riddle:", "purple")

        user_answer = cleanse(input())
        while (not user_answer.isnumeric()) or (int(user_answer) not in list(range(1, len(options) + 1))):
            print_in_color("\nThat wasn't one of the options! Take a closer look and try again.", "red")
            print_in_color("Please choose the correct answer to this riddle:", "purple")
            user_answer = cleanse(input())

        user_answer_string = [option for number, option in options if number == int(user_answer)][0]
        if user_answer_string == riddle_data["answer"]:
            riddle_success(character)
        else:
            print_in_color(f"\n{character['name']}, I knew a creature such as yourself was not intellectually gifted. "
                           f"That answer is far from correct and for that you must be punished!", "red")
            lost_hp = round(character["current_hp"] * 0.25)
            character["current_hp"] -= lost_hp
            print_in_color(f"[{character['name']} | hp: -{lost_hp}]", "yellow")

    return riddle


def create_batch_of_enemy_battles(amount: int) -> list:
    battles = []

    with open("enemies.json") as file_object:
        enemy_data = json.load(file_object)

        for enemy in enemy_data:
            battles.append(generate_enemy_battle(enemy))

    return battles[:amount + 1]


def create_batch_of_riddles(amount: int) -> list:
    riddles = []

    with open("riddles.json") as file_object:
        riddles_data = json.load(file_object)

        for riddle in riddles_data:
            riddles.append(generate_riddle(riddle))

    return riddles[:amount + 1]


def get_generic_room_description():
    descriptions = [
        "\nAs your foot passes the threshold into the next room, you feel something slither across your toes..",
        "\nYou are approaching the next room, and you see a dark mist fly past the archway..",
        "\nThe room feels cold and appears empty, but you sense a presence lingering..",
        "\nYou can taste the dampness in the air as you enter through the arched cobblestone..",
        "\nThe cold stone walls seem to radiate brisk air as you enter the room..",
        "\nYou step forward into the next room, you examine the walls and notice the hand of a skeleton jammed between "
        "two stones..",
        "\nYou hear the soft tapping of spider legs across the cobblestone archway..",
        "\nBeyond the cobblestone archway is a crumbling room, covered in crawling insects, broken pottery and bat "
        "droppings..",
        "\nTo the west you see a small statue of the queen's crown, crumbling onto the stone floor. It is covered in "
        "small bones, rat droppings and dead insects..",
        "\nA warn banner hangs from archway, displaying the crest of our dear queen. It is battered and torn, "
        "covered in condensation and insects..",
        "\nA fallen statue blocks the archway. You are able to slip thorough under arm, and enter into a room too "
        "clean for comfort..",
        "\nYou hear the drip of water to your east. There is a small fountain streaming out of the mouth of a stone "
        "gargoyle, mounted to the wall..",
        "\nA dim torch highlights the features of a pillaged statue, that has been eaten by time itself..",
        "\nThe deep purple banners flood the walls, with bats gripping to the bottom. You enter silently as to not "
        "disrupt them..",
        "\nA small puddle makes contact with the sole of your foot. You look up to see a crack in the cobblestone "
        "dripping at an unsettling-ly slow pace..",
        "\nIvy cracks the cobblestone and lines the ceiling. It's vines seem to plague the room, having propagated "
        "from north wall..",
        "\nA gloomy torch sits on the wall to the south. It's light fading with each grain of the hourglass..",
        "\nUnder your foot you hear the crack of bone. The room is a wasteland of bone and insects..",
        "\nA minor hum echoes off of the cobblestone walls. It is not random, but in an unsettling rhythm..",
        "\nA grand statue of the kingdom stands 10 feet tall in the far corner of the room, silently inspiring you to "
        "escape..",
        "\nOvergrown vines plague the stone floor, making you conscious of your feet. You fear that getting your foot "
        "stuck could render you a target for attack..",
        "\nBroken pottery carpets the floor. As you step you hear the cracking and fear that there may be creatures "
        "lurking beneath..",
        "\nYou advance carefully deeper through the castle dungeon, and enter a dark room, lit only by a dim torch..",
        "\nThe archway to the next room is crumbling under the damp runoff, pebbles fall like rain as you cover your "
        "head to enter..",
        "\nThere is a suspicious hole on the west wall, you fear something may be watching.."
    ]

    return random.choice(descriptions)


def get_generic_actions():
    actions = []

    # 36 battles
    enemy_battles = create_batch_of_enemy_battles(12)
    enemy_battles *= 3
    actions += enemy_battles

    # 36 riddles
    riddles = create_batch_of_riddles(26)
    actions += (riddles + riddles[:11])

    # 13 spider web rooms
    actions += list(itertools.repeat(spider_web_blockade, 13))

    # 12 empty rooms
    actions += list(itertools.repeat(empty_room, 12))

    random.shuffle(actions)

    return actions


def main():
    test_char = make_character("joe")

    # skeleton_soldier(test_char)
    # print(get_generic_room_description())
    # get_generic_challenges()(test_char)

    # spider_web_blockade(test_char)

    # riddles = create_batch_of_riddles(5)
    # riddles[0](test_char)

    battles = create_batch_of_enemy_battles(5)
    battles[0](test_char)


if __name__ == '__main__':
    main()
