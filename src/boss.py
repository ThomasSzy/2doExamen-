import pygame
from pygame.locals import *
from config import *
from sprite_sheet import SpriteSheet
from images import *
from disparo import Disparo
import random
from sounds import *


class Boss(pygame.sprite.Sprite):
    def __init__(self, groups, sprite_sheet: SpriteSheet):
        super().__init__(groups)
        self.score = 50
        self.time = 0  # AGREGAMOS LUEGO EL TIME COMO PARAMETRO
        self.key = 0

        self.animations = sprite_sheet.get_animations_dict(scale=1)
        self.current_sprite = 0
        self.image = self.animations["left"][0]
        self.speed = 2
        self.last_update = pygame.time.get_ticks()
        self.time_animation = 1000
        self.mirando = "right"


class BossMove(Boss):
    def __init__(
        self,
        groups,
        sprite_sheet: SpriteSheet,
        game,
        dir,
        ubication=(0, 800),
    ):
        super().__init__(groups, sprite_sheet)
        self.gravedad = 1
        self.speed_vertical = 0
        self.jump_power = -20
        self.rect = self.image.get_rect(midleft=(ubication))
        self.live = 10
        self.direction = dir
        self.game = game
        self.last_normal_attack = pygame.time.get_ticks()
        self.normal_attack_interval = 1000

        self.last_especial_attack = pygame.time.get_ticks()
        self.especial_attack_interval = 10000

    def update(self):
        self.speed_vertical += GRAVEDAD
        self.rect.y += self.speed_vertical

        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT
            self.speed_vertical = 0

        if self.rect.right >= WIDTH or self.rect.left <= 0:
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
            current_time = pygame.time.get_ticks()
            if current_time - self.last_update >= self.time_animation:
                self.mirando = "right"
                self.current_sprite += 1

                self.perform_attack(self.game)

                self.image = self.animations["right"][self.current_sprite]
                if self.current_sprite == 2:
                    self.current_sprite = 0
                self.last_update = current_time
        if self.direction == "left":
            self.rect.x -= self.speed
            current_time = pygame.time.get_ticks()
            if current_time - self.last_update >= self.time_animation:
                self.mirando = "left"
                self.current_sprite += 1

                self.perform_attack(self.game)

                self.image = self.animations["left"][self.current_sprite]
                if self.current_sprite == 2:
                    self.current_sprite = 0
                self.last_update = current_time

    def live_boss(self, screen):
        if self.live == 10:
            screen.blit(live_boss_10, (844, 23))
        if self.live == 9:
            screen.blit(live_boss_9, (844, 23))
        if self.live == 8:
            screen.blit(live_boss_8, (844, 23))
        if self.live == 7:
            screen.blit(live_boss_7, (844, 23))
        if self.live == 6:
            screen.blit(live_boss_6, (844, 23))
        if self.live == 5:
            screen.blit(live_boss_5, (844, 23))
        if self.live == 4:
            screen.blit(live_boss_4, (844, 23))
        if self.live == 3:
            screen.blit(live_boss_3, (844, 23))
        if self.live == 2:
            screen.blit(live_boss_2, (844, 23))
        if self.live == 1:
            screen.blit(live_boss_1, (844, 23))
        if self.live == 0:
            screen.blit(live_boss_0, (844, 23))

    def perform_attack(self, game):
        current_time = pygame.time.get_ticks()

        if current_time - self.last_normal_attack >= self.normal_attack_interval:
            self.shoot(game, "normal")
            self.last_normal_attack = current_time

        if current_time - self.last_especial_attack >= self.especial_attack_interval:
            self.shoot(game, "especial")
            self.last_especial_attack = current_time

    def shoot(self, game, attack_type):
        if attack_type == "normal":
            atack_1_boss()
            Disparo(
                [game.all_sprites, game.boss_shoot],
                self.rect.midright,
                self.mirando,
                attack_boss_2,
                (70, 70),
                5,
            )
        elif attack_type == "especial":
            atack_2_boss()
            Disparo(
                [game.all_sprites, game.boss_special],
                self.rect.midright,
                self.mirando,
                attack_boss_1,
                (100, 100),
                5,
            )
