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
from time_game import Time
from enemy_lvl_2 import *

# from explosion import Explosion


class NivelDos:
    def __init__(self) -> None:
        pygame.init()
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font("./src/assets/fonts/game_over.ttf", 50)
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Level 1 ")
        self.is_paused = False
        self.all_sprites = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.plataformas = pygame.sprite.Group()
        self.plataformas_invisible = pygame.sprite.Group()
        self.items = pygame.sprite.Group()
        self.obstaculos = pygame.sprite.Group()
        self.doors = pygame.sprite.Group()
        self.player = pygame.sprite.Group()
        self.player_shoots = pygame.sprite.Group()
        self.player_granates = pygame.sprite.Group()
        self.granates_explote = pygame.sprite.Group()
        self.enemies_shoots = pygame.sprite.Group()

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

        sprite_sheet_enemy_1 = SpriteSheet(
            warrior_image.convert_alpha(),
            4,
            2,
            WIDTH_WARR,
            HEIGHT_WARR,
            ["right", "left", "kill_right", "kill_left"],
        )
        sprite_sheet_enemy_2 = SpriteSheet(
            warrior_image.convert_alpha(),
            4,
            2,
            WIDTH_WARR,
            HEIGHT_WARR,
            ["right", "left", "kill_right", "kill_left"],
        )
        sprite_sheet_enemy_3 = SpriteSheet(
            warrior_image.convert_alpha(),
            4,
            2,
            WIDTH_WARR,
            HEIGHT_WARR,
            ["right", "left", "kill_right", "kill_left"],
        )

        sprite_sheet_enemy_4 = SpriteSheet(
            warrior_image.convert_alpha(),
            4,
            2,
            WIDTH_WARR,
            HEIGHT_WARR,
            ["right", "left", "kill_right", "kill_left"],
        )

        self.player = PlayerJumper(
            [self.all_sprites, self.player], sprite_sheet_player, sprite_shoot, 2, 2
        )
        self.enemy_1 = EnemyMoove(
            [self.all_sprites, self.enemies],
            sprite_sheet_enemy_1,
            "left",
            self,
            (1081, 764),
        )

        self.enemy_2 = EnemyMoove(
            [self.all_sprites, self.enemies],
            sprite_sheet_enemy_2,
            "right",
            self,
            (580, 487),
        )
        self.enemy_3 = EnemyMoove(
            [self.all_sprites, self.enemies],
            sprite_sheet_enemy_3,
            "right",
            self,
            (67, 488),
        )

        self.enemy_4 = EnemyMoove(
            [self.all_sprites, self.enemies],
            sprite_sheet_enemy_3,
            "left",
            self,
            (1130, 147),
        )

        # items
        self.coin = Item(87, 76, 0, coins_image)
        self.items.add(self.coin)
        self.coin = Item(519, 298, 0, coins_image)
        self.items.add(self.coin)
        self.coin = Item(10, 76, 0, coins_image)
        self.items.add(self.coin)
        self.coin = Item(163, 76, 0, coins_image)
        self.items.add(self.coin)

        self.key_item = Item(1185, 317, 2, key_image)
        self.items.add(self.key_item)

        self.lives_item = Item(15, 330, 3, live_image)
        self.items.add(self.lives_item)

        self.lives_item = Item(600, 245, 3, live_image)
        self.items.add(self.lives_item)

        self.ammunation = Item(
            1078,
            636,
            4,
            ammunation_image,
        )
        self.items.add(self.ammunation)

        self.granates = Item(21, 497, 5, granates_image)
        self.items.add(self.granates)

        self.key_door = self.player.key
        self.door_item = Door(0, 730, 0, door_lvl_2_image, 2)
        self.doors.add(self.door_item)

        # obstaculos
        self.fire_obstaculo = Obstaculo(1180, 663, 0, fire_image)
        self.items.add(self.fire_obstaculo)

        self.stone_obstacle = Obstaculo(727, 800, 1, [stone_obstacle])
        self.items.add(self.stone_obstacle)

        # Plataformas

        Plataforma(
            [self.all_sprites, self.plataformas],
            (1000, 663, 200, 50),
            platforms_lvl_2_image,
        )

        Plataforma(
            [self.all_sprites, self.plataformas],
            (1000, 770, 30, 30),
            platforms_lvl_2_image,
        )

        Plataforma(
            [self.all_sprites, self.plataformas],
            (746, 492, 200, 25),
            platforms_lvl_2_image,
        )

        Plataforma(
            [self.all_sprites, self.plataformas],
            (557, 492, 70, 25),
            platforms_lvl_2_image,
        )

        Plataforma(
            [self.all_sprites, self.plataformas],
            (420, 462, 70, 25),
            platforms_lvl_2_image,
        )

        Plataforma(
            [self.all_sprites, self.plataformas],
            (290, 484, 70, 25),
            platforms_lvl_2_image,
        )

        Plataforma(
            [self.all_sprites, self.plataformas],
            (0, 350, 250, 25),
            platforms_lvl_2_image,
        )

        Plataforma(
            [self.all_sprites, self.plataformas],
            (0, 520, 230, 25),
            platforms_lvl_2_image,
        )

        Plataforma(
            [self.all_sprites, self.plataformas],
            (324, 180, 200, 25),
            platforms_lvl_2_image,
        )

        Plataforma(
            [self.all_sprites, self.plataformas],
            (0, 87, 200, 25),
            platforms_lvl_2_image,
        )

        Plataforma(
            [self.all_sprites, self.plataformas],
            (700, 180, 200, 25),
            platforms_lvl_2_image,
        )
        Plataforma(
            [self.all_sprites, self.plataformas],
            (780, 180, 200, 25),
            platforms_lvl_2_image,
        )

        Plataforma(
            [self.all_sprites, self.plataformas],
            (1150, 180, 70, 25),
            platforms_lvl_2_image,
        )

        Plataforma(
            [self.all_sprites, self.plataformas],
            (1177, 339, 70, 25),
            platforms_lvl_2_image,
        )

        Plataforma(
            [self.all_sprites, self.plataformas],
            (570, 262, 70, 25),
            platforms_lvl_2_image,
        )

        self.salida_door = PlataformaInvisible(
            [self.all_sprites, self.plataformas_door], 50, 50, 0, 750
        )

        music_level_2()

    def detect_shoot(self):
        hits = pygame.sprite.groupcollide(self.enemies, self.player_shoots, False, True)

        for hit in hits:
            if hit == self.enemy_1:
                self.player.score += 10
                self.enemy_1.live -= 1
            elif hit == self.enemy_2:
                self.player.score += 10
                self.enemy_2.live -= 1

            elif hit == self.enemy_3:
                self.player.score += 10
                self.enemy_3.live -= 1

            elif hit == self.enemy_4:
                self.player.score += 10
                self.enemy_4.live -= 1

            if self.enemy_1.live == 0:
                self.enemy_1.kill()

            if self.enemy_2.live == 0:
                self.enemy_2.kill()

            if self.enemy_3.live == 0:
                self.enemy_3.kill()

            if self.enemy_4.live == 0:
                self.enemy_4.kill()

        current_time_live = pygame.time.get_ticks()

        if current_time_live - self.time_concurrido_enemy > self.time_colision_enemy:
            hits = pygame.sprite.spritecollide(self.player, self.enemies, False)
            for hit in hits:
                self.player.live -= 1
                if self.player.live == 0:
                    self.player.kill()

                self.time_concurrido_enemy = current_time_live

            # def hit_enemie(self):
            hits_enemies = pygame.sprite.spritecollide(
                self.player, self.enemies_shoots, True
            )

            for hit in hits_enemies:
                self.player.live -= 1
                if self.player.live == 0:
                    self.player.kill()

    def detect_explosion(self):
        explosiones = pygame.sprite.groupcollide(
            self.enemies, self.granates_explote, False, False
        )
        for explosion in explosiones:
            if explosion == self.enemy_1:
                self.player.score += 10
                self.enemy_1.live -= 1
            elif explosion == self.enemy_2:
                self.player.score += 10
                self.enemy_2.live -= 1

            elif explosion == self.enemy_3:
                self.player.score += 10
                self.enemy_3.live -= 1

            elif explosion == self.enemy_4:
                self.player.score += 10
                self.enemy_4.live -= 1

            if self.enemy_1.live == 0:
                self.enemy_1.kill()

            if self.enemy_2.live == 0:
                self.enemy_2.kill()

            if self.enemy_3.live == 0:
                self.enemy_3.kill()

            if self.enemy_4.live == 0:
                self.enemy_4.kill()

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
            self.time_game.run()
            self.clock.tick(FPS)
            self.handle_events()
            self.detect_shoot()
            self.detect_explosion()
            self.draw()
            self.update()
            self.salida()

            if self.player.live <= 0:
                self.show_score_screen()
        self.close()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    self.player.jump()
                if event.key == K_TAB:
                    cambiar_modo()
                if event.key == K_p:
                    self.pause()
                if event.key == K_r and self.player.live <= 0:
                    self.restart_game()
                    return

            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.player.shoot(self)
                    print(f"Clic izquierdo en las coordenadas: {event.pos}")
                if event.button == 3:
                    self.player.granate(self)

    def draw(self):
        self.screen.blit(scaled_background_lvl_2, (0, 0))
        if get_mode():
            self.draw_debug()
        self.items.draw(self.screen)
        self.obstaculos.draw(self.screen)
        self.doors.draw(self.screen)
        self.all_sprites.draw(self.screen)
        self.player.live_player(self.screen)
        self.player.ammo_player(self.screen)

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

        plataformas_granadas = pygame.sprite.groupcollide(
            self.player_granates, self.plataformas, False, False
        )
        for granada, plataformas_colisionadas in plataformas_granadas.items():
            for plataforma in plataformas_colisionadas:
                if (
                    granada.rect.bottom >= plataforma.rect.top
                    and granada.rect.top <= plataforma.rect.top
                    and granada.speed_vertical > 0
                ):
                    granada.rect.bottom = plataforma.rect.top
                    granada.speed_vertical = 0
                    granada.speed = 0

        # Plataforma enemy
        self.plataforma_enemy(self.enemy_1)
        self.plataforma_enemy(self.enemy_2)
        self.plataforma_enemy(self.enemy_3)
        self.plataforma_enemy(self.enemy_4)
        self.all_sprites.update()
        self.items.update(self.player)
        self.doors.update(self.player)
        self.dibujar_texto(f"Score:  {self.player.score}", self.font, GOLD, 1100, 0)
        self.dibujar_texto(f": {self.player.ammo}", self.font, WITHE, 471, 0)
        self.dibujar_texto(f": {self.player.ammo_granates}", self.font, WITHE, 350, 0)
        self.time_game.draw(self)
        pygame.display.flip()

    def plataforma_enemy(self, enemy):
        plataformas_dino = pygame.sprite.spritecollide(enemy, self.plataformas, False)
        for plataforma in plataformas_dino:
            if enemy.rect.bottom >= plataforma.rect.top and enemy.speed_vertical > 0:
                enemy.rect.bottom = plataforma.rect.top
                enemy.speed_vertical = 0

    def pause(self):
        self.ticks_pause = pygame.time.get_ticks()

        self.time_game.pause_start_time = self.ticks_pause
        self.screen.blit(background_pause_image.convert_alpha(), (0, 0))
        self.dibujar_texto("Pause", self.font, WITHE, (WIDTH // 2), (HEIGHT // 2))
        pygame.display.flip()
        wait_user()

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
#     game = NivelDos()
#     game.run()
