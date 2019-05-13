from TicTacToe import get_marker
from copy import copy


class Ai:
    def __init__(self, board):
        self.board = board

    def make_move(self, player_marker):
        moves = self.score_moves(self.board)
        score, move = max(moves, key=lambda m: m[0])
        # print(score, move)
        # print('self.board IN MAKE MOVES', self.board)
        self.board.markers[move[0]][move[1]] = player_marker
        self.board.draw()
        self.board.check_if_end(player_marker)
        self.board.players_turn = not self.board.players_turn

    def score_moves(self, board):
        available_moves = []
        scores = []
        for x in range(board.size):
            for y in range(board.size):
                if board.markers[x][y] is None:
                    available_moves.append((x, y))

        yield 1, available_moves[0]
