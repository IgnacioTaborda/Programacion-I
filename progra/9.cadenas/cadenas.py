def identificar_palindromo(cadena : str) -> bool:
    
    cadena = cadena.lower()
    cadena_nueva = []
    for i in range(len(cadena)):
        if cadena[i] != " ":
            cadena_nueva.append(cadena[i])
    
    cadena_invertida = cadena_nueva[::-1]
    if cadena_nueva == cadena_invertida:
        return True
    else:
        return False
    
#print(identificar_palindromo("anita lava tina"))

#SPLIT -- Metodo
#corta la cadena con el valor que le pongas entre parentesis
#convierte un string, en una lista de strings.

cadena = "Hola Mundo"
print(id(cadena))
lista_str = cadena.split(" Mundo")
#print(lista_str)
#al sacar mundo, lo entiende como un caracter vacio

#REPLACE -- Metodo
#reemplaza una parte de nuestro string por otra
#(que cosa queremos reemplzar,porque lo queremos reemplzar, cuantas veces)

cadena = cadena.replace("Mundo","Giles")
print(cadena)
print(id(cadena))

#JOIN
