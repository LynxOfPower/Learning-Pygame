#I guess we're learning pygame. let's see how this goes!


# REMINDERS FOR NEXT STREAM:
# - Get sprites for grid [X] (This is pretty much started, the question is if I'm doing it right)
# - Get a hover sprite up for grid sprites. (Possibly done with a def hover() in an external file?) []
# - work on UI on the right hand of the screen []


import pygame
import random

# print(pygame.ver)

pygame.init()

screen_width = 800
screen_height = 800

screen = pygame.display.set_mode([screen_width, screen_height]) # Drawing Window

## CLASSES ##
class hover():
    def __init__():
        print("TO BE IMPLEMENTED")

    def isHovering():
        print("TO BE IMPLEMENTED")

## SPRITES ##
class GridTiles(pygame.sprite.Sprite):
    def __init__(self):
        super(GridTiles, self).__init__()
        self.surf = pygame.Surface((32, 32))
        self.image = pygame.image.load("data/gfx/soilX5.png")

tile = GridTiles() # initialize the GridTiles sprite in this variable.


running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((37, 36, 37))

    # #TOP ROW
    screen.blit(tile.image, (100, 200))
    screen.blit(tile.image, (275, 200))
    screen.blit(tile.image, (450, 200))

    # #MIDDLE ROW
    screen.blit(tile.image, (100, 375))
    screen.blit(tile.image, (275, 375))
    screen.blit(tile.image, (450, 375))

    # #BOTTOM ROW
    screen.blit(tile.image, (100, 550))
    screen.blit(tile.image, (275, 550))
    screen.blit(tile.image, (450, 550))

    pygame.display.flip()

pygame.quit()

# This has been coded by Isaiah Durey
# If it's coded badly, to bad, get rekt nerd.
# Just kidding, I'm sorry D: