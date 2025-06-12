def es_dato(diccionario : dict, key : str, valor : str) -> bool:
    """Recibimos un diccionario con una key y un valor. Si el valor
    se encuentra dentro de la key, se retornara True, de lo contrario,
    un False.

    Args:
        diccionario (dict): Diccionario que contiene los datos
        key (str): Key que contiene el valor a verificar
        valor (str): Valor a evaluar. Si la key contiene este valor, retorna True

    Returns:
        bool: Si el valor se encuentra dentro de la key, se retorna 
        True. De lo contrario, se retorna False
    """
    resultado = False
    if diccionario[key] == valor:
        resultado = True 

    return resultado

def calcular_max_raza(diccionario : list[dict], key_a_evaluar : str, key_raza : str, raza : str) -> dict:
    """Recorre una lista de diccionarios y evalúa el valor asociado a `key_a_evaluar`, 
    pero solo considera aquellos elementos cuyo valor en `key_raza` coincida con la `raza` indicada.

    Args:
        diccionario (list[dict]): Lista de diccionarios
        key_a_evaluar (str): Clave cuyo valor numérico se usará para encontrar el máximo
        key_raza (str): Clave que indica la raza del elemento
        raza (str): Raza que se usará como filtro 

    Returns:
        dict: Retorna el diccionario que contenga el mayor valor dentro de key_a_evaluar, siempre y cuando,
        pertenezca a la raza.
    """
    mas_alto = None
    for i in range(len(diccionario)):
        altura = diccionario[i][key_a_evaluar]
        es_raza = es_dato(diccionario[i],key_raza,raza)
        
        if (es_raza == True) and ((mas_alto == None) or (altura > mas_alto)):
            mas_alto =  altura
            diccionario_max = i
    return diccionario_max
            
        

