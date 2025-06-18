import pygame as pg
import variables as var
import auxiliares as aux

lista_botones = aux.crear_lista_botones(4,var.DIMENSION_BOTON,"purple")

def mostrar_menu(pantalla : pg.Surface, cola_eventos : list[pg.event.Event]) -> str:
    retorno = "menu"    
    pg.display.set_caption("MENU")
    
    for evento in cola_eventos:
        if evento.type == pg.QUIT:
            retorno = "salir"
        elif evento.type == pg.MOUSEBUTTONDOWN:
            if lista_botones[var.BOTON_JUGAR]['rectangulo'].collidepoint(evento.pos):
                retorno = "juego"
            elif lista_botones[var.BOTON_AJUSTE]['rectangulo'].collidepoint(evento.pos):
                retorno = "configuracion"
            elif lista_botones[var.BOTON_HISTORIA]['rectangulo'].collidepoint(evento.pos):
                retorno = "historia"
            elif lista_botones[var.BOTON_SALIR]['rectangulo'].collidepoint(evento.pos):
                retorno = "salir"
                
    pantalla.fill()