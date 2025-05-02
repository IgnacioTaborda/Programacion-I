def ordenar_bubble_sort(mi_lista: list) -> list: 
    
    largo_lista = len(mi_lista)
    for indice in range(largo_lista) - 1:
        
            for sub_indice in range(indice + 1,largo_lista): #ORDENAR DE FORMA DESCENDENTE
                
                if mi_lista[indice] < mi_lista[sub_indice]:
                    auxiliar = mi_lista[indice]
                    mi_lista[indice] = mi_lista[sub_indice]
                    mi_lista[sub_indice] = auxiliar
                    
def ordenar_selection_sort(mi_lista:list) ->list:
    largo_list = len(mi_lista)
    for indice in range(largo_list - 1):
        indice_de_elemento_mayor = indice
        for subindice in range(indice + 1, largo_list):
            if mi_lista[indice_de_elemento_mayor] < mi_lista[subindice]:
                indice_de_elemento_mayor = mi_lista[subindice]