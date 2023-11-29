import pygame
from config import *
from main_menu import *

# CONFIGURACION VER SI LO HAGO O NO


class Controls:
    def __init__(self) -> None:
        """
        Muestra la pantalla de opciones.

        esta funcion se encarga de crear mostrar las opciones del juego y
        poder volver hacia el menu principal.
        """
        pygame.mouse.set_visible(True)
        pygame.mixer.music.stop()
        pygame.display.set_caption("Controls")
        self.background_controls = pygame.transform.scale(
            background_controls.convert_alpha(), (WIDTH, HEIGHT)
        )
        self.running = True
        self.boton_back = pygame.Rect(380, 680, 200, 50)

    def run(self):
        while self.running:
            self.handle_events()
            self.render()
            pygame.time.delay(FPS)
            pygame.display.flip()

        self.close()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    cursor = event.pos
                    if self.boton_back.collidepoint(cursor[0], cursor[1]):
                        ...

    def render(self):
        self.menu.screen.blit(self.background_controls, (0, 0))
        # DESCARGAR FOTO DE CASITA PARA COLOCAR EN EL BOTON
        self.menu.crear_boton(
            self.menu.screen, self.boton_back, self.menu.image_config, RED, BLUE
        )

    def close(self):
        pygame.quit()
