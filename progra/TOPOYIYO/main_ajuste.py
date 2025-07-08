import pygame as pg
import variables as var
import funciones as fun
import boton 
pg.init()
pg.mixer.init()

def ajustes(pantalla,pantalla_actual): 
    pg.display.set_caption("DRAGON BALL CARD GAME - AJUSTES")
    pantalla.blit(var.FONDO_AJUSTE,(0,0))
    #pantalla.blit(var.FONDO_IMG,(0,0))
    fun.draw_text("AJUSTES",var.fuente_titulo,(0,0,0),285,100,pantalla)        
    boton_volver = boton.botonazo("VOLVER",650,500,pantalla,var.fuente,150,25)

    if boton_volver.collidepoint(pg.mouse.get_pos()) and pg.mouse.get_pressed()[0]:
        var.EFECTO_BOTONES.play()
        print("VOLVER")
        pg.time.delay(300)
        pantalla_actual = "menu"
    return pantalla_actual