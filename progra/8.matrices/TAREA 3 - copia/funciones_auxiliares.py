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
        list: Retorna una lista con la cantidad de [filas, columnas]
    """
    longitud_matriz = []
    if len(matriz) > 0: #Valida que la matriz no este vacia
        cant_filas = len(matriz)
        cant_columnas = len(matriz[0]) #matriz[0] = primera fila
        longitud_matriz = [cant_filas, cant_columnas]
    else:
        print("La matriz esta vacia")
    return longitud_matriz

def multiplicar_listas(lista_1 : list, lista_2 : list) -> list:
    longitud_lista_1 = len(lista_1)
    longitud_lista_2 = len(lista_2)
    
    if longitud_lista_1 == longitud_lista_2:
        lista_resultado = []
        for i in range(longitud_lista_1):
            resultado = lista_1[i] * lista_2[i]
            lista_resultado.append(resultado)
        return lista_resultado
    else:
        print("No se pueden multiplicar las listas ingresadas")
        
def sumar_elementos_de_una_lista(lista : list) -> int:
    """Suma todos los elementos de una lista

    Args:
        lista (list): Lista númerica a sumar

    Returns:
        int: Retorna la suma de todos los elementos de una lista
    """
    resultado = 0
    for i in range(len(lista)):
        resultado += lista[i]
    return resultado

                
def matriz_traspuesta(matriz: list) -> list:
    """Esta función recibe por parametro una matriz y convierte las columnas en filas y
    viceversa.

    Args:
        matriz (list): Matriz a convertir

    Returns:
        list: Retorna la matriz traspuesta
    """
    matriz_longitud = validar_longitud_de_una_matriz(matriz) #3,4
    matriz_resultado = crear_una_matriz(matriz_longitud[1],matriz_longitud[0]) #4,3
    for i in range(matriz_longitud[1]): #4
        for j in range(matriz_longitud[0]): #3
            matriz_resultado[i][j] = matriz[j][i]
            #al poner matriz "j" antes que "i" hago que se mantenga en la fila 1 pero que agarre los primeros elementos de la columna
    return matriz_resultado