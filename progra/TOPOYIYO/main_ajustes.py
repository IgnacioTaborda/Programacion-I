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

def pantalla_ajustes(pantalla,pantalla_actual,cola_de_eventos): 
    
    for evento in cola_de_eventos:    
        if evento.type == pg.QUIT:
            pantalla_actual = "salir"
            
    #PANTALLA
    pantalla.blit(var.FONDO_AJUSTES,(0,0))
    fun.draw_text("SETTINGS",var.FUENTE_TITULO,var.COLOR_BLANCO,675,75,pantalla)  
    
    #BOTON       
    boton_volver = boton.boton_img(var.BTN_ATRAS,1350,800,pantalla)
    boton_activar_musica = boton.boton_img(var.BTN_MUSIC_ON,700,175,pantalla)
    boton_desactivar_musica = boton.boton_img(var.BTN_MUSIC_OFF,700,375,pantalla)

       
    #ACCIONES - BOTONES
    if pg.mouse.get_pressed()[0]:     
        if boton_volver.collidepoint(pg.mouse.get_pos()):
            var.EFECTO_BOTONES.play()
            pantalla_actual = "menu"
            
        elif boton_activar_musica.collidepoint(pg.mouse.get_pos()):
            pg.mixer.music.play(-1)
            var.EFECTO_BOTONES.play()
            
        elif boton_desactivar_musica.collidepoint(pg.mouse.get_pos()):
            pg.mixer.music.pause()
            var.EFECTO_BOTONES.play()
             
        pg.time.delay(100)
    
    return pantalla_actual