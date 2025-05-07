from utn_fra.datasets import (
    lista_autos_cantidades, lista_autos_ganancias,
    lista_autos_marcas, lista_autos_modelos, lista_autos_precios)

def mostrar_menu():
    texto = \
        '''
        1 - Obtener existencias: para ello deberá crear una función que cargue la existencia de cada vehículo en todos los 
            garajes de la concesionaria.
        2 - Calcular la cantidad total de unidades almacenadas entre todos los vehículos de la concesionaria
        3 - Mostrar en consola los datos completos del garaje que almacena menos unidades de vehículos
        4 - Mostrar en consola los datos completos del/los garaje/s que tiene la máxima cantidad de unidades almacenadas
        5 - Obtener recaudación: para ello deberás crear una función que calcule la recaudación de cada garaje y sobreescriba 
            el resultado en la ubicación correspondiente de la columna “Ganancias” (lista de ganancias) de cada garage, 
            teniendo en cuenta su precio unitario y cantidad de unidades almacenadas en cada garaje
        6 - Mostrar la cantidad de garajes que hayan almacenado 6 o más unidades de vehículos.
        7 - Mostrar en consola lo siguiente:
            a.Los porcentajes de unidades de cada marca de vehículo sobre el total de vehículos almacenados entre 
            todos los garajes de la sede matriz.
            b.Todos los datos del garaje con el máximo porcentaje de vehículos almacenados respecto al total.
        8 - Generar un informe con la recaudación de cada garaje, ordenada de mayor a menor
        9 - Salir
        '''
    print(texto)
    
def obtener_existencias(garage:int): 
        mensaje= \
            f'''
            Garaje N° {garage + 1}
            Marca: {lista_autos_marcas[garage]}
            Modelo: {lista_autos_modelos[garage]}
            Precio Unit: ${lista_autos_precios[garage]}
            Cantidad: {lista_autos_cantidades[garage]}
            Ganancias: {lista_autos_ganancias[garage]}
            '''
            
        print(mensaje) 
        
def imprimir_porcentaje_de_unidades(porcentaje:float, marca:str):
    print(f"El porcentaje de {marca} es de: {round(porcentaje, 2)}%")