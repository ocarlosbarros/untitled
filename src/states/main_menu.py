import pygame
from settings.font import Font
from settings.general_settings import HEIGHT, WHITE, BUTTON_PADDING, HORIZONTAL_CENTER, VERTICAL_CENTER

class MainMenu:

    

    def __init__(self, screen):
        self.screen = screen
        self.font = Font(None, 72)
        self.play_text = self.create_text("Jogar")
        self.restart_text = self.create_text("Recomeçar")
        self.options_text = self.create_text("Opções")
        self.quitgame_text = self.create_text("Sair")
        
        self.menu_total_height = (
            self.play_text.get_height()
            + self.restart_text.get_height()
            + self.options_text.get_height()
            + self.quitgame_text.get_height()
            + (BUTTON_PADDING * 3)
        )
        self.menu_start_pos_y = (HEIGHT - self.menu_total_height) / 2
        self.play_position = (self.font.horizontal_align(self.play_text.get_width()), self.menu_start_pos_y )
        self.restart_position = (self.font.horizontal_align(self.restart_text.get_width()), self.play_position[1] + self.play_text.get_height() + BUTTON_PADDING)
        self.options_position = (self.font.horizontal_align(self.options_text.get_width()), self.restart_position[1] + self.restart_text.get_height() + BUTTON_PADDING)
        self.quitgame_position = (self.font.horizontal_align(self.quitgame_text.get_width()), self.options_position[1] + self.options_text.get_height() + BUTTON_PADDING)
        
        self.play_button = self.create_button(self.play_text, self.play_position, "topleft")
        self.restart_button = self.create_button(self.restart_text, self.restart_position, "topleft")
        self.options_button = self.create_button(self.options_text, self.options_position, "topleft")
        self.quitgame_button = self.create_button(self.quitgame_text, self.quitgame_position, "topleft")


        self.left_mouse_button = 1

    def update(self, events):
        
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == self.left_mouse_button:
                    transition = self.check_button_click(event.pos)

                    if transition:
                        return transition
        
        return None

    def check_button_click(self, mouse_position):

        print("Play:", self.play_button.collidepoint(mouse_position))
        print("Restart:", self.restart_button.collidepoint(mouse_position))
        print("Options:", self.options_button.collidepoint(mouse_position))
        print("Quit:", self.quitgame_button.collidepoint(mouse_position))

        if self.play_button.collidepoint(mouse_position):
            return "gameplay"
        
        elif self.restart_button.collidepoint(mouse_position):
             return "restart"

        elif self.options_button.collidepoint(mouse_position):
             return "options"

        elif self.quitgame_button.collidepoint(mouse_position):
            return "quit"                    
                                
                                
    
    def create_text(self, text_button, color = "WHITE"):
        created_text = self.font.create_text(text_button, color)
        print(created_text)
        return created_text

    def create_button(self, text, position, anchor):
        button_rect = self.font.create_button_rect(text, position, anchor)
        button_rect.inflate_ip(5, 5)
        return button_rect
    
    def draw(self):

        self.screen.show((77, 77, 77))

        
        self.screen.draw(self.play_text, self.play_position)
        self.screen.draw(self.restart_text, self.restart_position)
        self.screen.draw(self.options_text, self.options_position)
        self.screen.draw(self.quitgame_text, self.quitgame_position)
        
        
        