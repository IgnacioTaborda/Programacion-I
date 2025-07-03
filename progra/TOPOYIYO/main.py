import pygame as pg
import variables as var
import funciones as fun
pg.init()

#####COFIGURACIONES#####
pg.display.set_caption(var.TITULO)
pg.display.set_icon(var.ICON)
surface = pg.display.set_mode(var.SCREEN)
corriendo = True
clocky = pg.time.Clock()

while corriendo:
    
    surface.fill((76,40,130))
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            corriendo = False
            
    fps = clocky.tick(60)
            
    
    fun.draw_text("EL SALTO DO PAPU",var.fuente_titulo,var.TEXT_COLOR,160,150,surface)
    fun.draw_text("JUGAR",var.fuente,var.TEXT_COLOR,350,250,surface)
    fun.draw_text("SALIR",var.fuente,var.TEXT_COLOR,350,315,surface)
    pg.display.flip()
                
pg.quit()