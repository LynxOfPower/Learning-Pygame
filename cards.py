import pygame

class firstCard:
    def __init__(self):
        self.position = pygame.Vector2()
        self.position.xy = 675, 25
        self.sprite = pygame.image.load("data/gfx/card1X3.png")