import pygame as pg
import variables as var
import funciones as fun
import boton 
import main_menu as menu
import main_ajuste as ajustes
import main_juego as game
pg.init()
pg.mixer.init()

#####COFIGURACIONES#####
pg.display.set_icon(var.ICON)
pg.mixer_music.load(var.MUSICA_MENU)
pantalla = pg.display.set_mode(var.SCREEN)
corriendo = True
clocky = pg.time.Clock()
pg.mixer.music.play(-1)
pg.mixer.music.set_volume(0.2)
pantalla_actual = "menu"
#####COFIGURACIONES##### 

while corriendo:
    
    fps = clocky.tick(60)

    for event in pg.event.get():
        if (event.type == pg.QUIT) or pantalla_actual == "salir":
            corriendo = False 
    
    if pantalla_actual == "menu":
        q = menu.menu(pantalla,pantalla_actual)
        pantalla_actual = q
    
    elif pantalla_actual == "ajustes":
        x = ajustes.ajustes(pantalla,pantalla_actual)
        pantalla_actual = x     
         
    elif pantalla_actual == "juego":
        y = game.juego(pantalla,pantalla_actual)
        pantalla_actual = y

    pg.display.flip()
                
pg.quit() 