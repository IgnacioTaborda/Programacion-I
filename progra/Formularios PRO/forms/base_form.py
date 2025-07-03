import pygame as pg

def create_base_form(name : str, pantalla : pg.Surface, active : bool, coords: tuple, level_num : int, music_path : str) -> dict:
    """A la hora de crear los formularios todos van a pedir estos datos, así que creamos esta función
    para evitar hardear siempre lo mismo

    Args:
        name (str): nombre del formulario (menu,juego,etc)
        pantalla (pg.Surface): 
        active (bool): si esta activo (True) lo mostramos en la pantalla
        coords (tuple): en donde vamos a dibujar el formulario
        level_num (int): 
        music_path (str): 

    Returns:
        dict: Retorna un diccionario con toda la data
    """
    form = {}
    form['screen'] = pantalla
    form['active'] = active
    form['x_coord'] = coords[0]
    form['y_coord'] = coords[1]
    form['level_number'] = level_num
    form['music_path'] = music_path
    return form
    
def draw(form_data : dict):
    form_data["screen"].blit(form_data.get("surface"))