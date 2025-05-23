def imprimir_menu():
    """Imprime por consola un menu de 7 opciones
    """
    menu = '''
    1 - Crear Matriz: para ello deberá crear una función que en base a las listas, cree una matriz con los datos para trabajar.
    2 - Recorrer la matriz y mostrar la info con formato: id,nombre,tipo,poder,condición.
    3 - Buscar y mostrar la info de los Pokémons que superen el promedio de poder.
    4 - Ordenar la matriz por poder DES de los Pokémons que sean legendarios.
    5 - Filtrar/buscar en la matriz todos los Pokémons cuyo tipo sea fuego y mostrarlos.
    6 - Trasponer la matriz y mostrar su información prolija.
    7 - Salir
    '''
    print(menu)
    
def imprimir_informacion(lista : list):
    informacion = f'''
    -Poke ID: {lista[0]}
    -Nombre: {lista[1]}
    -Tipo: {lista[2]}
    -Poder: {lista[3]}
    -Condición: {lista[4]}
    ''' 