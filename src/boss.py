import pygame
from os import path 
from config import *
from boss_fireball import BossFireball
from explosion import Explosion
from pausa_y_terminar import *
from score import Score



class Boss(pygame.sprite.Sprite):
    def __init__(self, groups, coordenadas, scale):
        super().__init__(groups)
        self.lives_boss = 3
        self.fireballs = []
        self.groups = groups
        self.coordenadas = coordenadas
        self.boss_idle = pygame.transform.scale(pygame.image.load(path.abspath('./src/assets/images/boss/idle boss.png')), (WIDTH_BOSS * scale, HEIGHT_BOSS * scale))
        self.boss_left = pygame.transform.scale(pygame.image.load(path.abspath('./src/assets/images/boss/leftt boss.png')), (WIDTH_BOSS * scale, HEIGHT_BOSS * scale))
        self.boss_right = pygame.transform.scale(pygame.image.load(path.abspath('./src/assets/images/boss/right boss.png')), (WIDTH_BOSS * scale, HEIGHT_BOSS * scale))
        self.boss_doble = pygame.transform.scale(pygame.image.load(path.abspath('./src/assets/images/boss/doble attack.png')), (WIDTH_BOSS * scale, HEIGHT_BOSS * scale))
        self.last_update = pygame.time.get_ticks()
        self.time_animation = 50
        self.attack_time = 2000
        self.last_attack_time = pygame.time.get_ticks()
        self.attack_sequence = ['left', 'right', 'double']
        self.current_attack = 0

        self.rect = self.boss_idle.get_rect(center=coordenadas)
        self.image = self.boss_idle
        self.direction = 'idle'
        self.muerto = False

        self.score = Score()

    def update(self):
        current_time = pygame.time.get_ticks()

        if current_time - self.last_attack_time > self.attack_time:
            self.last_attack_time = current_time
            self.direction = self.attack_sequence[self.current_attack]
            self.shoot_fireball()
            self.current_attack += 1
            if self.current_attack >= len(self.attack_sequence):
                self.current_attack = 0

        if current_time - self.last_update >= self.time_animation:
            if self.direction == 'left':
                self.image = self.boss_left
                self.mask = pygame.mask.from_surface(self.image)
            elif self.direction == 'right':
                self.image = self.boss_right
                self.mask = pygame.mask.from_surface(self.image)
            elif self.direction == 'double':
                self.image = self.boss_doble
                self.mask = pygame.mask.from_surface(self.image)
            else:
                self.image = self.boss_idle
                self.mask = pygame.mask.from_surface(self.image)

            self.last_update = current_time

        self.death_boss()

    def shoot_fireball(self):
        if self.direction == 'left':
            fireball = BossFireball(self.groups, self.rect, 'left')
            sound_boss_shoot.play()
            self.fireballs.append(fireball)
        elif self.direction == 'right':
            fireball = BossFireball(self.groups, self.rect, 'right')
            sound_boss_shoot.play()
            self.fireballs.append(fireball)
        elif self.direction == 'double':
            fireball_1 = BossFireball(self.groups, self.rect, 'left')
            fireball_2 = BossFireball(self.groups, self.rect, 'right')
            sound_boss_shoot.play()
            self.fireballs.append(fireball_1)
            self.fireballs.append(fireball_2)

    
    def death_boss(self):
        if self.lives_boss == 0 and not self.muerto:
            self.score.sumar_puntaje(500)
            self.kill()
            Explosion(self.groups, self.rect.center)
            sound_boss_death.play()
            self.muerto = True
            
   
    

    def get_all_fireballs(self):
        return self.fireballs