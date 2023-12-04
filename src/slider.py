import pygame 
from config import *

class Slider:
    def __init__(self, pos: tuple, size:tuple, initial_val: float, min: int, max:int, screen)  -> None:
        self.pos = pos
        self.size = size
        self.screen = screen
        
        self.slider_left_pos = self.pos[0] - (size[0]//2)
        self.slider_right_pos = self.pos[0] + (size[0]//2)
        self.slider_top_pos = self.pos[1] - (size[1]//2)
    
        self.min = min
        self.max = max
        self.initial_val = (self.slider_right_pos - self.slider_left_pos)* initial_val #porcentaje 

        self.container_rect = pygame.Rect(self.slider_left_pos, self.slider_top_pos, self.size[0], self.size[1])

        self.button_rect = pygame.Rect(self.slider_right_pos - BALL_SLIDER[0], self.slider_top_pos, BALL_SLIDER[0], BALL_SLIDER[1])
        
    def move_slider(self, mouse_pos):
        self.button_rect.centerx = mouse_pos[0]

    def reder(self):
        pygame.draw.rect(self.screen, negro, self.container_rect, border_radius= 10)
        pygame.draw.rect(self.screen, azul, self.button_rect, border_radius= 20)

    def get_value(self):
        valor_normalizado = (self.button_rect.centerx - self.slider_left_pos) / (self.slider_right_pos - self.slider_left_pos)
        valor_normalizado = max(0, min(1, valor_normalizado))
        pygame.mixer.music.set_volume(valor_normalizado)

        return valor_normalizado
