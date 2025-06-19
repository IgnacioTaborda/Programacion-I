import pygame as pg
import variables as var
import forms.menu as menu

def pythonisa(): 
    
    pg.display.set_caption(var.TITULO_JUEGO) #Titulo del juego q se ve arriba de todo
    pantalla = pg.display.set_mode(var.DIMESION_PANTALLA) #Tamaño de pantalla
    corriendo = True
    reloj = pg.time.Clock()  #FPS
    form_actual = "menu" #Donde inicia el juego, osea, en el menú
    bandera_juego = False #PARA SABER SI YA ESTAMOS JUGANDO
    datos_juego = {
        "puntuacion" : 0,
        "cantidad_vidas" : var.CANT_VIDAS,
        "nombre" : "",
        "volumen_musica" : 100
        
    }
     
    while corriendo:
        
        cola_eventos = pg.event.get() #Nos traemos todos los eventos que estan ocurriendo en el momento
        reloj.tick(var.FPS) #ESTABLECER FPS
        
        if form_actual == "menu":
            form_actual = menu.mostrar_menu(pantalla,cola_eventos) #HAY QUE USAR LA PANTALLA EN TODOS LADOS
        elif form_actual == "salir":
            corriendo = False    
            
            
            
            
            
            
            