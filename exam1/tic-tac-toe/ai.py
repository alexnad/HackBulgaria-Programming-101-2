from game import Game, InvalidMoveError


class AI:
    MAIN_OPOSITES = (0, 8)
    SECONDARY_OPOSITES = (2, 6)

    def __init__(self, board=None):
        self._game = Game(board)

    def current_state(self):
        return self._game.state_of_board()

    def at(self, position):
        return self._game.at(position)

    def outcome(self):
        return self._game.calculate_outcome()

    def valid_move(self, position):
        return(self._game.valid_move(position))

    def winning(self):
        for i in range(9):
            if self._game.valid_move(i):
                test_game = Game(self._game.state_of_board())
                test_game.change_player()
                test_game.play(i)
                if test_game.calculate_outcome() == Game.O_WINS:
                    return i

    def opponent_winning(self):
        for i in range(9):
            if self._game.valid_move(i):
                test_game = Game(self._game.state_of_board())
                test_game.play(i)
                if test_game.calculate_outcome() == Game.X_WINS:
                    return i

    def safe_move(self):
        center_square = 4
        corners = [0, 2, 6, 8]
        oposite_corners = [self.MAIN_OPOSITES, self.SECONDARY_OPOSITES]
        for oposites in oposite_corners:
            if self._game.at(oposites[0]) == Game.X and self._game.valid_move(oposites[1]):
                return oposites[1]
            elif self._game.at(oposites[1]) == Game.X and self._game.valid_move(oposites[0]):
                return oposites[0]

        if self._game.valid_move(center_square):
            return center_square

        for corner in corners:
            if self._game.valid_move(corner):
                return corner

        for square in range(9):
            if self._game.valid_move(square):
                return square

    def play(self, opponent_position):
        if not self._game.valid_move(opponent_position):
            raise InvalidMoveError

        self._game.play(opponent_position)
        if self._game.calculate_outcome() == Game.IN_PROGRESS:
            if self.winning():
                position = self.winning()
                self._game.play(position)

            elif self.opponent_winning():
                position = self.opponent_winning()
                self._game.play(position)

            else:
                position = self.safe_move()
                self._game.play(position)
        return self._game.calculate_outcome()
