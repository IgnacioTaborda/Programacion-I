from utn_fra.datasets import (
    lista_autos_cantidades, lista_autos_ganancias,
    lista_autos_marcas, lista_autos_modelos, lista_autos_precios)

def mostrar_menu():
    """Muestra un menu con 9 opciones ya definidas
    """
    texto = \
        '''
        Aclaración: Si desea saber las ganancias, previamente debe seleccionar la Opción 5, de lo contrario, no se mostrar
        1 - Obtener existencias.
        2 - Cantidad total de unidades almacenadas entre todos los vehículos de la concesionaria
        3 - Datos completos del garaje que almacena menos unidades de vehículos
        4 - Datos completos del/los garaje/s que tiene la máxima cantidad de unidades almacenadas
        5 - Obtener recaudación
        6 - Garajes que almacenan 6 o más unidades de vehículos.
        7 - Mostrar en consola lo siguiente:
            a.Los porcentajes de unidades de cada marca de vehículo sobre el total de vehículos almacenados entre 
            todos los garajes de la sede matriz.
            b.Todos los datos del garaje con el máximo porcentaje de vehículos almacenados respecto al total.
        8 - Generar un informe con la recaudación de cada garaje, ordenada de mayor a menor
        9 - Salir
        '''
    print(texto)
    
def obtener_existencias(garaje:int):
    """Da un informe por consola con: el número de garage, marca que almacena, modelo, 
    precio unitario, cantidad y ganancias.

    Args:
        garaje (int): El número de garaje
    """
    mensaje= \
        f'''
        Garaje N° {garaje + 1}
        Marca: {lista_autos_marcas[garaje]}
        Modelo: {lista_autos_modelos[garaje]}
        Precio Unit: ${lista_autos_precios[garaje]}
        Cantidad: {lista_autos_cantidades[garaje]}
        Ganancias: {lista_autos_ganancias[garaje]}
        '''
        
    print(mensaje) 
    
def mensaje_ej_7(marca : str, porcentaje : int):
    print(f"{marca} tiene el {porcentaje}% de coches")