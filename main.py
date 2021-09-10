import pygame
from pygame.math import Vector2
from pygame.locals import *
from tiles import GridTiles
from cards import firstCard

pygame.init()

screen_width = 800
screen_height = 800

screen = pygame.display.set_mode([screen_width, screen_height]) # Drawing Window

# Initiate Sprites
tile = GridTiles()
cardOne = firstCard()


running = True
while running:

    planting = False

    ## Get mouse position ##
    mouseX, mouseY = pygame.mouse.get_pos()

    # Screen fill color
    screen.fill((37, 36, 37))

    # Draw the card to the screen
    screen.blit(cardOne.sprite, cardOne.position)

    # Create the grid.
    screen.blit(tile.sprite, (100, 200))
    xPos, yPos = 100, 200
    for grid in range(1, 9):
        if (grid % 3 == 0):
            yPos += 175
            xPos = 100
        else:
            xPos += 175 
        screen.blit(tile.sprite, (xPos, yPos))

    ## EVENT HANDLER ##
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if mouseX >= cardOne.position[0] and mouseY >= cardOne.position[1] and mouseX <= cardOne.position[0] + tile.sprite.get_width() and mouseY <= cardOne.position[1] + tile.sprite.get_width():
                planting = True
                print("Planting mode on. planting = " + str(planting))

    pygame.display.flip()

pygame.quit()

# This has been coded by Isaiah Durey
# If it's coded badly, to bad, get rekt nerd.
# Just kidding, I'm sorry D: