from utn_fra.datasets import (
    lista_sw_nombres, lista_sw_generos, lista_sw_alturas, lista_sw_pesos
)
def calcular_promedio_matriz(matriz : list[list], fila : int) -> float:
    """Recibe por parametro una matriz y una fila para calcular el promedio
    de dicha fila.

    Args:
        matriz (list[list]): Matriz que contenga la fila a promediar
        fila (int): Fila a promediar

    Returns:
        float: Retorna el promedio de la fila
    """
    acumulador = 0
    largo_columna = len(matriz[0])
    
    for i in range(largo_columna):
        acumulador += matriz[fila][i]
    
    promedio = acumulador / largo_columna
    promedio = round(promedio,2)
    
    return promedio

