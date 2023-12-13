import pygame
from pygame.locals import *
from config import *
from os import path
from pausa_y_terminar import *
from slider import Slider
from level_menu import LevelMenu
from txt_box import TextBox
from sqlite_score import Sqlite

class StartScreen(LevelMenu):
    def __init__(self, font, fondo, play) -> None:
        self.play = play
        self.font = font
        self.bkg = fondo
        self.button_play = pygame.Rect(WIDTH // 2 - WIDTH_BUTTON // 2, HEIGHT // 2, WIDTH_BUTTON, HEIGHT_BUTTON)
        self.button_config = pygame.Rect(WIDTH // 2 - WIDTH_BUTTON // 2, HEIGHT // 2 + HEIGHT_BUTTON * 1.5, WIDTH_BUTTON, HEIGHT_BUTTON)
        self.button_exit = pygame.Rect(WIDTH // 2 - WIDTH_BUTTON // 2, HEIGHT // 2 + HEIGHT_BUTTON * 3, WIDTH_BUTTON, HEIGHT_BUTTON)
        self.button_level = pygame.Rect(WIDTH // 2 - WIDTH_BUTTON // 2, HEIGHT // 2 + HEIGHT_BUTTON * 4.5, WIDTH_BUTTON, HEIGHT_BUTTON)
        self.slider = Slider((WIDTH // 2, HEIGHT // 2 + HEIGHT_BUTTON * 2), (WIDTH_SLIDER, HEIGHT_SLIDER), 1, 0, 100, screen)
        self.txt_box = TextBox()
        self.sqlite_score= Sqlite()

    def esperar_click(self, texto_1, texto_2, texto_3,  color, segundo_color):
        while not self.play:
            screen.blit(self.bkg, (0,0))
            mostrar_texto(screen, 'Garen el poderoso', self.font, (WIDTH //2, HEIGHT // 6), negro, None )
            crear_boton(screen, self.button_play, texto_1, color, segundo_color)
            crear_boton(screen, self.button_config, texto_2, color, segundo_color)
            crear_boton(screen, self.button_exit, texto_3, color, segundo_color)
            scores = self.sqlite_score.get_scores()
            for i in range(3):
                player_name, score = scores[i]
                rect_score = pygame.Rect(WIDTH - 250 , (HEIGHT // 2 - 75) + (HEIGHT_BUTTON * i), 200, HEIGHT_BUTTON)
                pygame.draw.rect(screen, blanco, rect_score)
                pygame.draw.rect(screen, negro, rect_score, 2)
                mostrar_texto(screen, f"{i + 1}. {player_name}: {score}",font_low, rect_score.center, negro, None)
            for e in pygame.event.get():
                self.txt_box.handle_event(e)
                if e.type == pygame.QUIT:
                    terminar()      
                if e.type == pygame.MOUSEBUTTONUP:
                    if e.button == 1 :
                        cursor = e.pos
                        if self.button_play.collidepoint(cursor[0], cursor[1]): 
                            return None
                        elif self.button_config.collidepoint(cursor[0], cursor[1]):
                            self.esperar_click_2('Continue', 'Exit', blanco, azul)
                        elif self.button_exit.collidepoint(cursor[0], cursor[1]):
                            return terminar() 
            self.txt_box.draw()
            pygame.display.flip()
           
    def mostrar_score(self):
        return self.sqlite_score.get_scores()
    
    def esperar_click_2(self, texto_1, texto_2, color, segundo_color):
        while True:
            screen.blit(self.bkg, (0,0))
            mouse_pos = pygame.mouse.get_pos()
            mouse = pygame.mouse.get_pressed()   
            mostrar_texto(screen, 'Pausa', self.font, (WIDTH //2, HEIGHT // 6), negro, None )
            crear_boton(screen, self.button_play, texto_1, color, segundo_color)
            crear_boton(screen, self.button_exit, texto_2, color, segundo_color)
            rect_slider = pygame.Rect(WIDTH // 2 - WIDTH_BUTTON - 60 // 2, HEIGHT // 2 + HEIGHT_BUTTON * 1.5, 415, 50)
            pygame.draw.rect(screen, gris, rect_slider, border_radius= 4)
            mostrar_texto(screen, 'Sonido:', font_low, (WIDTH // 2 - 170, HEIGHT // 2 + HEIGHT_BUTTON * 2), negro, None)
            self.slider.reder()

            if self.slider.container_rect.collidepoint(mouse_pos) and mouse[0]:
                self.slider.move_slider(mouse_pos)
            volumen = self.slider.get_value()
            pygame.mixer.music.set_volume(volumen)
            porcentage = volumen * 100
            mostrar_texto(screen, f'{porcentage:.0f}%', font_low, (WIDTH // 2 + 150, HEIGHT // 2 + HEIGHT_BUTTON * 2), negro, None)

            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    terminar()
                if mouse[0]:
                    if self.button_play.collidepoint(mouse_pos[0], mouse_pos[1]):
                        return None 
                    elif self.button_exit.collidepoint(mouse_pos[0], mouse_pos[1]):
                        return terminar()
            pygame.display.flip()

    def get_player_name(self):
        return self.txt_box.get_text()


