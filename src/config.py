import pygame
from os import path

WIDTH = 800
HEIGHT = 600

FPS = 60


GRAVITY = 1
JUMP = -20

WIDTH_PLAYER = 44
HEIGHT_PLAYER = 45
SPEED_PLAYER = 5

WIDTH_FIREBALL = 133
HEIGHT_FIREBALL = 133
FIREBALL_SPEED = 7


WIDTH_ENEMY= 128
HEIGHT_ENEMY= 128
SPEED_ENEMY = 1

WIDTH_PINCHE = 25
HEIGHT_PINCHE = 25

WIDTH_PLATFORM = 100
HEIGHT_PLATFORM = 20

WIDTH_DOOR = 64
HEIGHT_DOOR = 96

WIDTH_BUTTON = 200
HEIGHT_BUTTON = 50

WIDTH_LIVES = 30
HEIGHT_LIVES = 30


WIDTH_SLIDER = 200
HEIGHT_SLIDER = 20

BALL_SLIDER = (20,20)
#colores 
negro = (0,0,0)
gris = (200,200,200)
blanco = (255, 255, 255)
azul = (0, 0, 255)
rojo = (250, 0, 0)
amarillo = (250, 250, 0)
verde = (0,250,0)
cyan = (52, 152, 219)
violeta = (165, 105, 189)
rosa = (255, 143, 231 )
naranja = (255, 128, 0)
colores = [rojo, amarillo, verde, cyan, violeta, rosa, naranja, azul, blanco, negro]

#direccionesy cargas 
pygame.init()
pygame.mixer.music.load(path.abspath('./src/assets/sounds/music.mp3'))
screen = pygame.display.set_mode((WIDTH, HEIGHT))
font = pygame.font.SysFont("32bit Regular", 75)
font_low = pygame.font.SysFont("32bit Regular", 40)
spike_image = path.abspath('./src/assets/images/spike2.png')
bkg = pygame.image.load(path.abspath('./src/assets/images/back.jpg'))
door = pygame.image.load(path.abspath('./src/assets/images/door.png'))
icon_path = pygame.image.load(path.abspath('./src/assets/images/blastalot crouch.png'))