def calcular_promedio(matriz : list[list], fila : int) -> float:
    """Esta función suma todos los elementos de una fila de una matriz

    Args:
        matriz (list[list]): Matriz que contenga la fila a sumar
        fila (int): Columna a sumar

    Returns:
        float: Retorna el promedio de dicha fila
    """
    columnas = len(matriz[0])
    if columnas > 0: 
        acumulador_de_poder = 0
        for i in range(columnas):
            acumulador_de_poder += matriz[fila][i]
            
        promedio_poder = acumulador_de_poder / columnas
        promedio_poder = round(promedio_poder,2)
        return promedio_poder  
    else:
        print("La matriz esta vacia!")