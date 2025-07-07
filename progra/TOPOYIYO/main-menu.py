import pygame as pg
import variables as var
import funciones as fun
import botonazo
pg.init()
pg.mixer.init()

#####COFIGURACIONES#####
pg.display.set_caption(var.TITULO)
pg.display.set_icon(var.ICON)
pg.mixer_music.load("./progra/TOPOYIYO/assetss/DBZ_OP_8_bits.wav")
pantalla = pg.display.set_mode(var.SCREEN)
corriendo = True
clocky = pg.time.Clock()
pg.mixer.music.play(-1)
pg.mixer.music.set_volume(0.2)
#####COFIGURACIONES#####

while corriendo:
    
    pantalla.blit(var.FONDO_IMG,(0,0))
    fps = clocky.tick(60)
    

    pantalla.blit(var.TITULO_IMG,(fun.centrar_img_eje_x(var.SCREEN[0],400),25))
    
    boton_jugar = botonazo.botonazo("JUGAR",350,250,pantalla,var.fuente,150,25)
    boton_ajustes = botonazo.botonazo("AJUSTES",350,325,pantalla,var.fuente,150,25)
    boton_salir = botonazo.botonazo("SALIR",350,400,pantalla,var.fuente,150,25)
    
    for event in pg.event.get():
        if (event.type == pg.QUIT) or (boton_salir.collidepoint(pg.mouse.get_pos()) and pg.mouse.get_pressed()[0]):
            var.EFECTO_BOTONES.play()
            corriendo = False    
            
        elif boton_jugar.collidepoint(pg.mouse.get_pos()) and pg.mouse.get_pressed()[0]:
            var.EFECTO_BOTONES.play()
            print("ESTAS JUGANDO")
            
        elif boton_ajustes.collidepoint(pg.mouse.get_pos()) and pg.mouse.get_pressed()[0]:
            var.EFECTO_BOTONES.play()
            print("ESTAS EN LOS AJUSTES")
            
    fun.draw_text("HECHO POR: IGNACIO TABORDA - DIV 315",var.fuente,var.TEXT_COLOR_BLANCO,200,500,pantalla)
   
    pg.display.flip()
                
pg.quit() 