import pygame
from pygame.locals import *
from config import *

class Platform(pygame.sprite.Sprite):
    def __init__(self, groups, position:tuple, width, height) -> pygame.Rect:
        super().__init__(groups)
        self.image = pygame.transform.scale(pygame.image.load('./src/assets/images/stoneplat.jpg').convert_alpha(), (width, height))
        self.rect = self.image.get_rect(topleft=position)
        self.mask_plat = pygame.mask.from_surface(self.image)
        