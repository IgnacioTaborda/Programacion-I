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

def calcular_promedio_lista(lista : list) -> float:
    """Suma todos los elementos de una lista y calcula el promedio

    Args:
        lista (list): Lista a calcular

    Returns:
        float: Promedio de la lista
    """
    largo_lista = len(lista)
    acumulador = 0
    for i in range(largo_lista):
        acumulador += lista[i]
    promedio = acumulador / largo_lista
    promedio = round(promedio,2)
    return promedio


def regla_de_3_simples(numero: int, total: int): 
    resultado = (numero * 100) / total
    return resultado