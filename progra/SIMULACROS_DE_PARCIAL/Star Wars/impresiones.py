def imprimir_menu():
    menu = '''
    1 - Mostrar Datos: Recorrer la matriz y mostrar la info con formato: nombre,género,altura,peso.
    2 - Buscar Datos: Buscar y mostrar la info de los personajes que no superen el promedio de altura ni de peso.
    3 - Ordenar Datos: Ordenar la matriz por peso ASC de todos los personajes.
    4 - Filtrar Datos: Filtrar/buscar en la matriz todos los personajes cuyo género sea “n/a” y mostrar toda su información.
    5 - Trasponer Datos: Trasponer la matriz y mostrar su información prolija.
    6 - Salir.
    '''
    print(menu)
    
def imprimir_datos_de_personaje(matriz : list[list], columna : int):
    """Imprime una columna que contenga los datos de un personaje

    Args:
        matriz (list[list]): Matriz que contenga la información
        de los personajes
        columna (int): Columna con los datos del personaje
    """
    datos = f'''
    -Nombre: {matriz[0][columna]}
    -Genero: {matriz[1][columna]}
    -Altura (cm): {matriz[2][columna]}
    -Peso (kg): {matriz[3][columna]}
    '''
    print(datos) 
    
    

lista = ['172', '167', '96', '202', '150', '178', '165', '97', '183', '182','z']



