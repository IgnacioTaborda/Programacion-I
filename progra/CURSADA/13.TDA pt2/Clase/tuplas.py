# tuplita = ("hola", "papulince", "gil")

# for i in range(len(tuplita)):
#     print(tuplita[i])

tuplita = ("hola", "papulince", "18")
saludo, apodo, edad = tuplita
# print(saludo)
# print(apodo)
# print(edad)
def agregar_a_tupla(tupla_og : tuple, nuevo_elemento : any) -> tuple:
    if type(nuevo_elemento) != list:    
        nuevo_elemento = [nuevo_elemento]
        
    nueva_tupla = tupla_og + tuple(nuevo_elemento)
    return nueva_tupla