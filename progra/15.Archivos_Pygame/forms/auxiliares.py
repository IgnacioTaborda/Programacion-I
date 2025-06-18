import pygame as pg

def crear_lista_botones(cantidad: int, dimension: tuple, color: str = "purple"):
    lista_botones = []
    for i in range(cantidad):
        boton = {}
        boton["superficie"] = pg.Surface(dimension)
        boton["rectangulo"] = boton.get("superficie").get_rect()
        boton["superficie"].fill(pg.Color(color))
        lista_botones.append(boton)
    return boton