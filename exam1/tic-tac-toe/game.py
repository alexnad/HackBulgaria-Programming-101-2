class InvalidMoveError(Exception):
    pass


class Game:
    X_WINS = '<x_wins>'
    O_WINS = '<o_wins>'
    TIE = '<tie>'
    IN_PROGRESS = '<in_progress>'

    EMPTY = ' '
    X = 'x'
    O = 'o'
    EMPTY_BOARD = [EMPTY] * 9

    WINNING_LINES = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],

        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],

        [0, 4, 8],
        [2, 4, 6]
    ]

    def __init__(self, board=None):
        self._board = board or self.EMPTY_BOARD[:]
        self._player = self.X

    def state_of_board(self):
        return [square for square in self._board]

    def at(self, position):
        if position in range(9):
            return self._board[position]
        return 'Indice out of range'

    def current_player(self):
        return self._player

    def change_player(self):
        if self._player == self.X:
            self._player = self.O
        else:
            self._player = self.X

    def valid_move(self, position):
        return position in range(9) and \
            self._board[position] == self.EMPTY and\
            self.calculate_outcome() == self.IN_PROGRESS

    def find_if_winnig(self, winnig_line):
        previous = self._board[winnig_line[0]]
        for position in winnig_line:
            empty_square = self._board[position] == self.EMPTY
            if empty_square or self._board[position] != previous:
                return False
        return previous

    def _winnig_player(self, winner):
        if winner == self.X:
            return self.X_WINS
        else:
            return self.O_WINS

    def calculate_outcome(self):
        for line in self.WINNING_LINES:
            outcome = self.find_if_winnig(line)
            if outcome is not False:
                return self._winnig_player(outcome)

        if self.EMPTY not in self._board:
            return self.TIE

        return self.IN_PROGRESS

    def play(self, position):
        if not self.valid_move(position):
            raise InvalidMoveError('Invalid Move!')

        self._board[position] = self._player
        self.change_player()
        return self.calculate_outcome()
