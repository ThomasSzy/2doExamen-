import pygame
from pygame.locals import *
from config import *
from sprite_sheet import SpriteSheet
from images import *
from disparo import Disparo, Granada
from sounds import *


class Player(pygame.sprite.Sprite):
    def __init__(
        self,
        groups,
        sprite_sheet: SpriteSheet,
        sprite_sheet_2: SpriteSheet,
        ubication=(0, HEIGHT),
    ):
        super().__init__(groups)
        self.score = 50
        self.time = 0  # AGREGAMOS LUEGO EL TIME COMO PARAMETRO
        self.key = 0

        self.animations = sprite_sheet.get_animations_dict(scale=1)
        self.current_sprite = 0
        self.image = self.animations["right"][self.current_sprite]
        self.rect = self.image.get_rect(topleft=(ubication))

        self.animations_2 = sprite_sheet_2.get_animations_dict(scale=1)
        self.current_sprite_2 = 0
        self.image_2 = self.animations_2["right"][self.current_sprite_2]
        self.rec_2 = self.image_2.get_rect(topleft=(ubication))

        self.mirando = "right"

        # 2,5
        self.speed = 8
        self.last_update = pygame.time.get_ticks()
        self.time_animation = 100

        self.shooting = False
        self.granates = False


class PlayerJumper(Player):
    def __init__(
        self,
        groups,
        sprite_sheet: SpriteSheet,
        sprite_sheet_2,
        ammo=10,
        granates=3,
        live=3,
        ubication=(0, HEIGHT),
    ):
        super().__init__(groups, sprite_sheet, sprite_sheet_2, ubication)
        self.live = live
        self.gravedad = 1
        self.speed_vertical = 0
        self.jump_power = -20
        self.shoot_frame = 0
        self.ammo = ammo
        self.ammo_granates = granates

    def update(self):
        self.speed_vertical += GRAVEDAD

        self.rect.y += self.speed_vertical
        self.jump_player = True
        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT
            self.speed_vertical = 0
            self.can_jump = True

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
                    self.image = self.animations["right"][self.current_sprite]
                    self.mirando = "left"
                    if self.current_sprite == 3:
                        self.current_sprite = 0
                    self.last_update = current_time
        else:
            current_time = pygame.time.get_ticks()
            if current_time - self.last_update >= 600:
                self.current_sprite += 1
                self.image = self.animations["idle"][self.current_sprite]
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

    def ammo_player(self, screen):
        if self.ammo <= 5:
            screen.blit(ammunation_shoot, (423, 8))
        if self.ammo_granates <= 5:
            screen.blit(granate_image_shoot_escalada, (330, 8))

    def jump(self):
        if self.rect.top > 99 and self.can_jump:
            self.speed_vertical = self.jump_power
            self.can_jump = False

    def shoot(self, game):
        if self.ammo >= 1:
            self.ammo -= 1
            disparo_shoot()
            self.shooting = True
            if self.shooting:
                if "right" in self.mirando and self.current_sprite_2 < len(
                    self.animations_2["right"]
                ):
                    self.image = self.animations_2["right"][self.current_sprite_2]
                    self.current_sprite_2 += 1
                    if self.current_sprite_2 == len(self.animations_2["right"]):
                        self.current_sprite_2 = 0
                elif "left" in self.mirando and self.current_sprite_2 < len(
                    self.animations_2["left"]
                ):
                    self.image = self.animations_2["left"][self.current_sprite_2]
                    self.current_sprite_2 += 1
                    if self.current_sprite_2 == len(self.animations_2["left"]):
                        self.current_sprite_2 = 0
            Disparo(
                [game.all_sprites, game.player_shoots], self.rect.midright, self.mirando
            )

    def granate(self, game):
        if self.ammo_granates >= 1:
            self.ammo_granates -= 1
            
            self.granates = True
            if self.granates:
                if "right" in self.mirando and self.current_sprite_2 < len(
                    self.animations_2["right"]
                ):
                    self.image = self.animations_2["right"][self.current_sprite_2]
                    self.current_sprite_2 += 1
                    if self.current_sprite_2 == len(self.animations_2["right"]):
                        self.current_sprite_2 = 0
                elif "left" in self.mirando and self.current_sprite_2 < len(
                    self.animations_2["left"]
                ):
                    self.image = self.animations_2["left"][self.current_sprite_2]
                    self.current_sprite_2 += 1
                    if self.current_sprite_2 == len(self.animations_2["left"]):
                        self.current_sprite_2 = 0
            Granada(
                [game.all_sprites, game.player_granates],
                game,
                self.rect.centerx,
                self.rect.centery,
                self.mirando,
            )
