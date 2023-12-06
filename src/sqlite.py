import sqlite3
import pygame


def gestionar_base_datos(nombre, score):
    with sqlite3.connect("Usuarios.db") as conexion:
        conexion.execute(
            "CREATE TABLE IF NOT EXISTS usuario (Nombre TEXT, score INTEGER)"
        )
        # try:
        #     conexion.execute(
        #         "INSERT INTO usuario (Nombre, score) VALUES (?, ?)", (nombre, score)
        #     )
        #     conexion.commit()
        #     print("Se insertó el usuario correctamente")

        # except Exception as a:
        #     print(f"Error: {a}")


def mostrar_datos(pantalla):
    conexion = sqlite3.connect("Usuarios.db")
    cursor = conexion.cursor()

    # Realizar la consulta a la base de datos
    cursor.execute("SELECT Nombre, score FROM usuario")
    datos = cursor.fetchall()

    posicion_y = 100
    for dato in datos:
        nombre = dato[0]
        score = dato[1]
        crear_texto(
            pantalla,
            f"Nombre: {nombre}, Score: {score}",
            (100, posicion_y),
            (255, 255, 255),
            20,
        )
        posicion_y += 30

    conexion.close()


def crear_texto(pantalla, texto, posicion, color, tamaño):
    Formato = pygame.font.Font(None, tamaño)
    texto = Formato.render(texto, True, color)
    pantalla.blit(texto, posicion)
