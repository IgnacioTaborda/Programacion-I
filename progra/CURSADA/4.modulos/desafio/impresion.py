def menu():
    """
    Esta funcion sirve para mostrar por consola 3 opciones (Piedra, Papel, Tijera) 
    """
    print(
        '''
            1 - Piedra
            2 - Papel
            3 - Tijera
        '''
    )

def impresion_de_opcion(opcion:int,usuario_o_maquina:str):
    """
    Esta funcion sirve para mostrar por consola la opcion que eligieron y quien fue

    Args:
        opcion (int): El numero de opcion elegida
        usuario_o_maquina (str): Quien eligio el número
    """
    match opcion:
            case 1:
                print(f"El {usuario_o_maquina} selecciono PIEDRA")
            case 2:
                print(f"El {usuario_o_maquina} selecciono PAPEL")
            case 3:
                print(f"El {usuario_o_maquina} selecciono TIJERA")
                
