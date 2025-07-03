import pygame as pg

def crear_lista_botones(cantidad: int, dimension: tuple, color: str = "purple"):
    lista_botones = []
    for i in range(cantidad):
        boton = {}
        boton["superficie"] = pg.Surface(dimension)
        boton["rectangulo"] = boton.get("superficie").get_rect() #conseguimos la superficie de arriba
        boton["superficie"].fill(pg.Color(color))
        lista_botones.append(boton)
    return lista_botones


def mostrar_texto(surface: pg.Surface, texto: str, pos: tuple, font, color = pg.Color('black')):
    words = []
    
    for word in texto.splitlines():
        words.append(word.split(' '))
    
    space = font.size(' ')[0]
    ancho_max, alto_max = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, False, color)
            ancho_palabra, alto_palabra = word_surface.get_size()
            if x + ancho_palabra >= ancho_max:
                x = pos[0]
                y += alto_palabra
            surface.blit(word_surface, (x, y))
            x += ancho_palabra + space
        x = pos[0]
        y += alto_palabra