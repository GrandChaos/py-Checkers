import pygame

from .constants import SQUARE_SIZE, CROWN, GREEN, BLUE


class Piece:
    PADDING = SQUARE_SIZE * 0.20  # % от размера квадрата
    OUTLINE = 2

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        self.selected = False

        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def make_king(self):
        self.king = True

    def set_selected(self, selected):
        self.selected = selected

    def draw(self, win):
        radius = SQUARE_SIZE // 2 - self.PADDING
        if not self.selected:
            pygame.draw.circle(win, BLUE, (self.x, self.y), radius + self.OUTLINE)
        else:
            pygame.draw.circle(win, GREEN, (self.x, self.y), radius + self.OUTLINE)
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)
        if self.king:
            win.blit(CROWN, (self.x - CROWN.get_width()//2,
                             self.y - CROWN.get_height()//2))

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()

    def __repr__(self):  # Representation
        return str(self.color)
