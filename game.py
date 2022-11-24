from board import make_board, describe_current_location, is_valid_move, print_board
from character import make_character, is_alive, move_character, get_character_name
from helpers import get_user_choice, print_in_color
from actions import cell_description


def game() -> None:
    rows = 10
    columns = 10
    achieved_goal = False

    board = make_board(rows, columns)

    # intro art and backstory

    character_name = get_character_name()
    character = make_character(character_name)

    # cell_description()

    print_board(rows, columns, character["position"])

    while is_alive(character) and not achieved_goal:
        # function to get users choice for direction
        direction = get_user_choice(board, character)

        if direction == "q" or direction == "quit":
            break
        elif is_valid_move(direction, board, character):
            # move the character to desired location
            move_character(direction, board, character)
            # show their new location
            print_board(rows, columns, character["position"])
            # describe current location
            describe_current_location(board, character)

            if board[character["position"]]["action"] is not None:
                action_function = board[character["position"]]["action"]
                action_function(character)

            # function to check if character leveled up, died, got items, etc.
                # if they pick up a special item or something and there is addition challenge then start that
                # if they levelled up, maybe print some cool ascii art or something
        else:
            print_in_color("There is no path in that direction, you can't walk through walls!!", "red")

    # Game over function


def main() -> None:
    """
    Drive the program.
    """
    game()


if __name__ == '__main__':
    main()
