from typing import Any
import pygame
from pygame.locals import *
from config import *
from sounds import *


class Obstaculo(pygame.sprite.Sprite):
    def __init__(self, x, y, obstaculo_type, imagenes_list) -> None:
        pygame.sprite.Sprite.__init__(self)

        # 0 = fire # 1 = Stone
        self.obstaculo_type = obstaculo_type
        self.imagenes_list = imagenes_list
        self.frame_index = 0
        self.last_update = pygame.time.get_ticks()
        # Este self.image toma la primer imagen que tiene la lista
        self.image = self.imagenes_list[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.has_collided = False
        self.collision_timer = 0

    def update(self, player) -> None:
        if self.rect.colliderect(player.rect) and not self.has_collided:
            # fire
            if self.obstaculo_type == 0:
                player.live -= 1
                fuego()
                self.has_collided = True
                self.collision_timer = pygame.time.get_ticks()
            if self.obstaculo_type == 1:
                player.live -= 1
                piedra()
                self.has_collided = True
                self.collision_timer = pygame.time.get_ticks()

        if self.has_collided and pygame.time.get_ticks() - self.collision_timer > 500:
            self.has_collided = False

        self.current_time = 200
        self.image = self.imagenes_list[self.frame_index]

        if pygame.time.get_ticks() - self.last_update > self.current_time:
            self.frame_index += 1
            self.last_update = pygame.time.get_ticks()

            if self.frame_index >= len(self.imagenes_list):
                self.frame_index = 0
