import tkinter as tk
from othello_ui import OthelloUI

class Othello:
    def __init__(self):
        self.board_size = 8
        self.board = [[0 for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.board[3][3] = 1  # Black
        self.board[4][4] = 1  # Black
        self.board[3][4] = -1 # White
        self.board[4][3] = -1 # White
        self.current_player = 1  # 1: Black, -1: White
        self.computer_player = -1 # -1: White
        self.ui = None

    def set_ui(self, ui):
        self.ui = ui

    def get_board(self):
        return self.board

    def place_piece(self, row, col):
        if self.board[row][col] == 0 and self.is_valid_move(row, col):
            self.board[row][col] = self.current_player
            self.flip_pieces(row, col)
            self.current_player *= -1
            return True
        return False

    def is_valid_move(self, row, col):
        for dr in range(-1, 2):
            for dc in range(-1, 2):
                if dr == 0 and dc == 0:
                    continue
                if self.can_flip(row, col, dr, dc):
                    return True
        return False

    def can_flip(self, row, col, dr, dc):
        opponent = -self.current_player
        r, c = row + dr, col + dc
        if not (0 <= r < self.board_size and 0 <= c < self.board_size and self.board[r][c] == opponent):
            return False

        r += dr
        c += dc
        while 0 <= r < self.board_size and 0 <= c < self.board_size:
            if self.board[r][c] == 0:
                return False
            if self.board[r][c] == self.current_player:
                return True
            r += dr
            c += dc
        return False

    def flip_pieces(self, row, col):
        for dr in range(-1, 2):
            for dc in range(-1, 2):
                if dr == 0 and dc == 0:
                    continue
                if self.can_flip(row, col, dr, dc):
                    self.flip_direction(row, col, dr, dc)

    def flip_direction(self, row, col, dr, dc):
        opponent = -self.current_player
        r, c = row + dr, col + dc
        while 0 <= r < self.board_size and 0 <= c < self.board_size and self.board[r][c] == opponent:
            self.board[r][c] = self.current_player
            r += dr
            c += dc

    def has_valid_moves(self, player):
        for row in range(self.board_size):
            for col in range(self.board_size):
                if self.board[row][col] == 0:
                    self.current_player = player
                    if self.is_valid_move(row, col):
                        return True
        return False

    def get_winner(self):
        black_count = 0
        white_count = 0
        for row in range(self.board_size):
            for col in range(self.board_size):
                if self.board[row][col] == 1:
                    black_count += 1
                elif self.board[row][col] == -1:
                    white_count += 1

        if black_count > white_count:
            return 1
        elif white_count > black_count:
            return -1
        else:
            return 0

    def is_game_over(self):
        return not (self.has_valid_moves(1) or self.has_valid_moves(-1))

    def display_board(self):
        for row in self.board:
            print(row)

if __name__ == "__main__":
    othello = Othello()
    othello.display_board()
