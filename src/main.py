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

print("ANTES DO LOOP", type(state_manager.currentState).__name__)

running = True
while running:

    print("ANTES DO UPDATE", type(state_manager.currentState).__name__)

    # simula um click em novo jogo
    state_manager.update()

    print("DEPOIS DO UPDATE", type(state_manager.currentState).__name__)


    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
