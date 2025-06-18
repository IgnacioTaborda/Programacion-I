import pygame as pg
import variables as var
import forms.menu as menu

def pythonisa():
    
    pg.display.set_caption(var.TITULO_JUEGO) #Titulo del juego q se ve arriba de todo
    pantalla = pg.display.set_mode(var.DIMESION_PANTALLA) #Tamaño de pantalla
    corriendo = True
    reloj = pg.time.Clock()  #FPS
    form_actual = "menu"
    bandera_juego = False
    datos_juego = {
        "puntuacion" : 0,
        "cantidad_vidas" : var.CANT_VIDAS,
        "nombre" : "",
        "volumen_musica" : 100
        
    }
    
    while corriendo:
        
        cola_Eventos = pg.event.get()
        reloj.tick(var.FPS) #ESTABLECER FPS
        
        if form_actual == "menu":
            form_actual = menu.mostrar_menu(pantalla,cola_Eventos) #HAY QUE USAR LA PANTALLA EN TODOS LADOS
        elif form_actual == "salir":
            corriendo = False    
            
            
            
            
            
            
            