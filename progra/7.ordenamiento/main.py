import os
from console_output import mostrar_menu
from fuciones_auxiliares import (
    validar_numero, obtener_existencias, calcular_unidades_almacenadas, garage_con_menor_unidades
)
from utn_fra.datasets import (
    lista_autos_cantidades, lista_autos_ganancias,
    lista_autos_marcas, lista_autos_modelos, lista_autos_precios)

def programa():
    sistema = True
    
    while sistema:
        mostrar_menu()
        opcion = validar_numero(1,9)
        match opcion:
            case 1:
                obtener_existencias()
            case 2:
                total_unidades_almacenadas = calcular_unidades_almacenadas()
                print(f"El total de unidades almacenadas es de {total_unidades_almacenadas}.")
            case 3:
                pass #soy un capo
            case 5:
                pass
            case 6:
                pass
            case 7:
                pass
            case 8:
                pass
            case 9: 
                sistema = False
                
        os.system('pause')
        os.system('cls')
                
programa()