from utn_fra.datasets import (
    lista_poke_ids, lista_poke_nombres,
    lista_poke_tipos, lista_poke_poderes,
    lista_poke_condiciones
)

def crear_matriz_de_5_filas(lista_1 : list, lista_2 : list, lista_3 : list, lista_4 : list, lista_5 : list) -> list[list]:
    """Crea una función de 5 filas, estas se pasan por parametro.

    Args:
        lista_1 (list): Primera lista
        lista_2 (list): Segunda lista
        lista_3 (list): Tercera lista
        lista_4 (list): Cuarta lista
        lista_5 (list): Quinta lista

    Returns:
        list[list]: Retorna la matriz de  5 filas
    """
    matriz = [
        lista_1,lista_2,lista_3,lista_4,lista_5,
    ]
    return matriz

def convertir_columna_en_fila(matriz : list[list], columna : int) -> list:
    """Esta función se encarga de hacer que una columna se vuelva una fila.

    Args:
        matriz (list[list]): Matriz con que contiene la columna
        columna (int): Columna a convertir

    Returns:
        list: Retorna la columna convertida en una fila
    """
    fila = []
    for filas in range(len(matriz)):
        fila.append(matriz[filas][columna])
    return fila


def crear_matriz_traspuesta(matriz : list[list]) -> list[list]:
    """Esta función se encarga de crear una matriz traspuesta, es decir, 
    hacer que todas las columnas se vuelvan filas. Si la matriz no tiene elementos,
    retorna una matriz vacia

    Args:
        matriz (list[list]): Matrias a trasponer

    Returns:
        list[list]: Retorna la matriz traspuesta
    """
    largo_matriz = len(matriz)
    matriz_traspuesta = []

    if largo_matriz > 0:
        for columnas in range(len(matriz[0])):
            fila = convertir_columna_en_fila(matriz,columnas)
            matriz_traspuesta.append(fila)
    else:
        print("La matriz esta vacia")
    return matriz_traspuesta

print(lista_poke_poderes)
print(len(lista_poke_poderes))