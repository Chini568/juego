import pygame
from pygame.locals import *
from config import *

class TextBox:
    def __init__(self):
        self.rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 - HEIGHT_BUTTON * 1.5, 200, 50)
        self.color_active = blanco
        self.color_inactive = negro
        self.color = self.color_inactive
        self.font = font_low
        self.text = ''
        self.active = False

    def handle_event(self, event):
        self.active = True
        if self.active:
                if event.type == KEYDOWN:
                    if event.key == K_RETURN:
                        self.active = False
                    elif event.key == K_BACKSPACE:
                        self.text = self.text[:-1]
                    else:
                        self.text += event.unicode

    def draw(self):
        width = max(200, self.rect.width)
        pygame.draw.rect(screen, blanco, self.rect, 2)  
        txt_surface = self.font.render(self.text, True, self.color)
        screen.blit(txt_surface, (self.rect.x + 5, self.rect.y + 5))
        self.rect.w = width

    def get_text(self):
        return self.text