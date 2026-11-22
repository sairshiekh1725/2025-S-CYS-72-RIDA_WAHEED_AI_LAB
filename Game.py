import tkinter as tk
from random import choice

WINNING_LINES = (
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6),
)

def winner(board):
    for a, b, c in WINNING_LINES:
        if board[a] != " " and board[a] == board[b] == board[c]:
            return board[a], (a, b, c)
    return None

def legal_moves(board):
    return [i for i, value in enumerate(board) if value == " "]

def minimax(board, is_ai_turn):
    result = winner(board)
    if result:
        return 1 if result[0] == "O" else -1
    if not legal_moves(board):
        return 0

    scores = []
    for move in legal_moves(board):
        board[move] = "O" if is_ai_turn else "X"
        scores.append(minimax(board, not is_ai_turn))
        board[move] = " "
    return max(scores) if is_ai_turn else min(scores)

def best_move(board):
    moves = legal_moves(board)
    if not moves:
        return None

    for symbol in ("O", "X"):
        for move in moves:
            board[move] = symbol
            result = winner(board)
            board[move] = " "
            if result and result[0] == symbol:
                return move

    best_score = -2
    choices = []
    for move in moves:
        board[move] = "O"
        score = minimax(board, False)
        board[move] = " "
        if score > best_score:
            best_score, choices = score, [move]
        elif score == best_score:
            choices.append(move)
    return choice(choices)

class TicTacToe:
    def __init__(self):
        self.board = [" "] * 9
        self.game_over = False

        self.window = tk.Tk()
        self.window.title("Tic-Tac-Toe AI - RIDA WAHEED")
        self.window.resizable(False, False)

        tk.Label(self.window, text="Tic-Tac-Toe", font=("Arial", 22, "bold")).grid(
            row=0, column=0, columnspan=3, pady=10)

        self.buttons = []
        for position in range(9):
            row, column = divmod(position, 3)
            button = tk.Button(
                self.window, text=" ", font=("Arial", 26, "bold"),
                width=4, height=2, bg="white",
                command=lambda p=position: self.play_human_move(p))
            button.grid(row=row + 1, column=column, padx=3, pady=3)
            self.buttons.append(button)

        self.status = tk.Label(self.window, text="Your turn: X",
                               font=("Arial", 13), fg="red")
        self.status.grid(row=4, column=0, columnspan=3, pady=8)

        tk.Button(self.window, text="New Game", font=("Arial", 12),
                  command=self.reset).grid(row=5, column=0, columnspan=3, pady=(0, 10))

    def play_human_move(self, position):
        if self.game_over or self.board[position] != " ":
            return
        self.board[position] = "X"
        self.buttons[position].config(text="X", fg="#d60000")
        self.buttons[position].config(state="disabled")

        if self.finish_if_needed():
            return

        self.status.config(text="AI is thinking: O", fg="#0057c8")
        self.window.update()
        move = best_move(self.board)
        if move is not None:
            self.board[move] = "O"
            self.buttons[move].config(text="O", fg="#0057c8")
            self.buttons[move].config(state="disabled")

        if not self.finish_if_needed():
            self.status.config(text="Your turn: X", fg="red")

    def finish_if_needed(self):
        result = winner(self.board)
        if result:
            symbol, line = result
            self.game_over = True
            for position in line:
                self.buttons[position].config(bg="#ffe066")
            self.status.config(text=f"{symbol} wins!", fg="#d60000" if symbol == "X" else "#0057c8")
            self.disable_all()
            return True
        if not legal_moves(self.board):
            self.game_over = True
            self.status.config(text="Draw!", fg="#555555")
            self.disable_all()
            return True
        return False

    def disable_all(self):
        for button in self.buttons:
            button.config(state="disabled")

    def reset(self):
        self.board = [" "] * 9
        self.game_over = False
        for button in self.buttons:
            button.config(text=" ", state="normal", bg="white", fg="black")
        self.status.config(text="Your turn: X", fg="red")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    TicTacToe().run()
