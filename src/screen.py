import pygame
from pygame.locals import *
from config import *
from os import path
from pausa_y_terminar import *
from slider import Slider
from level_menu import LevelMenu

class StartScreen(LevelMenu):
    def __init__(self, screen, font, fondo, play) -> None:
        self.play = play
        self.screen = screen
        self.font = font
        self.bkg = fondo
        self.button_play = pygame.Rect(WIDTH // 2 - WIDTH_BUTTON // 2, HEIGHT // 2, WIDTH_BUTTON, HEIGHT_BUTTON)
        self.button_config = pygame.Rect(WIDTH // 2 - WIDTH_BUTTON // 2, HEIGHT // 2 + HEIGHT_BUTTON * 1.5, WIDTH_BUTTON, HEIGHT_BUTTON)
        self.button_exit = pygame.Rect(WIDTH // 2 - WIDTH_BUTTON // 2, HEIGHT // 2 + HEIGHT_BUTTON * 3, WIDTH_BUTTON, HEIGHT_BUTTON)
        self.button_level = pygame.Rect(WIDTH // 2 - WIDTH_BUTTON // 2, HEIGHT // 2 + HEIGHT_BUTTON * 4.2, WIDTH_BUTTON, HEIGHT_BUTTON)
        self.slider = Slider((WIDTH // 2, HEIGHT // 2 + HEIGHT_BUTTON * 2), (WIDTH_SLIDER, HEIGHT_SLIDER), 1, 0, 100, self.screen)

    def esperar_click(self, texto_1, texto_2, texto_3,  color, segundo_color):
        while not self.play:
            self.screen.blit(self.bkg, (0,0))
            mostrar_texto(self.screen, 'Garen el poderoso', self.font, (WIDTH //2, HEIGHT // 6), negro, None )
            crear_boton(self.screen, self.button_play, texto_1, color, segundo_color)
            crear_boton(self.screen, self.button_config, texto_2, color, segundo_color)
            crear_boton(self.screen, self.button_exit, texto_3, color, segundo_color)
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    terminar()      
                
                if e.type == pygame.MOUSEBUTTONUP:
                    if e.button == 1 :
                        cursor = e.pos
                        if self.button_play.collidepoint(cursor[0], cursor[1]): 
                            return None
                        elif self.button_config.collidepoint(cursor[0], cursor[1]):
                            self.esperar_click_2('Continue', 'Exit', blanco, azul)
                        elif self.button_level.collidepoint(cursor[0], cursor[1]):
                            return terminar() 
            pygame.display.flip()
           

    def esperar_click_2(self, texto_1, texto_2, color, segundo_color):
        while True:
            self.screen.blit(self.bkg, (0,0))
            mouse_pos = pygame.mouse.get_pos()
            mouse = pygame.mouse.get_pressed()   
            mostrar_texto(self.screen, 'Pausa', self.font, (WIDTH //2, HEIGHT // 6), negro, None )
            crear_boton(self.screen, self.button_play, texto_1, color, segundo_color)
            crear_boton(self.screen, self.button_exit, texto_2, color, segundo_color)
            rect_slider = pygame.Rect(WIDTH // 2 - WIDTH_BUTTON - 60 // 2, HEIGHT // 2 + HEIGHT_BUTTON * 1.5, 415, 50)
            pygame.draw.rect(self.screen, gris, rect_slider, border_radius= 4)
            mostrar_texto(self.screen, 'Sonido:', font_low, (WIDTH // 2 - 170, HEIGHT // 2 + HEIGHT_BUTTON * 2), negro, None)
            self.slider.reder()

            if self.slider.container_rect.collidepoint(mouse_pos) and mouse[0]:
                self.slider.move_slider(mouse_pos)
            volumen = self.slider.get_value()
            pygame.mixer.music.set_volume(volumen)
            porcentage = volumen * 100
            mostrar_texto(self.screen, f'{porcentage:.0f}%', font_low, (WIDTH // 2 + 150, HEIGHT // 2 + HEIGHT_BUTTON * 2), negro, None)

            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    terminar()
                if mouse[0]:
                    if self.button_play.collidepoint(mouse_pos[0], mouse_pos[1]):
                        return None 
                    elif self.button_exit.collidepoint(mouse_pos[0], mouse_pos[1]):
                        return terminar()
            pygame.display.flip()