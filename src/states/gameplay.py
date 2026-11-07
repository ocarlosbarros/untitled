import pygame
import player

class Gameplay:

    def __init__(self, screen):
        self.screen = screen
        

    def update(self, events):
        return None
        #(578, 357)
        #print("EVENTS", self.events)
        pass
        # for event in self.events:
        #     print(event.type)
        #     if event.type == pygame.KEYDOWN:
                
        #         if event.key == pygame.K_a:
        #             print("Andandndo Esquerda")
        #         elif event.key == pygame.K_d:
        #             print("Andando direita")

    def draw(self):

        self.screen.show((0, 0, 0))
        
        player.draw(self.screen.surface)