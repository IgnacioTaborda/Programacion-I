import pygame as pg
import variables as var
import funciones as fun
import boton 
pg.init()
pg.mixer.init()

#####COFIGURACIONES#####
pg.mixer_music.load(var.MUSICA_DE_FONDO)
pg.mixer.music.play(-1)
pg.mixer.music.set_volume(0.2)
pg.display.set_caption(var.CAPTION_RANKING)
#####COFIGURACIONES##### 

def pantalla_ranking(pantalla,pantalla_actual,cola_de_eventos): 
    
    for evento in cola_de_eventos:    
        if evento.type == pg.QUIT:
            pantalla_actual = "salir"
            
    #PANTALLA
    pantalla.blit(var.FONDO_RANKING,(0,0))
    fun.draw_text("RANKING",var.FUENTE_TITULO,var.COLOR_BLANCO,675,75,pantalla)  
    
    #BOTON       
    boton_volver = boton.boton_img(var.BTN_ATRAS,1350,800,pantalla)

    #ACCIÓN - BOTON
    if boton_volver.collidepoint(pg.mouse.get_pos()) and pg.mouse.get_pressed()[0]:
        var.EFECTO_BOTONES.play()
        pg.time.delay(300) 
        pantalla_actual = "menu"
    
    return pantalla_actual