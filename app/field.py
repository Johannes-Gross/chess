import pygame
from app.piece import Piece

class Field():
    DARK = (102, 51, 0)
    LIGHT = (255, 204, 153)
    def __init__(self, file: float, rank: float, width: float, height: float, occupying_piece: Piece = None):
        self.file = file
        self.rank = rank
        self.width = width
        self.height = height
        self.x_left = file * width
        self.y_top = rank * height
        self.color = self.DARK if (file + rank) % 2 == 0 else self.LIGHT
        self.occupying_piece = occupying_piece
        self.rect = pygame.Rect(self.x_left, self.y_top, self.width, self.height)
    
    def draw(self, screen) -> None:
        pygame.draw.rect(screen, self.color, self.rect)

        if self.occupying_piece is not None:
            self.occupying_piece.draw(screen, self.x_left, self.y_top)


