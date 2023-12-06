import pygame
from random import randint
from sys import *
from pygame import *
from images import *
from config import *
from nivel_1 import NivelUno
from nivel_2 import NivelDos
from nivel_3 import NivelTres


def main_menu():
    centro_x = SCREEN.get_width() // 2
    button_width = 200
    button_heigth = 50
    boton_comenzar = pygame.Rect(centro_x - button_width // 2, 400, 200, 50)
    boton_options = pygame.Rect(centro_x - button_width // 2, 500, 200, 50)
    boton_quit = pygame.Rect(centro_x - button_width // 2, 600, 200, 50)
    boton_back = pygame.Rect(centro_x - button_width // 2, 500, 200, 50)
    font = pygame.font.SysFont(None, 30)
    # musica_intro()
    while True:
        pygame.mouse.set_visible(True)
        run_lvl_1 = True
        run_lvl_2 = False
        run_lvl_3 = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    cursor = event.pos
                    if boton_comenzar.collidepoint(cursor[0], cursor[1]):
                        if run_lvl_1:
                            nivel_uno = NivelUno()
                            nivel_uno.run()
                            run_lvl_1 = False

                        if nivel_uno.level_completed:
                            nivel_dos = NivelDos()
                            nivel_dos.run()
                            run_lvl_2 = False

                        if nivel_dos.level_completed:
                            nivel_tres = NivelTres()
                            nivel_tres.run()
                            run_lvl_3 = False

                    elif boton_options.collidepoint(cursor[0], cursor[1]):
                        options()
                    elif boton_quit.collidepoint(cursor[0], cursor[1]):
                        exit()

        SCREEN.blit(background_init_image, (0, 0))

        crear_boton(
            SCREEN,
            boton_comenzar,
            "Comenzar",
            WITHE,
            BLUE,
        )
        crear_boton(
            SCREEN,
            boton_options,
            "Opciones",
            WITHE,
            BLUE,
        )
        crear_boton(
            SCREEN,
            boton_quit,
            "Salir",
            WITHE,
            BLUE,
        )

        pygame.display.flip()


def options():
    """
    Muestra la pantalla de opciones.

    esta funcion se encarga de crear mostrar las opciones del juego y
    poder volver hacia el menu principal.
    """
    pygame.mixer.music.stop()
    pygame.display.set_caption("Options")

    while True:
        pygame.mouse.set_visible(True)

        boton_back = pygame.Rect(380, 680, 200, 50)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    cursor = event.pos
                    if boton_back.collidepoint(cursor[0], cursor[1]):
                        pygame.display.set_caption("The Simpsons")
                        main_menu()

        SCREEN.blit(background_controls, (0, 0))
        crear_boton(
            SCREEN,
            boton_back,
            "Back",
            WITHE,
            BLUE,
        )
        pygame.display.flip()


def crear_boton(screen, rect, texto, color_normal, color_hover):
    """
    Crea los botones y su iteracion

    Args:
        screen (int): tamaño de pantalla
        rect (int): rectangulo del boton
        texto (str): texto que muestra el boton
        color_normal (str): Color principal
        color_hover (str): Color al pasar el mouse por encima
    """
    posicion_mouse = pygame.mouse.get_pos()

    if rect.collidepoint(posicion_mouse):
        pygame.draw.rect(screen, color_hover, rect, border_radius=20)
    else:
        pygame.draw.rect(screen, color_normal, rect, border_radius=20)

    screen_text_boton(screen, texto, rect.centerx, rect.centery)


def screen_text_boton(superficie, texto, x, y, font_size=24, color=BLACK):
    """
    Muestra el texto del boton

    Args:
        superficie (int): donde se coloca el boton
        texto (str): El texto que va encima del boton
        x (int): Posicion del rect en el eje x
        y (int): Posicion del rect en el eje y
        font_size (int): tamaño de fuente
        color (str): Color del texto
    """
    fuente = pygame.font.SysFont("comicsans", font_size)
    render = fuente.render(texto, True, color)
    rect_text = render.get_rect(center=(x, y))
    superficie.blit(render, rect_text)
