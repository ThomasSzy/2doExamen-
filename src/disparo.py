import pygame
from pygame.locals import *
from config import *
from images import *
from sounds import *


class Disparo(pygame.sprite.Sprite):
    def __init__(
        self,
        groups,
        coordenadas,
        direccion="left",
        image=shoot_player,
        scale=(20, 20),
        speed=3,
    ) -> None:
        super().__init__(groups)

        self.image = pygame.transform.scale(
            image.convert_alpha(),
            (scale),
        )

        self.direccion = direccion

        self.rect = self.image.get_rect(midright=coordenadas)
        self.speed = speed

    def update(self):
        if self.direccion == "right":
            self.rect.x += self.speed

        if self.direccion == "left":
            self.rect.x -= self.speed

        if self.direccion == "left":
            self.rotation_angle = 180
        else:
            self.rotation_angle = 0

        self.image = pygame.transform.rotate(self.image, self.rotation_angle)

        if self.rect.left < 0 or self.rect.left > WIDTH:
            self.kill()


class Granada(pygame.sprite.Sprite):
    def __init__(self, groups, game, x, y, direccion="left") -> None:
        super().__init__(groups)
        # pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.timer = 100
        self.speed_vertical = -11
        self.speed = 5
        self.image = granate_img.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.direccion = direccion
        # self.granates_explote = pygame.sprite.Group()

    def update(self):
        self.speed_vertical += GRAVEDAD_GRANADA
        dx = self.speed
        dy = self.speed_vertical

        if self.rect.left + dx < 0:
            self.direccion = "right"
            dx = self.speed

        if self.direccion == "right":
            self.rect.x += dx
            self.rect.y += dy

        if self.rect.right + dx > WIDTH:
            self.direccion = "left"
            dx = self.speed

        if self.direccion == "left":
            self.rect.x -= dx
            self.rect.y += dy

        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT
            self.speed = 0

        self.timer -= 1
        if self.timer <= 0:
            self.kill()
            Explosion(
                [self.game.all_sprites, self.game.granates_explote],
                self.rect.x,
                self.rect.y,
            )


class Explosion(pygame.sprite.Sprite):
    def __init__(self, groups, x, y) -> None:
        super().__init__(groups)
        self.images = explosion_image
        self.frame_index = 0
        self.image = self.images[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.last_update = pygame.time.get_ticks()
        # self.counter = 0

    def update(self):
        granada_explocion()
        self.current_time = 150
        self.image = self.images[self.frame_index]

        if pygame.time.get_ticks() - self.last_update > self.current_time:
            self.frame_index += 1
            self.last_update = pygame.time.get_ticks()

            if self.frame_index >= len(self.images):
                self.kill()
