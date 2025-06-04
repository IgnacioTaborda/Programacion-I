def pedir_numero() -> int:
    """Pide un número por consola y lo retorna parseado, si el
    dato ingresado solo contiene caracteres numericos. De lo la contrario
    función se llama así hasta que se ingrese un número valido.

    Returns:
        int: Retorna el número parseado a int
    """
    numero = input("Ingrese un número entero: ")
    if numero.isdigit():
        resultado = int(numero)
    else: 
        resultado = pedir_numero()
    return resultado

def validar_rango_numerico(numero : int, num_min : int, num_max : int) -> int:
    """Si el primer número ingresado por parametro se encuentra dentro del rango
    num_min - num_max, se retorna el número. De lo contrario la función se llama
    así misma hasta que se ingrese un número valido.

    Args:
        numero (int): Número a validar
        num_min (int): Número minimo aceptado
        num_max (int): Número maximo aceptado

    Returns:
        int: Retorna el número validado
    """
    if num_max >= numero >= num_min:
        resultado = numero
    else:
        print(f'''
              Error, el número {numero} no se encuentra dentro del rango {num_min} - {num_max}.
              Por favor, ingrese un número que se encuentre dentro del rango
              '''
            )
        numero = pedir_numero()
        resultado = validar_rango_numerico(numero,num_min,num_max)
    return resultado