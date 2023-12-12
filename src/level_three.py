import pygame
from config import *
from level import Level
from player import Player
from boss import Boss

class LevelThree(Level):
    def __init__(self) -> None:
        super().__init__(screen)
        self.bkg = bkg
        self.pos = (WIDTH - WIDTH_PLATFORM // 2, 125 - HEIGHT_DOOR)
        self.door_rect = door.get_rect(topleft = self.pos)
        self.platforms = []
        self.obst = []
        self.enemies = []
        self.boss = Boss([self.all_sprites], (WIDTH // 2, HEIGHT),  2)
        self.player =  self.player = Player([self.all_sprites], (WIDTH - WIDTH_PLAYER // 2, HEIGHT - HEIGHT_PLAYER // 2), self.platforms, self.obst, 4, screen, self.enemies, self.boss)

