import os
from game import Game  # , InvalidMoveError
from ai import AI


BOARD = """
        0 | 1 | 2
        ---------
        3 | 4 | 5
        ---------
        6 | 7 | 8
"""


class CLI:
    def __init__(self):
        self._game = AI()

    def play(self):
        outcome = Game.IN_PROGRESS
        while outcome == Game.IN_PROGRESS:
            self._draw_board()
            move = None
            while move is None:
                move = self._get_move()

            outcome = self._game.play(move)
            self._clear()
        self._announce_outcome(outcome)

    def _announce_outcome(self, outcome):
        if outcome == Game.X_WINS:
            print('Congratulations! You won!')
        if outcome == Game.O_WINS:
            print('Sorry, you loose. Better luck next time')
        else:
            print('It\'a a tie')

    def _get_move(self):
        try:
            position = int(input('Enter your move>'))
            if self._game.valid_move(position):
                return position
            print("Wrong input!")
        except ValueError:
            print("Wrong input!")
            return None

    def _clear(self):
        os.system('clear')

    def _draw_board(self):
        state = self._game.current_state()
        symbols = {str(place): symbol for place, symbol in enumerate(state)}
        print(self._fill_board(symbols))

    def _fill_board(self, symbols):
        new_board = []
        for character in BOARD:
            if character in symbols and symbols[character] != Game.EMPTY:
                new_board.append(symbols[character])
            else:
                new_board.append(character)

        return "".join(new_board)

CLI().play()
