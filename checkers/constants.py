import pygame

WIDTH, HEIGHT = 400, 400
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS

# RGB
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
DARK_GRAY = (64, 64, 64)
LIGHT_GRAY = (192, 192, 195)
BLUE = (64, 64, 255)
GREEN = (0, 255, 0)

CROWN = pygame.transform.scale(pygame.image.load('checkers/assets/crown.png'), (SQUARE_SIZE//3, SQUARE_SIZE//4))

# Отслеживание направления доски
DOWN = 1
UP = -1

CAPTION = "py-Checkers: It's %s player's turn"
