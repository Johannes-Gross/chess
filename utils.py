import pygame
from app.board import Board

def draw_frame(screen: pygame.Surface, board: Board):
    screen.fill("white")
    board.draw(screen)
    pygame.display.update()
