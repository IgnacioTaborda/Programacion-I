def crear_matriz(lista_1 : list, lista_2 : list, lista_3 : list, lista_4 : list, lista_5 : list) -> list[list]:
    """Crea una matriz en base a las listas pasadas por parametro y la retorna

    Args:
        lista_1 (list): Lista para formar la matriz de la función
        lista_2 (list): Lista para formar la matriz de la función
        lista_3 (list): Lista para formar la matriz de la función
        lista_4 (list): Lista para formar la matriz de la función
        lista_5 (list): Lista para formar la matriz de la función

    Returns:
        list[list]: Retorna una matriz de 5 filas.
    """
    matriz = [
        lista_1,
        lista_2,
        lista_3,
        lista_4,
        lista_5
    ]
    return matriz

def crear_texto_info_pokemon(matriz : list[list], indice_columnas : int) -> str:
    """Recorre la fila de la matriz en la columna especificada y crea un texto con
    la info de cada fila en esa misma columna,

    Args:
        matriz (list[list]): La matriz de datos
        indice_columnas (int): EL indice de la columna actual de donde se tienen que sacar los datos fila a fila

    Returns:
        str: La info de toda la columna 
    """
    texto = ""
    for k in range(len(matriz)):
        texto += f"{matriz[k][indice_columnas]},"
    texto = texto[:-1]
    return texto


def mostrar_matriz(matriz : list[list]):
    """Muestra la info de la matriz con cada campo separado por coma.

    Args:
        matriz (list[list]): La matriz de los datos
        
    """
    cant_columnas = len(matriz[0])
    for i in range(cant_columnas):
        texto = crear_texto_info_pokemon(matriz,i)
        print(texto)
        

def calcular_promedio_matriz(matriz : list[list], indice_fila : int) -> float:
    promedio = 0
    if matriz:    
        cantidad = len(matriz[indice_fila])
        suma = 0
        
        for i in matriz[indice_fila]:
            suma += i
        promedio = suma / cantidad
    return promedio


def obtener_indices_promedio_superior(matriz : list[list], indice_fila : int) -> list[int]:
    promedio = calcular_promedio_matriz(matriz,indice_fila)
    lista_indices = []
    print(f"El promedio de Poder es: {promedio:5.2f}")
    for i in range(len(matriz[indice_fila])):
        if matriz[indice_fila][i] > promedio:
            lista_indices.append([i])
    return lista_indices

def obtener_elemento(matriz_base : list[list],matriz_filtro : list[list],indice_columna : int):
    for k in range(len(matriz_base)):
        elemento = matriz_base[k][indice_columna]
        matriz_filtro[k].append(elemento)

def filtrar_matriz_poder_superior(matriz : list[list], indice_fila : int):
    indices_superadores = obtener_indices_promedio_superior(matriz,indice_fila)
    matriz_filtrada = [
        [],[],[],[],[]
    ]
    
    for i in indices_superadores:
        for k in range(len(matriz)):
            elemento = matriz[k][i]
            matriz_filtrada[k].append(elemento)
    return matriz_filtrada

#4 ---------------------------------------------------------------------------------------------------
def obtener_indices_filtrado(matriz : list[list], indice_fila : int, elemento_buscar : str) -> list[int]:

    lista_indices = []
    
    for i in range(len(matriz[indice_fila])):
        if matriz[indice_fila][i] > elemento_buscar:
            lista_indices.append([i])
    return lista_indices

def filtrar_matriz_poder_superior(matriz : list[list], indice_fila : int, elemento_buscar : str):
    indices_superadores = obtener_indices_filtrado(matriz,indice_fila,elemento_buscar)
    matriz_filtrada = [
        [],[],[],[],[]
    ]
    
    for i in indices_superadores:
        for k in range(len(matriz)):
            elemento = matriz[k][i]
            matriz_filtrada[k].append(elemento)
    return matriz_filtrada