def es_dato(diccionario : dict, key : str, valor : str) -> bool:
    """Recibimos un diccionario con una key y un valor. Si el valor
    se encuentra dentro de la key, se retornara True, de lo contrario,
    un False.

    Args:
        diccionario (dict): Diccionario que contiene los datos
        key (str): Key que contiene el valor a verificar
        valor (str): Valor a evaluar

    Returns:
        bool: Si el valor se encuentra dentro de la key, se retorna 
        True. De lo contrario, se retorna False
    """
    resultado = False
    if diccionario[key] == valor:
        resultado = True

    return resultado

def calcular_min(diccionario : dict, key : str, valor : str) -> str:
    pass
