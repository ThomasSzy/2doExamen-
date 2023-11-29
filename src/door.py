from typing import Any
import pygame
from pygame.locals import *
from config import *


class Door(pygame.sprite.Sprite):
    def __init__(self, x, y, items_type, imagenes_list, frames) -> None:
        pygame.sprite.Sprite.__init__(self)
        # 0 = door 1.   1 = door 2
        self.frame = frames
        self.item_type = items_type
        self.imagenes_list = imagenes_list
        self.frame_index = 0
        self.last_update = pygame.time.get_ticks()
        # Este self.image toma la primer imagen que tiene la lista
        self.image = self.imagenes_list[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect = (x, y)

    def update(self, player) -> None:
        if player.key == 1:
            self.current_time = 300
            self.image = self.imagenes_list[self.frame_index]

            if pygame.time.get_ticks() - self.last_update > self.current_time:
                self.frame_index += 1
                self.last_update = pygame.time.get_ticks()

                if self.frame_index >= len(self.imagenes_list):
                    self.frame_index = self.frame
