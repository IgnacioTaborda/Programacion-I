import pygame as pg
import variables as var
import os

pg.init() #arrancamos 
indice_actual = 0
lista = var.lista_numeros

screen = pg.display.set_mode((var.DIMENSION_PANTALLA))
pg.display.set_caption("Mi py juego Bv") #titulo
clock = pg.time.Clock()

corriendo = True

while corriendo:
    
    eventos_pygame = pg.event.get()
    
    for evento in eventos_pygame:
        if evento.type == pg.QUIT:
            corriendo = False
            
        if evento.type == pg.MOUSEBUTTONDOWN:
            if evento.button == 1 and indice_actual < (len(lista) - 1):
                indice_actual += 1
            else:
                indice_actual = 0
            
    screen.fill(var.COLOR_ROJO)
    
    texto = pg.font.SysFont("Arial", 27)
    texto = texto.render(f"{lista[indice_actual]}", True, var.COLOR_NEGRO)
    
    coordenada = (500,500)
    screen.blit(texto,coordenada)
    
    pg.display.flip()
    clock.tick(var.FPS) #FPS

pg.quit()
