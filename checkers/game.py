import pygame

from checkers.board import Board
from checkers.constants import BLACK, WHITE, BLUE, SQUARE_SIZE, CAPTION


class Game:

    def __init__(self, win):
        self._init()
        self.win = win

    def update(self):
        self.board.draw(self.win)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()

    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = BLACK
        self.valid_moves = {}

    def reset(self):
        self._init()

    def select(self, row, col):
        if self.board.selected_piece is not None:
            result = self._move(row, col)
            if not result:
                # self.selected.set_selected(False)
                # self.selected = None
                self.board.selected_piece.set_selected(False)
                self.board.set_selected_piece(None)
                self.valid_moves = {}
                # self.select(row, col)

        piece = self.board.get_piece(row, col)
        if piece != 0 and piece.color == self.turn:
            # piece.set_selected(True)
            # self.selected = piece
            piece.set_selected(True)
            self.board.set_selected_piece(piece)
            self.valid_moves = self.board.get_valid_moves(piece)
            return True

        return False

    def _move(self, row, col):
        # piece = self.board.get_piece(row, col)
        piece = self.board.get_selected_piece()
        if self.board.get_piece(row, col) == 0 and (row, col) in self.valid_moves:
            self.board.move(piece, row, col)
            skipped = self.valid_moves[(row, col)]
            if skipped:
                self.board.remove(skipped)
            self.change_turn()
        else:
            return False
        return True

    def change_turn(self):
        self.valid_moves = {}
        # self.selected = None
        if self.turn == BLACK:
            self.turn = WHITE
            color = "White"
        else:
            self.turn = BLACK
            color = "Black"

        caption = CAPTION % color
        pygame.display.set_caption(caption)

    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, BLUE, (col * SQUARE_SIZE + SQUARE_SIZE // 2,
                                                row * SQUARE_SIZE + SQUARE_SIZE // 2),
                               SQUARE_SIZE // 5)

    def winner(self):
        return self.board.winner()

    def get_board(self):
        return self.board

    def AI_move(self, board):
        self.board = board
        self.change_turn()
