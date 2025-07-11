import pygame as pg

def draw_text(texto : str, fuente : any, color : any, posicion_x : int, posicion_y : int, pantalla : str):
    """Muestra el texto ingresado por parametro en pantalla

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
    
def centrar_img_eje_x(ancho_pantalla : int, ancho_img : int) -> int:
    """Esta función se encarga de poner en el centro de la pantalla una imagen

    Args:
        ancho_pantalla (int): Ancho de la pantalla 
        ancho_img (int): Ancho de la imagen

    Returns:
        int: Retortna en que posición del eje "X" se tiene que encontrar
        la imagen para estar en el medio de la pantalla.
    """
    eje_x = (ancho_pantalla / 2) - (ancho_img / 2)
    return eje_x
    
def leer_csv(archivo : str) -> list[list]:
    """Recibe un archivo csv por parametro y retorna una matriz que 
    contiene cada renglon en una lista. 

    Args:
        archivo (str): Ruta del archivo csv

    Returns:
        list[list]: Retona una matriz en la que cada lista es un
        renglon y parsea el 2do elemento a un número entero
    """
    ranking = []
    with open(file=archivo, mode="r", encoding="utf-8") as archivo:
        for i in archivo.readlines():
            renglon = i.replace("\n","")
            separador = ","
            lista = renglon.split(separador)
            lista[1] = int(lista[1])
            ranking.append(lista)  
    return ranking
    
def reducir_tamano_img(imagen : str, reduccion : int):
    alto = int(imagen.get_height() * float(f'0.{reduccion}'))
    ancho = int(imagen.get_width() * float(f'0.{reduccion}'))
    imagen_reducida = pg.transform.scale(imagen, (ancho, alto))
    return imagen_reducida

def ordenar_matriz_descendente(matriz : list[list], columna : int):
    largo_lista = len(matriz)

    for i in range(largo_lista-1):
        
        for j in range(i+1,largo_lista):
            if matriz[i][columna] < matriz[j][columna]:
                aux = matriz[i]
                matriz[i] = matriz[j]
                matriz[j] = aux

    return matriz
            