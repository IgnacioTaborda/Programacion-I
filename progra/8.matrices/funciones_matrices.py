def mostrar_matriz(matriz:list):
    for i in range(len(matriz)): #fila
        for j in range(len(matriz[i])): #columna
            print(matriz[i][j], end=" ")
        print("")
        
def crear_una_matriz(cant_filas: int, cant_columnas: int, valor_inicial = 0)->list:
    matriz = []
    for i in range(cant_filas):
        fila = [valor_inicial] * cant_columnas
        matriz.append(fila) 
    return matriz
    
