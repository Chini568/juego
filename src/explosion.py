import pygame
from sprite_sheet import Sprites


class Explosion(pygame.sprite.Sprite):
    def __init__(self, groups, coordenadas) -> None:
        super().__init__(groups)
        self.sheet = Sprites(pygame.image.load("./src/assets/images/exp.png").convert_alpha(), 64, 64, 1, 16)
        self.animations = self.sheet.get_animation(2)
        self.frame = 0
        self.image = self.animations[self.frame]
        self.rect = self.image.get_rect(center = coordenadas)
        self.last_update = pygame.time.get_ticks()
        self.speed_frame = 25
        self.explosion_s = pygame.mixer.Sound('./src/assets/sounds/explosion.wav')

    def update(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_update >= self.speed_frame:
            self.frame += 1
            if self.frame == len(self.animations):
                self.kill()
                self.explosion_s.play()
            else:
                self.image = self.animations[self.frame]
            self.last_update = current_time