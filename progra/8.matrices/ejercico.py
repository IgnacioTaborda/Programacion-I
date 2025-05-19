def incializar_matriz(cant_filas:int, cant_columnas:int, valor_default:int) -> list[list]:
    matriz_resultante = []
    
    for indice in range(cant_filas):
        fila = [valor_default] * cant_columnas #4
        #[true, true, true, true]
        matriz_resultante.append(fila)
    return matriz_resultante

def mostrar_matrix(matriz:list[list]): #EN LA PPT ESTA MOCHO MEJOR BV
    for i in range(len(matriz)):
        lista_fila = len(matriz[i])
        for j in range(lista_fila):
            dato = matriz[i][j]
            print(dato, end=" ")
        print("")

matriz = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

mostrar_matrix(matriz)