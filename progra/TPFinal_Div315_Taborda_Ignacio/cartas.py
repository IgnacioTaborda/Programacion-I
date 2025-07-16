import os

def extraer_datos_carta(archivo : list) -> dict:
    carta = {
        "ID" : archivo[0],
        "HP" : archivo[2],
        "ATK" : archivo[4],
        "DEF" : archivo[6],
        "Bonus" : archivo[7],
    }
    return carta

ruta_carpeta = "./assetss/cartas/black_deck_expansion_1"

def armar_mazo_clase(ruta_carpeta):
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

x = armar_mazo_clase(ruta_carpeta)
print(x)