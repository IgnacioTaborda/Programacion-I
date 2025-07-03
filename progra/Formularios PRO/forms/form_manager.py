import pygame as pg

def create_form_manager(pantalla : pg.Surface, datos_juego : list[dict]) -> list[dict]:
    """Administrador de formularios que se va a encargar de adm a todos (menu,juego,opciones),


    Args:
        pantalla (pg.Surface): Pantalla en la que se van a dibujar los forms
        datos_juego (list[dict]): Datos del juego

    Returns:
        list[dict]: Retorna un diccionario
    """
    form = {}
    form['main_screen'] = pantalla
    form['current_level'] = 1
    form['game_started'] = False
    form['player'] = None
    form['enemy'] = None
    
    form['form_list'] = [
        #TODAS LAS PANTALLAS QUE VA A TENER EL JUEGO
    ]
    
    return form