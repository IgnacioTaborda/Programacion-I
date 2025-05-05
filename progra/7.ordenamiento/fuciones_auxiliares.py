from utn_fra.datasets import (
    lista_autos_cantidades, lista_autos_ganancias,
    lista_autos_marcas, lista_autos_modelos, lista_autos_precios)
    
def obtener_existencias():
    for indice in range(len(lista_autos_ganancias)):
        
        mensaje= \
            f'''
            Garaje N° {indice + 1}
            Marca: {lista_autos_marcas[indice]}
            Modelo: {lista_autos_modelos[indice]}
            Precio Unit: ${lista_autos_precios[indice]}
            Cantidad: {lista_autos_cantidades[indice]}
            Ganancias: {lista_autos_ganancias[indice]}
            '''
            
        print(mensaje)        
    
def validar_numero(numero_min: int, numero_max: int) -> int:
    numero = input(f"Ingrese un numero [{numero_min} - {numero_max}]: ")
    
    while not numero.isdigit() or (numero_min < int(numero) > numero_max):
        numero = input("Error. Ingrese un numero valido: ")
    edad_int = int(numero)
    return edad_int

def calcular_unidades_almacenadas():
    total = 0
    for i in range(len(lista_autos_cantidades)):
        total += lista_autos_cantidades[i]
    return total

def garage_con_menor_unidades() -> int:
    menor = None
    garage_menor = None
    for i in range(len(lista_autos_cantidades)):
        if (menor > lista_autos_cantidades[i]) or menor == None:
            menor = lista_autos_cantidades[i]
            garage_menor = i
    return garage_menor