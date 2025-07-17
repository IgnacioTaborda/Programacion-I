def crear_matriz(lista_1 : list, lista_2 : list,lista_3 : list) -> list[list]:
    """Esta función se encarga de hacer una matriz de filas.

    Args:
        lista_1 (list): Primera fila
        lista_2 (list): Segunda fila
        lista_3 (list): Tercera fila

    Returns:
        list[list]: Retorna una matriz de 3 filas
    """
    matriz = [lista_1,lista_2,lista_3]
    return matriz

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

def encontrar_valor(matriz : list[list], fila : int, valor : any) -> list:
    """Esta función se encarga de recorrer la fila de una matriz y buscar en cada
    elemento para revisar que contenga el valor ingresado. Si el elemento contiene
    el valor, se agrega su indice en una lista.

    Args:
        matriz (list[list]): Matriz que contiene la fila a recorrer
        fila (int): Fila a recorrer
        valor (any): Valor a buscar

    Returns:
        list: Retorna una lista con los indices de los elementos que 
        contienen el valor
    """
    lista_indices = []
    
    for i in range(len(matriz[fila])):
        if valor in matriz[fila][i]:
            lista_indices.append(i)
    return lista_indices


def obtener_indice_mayor(matriz : list[list], inicio : int, fila : int, indice_mayor : int) -> int:
    """Esta función se encarga de obtener el indice del mayor valor que hay en la lista
        #obtener_indice_mayor(matriz, i + 1, fila, i)
    Args:
        matriz (list[list]): Matriz que contenga la lista
        inicio (int): Indice con el que empezamos a comparar
        fila (int): Lista a recorrer
        indice_mayor (int): Primer indice que usaremos para comparar

    Returns:
        int: Retorna el indice en el que se encuentre el mayor valor
    """
    largo_columna = len(matriz[fila])
    for j in range(inicio, largo_columna):
        if int(matriz[fila][indice_mayor]) < int(matriz[fila][j]):
            indice_mayor = j
    return indice_mayor

def intercambiar_columnas(matriz : list[list], indice_mayor : int, columna : int):
    """Esta función se encarga de reorganizar las columnas de la matriz de mayor a menor.

    Args:
        matriz (list[list]): Matriz que contiene las columnas
        indice_mayor (int): Indice en el que se encuentra el mayor valor
        columna (int): Columna a mover
    """
    for f in range(len(matriz)):
        aux = matriz[f][columna]
        matriz[f][columna] = matriz[f][indice_mayor]
        matriz[f][indice_mayor] = aux

def ordenar_fila_matriz_descendente(matriz : list[list], fila : int):
    """Esta función se encarga de ordenar los valores de la fila de una columna de
    menor a mayor

    Args:
        matriz (list[list]): Matriz que contenga la fila a ordenar
        fila (int): Fila a ordenar
    """
    largo_columna = len(matriz[fila])
    for i in range(largo_columna):
        indice_mayor = obtener_indice_mayor(matriz, i + 1, fila, i)
        if indice_mayor != i:
            intercambiar_columnas(matriz, indice_mayor, i)
                