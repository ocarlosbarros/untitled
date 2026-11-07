import pygame

from screen import Screen
from state_manager import StateManager
from settings.general_settings import WIDTH, HEIGHT

pygame.init()

# Screen config
BGCOLOR_MENU = (77,77,77)
BGCOLOR_GAMEPLAY = (0, 0, 0)

screen = Screen("Untitled Game", (WIDTH, HEIGHT))

#State Manager
state_manager = StateManager(screen)

left_mouse_button = 1

running = True
while running:
    
    state_manager.draw()

    pygame.display.update()
    
    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        state_manager.update(events) 
