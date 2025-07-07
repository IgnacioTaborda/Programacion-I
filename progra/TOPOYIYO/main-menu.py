import pygame as pg
import variables as var
import funciones as fun
import botonazo
pg.init()
pg.mixer.init()

#####COFIGURACIONES#####
pg.display.set_caption(var.TITULO)
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
        if (event.type == pg.QUIT):
            corriendo = False 
    
    if pantalla_actual == "menu":
        pantalla.blit(var.FONDO_MENU,(0,0))
        pantalla.blit(var.TITULO_IMG,(fun.centrar_img_eje_x(var.SCREEN[0],400),25))
        
        boton_jugar = botonazo.botonazo("JUGAR",350,250,pantalla,var.fuente,150,25)
        boton_ajustes = botonazo.botonazo("AJUSTES",350,325,pantalla,var.fuente,150,25)
        boton_salir = botonazo.botonazo("SALIR",350,400,pantalla,var.fuente,150,25)
        
        if boton_salir.collidepoint(pg.mouse.get_pos()) and pg.mouse.get_pressed()[0]:
                var.EFECTO_BOTONES.play()
                #pg.display.flip()
                pg.time.delay(300)
                corriendo = False 

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
    
    elif pantalla_actual == "ajustes":
        pantalla.fill(var.TEXT_COLOR_BLANCO)
        #pantalla.blit(var.FONDO_IMG,(0,0))
        fun.draw_text("AJUSTES",var.fuente_titulo,(0,0,0),285,100,pantalla)        
        boton_volver = botonazo.botonazo("VOLVER",650,500,pantalla,var.fuente,150,25)

        if boton_volver.collidepoint(pg.mouse.get_pos()) and pg.mouse.get_pressed()[0]:
            var.EFECTO_BOTONES.play()
            print("VOLVER")
            pg.time.delay(300)
            pantalla_actual = "menu"
        
         
    elif pantalla_actual == "juego":
        pantalla.fill(var.TEXT_COLOR_VIOLETA)
        fun.draw_text("JUEGO",var.fuente_titulo,var.TEXT_COLOR_BLANCO,285,100,pantalla)        
        boton_volver = botonazo.botonazo("VOLVER",650,500,pantalla,var.fuente,150,25)

        if boton_volver.collidepoint(pg.mouse.get_pos()) and pg.mouse.get_pressed()[0]:
            var.EFECTO_BOTONES.play()
            print("VOLVER")
            pg.time.delay(300)
            pantalla_actual = "menu"

    pg.display.flip()
                
pg.quit() 