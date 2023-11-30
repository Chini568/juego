import pygame
from pygame.locals import *
from config import *

class Obst(pygame.sprite.Sprite):
    def __init__(self, groups, position:tuple, image_path:str, direction:str, width, height) -> None:
        super().__init__(groups)
        self.direction = direction  # 'up', 'down', 'left', 'right'
        original_image = pygame.transform.scale(pygame.image.load(image_path).convert_alpha(), (width, height))
        self.image = self.rotate_triangle(original_image)
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(bottomleft =position)

    def rotate_triangle(self, image):
        if self.direction == 'up':
            return image
        elif self.direction == 'down':
            return pygame.transform.rotate(image, 180)
        elif self.direction == 'left':
            return pygame.transform.rotate(image, 90)
        elif self.direction == 'right':
            return pygame.transform.rotate(image, -90)
        else:
            return image
