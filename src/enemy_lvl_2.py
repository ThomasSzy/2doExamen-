import pygame
from pygame.locals import *
from config import *
from sprite_sheet import SpriteSheet
from images import *
from disparo import Disparo
from sounds import *


class Enemy(pygame.sprite.Sprite):
    def __init__(self, groups, sprite_sheet: SpriteSheet, scale=1, gravedad=0):
        super().__init__(groups)
        self.score = 50
        self.time = 0  # AGREGAMOS LUEGO EL TIME COMO PARAMETRO
        self.key = 0
        self.scale = scale

        self.animations = sprite_sheet.get_animations_dict(self.scale)
        self.current_sprite = 0
        self.image = self.animations["left"][
            0
        ]  # Tomamos la primera imagen de la animación "left"
        self.speed = 0  # Establecemos la velocidad a 0 para que el enemigo esté quieto
        self.last_update = pygame.time.get_ticks()
        self.time_animation = 3000
        self.mirando = "self"
        self.shoot_timer = pygame.time.get_ticks()
        self.shoot_interval = 3000


class EnemyMoove(Enemy):
    def __init__(
        self,
        groups,
        sprite_sheet: SpriteSheet,
        dir,
        game,
        ubication=(190, 463),
        live=2,
        image=shoot_enemy,
        scale=1,
    ):
        super().__init__(groups, sprite_sheet, scale)
        self.gravedad = 1
        self.speed_vertical = 0
        self.jump_power = -20
        self.rect = self.image.get_rect(midleft=(ubication))
        self.live = live
        self.direction = dir
        self.game = game
        self.image_shoot = image

    def update(self):
        self.speed_vertical += GRAVEDAD
        self.rect.y += self.speed_vertical
        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT
            self.speed_vertical = 0

        if self.direction == "left":
            current_time = pygame.time.get_ticks()
            if current_time - self.last_update >= self.time_animation:
                self.mirando = "left"
                self.shoot(self.game)
                self.shoot_timer = current_time
                self.current_sprite += 1
                self.image = self.animations["left"][
                    self.current_sprite % len(self.animations["left"])
                ]
                self.last_update = current_time
        elif self.direction == "right":
            current_time = pygame.time.get_ticks()
            if current_time - self.last_update >= self.time_animation:
                self.mirando = "right"
                self.shoot(self.game)
                self.shoot_timer = current_time
                self.current_sprite += 1
                self.image = self.animations["right"][
                    self.current_sprite % len(self.animations["right"])
                ]
                self.last_update = current_time

    def shoot(
        self,
        game,
    ):
        self.shooting = True
        disparo_enemigo()
        Disparo(
            [game.all_sprites, game.enemies_shoots],
            self.rect.midright,
            self.mirando,
            self.image_shoot,
            (40, 30),
        )
