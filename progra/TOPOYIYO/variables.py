import pygame as pg
pg.init()
pg.mixer.init()

#####MENU##### 
TITULO = "DRAGON BALL CARD GAME - MAIN MENU"
ICON = pg.image.load("./progra/TOPOYIYO/assetss/star_4.png")
MUSICA_MENU = "./progra/TOPOYIYO/assetss/DBZ_OP_8_bits.wav"

#####PANTALLA#####
SCREEN = (800,600)
TITULO_IMG = pg.image.load("./progra/TOPOYIYO/assetss/dbz_titulo.png")
FONDO_IMG = pg.image.load("./progra/TOPOYIYO/assetss/kame_house.jpg")
fuente_titulo = pg.font.SysFont("arialblack", 45)
fuente = pg.font.SysFont("arialblack", 15)

#####COLORES#####
TEXT_COLOR_BLANCO = (255,255,255)
TEXT_COLOR_VIOLETA = (76,40,130)

#####BOTONES#####
BTN_JUGAR = pg.image.load("./progra/TOPOYIYO/assetss/btn_jugar.png")
BTN_RANKING = pg.image.load("./progra/TOPOYIYO/assetss/btn_ranking.png")
BTN_SALIR = pg.image.load("./progra/TOPOYIYO/assetss/btn_salir.png")

#####SONIDOS#####
#MUSICA_MAIN_MENU = pg.mixer_music.load("./progra/TOPOYIYO/assetss/DBZ_OP_8_bits.mp3")
EFECTO_BOTONES = pg.mixer.Sound("./progra/TOPOYIYO/assetss/radar_sound.mp3")