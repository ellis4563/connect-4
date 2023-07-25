from typing import Optional, Literal, TypeAlias

ROWS = 6
COLUMNS = 7

Piece: TypeAlias = Literal["RED", "YELLOW"]

RED: Piece = "RED"
YELLOW: Piece = "YELLOW"

State: TypeAlias = Literal["RED_TURN", "YELLOW_TURN", "RED_WIN", "YELLOW_WIN", "DRAW"]

RED_TURN: State = "RED_TURN"
YELLOW_TURN: State = "YELLOW_TURN"
RED_WIN: State = "RED_WIN"
YELLOW_WIN: State = "YELLOW_WIN"
DRAW: State = "DRAW"

Board = list[list[Optional[Piece]]]


MAKE_TEXT_RED = "\x1B[37;41m"
MAKE_TEXT_YELLOW = "\x1B[30;43m"
RESET_TEXT_COLOR = "\x1B[0m"


def empty_board() -> Board:
    """
    This function returns an empty board.

    Inputs:

    Returns:
        the empty board
    """
    return [
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
    ]


def get_input(board: Board, state: State) -> int:
    """
    This function checks prompts the user for an input and returns the result.
    It prompts them until they enter a valid move.

    Inputs:
        board: the board
        state: the current state

    Returns:
        a number from 0 to 6 that represents a valid move
    """
    print()
    if state == RED_TURN:
        prompt = "Red's move: "
    else:
        prompt = "Yellow's move: "

    while True:
        try:
            raw = input(prompt)
            move = int(raw) - 1
            if is_valid(board, move):
                print()
                return move
        except ValueError:
            pass
        print("Invalid move! ", end="")


def get_horizontal_winner(board: Board) -> Optional[Piece]:
    """
    This function returns a color if there are 4 horizontal pieces of that color
    in a row. It returns `None` otherwise.

    Inputs:
        board: the board to search

    Returns:
        `None` if there is no winner and the piece color if there is a horizontal winner
    """
    for i in range(0, 6):
        for j in range(0, 4):
            if (
                board[i][j] == RED
                and board[i][j + 1] == RED
                and board[i][j + 2] == RED
                and board[i][j + 3] == RED
            ):
                return RED
            if (
                board[i][j] == YELLOW
                and board[i][j + 1] == YELLOW
                and board[i][j + 2] == YELLOW
                and board[i][j + 3] == YELLOW
            ):
                return YELLOW
    return None


def get_vertical_winner(board: Board) -> Optional[Piece]:
    """
    This function returns a color if there are 4 vertical pieces of that color
    in a row. It returns `None` otherwise.

    Inputs:
        board: the board to search

    Returns:
        `None` if there is no winner and the piece color if there is a vertical winner
    """
    for i in range(0, 3):
        for j in range(0, 7):
            if (
                board[i][j] == RED
                and board[i + 1][j] == RED
                and board[i + 2][j] == RED
                and board[i + 3][j] == RED
            ):
                return RED
            if (
                board[i][j] == YELLOW
                and board[i + 1][j] == YELLOW
                and board[i + 2][j] == YELLOW
                and board[i + 3][j] == YELLOW
            ):
                return YELLOW
    return None


def get_up_diagonal_winner(board: Board) -> Optional[Piece]:
    """
    This function returns a color if there are 4 diagonal pieces of that color
    in a row. It returns `None` otherwise.

    Inputs:
        board: the board to search

    Returns:
        `None` if there is no winner and the piece color if there is a diagonal winner
    """
    for i in range(0, 3):
        for j in range(0, 4):
            if (
                board[i + 3][j] == RED
                and board[i + 2][j + 1] == RED
                and board[i + 1][j + 2] == RED
                and board[i][j + 3] == RED
            ):
                return RED
            if (
                board[i + 3][j] == YELLOW
                and board[i + 2][j + 1] == YELLOW
                and board[i + 1][j + 2] == YELLOW
                and board[i][j + 3] == YELLOW
            ):
                return YELLOW
    return None


def get_down_diagonal_winner(board: Board) -> Optional[Piece]:
    """
    This function returns a color if there are 4 diagonal pieces of that color
    in a row. It returns `None` otherwise.

    Inputs:
        board: the board to search

    Returns:
        `None` if there is no winner and the piece color if there is a diagonal winner
    """
    for i in range(0, 3):
        for j in range(0, 4):
            if (
                board[i][j] == RED
                and board[i + 1][j + 1] == RED
                and board[i + 2][j + 2] == RED
                and board[i + 3][j + 3] == RED
            ):
                return RED
            if (
                board[i][j] == YELLOW
                and board[i + 1][j + 1] == YELLOW
                and board[i + 2][j + 2] == YELLOW
                and board[i + 3][j + 3] == YELLOW
            ):
                return YELLOW
    return None


def get_winner(board: Board) -> Optional[Piece]:
    """
    This function returns a color if there is a winner. It returns `None` otherwise.

    Inputs:
        board: the board to search

    Returns:
        `None` if there is no winner and the piece color if there is a winner
    """
    winner = get_horizontal_winner(board)
    if winner == RED:
        return RED
    if winner == YELLOW:
        return YELLOW

    winner = get_vertical_winner(board)
    if winner == RED:
        return RED
    if winner == YELLOW:
        return YELLOW

    winner = get_up_diagonal_winner(board)
    if winner == RED:
        return RED
    if winner == YELLOW:
        return YELLOW

    winner = get_down_diagonal_winner(board)
    if winner == RED:
        return RED
    if winner == YELLOW:
        return YELLOW

    return None


def no_more_moves(board: Board) -> bool:
    """
    This function returns `True` if the board has no more moves (ie, the board
    is full of pieces).

    Inputs:
        board: the board to check

    Returns:
        `True` if the board is full
    """
    for row in board:
        for piece in row:
            if piece == None:
                return False
    return True


def is_valid(board: Board, move: int) -> bool:
    """
    This function returns `True` if the move is valid (ie, the move is between 0
    and 6 and the column is not full).

    Inputs:
        board: the board
        move: the move to check

    Returns:
        `True` if the move is valid
    """
    if move < 0:
        return False
    if move > 6:
        return False

    if board[0][move] == None:
        return True
    else:
        return False


def put_piece(board: Board, move: int, piece: Piece) -> None:
    """
    This function updates the board with the given piece at the given move. It
    assumes that move is valid.

    Inputs:
        board: the board
        move: the move
        piece: the piece

    Returns:
        None
    """
    for i in range(5, -1, -1):
        if board[i][move] == None:
            board[i][move] = piece
            return


def update(state: State, board: Board) -> State:
    """
    This function handles input, updates the board and returns the next state.

    Inputs:
        state: The state
        board: the board to be updated (in place)

    Returns:
        the new state
    """
    move = get_input(board, state)

    if state == RED_TURN:
        put_piece(board, move, RED)
    if state == YELLOW_TURN:
        put_piece(board, move, YELLOW)

    winner = get_winner(board)
    if winner == RED:
        return RED_WIN
    if winner == YELLOW:
        return YELLOW_WIN

    if no_more_moves(board):
        return DRAW

    if state == RED_TURN:
        return YELLOW_TURN
    else:
        return RED_TURN


def print_board(board: Board) -> None:
    """
    This function takes the board and prints it.

    Inputs:
        board: the board

    Returns:
        None
    """
    print(" 1 2 3 4 5 6 7")
    for row in board:
        for piece in row:
            if piece == YELLOW:
                print(" y", end="")
            if piece == RED:
                print(" R", end="")
            if piece is None:
                print(" .", end="")
        print("")
