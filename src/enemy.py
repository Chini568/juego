import pygame
from config import *
from sprite_sheet import Sprites
from os import path

class Enemy(pygame.sprite.Sprite):
    def __init__(self, groups, coordenadas, cols) -> None:
        super().__init__(groups)
        self.cols = cols
        self.coordenadas = coordenadas
        self.enemy_sheet = Sprites(pygame.image.load(path.abspath('./src/assets/images/enemy.png')).convert_alpha(), WIDTH_ENEMY, HEIGHT_ENEMY, 2, 6, ['left', 'right'])
        self.animations = self.enemy_sheet.get_animation_dict(scale= 0.7)
        self.current_sprite = 0
        self.image = self.animations["right"][self.current_sprite]
        self.rect = self.image.get_rect(center = coordenadas)
        self.last_update = pygame.time.get_ticks()
        self.time_animation = 50
        self.speed_x = 0
        self.speed_x = SPEED_ENEMY
        self.direction = "right"

    def update(self):
        if self.image == self.animations["right"][self.current_sprite] and self.rect.right <= WIDTH:
            self.rect.x += SPEED_ENEMY
            current_time = pygame.time.get_ticks()  
            if current_time - self.last_update >= self.time_animation:
                self.current_sprite += 1
                self.image = self.animations['right'][self.current_sprite]
                self.mask = pygame.mask.from_surface(self.image)
                if self.current_sprite == self.cols - 1 :
                    self.current_sprite = 0 
                self.last_update = current_time
        else:
            if self.rect.left >= 0:
                self.rect.x -= SPEED_ENEMY
                current_time = pygame.time.get_ticks()  
                if current_time - self.last_update >= self.time_animation:
                    self.current_sprite += 1
                    self.image = self.animations['left'][self.current_sprite]
                    self.mask = pygame.mask.from_surface(self.image)
                    if self.current_sprite == self.cols - 1 :
                        self.current_sprite = 0 
                    self.last_update = current_time
                    
        if self.rect.right >= WIDTH:
            self.direction = "left"
        elif self.rect.left <= 0:
            self.direction = "right"

        if self.direction == "right":
            self.rect.x += self.speed_x
            self.image = self.animations['right'][self.current_sprite]
        else:
            self.rect.x -= self.speed_x
            self.image = self.animations['left'][self.current_sprite]


