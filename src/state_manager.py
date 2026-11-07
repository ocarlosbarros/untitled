import pygame

from states.gameplay import Gameplay
from states.main_menu import MainMenu
from states.options import Options

class StateManager:

    def __init__(self, screen):
        self.screen = screen
        self.currentState = MainMenu(screen)

    
    def setState(self, new_state):
        self.currentState = new_state

    def update(self, events):

        transition = self.currentState.update(events)
        
        self.setTransition(transition)
        
        
    def draw(self):
        self.currentState.draw()

    
    def setTransition(self, transition):

        match transition:
            case "gameplay":
                self.currentState = Gameplay(self.screen)
                return 
            case "options":
                self.currentState = Options(self.screen)

            case "quit":
                pygame.quit()
                return
            # None é uma resposta esperada para manter o estado atual. Cada método update de cada estado retorna None
            case None:
                return
            # Caso acontece uma operação não prevista nada acontece
            case _:
                return