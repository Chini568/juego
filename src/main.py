import pygame
from pygame.locals import *
from config import *
from level_one import LevelOne
from level_two import LevelTwo
from level_three import LevelThree
from level_menu import LevelMenu
from screen import StartScreen
from pausa_y_terminar import *
 
pygame.init()
class Game:
    def __init__(self):
        pygame.mixer.music.set_volume(0.5)
        pygame.display.set_caption("Juego final")
        pygame.display.set_icon(icon_path)
        self.clock = pygame.time.Clock()
        self.all_sprites = pygame.sprite.Group()
        self.running = True
        self.play = False
        self.hud = pygame.Rect(0, 0, WIDTH, HEIGHT // 12)
        self.menu = StartScreen(screen, font, bkg, self.play)
        self.current_level = None
        self.change_level = False

    def select_level(self):
        self.level_menu = LevelMenu(bkg, screen, font, True)
        self.selected_level = self.level_menu.esperar_click_level('Level 1', 'Level 2', 'Level 3', blanco, azul)
        if self.selected_level == 1:
           return  LevelOne()
        elif self.selected_level == 2:
           return  LevelTwo()
        elif self.selected_level == 3:
           return  LevelThree()

    def run(self):
        self.start_screen = StartScreen(screen, font, bkg, game.play)
        self.start_screen.esperar_click('Play', 'Config', 'Exit', blanco, azul)
        level_selected = self.select_level()
        pygame.mixer.music.play(-1)
        self.current_level = level_selected
        self.running = True
        self.player = level_selected.player
        while self.running:
            self.time = pygame.time.get_ticks() / 1000
            self.handle_events()
            if self.change_level:
                self.current_level = self.select_level()
                self.player = self.current_level.player
                self.change_level = False
            self.update()
            self.draw()
            self.clock.tick(FPS)
        self.close()

    def handle_events(self):
        for e in pygame.event.get():
            if e.type == QUIT:
                self.running = False
            if e.type == KEYDOWN:
                if e.key == K_p:
                    self.menu.esperar_click_2('Continue', 'Exit', blanco, azul)

    def complete_level(self):
        door_rect = self.current_level.door_rect
        if self.player and door_rect and self.player.rect.colliderect(door_rect):
            self.change_level = True
            
    def update(self):
        if self.player:
            self.player.move()
            self.player.lose_lives()
            self.player.jump()
            self.current_level.update()
            self.complete_level()
            if self.current_level.enemies:
                for enemy in self.current_level.enemies:
                    enemy.update()
            if self.current_level.obst:
                for obst in self.current_level.obst:
                    obst.update()
            if self.current_level.platforms:
                for platform in self.current_level.platforms:
                    platform.update()
        self.all_sprites.update()

    def draw(self):
        self.current_level.draw()
        self.all_sprites.draw(screen)
        pygame.draw.rect(screen, azul, self.hud)
        mostrar_texto(screen, f'{int(self.time)}', font_low, (WIDTH // 2, 20), blanco, None)
        mostrar_texto(screen, f'{int()}', font_low, (700, 20), blanco, None)
        self.player.draw_lives()  
        pygame.display.flip()

    def close(self):
        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()
    
        
    