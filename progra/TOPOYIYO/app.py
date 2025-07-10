import pygame as pg
import variables as var
import main_menu as menu
import main_ranking as ranking
import main_juego as game
import main_ajustes as ajustes
pg.init()

#####COFIGURACIONES#####
corriendo = True
pantalla = pg.display.set_mode(var.SCREEN)
pantalla_actual = "menu"
clocky = pg.time.Clock()
pg.display.set_icon(var.ICON)
#####COFIGURACIONES##### 

while corriendo:
    
    fps = clocky.tick(60) 

    cola_de_eventos = pg.event.get()
    
    match pantalla_actual:
        case "menu":
            pantalla_actual = menu.pantalla_menu(pantalla,pantalla_actual,cola_de_eventos)
        case "juego":
            pantalla_actual = game.pantalla_juego(pantalla,pantalla_actual,cola_de_eventos)
        case "ranking":
            pantalla_actual = ranking.pantalla_ranking(pantalla,pantalla_actual,cola_de_eventos)
        case "ajustes":
            pantalla_actual = ajustes.pantalla_ajustes(pantalla,pantalla_actual,cola_de_eventos)
        case "salir":
            corriendo = False
           

    pg.display.flip()
                
pg.quit() 