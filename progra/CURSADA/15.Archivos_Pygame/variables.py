import pygame as pg

TITULO_JUEGO = "PYTHONISA DEL TAROT"
DIMESION_PANTALLA = (1280, 720)

FPS = 30
CANT_VIDAS = 3

DIMENSION_BOTON = (250, 60)

BOTON_JUGAR = 0
BOTON_AJUSTE = 1
BOTON_HISTORIA = 2
BOTON_SALIR = 3

 
COLOR_BLANCO = (255,255,255) 

RUTA_FONDO = './assets/background/fondo_tablero.png'
fondo = pg.image.load(RUTA_FONDO)
