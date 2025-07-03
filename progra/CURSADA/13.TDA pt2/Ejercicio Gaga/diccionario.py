from lady_gaga import playlist_lady_gaga 
from calculos import convertir_minutos_a_segundos
from datetime import date

def convertir_duracion_en_segundos(diccionario : dict, duracion : str) -> int:
    """Esta función recibe por parametro un diccionario que tiene la duración de
    un video en el formato minutos:segundos. Crea una lista: ['minutos', 'segundos'].
    Hace uso de otra función para convertir los minutos en segundos, parsea ambos elementos
    y los suma, para posteriormente retornar el resultado.

    Args:
        diccionario (dict): Diccionario que tiene el valor a convertir
        duracion (str): Key que contiene el valor a convertir

    Returns:
        int: Retorna el tiempo, originalmente escrito en minutos:segundos, en
        segundos.
    """
    tiempo = str(diccionario[duracion])
    tiempo = tiempo.split(":")

    minutos = int(tiempo[0])
    minutos = convertir_minutos_a_segundos(minutos)
    segundos = int(tiempo[1])

    duracion_segundos = minutos + segundos

    return duracion_segundos
    
def convertir_reproduciones_str_a_int(diccionario : dict, vistas : str) -> int:
    """Esta función se encarga de convertir la cantidad de reproducciones que tiene
    un video, vista con el formato "x millones" a número entero.

    Args:
        diccionario (dict): Diccionario que contiene las visitas
        vistas (str): Key con la cantidad de visitas a convertir

    Returns:
        int: Retorna la duración del video en formato entero.
    """
    reproducciones = str(diccionario[vistas])
    reproducciones = reproducciones.replace(" millones","")  
    reproducciones = int(reproducciones)
    reproducciones = reproducciones * 1000000
    
    return reproducciones

def añadir_colaboradores(diccionario : dict, titulo : str):
    tema = str(diccionario[titulo])
    colaboradores = tema.split(" - ")
    del colaboradores[-1]
    colaboradores = tema.split(" | ")
    return colaboradores
    
    
'''def convertir_str_en_date(diccionario : dict, fecha : str) -> date:
    """Esta función recibe por parametro un diccionario que tiene la fecha de
    un video de clase STR. Haciendo uso del modulo "datetime" cambia la clase a
    DATETIME.DATE

    Args:
        diccionario (dict): _description_
        fecha (str): _description_

    Returns:
        date: _description_
    """
    fecha_de_lanzamiento = diccionario[fecha]
    fecha_de_lanzamiento = date.fromisoformat(fecha_de_lanzamiento)
    return fecha_de_lanzamiento

'''


