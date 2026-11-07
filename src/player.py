import pygame
from settings.general_settings import WHITE

pos_x = 50

triangle_points = [(pos_x, 100),(pos_x, 200),(150, 150)]
    
def draw(screen):
    pygame.draw.polygon(screen, WHITE, triangle_points)   


def move(velocity_x, pos_y):
    triangle_points = [(pos_x + velocity_x, 100),(pos_x + velocity_x, 200),(150, 150)]