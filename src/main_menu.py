import pygame
from config import *
from images import *


class Menu:
    def __init__(self):
        self.running = True
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.backgrounds = pygame.Surface((WIDTH, HEIGHT))
        pygame.display.set_caption("Time Machine")
        pygame.display.set_icon(
            pygame.image.load("./src/assets/images/icono/icono_game.png")
        )
        self.background_init = pygame.transform.scale(
            background_init_image.convert_alpha(), (WIDTH, HEIGHT)
        )
        self.image_start = pygame.transform.scale(icon_play.convert_alpha(), (60, 60))
        self.image_config = pygame.transform.scale(
            icon_options.convert_alpha(), (80, 60)
        )
        self.image_options = pygame.transform.scale(
            icon_controls.convert_alpha(), (80, 60)
        )
        self.boton_comenzar = pygame.Rect(CENTER_X - BUTTON_WIDTH // 2, 500, 200, 100)
        self.boton_options = pygame.Rect(CENTER_X + 450 // 2, 500, 200, 100)
        self.boton_config = pygame.Rect(CENTER_X - 450, 500, 200, 100)
        self.boton_back = pygame.Rect(CENTER_X - 450, 500, 200, 100)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    cursor = event.pos
                    if self.boton_comenzar.collidepoint(cursor[0], cursor[1]):
                        print("Comenzar")
                    elif self.boton_options.collidepoint(cursor[0], cursor[1]):
                        print("Comenzar")
                    elif self.boton_config.collidepoint(cursor[0], cursor[1]):
                        print("config")

    def render(self):
        self.screen.blit(self.background_init, (0, 0))

        # Dibujar y actualizar los botones
        self.crear_boton(self.screen, self.boton_comenzar, self.image_start, RED, BLUE)
        self.crear_boton(self.screen, self.boton_options, self.image_options, RED, BLUE)
        self.crear_boton(self.screen, self.boton_config, self.image_config, RED, BLUE)

        pygame.display.flip()

    def crear_boton(self, screen, rect, texto, color_normal, color_hover):
        posicion_mouse = pygame.mouse.get_pos()

        if rect.collidepoint(posicion_mouse):
            pygame.draw.rect(screen, color_hover, rect, border_radius=20)
        else:
            pygame.draw.rect(screen, color_normal, rect, border_radius=20)

        self.screen_imagen_boton(screen, texto, rect.centerx, rect.centery)

    def screen_imagen_boton(self, superficie, imagen, x, y):
        rect_imagen = imagen.get_rect(center=(x, y))
        superficie.blit(imagen, rect_imagen)
