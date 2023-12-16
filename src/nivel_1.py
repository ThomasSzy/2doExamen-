import pygame
from pygame.locals import *
from player import PlayerJumper
from config import *
from sprite_sheet import SpriteSheet
from plataformas import Plataforma, PlataformaInvisible
from images import *
from items import Item
from obstaculos import Obstaculo
from door import Door
from debug import *
from enemy import *
from time_game import Time
from sounds import *

# from explosion import Explosion


class NivelUno:
    def __init__(self) -> None:
        pygame.init()
        self.return_to_menu = False
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font("./src/assets/fonts/game_over.ttf", 50)
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Level 1 ")
        self.all_sprites = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.plataformas = pygame.sprite.Group()
        self.plataformas_invisible = pygame.sprite.Group()
        self.items = pygame.sprite.Group()
        self.obstaculos = pygame.sprite.Group()
        self.doors = pygame.sprite.Group()
        self.player = pygame.sprite.Group()
        self.player_shoots = pygame.sprite.Group()

        self.plataformas_door = pygame.sprite.Group()

        self.time_concurrido_enemy = 0
        self.time_colision_enemy = 500
        self.level_completed = False
        sprite_sheet_player = SpriteSheet(
            player_image.convert_alpha(),
            5,
            4,
            WIDTH_PLAYER,
            HEIGHT_PLAYER,
            ["idle", "right", "left", "front", "jump"],
        )

        sprite_shoot = SpriteSheet(
            player_shoot.convert_alpha(),
            2,
            2,
            64,
            64,
            ["right", "left"],
        )

        sprite_sheet_enemy = SpriteSheet(
            dinos_image_run.convert_alpha(),
            2,
            3,
            WIDTH_DINO,
            HEIGHT_DINO,
            ["left", "right"],
        )
        sprite_sheet_enemy_2 = SpriteSheet(
            dinos_image_run.convert_alpha(),
            2,
            3,
            WIDTH_DINO,
            HEIGHT_DINO,
            ["left", "right"],
        )
        sprite_sheet_enemy_3 = SpriteSheet(
            dinos_image_run.convert_alpha(),
            2,
            3,
            WIDTH_DINO,
            HEIGHT_DINO,
            ["left", "right"],
        )

        self.player = PlayerJumper(
            [self.all_sprites, self.player], sprite_sheet_player, sprite_shoot
        )
        self.enemy_1 = EnemyMoove(
            [self.all_sprites, self.enemies],
            sprite_sheet_enemy,
            (952, 750),
        )

        self.enemy_2 = EnemyMoove(
            [self.all_sprites, self.enemies],
            sprite_sheet_enemy_2,
            (10, 476),
        )
        self.enemy_3 = EnemyMoove(
            [self.all_sprites, self.enemies],
            sprite_sheet_enemy_3,
            (870, 220),
        )

        # items
        self.coin = Item(15, 40, 0, coins_image)
        self.items.add(self.coin)
        self.coin = Item(519, 298, 0, coins_image)
        self.items.add(self.coin)

        self.clock_item = Item(15, 470, 1, clock_image)
        self.items.add(self.clock_item)

        self.key_item = Item(1182, 450, 2, key_image)
        self.items.add(self.key_item)

        self.lives_item = Item(15, 250, 3, live_image)
        self.items.add(self.lives_item)
        self.key_door = self.player.key
        self.door_item = Door(1127, 100, 0, door_lvl_1_image, 3)
        self.doors.add(self.door_item)

        # obstaculos
        self.fire_obstaculo = Obstaculo(480, 780, 0, fire_image)
        self.items.add(self.fire_obstaculo)

        # Tiempo

        # Plataforma

        Plataforma(
            [self.all_sprites, self.plataformas],
            (0, 500, 200, 50),
            platforms_lvl_1_image,
        )
        Plataforma(
            [self.all_sprites, self.plataformas],
            (200, 500, 200, 50),
            platforms_lvl_1_image,
        )

        Plataforma(
            [self.all_sprites, self.plataformas],
            (500, 600, 200, 50),
            platforms_lvl_1_image,
        )

        Plataforma(
            [self.all_sprites, self.plataformas],
            (0, 267, 110, 50),
            platforms_lvl_1_image,
        )
        Plataforma(
            [self.all_sprites, self.plataformas],
            (180, 334, 100, 50),
            platforms_lvl_1_image,
        )
        Plataforma(
            [self.all_sprites, self.plataformas],
            (0, 60, 100, 50),
            platforms_lvl_1_image,
        )

        Plataforma(
            [self.all_sprites, self.plataformas],
            (330, 150, 100, 50),
            platforms_lvl_1_image,
        )

        Plataforma(
            [self.all_sprites, self.plataformas],
            (514, 170, 200, 50),
            platforms_lvl_1_image,
        )

        Plataforma(
            [self.all_sprites, self.plataformas],
            (719, 307, 275, 50),
            platforms_lvl_1_image,
        )

        Plataforma(
            [self.all_sprites, self.plataformas],
            (1075, 158, 200, 50),
            platforms_lvl_1_image,
        )

        Plataforma(
            [self.all_sprites, self.plataformas],
            (1159, 477, 100, 50),
            platforms_lvl_1_image,
        )

        self.salida_door = PlataformaInvisible(
            [self.all_sprites, self.plataformas_door], 50, 50, 1100, 107
        )

        invisible_platform = PlataformaInvisible(
            [self.all_sprites, self.plataformas_invisible], 50, 50, 399, 459
        )
        self.invisible_platform_2 = PlataformaInvisible(
            [self.all_sprites, self.plataformas_invisible], 50, 50, 990, 280
        )
        self.invisible_platform_3 = PlataformaInvisible(
            [self.all_sprites, self.plataformas_invisible], 50, 50, 675, 270
        )

        music_level_1()

    def detect_shoot(self):
        hits = pygame.sprite.groupcollide(self.enemies, self.player_shoots, False, True)

        for hit in hits:
            if hit == self.enemy_1:
                self.player.score += 10
                self.enemy_1.live -= 1
                herida_dino()
            elif hit == self.enemy_2:
                self.player.score += 10
                self.enemy_2.live -= 1
                herida_dino()
            elif hit == self.enemy_3:
                self.player.score += 10
                self.enemy_3.live -= 1
                herida_dino()

            if self.enemy_1.live == 0:
                self.enemy_1.kill()

            if self.enemy_2.live == 0:
                self.enemy_2.kill()

            if self.enemy_3.live == 0:
                self.enemy_3.kill()

        current_time_live = pygame.time.get_ticks()

        if current_time_live - self.time_concurrido_enemy > self.time_colision_enemy:
            hits = pygame.sprite.spritecollide(self.player, self.enemies, False)
            for hit in hits:
                self.player.live -= 1
                mordida()
                if self.player.live <= 0:
                    print("lose")

                self.time_concurrido_enemy = current_time_live

    def dibujar_texto(self, texto, fuente, color, x, y):
        img = fuente.render(texto, True, color)
        self.screen.blit(img, (x, y))

    def draw_debug(self):
        # Dibuja las hitboxes
        for sprite in self.all_sprites.sprites() + self.items.sprites():
            pygame.draw.rect(self.screen, RED, sprite.rect, 2)

    def run(self):
        self.running = True

        while self.running:
            self.time_game = Time(self, self.player)
            self.score_max()
            self.time_game.run()
            self.clock.tick(FPS)
            self.handle_events()
            self.detect_shoot()
            self.draw()
            self.update()
            self.salida()

            if self.player.live <= 0:
                self.show_score_screen()

        self.close()

    def player_live(self):
        self.screen.blit(background_lose.convert_alpha(), (0, 0))

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False
                self.close()

            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    self.player.jump()
                if event.key == K_TAB:
                    cambiar_modo()
                if event.key == K_p:
                    self.screen.blit(background_pause_image, (0, 0))
                    self.dibujar_texto(
                        "Pause", self.font, WITHE, (WIDTH // 2), (HEIGHT // 2)
                    )
                    pygame.display.flip()
                    wait_user()
                if event.key == K_r and self.player.live <= 0:
                    self.restart_game()
                    return
                elif event.key == K_ESCAPE:
                    self.running = False
                    self.close()
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.player.shoot(self)
                    print(f"Clic izquierdo en las coordenadas: {event.pos}")

    def draw(self):
        self.screen.blit(background_lvl_1_image, (0, 0))
        if get_mode():
            self.draw_debug()
        self.items.draw(self.screen)
        self.obstaculos.draw(self.screen)
        self.doors.draw(self.screen)
        self.all_sprites.draw(self.screen)
        self.player.live_player(self.screen)

    def salida(self):
        plataformas_door = pygame.sprite.spritecollide(
            self.player, self.plataformas_door, False
        )
        for plataforma in plataformas_door:
            if self.player.rect.bottom >= plataforma.rect.top and self.player.key >= 1:
                self.level_completed = True
                self.running = False

    def update(self):
        plataformas_player = pygame.sprite.spritecollide(
            self.player, self.plataformas, False
        )
        for plataforma in plataformas_player:
            if (
                self.player.rect.bottom >= plataforma.rect.top
                and self.player.speed_vertical > 0
            ):
                self.player.rect.bottom = plataforma.rect.top
                self.player.speed_vertical = 0
                self.player.can_jump = True

        plataforma_invisible = pygame.sprite.spritecollide(
            self.enemy_2, self.plataformas_invisible, False
        )

        for plataforma in plataforma_invisible:
            if (
                self.enemy_2.rect.right >= plataforma.rect.left
                and self.enemy_2.speed > 0
            ):
                self.enemy_2.direction = "left"

        # Enemigo doble plataforma invisible
        if (
            self.enemy_3.rect.right >= self.invisible_platform_2.rect.left
            and self.enemy_3.speed >= 0
        ):
            self.enemy_3.direction = "left"
        elif self.enemy_3.rect.left <= self.invisible_platform_3.rect.right:
            self.enemy_3.direction = "right"

        self.plataforma_dino(self.enemy_1)
        self.plataforma_dino(self.enemy_2)
        self.plataforma_dino(self.enemy_3)
        self.all_sprites.update()
        self.items.update(self.player)
        self.doors.update(self.player)
        self.dibujar_texto(f"Score:  {self.player.score}", self.font, GOLD, 1100, 0)
        self.time_game.draw(self)
        pygame.display.flip()

    def plataforma_dino(self, enemy):
        plataformas_dino = pygame.sprite.spritecollide(enemy, self.plataformas, False)
        for plataforma in plataformas_dino:
            if enemy.rect.bottom >= plataforma.rect.top and enemy.speed_vertical > 0:
                enemy.rect.bottom = plataforma.rect.top
                enemy.speed_vertical = 0

    def score_max(self):
        directorio = os.getcwd()
        path_completo = os.path.join(directorio, "puntuacion_maxima.txt")

        if os.path.exists(path_completo):
            with open("puntuacion_maxima.txt", "r") as file:
                puntuacion_maxima = int(file.read())

        else:
            puntuacion_maxima = 0

        if self.player.score > puntuacion_maxima:
            with open(path_completo, "w") as file:
                file.write(str(self.player.score))

    def restart_game(self):
        self.__init__()
        self.run()

    def show_score_screen(self):
        self.screen.blit(background_lose.convert_alpha(), (0, 0))
        losse()
        self.dibujar_texto(
            f"{self.player.score}",
            pygame.font.Font("./src/assets/fonts/game_over.ttf", 150),
            WITHE,
            245,
            365,
        )
        self.dibujar_texto(
            "Presiona R para reiniciar",
            self.font,
            WITHE,
            300,
            400,
        )
        pygame.display.flip()

        waiting_for_restart = True
        while waiting_for_restart:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
                    waiting_for_restart = False
                elif event.type == KEYDOWN:
                    if event.key == K_r:
                        self.restart_game()
                        waiting_for_restart = False
                    elif event.key == K_ESCAPE:
                        self.running = False
                        waiting_for_restart = False

    def close(self):
        pygame.quit()


# if __name__ == "__main__":
#     game = NivelUno()
#     game.run()
