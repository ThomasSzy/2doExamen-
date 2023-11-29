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

player_shoot = pygame.image.load("./src/assets/images/player/sprite_shoot_player.png")

explosion_shoot = pygame.image.load(
    "./src/assets/images/shoot/explosion/explosion_sprite.png"
)


# Iconos Image
icon_controls = pygame.image.load("./src/assets/images/buttons/icono_controles.png")
icon_options = pygame.image.load("./src/assets/images/buttons/icono_opciones.png")
icon_play = pygame.image.load("./src/assets/images/buttons/icono_play.png")


# Enemies
# dino


dinos_image_run = pygame.image.load("./src/assets/images/enemies/sprite_dino_run.png")


warrior_image = pygame.image.load("./src/assets/images/enemies/sprite_soldado_2.png")

# Objets


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


# Backgrounds

# FALTAN BACKGROUND INIT,FINISH,CONFIG,PAUSE,LOSE,BACKGROUND LVL 3.


# FALTA
background_init_image = pygame.image.load(
    "./src/assets/images/backgrounds/background_init.jpg"
)

background_controls = pygame.image.load(
    "./src/assets/images/backgrounds/controls_game.jpg"
)

# FALTA
# background_finish_image = pygame.image.load(
#     "./src/assets/images/Backgrounds/boy.png"
# )

# FALTA
# background_config_image = pygame.image.load(
#     "./src/assets/images/Backgrounds/boy.png"
# )

# FALTA
background_pause_image = pygame.image.load(
    "./src/assets/images/Backgrounds/background_pause.png"
)

# FALTA
# background_lose_image = pygame.image.load("./src/assets/images/Backgrounds/boy.png")

background_lvl_1_image = pygame.image.load(
    "./src/assets/images/Backgrounds/Background_lvl_1.jpg"
)

background_lvl_2_image = pygame.image.load(
    "./src/assets/images/Backgrounds/Background_lvl2.jpg"
)
scaled_background_lvl_2 = pygame.transform.scale(background_lvl_2_image, (1200, 800))

# FALTA
# background_lvl_3_image = pygame.image.load(
#     "./src/assets/images/Backgrounds/boy.png"
# ).convert_alpha()


# Platforms

platforms_lvl_1_image = pygame.image.load(
    "./src/assets/images/platform/plataforma_lvl1.png"
)

platforms_lvl_2_image = pygame.image.load(
    "./src/assets/images/platform/plataforma_lvl2.jpg"
)

# FALTA
# platforms_lvl_3_image = pygame.image.load(
#     "./src/assets/images/platform/plataforma_lvl3.jpg"
# ).convert_alpha()


# Boss


boss_image = pygame.image.load("./src/assets/images/boss/sprite_boss.png")

attack_boss_1 = pygame.image.load("./src/assets/images/boss/attack_1.png")

attack_boss_2 = pygame.image.load("./src/assets/images/boss/attack_2.png")
