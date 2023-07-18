from typing import Optional, Literal, TypeAlias

import pygame

from constants import (
    rows,
    columns,
    padding,
    top_padding,
    piece_size,
    border_size,
    border_color,
    background_color,
    red_color,
    yellow_color,
    text_holder,
    number_x_offset,
    number_y_offset,
)

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


def empty_board() -> Board:
    """
    This function returns an empty board.

    Inputs:

    Returns:
        the empty board
    """
    raise NotImplementedError


def get_input() -> tuple[Optional[int], bool]:
    """
    This function checks the pygame events to see if any of the number keys
    from 1 to 6 were pressed. It also checks if the app should exit.

    Inputs:

    Returns:
        move, done: move is an number from 0 to 6 or `None` and done is a bool
    """
    raise NotImplementedError


def get_horizontal_winner(board: Board) -> Optional[Piece]:
    """
    This function returns a color if there are 4 horizontal pieces of that color
    in a row. It returns `None` otherwise.

    Inputs:
        board: the board to search

    Returns:
        `None` if there is no winner and the piece color if there is a horizontal winner
    """
    raise NotImplementedError


def get_vertical_winner(board: Board) -> Optional[Piece]:
    """
    This function returns a color if there are 4 vertical pieces of that color
    in a row. It returns `None` otherwise.

    Inputs:
        board: the board to search

    Returns:
        `None` if there is no winner and the piece color if there is a vertical winner
    """
    raise NotImplementedError


def get_up_diagonal_winner(board: Board) -> Piece | None:
    """
    This function returns a color if there are 4 diagonal pieces of that color
    in a row. It returns `None` otherwise.

    Inputs:
        board: the board to search

    Returns:
        `None` if there is no winner and the piece color if there is a diagonal winner
    """
    raise NotImplementedError


def get_down_diagonal_winner(board: Board) -> Optional[Piece]:
    """
    This function returns a color if there are 4 diagonal pieces of that color
    in a row. It returns `None` otherwise.

    Inputs:
        board: the board to search

    Returns:
        `None` if there is no winner and the piece color if there is a diagonal winner
    """
    raise NotImplementedError


def get_winner(board: Board) -> Optional[Piece]:
    """
    This function returns a color if there is a winner. It returns `None` otherwise.

    Inputs:
        board: the board to search

    Returns:
        `None` if there is no winner and the piece color if there is a winner
    """
    raise NotImplementedError


def no_more_moves(board: Board) -> bool:
    """
    This function returns `True` if the board has no more moves (ie, the board
    is full of pieces).

    Inputs:
        board: the board to check

    Returns:
        `True` if the board is full
    """
    raise NotImplementedError


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
    raise NotImplementedError


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
    raise NotImplementedError


def update(state: State, board: Board) -> tuple[State, bool]:
    """
    This function handles input, updates the board and returns the next state.

    Inputs:
        state: The state
        board: the board to be updated (in place)

    Returns:
        state, done: state is the new state, done is `True` if the app should exit.
    """
    raise NotImplementedError


def draw(state: State, board: Board, screen: pygame.Surface) -> None:
    """
    This function takes the state and the board and draws them to the screen.

    Inputs:
        state: the state
        board: the board
        screen: the screen to draw to

    Returns:
        None
    """
    raise NotImplementedError
