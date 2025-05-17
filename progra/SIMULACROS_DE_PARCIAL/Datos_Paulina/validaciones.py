def validar_numero() -> int:
    """Esta función pide que se ingrese un número por consola y valida que solo contenga digitos.
    De ser el caso, se retorna el número parseado a entero, de lo contrario, la función se llama
    así misma.

    Returns:
        int: Retorna el número ingresado por consola en entero
    """
    numero = input("Ingrese un número: ")
    if numero.isdigit():
        numero_int = int(numero)
        return numero_int
    else:
        print("Error!")
        return validar_numero()

def validar_rango_numerico(numero : int, num_min : int, num_max : int) -> int:
    """Esta función se encarga de validar un número ingresado por parametro. Si el número 
    se encuentra dentro del rango requerido, se retorna. De no ser el caso, se hace uso de 
    otra función para que el usuario pueda ingresar un nuevo número por consola y lo valida.

    Args:
        numero (int): Número a validar
        num_min (int): Valor minimo aceptado
        num_max (int): Valor maximo aceptado

    Returns:
        int: Retorna el número validado
    """
    if num_max >= numero >= num_min:
        return numero
    else:
        numero = validar_numero()
        return validar_rango_numerico(numero,num_min,num_max)