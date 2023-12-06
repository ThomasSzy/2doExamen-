import pygame
from pygame import *


# Pantalla y FPS
WIDTH = 1200
HEIGHT = 800

CENTER_SCREEN = (WIDTH // 2, HEIGHT // 2)
FPS = 60
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
# Player
WIDTH_PLAYER = 50
HEIGHT_PLAYER = 50

WIDTH_PLAYER_SHOOT = 84
HEIGHT_PLAYER_SHOOT = 64

# Dino
WIDTH_DINO = 120
HEIGHT_DINO = 80


# Soldado

WIDTH_WARR = 64
HEIGHT_WARR = 64

# Boss
WIDTH_BOSS = 64
HEIGHT_BOSS = 77

# Gravedad y Colores
GRAVEDAD = 1

WITHE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GOLD = (255, 215, 0)

# Granadas
GRAVEDAD_GRANADA = 0.85

# Items
WIDTH_COIN = 64
HEIGHT_COIN = 64

# font


# buttons


CENTER_X = SCREEN.get_width() // 2
BUTTON_WIDTH = 200
BUTTON_HEIGHT = 50


def wait_user():
    """
    Quita el juego al colocar la tecla definida
    detiene el juego temporalmente para y esperar a la accion que realice el usuario

    Returns:
        None: La funcion no devuelve ningun valor
    """
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit_game()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    exit_game()
                return None


def exit_game():
    """
    Quita el juego
    """
    pygame.QUIT
    exit()
