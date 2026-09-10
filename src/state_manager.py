from states.gameplay import Gameplay
from states.main_menu import MainMenu


class StateManager:

    def __init__(self, screen):
        self.screen = screen
        self.currentState = MainMenu(screen)


    def setState(self, new_state):
        self.currentState = new_state


    def update(self):
        transition = self.currentState.update()

        if transition == 'gameplay':
            self.setState(Gameplay(self.screen))

    def draw(self):
        self.currentState.draw()
