def imprimir_menu() -> None:
    menu = ''' 
    A - Imprimir el nombre de cada personaje de género Masculino
    B - Imprimir el nombre de cada personaje de género Femenino
    C - Determinar cuál es el personaje más alto de raza “Human”
    D - Determinar cuál es el personaje más alto de raza “Desconocido”
    E- Determinar cuál es el personaje más bajo  de raza “Symbiote”
    F - Determinar cuál es el personaje más bajo  de raza “Mutant”
    G - Determinar la altura promedio de los  personajes de empresa “DC Comics”
    H - Determinar la altura promedio de los  personajes de empresa “Marvel Comics”
    I - Informar cual es el Nombre del personaje asociado a cada uno de los indicadores 
        anteriores (ítems C a F)
    J - Determinar cuántos personajes tienen cada tipo de color de ojos.
    K - Determinar cuántos personajes tienen cada tipo de color de pelo.
    L - Determinar cuántos personajes tienen cada tipo de alineación (En caso de no tener 
        ningún tipo de alineación [o tener un string vacío], Inicializarlo con ‘No Tiene’). 
    M - Listar todos los personajes agrupados por color de ojos.
    N - Listar todos los personajes agrupados por color de pelo.
    O - Listar todos los personajes agrupados por empresa
    P - MUCHO TEXTO
    Q - Salir
    '''
    print(menu)

def imprimr_nombre_genero(diccionario : dict, nombre : str, genero : str) -> None:
    """Imprime por consola el nombre y el genero de un personaje

    Args:
        diccionario (dict): Diccionario que tenga los nombres y generos
        nombre (str): Key que almacene el nombre del personaje
        genero (str): Key que almacene el genero del personaje
    """
    gracia = diccionario[nombre]
    sexo = diccionario[genero]
    mensaje = f"El personaje {gracia} es {sexo}"
    print(mensaje)