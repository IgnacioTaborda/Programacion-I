from utn_fra.datasets import matriz_data_heroes_small,matriz_data_heroes

def buscar_menor_valor(lista : list) -> int: 
    """Esta función se encarga de buscar el menor valor de una lista y
    lo retorna.

    Args:
        lista (list): Lista a evaluar 

    Returns:
        int: Menor valor encontrado
    """
    menor = None
    for i in range(len(lista)):
        if menor == None or menor > lista[i]:
            menor = lista[i]
    return menor

def buscar_mayor_valor(lista : list) -> int:
    """Esta función se encarga de buscar el mayor valor de una lista y
    lo retorna.

    Args:
        lista (list): Lista a evaluar 

    Returns:
        int: Mayor valor encontrado
    """
    mayor = None
    for i in range(len(lista)):
        if mayor == None or mayor < lista[i]:
            mayor = lista[i]
    return mayor

def encontrar_indice_por_valor(lista : list, valor : int) -> list:
    """Esta función recorre una lista, busca el valor ingresado por parametro y 
    devuelve una lista con la/las posicion/posiciones en la/las que se encuentra el valor.
    De no encontrarse el valor en la lista, retorna una lista vacia.

    Args:
        lista (list): Lista a recorrer
        valor (int): Valor a buscar

    Returns:
        list: Lista con la/las posicion/posiciones en la/las que se encuentra el valor | 
        De  no encontrarse el valor en la lista, retorna una lista vacia
    """
    lista_valor = []
    for i in range(len(lista)):
        if lista[i] == valor:
            lista_valor.append(i)
    return lista_valor

def calcular_promedio_lista(lista : list) -> float:
    """Suma todos los elementos de una lista y calcula el promedio

    Args:
        lista (list): Lista a calcular

    Returns:
        float: Promedio de la lista
    """
    largo_lista = len(lista)
    acumulador = 0
    for i in range(largo_lista):
        acumulador += lista[i]
    promedio = acumulador / largo_lista
    promedio = round(promedio,2)
    return promedio 

def convertir_columna_en_fila(matriz : list[list], columna : int) -> list:
    fila = []
    for j in range(len(matriz)):
            fila.append(matriz[j][columna])
    return fila

def crear_matriz_traspuesta(matriz : list[list]):
    matriz_traspuesta = []
    for i in range(len(matriz[0])):
        fila = convertir_columna_en_fila(matriz,i)
        matriz_traspuesta.append(fila)     
    return matriz_traspuesta 


            
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
]

print(crear_matriz_traspuesta(matriz))