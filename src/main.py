import pygame
from screens.screen import Screen

pygame.init()

# Screen config
HD_RESOLUTION = (1280, 720)
BGCOLOR_MENU = (77,77,77)
BGCOLOR_GAMEPLAY = (0, 0, 0)

screen = Screen("Untitled Game", HD_RESOLUTION)

#Screen Manager
context = 2



running = True
while running:

    if(context == 1):
        screen.show(BGCOLOR_MENU)
    else:
        screen.show(BGCOLOR_GAMEPLAY)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
