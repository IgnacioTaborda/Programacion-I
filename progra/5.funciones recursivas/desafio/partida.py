def determinar_al_ganador(puntos_jugador:int, puntos_maquina:int):
    """Resultado final del juego, determina quien gano, muestra al ganador por cuantos puntos

    Args:
        puntos_jugador (int): Puntos del jugador
        puntos_maquina (int): Puntos de la maquina

    Returns:
        _type_: _description_
    """
    if puntos_jugador > puntos_maquina:
        ganador = "Jugador"
    else:
        ganador = "Maquina"
    return ganador