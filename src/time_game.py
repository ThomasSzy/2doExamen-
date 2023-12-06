import pygame
from config import *

# from images import background_controls


class Time:
    def __init__(self, game, player) -> None:
        self.font = pygame.font.Font("./src/assets/fonts/game_over.ttf", 50)
        # self.time = time_ticks // 1000
        self.time = pygame.time.get_ticks() // 1000
        self.time_levels = 180
        self.paused = False

        self.pause_start_time = 0
        self.player = player
        self.game = game
        self.is_running = True
        self.time_game = 0


    def run(self):
        self.time_game = self.time_levels - self.time + self.player.time
        if self.time_game <= 0:
            self.game.running = False

    def draw(self, game):
        minutes = self.time_game // 60
        seconds = self.time_game % 60
        tiempo_formateado = f"Tiempo: {minutes:02d}:{seconds:02d}"
        # tiempo_formateado = f"Tiempo: {self.time_game}"
        self.dibujar_texto(tiempo_formateado, WITHE, 550, 0, game)

    def dibujar_texto(self, texto, color, x, y, game):
        img = self.font.render(texto, True, color)
        game.screen.blit(img, (x, y))
