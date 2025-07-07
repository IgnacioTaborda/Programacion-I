import pygame as pg
pg.init()
pg.mixer.init()

#####MENU##### 
TITULO = "DRAGON BALL CARD GAME - MAIN MENU"
ICON = pg.image.load("./progra/TOPOYIYO/assetss/icons/star_4.png")
MUSICA_MENU = "./progra/TOPOYIYO/assetss/sonido/DBZ_OP_8_bits.wav"

#####PANTALLAS#####
SCREEN = (800,600)
TITULO_IMG = pg.image.load("./progra/TOPOYIYO/assetss/icons/dbz_titulo.png")
FONDO_MENU = pg.image.load("./progra/TOPOYIYO/assetss/fondos/kame_house.jpg")
FONDO_AJUSTE = pg.image.load("./progra/TOPOYIYO/assetss/fondos/namek.jpg")
fuente_titulo = pg.font.SysFont("arialblack", 45)
fuente = pg.font.SysFont("arialblack", 15)

#####COLORES#####
TEXT_COLOR_BLANCO = (255,255,255)
TEXT_COLOR_VIOLETA = (76,40,130)

#####SONIDOS#####
EFECTO_BOTONES = pg.mixer.Sound("./progra/TOPOYIYO/assetss/sonido/radar_sound.mp3")