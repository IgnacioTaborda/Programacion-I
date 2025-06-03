import copy
####### SHALLOWCOPY #######
# lista = [[1, 2, 5, 7, 3],[1, 2, 5, 7, 3]]
# lista_copia = copy.copy(lista)


# lista_copia[0] = [7777]

# print(lista)
# print(id(lista[0]))
# print(lista_copia)
# print(id(lista_copia[0]))

####### DEEPCOPY #######

lista = [[1, 2, 5, 7, 3],[1, 2, 5, 7, 3]]
lista_copia = copy.deepcopy(lista)


lista_copia[0][0] = 7777

print(lista)
print(id(lista[0]))
print(lista_copia)
print(id(lista_copia[0]))