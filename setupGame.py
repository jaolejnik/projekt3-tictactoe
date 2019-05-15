import pygame

'''
File to store some utility functions and global variables.
'''

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
    '''
    Function that returns markers, 'o' if it's
    players turn, 'x' if not.
    '''
    return 'o' if players_turn else 'x'


def resize_sprite(sprite, board_size):
    '''
    Resizes a given sprite using a size of a board as scale.
    '''
    sprite_rect = sprite.get_rect()
    sprite = pygame.transform.scale(sprite, (int(3 / board_size * sprite_rect.width), int(3 / board_size * sprite_rect.height)))
    return sprite


def text_objects(text, font, color):
    '''
    Utility function for easier creation of pygame text objects.
    '''
    text_surface = font.render(text, True, color)
    return text_surface, text_surface.get_rect()


def display_message(font_type, size, message, color, pos):
    '''
    Utility function for displaying a text in the display window.
    '''
    text = pygame.font.Font(font_type, size)
    text_surf, text_rect = text_objects(message, text, color)
    text_rect.center = pos
    display_window.blit(text_surf, text_rect)


def display_message_stroke(font_type, size, message, color, pos, s_color, stroke):
    '''
    Creates a message with an outline of given color.
    '''
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
    '''
    Utility function for easier creation of buttons.
    '''
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