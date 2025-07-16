import os
import random
import json
import herramientas.funciones_archivos as fun_archivos
import variables as var

######## CARTA #########
def extraer_datos_carta(archivo : list) -> dict:
    """Crea un diccionario que contiene las stats de la carta

    Args:
        archivo (list): Lista que contiene las stats de la carta

    Returns:
        dict: Retorna un diccionario que tiene las stats
        de la carta
    """
    carta = {
        "ID" : archivo[0],
        "HP" : archivo[2],
        "ATK" : archivo[4],
        "DEF" : archivo[6],
        "Bonus" : int(archivo[7]),
    }
    return carta

def armar_mazo_carpeta(ruta_carpeta : str) -> dict:
    """Crea un diccionario que contiene sub-diccionarios con
    cartas y sus stats.

    Args:
        ruta_carpeta (str): Ruta de la carpeta que tiene las
        cartas

    Returns:
        dict: Retorna un diccionario que tiene sub-diccionarios,
        que contienen cartas con sus valores (ID, HP, ATK, DEF y BONUS)
    """
#No arma el mazo para jugar, solo es la carpeta
    mazo_dict = {}
    contador = 1

    for archivo in os.listdir(ruta_carpeta):
        ruta_archivo = os.path.join(ruta_carpeta, archivo) #literalmente es la ruta del archivo
        
        if os.path.isfile(ruta_archivo):# Verificar si es un archivo y no una subcarpeta
            archivo = archivo.replace(".png","")
            archivo = archivo.split("_")
            largo_archivo = len(archivo)
            
            if largo_archivo == 8:
                archivo = extraer_datos_carta(archivo)
                mazo_dict[contador] = archivo
                contador += 1
    return mazo_dict


def armar_mazo_aleatorio(cantidades: dict, cartas_rutas: dict) -> dict:
    """Crea un mazo aleatorio respetando las cantidades del JSON.

    Args:
        cantidades (dict): Diccionario con las cantidades de cartas por expansión.
        cartas_rutas (dict): Diccionario con las rutas de las cartas y sus stats.

    Returns:
        dict: Mazo aleatorio generado con las cartas especificadas por cantidad.
    """
    mazo_aleatorio = {}

    # Iteramos sobre las cantidades de cartas
    for nombre_mazo, cantidad in cantidades.items():
        # Comprobamos que la ruta esté presente en cartas_rutas
        if nombre_mazo in cartas_rutas:
            # Obtenemos la ruta de las cartas de esa expansión
            ruta = cartas_rutas[nombre_mazo]
            # Usamos la función que arma el mazo desde la ruta (tú ya tienes algo similar)
            cartas_mazo = armar_mazo_carpeta(ruta)  # Obtener las cartas de la carpeta
            # Seleccionamos aleatoriamente las cartas necesarias para el mazo
            mazo_aleatorio[nombre_mazo] = random.sample(list(cartas_mazo.values()), cantidad)
    
    return mazo_aleatorio

def unificar_cartas(mazo: dict) -> list:
    """Une todas las cartas de un mazo en una lista única y las mezcla aleatoriamente."""
    cartas_unidas = []
    for cartas in mazo.values():
        cartas_unidas.extend(cartas)
    
    random.shuffle(cartas_unidas)  # Mezcla las cartas para que el orden sea aleatorio
    return cartas_unidas

def sumar_stats_totales(cartas: list) -> dict:
    """Suma las stats totales del mazo."""
    total = {"HP": 0, "ATK": 0, "DEF": 0}
    for carta in cartas:
        total["HP"] += int(carta["HP"])
        total["ATK"] += int(carta["ATK"])
        total["DEF"] += int(carta["DEF"])
    return total

######## PELEA #########



# x = armar_mazo_clase(ruta_carpeta)
# print(x)

# def armar_mazo_total(archivo_json : str) -> dict:
#     """Crea un diccionario que contiene multiples diccionarios
#     que sub-diccionarios que tienen cartas con sus valores.

#     Args:
#         archivo_json (str): Ruta del JSON que tiene las rutas
#         de los mazos.

#     Returns:
#         dict: Retorna un diccionario que contiene otros diccionarios,
#         dentro de dichos diccionarios, contienen otros diccionarios que
#         son las cartas del mazo. La etiqueta es el número de carta y en 
#         el valor se cuentra el: ID, HP, ATK, DEF y BONO

#     """
#     archivo_json = fun_archivos.leer_json(archivo_json)
#     cartas_rutas = archivo_json.get("rutas_cartas")

#     for nombre_mazo, ruta in cartas_rutas.items():
#         cartas_rutas[nombre_mazo] = armar_mazo_carpeta(ruta)
#     return cartas_rutas