import pygame
from pygame.locals import *
from config import *


class Disparo(pygame.sprite.Sprite):
    def __init__(self, groups, coordenadas, direccion="left") -> None:
        super().__init__(groups)

        self.image = pygame.transform.scale(
            pygame.image.load(
                "./src/assets/images/shoot/shoot_player.png"
            ).convert_alpha(),
            (40, 20),
        )
        self.direccion = direccion

        self.rect = self.image.get_rect(midbottom=coordenadas)
        self.speed = 3

    def update(self):
        if self.direccion == "right":
            self.rect.x += self.speed

        if self.direccion == "left":
            self.rect.x -= self.speed

        if self.direccion == "left":
            self.rotation_angle = 180
        else:
            self.rotation_angle = 0

        self.image = pygame.transform.rotate(self.image, self.rotation_angle)

        if self.rect.bottom < 0:
            self.kill()
