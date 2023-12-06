import pygame
from config import *


class SpriteSheet:
    def __init__(self, sheet, rows, cols, width, height, keys=None):
        self.sheet = sheet
        self.width = self.sheet.get_width()
        self.height = self.sheet.get_height()
        self.rows = rows
        self.cols = cols
        self.width_sprite = width
        self.height_sprite = height
        self.keys = keys

    def get_animations(self, scale):
        self.width = scale * self.width
        self.height = scale * self.height
        self.width_sprite = scale * self.width_sprite
        self.height_sprite = scale * self.height_sprite
        # Agrandamos lo el tamaño del sprite

        self.sheet = pygame.transform.scale(self.sheet, (self.width, self.height))

        contador_columnas = 0
        animation_list = []

        for row in range(self.rows):
            animation_row = []
            for _ in range(
                self.cols
            ):  # -> Cuando no vamos a usar un for lo usamos como _ solo lo usamos para que itere 5 veces
                animation_row.append(
                    self.sheet.subsurface(
                        contador_columnas * self.width_sprite,
                        row * self.height_sprite,
                        self.width_sprite,
                        self.height_sprite,
                    )
                )  # ---> Le pasamos lo que miden esos rectangulos
                contador_columnas += 1

            contador_columnas = 0
            animation_list.append(animation_row)

        return animation_list

    def get_animations_dict(self, scale=1):
        self.width = scale * self.width
        self.height = scale * self.height
        self.width_sprite = scale * self.width_sprite
        self.height_sprite = scale * self.height_sprite
        # Agrandamos lo el tamaño del sprite

        self.sheet = pygame.transform.scale(self.sheet, (self.width, self.height))

        contador_columnas = 0
        animation_dict = {}

        for row in range(self.rows):
            animation_row = []
            for _ in range(
                self.cols
            ):  # -> Cuando no vamos a usar un for lo usamos como _ solo lo usamos para que itere 5 veces
                animation_row.append(
                    self.sheet.subsurface(
                        contador_columnas * self.width_sprite,
                        row * self.height_sprite,
                        self.width_sprite,
                        self.height_sprite,
                    )
                )  # ---> Le pasamos lo que miden esos rectangulos
                contador_columnas += 1

            animation_dict[self.keys[row]] = animation_row
            contador_columnas = 0

        return animation_dict
