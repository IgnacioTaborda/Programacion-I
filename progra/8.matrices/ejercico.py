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
            dato = lista_fila[j]
            print(dato, end=" ")

mostrar_matrix(incializar_matriz(3,5,7))