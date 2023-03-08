import pygame
import os

class Piece():
    
    def __init__(self, color: str, tile_width: float, tile_heigth: float, img_path) -> None:
        self.color = color
        self.img = pygame.transform.scale(pygame.image.load(os.getcwd() + img_path), (tile_width - 20, tile_heigth - 20))
    
    def draw(self, window, x, y):
        window.blit(self.img, (x + 10, y + 10))


    