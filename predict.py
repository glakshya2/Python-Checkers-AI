import numpy as np
import tensorflow as tf
from checkers.board import Board
from checkers.piece import Piece
from checkers.constants import WHITE
from minimax.algorithm import minimax


def convert_to_arr(board):
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
                
    return board_arr

def preprocess_board(board_arr):
    board_array = np.array(board_arr)
    board_matrix = np.reshape(board_array, (8,8))
    
    one_hot_board = np.zeros((8,8,5))
    for i in range(8):
        for j in range(8):
            if board_matrix[i][j] == 1:
                one_hot_board[i][j][0] = 1
            elif board_matrix[i][j] == 2:
                one_hot_board[i][j][1] = 1
            elif board_matrix[i][j] == -1:
                one_hot_board[i][j][2] = 1
            elif board_matrix[i][j] == -2:
                one_hot_board[i][j][3] = 1
            else:
                one_hot_board[i][j][4] = 1

    one_hot_board = np.expand_dims(one_hot_board, axis=0)

    return one_hot_board
    
def make_move(board, piece, prediction, skip):
    board.move(piece, prediction[2], prediction[3])
    if skip:
        board.remove(skip)
        
    return board

def predict_move(board):
    board_arr = convert_to_arr(board)
    preprocessed = preprocess_board(board_arr)
    model = tf.keras.models.load_model('checkers_rnn')
    
    prediction = model.predict(preprocessed)
    prediction = np.round(prediction).astype(int)
    print(prediction)
    
    piece= board.get_piece(prediction[0][0], prediction[0][1])
    if piece:
        moves = board.get_valid_moves(piece)
        if (prediction[0][2], prediction[0][3]) in moves:
            skip = moves[(prediction[0][2], prediction[0][3])]
            return make_move(board, piece, prediction, skip)
        else:
            return minimax(board, 3, WHITE, None)[1]
    else:
        return minimax(board, 3, WHITE, None)[1]