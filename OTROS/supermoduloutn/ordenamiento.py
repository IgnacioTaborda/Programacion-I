##ASCENDENTE##########################################################################################

def obtener_indice_menor(matriz : list[list], inicio : int, fila : int, indice_menor : int) -> int:
    """Esta función se encarga de obtener el indice del menor valor de la lista de una matriz.

    Args:
        matriz (list[list]): Matriz que contenga la lista
        inicio (int): Indice por el que se comienza a recorrer la lista
        fila (int): Fila a recorrer
        indice_menor (int): Indice con el que se comienza a comparar

    Returns:
        int: Retorna el indice del menor valor
    """
    
    largo_columna = len(matriz[fila])
    for j in range(inicio,largo_columna):
        if matriz[fila][indice_menor] > matriz[fila][j]:
            indice_menor = j
    return indice_menor

def ordenar_fila_matriz_ascendente(matriz : list[list], fila : int):
    """Esta función se encarga de ordenar la fila de una matriz de menor a mayor.
    Hace uso de otra función para encontrar el menor indice. 

    Args:
        matriz (list[list]): Matriz que contenga la lista a ordenar
        fila (int): Fila a ordenar
    """
    largo_columna = len(matriz[fila])
    for i in range(largo_columna):
        indice_menor = i
                
        indice_menor = obtener_indice_menor(matriz,i+1,fila,indice_menor)
                
        if indice_menor != i:
            auxiliar = matriz[fila][i]
            matriz[fila][i] = matriz[fila][indice_menor]
            matriz[fila][indice_menor] = auxiliar
            
##DESCENDENTE##########################################################################################            
            
def obtener_indice_mayor(matriz : list[list], inicio : int, fila : int, indice_mayor : int) -> int:
    """Esta función se encarga de obtener el indice del mayor valor de la lista de una matriz.

    Args:
        matriz (list[list]): Matriz que contenga la lista
        inicio (int): Indice por el que se comienza a recorrer la lista
        fila (int): Fila a recorrer
        indice_menor (int): Indice con el que se comienza a comparar

    Returns:
        int: Retorna el indice del mayor valor
    """
    
    largo_columna = len(matriz[fila])
    for j in range(inicio,largo_columna):
        if matriz[fila][indice_mayor] < matriz[fila][j]:
            indice_mayor = j
    return indice_mayor

def ordenar_fila_matriz_descendente(matriz : list[list], fila : int):
    """Esta función se encarga de ordenar la fila de una matriz de mayor a menor.
    Hace uso de otra función para encontrar el mayor indice. 

    Args:
        matriz (list[list]): Matriz que contenga la lista a ordenar
        fila (int): Fila a ordenar
    """
    largo_columna = len(matriz[fila])
    for i in range(largo_columna):
        indice_mayor = i
                
        indice_mayor = obtener_indice_mayor(matriz,i+1,fila,indice_mayor)
                
        if indice_mayor != i:
            auxiliar = matriz[fila][i]
            matriz[fila][i] = matriz[fila][indice_mayor]
            matriz[fila][indice_mayor] = auxiliar
            
############# CREAR FILA ORDENADA ##########################################################################