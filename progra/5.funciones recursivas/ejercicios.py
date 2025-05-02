def ingresar_numero_entero() -> int:
    '''
    La funcion le pide al usuario que ingrese un numero entero, y lo retorna.
    '''
    num = input("Ingrese un numero entero: ")
    while not num.isdigit():
        num = input("Ingrese un numero entero: ")
    num_int = int(num)
    return num_int

def validar_numero_entre(numero:int, min:int, max:int):
    '''
    Valida que el usuario ingrese un numero entre un rango determinado
    min: nnumero minimo (int)
    max: numero maximo (int)
    return: retorna el numero dentro del rango permitdo, parseando a entero 
    '''
    while (int(numero) < min) or (int(numero) > max):
        numero = input(f"Ingrese un numero valido entre {min} y {max}: ")
    numero_int = int(numero)
    return numero_int

#1.Realizar una función recursiva que calcule la suma de los primeros números naturales
# def sumar_naturales(numero:int) -> int:
#     if numero == 1:
#         resultado = 1
#     else:
#         resultado = numero + sumar_naturales(numero-1)
#     return resultado

# d = ingresar_numero_entero()
# v_d = validar_numero_entre(d,1,10)
# x = sumar_naturales(v_d)
# print(x)

#2.Realizar una función recursiva que calcule la potencia de un número
# def calcular_potencia(base:int, exponente:int) -> int:
#     if exponente == 0:
#         resultado = 1
#     else:
#         resultado = base * calcular_potencia(base, exponente-1)
#     return resultado
        
# d = ingresar_numero_entero()
# v_d = validar_numero_entre(d,1,10)
# x = calcular_potencia(v_d,4)
# print(x)

#3.Realizar una función recursiva que permita realizar la suma de los dígitos de un número:
# def sumar_digitos(numero:int)->int:
#     if numero < 10:
#         resultado = numero
#     else:
#         resultado = sumar_digitos(numero//10) + numero % 10
#     return resultado
    
# d = ingresar_numero_entero()
# x = sumar_digitos(d)
# print(x)

#4.Realizar una función para calcular el número de Fibonacci de un número ingresado por consola. 
def calcular_fibonacci(numero:int)->int:
    if numero == 0 or numero == 1:
        resultado = numero
    else:
        resultado = calcular_fibonacci(numero-1) + calcular_fibonacci(numero-2)
    return resultado
        
d = ingresar_numero_entero()
x = calcular_fibonacci(d)
print(x)