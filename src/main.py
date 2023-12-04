import pygame
from os import path
from config import *
from pygame.locals import *
from player import Player
from platforms import Platform
from obst import Obst
from screen import StartScreen
from pausa_y_terminar import mostrar_texto
from enemy import Enemy
from level_menu import LevelMenu
from fireball import Fireball




class Game():
    def __init__(self) -> None:
        self.inicia_volumen = 0.5
        pygame.mixer.music.set_volume(self.inicia_volumen)
        pygame.display.set_caption("Juego final")
        pygame.display.set_icon(icon_path)
        self.clock = pygame.time.Clock()
        self.all_sprites = pygame.sprite.Group()
        self.running = True
        self.play = False
        self.hud = pygame.Rect(0, 0, WIDTH, HEIGHT // 12)
        self.platforms = [
            Platform([self.all_sprites], (500,450), WIDTH_PLATFORM, HEIGHT_PLATFORM),
            Platform([self.all_sprites], (300,300), WIDTH_PLATFORM, HEIGHT_PLATFORM),
            Platform([self.all_sprites], (WIDTH - WIDTH_PLATFORM,125), WIDTH_PLATFORM, HEIGHT_PLATFORM),
            Platform([self.all_sprites], (500 ,160), WIDTH_PLATFORM, HEIGHT_PLATFORM)
        ]
        self.x_platform_1, self.y_platform_1  = self.platforms[0].rect.topleft
        self.x_platform_2, self.y_platform_2  = self.platforms[1].rect.topleft
        self.obst = [
            Obst([self.all_sprites], (self.x_platform_1, self.y_platform_1 ), spike_image, 'up',WIDTH_PINCHE, HEIGHT_PINCHE),
            Obst([self.all_sprites], (self.x_platform_2, self.y_platform_2), spike_image, 'up',WIDTH_PINCHE, HEIGHT_PINCHE),
            Obst([self.all_sprites], (self.x_platform_2 + WIDTH_PINCHE, self.y_platform_2), spike_image, 'up',WIDTH_PINCHE, HEIGHT_PINCHE)
        ]
        self.enemies = [
            Enemy([self.all_sprites], (0 + WIDTH_ENEMY, (HEIGHT - HEIGHT_ENEMY //  4) - 4   ), 6)
        ]
        self.player = Player([self.all_sprites], (WIDTH - WIDTH_PLAYER // 2, HEIGHT - HEIGHT_PLAYER // 2), self.platforms, self.obst, 4, screen, self.enemies)


    def run(self):
        self.render_pause()
        self.menu = StartScreen(screen, font, bkg, self.play)
        self.menu.esperar_click('Play', 'Options', 'Exit', blanco, azul)
        self.play = True
        self.render_pause()
        self.level_menu = LevelMenu(bkg, screen, font, self.play)
        self.select_level = self.level_menu.esperar_click_level('Level 1', 'Level 2', 'Level 3', blanco, azul)
        pygame.mixer.music.play(-1)
        self.running = True
        while self.running:
            self.tiempo = pygame.time.get_ticks() / 1000
            self.handle_events()
            self.update()
            self.reder()
            self.clock.tick(FPS)
        self.close()
        

    def handle_events(self):
        for e in pygame.event.get():
            if e.type == QUIT:
                self.running = False
            if e.type == KEYDOWN:
                if e.key == K_ESCAPE:
                    self.menu.esperar_click_2( 'Continue', 'Exit',blanco, azul)
        self.player.move()
        self.player.jump()

    def update(self):
        self.all_sprites.update()
        self.player.lose_lives()   

    def reder(self):
        screen.blit(bkg, (0,0))
        screen.blit(door, (WIDTH - WIDTH_PLATFORM // 2 , 125 - HEIGHT_DOOR))
        self.all_sprites.draw(screen)
        pygame.draw.rect(screen, azul, self.hud)
        self.player.draw_lives()
        mostrar_texto(screen, f'Tiempo: {int(self.tiempo)}', font_low, (WIDTH // 2, 20), gris, None)
        mostrar_texto(screen, f'{int()}', font_low, (WIDTH - 100 , 20), gris, None)
        pygame.display.flip()

    def render_pause(self):
        screen.blit(bkg, (0,0))
        pygame.display.flip()

    def close(self):
        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.run()
