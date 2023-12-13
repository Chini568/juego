import pygame
from sprite_sheet import Sprites
from pygame.locals import * 
from config import *
from explosion import Explosion
from os import path
from fireball import Fireball
from pausa_y_terminar import *
from score import Score

class Player(pygame.sprite.Sprite):
    def __init__(self, groups, coordenadas, platforms, obst:list, cols:int, screen, enemies, boss) -> None:
        super().__init__(groups)
        self.boss = boss
        self.coordenadas = coordenadas
        self.screen = screen
        self.enemies = enemies
        self.obst = obst
        self.cols = cols
        self.platforms = platforms
        self.groups = groups

        self.direction = 'left'
        self.damage = False

        self.oof = pygame.mixer.Sound(path.abspath('./src/assets/sounds/oof.mp3'))
        self.lives_img = pygame.transform.scale(pygame.image.load(path.abspath('./src/assets/images/vida.png')), (WIDTH_LIVES, HEIGHT_LIVES))
        self.sheet = Sprites(pygame.image.load(path.abspath("./src/assets/images/shoot knight comp.png")).convert_alpha(), WIDTH_PLAYER, HEIGHT_PLAYER, 10, 4 , ['right', 'left', 'idle_left', 'idle_right', 'jump_right', 'jump_left', 'shoot_idle_right', 'shoot_idle_left', 'shoot_run_right', 'shoot_run_left'])

        self.current_sprite = 0
        self.animations = self.sheet.get_animation_dict(scale= 1.6)
        self.image = self.animations["idle_left"][self.current_sprite]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(center = coordenadas)

        self.last_update = pygame.time.get_ticks()
        self.last_damage_time = pygame.time.get_ticks()
        self.last_shoot_time = pygame.time.get_ticks()

        self.time_animation = 50
        self.damage_cooldown = 1000  

        self.shoot_cooldown = 3000

        self.lives = 3
        self.speed_v = 0
        self.can_jump = True

        self.exploto = False

        self.fireball = None

        self.score = Score()
    def update(self):
        self.speed_v += GRAVITY 
        self.rect.y += self.speed_v
        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT
            self.speed_v = 0
            self.can_jump = True

  
    def move(self):     
        self.keys = pygame.key.get_pressed()
        if self.keys[K_a] or self.keys[K_LEFT]:
            self.direction = 'left'
            if self.rect.left >= 0:
                self.rect.x -= SPEED_PLAYER
                current_time = pygame.time.get_ticks()  
                if current_time - self.last_update >= self.time_animation:
                    self.current_sprite += 1
                    self.image = self.animations['left'][self.current_sprite]
                    self.mask = pygame.mask.from_surface(self.image)
                    if self.current_sprite == self.cols - 1 :
                        self.current_sprite = 0 
                    self.last_update = current_time


        elif self.keys[K_d] or self.keys[K_RIGHT]:
            self.direction = 'right'
            if self.rect.right <= WIDTH:
                self.rect.x += SPEED_PLAYER
                current_time = pygame.time.get_ticks()  
                if current_time - self.last_update >= self.time_animation:
                    self.current_sprite += 1
                    self.image = self.animations['right'][self.current_sprite]
                    self.mask = pygame.mask.from_surface(self.image)
                    if self.current_sprite == self.cols - 1 :
                        self.current_sprite = 0 
                    self.last_update = current_time

                    
        elif self.keys[K_l] and self.direction == 'right':
            current_time = pygame.time.get_ticks()  
            if current_time - self.last_update >= self.time_animation:
                self.current_sprite += 1
                self.image = self.animations['shoot_idle_right'][self.current_sprite]
                self.mask = pygame.mask.from_surface(self.image)
                if self.current_sprite == self.cols - 1 :
                    self.current_sprite = 0 
                self.last_update = current_time
                if current_time - self.last_shoot_time > self.shoot_cooldown:
                    self.fireball = Fireball(self.groups, self.enemies, self.rect, self, self.direction, self.cols, self.boss)
                    self.last_shoot_time = current_time
                    sound_laser.play()

        elif self.keys[K_l] and self.direction == 'left':
            current_time = pygame.time.get_ticks()  
            if current_time - self.last_update >= self.time_animation:
                self.current_sprite += 1
                self.image = self.animations['shoot_idle_left'][self.current_sprite]
                self.mask = pygame.mask.from_surface(self.image)
                if self.current_sprite == self.cols - 1 :
                    self.current_sprite = 0 
                self.last_update = current_time
                if current_time - self.last_shoot_time > self.shoot_cooldown:
                    self.fireball = Fireball(self.groups, self.enemies, self.rect, self, self.direction, self.cols, self.boss)
                    self.last_shoot_time = current_time
                    sound_laser.play()
               
        else:
            if self.direction == 'right':
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
            if pygame.sprite.collide_rect(self, platform) and self.speed_v > 0:
                    self.on_platform = True
                    self.rect.bottom = platform.rect.top
                    self.speed_v = 0
                    self.can_jump = True
                    if self.keys[K_s] or self.keys[K_DOWN]:
                        self.rect.top = platform.rect.bottom
            else:
                self.on_platform = False
        
                
    def lose_lives(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_damage_time > self.damage_cooldown:
            for obst in self.obst:
                if pygame.sprite.collide_mask(self, obst) and not self.damage:
                    if self.lives >=  1: 
                        self.lives -= 1
                        self.damage = True
                        self.last_damage_time = current_time
                        self.oof.play()
                        self.score.restar_puntaje(100)

        if self.boss != None:                
            if current_time - self.last_damage_time > self.damage_cooldown:
                for fireballs_boss in self.boss.get_all_fireballs():
                    if (pygame.sprite.collide_mask(self, fireballs_boss) or pygame.sprite.collide_mask(self, self.boss)) and not self.damage:
                        if self.lives >= 1:
                            self.lives -= 1
                            self.damage = True
                            self.last_damage_time = current_time
                            self.oof.play()
                            self.score.restar_puntaje(100)
            else:
                self.damage = False

        current_time = pygame.time.get_ticks()
        if current_time - self.last_damage_time > self.damage_cooldown:
            for enemy in self.enemies:
                if pygame.sprite.collide_mask(self, enemy) and not self.damage:
                    if self.lives >=  1: 
                        self.lives -= 1
                        self.damage = True
                        self.last_damage_time = current_time
                        self.oof.play()  
                        self.score.restar_puntaje(100)
                       
                       
        else:
            self.damage = False

        self.death()

    def death(self):
        if self.lives == 0 and not self.exploto:
            self.kill()
            Explosion(self.groups, self.rect.center)
            self.exploto = True
            
    def draw_lives(self):
        lives_x = 0
        for _ in range(self.lives):
            self.screen.blit(self.lives_img, (lives_x, 0))
            lives_x += WIDTH_LIVES + 5

    def jump(self):
        if self.speed_v == 0 and self.can_jump:
            if self.keys[K_UP] or self.keys[K_SPACE]:
                self.speed_v += JUMP
                self.can_jump = False

 
        