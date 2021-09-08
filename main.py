import pygame
from tiles import GridTiles
from cards import firstCard

# print(pygame.ver)

pygame.init()

screen_width = 800
screen_height = 800

screen = pygame.display.set_mode([screen_width, screen_height]) # Drawing Window

tile = GridTiles() # initialize the GridTiles sprite in this variable.
cardOne = firstCard()

running = True
while running:

    ## Get mouse position ##
    mouseX, mouseY = pygame.mouse.get_pos()

    # Screen fill color
    screen.fill((37, 36, 37))

    # Draw the card to the screen
    screen.blit(cardOne.mainSprite, cardOne.position)

    #TOP ROW
    screen.blit(tile.image, (100, 200))
    screen.blit(tile.image, (275, 200))
    screen.blit(tile.image, (450, 200))

    #MIDDLE ROW
    screen.blit(tile.image, (100, 375))
    screen.blit(tile.image, (275, 375))
    screen.blit(tile.image, (450, 375))

    #BOTTOM ROW
    screen.blit(tile.image, (100, 550))
    screen.blit(tile.image, (275, 550))
    screen.blit(tile.image, (450, 550))

    ## EVENT HANDLER ##
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if mouseX >= cardOne.position[0] and mouseY >= cardOne.position[1] and mouseX <= cardOne.position[0] + 96 and mouseY <= cardOne.position[1] + 96:
                print("Mouse is here!")
                cardOne.position = mouseX / 2, mouseY / 2
    pygame.display.flip()

pygame.quit()

# This has been coded by Isaiah Durey
# If it's coded badly, to bad, get rekt nerd.
# Just kidding, I'm sorry D: