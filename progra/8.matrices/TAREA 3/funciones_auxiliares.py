def mostrar_matriz(matriz:list):
    """Esta función recibe un matriz y muestra sus elementos uno por uno por consola, cuando 
    termina de recorrer cada fila hace un salto de linea.

    Args:
        matriz (list): Matriz que se va a mostar por consola
    """
    for i in range(len(matriz)): #fila
        for j in range(len(matriz[i])): #columna
            print(matriz[i][j], end=" ")
        print("")
        
def crear_una_matriz(cant_filas: int, cant_columnas: int, valor_inicial = 0)->list:
    """Crea una matriz de dimensiones can_filas x cant_columnas y las inicializa con un valor
    definido por el usuario, o por default en 0.

    Args:
        cant_filas (int): Cantidad de filas que tendra la matriz
        cant_columnas (int): Cantidad de columnas que tendra la matriz
        valor_inicial (int, optional): Valor de cada elemento de la matriz. Default 0.

    Returns:
        list: Retorna la matriz de dimensiones can_filas x cant_columnas
    """
    matriz = []
    for i in range(cant_filas):
        fila = [valor_inicial] * cant_columnas
        matriz.append(fila) 
    return matriz 
    
def validar_longitud_de_una_matriz(matriz:list) -> list:
    """Muestra la cantidad de filas y columnas que tiene una matriz en caso de que
    la matriz no este vacia

    Args:
        matriz (list): Matriz a validar

    Returns:
        list: Retorna una lista con la cantidad de filas y columnas
    """
    longitud_matriz = []
    if len(matriz) > 0: #Valida que la matriz no este vacia
        cant_filas = len(matriz)
        cant_columnas = len(matriz[0])
        longitud_matriz = [cant_filas, cant_columnas]
    else:
        print("La matriz esta vacia")
    return longitud_matriz
