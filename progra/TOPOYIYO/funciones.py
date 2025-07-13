import pygame as pg
import json

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
    """Recibe un archivo CSV por parametro y retonar una matriz
    con la informacion

    Args:
        archivo (str): _description_

    Returns:
        list[list]: Retorno el archivo en una matriz, donde
        cada lista representa un renglon.
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
            
def ordenar_matriz_descendente_mejorada(matriz : list[list], columna : int):
    largo_matriz = len(matriz)

    for i in range(largo_matriz - 1):
        indice_elemento_mayor = i

        for j in range(i+1, largo_matriz):
            if matriz[indice_elemento_mayor][columna] < matriz[j][columna]:
                indice_elemento_mayor = j

        if indice_elemento_mayor != i:
            aux = matriz[i]
            matriz[i] = matriz[indice_elemento_mayor]
            matriz[indice_elemento_mayor] = aux
    return matriz

def escribir_csv(csv: str, datos: list[list]):
    """Recibe una matriz y la escribe en un archivo CSV

    Args:
        csv (str): Archivo CSV en donde se escribiran los datos
        datos (list[list]): Matriz con los datos a escribir
    """
    with open(file=csv, mode="w", encoding="utf-8") as archivo:
        largo_matriz = len(datos)
        largo_fila = len(datos[0])
        
        for i in range(largo_matriz):
            linea = ""
            for j in range(largo_fila):     
                linea += str(datos[i][j])
                if j == 0:
                    linea += ","
            archivo.write(linea + "\n")
            
def leer_json(archivo : str) -> dict[dict]:
    with open(file=archivo, mode="r", encoding="utf-8") as archivo:
        jsoncito = json.load(archivo) 
    return jsoncito    

def sobrescribir_json(archivo_og, actualizacion):
    with open(file=archivo_og, mode="w", encoding="utf-8") as archivo:
        json.dump(obj=actualizacion, fp=archivo, indent=4)