# def botonazo(texto : str, posicion_x : int, posicion_y : int, pantalla : str, fuente : str, ancho_boton : int, alto_boton : int):
#     """Esta función se encarga de crear un botón rectangulo de color gris que contenga un texto

#     Args:
#         texto (str): Texto que va a tener el botón
#         posicion_x (int): Posición X del texto
#         posicion_y (int): Posición Y del texto
#         pantalla (str): Variable que contiene la pantalla
#         fuente (str): Fuente que va a tener el texto
#         ancho_boton (int): Ancho del botón
#         alto_boton (int): Alto del botón
#     """
#     boton = {}
#     boton["texto"] = texto
#     boton["posicion_x"] = posicion_x
#     boton["posicion_y"] = posicion_y
#     boton["fuente"] = fuente
#     boton["ancho_boton"] = ancho_boton
#     boton["alto_boton"] = alto_boton
#     boton["pantalla"] = pantalla
    
#     boton_rectangulo = pg.rect.Rect(boton.get("posicion_x") - 40, boton.get("posicion_y"), boton.get("ancho_boton"),boton.get("alto_boton"))
    
#     mouse_pos = pg.mouse.get_pos()
#     click_izquierdo = pg.mouse.get_pressed()[0]
    
#     activar_efecto_boton = efecto_click(mouse_pos,click_izquierdo,boton_rectangulo)
    
#     if activar_efecto_boton == True:
#         pg.draw.rect(boton.get("pantalla"), "dark gray", boton_rectangulo,0,5)
#     else:
#         pg.draw.rect(boton.get("pantalla"), "gray", boton_rectangulo,0,5)       
#     pg.draw.rect(boton.get("pantalla"), "black", boton_rectangulo,2,5)
    
#     fun.draw_text(boton.get("texto"),boton.get("fuente"),"black",boton.get("posicion_x"),boton.get("posicion_y"),boton.get("pantalla"))
    
#     return boton_rectangulo

#TITULO
#fun.draw_text("EL SALTO DO PAPU",var.fuente_titulo,var.TEXT_COLOR_BLANCO,160,150,pantalla)

