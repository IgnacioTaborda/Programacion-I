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
            case 3: #PUEDE HABER MAS DE UNO ASI QUE ESTA MALETA
                auxiliar = None
                indice = None
                for i in range(len(lista_autos_cantidades)):
                    if auxiliar == None or lista_autos_cantidades[i] < auxiliar:
                        auxiliar = lista_autos_cantidades[i]
                        indice = i
                for j in range(len(lista_autos_ganancias)):
                    if j == indice:
                        mensaje= \
                            f'''
                            Garaje N° {j + 1}
                            Marca: {lista_autos_marcas[j]}
                            Modelo: {lista_autos_modelos[j]}
                            Precio Unit: ${lista_autos_precios[j]}
                            Cantidad: {lista_autos_cantidades[j]}
                            Ganancias: {lista_autos_ganancias[j]}
                            '''
                            
                        print(mensaje) 
            case 4: #PUEDE HABER MAS DE UNO ASI QUE ESTA MALETA
                auxiliar = None
                indice = None
                for i in range(len(lista_autos_cantidades)):
                    if auxiliar == None or lista_autos_cantidades[i] > auxiliar:
                        auxiliar = lista_autos_cantidades[i]
                        indice = i
                for j in range(len(lista_autos_ganancias)):
                    if j == indice:
                        mensaje= \
                            f'''
                            Garaje N° {j + 1}
                            Marca: {lista_autos_marcas[j]}
                            Modelo: {lista_autos_modelos[j]}
                            Precio Unit: ${lista_autos_precios[j]}
                            Cantidad: {lista_autos_cantidades[j]}
                            Ganancias: {lista_autos_ganancias[j]}
                            '''
                            
                        print(mensaje)
            case 5:
                for i in range(len(lista_autos_precios)):
                    resultado = 0
                    resultado = lista_autos_precios[i] * lista_autos_cantidades[i]
                    lista_autos_ganancias[i] = resultado
                print(lista_autos_ganancias)
            case 6:
                for j in range(len(lista_autos_cantidades)):
                    if lista_autos_cantidades[j] >= 6:
                        mensaje= \
                            f'''
                            Garaje N° {j + 1}
                            Marca: {lista_autos_marcas[j]}
                            Modelo: {lista_autos_modelos[j]}
                            Precio Unit: ${lista_autos_precios[j]}
                            Cantidad: {lista_autos_cantidades[j]}
                            Ganancias: {lista_autos_ganancias[j]}
                            '''
                            
                        print(mensaje)
            case 7:
                pass
            case 8:
                pass
            case 9: 
                print("Hasta la proxima!")
                sistema = False
                
        os.system('pause')
        os.system('cls')
                
programa()