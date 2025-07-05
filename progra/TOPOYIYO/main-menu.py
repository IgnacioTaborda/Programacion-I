import pygame as pg
import variables as var
import funciones as fun
import botonazo
pg.init()

#####COFIGURACIONES#####
pg.display.set_caption(var.TITULO)
pg.display.set_icon(var.ICON)
pantalla = pg.display.set_mode(var.SCREEN)
corriendo = True
clocky = pg.time.Clock()
#####COFIGURACIONES#####

while corriendo:
    
    pantalla.fill((76,40,130))
    fps = clocky.tick(60)

    fun.draw_text("EL SALTO DO PAPU",var.fuente_titulo,var.TEXT_COLOR_BLANCO,160,150,pantalla)
    
    boton_jugar = botonazo.botonazo("JUGAR",350,250,pantalla,var.fuente,150,25)
    boton_ajustes = botonazo.botonazo("AJUSTES",350,315,pantalla,var.fuente,150,25)
    boton_salir = botonazo.botonazo("SALIR",350,390,pantalla,var.fuente,150,25)
    
    for event in pg.event.get():
        if (event.type == pg.QUIT) or (boton_salir.collidepoint(pg.mouse.get_pos()) and pg.mouse.get_pressed()[0]):
            corriendo = False
            
    
        
    
    pg.display.flip()
                
pg.quit()