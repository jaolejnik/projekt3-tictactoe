from setupGame import *
import copy

INF = 100


class Ai:
    def __init__(self, board):
        self.board = board

    def make_move(self, player_marker):
        print('ROBIE RUCH')
        print('-----------')
        move = self.best_move()
        self.board.markers[move[0]][move[1]] = player_marker
        self.board.draw()
        self.board.check_if_end(player_marker)
        self.board.players_turn = not self.board.players_turn

    def check_possible_moves(self):
        available_moves = []
        for x in range(self.board.size):
            for y in range(self.board.size):
                if self.board.markers[x][y] is None:
                    available_moves.append((x, y))
        return available_moves

    def best_move(self):
        best_value = -INF
        best_move = None
        available_moves = self.check_possible_moves()

        for move in available_moves:
            self.board.markers[move[0]][move[1]] = get_marker(self.board.players_turn)
            move_value = self.minimax(3, False, -INF, INF)
            self.board.markers[move[0]][move[1]] = None
            print('MOVE VALUE', move_value)
            if move_value > best_value:
                best_value = move_value
                best_move = move

        return best_move

    def minimax(self, depth, max_player, alpha, beta):
        print('TERAZ GRACZ', get_marker(max_player))
        self.board.print_board()

        if self.board.check_win(get_marker(max_player)):
            return -10 if max_player else 10

        if self.board.full() or depth == 0:
            return 0

        available_moves = self.check_possible_moves()
        print('MOZE SIE RUSZYC:', available_moves)

        if max_player:
            max_eval = -INF
            for move in available_moves:
                self.board.markers[move[0]][move[1]] = get_marker(False)
                eval = self.minimax(depth - 1, False, alpha, beta)
                self.board.markers[move[0]][move[1]] = None
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return max_eval

        else:
            #print('TERAZ GRACZ MIN', get_marker(not max_player))
            min_eval = INF
            for move in available_moves:
                self.board.markers[move[0]][move[1]] = get_marker(True)
                eval = self.minimax(depth - 1, True, alpha, beta)
                self.board.markers[move[0]][move[1]] = None
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
                #print('MIN EVAL', min_eval)
            return min_eval

