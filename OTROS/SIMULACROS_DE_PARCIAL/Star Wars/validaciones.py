def validar_numero() -> int:
    """Pide que se ingrese un número por consola, si solo contiene digitos, retorna
    el número parseado. De lo contrario, la función se llama a si misma hasta que se 
    ingrese un número

    Returns:
        int: Retorna el numero ingresado por consola 
    """
    numero = input("Ingrese un número: ")
    if numero.isdigit():
        numero = int(numero)
        return numero
    else:
        return validar_numero() 
        
        
def validar_rango_numerico(numero : int, num_min : int, num_max : int) -> int:
    """Se encarga de validar que el número ingresado por parametro se encuentre 
    dentro del rango num_min - num_max. De lo contrario, se le pide al usuario que
    ingrese un nuevo número por consola y se verifica que se encuentre dentro del rango.

    Args:
        numero (int): Número a validar
        num_min (int): Número minimo valido
        num_max (int): Número maximo valido

    Returns:
        int: Retorna el número validado
    """
    if num_max >= numero >= num_min:
        return numero
    else:
        print(f"Error. El número no se encuentra dentro del rango {num_min} - {num_max}")
        numero = validar_numero()
        return validar_rango_numerico(numero,num_min,num_max)        


