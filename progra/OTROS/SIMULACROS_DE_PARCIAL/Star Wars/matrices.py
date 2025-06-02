from utn_fra.datasets import (
    lista_sw_nombres, lista_sw_generos, lista_sw_alturas, lista_sw_pesos
)
def crear_matriz_de_4_filas(lista_1 : list, lista_2 : list, lista_3 : list, lista_4 : list) -> list[list]:
    """Se la pasan por parametro 4 listas y se devuelve una matriz de 4 filas con X cantidad de columnas.

    Args:
        lista_1 (list): Lista 1
        lista_2 (list): Lista 2
        lista_3 (list): Lista 3
        lista_4 (list): Lista 4

    Returns:
        list[list]: Retorna una matriz 
    """
    matriz = [lista_1,lista_2,lista_3,lista_4]
    return matriz 

def parsear_int(matriz : list[list], fila : int):
    """Esta función sirve para convertir strings, que solo contengan digitos,
    en números enteros.

    Args:
        lista (list): Lista a convertir

    Returns:
        list: Retorna la lista con los números parseados
    """
    largo_columnas = len(matriz[0])
        
    for i in range(largo_columnas):
        elemento = matriz[fila][i]
        if elemento.isdigit():
            elemento = int(elemento)
        matriz[fila][i] = elemento
    
    

def convertir_columna_en_fila(matriz : list[list], columna : int) -> list:
    """Esta función recibe por parametro una función y una columna, la columna la convierte
    en una fila.

    Args:
        matriz matriz (list[list]): _description_
        columna (int): Columna a convertir

    Returns:
        list: Retorna la columna convertida en una lista
    """
    fila = []
    for filas in range(len(matriz)):
        fila.append(matriz[filas][columna])
    return fila


def trasponer_matriz(matriz : list[list]):
    """Recibe por parametro una matriz y convierte sus columnas en filas.

    Args:
        matriz (list[list]): Matriz a trasponer

    Returns:
        list[list]: Retorna la matriz traspuesta
    """
    matriz_traspuesta = []
    for columnas in range(len(matriz[0])):
        fila = convertir_columna_en_fila(matriz,columnas)
        matriz_traspuesta.append(fila)
    return matriz_traspuesta

def encontrar_minimo(matriz, inicio,fila):
    min_index = inicio
    for j in range(inicio + 1, len(matriz[fila])):
        if matriz[fila][j] < matriz[fila][min_index]:
            min_index = j
    return min_index

def selection_sort_ascendente(matriz : list[list], fila : int):
    largo_columna = len(matriz[0])
    for i in range(largo_columna):
        min_index = encontrar_minimo(matriz, i,fila)
        temp = matriz[fila][i]
        matriz[fila][i] = matriz[fila][min_index]
        matriz[fila][min_index] = temp
    