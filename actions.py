# 10 basic challenges which can be mob fights or puzzles
# 3 sub boss fights
# 1 final boss fights
from helpers import cleanse
from character import make_character

import random


def get_generic_room_description():
    descriptions = [
        "aaa theres a snake",
        "oo i think i see a ghost"


    ]
    return random.choice(descriptions)


def possessed_knight(character: dict) -> None:
    print("A possessed knight materializes in front of me...\n")
    user_action = cleanse(input("What should I do? \n\n Type: \n 1 \t to run away \n 2 \t to attack the enemy\n\n"))

    if user_action == '1':
        print("I got away!")
    elif user_action == '2':
        print("I will get you!")
        # skill_prompt = input(print("Should I use a skill?"))
        # if skill_prompt == 'y' or 'yes':
        #     print()
    else:
        print("Please type a valid input")


def skeleton_soldier(character: dict) -> None:
    enemy = {
        "name": "Skeleton Soldier",
    }
    print("It's a skeleton...\n")
    user_action = cleanse(input("What should I do? \n\n Type: \n 1 \t to run away \n 2 \t to attack the enemy\n\n"))

    if user_action == '1':
        print("I got away!")
    elif user_action == '2':
        counter = 1
        print(f'I will get you {enemy["name"]}!')
        print("Should I use a skill?")
        for skills in list(character["abilities"].keys()):
            print("Type:")
            print(f'{counter} \t {skills}')
            counter += 1
        skill_prompt = cleanse(input())
    #     if skill_prompt == '1':
    #         # print(f'Select skill: \n\n Type: \n 1 \t {} \n 2 \t No \n\n')
    #         # # maybe use for loop to list through each ability
    #         # # skill_slection = input()
    #         # print(f"You selected {skill_slection}")
    #     elif skill_prompt == '2':
    #         # attack phase
    #     else:
    #         print("Please select a valid input")
    # else:
        print("Please select a valid input")


def get_generic_challenges():
    challenges = [
        possessed_knight,
        skeleton_soldier,
    ]
    return random.choice(challenges)


def main():
    test_char = make_character("joe")

    skeleton_soldier(test_char)
    # print(get_generic_room_description())
    # get_generic_challenges()(test_char)


if __name__ == '__main__':
    main()
