import pygame as pg
import forms.base_form as base_form
from utn_fra.pygame_widgets import (
    Button, Label
)
import variables as var



def init_form_main_menu(name : str, pantalla : pg.Surface, active : bool, coords: tuple, level_num : int, music_path : str):
    form = base_form.create_base_form(name,pantalla,active,coords,level_num,music_path)
    
    form["surface"] = pg.image.load("./Formularios PRO/background/fondo_4.png")
    form["surface"] = pg.transform.scale(form.get("surface"),var.PANTALLA)
    
    form["rect"] = form.get("surface").get_rect()
    form["rect"].x = coords[0]
    form["rect"].y = coords[1]
    
    form["btn_jugar"] = Button(x=var.PANTALLA(0)//2, y=275, text="JUGAR", screen= form.get("patalla"), font_path=var.FUENTE_ALAGARD, font_size=30, on_click=None,on_click_param=None) #o screen
    form["btn_historia"] = Button(x=var.PANTALLA(0)//2, y=115, text="HISTORIA", screen= form.get("patalla"), font_path=var.FUENTE_ALAGARD, font_size=30, on_click=None,on_click_param=None) #o screen
    form["btn_salir"] = Button(x=var.PANTALLA(0)//2, y=355, text="SALIR", screen= form.get("patalla"), font_path=var.FUENTE_ALAGARD, font_size=30, on_click=None,on_click_param=None) #o screen
    
    form['widgets_list'] = [
        form.get('lbl_titulo'), form.get('btn_jugar'), form.get('btn_ranking'),form.get('btn_historia'), form.get('btn_salir')
    ]
    #LOS WIDGETS QUE VAMOS A DIBUJAR
    
    return form

def draw(form_data : dict):
    base_form.draw(form_data)
    
    for widget in form_data.get('widgets_list'):
        widget.draw()
        
def update_widgets(form_data: dict):
    for widget in form_data.get('widgets_list'):
        widget.update()