from board import make_board, describe_current_location, is_valid_move
from character import make_character, is_alive, move_character
from helpers import get_user_choice
from printing import print_board


def game() -> None:
    rows = 10
    columns = 10

    board = make_board(rows, columns)

    character_name = input("Please enter a name for your character: ")
    character = make_character(character_name)

    achieved_goal = False

    # function with pre game description

    while is_alive(character) and not achieved_goal:
        # function to get users choice for direction
        direction = get_user_choice()

        if is_valid_move(direction, board, character):
            # function to move the character
            move_character(direction, board, character)
            print_board(rows, columns, character["position"])

            # describe current location
            describe_current_location(board, character)

            # then execute the action function

            # function to check if character leveled up, died, got items, etc.
                # if they pick up a special item or something and there is addition challenge then start that

                # if they levelled up, maybe print some cool ascii art or something

        # else:
            # tell the user that they can't go in that direction


def main() -> None:
    """
    Drive the program.
    """
    game()


if __name__ == '__main__':
    main()
