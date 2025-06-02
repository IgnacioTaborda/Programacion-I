def calcular_promedio_matriz(matriz : list[list], fila : int) -> float: 
    """Recibe por parametro una matriz y una fila para calcular el promedio
    de dicha fila.

    Args:
        matriz (list[list]): Matriz que contenga la fila a promediar
        fila (int): Fila a promediar

    Returns:
        float: Retorna el promedio de la fila. Si no contiene números, se retorna 0.
    """
    acumulador = 0
    contador = 0
    largo_columna = len(matriz[0])
    
    for i in range(largo_columna):
        tipo = type(matriz[fila][i])
        if tipo == int or tipo == float:
            acumulador += matriz[fila][i]
            contador += 1
    
    if contador != 0: 
        promedio = acumulador / contador
        promedio = round(promedio,2)
    else:
        promedio = 0
        
    return promedio

'''matriz = [
    [1, 2.5, "hola", 42],
    [3.14, "python", 7],
    [0.99, "mundo", "GPT"]
]

print(calcular_promedio_matriz(matriz,0))
print(calcular_promedio_matriz(matriz,1))
'''