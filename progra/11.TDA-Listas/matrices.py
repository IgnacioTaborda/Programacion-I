import copy
lista = [[1, 2, 5, 7, 3],[1, 2, 5, 7, 3]]
lista_copia_pete = lista
lista_copia = copy.copy(lista)


lista_copia[0] = 7777

print(lista)
print(id(lista))
print(lista_copia_pete)
print(id(lista_copia_pete))
print(lista_copia)
print(id(lista_copia))