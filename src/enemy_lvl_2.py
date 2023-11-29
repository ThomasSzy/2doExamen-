import pygame
from pygame.locals import *
from config import *
from sprite_sheet import SpriteSheet
from images import *
from disparo import Disparo


class Enemy(pygame.sprite.Sprite):
    def __init__(self, groups, sprite_sheet: SpriteSheet):
        super().__init__(groups)
        self.score = 50
        self.time = 0  # AGREGAMOS LUEGO EL TIME COMO PARAMETRO
        self.key = 0

        self.animations = sprite_sheet.get_animations_dict(scale=1)
        self.current_sprite = 0
        self.image = self.animations["left"][
            0
        ]  # Tomamos la primera imagen de la animación "left"
        self.speed = 0  # Establecemos la velocidad a 0 para que el enemigo esté quieto
        self.last_update = pygame.time.get_ticks()
        self.time_animation = 1000
        self.mirando = "left"


class EnemyMoove(Enemy):
    def __init__(
        self,
        groups,
        sprite_sheet: SpriteSheet,
        dir,
        ubication=(190, 463),
        live=2,
    ):
        super().__init__(groups, sprite_sheet)
        self.gravedad = 1
        self.speed_vertical = 0
        self.jump_power = -20
        self.rect = self.image.get_rect(midleft=(ubication))
        self.live = live
        self.direction = dir

    def update(self):
        self.speed_vertical += GRAVEDAD
        self.rect.y += self.speed_vertical
        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT
            self.speed_vertical = 0

        if self.direction == "left":
            current_time = pygame.time.get_ticks()
            if current_time - self.last_update >= self.time_animation:
                self.current_sprite += 1
                self.image = self.animations["left"][
                    self.current_sprite % len(self.animations["left"])
                ]
                self.last_update = current_time
        elif self.direction == "right":
            current_time = pygame.time.get_ticks()
            if current_time - self.last_update >= self.time_animation:
                self.current_sprite += 1
                self.image = self.animations["right"][
                    self.current_sprite % len(self.animations["right"])
                ]
                self.last_update = current_time

    def shoot(self, game):
        self.shooting = True
        Disparo(
            [game.all_sprites, game.enemies_shoots], self.rect.midright, self.mirando
        )
