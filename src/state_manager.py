from states.main_menu import MainMenu


class StateManager:

    def __init__(self, screen):
        self.screen = screen
        self.currentState = MainMenu(screen)


    def setState(self, new_state):
        self.currentState = new_state 