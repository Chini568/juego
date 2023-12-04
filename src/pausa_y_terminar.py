import pygame
from sys import exit
from config import *


def terminar():
    pygame.quit()
    exit()

def pausa():
    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                terminar()

            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    terminar()           
                return
        
                    
def mostrar_texto_boton(superficie, texto, x, y, font_size = 36, color = (0,0,0) ):
    fuente = pygame.font.SysFont('32bit Regular', font_size)
    render = fuente.render(texto, True, color)
    rect_texto = render.get_rect(center = (x, y))
    superficie.blit(render, rect_texto)


def crear_boton(screen, rect:pygame.Rect ,texto, color, color_hover):
    posicion_mouse = pygame.mouse.get_pos()
    if rect.collidepoint(posicion_mouse):
        pygame.draw.rect(screen, color_hover, rect, border_radius= 10)
    else:
        pygame.draw.rect(screen, color, rect, border_radius= 10)
    mostrar_texto_boton(screen, texto, rect.centerx, rect.centery)


def mostrar_texto(superficie, texto, fuente, cordenadas, color_fuente, color_fondo = (0,0,0)):
    superficie_texto = fuente.render(texto, True, color_fuente, color_fondo)
    rect_texto = superficie_texto.get_rect()
    rect_texto.center = cordenadas
    superficie.blit(superficie_texto, rect_texto)
