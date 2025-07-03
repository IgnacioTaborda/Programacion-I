import pygame as pg

def draw_text(texto : str, fuente : str, text_color : str, x : int, y : int, pantalla : str):
    """Muestra texto en pantallas

    Args:
        texto (str): _description_
        fuente (str): _description_
        text_color (str): _description_
        x (int): _description_
        y (int): _description_
        pantalla (str): _description_
    """
    text = fuente.render(texto,True, text_color)
    pantalla.blit(text,(x,y))