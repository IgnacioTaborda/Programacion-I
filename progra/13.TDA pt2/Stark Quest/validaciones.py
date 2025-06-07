def validar_opcion(opcion : str, lista_de_opciones : list) -> str:
    """Esta función recibe un opción y una lista de strings con opciones correctas.
    Si la opción se encuentra dentro de la lista, se retorna, de lo contrario, la 
    función se llama así misma y se pide que se haga un nuevo ingreso hasta que se 
    ingrese una opción valida.

    Args:
        opcion (str): Opción a validar
        lista_de_opciones (list): Lista con opciones validas (Strings en mayúscula)
)
    Returns:
        str: Retorna la opción validada
    """
    opcion = opcion.upper()
    if opcion in lista_de_opciones:
        resultado = opcion
    else:
        rango_lista = [lista_de_opciones[0],lista_de_opciones[-1]]
        opcion = input(f"Error. La opción ingresada debe ser entre [{rango_lista[0]} - {rango_lista[1]}]: ") 
        resultado = validar_opcion(opcion, lista_de_opciones)

    return resultado
