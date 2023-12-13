import pygame
from config import *
from pausa_y_terminar import *



class LevelMenu:
    def __init__(self, bkg, screen, font, play) -> None:
        self.play = play
        self.bkg = bkg
        self.screen = screen
        self.font = font
        self.btn_1 =  pygame.Rect(WIDTH // 2 - WIDTH_BUTTON // 2, HEIGHT // 2 , WIDTH_BUTTON, HEIGHT_BUTTON)
        self.btn_2 =  pygame.Rect(WIDTH // 2 - WIDTH_BUTTON // 2, HEIGHT // 2 + HEIGHT_BUTTON * 1.5, WIDTH_BUTTON, HEIGHT_BUTTON)
        self.btn_3 =  pygame.Rect(WIDTH // 2 - WIDTH_BUTTON // 2, HEIGHT // 2 + HEIGHT_BUTTON * 3, WIDTH_BUTTON, HEIGHT_BUTTON)

    def esperar_click_level(self, texto_1, texto_2, texto_3,  color, segundo_color):
        while self.play:
            screen.blit(bkg, (0,0))
            mostrar_texto(self.screen, 'Level Menu', self.font, (WIDTH //2, HEIGHT // 6), negro, None )
            crear_boton(self.screen, self.btn_1, texto_1, color, segundo_color)
            crear_boton(self.screen, self.btn_2, texto_2, color, segundo_color)
            crear_boton(self.screen, self.btn_3, texto_3, color, segundo_color)
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    terminar()      
                
                if e.type == pygame.MOUSEBUTTONDOWN:
                    if e.button == 1 :
                        cursor = e.pos
                        if self.btn_1.collidepoint(cursor[0], cursor[1]):
                            self.level =1
                        elif self.btn_2.collidepoint(cursor[0], cursor[1]):
                            self.level = 2
                        elif self.btn_3.collidepoint(cursor[0], cursor[1]):
                            self.level = 3
                    return self.level
            pygame.display.flip()
        

    