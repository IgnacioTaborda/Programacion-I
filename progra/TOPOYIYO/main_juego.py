import pygame as pg
import variables as var
import funciones as fun
import boton 
pg.init()
pg.mixer.init()

#####COFIGURACIONES#####
pg.mixer_music.load(var.MUSICA_PELEA)
pg.mixer.music.play(-1)
pg.mixer.music.set_volume(0.2)
pg.display.set_caption(var.CAPTION_JUEGO)
#####COFIGURACIONES##### 


def pantalla_juego(pantalla,pantalla_actual,cola_de_eventos): 
    
    for evento in cola_de_eventos:    
        if evento.type == pg.QUIT:
            pantalla_actual = "salir"
        if evento.type == pg.KEYDOWN:
            match evento.type:
                case K_esc:
                    pantalla_actual = "salir"
            
    #PANTALLA
    pantalla.blit(var.FONDO_BATALLA,(0,0))
    fun.draw_text("JUEGO",var.FUENTE_TITULO,var.COLOR_BLANCO,675,75,pantalla)
    
    #JUGADOR
    pantalla.blit(var.JUGADOR_SCOUTER,((50,625)))
    fun.draw_text("Player",var.FUENTE_TITULO,var.COLOR_AMARILLO,275,645,pantalla)
    
    #CARTAS - JUGADOR
    carta = fun.reducir_tamano_img(var.CARTA,85)
    pantalla.blit(carta,(20,90))
    carta_trasera = fun.reducir_tamano_img(var.CARTA_TRASERA,85)
    pantalla.blit(carta_trasera,(340,90))
    
    #ENEMIGO
    pantalla.blit(var.ENMIGO_SCOUTER,((1075,625)))
    fun.draw_text("Enemy",var.FUENTE_TITULO,var.COLOR_AMARILLO,1115,645,pantalla)
            
    #CARTAS - ENEMIGO
    carta = fun.reducir_tamano_img(var.CARTA,85)
    pantalla.blit(carta,(945,90))
    carta_trasera = fun.reducir_tamano_img(var.CARTA_TRASERA,85)
    pantalla.blit(carta_trasera,(1265,90))
    
    #BOTONES
    boton_jugar = boton.boton_img(var.BTN_JUGAR,700,650,pantalla)
    boton_shield = boton.boton_img(var.BTN_SHIELD,700,700,pantalla)
    boton_heal = boton.boton_img(var.BTN_HEAL,700,750,pantalla)
       
    #ACCIONES - BOTONES
    if pg.mouse.get_pressed()[0]:
        if boton_jugar.collidepoint(pg.mouse.get_pos()):
            print("JUGAR")
            var.EFECTO_BOTONES.play()   
            
        elif boton_shield.collidepoint(pg.mouse.get_pos()):
            var.EFECTO_BOTONES.play()  
            print("SHIELD")      
            
        elif boton_heal.collidepoint(pg.mouse.get_pos()):
            var.EFECTO_BOTONES.play()
            print("HEALS")
        pg.time.delay(300)
    
    return pantalla_actual