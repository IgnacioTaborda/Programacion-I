def validar_numero_entre(numero:str, min:int, max:int)->int:
    """
    Valida que el usuario ingrese un numero entre un rango determinado
    
    Args:
        numero (str): _description_
        min (int): Número minimo
        max (int): Número maximo

    Returns:
        int: Retorna el numero dentro del rango permitdo, parseando a entero
    """
    while not numero.isdigit() or (int(numero) < min) or (int(numero) > max):
        numero = input(f"Ingrese un numero valido entre {min} y {max}: ")
    numero_int = int(numero)
    return numero_int

def validar_ganador_ronda(opcion_jugador:int,opcion_maquina:int)->str:
    """Determina quien gano la ronda o si hubo empate

    Args:
        opcion_jugador (int): Opcion que eligio el jugador
        opcion_maquina (int): Opcion que eligio la maquina

    Returns:
        str: Retorna el ganador de la ronda
    """
    if opcion_jugador == opcion_maquina:
        resultado = "Empate"
    elif (opcion_jugador == 1 and opcion_maquina == 3) or (opcion_jugador == 2 and opcion_maquina == 1) or (opcion_jugador == 3 and opcion_maquina == 2):
        resultado = "Jugador" 
    else:
        resultado = "Maquina"
    return resultado
