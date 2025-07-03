import pygame as pg
import variables as var
import sys
import forms.form_manager as form_manager
 

def pythonisa():
    
    pg.init()
    pg.display.set_caption("PRIMER JUEGUBI")
    pantalla = pg.display.set_mode(var.PANTALLA)
    corriendo = True
    reloj = pg.time.Clock()
    datos_juego = {
        "puntaje" : 0,
        "cant_vidas" : var.CANT_VIDAS,
        "nombre" : "Player",
        "volumen_musica" : 100,
        "tiempo_finalizado" : None
    }
    
    forms = form_manager.create_form_manager(pantalla, datos_juego)
    
    while corriendo:
        
        event_list = pg.event.get()
        
        for event in event_list:
            if event.type == pg.QUIT:
                corriendo = False
                
        pg.display.flip() #actualiza toda la pantalla - update actualiza toda o algo en especifico
                
                
    pg.quit
    sys.exit()