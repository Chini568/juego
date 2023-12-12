import pygame
from config import *
from level import Level
from platforms import Platform
from obst import Obst
from enemy import Enemy
from player import Player
class LevelTwo(Level):
    def __init__(self) -> None:
        super().__init__(screen)
        self.bkg = bkg_2
        self.pos = (WIDTH - WIDTH_PLATFORM // 2, 125 - HEIGHT_DOOR)
        self.door = door
        self.door_rect = door.get_rect(topleft = self.pos)  
        self.platforms = [
            Platform([self.all_sprites], (100,450), WIDTH_PLATFORM, HEIGHT_PLATFORM),
            Platform([self.all_sprites], (300,300), WIDTH_PLATFORM, HEIGHT_PLATFORM),
            Platform([self.all_sprites], (WIDTH - WIDTH_PLATFORM,125), WIDTH_PLATFORM, HEIGHT_PLATFORM),
            Platform([self.all_sprites], (500 ,160), WIDTH_PLATFORM, HEIGHT_PLATFORM)
        ]
        self.x_platform_1, self.y_platform_1  = self.platforms[0].rect.topleft
        self.x_platform_2, self.y_platform_2  = self.platforms[1].rect.topleft
        self.obst = [
            Obst([self.all_sprites], (self.x_platform_1, self.y_platform_1 ), spike_image, 'up',WIDTH_PINCHE, HEIGHT_PINCHE),
            Obst([self.all_sprites], (self.x_platform_2 + WIDTH_PLATFORM - WIDTH_PINCHE, self.y_platform_2), spike_image, 'up',WIDTH_PINCHE, HEIGHT_PINCHE),
            Obst([self.all_sprites], (self.x_platform_2 , self.y_platform_2), spike_image, 'up',WIDTH_PINCHE, HEIGHT_PINCHE)
        ]
        self.enemies = [
            Enemy([self.all_sprites], (0 + WIDTH_ENEMY, (HEIGHT - HEIGHT_ENEMY //  4) - 4   ), 6)
        ]
        self.player  = Player([self.all_sprites], (WIDTH - WIDTH_PLAYER, HEIGHT - HEIGHT_PLAYER), self.platforms, self.obst, 4, screen, self.enemies, None)
