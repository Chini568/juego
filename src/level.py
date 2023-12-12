import pygame
from config import *

class Level:
    def __init__(self, screen):
        self.screen = screen
        self.all_sprites = pygame.sprite.Group()
        self.platforms = []  
        self.obst = []       
        self.enemies = []
        self.bkg = None   
        self.pos = None
        self.door_rect = None
        self.door = None
        self.boss = None
        
    def update(self):
        self.all_sprites.update()
    
    def draw(self):
        screen.blit(self.bkg, (0, 0))
        if self.door != None:
            screen.blit(self.door, self.pos)
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, sprite.rect)
        