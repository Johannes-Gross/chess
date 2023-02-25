import pygame
from app.field import Field

class Board():
    NUM_RANKS = 8
    NUM_FILES = 8
    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height
    
    def draw(self, screen) -> None:
        for col in range(self.NUM_FILES):
            for row in range(self.NUM_RANKS):
                Field(col, row, self.width / self.NUM_FILES, self.height / self.NUM_RANKS).draw(screen)

        
