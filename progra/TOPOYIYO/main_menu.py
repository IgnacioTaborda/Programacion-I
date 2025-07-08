import pygame as pg
import variables as var
import funciones as fun
import boton 
pg.init()
pg.mixer.init()

def menu(pantalla,pantalla_actual): 
    pantalla.blit(var.FONDO_MENU,(0,0))
    pantalla.blit(var.TITULO_IMG,(fun.centrar_img_eje_x(var.SCREEN[0],400),25))
    pg.display.set_caption(var.TITULO)
    
    boton_jugar = boton.botonazo("JUGAR",350,250,pantalla,var.fuente,150,25)
    boton_ajustes = boton.botonazo("AJUSTES",350,325,pantalla,var.fuente,150,25)
    boton_salir = boton.botonazo("SALIR",350,400,pantalla,var.fuente,150,25)
    
    if boton_salir.collidepoint(pg.mouse.get_pos()) and pg.mouse.get_pressed()[0]:
        var.EFECTO_BOTONES.play()
        #pg.display.flip()
        pg.time.delay(300)
        pantalla_actual = "salir" 

    elif boton_jugar.collidepoint(pg.mouse.get_pos()) and pg.mouse.get_pressed()[0]:
        var.EFECTO_BOTONES.play()
        print("ESTAS JUGANDO")
        pantalla_actual = "juego"
            
    elif boton_ajustes.collidepoint(pg.mouse.get_pos()) and pg.mouse.get_pressed()[0]:
        var.EFECTO_BOTONES.play()
        print("ESTAS EN LOS AJUSTES")
        pg.time.delay(300)
        pantalla_actual = "ajustes"
            
    fun.draw_text("HECHO POR: IGNACIO TABORDA - DIV 315",var.fuente,var.TEXT_COLOR_BLANCO,200,500,pantalla)
    return pantalla_actual