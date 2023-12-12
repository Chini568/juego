import pygame
from config import *
from sprite_sheet import Sprites

class BossFireball(pygame.sprite.Sprite):
    def __init__(self, groups, boss_rect, direction):
        super().__init__(groups)
        self.boss_rect = boss_rect
        self.direction = direction
        self.screen = pygame.display.get_surface()
        self.sheet = Sprites(pygame.image.load(path.abspath("./src/assets/images/fireball boss.png")).convert_alpha(), WIDTH_FIREBALL, HEIGHT_FIREBALL, 1, 24, ['idle'])
        self.current_sprite = 0
        self.last_update = pygame.time.get_ticks()
        self.animations = self.sheet.get_animation_dict(scale=0.4)
        self.time_animation = 100
        self.image = self.animations['idle'][self.current_sprite]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()

        if self.direction == 'left':
            self.rect.midright = (self.boss_rect.midleft[0] + WIDTH_BOSS + 10 , self.boss_rect.midleft[1] - 10 )
        elif self.direction == 'right':
            self.rect.midleft = (self.boss_rect.midright[0] - WIDTH_BOSS + 10 , self.boss_rect.midright[1] - 10 )

    def update(self):
        if self.direction == 'left':
            self.rect.x -= FIREBALL_SPEED
        elif self.direction == 'right':
            self.rect.x += FIREBALL_SPEED

        current_time = pygame.time.get_ticks()
        if current_time - self.last_update >= self.time_animation:
            self.current_sprite += 1
            self.image = self.animations['idle'][self.current_sprite]
            self.mask = pygame.mask.from_surface(self.image)
            if self.current_sprite == len(self.animations['idle']) - 1:
                self.current_sprite = 0
            self.last_update = current_time
