import os
from impresiones import mostrar_menu, obtener_existencias
from fuciones_auxiliares import (
    total_unidades, menor_unidad, mayor_unidad, conseguir_indices_por_valor, obtener_recaudacion,
    obtener_garages_con_6_o_mas
)
from validaciones import (pedir_numero, validar_rango)
from utn_fra.datasets import (
    lista_autos_cantidades, lista_autos_ganancias,
    lista_autos_marcas, lista_autos_modelos, lista_autos_precios)

def programa():
    encendido = True
    while encendido:
        mostrar_menu()
        opcion = pedir_numero()
        opcion = validar_rango(opcion,1,9)
        
        match opcion:
            case 1:
                #1.Obtener existencias
                for i in range(len(lista_autos_marcas)):
                    obtener_existencias(i)
            case 2:
                #2.Todas las unidades de todos los garages
                todas_las_unidades = total_unidades(lista_autos_cantidades)
                print(f"El total de unidades almacenadas es de: {todas_las_unidades}")
            
            case 3:
                #3.Datos del garage con menos unidades almacenadas
                menor_cant_almacenada = menor_unidad(lista_autos_cantidades)
                lista_menores_garage = conseguir_indices_por_valor(menor_cant_almacenada,lista_autos_cantidades)
                for i in range(len(lista_menores_garage)):
                    obtener_existencias(lista_menores_garage[i])
            
            case 4:
                #4.Datos del garage con más unidades almacenadas
                mayor_cant_almacenada = mayor_unidad(lista_autos_cantidades)
                lista_mayores_garage = conseguir_indices_por_valor(mayor_cant_almacenada,lista_autos_cantidades)
                for i in range(len(lista_mayores_garage)):
                    obtener_existencias(lista_mayores_garage[i])
            
            case 5:
                #5.Obtener recaudación
                obtener_recaudacion(lista_autos_ganancias)
                print("Las recaudaciones se obtuvieron con exito, para visualizarlas, seleccione la opción 1.")
                pass
            
            case 6:
                #6.Garages con 6 o más unidades almacenadas
                garages_con_masigual_6 = obtener_garages_con_6_o_mas(lista_autos_cantidades)
                for i in range(len(garages_con_masigual_6)):
                    obtener_existencias(garages_con_masigual_6[i])
                
            case 7:
                pass
            case 8:
                pass
            case 9: 
                #SALIR
                print("Gracias por usar el programa!")
                encendido = False
        os.system('pause')
        os.system('cls')
        
programa()

