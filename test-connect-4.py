import game
YELLOW = 'YELLOW'
RED = 'RED'

from constants import (
    rows,
    columns,
)

def test_empty_board():
    board = [[None, None, None, None, None, None, None],
             [None, None, None, None, None, None, None],
             [None, None, None, None, None, None, None],
             [None, None, None, None, None, None, None],
             [None, None, None, None, None, None, None],
             [None, None, None, None, None, None, None]]
    assert game.empty_board() == board

def test_put_piece_1():
    board = game.empty_board()
    game.put_piece(board, 0, YELLOW)
    assert board[rows-1][0] == YELLOW

def test_put_piece_2():
    board = game.empty_board()
    for _ in range(3):
        game.put_piece(board, 0, YELLOW)
    game.put_piece(board, 0, RED)
    assert board[rows-4][0] == RED

def test_put_piece_3():
    board = game.empty_board()
    for _ in range(3):
        game.put_piece(board, 3, YELLOW)
    game.put_piece(board, 3, RED)
    assert board[rows-4][3] == RED

def test_is_valid_1():
    board = game.empty_board()
    assert game.is_valid(board, -1) is False

def test_is_valid_2():
    board = game.empty_board()
    assert game.is_valid(board, 0) is True
  
def test_is_valid_3():
    board = game.empty_board()
    assert game.is_valid(board, 7) is False

def test_is_valid_4():
    board = game.empty_board()
    assert game.is_valid(board, 5) is True

def test_is_valid_5():
    board = game.empty_board()
    for _ in range(6):
        game.put_piece(board, 0, YELLOW)
    assert game.is_valid(board, 0) is False

def test_is_valid_6():
    board = game.empty_board()
    for _ in range(5):
        game.put_piece(board, 0, YELLOW)
    assert game.is_valid(board, 0) is True

def test_no_more_moves_1():
    board = game.empty_board()
    for i in range(7):
        for _ in range(6):
            game.put_piece(board, i, YELLOW)
    assert game.no_more_moves(board) is True

def test_no_more_moves_2():
    board = game.empty_board()
    for i in range(7):
        for _ in range(5):
            game.put_piece(board, i, YELLOW)
    assert game.no_more_moves(board) is False

def test_get_winner_1():
    board = [[None, None, None, None, None, None, None],
             [None, None, None, RED, RED, None, None],
             [None, None, None, YELLOW, RED, None, YELLOW],
             [None, None, None, YELLOW, YELLOW, YELLOW, RED],
             [None, None, None, RED, YELLOW, RED, YELLOW],
             [None, None, None, YELLOW, RED, RED, YELLOW]]
    assert game.get_winner(board) == YELLOW

def test_get_winner_2():
    board = [[None, None, None, None, None, None, None],
             [None, None, None, RED, RED, None, None],
             [None, None, None, YELLOW, RED, None, YELLOW],
             [None, None, None, YELLOW, YELLOW, YELLOW, RED],
             [None, None, None, RED, YELLOW, RED, YELLOW],
             [None, None, None, YELLOW, RED, RED, YELLOW]]
    assert game.get_winner(board) == YELLOW

def test_get_winner_3():
    board = [[None, None, None, None, None, None, None],
             [None, None, YELLOW, YELLOW, None, RED, YELLOW],
             [None, None, RED, RED, RED, RED, RED],
             [None, None, RED, RED, YELLOW, YELLOW, YELLOW],
             [None, None, YELLOW, YELLOW, RED, YELLOW, RED],
             [None, None, RED, YELLOW, YELLOW, YELLOW, RED]]
    assert game.get_winner(board) == RED

def test_get_winner_3():    
    board = game.empty_board()
    game.put_piece(board, 0, YELLOW)    
    assert game.get_winner(board) is None