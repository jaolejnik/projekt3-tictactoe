import pygame

# ------------CONSTANTS------------
# Screen resolution
WIDTH = 800
HEIGHT = 800

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (115, 115, 115,)
LIGHT_GRAY = (225, 225, 225)
DARK_GRAY = (75, 75, 75)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# sprites
CROSS = pygame.image.load('sprites/x.png')
CIRCLE = pygame.image.load('sprites/o.png')
WIN_SCREEN = pygame.image.load('sprites/win.png')
LOSE_SCREEN = pygame.image.load('sprites/lose.png')
DRAW_SCREEN = pygame.image.load('sprites/draw.png')
# --------------------------------

#

# Set resolution and caption
display_window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic-Tac-Toe')


def get_marker(players_turn):
    return 'o' if players_turn else 'x'


def resize_sprite(sprite, board_size):
    sprite_rect = sprite.get_rect()
    sprite = pygame.transform.scale(sprite, (int(3 / board_size * sprite_rect.width), int(3 / board_size * sprite_rect.height)))
    return sprite


def text_objects(text, font, color):
    text_surface = font.render(text, True, color)
    return text_surface, text_surface.get_rect()


def display_message(font_type, size, message, color, pos):
    text = pygame.font.Font(font_type, size)
    text_surf, text_rect = text_objects(message, text, color)
    text_rect.center = pos
    display_window.blit(text_surf, text_rect)


def display_message_stroke(font_type, size, message, color, pos, s_color, stroke):
    display_message(font_type, size, message, s_color, (pos[0] + stroke, pos[1]))
    display_message(font_type, size, message, s_color, (pos[0] - stroke, pos[1]))
    display_message(font_type, size, message, s_color, (pos[0], pos[1] + stroke))
    display_message(font_type, size, message, s_color, (pos[0], pos[1] - stroke))
    display_message(font_type, size, message, s_color, (pos[0] + stroke, pos[1] - stroke))
    display_message(font_type, size, message, s_color, (pos[0] + stroke, pos[1] + stroke))
    display_message(font_type, size, message, s_color, (pos[0] - stroke, pos[1] - stroke))
    display_message(font_type, size, message, s_color, (pos[0] - stroke, pos[1] + stroke))
    display_message(font_type, size, message, color, pos)


def button(message, pos_x, pos_y, width, height, inactive_color, active_color, action=None):
    mouse_pos = pygame.mouse.get_pos()
    mouse_clicked = pygame.mouse.get_pressed()

    if pos_x < mouse_pos[0] < pos_x + width and pos_y < mouse_pos[1] < pos_y + height:
        pygame.draw.rect(display_window, active_color, ((pos_x, pos_y), (width, height)))
        if mouse_clicked[0] == 1 and action is not None:
            pygame.time.delay(50)
            action()
    else:
        pygame.draw.rect(display_window, inactive_color, ((pos_x, pos_y), (width, height)))
    display_message(None, int(height/2), message, BLACK, (pos_x + width/2, pos_y + height/2))


def check_cols(seq, markers):
        for col in markers:
            for i in range(len(col) - len(seq) + 1):
                if seq == col[i:i+len(seq)]:
                    return True


def check_rows(seq, markers):
    for y in range(len(markers)):
        row = [markers[x][y] for x in range(len(markers))]
        for i in range(len(row) - len(seq) + 1):
            if seq == row[i:i+len(seq)]:
                return True


def check_diag(seq, markers):
    # checking the main diagonal (from the top left to the bottom right corner)
    #   first half
    size = len(markers)
    row = 0
    while row < size:
        x = size - 1
        y = row
        diagonal = []
        while y >= 0:
            # print('X,Y', (x,y))
            diagonal.append(markers[x][y])
            x -= 1
            y -= 1
        if len(diagonal) >= len(seq):
            for i in range(len(diagonal) - len(seq) + 1):
                # print('diag', diagonal[i:i + len(seq)])
                if seq == diagonal[i:i + len(seq)]:
                    # print(1)
                    return True
        row += 1
    #   second half
    col = size - 1 - 1
    while col > 0:
        x = col
        y = size - 1
        diagonal = []
        while x > 0:
            diagonal.append(markers[x][y])
            x -= 1
            y -= 1
        if len(diagonal) >= len(seq):
            for i in range(len(diagonal) - len(seq) + 1):
                if seq == diagonal[i:i + len(seq)]:
                    # print(2)
                    return True
        col -= 1

    # checking antidiagonal (from the top right to the bottom left corner)
    #   first half
    row = 0
    while row < size:
        x = 0
        y = row
        diagonal = []
        while y >= 0:
            diagonal.append(markers[x][y])
            x += 1
            y -= 1
        if len(diagonal) >= len(seq):
            for i in range(len(diagonal) - len(seq) + 1):
                if seq == diagonal[i:i+len(seq)]:
                    # print(3)
                    return True
        row += 1
    #   second half
    col = 1
    while col < size:
        x = col
        y = size - 1
        diagonal = []
        while x <= size - 1:
            diagonal.append(markers[x][y])
            x += 1
            y -= 1
        if len(diagonal) >= len(seq):
            for i in range(len(diagonal) - len(seq) + 1):
                if seq == diagonal[i:i + len(seq)]:
                    # print(4)
                    return True
        col += 1


def check_win(markers, player_mark, win_condition):
    win = [player_mark] * win_condition
    return check_rows(win, markers) or check_cols(win, markers) or check_diag(win, markers)

