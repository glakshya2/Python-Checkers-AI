from checkers.board import Board
from checkers.piece import Piece
from checkers.constants import RED
from checkers.constants import WHITE
from minimax.algorithm import minimax
import random
import pandas as pd
import threading
import warnings

warnings.filterwarnings("ignore")


def generate_data(name):
    df = pd.DataFrame(columns=["Board", "Move"])

    for gen_no in range(12200):
        red_pieces = random.randint(1, 12)
        white_pieces = random.randint(1, 12)
        red_kings = random.randint(0, red_pieces)
        white_kings = random.randint(0, white_pieces)
        board = Board()
        red_positions = random.sample(range(0, 32, 2), red_pieces)
        for pos in red_positions:
            row = pos // 4
            col = (pos % 4) * 2 + (row % 2)
            board.board[row][col] = Piece(row, col, RED)

        red_king_positions = random.sample(red_positions, red_kings)
        for pos in red_king_positions:
            row = pos // 4
            col = (pos % 4) * 2 + (row % 2)
            board.board[row][col].make_king()

        white_positions = random.sample(range(0, 32, 2), white_pieces)
        for pos in white_positions:
            row = pos // 4
            col = (pos % 4) * 2 + (row % 2)
            board.board[row][col] = Piece(row, col, WHITE)

        white_king_positions = random.sample(white_positions, white_kings)
        for pos in white_king_positions:
            row = pos // 4
            col = (pos % 4) * 2 + (row % 2)
            board.board[row][col].make_king()

        move = minimax(board, 3, WHITE, None)

        board_arr = []
        for i in range(8):
            for j in range(8):
                piece = board.get_piece(i, j)
                if piece:
                    if piece.color == WHITE:
                        if piece.king:
                            board_arr.append(2)
                        else:
                            board_arr.append(1)
                    else:
                        if piece.king:
                            board_arr.append(-2)
                        else:
                            board_arr.append(-1)
                else:
                    board_arr.append(0)

        data = pd.DataFrame({"Board": [board_arr], "Move": [move[2]]})
        df = df.append(data, ignore_index=True)
        print("generate:", gen_no)
        if gen_no % 50 == 0:
            df.to_csv(name, index=False)


threads = [
    threading.Thread(target=generate_data, args=(f"data{i}.csv",)) for i in range(8)
]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()
