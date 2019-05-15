from setupGame import *

INF = 1000


class Ai:
    '''
    Class that represents a bot, that plays the game of Tic-Tac-Toe.
    It evaluates the board and performs the best move.
    '''
    def __init__(self, board):
        self.board = board

    def make_move(self, player_marker):
        '''
        Calls best_move() to find the best possible move and then performs it.
        '''
        display_message_stroke(None, 100, 'THINKING...', BLACK, (WIDTH/2, HEIGHT/2), WHITE, 4)
        pygame.display.update()
        move = self.best_move()
        self.board.markers[move[0]][move[1]] = player_marker
        self.board.draw()
        self.board.check_if_end(player_marker)
        self.board.players_turn = not self.board.players_turn

    def check_possible_moves(self):
        '''
        Return all available moves at the current board.
        '''
        available_moves = []
        for x in range(self.board.size):
            for y in range(self.board.size):
                if self.board.markers[x][y] is None:
                    available_moves.append((x, y))
        return available_moves

    def best_move(self):
        '''
        Finds the best move for the current state of the board
        '''
        best_value = -INF
        best_move = None
        available_moves = self.check_possible_moves()
        depth = 2 * self.board.size - self.board.win_condition

        for move in available_moves:
            self.board.markers[move[0]][move[1]] = get_marker(self.board.players_turn)
            move_value = self.minimax(depth, False, -INF, INF)
            self.board.markers[move[0]][move[1]] = None
            if move_value > best_value:
                best_value = move_value
                best_move = move

        return best_move

    def minimax(self, depth, max_player, alpha, beta):
        '''
        Performs minimax algorithm, that evaluates and finds the best moves for maximazing
        and minimazing players.
        '''
        print('TERAZ GRACZ', get_marker(max_player))
        self.board.print_board()

        if self.board.check_win(get_marker(max_player)):
            return -10 if max_player else 10

        if self.board.full() or depth == 0:
            return 0


        available_moves = self.check_possible_moves()

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
            min_eval = INF
            for move in available_moves:
                self.board.markers[move[0]][move[1]] = get_marker(True)
                eval = self.minimax(depth - 1, True, alpha, beta)
                self.board.markers[move[0]][move[1]] = None
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return min_eval

