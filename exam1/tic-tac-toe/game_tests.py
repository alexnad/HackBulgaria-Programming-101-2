import unittest
from game import Game
from game import InvalidMoveError


class TestGame(unittest.TestCase):
    def assert_outcome(self, expected_outcome, board):
        game = Game(board)
        self.assertEqual(game.calculate_outcome(), expected_outcome)

    def test_win_by_row(self):
        self.assert_outcome(Game.X_WINS, ['x', 'x', 'x',
                                          'o', 'x', 'x',
                                          ' ', 'o', 'o'])

        self.assert_outcome(Game.O_WINS, ['x', ' ', ' ',
                                          'o', 'o', 'o',
                                          ' ', 'x', 'x'])

        self.assert_outcome(Game.X_WINS, ['o', ' ', ' ',
                                          ' ', 'o', 'o',
                                          'x', 'x', 'x'])

    def test_win_by_column(self):
        self.assert_outcome(Game.X_WINS, ['x', 'x', 'o',
                                          'o', 'x', 'x',
                                          ' ', 'x', 'o'])

        self.assert_outcome(Game.O_WINS, ['x', 'o', ' ',
                                          'o', 'o', 'x',
                                          ' ', 'o', 'x'])

        self.assert_outcome(Game.X_WINS, ['o', 'x', ' ',
                                          ' ', 'x', 'o',
                                          'x', 'x', 'o'])

    def test_win_by_diagonal(self):
        self.assert_outcome(Game.X_WINS, ['x', 'o', 'x',
                                          'o', 'x', 'o',
                                          'o', 'o', 'x'])

        self.assert_outcome(Game.O_WINS, ['x', ' ', 'o',
                                          'x', 'o', 'o',
                                          'o', 'x', 'x'])

    def test_tie_and_in_progress_outcome(self):
        self.assert_outcome(Game.TIE, ['o', 'o', 'x',
                                       'x', 'x', 'o',
                                       'o', 'x', 'o'])

        self.assert_outcome(Game.IN_PROGRESS, ['o', 'x', ' ',
                                               ' ', 'o', 'o',
                                               'x', ' ', 'x'])

        self.assert_outcome(Game.IN_PROGRESS, ['o', ' ', 'o',
                                               'x', 'x', 'o',
                                               'x', 'o', 'x'])

    def test_few_moves(self):
        game = Game()
        game.play(1)
        game.play(2)
        game.play(3)

        self.assertFalse(game.valid_move(2))
        self.assertEqual(game.at(1), game.X)
        self.assertEqual(game.at(2), game.O)
        self.assertEqual(game.current_player(), game.O)

    def test_if_move_is_valid(self):
        game = Game()
        self.assertTrue(game.valid_move(3))
        self.assertFalse(game.valid_move(9))

    def test_play_an_invalid_move(self):
        game = Game()
        game.play(1)

        with self.assertRaises(InvalidMoveError):
            game.play(1)

    def test_invalid_move_if_game_is_over(self):
        game = Game(['x', 'o', ' ',
                     'o', 'o', 'x',
                     ' ', 'o', 'x'])
        with self.assertRaises(InvalidMoveError):
            game.play(2)

if __name__ == "__main__":
    unittest.main()
