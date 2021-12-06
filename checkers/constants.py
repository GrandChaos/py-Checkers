import pygame

WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS

# rgb
DARK_GRAY = (92, 92, 92)
LIGHT_GRAY = (192, 192, 192)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (192, 192, 255)
GREY = (128, 128, 128)

CROWN = pygame.transform.scale(pygame.image.load('checkers/assets/crown.png'), (44, 25))
