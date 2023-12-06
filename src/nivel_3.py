import pygame
from pygame.locals import *
from player import PlayerJumper
from config import *
from sprite_sheet import SpriteSheet
from plataformas import Plataforma, MoovePlatform, PlataformaInvisible
from images import *
from items import Item
from obstaculos import Obstaculo
from debug import *
from time_game import Time
from enemy_lvl_2 import *
from boss import *
from sounds import *

# from explosion import Explosion


class NivelTres:
    def __init__(self) -> None:
        pygame.init()
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font("./src/assets/fonts/game_over.ttf", 50)
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Level 1 ")
        self.is_paused = False
        # pygame.display.set_icon(
        #     pygame.image.load("./src/assets/images//icono.png")
        # )
        # agrego al juego un grupo de sprite
        self.all_sprites = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.plataformas = pygame.sprite.Group()
        self.items = pygame.sprite.Group()
        self.obstaculos = pygame.sprite.Group()
        self.doors = pygame.sprite.Group()
        self.player = pygame.sprite.Group()
        self.player_shoots = pygame.sprite.Group()
        self.player_granates = pygame.sprite.Group()
        self.granates_explote = pygame.sprite.Group()
        self.enemies_shoots = pygame.sprite.Group()
        self.boss_group = pygame.sprite.Group()
        self.boss_shoot = pygame.sprite.Group()
        self.boss_special = pygame.sprite.Group()
        ### ### ### ### ### ### ### ###

        self.time_concurrido_enemy = 0
        self.time_colision_enemy = 500

        ### ### ### ### ### ### ### ### ###
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

        # Boss

        boss_sheet = SpriteSheet(
            boss_image.convert_alpha(),
            5,
            3,
            64,
            77,
            ["live", "left", "right", "left_atack", "right_atack"],
        )

        sprite_sheet_enemy_1 = SpriteSheet(
            ship_enemy.convert_alpha(),
            2,
            2,
            130,
            130,
            ["right", "left"],
        )
        sprite_sheet_enemy_2 = SpriteSheet(
            ship_enemy.convert_alpha(), 2, 2, 130, 130, ["right", "left"]
        )

        self.player = PlayerJumper(
            [self.all_sprites, self.player],
            sprite_sheet_player,
            sprite_shoot,
            12,
            2,
            3,
            (273, HEIGHT),
        )

        self.boss = BossMove(
            [self.all_sprites, self.boss_group], boss_sheet, self, "right", (0, 800)
        )

        self.enemy_1 = EnemyMoove(
            [self.all_sprites, self.enemies],
            sprite_sheet_enemy_1,
            "right",
            self,
            (0, 450),
            3,
            shoot_ship,
            0.5,
        )

        self.enemy_2 = EnemyMoove(
            [self.all_sprites, self.enemies],
            sprite_sheet_enemy_2,
            "left",
            self,
            (1132, 494),
            3,
            shoot_ship,
            0.5,
        )

        # items
        self.coin = Item(220, 199, 0, coins_image)
        self.items.add(self.coin)

        self.coin = Item(180, 199, 0, coins_image)
        self.items.add(self.coin)

        self.coin = Item(260, 199, 0, coins_image)
        self.items.add(self.coin)

        self.lives_item = Item(1174, 770, 3, live_image)
        self.items.add(self.lives_item)

        self.lives_item = Item(1135, 304, 3, live_image)
        self.items.add(self.lives_item)

        self.lives_item = Item(94, 269, 3, live_image)
        self.items.add(self.lives_item)

        self.clock_item = Item(633, 105, 1, clock_image)
        self.items.add(self.clock_item)

        self.ammunation = Item(
            355,
            490,
            4,
            ammunation_image,
        )
        self.items.add(self.ammunation)

        self.ammunation = Item(
            920,
            324,
            4,
            ammunation_image,
        )
        self.items.add(self.ammunation)

        self.granates = Item(170, 490, 5, granates_image)
        self.items.add(self.granates)

        self.granates = Item(950, 324, 5, granates_image)
        self.items.add(self.granates)

        self.stone_obstacle = Obstaculo(50, 740, 1, fire_largo)
        self.items.add(self.stone_obstacle)

        # Plataformas

        self.plataforma_central = Plataforma(
            [self.all_sprites, self.plataformas],
            (450, 585, 200, 70),
            platforms_lvl_3,
        )

        Plataforma(
            [self.all_sprites, self.plataformas],
            (100, 450, 150, 70),
            platforms_lvl_3,
        )

        Plataforma(
            [self.all_sprites, self.plataformas],
            (1011, 317, 150, 70),
            platforms_lvl_3,
        )

        Plataforma(
            [self.all_sprites, self.plataformas],
            (862, 337, 150, 70),
            platforms_lvl_3,
        )

        self.platform_stone_1 = Plataforma(
            [self.all_sprites, self.plataformas],
            (1150, 577, 50, 50),
            platform_stone,
        )

        Plataforma(
            [self.all_sprites, self.plataformas],
            (0, 400, 50, 50),
            platform_stone,
        )

        Plataforma(
            [self.all_sprites, self.plataformas],
            (340, 500, 50, 50),
            platform_stone,
        )

        Plataforma(
            [self.all_sprites, self.plataformas],
            (72, 277, 50, 50),
            platform_stone,
        )

        Plataforma(
            [self.all_sprites, self.plataformas],
            (614, 123, 50, 50),
            platform_stone,
        )
        # plataformas invisibles:

        # Plataforma con movimiento

        self.platform_nube = MoovePlatform(
            [self.all_sprites, self.plataformas],
            (1000, 589, 100, 55),
            platform_nube,
            "right",
        )

        self.platform_nube_2 = MoovePlatform(
            [self.all_sprites, self.plataformas],
            (1000, 200, 100, 55),
            platform_nube,
            "right",
        )

        music_level_3()

    def live_boss(self):
        current_time_live = pygame.time.get_ticks()

        if current_time_live - self.time_concurrido_enemy > 15000:
            print("live")
            if self.boss.live <= 9:
                self.boss.live += 1
                self.time_concurrido_enemy = current_time_live
        if self.boss.live == 5:
            self.boss.speed = 4
        elif self.boss.live <= 4:
            self.boss.speed = 6
        else:
            self.boss.speed = 2

    def detect_shoot(self):
        hits = pygame.sprite.groupcollide(self.enemies, self.player_shoots, False, True)

        for hit in hits:
            if hit == self.enemy_1:
                self.player.score += 10
                self.enemy_1.live -= 1

            if hit == self.enemy_2:
                self.player.score += 10
                self.enemy_2.live -= 1

            if self.enemy_1.live == 0:
                self.enemy_1.kill()
                self.player.ammo += 1

            if self.enemy_2.live == 0:
                self.enemy_2.kill()
                self.player.ammo += 1

        current_time_live = pygame.time.get_ticks()

        if current_time_live - self.time_concurrido_enemy > self.time_colision_enemy:
            hits = pygame.sprite.spritecollide(self.player, self.enemies, False)
            for hit in hits:
                self.player.live -= 1
                if self.player.live == 0:
                    self.player.kill()

                self.time_concurrido_enemy = current_time_live

            # enemies shoots
            hits_enemies = pygame.sprite.spritecollide(
                self.player, self.enemies_shoots, True
            )

            for hit in hits_enemies:
                self.player.live -= 1
                if self.player.live == 0:
                    self.player.kill()

        # boss shoot
        current_time_live = pygame.time.get_ticks()
        if current_time_live - self.time_concurrido_enemy > self.time_colision_enemy:
            hits = pygame.sprite.spritecollide(self.player, self.boss_shoot, False)
            for hit in hits:
                self.player.live -= 1
                if self.player.live == 0:
                    self.player.kill()

                self.time_concurrido_enemy = current_time_live

            hits_enemies = pygame.sprite.spritecollide(
                self.player, self.enemies_shoots, True
            )

        current_time_live = pygame.time.get_ticks()
        if current_time_live - self.time_concurrido_enemy > self.time_colision_enemy:
            hits = pygame.sprite.spritecollide(self.player, self.boss_special, False)
            for hit in hits:
                self.player.live -= 2
                if self.player.live == 0:
                    self.player.kill()

                self.time_concurrido_enemy = current_time_live

            hits_enemies = pygame.sprite.spritecollide(
                self.player, self.enemies_shoots, True
            )

    def detect_explosion(self):
        current_time_live = pygame.time.get_ticks()
        if current_time_live - self.time_concurrido_enemy > self.time_colision_enemy:
            explosiones = pygame.sprite.groupcollide(
                self.enemies, self.granates_explote, False, False
            )
            for explosion in explosiones:
                if explosion == self.enemy_1:
                    self.player.score += 10
                    self.enemy_1.live -= 2
                if explosion == self.enemy_2:
                    self.player.score += 10
                    self.enemy_2.live -= 2

                    self.time_concurrido_enemy = current_time_live

                if self.enemy_1.live <= 0:
                    self.enemy_1.kill()

                if self.enemy_2.live <= 0:
                    self.enemy_2.kill()

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
            self.live_boss()
            self.detect_shoot()
            self.detect_explosion()
            self.explote_boss()
            self.draw()
            self.update()
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
        self.screen.blit(scaled_background_lvl_3, (0, 0))
        if get_mode():
            self.draw_debug()
        self.items.draw(self.screen)
        self.obstaculos.draw(self.screen)
        self.doors.draw(self.screen)
        self.all_sprites.draw(self.screen)
        self.player.live_player(self.screen)
        self.boss.live_boss(self.screen)
        self.player.ammo_player(self.screen)

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

        if (
            self.platform_nube.rect.left <= self.plataforma_central.rect.right
            and self.platform_nube.speed >= 0
        ):
            self.platform_nube.direction = "right"
        elif self.platform_nube.rect.right >= self.platform_stone_1.rect.left:
            self.platform_nube.direction = "left"

        # Plataforma enemy
        self.plataforma_enemy(self.enemy_1)
        self.plataforma_enemy(self.enemy_2)
        self.plataforma_enemy(self.boss)
        self.all_sprites.update()
        self.items.update(self.player)
        self.doors.update(self.player)
        self.dibujar_texto(f"Live Enemy:", self.font, RED, 840, 0)
        self.dibujar_texto(f"Score:  {self.player.score}", self.font, GOLD, 1100, 0)
        self.dibujar_texto(f": {self.player.ammo}", self.font, WITHE, 471, 0)
        self.dibujar_texto(f": {self.player.ammo_granates}", self.font, WITHE, 350, 0)
        self.damage_enemy()
        self.time_game.draw(self)
        pygame.display.flip()

    def damage_enemy(self):
        damages = pygame.sprite.groupcollide(
            self.boss_group, self.player_shoots, False, True
        )

        for damage in damages:
            if damage == self.boss:
                self.player.score += 5
                self.boss.live -= 1

        if self.boss.live <= 0:
            self.boss.kill()
            self.final_game()

        current_time_live = pygame.time.get_ticks()

        if current_time_live - self.time_concurrido_enemy > self.time_colision_enemy:
            damages = pygame.sprite.spritecollide(self.player, self.boss_group, False)
            for damage in damages:
                self.player.live -= 1
                if self.player.live == 0:
                    self.player.kill()

                self.time_concurrido_enemy = current_time_live

    def explote_boss(self):
        current_time_live = pygame.time.get_ticks()
        if current_time_live - self.time_concurrido_enemy > self.time_colision_enemy:
            explosiones = pygame.sprite.groupcollide(
                self.boss_group, self.granates_explote, False, False
            )
            for explosion in explosiones:
                if explosion == self.boss:
                    self.player.score += 10
                    self.boss.live -= 2

                self.time_concurrido_enemy = current_time_live

    def plataforma_enemy(self, enemy):
        plataformas = pygame.sprite.spritecollide(enemy, self.plataformas, False)
        for plataforma in plataformas:
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

    def final_game(self):
        self.screen.blit(scaled_background_finish.convert_alpha(), (0, 0))
        self.dibujar_texto(
            "--Boss Final Eliminado--",
            self.font,
            WITHE,
            (450),
            (140),
        )
        self.dibujar_texto(
            f"{self.player.score}",
            pygame.font.Font("./src/assets/fonts/game_over.ttf", 150),
            GOLD,
            (380),
            (590),
        )

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
