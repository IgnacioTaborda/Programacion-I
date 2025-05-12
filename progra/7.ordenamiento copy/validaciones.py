def pedir_numero() -> int:
    """Pide un numero por consola y valida que solo contenga digitos, de lo contrario,
    tira error y se vuelve a llamar así misma hasta que solo se ingresen digitos.

    Returns:
        int: Retorna el numero ingresado y parceado
    """
    numero = input("Ingrese un numero: ")
    if numero.isdigit():
        numero_int = int(numero)
        return numero_int
    else:
        print("Error. Ingrese un número.")
        return pedir_numero()
        
def validar_rango(numero : int, num_min : int, num_max : int) -> int:
    """Valida que el numero ingresado por parametro se encuentre dentro del rango asignado, 
    de lo contrario, la función llama a otra para que se ingrese un nuevo número y se llama
    así misma para validar que el nuevo número se encuentre dentro del rango.

    Args:
        numero (int): Número a validar
        num_min (int): Número minimo
        num_max (int): Número maximo

    Returns:
        int: Retorna el número validado
    """
    if num_max >= numero >= num_min:
        return numero
    else:
        print(f"Error. Ingrese un numero dentro del rango [{num_min} - {num_max}]")
        numero = pedir_numero()
        return validar_rango(numero, num_min, num_max)
        
        
p = validar_rango(5,1,10)
print(p)
