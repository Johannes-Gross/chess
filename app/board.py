import pygame
from app.field import Field
from app.pieces.rook import Rook
from app.pieces.bishop import Bishop
from app.pieces.knight import Knight
from app.pieces.queen import Queen
from app.pieces.king import King
from app.pieces.pawn import Pawn

class Board():
    NUM_RANKS = 8
    NUM_FILES = 8
    INIT_POSITION = [
            ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR'], 
            ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'], 
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP'], 
            ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'], 
        ]

    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height
        self.tile_width = width / self.NUM_FILES
        self.tile_height = height / self.NUM_RANKS
        self.turn = "white"
        self.position = self._setup_board()

    def _setup_board(self) -> list[list[Field]]:
        position = [[0] * self.NUM_FILES for _ in range(self.NUM_RANKS)]
        for row in range(self.NUM_RANKS):
            for col in range(self.NUM_FILES):
                if self.INIT_POSITION[row][col] == '':
                    position[row][col] = Field(col, row, self.tile_width, self.tile_height)
                
                else:
                    if self.INIT_POSITION[row][col][1] == 'R':
                        piece = Rook(self.INIT_POSITION[row][col][0], self.tile_width, self.tile_height)
                        
                    elif self.INIT_POSITION[row][col][1] == 'N':
                        piece = Knight(self.INIT_POSITION[row][col][0], self.tile_width, self.tile_height)
                    
                    elif self.INIT_POSITION[row][col][1] == 'B':
                        piece = Bishop(self.INIT_POSITION[row][col][0], self.tile_width, self.tile_height)

                    elif self.INIT_POSITION[row][col][1] == 'Q':
                        piece = Queen(self.INIT_POSITION[row][col][0], self.tile_width, self.tile_height)
                    
                    elif self.INIT_POSITION[row][col][1] == 'K':
                        piece = King(self.INIT_POSITION[row][col][0], self.tile_width, self.tile_height)
                    
                    elif self.INIT_POSITION[row][col][1] == 'P':
                        piece = Pawn(self.INIT_POSITION[row][col][0], self.tile_width, self.tile_height)

                    position[row][col] = Field(col, row, self.width / self.NUM_FILES, self.height / self.NUM_RANKS, piece)
                        
        return position
    
    def draw(self, window) -> None:
        for row in range(self.NUM_RANKS):
            for col in range(self.NUM_FILES):
                self.position[row][col].draw(window)

        
