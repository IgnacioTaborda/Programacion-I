from utn_fra.datasets import (
    matriz_data_heroes,lista_alturas_heroes,lista_poder_heroes,lista_generos_heroes,
    lista_apodos_heroes,lista_identidades_heroes,lista_nombres_heroes
)

def mostrar_menu_principal():
    menu = '''
    1 - Recorrer la matriz imprimiendo por consola el nombre de cada personaje
    2 - Recorrer la matriz imprimiendo por consola el nombre de cada personaje junto a la altura del mismo.
    3 - Recorrer la matriz y mostrar todos los datos del personaje más débil.
    4 - Recorrer la matriz y mostrar todos los datos del personaje más fuerte.
    5 - Recorrer la matriz y determinar la altura promedio de los personajes.
    6 - Recorrer la matriz y determinar LA MITAD DEL PROMEDIO de poder de los personajes.
    7 - Calcular e informar cual es el personaje más y menos alto.
    8 - Determinar el promedio de nivel de poder de todos los personajes e informar qué personaje/s están por encima de ese promedio.
    9 - Calcular e informar la cantidad total de personajes.
    10 - Calcular e informar cuántos personajes son de género Femenino, cuantos Masculino y cuantos No-Binario
    11 - Ordenar los personajes en orden descendente según su poder, luego mostrarlos por consola con su nombre y poder numérico.
    12 - Ordenar los personajes en orden ascendente según su altura. Luego mostrar por consola su nombre y altura numérica. 
    13 - Determinar el promedio de poder de todos los personajes MASCULINOS e informar qué personaje/s FEMENINOS están por encima de ese promedio.
    14 - Determinar el promedio de altura de todos los personajes FEMENINOS e informar qué personaje/s (cualquier género) están por debajo de ese promedio.
    15 - Determinar el promedio de nivel de poder de los personajes No-Binario e informar qué personaje/s (cualquier género) están por encima de ese promedio
    16 - Salir
     
    '''
    print(menu)
    
def imprimir_datos(i : int):
    datos = f'''
    El nombre del personaje es {lista_nombres_heroes[i]}
    La identidad del personaje es {lista_identidades_heroes[i]}
    El apodo del personaje es {lista_apodos_heroes[i]}
    El sexo del personaje es {lista_generos_heroes[i]}
    El poder del personaje es {lista_poder_heroes[i]}
    La altura del personaje es {lista_alturas_heroes[i]}
    '''
    print(datos)
