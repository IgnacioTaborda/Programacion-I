from utn_fra.datasets import (
    lista_autos_cantidades, lista_autos_ganancias,
    lista_autos_marcas, lista_autos_modelos, lista_autos_precios)     
    
def total_unidades(lista : list) -> int:
    """Suma todos los elementos de una lista

    Args:
        lista (list): Lista con los elementos que se busca sumar

    Returns:
        int: Retorna el total de la suma de todos los elementos de la lista
    """
    total = 0
    for i in range(len(lista)):
        total += lista[i]
    return total

def menor_unidad(lista : list) -> int:
    """Recorre la lista ingresada por parametro y busca el menor elemento

    Args:
        lista (list): Lista con elementos 

    Returns:
        int: Retorna el menor elemento de la lista
    """
    auxiliar = None
    for i in range(len(lista)):
        if auxiliar == None or auxiliar > lista[i]:
            auxiliar = lista[i]
    return auxiliar

def mayor_unidad(lista : list) -> int:
    """Recorre la lista ingresada por parametro y busca el mayor elemento

    Args:
        lista (list): Lista con elementos 

    Returns:
        int: Retorna el mayor elemento de la lista
    """
    auxiliar = None
    for i in range(len(lista)):
        if auxiliar == None or auxiliar < lista[i]:
            auxiliar = lista[i]
    return auxiliar

def conseguir_indices_por_valor(valor : int, lista : list) -> list:
    """Recorre una lista para para encontrar el indice del/los elementos que tengan el mismo
    valor que se ingreso por parametro.

    Args:
        valor (int): Valor que se busca en la lista
        lista (list): Lista que se va a recorrer

    Returns:
        list: Retorna una lista con los indices que su valor coincida con el valor ingresado por parametro.
        Si no se encontro el valor en la lista, retorna una lista vacia.
    """
    lista_menor = []
    for i in range(len(lista)):
        if valor == lista[i]:
            lista_menor.append(i)
    return lista_menor
   
def obtener_recaudacion(lista_autos_ganancias:list) -> list:
    """Recorre una lista y las ganancias que va sumando las incorpora a la lista

    Args:
        lista_autos_ganancias (list): Lista en la que se almacenan las ganancias

    Returns:
        list: Retorna la lista con las ganancias 
    """
    for i in range(len(lista_autos_ganancias)):
        suma = lista_autos_cantidades[i] * lista_autos_precios[i]   
        lista_autos_ganancias[i] = suma
    return lista_autos_ganancias    

def obtener_garajes_con_6_o_mas(lista_autos_cantidades : list) -> list:
    lista_garajes = []
    for i in range(len(lista_autos_cantidades)):
        if lista_autos_cantidades[i] >= 6:
            lista_garajes.append(i)
    return lista_garajes

def eliminar_elementos_repetidos(lista : list) -> list:
    """Recibe una lista por parametro y elimina los elementos repetidos.

    Args:
        lista_autos_marcas (list): Lista a recorrer

    Returns:
        list: Retorna una lista sin elementos repetidos
    """
    lista_sin_repetidos = []
    
    for i in range(len(lista)):
        if lista[i] not in lista_sin_repetidos:
            lista_sin_repetidos.append(lista[i])
    return lista_sin_repetidos

def crear_una_lista(largo : int, valor = 0) -> list:
    lista = [valor] * largo
    return lista

def regla_de_3_simples(numero: int, total: int):
    resultado = (numero * 100) / total
    return resultado

def ordenar_lista(lista : list) -> list:
    largo_lista = len(lista)
    for i in range(largo_lista-1):
        for j in range(i+1,largo_lista):
            if lista[j] > lista[i]:
                auxiliar = lista[i]
                lista[i] = lista[j]
                lista[j] = auxiliar
    lista_ordenada = lista
    return lista_ordenada

print(ordenar_lista(lista = [6,4,2,1,67,5]))





'''x = menor_unidad(lista_autos_cantidades)
xd = conseguir_indices_por_valor(x,lista_autos_cantidades)
print(xd)'''
            
'''lista = [6,4,2,1,67,1,1]
menor = menor_unidad(lista)
mayor = mayor_unidad(lista)
print(conseguir_indices_por_valor(menor,lista))
print(conseguir_indices_por_valor(mayor,lista))'''