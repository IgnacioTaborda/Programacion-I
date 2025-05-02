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
    

def validar_edad(edad:int) -> int:
    """_summary_

    Args:
        edad (str): _description_

    Returns:
        int: Retorna la edad validada
    """
    
    
    '''
    Recibe una edad en formato str, valida que este formada por numeros y que numericamente sea mayor
    o igual a 8. En caso de cumplir, retonr la edad parseada a entero
    '''
    while not edad.isdigit() or (int(edad) < 18):
        edad = input("Ingrese una edad: ")
    edad_int = int(edad)
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