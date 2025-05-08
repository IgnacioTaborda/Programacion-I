def mostrar_matriz(matriz:list):
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
        valor_inicial (int, optional): Valor de cada elemento de la matriz. Defaults to 0.

    Returns:
        list: Retorna la matriz de dimensiones can_filas x cant_columnas
    """
    matriz = []
    for i in range(cant_filas):
        fila = [valor_inicial] * cant_columnas
        matriz.append(fila) 
    return matriz
    
def encontrar_valor_entero(matriz: list, valor: int):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                print(f"Se ha encontrado el {valor}, en la fila {i} columna {j}!")
                
def sumar_matrices(matriz_1: list, matriz_2: list) -> list:
    matriz_1_longitud = validar_longitud_de_una_matriz(matriz_1)
    matriz_2_longitud = validar_longitud_de_una_matriz(matriz_2)
    matriz_resultado = []
    if matriz_1_longitud == matriz_2_longitud:
        matriz_resultado = crear_una_matriz(matriz_1_longitud[0],matriz_1_longitud[1])
        for i in range(matriz_1_longitud[0]):
            suma = 0
            for j in range(matriz_1_longitud[1]):
                suma = matriz_1[i][j] + matriz_2[i][j]
                matriz_resultado[i][j] = suma
    else:
        print("Error. Las matrices no tienen el mismo tamaño.")
    return matriz_resultado
    
    
def validar_longitud_de_una_matriz(matriz:list) -> list:
    """Muestra la cantidad de filas y columnas que tiene una matriz en caso de que
    la matriz no este vacia

    Args:
        matriz (list): Matriz a validar

    Returns:
        list: Retorna una lista con la cantidad de filas y columnas
    """
    longitud_matriz = []
    if len(matriz) > 0: #VALIDAMOS QUE LA MATRIZ NO ES VACIA
        cant_filas = len(matriz)
        cant_columnas = len(matriz[0])
        longitud_matriz = [cant_filas, cant_columnas]
    else:
        print("La matriz esta vacia")
    return longitud_matriz

def multiplicar_matriz_escalar(matriz: list, escalar: int) -> list:
    matriz_longitud = validar_longitud_de_una_matriz(matriz)
    matriz_resultado = crear_una_matriz(matriz_longitud[0],matriz_longitud[1], None)
    for i in range(matriz_longitud[0]):
        for j in range(matriz_longitud[1]):
            multiplicacio = matriz[i][j] * escalar
            matriz_resultado[i][j] = multiplicacio
    return matriz_resultado

def matriz_traspuesta(matriz: list):
    matriz_longitud = validar_longitud_de_una_matriz(matriz) #3,4
    matriz_resultado = crear_una_matriz(matriz_longitud[1],matriz_longitud[0]) #4,3
    for i in range(matriz_longitud[1]): #4
        for j in range(matriz_longitud[0]): #3
            matriz_resultado[i][j] = matriz[j][i]
            #al poner matriz "j" antes que "i" hago que se mantenga en la fila 1 pero que agarre los primeros elementos de la columna
    return matriz_resultado


def multiplicar_dos_matrices(matriz_a: list, matriz_b: list):
    matriz_a_longitud = validar_longitud_de_una_matriz(matriz_a)#fila x columna
    matriz_b_longitud = validar_longitud_de_una_matriz(matriz_b)#fila x columna
    matriz_resultado = []
    
    #Verifico que la cantidad de columnas de la matriz a sea igual a la cantidad de filas de la matriz b
    if matriz_a_longitud[1] == matriz_b_longitud[0]:
        #CREO LA MATRIZ RESULTADO CON SUS DIMENSIONES CORRESPONDIENTES
        matriz_resultado = crear_una_matriz(matriz_a_longitud[0],matriz_b_longitud[1])
        matriz_resultado_longitud = validar_longitud_de_una_matriz(matriz_resultado)#fila x columna
        #HACER QUE LA MATRIZ B SEA TRASPUESTA
        #matriz_b = matriz_traspuesta(matriz_b)
        for i in range(matriz_resultado_longitud[0]): #aca paso las dos listas
            for j in range(matriz_resultado_longitud[1]): #aca paso las columnas
                for k in range(matriz_a_longitud[1]):
                    resultado = matriz_a[i][k] * matriz_b[k][j]
                    matriz_resultado[i][j] += resultado
        return matriz_resultado       
    else:
        print("Error. Las matrices no tienen el mismo tamaño.")


matriz_a = [
    [3, 7, 5],
    [12, 2, 11],
]

matriz_b = [
    [3, 16],
    [1, 4],
    [4, 22]
]
resultado = multiplicar_dos_matrices(matriz_a, matriz_b)
mostrar_matriz(resultado)


# matriz_a_longitud = validar_longitud_de_una_matriz(matriz_a)#fila x columna
# matriz_b_longitud = validar_longitud_de_una_matriz(matriz_b)#fila x columna
# matriz_resultado = crear_una_matriz(matriz_a_longitud[0],matriz_b_longitud[0])


# print(matriz_resultado)
# print(matriz_b_longitud)