import pygame
from os import path
from config import *
from pygame.locals import *
from player import Player
from sprite_sheet import Sprites
from platforms import Platform
from obst import Obst

class Game():
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Juego final")
        self.spike_image = path.abspath('./src/assets/images/spike2.png')
        self.bkg = pygame.image.load(path.abspath('./src/assets/images/bg001.png'))
        self.door = pygame.image.load(path.abspath('./src/assets/images/door.png'))
        self.plat_dir= path.abspath('./src/assets/images/Platform.png')
        self.clock = pygame.time.Clock()
        self.running = True
        self.all_sprites = pygame.sprite.Group()
        self.platforms = [
            Platform([self.all_sprites], (500,450), WIDTH_PLATFORM, HEIGHT_PLATFORM, self.plat_dir),
            Platform([self.all_sprites], (300,300), WIDTH_PLATFORM, HEIGHT_PLATFORM, self.plat_dir),
            Platform([self.all_sprites], (WIDTH - WIDTH_PLATFORM,125), WIDTH_PLATFORM, HEIGHT_PLATFORM, self.plat_dir),
            Platform([self.all_sprites], (500 ,160), WIDTH_PLATFORM, HEIGHT_PLATFORM, self.plat_dir)
        ]
        self.x_platform_1, self.y_platform_1  = self.platforms[0].rect.topleft
        self.x_platform_2, self.y_platform_2  = self.platforms[1].rect.topleft
        self.obst = [
            Obst([self.all_sprites], (self.x_platform_1, self.y_platform_1 ), self.spike_image, 'up',WIDTH_PINCHE, HEIGHT_PINCHE),
            Obst([self.all_sprites], (self.x_platform_2, self.y_platform_2), self.spike_image, 'up',WIDTH_PINCHE, HEIGHT_PINCHE),
            Obst([self.all_sprites], (self.x_platform_2 + WIDTH_PINCHE, self.y_platform_2), self.spike_image, 'up',WIDTH_PINCHE, HEIGHT_PINCHE)
        ]
        self.player = Player([self.all_sprites], (WIDTH - WIDTH_PLAYER // 2, HEIGHT - HEIGHT_PLAYER // 2), self.platforms, self.obst, 4)

    def run(self):
        while True:
            while self.running:
                self.handle_events()
                self.update()
                self.reder()
                self.clock.tick(FPS)
            self.close()

    def handle_events(self):
        for e in pygame.event.get():
            if e.type == QUIT:
                self.running = False
            self.player.jump()

    def update(self):
        self.all_sprites.update()

    def reder(self):
        self.screen.blit(self.bkg, (0,0))
        self.screen.blit(self.door, (WIDTH - WIDTH_PLATFORM // 2 , 125 - HEIGHT_DOOR))
        self.all_sprites.draw(self.screen)
        pygame.display.flip()

    def close(self):
        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.run()
