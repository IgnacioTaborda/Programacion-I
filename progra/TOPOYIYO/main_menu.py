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
pg.display.set_caption(var.CAPTION_MENU)
#####COFIGURACIONES##### 

def pantalla_menu(pantalla,pantalla_actual,cola_de_eventos): 
    
    for evento in cola_de_eventos:    
        if evento.type == pg.QUIT:
            pantalla_actual = "salir"
    
    #PANTALLA
    pantalla.blit(var.FONDO_MENU,(0,0))
    pantalla.blit(var.TITULO_IMG,(600,100))
    
    #BOTONES
    boton_jugar = boton.boton_img(var.BTN_JUGAR,700,425,pantalla)
    boton_ranking = boton.boton_img(var.BTN_RANKING,700,500,pantalla)
    boton_ajustes = boton.boton_img(var.BTN_CONFIGURACIONES,700,575,pantalla)
    boton_salir = boton.boton_img(var.BTN_SALIR,700,650,pantalla)
       
    #ACCIONES - BOTONES
    if pg.mouse.get_pressed()[0]:
        if boton_jugar.collidepoint(pg.mouse.get_pos()):
            var.EFECTO_BOTONES.play()
            pantalla_actual = "juego"
            
        elif boton_ranking.collidepoint(pg.mouse.get_pos()):
            var.EFECTO_BOTONES.play()
            pantalla_actual = "ranking"
            
        elif boton_ajustes.collidepoint(pg.mouse.get_pos()):
            var.EFECTO_BOTONES.play()
            pantalla_actual = "ajustes"
            
        elif boton_salir.collidepoint(pg.mouse.get_pos()):
            var.EFECTO_BOTONES.play()
            pg.time.delay(300)
            pantalla_actual = "salir" 
            
    fun.draw_text("HECHO POR: IGNACIO TABORDA - DIV 315",var.FUENTE,var.COLOR_BORDO,570,800,pantalla)
    return pantalla_actual