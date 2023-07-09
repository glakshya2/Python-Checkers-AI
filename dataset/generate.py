from ..checkers.board import Board 
from ..checkers.board import Piece
from ..checkers.constants import RED 
from ..checkers.constants import WHITE
import random

for gen_no in range(50000):
    red_pieces = random.randint(1,12)
    white_pieces = random.randint(1,12)
    red_kings = random.randint(0, red_pieces)
    white_kings = random.randint(0, white_pieces)
    board = Board
    red_positions = random.sample(range(0, 32, 2), red_pieces)
    for pos in red_positions:
        row = pos // 4
        col = (pos % 4) * 2 + (row % 2)
        board[row][col] = Piece(row, col, RED)
        
    red_king_positions = random.sample(red_positions, red_kings)
    for pos in red_king_positions:
        row = pos // 4
        col = (pos % 4) * 2 + (row % 2)
        board[row][col].make_king()
        
    
    white_positions = random.sample(range(0, 32, 2), white_pieces)
    for pos in white_positions:
        row = pos // 4
        col = (pos % 4) * 2 + (row % 2)
        board[row][col] = Piece(row, col, WHITE)
        
    white_king_positions = random.sample(white_positions, white_kings)
    for pos in white_king_positions:
        row = pos // 4
        col = (pos % 4) * 2 + (row % 2)
        board[row][col].make_king()
    
    