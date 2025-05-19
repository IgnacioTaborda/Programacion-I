from funciones_auxiliares import (
    validar_longitud_de_una_matriz, crear_una_matriz, mostrar_matriz, multiplicar_listas,sumar_elementos_de_una_lista,
    matriz_traspuesta
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
    
    if matriz_a_longitud[1] == matriz_b_longitud[0]: 
        
        matriz_resultado = crear_una_matriz(matriz_a_longitud[0],matriz_b_longitud[1])
        matriz_resultado_longitud = validar_longitud_de_una_matriz(matriz_resultado)
        matriz_b = matriz_traspuesta(matriz_b)

        for i in range(matriz_resultado_longitud[0]): 
            
            for j in range(matriz_resultado_longitud[1]): 
                
                calculo = multiplicar_listas(matriz_a[i],matriz_b[j])
                calculo = sumar_elementos_de_una_lista(calculo)
                matriz_resultado[i][j] = calculo
        
        return matriz_resultado
                     
    else:
        print("Error. Las matrices no tienen el mismo tamaño.")


matriz1 = [
    [1, 4],
    [2, 5],
    [3, 6]
]


matriz2 = [
    [9, 8],
    [7, 6]
]   




resultado = multiplicar_dos_matrices(matriz1, matriz2)
mostrar_matriz(resultado)



        
    

