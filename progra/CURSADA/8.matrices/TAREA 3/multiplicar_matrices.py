from funciones_auxiliares import (
    validar_longitud_de_una_matriz, crear_una_matriz, mostrar_matriz
)

def multiplicar_dos_matrices(matriz_a: list, matriz_b: list) -> list | None:
    """Esta función se encarga de multiplicar dos matrices siempre y cuando la primer matriz sea 
    de dimension (mxn) y la segunda de dimension (nxp)

    Args:
        matriz_a (list): La primer matriz que se quiere multiplicar
        matriz_b (list): La segunda matriz que se quiere multiplicar

    Returns:
        list | None: En caso de que la primer matriz sea de dimension (mxn) y la segunda de dimension (nxp)
        se retorna una nueva matriz con el resultado, de lo contrario, no retorna nada.
    """
    matriz_a_longitud = validar_longitud_de_una_matriz(matriz_a)
    matriz_b_longitud = validar_longitud_de_una_matriz(matriz_b)

    matriz_resultado = []
    
    if matriz_a_longitud[1] == matriz_b_longitud[0]: 
        
        matriz_resultado = crear_una_matriz(matriz_a_longitud[0],matriz_b_longitud[1])
        matriz_resultado_longitud = validar_longitud_de_una_matriz(matriz_resultado)


# Evita usar 3 bucles anidados, es una muy mala practica.

        for i in range(matriz_resultado_longitud[0]):
            
            for j in range(matriz_resultado_longitud[1]):
                
                for k in range(matriz_a_longitud[1]): 
                    
                    resultado = matriz_a[i][k] * matriz_b[k][j]
                    matriz_resultado[i][j] += resultado
                    
        return matriz_resultado       
    else:
        print("Error. Las matrices no tienen el mismo tamaño.")


matriz_1 = [
    [1, 2, 3, 4, 5],
    [0, 1, 0, 1, 0],
    [9, 8, 7, 6, 5],
    [1, 0, 1, 0, 1]
]

matriz_2 = [
    [1, 0, 1],
    [2, 1, 0],
    [3, 0, 2],
    [4, 1, 0],
    [5, 0, 1]
]


resultado = multiplicar_dos_matrices(matriz_1, matriz_2)
mostrar_matriz(resultado)