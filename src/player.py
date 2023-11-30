import pygame
from sprite_sheet import Sprites
from pygame.locals import * 
from config import *
from explosion import Explosion

class Player(pygame.sprite.Sprite):
    def __init__(self, groups, coordenadas, platforms, obst:list, cols:int ) -> None:
        super().__init__(groups)
        self.groups = groups
        self.obst = obst
        self.cols = cols
        self.platforms = platforms
        self.right = False
        self.sheet = Sprites(pygame.image.load("./src/assets/images/playerknight_comp.png").convert_alpha(), WIDTH_PLAYER, HEIGHT_PLAYER, 6, 4 , ['jump_right', 'right', 'left', 'jump_left', 'idle_left', 'idle_right'])
        self.animations = self.sheet.get_animation_dict(scale= 1.6)
        self.current_sprite = 0
        self.image = self.animations["idle_left"][self.current_sprite]
        self.rect = self.image.get_rect(center = coordenadas)
        self.speed = 5 
        self.last_update = pygame.time.get_ticks()
        self.time_animation = 150
        self.speed_v = 0

    def update(self):
        self.speed_v += GRAVITY 
        self.rect.y += self.speed_v
        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT
            self.speed_v = 0 

        
        keys = pygame.key.get_pressed()
        if keys[K_d] or keys[K_RIGHT]:
            if self.rect.right <= WIDTH:
                self.rect.x += self.speed
                current_time = pygame.time.get_ticks()  
                if current_time - self.last_update >= self.time_animation:
                    self.current_sprite += 1
                    self.image = self.animations['right'][self.current_sprite]
                    self.mask = pygame.mask.from_surface(self.image)
                    if self.current_sprite == self.cols - 1 :
                        self.current_sprite = 0 
                    self.last_update = current_time
                    self.right = True
                    
        if keys[K_a] or keys[K_LEFT]:
            if self.rect.left >= 0:
                self.rect.x -= self.speed
                current_time = pygame.time.get_ticks()  
                if current_time - self.last_update >= self.time_animation:
                    self.current_sprite += 1
                    self.image = self.animations['left'][self.current_sprite]
                    self.mask = pygame.mask.from_surface(self.image)
                    if self.current_sprite == self.cols - 1 :
                        self.current_sprite = 0 
                    self.last_update = current_time
                    self.right = False
        
        else:
            if self.right:
                current_time = pygame.time.get_ticks()  
                if current_time - self.last_update >= self.time_animation:
                    self.current_sprite += 1
                    self.image = self.animations['idle_right'][self.current_sprite]
                    self.mask = pygame.mask.from_surface(self.image)
                    if self.current_sprite == self.cols - 1 :
                        self.current_sprite = 0 
                    self.last_update = current_time
            else:
                current_time = pygame.time.get_ticks()  
                if current_time - self.last_update >= self.time_animation:
                    self.current_sprite += 1
                    self.image = self.animations['idle_left'][self.current_sprite]
                    self.mask = pygame.mask.from_surface(self.image)
                    if self.current_sprite == self.cols - 1 :
                        self.current_sprite = 0 
                    self.last_update = current_time
                    
        for platform in self.platforms:
            if pygame.sprite.collide_rect(self, platform):
                if self.speed_v > 0:
                    self.on_platform = True
                    self.rect.bottom = platform.rect.top
                    self.speed_v = 0
                    if keys[K_s] or keys[K_DOWN]:
                        self.rect.top = platform.rect.bottom
            else:
                self.on_platform = False
                

        for obst in self.obst:
            if pygame.sprite.collide_mask(self, obst):
                self.kill()
                Explosion(self.groups, self.rect.center)

    def jump(self):
        keys = pygame.key.get_pressed()
        if self.speed_v == 0:
            if keys[K_UP] or keys[K_SPACE] and keys[K_RIGHT] or keys[K_d]:
                self.speed_v += JUMP
                current_time = pygame.time.get_ticks()  
                if current_time - self.last_update >= self.time_animation:
                    self.current_sprite += 1
                    self.image = self.animations['jump_right'][self.current_sprite]
                    self.mask = pygame.mask.from_surface(self.image)
                    if self.current_sprite == self.cols - 1 :
                        self.current_sprite = 0 
                    self.last_update = current_time