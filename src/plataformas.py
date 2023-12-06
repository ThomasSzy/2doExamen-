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
    def __init__(self, groups, width, height, x, y):
        super().__init__(groups)
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)


class MoovePlatform(Plataforma):
    def __init__(
        self, groups, rectangulo: pygame.rect, image_platform=None, direction="right"
    ) -> None:
        super().__init__(groups, rectangulo, image_platform)
        self.speed = 1
        self.direction = direction

    def update(self):
        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT

        if self.rect.right >= WIDTH or self.rect.left <= 0:
            # Cambia la dirección del enemigo
            if self.direction == "right":
                self.direction = "left"
            else:
                self.direction = "right"

            if self.direction == "left":
                self.rect.right = WIDTH
            else:
                self.rect.left = 0
        if self.direction == "right":
            self.rect.x += self.speed
        if self.direction == "left":
            self.rect.x -= self.speed
