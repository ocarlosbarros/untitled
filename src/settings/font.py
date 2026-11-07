import pygame
from settings.general_settings import WHITE, WIDTH, HEIGHT

class Font:
    
    def __init__(self, font_family, font_size):
        self.font = pygame.font.SysFont(font_family, font_size)

    def create_text(self, text, antialias = True, color = WHITE):
        text = self.font.render(text, antialias, color)
        return text

    def create_button_rect(self, surface, position, anchor = "center"):
        text_rect = surface.get_rect(**{anchor:position })
        return text_rect

    def horizontal_align(self, width) -> int:
        horizontal_align = (WIDTH - width) / 2
        return horizontal_align

    def vertical_align(self, height) -> int:
        vertical_align = (HEIGHT - height) / 2 
        return vertical_align


    def align_center(self, width, height):
        width_center = self.horizontal_align(width)
        height_center = self.vertical_align(height)
        return (width_center, height_center)