import pygame
from config import *
from images import *
from main_menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.main_menu = Menu()

    def run(self):
        while self.main_menu.running:
            self.main_menu.handle_events()
            self.main_menu.render()
            pygame.time.delay(FPS)


if __name__ == "__main__":
    game = Game()
    game.run()
