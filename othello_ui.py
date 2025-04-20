import tkinter as tk
import tkinter.messagebox
import time
import random

class OthelloUI:
    def __init__(self, game):
        self.game = game
        self.window = tk.Tk()
        self.window.title("Othello")
        self.window.configure(bg="green")
        self.buttons = []
        self.board_size = game.board_size
        self.create_board()
        self.game.set_ui(self)

    def create_board(self):
        for row in range(self.board_size):
            button_row = []
            for col in range(self.board_size):
                button = tk.Button(
                    self.window,
                    width=4,
                    height=2,
                    bg="green",
                    fg="white",
                    command=lambda r=row, c=col: self.on_button_click(r, c)
                )
                button.grid(row=row, column=col)
                button_row.append(button)
            self.buttons.append(button_row)
        self.update_board()

    def on_button_click(self, row, col):
        if self.game.place_piece(row, col):
            self.update_board()
            if self.game.is_game_over():
                self.show_winner()
            else:
                self.window.after(3000, self.computer_move)

    def computer_move(self):
        possible_moves = []
        for row in range(self.board_size):
            for col in range(self.board_size):
                self.game.current_player = self.game.computer_player
                if self.game.board[row][col] == 0 and self.game.is_valid_move(row, col):
                    possible_moves.append((row, col))

        if possible_moves:
            row, col = random.choice(possible_moves)
            self.game.current_player = self.game.computer_player
            if self.game.place_piece(row, col):
                self.update_board()
                if self.game.is_game_over():
                    self.show_winner()
                elif not self.game.has_valid_moves(self.game.current_player):
                    self.game.current_player *= -1
                    if not self.game.has_valid_moves(self.game.current_player):
                        self.show_winner()

    def update_board(self):
        board = self.game.get_board()
        for row in range(self.board_size):
            for col in range(self.board_size):
                if board[row][col] == 1:
                    self.buttons[row][col].config(text="B", fg="black")
                elif board[row][col] == -1:
                    self.buttons[row][col].config(text="W", fg="lightgray")
                else:
                    self.buttons[row][col].config(text="", fg="black")

    def show_winner(self):
        winner = self.game.get_winner()
        if winner == 1:
            message = "Black wins!"
        elif winner == -1:
            message = "White wins!"
        else:
            message = "It's a tie!"
        tkinter.messagebox.showinfo("Game Over", message)

    def start(self):
        self.window.mainloop()

if __name__ == "__main__":
    from othello import Othello
    game = Othello()
    ui = OthelloUI(game)
    ui.start()
