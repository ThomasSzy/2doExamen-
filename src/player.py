import pygame
from pygame.locals import *
from config import *
from sprite_sheet import SpriteSheet
from images import *
from disparo import Disparo


class Player(pygame.sprite.Sprite):
    def __init__(
        self,
        groups,
        sprite_sheet: SpriteSheet,
        ubication=(0, HEIGHT),
    ):
        super().__init__(groups)
        self.score = 50
        self.time = 0  # AGREGAMOS LUEGO EL TIME COMO PARAMETRO
        self.key = 0

        self.animations = sprite_sheet.get_animations_dict(scale=1)
        self.current_sprite = 0
        self.image = self.animations["rigth"][self.current_sprite]
        self.rect = self.image.get_rect(topleft=(ubication))

        self.mirando = "right"

        self.speed = 2
        self.last_update = pygame.time.get_ticks()
        self.time_animation = 100

        self.shooting = False


class PlayerJumper(Player):
    def __init__(
        self,
        groups,
        sprite_sheet: SpriteSheet,
        live=3,
    ):
        super().__init__(groups, sprite_sheet)
        self.live = live
        self.gravedad = 1
        self.speed_vertical = 0
        self.jump_power = -20
        self.shoot_frame = 0

    def update(self):
        self.speed_vertical += GRAVEDAD

        self.rect.y += self.speed_vertical
        self.jump_player = True
        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT
            self.speed_vertical = 0

        keys = pygame.key.get_pressed()
        if keys[K_d]:
            if self.rect.right <= WIDTH:
                self.rect.x += self.speed
                current_time = pygame.time.get_ticks()
                if current_time - self.last_update >= self.time_animation:
                    self.current_sprite += 1
                    self.image = self.animations["left"][self.current_sprite]
                    self.mirando = "right"
                    if self.current_sprite == 3:
                        self.current_sprite = 0
                    self.last_update = current_time

        if keys[K_a]:
            if self.rect.left >= 0:
                self.rect.x -= self.speed
                current_time = pygame.time.get_ticks()
                if current_time - self.last_update >= self.time_animation:
                    self.current_sprite += 1
                    self.image = self.animations["rigth"][self.current_sprite]
                    self.mirando = "left"
                    if self.current_sprite == 3:
                        self.current_sprite = 0
                    self.last_update = current_time

    def live_player(self, screen):
        if self.live == 3:
            screen.blit(corazon_lleno, (20, 10))
            screen.blit(corazon_lleno, (60, 10))
            screen.blit(corazon_lleno, (100, 10))
        elif self.live == 2:
            screen.blit(corazon_lleno, (20, 10))
            screen.blit(corazon_lleno, (60, 10))
        elif self.live == 1:
            screen.blit(corazon_lleno, (20, 10))

    def jump(self):
        if self.rect.top > 99:
            self.speed_vertical = self.jump_power

    def shoot(self, game):
        self.shooting = True
        Disparo(
            [game.all_sprites, game.player_shoots], self.rect.midright, self.mirando
        )
