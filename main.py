import sys
import pygame

from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, CAPTION, WHITE
from checkers.game import Game
from minimax_algorithm.algorithm import minimax

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(CAPTION % "Black")


def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col


def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    AI = True
    depth = 2

    while run:
        clock.tick(FPS)

        if AI and game.turn == WHITE:
            value, new_board = minimax(game.get_board(), depth, WHITE, game)
            game.AI_move(new_board)
            pygame.time.delay(500)

        if game.winner() is not None:
            print(f'Game winner: {game.winner()}')
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)

        game.update()


main()
