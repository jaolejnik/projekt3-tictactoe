from setupGame import *


class Board:
    def __init__(self, size=3, win_condition=3):
        self.size = size
        self.win_condition = win_condition
        self.box_size = WIDTH / (1.1 * self.size + 0.1)
        self.gap_size = 0.1 * self.box_size
        self.markers = [[None for x in range(self.size)] for y in range(self.size)]
        self.players_turn = True
        self.winner = None
        '''
        Sizes of gaps and boxes are calculated from this equation:
            { WIDTH( or HEIGHT) = BOARD_SIZE * (FIELD_SIZE + GAP_SIZE)
            { GAP_SIZE = 0.1 * FIELD_SIZE
        '''

    def draw_grid(self):
        display_window.fill(DARK_GRAY)
        x = self.gap_size
        for i in range(self.size):
            y = self.gap_size
            for j in range(self.size):
                pygame.draw.rect(display_window, GRAY, [x, y, self.box_size, self.box_size])
                y += self.gap_size + self.box_size
            x += self.gap_size + self.box_size

    def draw_markers(self):
        for x in range(self.size):
            for y in range(self.size):
                marker = self.markers[x][y]
                if not marker:
                    continue
                center_x = self.gap_size + x * (self.gap_size + self.box_size)
                center_y = self.gap_size + y * (self.gap_size + self.box_size)
                display_window.blit(marker, (center_x, center_y))

    def marker_clicked(self, player_mark):
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()
        x = self.gap_size
        for i in range(self.size):
            y = self.gap_size
            for j in range(self.size):
                if not self.markers[i][j]:
                    if x < mouse_pos[0] < x + self.box_size and y < mouse_pos[1] < y + self.box_size:
                        display_window.blit(player_mark, (x, y))
                        if mouse_click[0] == 1:
                            self.markers[i][j] = player_mark
                            self.check_if_end(player_mark)
                            self.players_turn = not self.players_turn
                y += self.gap_size + self.box_size
            x += self.gap_size + self.box_size

    def draw(self):
        self.draw_grid()
        self.draw_markers()

    def player_move(self, player_mark):
        self.draw()
        self.marker_clicked(player_mark)

    def check_cols(self, seq):
        for col in self.markers:
            for i in range(len(col) - len(seq) + 1):
                if seq == col[i:i+len(seq)]:
                    return True

    def check_rows(self, seq):
        for y in range(self.size):
            row = [self.markers[x][y] for x in range(self.size)]
            for i in range(len(row) - len(seq) + 1):
                if seq == row[i:i+len(seq)]:
                    return True

    def check_diag(self, seq):
        # checking the main diagonal (from the top left to the bottom right corner)
        #   first half
        row = 0
        while row < self.size:
            x = self.size - 1
            y = row
            diagonal = []
            while y >= 0:
                # print('X,Y', (x,y))
                diagonal.append(self.markers[x][y])
                x -= 1
                y -= 1
            if len(diagonal) >= self.win_condition:
                for i in range(len(diagonal) - len(seq) + 1):
                    # print('diag', diagonal[i:i + len(seq)])
                    if seq == diagonal[i:i + len(seq)]:
                        # print(1)
                        return True
            row += 1
        #   second half
        col = self.size - 1 - 1
        while col > 0:
            x = col
            y = self.size - 1
            diagonal = []
            while x > 0:
                diagonal.append(self.markers[x][y])
                x -= 1
                y -= 1
            if len(diagonal) >= self.win_condition:
                for i in range(len(diagonal) - len(seq) + 1):
                    if seq == diagonal[i:i + len(seq)]:
                        # print(2)
                        return True
            col -= 1

        # checking antidiagonal (from the top right to the bottom left corner)
        #   first half
        row = 0
        while row < self.size:
            x = 0
            y = row
            diagonal = []
            while y >= 0:
                diagonal.append(self.markers[x][y])
                x += 1
                y -= 1
            if len(diagonal) >= self.win_condition:
                for i in range(len(diagonal) - len(seq) + 1):
                    if seq == diagonal[i:i+len(seq)]:
                        # print(3)
                        return True
            row += 1
        #   second half
        col = 1
        while col < self.size:
            x = col
            y = self.size - 1
            diagonal = []
            while x <= self.size - 1:
                diagonal.append(self.markers[x][y])
                x += 1
                y -= 1
            if len(diagonal) >= self.win_condition:
                for i in range(len(diagonal) - len(seq) + 1):
                    if seq == diagonal[i:i + len(seq)]:
                        # print(4)
                        return True
            col += 1

    def check_win(self, player_mark):
        win = [player_mark] * self.win_condition
        return self.check_rows(win) or self.check_cols(win) or self.check_diag(win)

    def full(self):
        counter = 0
        for col in self.markers:
            if None in col:
                counter += 1
        return counter == 0

    def check_if_end(self, player_mark):
        if self.full():
            self.winner = 'draw'
        if self.check_win(player_mark):
            self.winner = player_mark
