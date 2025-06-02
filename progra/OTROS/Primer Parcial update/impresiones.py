from utn_fra.datasets import (
    lista_bzrp_nombres, lista_bzrp_vistas, lista_bzrp_duracion
)

matriz = [lista_bzrp_nombres, lista_bzrp_vistas, lista_bzrp_duracion]


def imprimir_menu():
    menu = '''
    1 - Recorrer la matriz y mostrar la info
    2 - Buscar y mostrar la info de los videos que superen el promedio de views y también el promedio de duración.
    3 - Ordenar la matriz por views DES de todos los videos.
    4 - Filtrar en la matriz todos los videos en cuyo nombre haya un numeral
    5 - Trasponer la matriz y mostrar su información prolija.
    6 - Salir.
    '''
    print(menu)
    
def imprimir_datos_matriz(matriz : list[list], columna : int): 
    """Imprime los datos de una columna 

    Args:
        matriz (list[list]): Matriz que contenga los datos
        columna (int): Columna con los datos a mostrar
    """
    datos = f'''
    {matriz[0][columna]} | {matriz[1][columna]} | {matriz[2][columna]}
    '''
    print(datos) 
 
    
def imprimir_datos_matriz_traspuesta(matriz : list[list], fila : int):
    """Imprime los datos de una fila 

    Args:
        matriz (list[list]): Matriz que contenga los datos
        fila (int): Fila con los datos a mostrar
    """
    datos = f''' 
    {matriz[fila][0]} | {matriz[fila][1] } | {matriz[fila][2]}
    '''
    print(datos)
    