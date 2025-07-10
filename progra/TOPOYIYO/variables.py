import pygame as pg
pg.init()
pg.mixer.init()

#####CAPTION##### 
CAPTION_MENU = "DRAGON BALL CARD GAME - MAIN MENU"
CAPTION_JUEGO = "DRAGON BALL CARD GAME - JUEGO"
CAPTION_RANKING = "DRAGON BALL CARD GAME - AJUSTES"

#####FONDOS#####
FONDO_MENU = pg.image.load("./progra/TOPOYIYO/assetss/fondos/kame_house_2.jpg")
FONDO_BATALLA = pg.image.load("./progra/TOPOYIYO/assetss/fondos/cell_games.jpeg")
FONDO_RANKING = pg.image.load("./progra/TOPOYIYO/assetss/fondos/kaio.jpeg") 
FONDO_AJUSTES = pg.image.load("./progra/TOPOYIYO/assetss/fondos/kaio.jpeg")

#####PANTALLA#####
SCREEN = (1600, 900)
ICON = pg.image.load("./progra/TOPOYIYO/assetss/icons/star_4.png")

#####IMGs#####
TITULO_IMG = pg.image.load("./progra/TOPOYIYO/assetss/icons/dbz_titulo.png")
JUGADOR_SCOUTER = pg.image.load("./progra/TOPOYIYO/assetss/jugadores/scouter_jugador.png")
ENMIGO_SCOUTER = pg.image.load("./progra/TOPOYIYO/assetss/jugadores/scouter_enemigo.png")
CARTA = pg.image.load("./progra/TOPOYIYO/assetss/cartas/1.0_HP_6500_ATK_13000_DEF_7000_10.png")
CARTA_TRASERA = pg.image.load("./progra/TOPOYIYO/assetss/cartas/reverse.png")

#####FUENTE#####
FUENTE_TITULO = pg.font.Font("./progra/TOPOYIYO/assetss/alagard.ttf", 65)
FUENTE = pg.font.Font("./progra/TOPOYIYO/assetss/alagard.ttf", 25)

#####COLORES#####
COLOR_BLANCO = (255,255,255)
COLOR_VIOLETA = (76,40,130)
COLOR_BORDO = (179,32,0)
COLOR_NARANJA = (236,129,19)
COLOR_AMARILLO = (248,255,111)

#####CANCIONES - SONIDOS#####
EFECTO_BOTONES = pg.mixer.Sound("./progra/TOPOYIYO/assetss/sonido/radar_sound.mp3")
MUSICA_PELEA = "./progra/TOPOYIYO/assetss/sonido/DBZ_OP_8_bits.wav"
MUSICA_DE_FONDO = "./progra/TOPOYIYO/assetss/sonido/DBZ_OP_8_bits.wav"

#####BOTONES#####
BTN_JUGAR = pg.image.load("./progra/TOPOYIYO/assetss/botones/btn_start.png")
BTN_RANKING = pg.image.load("./progra/TOPOYIYO/assetss/botones/btn_ranking.png")
BTN_CONFIGURACIONES = pg.image.load("./progra/TOPOYIYO/assetss/botones/btn_settings.png")
BTN_ATRAS = pg.image.load("./progra/TOPOYIYO/assetss/botones/btn_back.png")
BTN_SALIR = pg.image.load("./progra/TOPOYIYO/assetss/botones/btn_quit.png")
BTN_SHIELD = pg.image.load("./progra/TOPOYIYO/assetss/botones/btn_shield.png")
BTN_HEAL = pg.image.load("./progra/TOPOYIYO/assetss/botones/btn_heal.png")
