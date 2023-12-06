import pygame
from pygame import *
from pygame.locals import *


# def musica_intro():
#     """
#     Comienza la musica del menu
#     """
#     pygame.mixer.music.load("./src/sounds/musica_the_simpsons.mp3")
#     pygame.mixer.music.set_volume(0.1)
#     pygame.mixer.music.play(-1)


# def music_game_1():
#     """
#     Comienza la musica del Juego
#     """
#     pygame.mixer.music.load("./src/sounds/music_game.mp3")
#     pygame.mixer.music.set_volume(0.1)
#     pygame.mixer.music.play(-1)


def mordida():
    """
    Sonido cuando choca con algo que le hace daño al personaje
    """
    mordida = pygame.mixer.Sound(
        "./src/assets/sounds/level_1/enemigo/mordida_dinosaurio.mp3"
    )
    mordida.set_volume(0.1)
    mordida.play()


def fuego():
    """
    Sonido cuando choca con algo que le hace daño al personaje
    """
    fuego = pygame.mixer.Sound("./src/assets/sounds/level_1/objetos/fuego.mp3")
    fuego.set_volume(0.1)
    fuego.play()


def reloj():
    """
    Sonido cuando choca con algo que le da ventaja al personaje
    """
    reloj = pygame.mixer.Sound("./src/assets/sounds/level_1/objetos/reloj.mp3")
    reloj.set_volume(0.1)
    reloj.play()


def moneda():
    """
    Sonido cuando choca con algo que le da ventaja al personaje
    """
    moneda = pygame.mixer.Sound("./src/assets/sounds/level_1/objetos/monedas.mp3")
    moneda.set_volume(0.1)
    moneda.play()


def corazon():
    """
    Sonido cuando choca con algo que le da ventaja al personaje
    """
    corazon = pygame.mixer.Sound("./src/assets/sounds/level_1/objetos/corazon.mp3")
    corazon.set_volume(0.1)
    corazon.play()


def llave():
    """
    Sonido cuando choca con algo que le da ventaja al personaje
    """
    llave = pygame.mixer.Sound("./src/assets/sounds/level_1/objetos/llave.mp3")
    llave.set_volume(0.1)
    llave.play()


def balas():
    """
    Sonido cuando choca con algo que le da ventaja al personaje
    """
    balas = pygame.mixer.Sound("./src/assets/sounds/level_1/objetos/cartuchos.mp3")
    balas.set_volume(0.1)
    balas.play()


def granada_tomada():
    """
    Sonido cuando choca con algo que le da ventaja al personaje
    """
    granada_tomada = pygame.mixer.Sound(
        "./src/assets/sounds/level_1/objetos/granada_agarrada.mp3"
    )
    granada_tomada.set_volume(0.1)
    granada_tomada.play()


def disparo_shoot():
    """
    Sonido cuando choca con algo que le da ventaja al personaje
    """
    disparo_shoot = pygame.mixer.Sound(
        "./src/assets/sounds/level_1/player/disparo_player.mp3"
    )
    disparo_shoot.set_volume(0.1)
    disparo_shoot.play()


def granada_explocion():
    granada_explocion = pygame.mixer.Sound(
        "./src/assets/sounds/level_1/player/granada.mp3"
    )
    granada_explocion.set_volume(0.1)
    granada_explocion.play()


def herida_dino():
    herida_dino = pygame.mixer.Sound(
        "./src/assets/sounds/level_1/enemigo/herida_dino.mp3"
    )
    herida_dino.set_volume(0.1)
    herida_dino.play()


def disparo_enemigo():
    disparo_enemigo = pygame.mixer.Sound(
        "./src/assets/sounds/level_2/disparo_soldados.mp3"
    )
    disparo_enemigo.set_volume(0.1)
    disparo_enemigo.play()


def piedra():
    piedra = pygame.mixer.Sound("./src/assets/sounds/level_1/objetos/piedra.mp3")
    piedra.set_volume(0.1)
    piedra.play()


def atack_1_boss():
    atack_1_boss = pygame.mixer.Sound("./src/assets/sounds/level_3/atack_1.mp3")
    atack_1_boss.set_volume(0.1)
    atack_1_boss.play()


def atack_2_boss():
    atack_2_boss = pygame.mixer.Sound("./src/assets/sounds/level_3/ataque_2.mp3")
    atack_2_boss.set_volume(0.1)
    atack_2_boss.play()


def music_level_1():
    """
    Sonido del nivel 1
    """
    pygame.mixer.music.load("./src/assets/sounds/level_1/background_sonido.mp3")
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(-1)


def losse():
    """
    Sonido del nivel 1
    """
    pygame.mixer.music.load("./src/assets/sounds/level_1/sond_loose.mp3")
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(-1)


def music_level_2():
    """
    Sonido del nivel 1
    """
    pygame.mixer.music.load("./src/assets/sounds/level_2/sound_lvl_2.mp3")
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(-1)


def music_level_3():
    """
    Sonido del nivel 1
    """
    pygame.mixer.music.load("./src/assets/sounds/level_3/sound_lvl_3.mp3")
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(-1)
