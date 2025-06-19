def parsear_int(matriz : list[list], fila : int):
    """Esta función sirve para convertir strings, que solo contengan digitos,
    en números enteros.

    Args:
        lista (list): Lista a convertir

    Returns:
        list: Retorna la lista con los números parseados
    """
    largo_columnas = len(matriz[0])
        
    for i in range(largo_columnas):
        elemento = matriz[fila][i]
        if elemento.isdigit():
            elemento = int(elemento)
        matriz[fila][i] = elemento
        
################################################################### #       
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
