import pygame as pg
import variables as var
import funciones as fun
import boton 
pg.init()
pg.mixer.init()

def juego(pantalla,pantalla_actual): 
    pg.display.set_caption("DRAGON BALL CARD GAME - JUEGO")
    pantalla.blit(var.FONDO_BATALLA,(0,0))
    fun.draw_text("JUEGO",var.fuente_titulo,var.TEXT_COLOR_BLANCO,285,100,pantalla)        
    boton_volver = boton.botonazo("VOLVER",650,500,pantalla,var.fuente,150,25)

    if boton_volver.collidepoint(pg.mouse.get_pos()) and pg.mouse.get_pressed()[0]:
        var.EFECTO_BOTONES.play()
        print("VOLVER")
        pg.time.delay(300)
        pantalla_actual = "menu"
    return pantalla_actual