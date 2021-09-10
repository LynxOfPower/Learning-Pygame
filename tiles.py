import pygame

class GridTiles(pygame.sprite.Sprite):
    def __init__(self):
        super(GridTiles, self).__init__()
        self.surf = pygame.Surface((32, 32))
        self.sprite = pygame.image.load("data/gfx/soilX5.png")