import pygame
from sprite_sheet import SpriteSheet
from images import *


class Explosion(pygame.sprite.Sprite):
    def __init__(self, groups, coordenadas) -> None:
        super().__init__(groups)
        self.shoot_explosion = SpriteSheet(
            explosion_shoot,
            3,
            4,
            64,
            64,
        )
        self.animations = self.shoot_explosion.get_animations_dict()
        self.frame = 0
        self.image = self.animations[self.frame]
        self.rect = self.image.get_rect()
        self.rect.center = coordenadas
        self.last_update = pygame.time.get_ticks()
        self.speed_frame = 50

    def update(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_update >= self.speed_frame:
            self.frame += 1
            if self.frame == len(self.animations):
                self.kill()
            else:
                self.image = self.animations[self.frame]
            self.last_update = current_time
