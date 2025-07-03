
"Validar el ingreso de una edad que este entre 18 y 98"

edad = None

#Formas de comenzar
#while edad == None
#while edad is None --> Validamos que el tipo de variable sea igual a None
#while not edad --> Mientras no haya nada (None/0) vamos a rellenar la variable con algo

while edad == None or edad > 98 or edad < 18:
#while edad == None or not (18 < edad < 98)
    edad_str = input("Ingrese su edad: ")
    
    if edad_str.isdigit():
        edad = int(edad_str)
    
    #"isdigit()" devuelve un booleano, si es un numero devuelve un True, de lo contrario, un False
    #"isalpha()" evalua que sean solo letras
    #"isalnum()" evalua que sean letras y numeros

    #metodos?
    
    #funciones de una clase?