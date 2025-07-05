import pygame as pg
pg.init()

#####MENU#####
TITULO = "TOPOMAX - MAIN MENU"
ICON = pg.image.load("./progra/TOPOYIYO/assetss/Berserk.png")

#####PANTALLA#####
SCREEN = (800,600)
fuente_titulo = pg.font.SysFont("arialblack", 45)
fuente = pg.font.SysFont("arialblack", 15)

#####COLORES#####
TEXT_COLOR_BLANCO = (255,255,255)

#####BOTONES#####
BTN_JUGAR = pg.image.load("./progra/TOPOYIYO/assetss/btn_jugar.png")
BTN_RANKING = pg.image.load("./progra/TOPOYIYO/assetss/btn_ranking.png")
BTN_SALIR = pg.image.load("./progra/TOPOYIYO/assetss/btn_salir.png")