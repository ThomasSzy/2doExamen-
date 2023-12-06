from typing import Any
import pygame
from pygame.locals import *
from config import *
from sounds import *


class Item(pygame.sprite.Sprite):
    def __init__(self, x, y, items_type, imagenes_list) -> None:
        pygame.sprite.Sprite.__init__(self)

        # 0 = monedas, 1=clock, 2=key, 3=live, 4=Ammunation, 5 = Granates
        self.item_type = items_type
        self.imagenes_list = imagenes_list
        self.frame_index = 0
        self.last_update = pygame.time.get_ticks()
        # Este self.image toma la primer imagen que tiene la lista
        self.image = self.imagenes_list[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self, player) -> None:
        # comprobar condicion
        if self.rect.colliderect(player.rect):
            # monedas
            if self.item_type == 0:
                player.score += 50
                moneda()
            elif self.item_type == 1:
                player.time += 30
                reloj()

            elif self.item_type == 2:
                player.key += 1
                llave()

            elif self.item_type == 3:
                player.live += 1
                corazon()
                if player.live >= 3:
                    player.live = 3

            elif self.item_type == 4:
                player.ammo += 3
                balas()

                if player.ammo >= 5:
                    player.ammo = 5

            elif self.item_type == 5:
                player.ammo_granates += 1
                granada_tomada()

                if player.ammo_granates >= 5:
                    player.ammo_granates = 5

            self.kill()

        self.current_time = 150
        self.image = self.imagenes_list[self.frame_index]

        if pygame.time.get_ticks() - self.last_update > self.current_time:
            self.frame_index += 1
            self.last_update = pygame.time.get_ticks()

            if self.frame_index >= len(self.imagenes_list):
                self.frame_index = 0
