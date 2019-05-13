from TicTacToe import players_mark
from copy import copy


class Ai:
    def __init__(self, board):
        self.board = board

    def make_move(self, player_marker):
        moves = self.score_moves(self.board)
        score, move = max(moves, key=lambda m: m[0])
        print(score, move)
        # print('self.board IN MAKE MOVES', self.board)
        self.board.markers[move[0]][move[1]] = player_marker
        self.board.draw()
        if self.board.full():
            self.board.winner = 'draw'
        print(self.board.check_win(player_marker))
        if self.board.check_win(player_marker):
            self.board.winner = player_marker
        self.board.players_turn = not self.board.players_turn

    def score_moves(self, board):
        # print('BOARD IN SCORE MOVES', board)
        available_moves = []
        for x in range(board.size):
            for y in range(board.size):
                if board.markers[x][y] is None:
                    available_moves.append((x, y))

        for move in available_moves:
            possible_setting = copy(board)
            possible_setting.markers[move[0]][move[1]] = players_mark(possible_setting.players_turn)

            if possible_setting.check_win(players_mark(possible_setting.players_turn)):
                score = -1 if possible_setting.players_turn else 1
                yield score, move
                continue
            '''
            if possible_setting.full():
                yield 1, move
                continue
            '''
            possible_setting.players_turn = not possible_setting.players_turn
            next_moves = list(self.score_moves(possible_setting))
            if not next_moves:
                yield 0, move
                continue

            scores, moves = zip(*next_moves)
            yield sum(scores), move
