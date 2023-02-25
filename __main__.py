import pygame
from utils import draw_frame
from app.board import Board

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
board = Board(SCREEN_WIDTH, SCREEN_HEIGHT)

running = True

# Game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

        elif event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mx, my = pygame.mouse.get_pos()
                # pass mouse click to board
    
    draw_frame(screen, board)
    

pygame.quit()



