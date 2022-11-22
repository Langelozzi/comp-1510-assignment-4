from board import make_board


def game() -> None:
    rows = 10
    columns = 10

    board = make_board(rows, columns)
    character = make_character()

    achieved_goal = False

    while is_alive(character) and not achieved_goal:
        pass
        # function to describe current location

        # function to get users choice for direction

        # function to check if the move is valid

        # if the move is valid
            # function to move the character

            # describe next location

            # if there is a challenge on that tile
                # then execute the challenge function

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
