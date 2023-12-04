import pygame
from config import *
from level import Level

class LevelOne(Level):
    def __init__(self, screen, player, platforms, bkg) -> None:
        super().__init__(screen, player, platforms, bkg)