def ordenar_bubble_sort(mi_lista: list) -> list: 
    largo_lista = len(mi_lista)
    for indice in range(largo_lista - 1):
        
            for sub_indice in range(indice + 1,largo_lista): #ORDENAR DE FORMA DESCENDENTE
                
                if mi_lista[indice] < mi_lista[sub_indice]:
                    auxiliar = mi_lista[indice]
                    mi_lista[indice] = mi_lista[sub_indice]
                    mi_lista[sub_indice] = auxiliar
    return mi_lista
                    
def ordenar_selection_sort(mi_lista:list) ->list: #DESCENDENTE
    largo_list = len(mi_lista)
    
    for indice in range(largo_list - 1):
        indice_de_elemento_mayor = indice
        
        for subindice in range(indice + 1, largo_list):
            
            if mi_lista[indice_de_elemento_mayor] < mi_lista[subindice]:
                indice_de_elemento_mayor = subindice
                
        if indice_de_elemento_mayor != subindice:
            auxiliar = mi_lista[indice_de_elemento_mayor]
            mi_lista[indice_de_elemento_mayor] = mi_lista[indice]
            mi_lista[indice] = auxiliar        
    return mi_lista
            
def ordenar_quick_sort(lista:list) -> list:
    
    if len(lista) < 2:
        return lista
    
    pivot = lista.pop() #COMO NO PUSE NADA DENTRO DEL POP, AGARRA EL ULTIMO ELEMENTO
    mas_chico = []
    mas_grande = []
    
    for numero in range(len(lista)):
        if numero < pivot: #BORRE EL IGUAL KIKIKIJIJIKJK
            mas_chico.append(numero)
        else:
            mas_grande.append(numero)

    return ordenar_quick_sort(mas_chico) + [pivot] + ordenar_quick_sort(mas_grande)