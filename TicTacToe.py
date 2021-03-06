from Board import *
from AI import *


class TicTacToe:
    '''
    Class to represent a game of Tic-Tac-Toe.
    '''
    def __init__(self, size=3):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.board_size = size
        self.win_condition = size
        self.board = None
        self.solo_mode = True
        self.bot = None
        self.in_progress = False
        self.winner = None

    def reduce_size(self):
        '''
        Reduces size of the board that will be created.
        Minimal size is 3.
        '''
        if self.board_size > 3:
            self.board_size -= 1
            self.win_condition = self.board_size

    def increase_size(self):
        '''
        Increases size of the board that will be created.
        Maximum size is 10
        '''
        if self.board_size < 10:
            self.board_size += 1
            self.win_condition = self.board_size

    def reduce_condition(self):
        '''
        Reduces size of the markers sequence that will be required to win.
        Minimal size is 3.
        '''
        if self.win_condition > 3:
            self.win_condition -= 1

    def increase_condition(self):
        '''
        Increases size of the markers sequence that will be required to win.
        '''
        if self.win_condition < self.board_size:
            self.win_condition += 1

    def show_winner(self):
        '''
        Displays message that informs a player if he is victorious.
        '''
        win_screen = True
        while win_screen:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    win_screen = False

            if self.board.winner == 'o':
                display_window.blit(WIN_SCREEN, (0, 0))
            elif self.board.winner == 'x':
                display_window.blit(LOSE_SCREEN, (0, 0))
            else:
                display_window.blit(DRAW_SCREEN, (0, 0))
            pygame.display.update()

    def game_loop(self):
        '''
        Handles events during the game and runs until there is a winner or a draw.
        '''
        while self.in_progress:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.in_progress = False
            if self.solo_mode:
                if self.board.players_turn:
                    self.board.player_move(get_marker(self.board.players_turn))
                else:
                    self.bot.make_move(get_marker(self.board.players_turn))
            else:
                self.board.player_move(get_marker(self.board.players_turn))
            if self.board.winner:
                self.in_progress = False
                self.show_winner()
            pygame.display.update()
            self.clock.tick(60)

    def start_game(self):
        '''
        Initializes the board, markers and the bot and the starts the game.
        '''
        global CROSS, CIRCLE
        CROSS = pygame.image.load('sprites/x.png')
        CIRCLE = pygame.image.load('sprites/o.png')
        self.board = Board(self.board_size, self.win_condition)
        self.board.CROSS = resize_sprite(CROSS, self.board_size)
        self.board.CIRCLE = resize_sprite(CIRCLE, self.board_size)
        self.bot = Ai(self.board)
        pygame.time.delay(500)
        self.in_progress = True
        self.game_loop()

    def close(self):
        '''
        Safe close of the game.
        '''
        pygame.quit()
        quit()

    def return_mode(self):
        '''
        Returns current game mode as a string.
        '''
        if self.solo_mode:
            return '1 PLAYER'
        else:
            return '2 PLAYERS'

    def change_mode(self):
        '''
        Changes current game mode.
        '''
        self.solo_mode = not self.solo_mode


    def run(self):
        '''
        Starts the whole game. Displays a start screen, where player can change size of the board and win condition.
        '''
        start_screen = True
        while start_screen:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_KP_ENTER:
                        start_screen = False
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        quit()
            display_window.fill(DARK_GRAY)
            display_message_stroke(None, 125, 'TIC-TAC-TOE', WHITE, (WIDTH / 2, HEIGHT / 8), BLACK, 5)

            display_message_stroke(None, 60, 'Game mode', WHITE, (WIDTH / 2, HEIGHT / 4), BLACK, 3)
            button(self.return_mode(), WIDTH/2 - 75, HEIGHT/3.5, 150, 70, WHITE, LIGHT_GRAY, self.change_mode)

            display_message_stroke(None, 60, 'Size of the board', WHITE, (WIDTH / 2, HEIGHT / 2.25), BLACK, 3)
            button(str(self.board_size), WIDTH / 2 - 35, HEIGHT / 2.1, 70, 70, WHITE, WHITE)
            button('-', WIDTH / 2 - 70, HEIGHT / 2.1 + 20, 30, 30, WHITE, LIGHT_GRAY, self.reduce_size)
            button('+', WIDTH / 2 + 40, HEIGHT / 2.1 + 20, 30, 30, WHITE, LIGHT_GRAY, self.increase_size)

            display_message_stroke(None, 50, 'Amount of signs in one line to win', WHITE, (WIDTH / 2, HEIGHT / 1.6), BLACK, 3)
            button(str(self.win_condition), WIDTH / 2 - 35, HEIGHT / 1.5, 70, 70, WHITE, WHITE)
            button('-', WIDTH / 2 - 70, HEIGHT / 1.5 + 20, 30, 30, WHITE, LIGHT_GRAY, self.reduce_condition)
            button('+', WIDTH / 2 + 40, HEIGHT / 1.5 + 20, 30, 30, WHITE, LIGHT_GRAY, self.increase_condition)

            button('START', WIDTH / 4 - 75, HEIGHT / 1.2, 150, 100, WHITE, LIGHT_GRAY, self.start_game)
            button('QUIT', 3 * WIDTH / 4 - 75, HEIGHT / 1.2, 150, 100, WHITE, LIGHT_GRAY, self.close)

            pygame.display.update()



if __name__ == "__main__":
    game = TicTacToe()
    game.run()
