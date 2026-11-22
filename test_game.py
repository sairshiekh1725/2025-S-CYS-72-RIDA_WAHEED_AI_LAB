import unittest

from Game import winner, legal_moves, best_move


class TicTacToeTests(unittest.TestCase):
    def test_empty_board(self):
        board = [" "] * 9
        self.assertEqual(len(legal_moves(board)), 9)
        self.assertIsNone(winner(board))

    def test_occupied_cell_rejected(self):
        board = ["X"] + [" "] * 8
        self.assertNotIn(0, legal_moves(board))

    def test_x_wins(self):
        board = ["X", "X", "X", "O", "O", " ", " ", " ", " "]
        self.assertEqual(winner(board)[0], "X")

    def test_o_wins(self):
        board = ["O", "O", "O", "X", "X", " ", " ", " ", " "]
        self.assertEqual(winner(board)[0], "O")

    def test_draw(self):
        board = ["X", "O", "X", "X", "O", "O", "O", "X", "X"]
        self.assertIsNone(winner(board))
        self.assertEqual(legal_moves(board), [])

    def test_ai_immediate_win(self):
        board = ["O", "O", " ", "X", "X", " ", " ", " ", " "]
        self.assertIn(best_move(board), (2,))

    def test_ai_blocks_immediate_threat(self):
        board = ["X", "X", " ", "O", " ", " ", " ", " ", " "]
        self.assertIn(best_move(board), (2,))


if __name__ == "__main__":
    unittest.main()
