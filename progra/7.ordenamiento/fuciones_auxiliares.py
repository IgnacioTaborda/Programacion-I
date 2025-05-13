from utn_fra.datasets import (
    lista_autos_cantidades, lista_autos_ganancias,
    lista_autos_marcas, lista_autos_modelos, lista_autos_precios)     
    
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
    numero_int = int(numero)
    return numero_int

def calcular_unidades_almacenadas(lista_unidades)->int:
    """Suma todas las unidades almacenadas de todos los garages

    Returns:
        int: Retorna la suma de todas las unidades
    """
    total = 0
    for i in range(len(lista_unidades)):
        total += lista_unidades[i]
    return total

def garage_con_menor_unidades(lista_menor_unidades:list) -> int:
    """Verifica cual es el garage con menor unidades almacenadas

    Returns:
        int: Devuelve el garage que tiene menos unidades
    """
    auxiliar = None
    indice = None
    for i in range(len(lista_menor_unidades)):
        if auxiliar == None or lista_menor_unidades[i] < auxiliar:
            auxiliar = lista_menor_unidades[i]
            indice = i
    return indice

def garage_con_mas_unidades(lista_mayor_unidades:list) -> int:
    """Verifica cual es el garage con mayor unidades almacenadas

    Returns:
        int: Devuelve el garage que tiene más unidades#
    """
    auxiliar = None
    indice = None
    for i in range(len(lista_mayor_unidades)):
        if auxiliar == None or lista_mayor_unidades[i] > auxiliar:
            auxiliar = lista_mayor_unidades[i]
            indice = i
    return indice

def calcular_gananacias() -> list:
    """Calcula la ganancia de cada garage

    Returns:
        list: Retorna una lista con la ganancia de todos los garages
    """
    for i in range(len(lista_autos_precios)):
        resultado = 0
        resultado = lista_autos_precios[i] * lista_autos_cantidades[i]
        lista_autos_ganancias[i] = resultado
    return lista_autos_ganancias

def regla_de_3_simples(numero: int, total: int):
    resultado = (numero * 100) / total
    return resultado

def total_autos_por_marca(marca: str):
    resultado = 0
    for i in range(len(lista_autos_marcas)):
        if lista_autos_marcas[i] == marca:
            resultado += lista_autos_cantidades[i]
    return resultado

def eliminar_elementos_repetidos_lista(lista)->list:
    largo_lista = len(lista)
    for i in range(largo_lista-1):
        for j in range(i+1,largo_lista):
            if lista[i] == lista[j]:
                lista[j] = None
                           
    lista_sin_repetidos = []
    for k in range(largo_lista):
        if lista[k] != None:
            lista_sin_repetidos.append(lista[k])
    return lista_sin_repetidos
