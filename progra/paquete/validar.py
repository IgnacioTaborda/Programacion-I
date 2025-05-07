def validar_nombre(nombre: str, mensaje: str) -> str:
    """ 
    Valida que el nombre contenga solamente letras

    Args:
        nombre (str): La palabra a evaluar
        mensaje (str): El texto a mostrar en caso de error

    Returns:
        str: La palabra validada
    """
    while not nombre.isalpha():
        nombre = input(mensaje)
    return nombre
    

def validar_numero(numero_min: int, numero_max: int) -> int:
    """Funcion que pide que se ingrese un número por consola y valida que se encuentre dentro del rango

    Args:
        numero_min (int): Número minimo
        numero_max (int): Número maximo

    Returns:
        int: Retorna el número validado
    """
    numero = input(f"Ingrese un numero [{numero_min} - {numero_max}]: ")
    
    while not numero.isdigit() or (numero_min < int(numero) > numero_max):
        numero = input("Error. Ingrese un numero valido: ")
    edad_int = int(numero)
    return edad_int



def validar_numero_entre(numero:str, min:int, max:int):
    '''
    Valida que el usuario ingrese un numero entre un rango determinado
    min: nnumero minimo (int)
    max: numero maximo (int)
    return: retorna el numero dentro del rango permitdo, parseando a entero 
    '''
    while not numero.isdigit() or (int(numero) < min) or (int(numero) > max):
        numero = input(f"Ingrese un numero valido entre {min} y {max}: ")
    numero_int = int(numero)
    return numero_int

def ingresar_numero_entero() -> int:
    '''
    La funcion le pide al usuario que ingrese un numero entero, y lo retorna.
    '''
    num = input("Ingrese un numero entero: ")
    while not num.isdigit():
        num = input("Ingrese un numero entero: ")
    num_int = int(num)
    return num_int

x = validar_nombre()
print(x)