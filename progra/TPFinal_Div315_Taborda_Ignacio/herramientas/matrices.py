def ordenar_matriz_descendente_mejorada(matriz : list[list], columna : int):
    largo_matriz = len(matriz)

    for i in range(largo_matriz - 1):
        indice_elemento_mayor = i

        for j in range(i+1, largo_matriz):
            if matriz[indice_elemento_mayor][columna] < matriz[j][columna]:
                indice_elemento_mayor = j

        if indice_elemento_mayor != i:
            aux = matriz[i]
            matriz[i] = matriz[indice_elemento_mayor]
            matriz[indice_elemento_mayor] = aux
    return matriz