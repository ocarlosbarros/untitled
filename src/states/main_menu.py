class MainMenu:

    def __init__(self, screen):
        self.screen = screen


    def update(self):
        return 'gameplay'

    
    def draw(self):
        self.screen.show((77, 77, 77))