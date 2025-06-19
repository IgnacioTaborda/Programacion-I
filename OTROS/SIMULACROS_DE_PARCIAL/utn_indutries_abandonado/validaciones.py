def validar_numero() -> int:
    """Esta función pide que se ingrese un número por consola, y valida que el dato
    ingresado solo contenga caracteres numericos, de lo contrario, se llama así misma
    hasta que se ingrese un dato valido.

    Returns:
        int: Retorna el número parseado a int
    """
    numero = input("Ingrese un número: ")
    if numero.isdigit():
        numero_int = int(numero)
        return numero_int
    else:
        print("Error.El dato ingresado debe contener solo números")
        return validar_numero()
    
def validar_rango_numerico(numero : int, num_min : int, num_max : int) -> int:
    """Esta función se encarga de recibir un número por parametro y valida que se encuentre
    dentro del rango num_min - num_max. De no encontrarse dentro del rango, hace uso de la 
    función "validar_numero" para que se ingrese por consola otro número y se llama así misma
    para validar que este nuevo dato se encuentre dentro del rango.

    Args:
        numero (int): Número a validar
        num_min (int): Número minimo aceptado
        num_max (int): Número maximo aceptado

    Returns:
        int: Retorna el número validado
    """
    if num_max >= numero >= num_min:
        return numero
    else:
        print(f"Error.El dato ingresado no se encuentra dentro del rango [{num_min} - {num_max}].")
        numero = validar_numero()
        return validar_rango_numerico(numero, num_min, num_max)
    
     
