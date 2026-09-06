import pygame

class Screen:

    def __init__ (self, title, resolution):
        self.surface = pygame.display.set_mode(resolution)
        pygame.display.set_caption(title)



    def show(self, background_color):
        self.surface.fill(background_color)