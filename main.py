import pygame

from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, CAPTION, WHITE
from checkers.game import Game
from minimax_algorithm.algorithm import minimax

FPS = 60

pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(CAPTION % "Black")


def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col


def draw_text(screen, text):
    font = pygame.font.SysFont("Arial", 27, True, False)
    text_object = font.render(text, True, pygame.Color('Orange'))
    text_location = pygame.Rect(0, 0, WIDTH, HEIGHT).move(WIDTH / 2 - text_object.get_width() / 2,
                                                          HEIGHT / 2 - text_object.get_height() / 2)
    screen.blit(text_object, text_location)
    text_object = font.render(text, True, pygame.Color("Blue"))
    screen.blit(text_object, text_location.move(-1, -1))
    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    clock.tick(FPS)
    game = Game(WIN)

    run = True
    begin = False
    AI = True
    depth = 3

    game.update()

    while run:
        if AI and game.turn == WHITE:
            value, new_board = minimax(game.get_board(), depth, WHITE, game)
            game.AI_move(new_board)
            pygame.time.delay(300)

        if game.winner() is not None:
            # print(f'Game winner: {game.winner()}')
            game.update()
            if game.winner() == WHITE:
                draw_text(WIN, 'WHITE WINS')
            else:
                draw_text(WIN, 'BLACK WINS')
            begin = False
            pygame.time.delay(2000)
            game.update()
            game = Game(WIN)

        for event in pygame.event.get():
            if not begin:
                draw_text(WIN, 'press: 1 - two players, 2 - computer')
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        AI = False
                        begin = True
                    if event.key == pygame.K_2:
                        AI = True
                        begin = True

            if event.type == pygame.QUIT:
                run = False

            if begin and event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)

            if begin and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    begin = False
                    game = Game(WIN)
                    game.update()

        if begin:
            game.update()

    pygame.quit()


main()
