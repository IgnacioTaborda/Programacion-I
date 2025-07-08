import pygame as pg
import funciones as fun
import variables as var


def determinar_si_fue_clickeada(mouse_pos : tuple, tecla : tuple, objeto : any) -> bool:
    """Al hacer click en el objeto, con la tecla ingresada por parametro, la función retorna
    True.

    Args:
        mouse_pos (tuple): Posición del mouse
        tecla (tuple): Tecla con la que se hace click
        boton_rectangulo (any): Objeto en el que se hace click (Imagen, texto, etc.)

    Returns:
        bool: En caso de hacer click en el objeto ingresado, se retorna True
    """
    if tecla and objeto.collidepoint(mouse_pos):
        return True

def botonazo(texto : str, posicion_x : int, posicion_y : int, pantalla : str, fuente : str, ancho_boton : int, alto_boton : int) -> object:
    """Esta función se encarga de crear un objeto rectangulo que cumple la función de un botón. De ancho_boton x alto_boton, 
    con un borde y texto de color rojo, y un fondo de color naranja. En el centro se va a dibujar el texto ingresado por parametro.
    

    Args:
        texto (str): Texto que va a tener el botón
        posicion_x (int): Posición X del texto
        posicion_y (int): Posición Y del texto
        pantalla (str): Variable que contiene la pantalla
        fuente (str): Fuente que va a tener el texto
        ancho_boton (int): Ancho del botón
        alto_boton (int): Alto del botón
        
    Returns:
        object: Retortna en que posición del eje "X" se tiene que encontrar
        la imagen para estar en el medio de la pantalla.
    """
    boton = {}
    boton["texto"] = texto
    boton["posicion_x"] = posicion_x
    boton["posicion_y"] = posicion_y
    boton["fuente"] = fuente
    boton["ancho_boton"] = ancho_boton
    boton["alto_boton"] = alto_boton
    boton["pantalla"] = pantalla

    boton_rectangulo = pg.rect.Rect(boton.get("posicion_x") - 40, boton.get("posicion_y"), boton.get("ancho_boton"),boton.get("alto_boton"))
    
    pg.draw.rect(boton.get("pantalla"), "orange", boton_rectangulo,0,5)       
    pg.draw.rect(boton.get("pantalla"), "red", boton_rectangulo,2,5)

    fun.draw_text(boton.get("texto"),boton.get("fuente"),"red",boton.get("posicion_x"),boton.get("posicion_y"),boton.get("pantalla"))

    return boton_rectangulo