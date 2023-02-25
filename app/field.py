import pygame

class Field():
    DARK = (102, 51, 0)
    LIGHT = (255, 247, 230)
    def __init__(self, file: float, rank: float, width: float, height: float):
        self.file = file
        self.rank = rank
        self.width = width
        self.height = height
        self.x_left = file* width
        self.y_top = rank * height
        self.color = self.DARK if (file + rank) % 2 == 0 else self.LIGHT
        self.occupying_piece = None
        self.rect = pygame.Rect(self.x_left, self.y_top, self.width, self.height)
    
    def draw(self, screen) -> None:
        # pygame.draw.rect(screen, self.color, )
        pygame.draw.rect(screen, self.color, self.rect)

        if self.occupying_piece is not None:
            # draw also the occupying piece
            pass


