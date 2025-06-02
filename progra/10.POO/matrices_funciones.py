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