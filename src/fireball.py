import pygame
from config import *
from sprite_sheet import Sprites
from pygame.locals import *
from score import Score


class Fireball(pygame.sprite.Sprite):
    def __init__(self, groups, enemies:list, player_rect, player, direction, cols, boss):
        super().__init__(groups)
        self.player = player
        self.boss = boss
        self.cols = cols
        self.enemies = enemies
        self.direction = direction
        self.screen = pygame.display.get_surface()
        self.sheet = Sprites(pygame.image.load(path.abspath("./src/assets/images/fireball blue.png")).convert_alpha(), WIDTH_FIREBALL, HEIGHT_FIREBALL, 1, 24, ['idle'])
        self.current_sprite = 0
        self.last_update = pygame.time.get_ticks()
        self.animations = self.sheet.get_animation_dict(scale=0.4)
        self.time_animation = 100
        self.image = self.animations['idle'][self.current_sprite]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.score = Score()
        if self.direction == 'right':
            self.rect.midright = (player_rect.midright[0] + 10, player_rect.midright[1] )
        else:
            self.rect.midleft = (player_rect.midleft[0] - 10,  player_rect.midleft[1])

    def update(self):
        if self.direction == 'right':
            self.rect.x += FIREBALL_SPEED
        else:
            self.rect.x -= FIREBALL_SPEED

        current_time = pygame.time.get_ticks()  
        if current_time - self.last_update >= self.time_animation:
            self.current_sprite += 1
            self.image = self.animations['idle'][self.current_sprite]
            self.mask = pygame.mask.from_surface(self.image)
            if self.current_sprite == self.cols - 1 :
                self.current_sprite = 0 
            self.last_update = current_time

        for enemy in self.enemies[:]:
            if pygame.sprite.collide_mask(self, enemy):
                self.enemies.remove(enemy)
                enemy.kill()
                sound_zombie_died.play()
                self.kill()
                self.fireball = False
                self.score.sumar_puntaje(100)

        if self.rect.right < 0 or self.rect.left > WIDTH:
            self.kill()
            self.fireball = False

        if self.boss != None:
            if pygame.sprite.collide_mask(self, self.boss):
                self.boss.lives_boss -= 1
                self.kill()



            
        