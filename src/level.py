import pygame
from config import *

class Level:
    def __init__(self, screen, player, platforms, bkg) -> None:
        self.screen = screen
        self.player = player
        self.platforms = platforms
        self.bkg = bkg

    def update(self, events):
        self.all_sprites = pygame.sprite.Group()
