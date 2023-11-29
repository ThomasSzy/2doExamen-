import pygame
from pygame.locals import *
from config import *
from config import pygame


class Plataforma(pygame.sprite.Sprite):
    def __init__(self, groups, rectangulo: pygame.rect, image_platform=None) -> None:
        super().__init__(groups)
        self.image = image_platform.convert_alpha()
        self.image = pygame.transform.scale(self.image, (rectangulo[2], rectangulo[3]))
        self.rect = self.image.get_rect(topleft=(rectangulo[0], rectangulo[1]))


class DrawPlatforms(Plataforma):
    def __init__(self, groups, rectangulo, image_platform) -> None:
        super().__init__(groups, rectangulo, image_platform)


class PlataformaInvisible(pygame.sprite.Sprite):
    def __init__(self, width, height, x, y):
        super().__init__()
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
