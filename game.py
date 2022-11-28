from board import make_board, describe_current_location, is_valid_move, print_board
from character import make_character, is_alive, move_character, get_character_name, show_stats, leveled_up, \
    level_up_sequence
from helpers import get_user_choice, print_in_color
from actions import cell_description, opening_dialogue, game_over, game_completed


def game() -> None:
    rows = 10
    columns = 10
    achieved_goal = False

    board = make_board(rows, columns)

    character_name = get_character_name()
    character = make_character(character_name)

    # opening_dialogue()
    # cell_description()

    while is_alive(character) and not achieved_goal:
        print_board(rows, columns, character["position"])
        choice = get_user_choice(board, character)

        if choice == "quit":
            break
        elif choice == "show stats":
            show_stats(character)
        elif is_valid_move(choice, board, character):

            move_character(choice, board, character)

            print_board(rows, columns, character["position"])

            room_solved = board[character["position"]]["solved"]
            if not room_solved:
                describe_current_location(board, character)

                action_function = board[character["position"]]["action"]
                if action_function is not None:
                    board[character["position"]]["solved"] = action_function(character)
            else:
                print_in_color("\nYou have already completed your duties here, please move on.\n", "cyan")

            if leveled_up(character):
                level_up_sequence(character)
        else:
            print_in_color("There is no path in that direction, you can't walk through walls!!", "red")

    if character["current_hp"] < 0:
        game_over(character)
    elif achieved_goal:
        game_completed(character)
    else:
        print_in_color("\nThanks for playing, we hope you play again sometime :)", "cyan")


def main() -> None:
    """
    Drive the program.
    """
    game()


if __name__ == '__main__':
    main()
