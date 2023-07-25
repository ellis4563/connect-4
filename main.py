import game


def main():
    board = game.empty_board()
    state = game.RED_TURN

    game.print_board(board)

    while True:
        state = game.update(state, board)
        game.print_board(board)

        if state == game.RED_WIN:
            print("\nRed wins!")
            break
        elif state == game.YELLOW_WIN:
            print("\nYellow wins!")
            break
        elif state == game.DRAW:
            print("\nDraw!")
            break


if __name__ == "__main__":
    main()
