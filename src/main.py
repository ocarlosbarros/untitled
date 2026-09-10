import pygame
from screen import Screen
from state_manager import StateManager

pygame.init()

# Screen config
HD_RESOLUTION = (1280, 720)
BGCOLOR_MENU = (77,77,77)
BGCOLOR_GAMEPLAY = (0, 0, 0)

screen = Screen("Untitled Game", HD_RESOLUTION)

#State Manager
state_manager = StateManager(screen)


left_mouse_button = 1

running = True
while running:
    
    state_manager.draw()

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == left_mouse_button:
                state_manager.update() 
