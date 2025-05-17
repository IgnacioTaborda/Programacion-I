def crear_matriz(filas : int, columnas : int, valor=0) -> list:
    """Esta función se encarga de crear una matriz fila x columna.

    Args:
        filas (int): Cantidad de filas que tendra la matriz
        columnas (int): Cantidad de columnas que tendra la matriz
        valor (int, optional): Se puede ingresar un valor con el que se
        inicializara la matriz. De no ingresarse uno, por default sera 0

    Returns:
        list: _description_
    """
    matriz = []
    for i in range(filas):
        fila = columnas * [valor]
        matriz.append(fila)
    return matriz

def cargar_datos_en_una_matriz(matriz : list, columna : int, valor : list) -> list:
    for i in range(len(matriz)):
        matriz[i][columna] = valor[i]
    return matriz
    


x = [[2, 2, 3, 8], [9, 10, 2, 7]]
print(x)
cargar_datos_en_una_matriz(x,0,[1, 2, 3, 4])
print(x)
cargar_datos_en_una_matriz(x,1,[1, 2, 3, 4])
print(x)
cargar_datos_en_una_matriz(x,2,[1, 2, 3, 4])
print(x)
cargar_datos_en_una_matriz(x,3,[1, 2, 3, 4])
print(x)