import pygame as pg

def draw_text(texto : str, fuente : any, color : any, posicion_x : int, posicion_y : int, pantalla : str):
    """Muestra texto ingresado por parametro en pantalla

    Args:
        texto (str): Texto a mostrar
        fuente (any): Fuente del texto
        color (any): Color del texto
        posicion_x (int): Posición X
        posicion_y (int): Posición Y
        pantalla (str): Surface
    """
    text = fuente.render(texto,True, color)
    pantalla.blit(text,(posicion_x,posicion_y))
    
def centrar_img_eje_x(resolucion_x_pantalla : int, resolucion_x_img : int, ) -> int:
    eje_x = (resolucion_x_pantalla / 2) - (resolucion_x_img / 2)
    return eje_x
    
     