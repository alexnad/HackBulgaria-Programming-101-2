import unittest
from game import Game
from ai import AI


class Test_Intelligence(unittest.TestCase):
    def assertOposites(self, expected_oposite, given_oposite, board=None):
        ai = AI(board)
        ai.play(given_oposite)
        self.assertEqual(ai.at(expected_oposite), Game.O)

    def assertSafeMove(self, expected, board):
        ai = AI(board)
        self.assertEqual(expected, ai.safe_move())

    def test_opponent_next_move_is_winning(self):
        ai = AI(['x', ' ', 'o',
                 ' ', ' ', ' ',
                 ' ', ' ', 'x'])

        self.assertEqual(ai.opponent_winning(), 4)
        self.assertEqual(ai.play(4), Game.X_WINS)

    def test_ai_winning(self):
        ai = AI(['o', ' ', 'x',
                 ' ', ' ', ' ',
                 ' ', ' ', 'o'])

        self.assertEqual(ai.winning(), 4)
        self.assertEqual(ai.play(1), Game.O_WINS)

    def test_take_center_if_possible(self):
        ai = AI([' ', 'x', ' ',
                 ' ', ' ', ' ',
                 ' ', ' ', ' '])
        self.assertEqual(ai.safe_move(), 4)

    def test_take_corner_if_posible(self):
        self.assertSafeMove(0, [' ', ' ', ' ',
                                ' ', 'x', ' ',
                                ' ', ' ', ' '])
        self.assertSafeMove(2, ['x', ' ', ' ',
                                ' ', 'x', ' ',
                                ' ', ' ', 'o'])

    def test_take_oposite_corner_if_posible(self):
        self.assertOposites(AI.MAIN_OPOSITES[0], AI.MAIN_OPOSITES[1])
        self.assertOposites(AI.SECONDARY_OPOSITES[1], AI.SECONDARY_OPOSITES[0])

    def test_take_last_empty_squares_if_center_and_corners_are_taken(self):
        self.assertSafeMove(1, ['x', ' ', 'o',
                                'o', 'x', 'x',
                                'x', ' ', 'o'])

    def test_ai_play_a_game(self):
        ai = AI()
        self.assertEqual(ai.play(1), Game.IN_PROGRESS)
        self.assertEqual(ai.at(4), Game.O)
        self.assertEqual(ai.play(8), Game.IN_PROGRESS)
        self.assertEqual(ai.at(0), Game.O)
        self.assertEqual(ai.play(2), Game.IN_PROGRESS)
        self.assertEqual(ai.at(5), Game.O)
        self.assertEqual(ai.play(6), Game.O_WINS)


if __name__ == "__main__":
    unittest.main()