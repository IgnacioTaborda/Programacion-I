
#Retorna solo un indice
def buscar_en_matriz(matriz : list, indice_donde_buscar : int, valor_a_buscar : str) -> int: #indice_donde_buscar == columna perri
    indice_encontrado = -1 #devolvemos esto por si no encontramos el valor
    indice = 0
    
    while indice < len(matriz[indice_donde_buscar]):
        if matriz[indice_donde_buscar][indice] == valor_a_buscar:
            indice_encontrado = indice
            break
        indice += 1
        
    return indice_encontrado
    #Por ej: querese saber cual garaje tiene un coche de tal valor, matriz = concesionaria, indice_donde_buscar = columna de precio.

def buscar_en_matriz_list(matriz : list, indice_donde_buscar : int, valor_a_buscar : str) -> list:
    lista_indice_encontrado = []
    indice = 0
    
    while indice < len(matriz[indice_donde_buscar]):
        if matriz[indice_donde_buscar][indice] == valor_a_buscar:
            lista_indice_encontrado.append(indice)
            
        indice += 1
        
    return lista_indice_encontrado