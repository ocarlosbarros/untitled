import pygame
import player

class Options:

    def __init__(self, screen):
        self.screen = screen
        

    def update(self, events):
        return None
        
    def draw(self):

        self.screen.show((0, 0, 255))
                