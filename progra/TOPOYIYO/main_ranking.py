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
    
    #RANKING
    ranking = fun.leer_csv(var.CSV)
    ranking = fun.ordenar_matriz_descendente_mejorada(ranking,1)
    fun.escribir_csv(var.CSV, ranking)
    eje_y = 180 
    posicion = 0
    for i in range(10):
        eje_y += 30
        posicion += 1
        fun.draw_text(f"{posicion}    {ranking[i][0]}",var.FUENTE,var.COLOR_NEGRO,600,eje_y,pantalla)
        fun.draw_text(f"{ranking[i][1]}",var.FUENTE,var.COLOR_NEGRO,1000,eje_y,pantalla)

    #BOTON       
    boton_volver = boton.boton_img(var.BTN_ATRAS,1350,800,pantalla)

    #ACCIÓN - BOTON
    if boton_volver.collidepoint(pg.mouse.get_pos()) and pg.mouse.get_pressed()[0]:
        var.EFECTO_BOTONES.play()
        pg.time.delay(300) 
        pantalla_actual = "menu"
    
    return pantalla_actual