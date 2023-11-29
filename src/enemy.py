import pygame
from pygame.locals import *
from config import *
from sprite_sheet import SpriteSheet
from images import *


class Enemy(pygame.sprite.Sprite):
    def __init__(self, groups, sprite_sheet: SpriteSheet):
        super().__init__(groups)
        self.score = 50
        self.time = 0  # AGREGAMOS LUEGO EL TIME COMO PARAMETRO
        self.key = 0

        self.animations = sprite_sheet.get_animations_dict(scale=1)
        self.current_sprite = 0
        self.image = self.animations["left"][self.current_sprite]
        self.speed = 2
        self.last_update = pygame.time.get_ticks()
        self.time_animation = 1000
        self.direction = "right"
        

class EnemyMoove(Enemy):
    def __init__(self, groups, sprite_sheet: SpriteSheet, ubication=(190, 463), live=2):
        super().__init__(groups, sprite_sheet)
        self.gravedad = 1
        self.speed_vertical = 0
        self.jump_power = -20
        self.rect = self.image.get_rect(midleft=(ubication))
        self.live = live

    def update(self):
        self.speed_vertical += GRAVEDAD
        self.rect.y += self.speed_vertical
        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT
            self.speed_vertical = 0

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
            current_time = pygame.time.get_ticks()
            if current_time - self.last_update >= self.time_animation:
                self.current_sprite += 1
                self.image = self.animations["right"][self.current_sprite]
                if self.current_sprite == 2:
                    self.current_sprite = 0
                self.last_update = current_time
        if self.direction == "left":
            self.rect.x -= self.speed
            current_time = pygame.time.get_ticks()
            if current_time - self.last_update >= self.time_animation:
                self.current_sprite += 1
                self.image = self.animations["left"][self.current_sprite]
                if self.current_sprite == 2:
                    self.current_sprite = 0
                self.last_update = current_time
