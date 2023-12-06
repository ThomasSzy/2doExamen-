import pygame
from pygame.locals import *
from config import *
import os

##############################################
# ESTAR ATENTO A QUE TENEMOS VARIAS CARPETAS EN LAS IMAGENES PUEDE GENERAR ERROR
##########################################


def escalar_image(image, scale):
    W = image.get_width()
    H = image.get_height()
    new_image = pygame.transform.scale(image, (W * scale, H * scale))
    return new_image


def contar_elementos(directorio):
    return len(os.listdir(directorio))


def lista_image(num_image, ruta_image, scale, lista_image):
    for i in range(num_image):
        img = pygame.image.load(f"{ruta_image}{i+1}.png")
        img = escalar_image(img, scale)
        lista_image.append(img)


# Player


player_image = pygame.image.load("./src/assets/images/player/sprite_ninja_move.png")


# player_kill_attack = pygame.image.load(
#     "./src/assets/images/player/sprite_shoot_arm_kill.png"
# )

player_shoot = pygame.image.load("./src/assets/images/player/sprite_shoot_player_2.png")

ammunation_shoot = pygame.image.load("./src/assets/images/shoot/shoot_player.png")

granate_image_shoot = pygame.image.load("./src/assets/images/shoot/granate/granate.png")
granate_image_shoot_escalada = escalar_image(granate_image_shoot, 1.5)


granate_img = explosion_shoot = pygame.image.load(
    "./src/assets/images/shoot/granate/granate.png"
)
# shoots

shoot_player = pygame.image.load("./src/assets/images/shoot/shoot_player.png")


shoot_enemy = pygame.image.load("./src/assets/images/enemies/shoot/shoot_enemy.png")

# Explosion Img
explosion_image = []
ruta_image = "./src/assets/images/shoot/explosion"
explosion_num_images = contar_elementos(ruta_image)

for i in range(explosion_num_images):
    img = pygame.image.load(f"./src/assets/images/shoot/explosion/exp{i+1}.png")
    img = escalar_image(img, 1)
    explosion_image.append(img)

# granada
# Iconos Image
icon_controls = pygame.image.load("./src/assets/images/buttons/icono_controles.png")
icon_options = pygame.image.load("./src/assets/images/buttons/icono_opciones.png")
icon_play = pygame.image.load("./src/assets/images/buttons/icono_play.png")


# Enemies


# enemy obstacul


# ship

ship_enemy = pygame.image.load("./src/assets/images/enemies/ship_enemy/ship.png")


shoot_ship = pygame.image.load("./src/assets/images/enemies/shoot/shoot_ship.png")


# dino


dinos_image_run = pygame.image.load("./src/assets/images/enemies/sprite_dino_run.png")


warrior_image = pygame.image.load("./src/assets/images/enemies/sprite_soldado_2.png")

# Objets
# Icons Amunnatios/Granates
ammunation_image = []
ruta_image = "./src/assets/images/objets/ammo"
amunnation_num_images = contar_elementos(ruta_image)

for i in range(amunnation_num_images):
    img = pygame.image.load(f"./src/assets/images/objets/ammo/ammo_{i+1}.png")
    img = escalar_image(img, 1)
    ammunation_image.append(img)


granates_image = []
ruta_image = "./src/assets/images/objets/ammo_granates"
granates_num_images = contar_elementos(ruta_image)

for i in range(granates_num_images):
    img = pygame.image.load(
        f"./src/assets/images/objets/ammo_granates/granate_{i+1}.png"
    )
    img = escalar_image(img, 1)
    granates_image.append(img)


# Clock
clock_image = []
ruta_image = "./src/assets/images/objets/clock"
clock_num_images = contar_elementos(ruta_image)

for i in range(clock_num_images):
    img = pygame.image.load(f"./src/assets/images/objets/clock/clock_{i+1}.png")
    img = escalar_image(img, 2)
    clock_image.append(img)


# key
key_image = []
ruta_image = "./src/assets/images/objets/llave"
key_num_images = contar_elementos(ruta_image)
for i in range(key_num_images):
    img = pygame.image.load(f"./src/assets/images/objets/llave/key_{i+1}.png")
    img = escalar_image(img, 1.2)
    key_image.append(img)

# lives
live_image = []
ruta_image = "./src/assets/images/objets/lives"
live_num_images = contar_elementos(ruta_image)
for i in range(live_num_images):
    img = pygame.image.load(f"./src/assets/images/objets/lives/live_{i+1}.png")
    img = escalar_image(img, 1.2)
    live_image.append(img)


# Coins
coins_image = []
ruta_image = "./src/assets/images/objets/coin"
coins_num_images = contar_elementos(ruta_image)

for i in range(coins_num_images):
    img = pygame.image.load(f"./src/assets/images/objets/coin/coin_{i+1}.png")
    img = escalar_image(img, 2)
    coins_image.append(img)


# obstaculos


fire_largo = []
ruta_image = "./src/assets/images/obstaculos/fire_largo"
fire_largo_num_images = contar_elementos(ruta_image)

for i in range(fire_largo_num_images):
    img = pygame.image.load(f"./src/assets/images/obstaculos/fire_largo/fire_{i+1}.png")
    img = escalar_image(img, 1)
    fire_largo.append(img)

fire_lvl_3 = []
ruta_image = "./src/assets/images/obstaculos/fire_lvl_3"
fire_lvl_3_num_images = contar_elementos(ruta_image)

for i in range(fire_lvl_3_num_images):
    img = pygame.image.load(f"./src/assets/images/obstaculos/fire_lvl_3/fire_{i+1}.png")
    img = escalar_image(img, 1.5)
    fire_lvl_3.append(img)


fire_image = []
ruta_image = "./src/assets/images/obstaculos/fire"
fire_num_images = contar_elementos(ruta_image)

for i in range(fire_num_images):
    img = pygame.image.load(f"./src/assets/images/obstaculos/fire/fire_{i+1}.png")
    img = escalar_image(img, 1)
    fire_image.append(img)

# Doors

door_lvl_1_image = []
ruta_image = "./src/assets/images/doors/lvl1"
door_num_images = contar_elementos(ruta_image)
for i in range(door_num_images):
    img = pygame.image.load(f"./src/assets/images/doors/lvl1/door_{i+1}.png")
    img = escalar_image(img, 1)
    door_lvl_1_image.append(img)

door_lvl_2_image = []
ruta_image = "./src/assets/images/doors/lvl2"
door_num_images = contar_elementos(ruta_image)
for i in range(door_num_images):
    img = pygame.image.load(f"./src/assets/images/doors/lvl2/door_{i+1}.png")
    img = escalar_image(img, 1)
    door_lvl_2_image.append(img)


corazon_lleno = pygame.image.load("./src/assets/images/player/live/live_lleno.png")
corazon_lleno = escalar_image(corazon_lleno, 1)


# Stone Obstaculo
stone_obstacle = pygame.image.load("./src/assets/images/obstaculos/stone/stone.png")

# Plataformas LEVEL 3


platform_nube = pygame.image.load(
    "./src/assets/images/platform/plataformas_lvl3/platform_nube.png"
)
platforms_lvl_3 = pygame.image.load(
    "./src/assets/images/platform/plataformas_lvl3/platform_principal.png"
)
platform_dirt = pygame.image.load(
    "./src/assets/images/platform/plataformas_lvl3/platform_dirt.png"
)


platform_stone = pygame.image.load(
    "./src/assets/images/platform/plataformas_lvl3/platform_rock.png"
)
# Backgrounds

# FALTAN BACKGROUND INIT,FINISH,CONFIG,PAUSE,LOSE,BACKGROUND LVL 3.


# FALTA
background_init_image_1 = pygame.image.load(
    "./src/assets/images/backgrounds/background_init.jpg"
)
background_init_image = pygame.transform.scale(background_init_image_1, (1200, 800))

background_controls_1 = pygame.image.load(
    "./src/assets/images/backgrounds/controls_game.jpg"
)
background_controls = pygame.transform.scale(background_controls_1, (1200, 800))

# FALTA
background_finish_image = pygame.image.load(
    "./src/assets/images/Backgrounds/background_level_3.jpg"
)
scaled_background_lvl_3 = pygame.transform.scale(background_finish_image, (1200, 800))
# FALTA
background_lose_1 = pygame.image.load(
    "./src/assets/images/Backgrounds/background_defeat.jpg"
)

background_lose = pygame.transform.scale(background_lose_1, (1200, 800))


background_pause_image_1 = pygame.image.load(
    "./src/assets/images/Backgrounds/background_pause.png"
)

background_pause_image = pygame.transform.scale(background_pause_image_1, (1200, 800))


background_login = pygame.image.load(
    "./src/assets/images/Backgrounds/ingrese_usuario.jpg"
)

background_user = pygame.transform.scale(background_login, (1200, 800))


background_lvl_1_image = pygame.image.load(
    "./src/assets/images/Backgrounds/Background_lvl_1.jpg"
)

background_lvl_2_image = pygame.image.load(
    "./src/assets/images/Backgrounds/Background_lvl2.jpg"
)
scaled_background_lvl_2 = pygame.transform.scale(background_lvl_2_image, (1200, 800))

# FALTA
background_finish = pygame.image.load(
    "./src/assets/images/Backgrounds/background_final.jpg"
).convert_alpha()

scaled_background_finish = pygame.transform.scale(background_finish, (1200, 800))


# Platforms

platforms_lvl_1_image = pygame.image.load(
    "./src/assets/images/platform/plataforma_lvl1.png"
)

platforms_lvl_2_image = pygame.image.load(
    "./src/assets/images/platform/plataforma_lvl2.jpg"
)


# Boss


boss_image = pygame.image.load("./src/assets/images/boss/sprite_boss.png")

attack_boss_1 = pygame.image.load("./src/assets/images/boss/attack_1.png")

attack_boss_2 = pygame.image.load("./src/assets/images/boss/attack_2.png")

# live boss

live_boss_10_normal = pygame.image.load(f"./src/assets/images/boss/live/live_1.png")
live_boss_10 = escalar_image(live_boss_10_normal, 2)

live_boss_9_normal = pygame.image.load(f"./src/assets/images/boss/live/live_2.png")
live_boss_9 = escalar_image(live_boss_9_normal, 2)

live_boss_8_normal = pygame.image.load(f"./src/assets/images/boss/live/live_3.png")
live_boss_8 = escalar_image(live_boss_8_normal, 2)

live_boss_7_normal = pygame.image.load(f"./src/assets/images/boss/live/live_4.png")
live_boss_7 = escalar_image(live_boss_7_normal, 2)

live_boss_6_normal = pygame.image.load(f"./src/assets/images/boss/live/live_5.png")
live_boss_6 = escalar_image(live_boss_6_normal, 2)

live_boss_5_normal = pygame.image.load(f"./src/assets/images/boss/live/live_6.png")
live_boss_5 = escalar_image(live_boss_5_normal, 2)

live_boss_4_normal = pygame.image.load(f"./src/assets/images/boss/live/live_7.png")
live_boss_4 = escalar_image(live_boss_4_normal, 2)

live_boss_3_normal = pygame.image.load(f"./src/assets/images/boss/live/live_8.png")
live_boss_3 = escalar_image(live_boss_3_normal, 2)

live_boss_2_normal = pygame.image.load(f"./src/assets/images/boss/live/live_9.png")
live_boss_2 = escalar_image(live_boss_2_normal, 2)

live_boss_1_normal = pygame.image.load(f"./src/assets/images/boss/live/live_10.png")
live_boss_1 = escalar_image(live_boss_1_normal, 2)

live_boss_0_normal = pygame.image.load(f"./src/assets/images/boss/live/live_11.png")
live_boss_0 = escalar_image(live_boss_0_normal, 2)
