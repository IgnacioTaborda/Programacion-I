import os
from impresiones import mostrar_menu, obtener_existencias, imprimir_porcentaje_de_unidades, bloqueador
from fuciones_auxiliares import (
    validar_numero, calcular_unidades_almacenadas, garage_con_menor_unidades, garage_con_mas_unidades,
    calcular_gananacias, regla_de_3_simples, total_autos_por_marca, eliminar_elementos_repetidos_lista
)
from utn_fra.datasets import (
    lista_autos_cantidades, lista_autos_ganancias,
    lista_autos_marcas, lista_autos_modelos, lista_autos_precios)

def programa():
    sistema = True
    bloqueo_opcion_1_3_4_6 = False
    
    while sistema:
        mostrar_menu()
        opcion = validar_numero(1,9)
        match opcion:
            
            case 1: 
                #Obtener existencias
                if bloqueo_opcion_1_3_4_6 == False:
                    bloqueador("ejecutar la opción 5")
                else:
                    for i in range(len(lista_autos_cantidades)):
                        obtener_existencias(i)
                    
            case 2:
                #Cantidad total de unidades almacenadas
                total_unidades_almacenadas = calcular_unidades_almacenadas(lista_autos_cantidades)
                print(f"El total de unidades almacenadas es de {total_unidades_almacenadas}.")
                
            case 3: #PUEDE HABER MAS DE UNO ASI QUE ESTA MALETA.
                #Minima cantidad de unidades almacenadas
                indice = garage_con_menor_unidades(lista_autos_cantidades)
                obtener_existencias(indice)
                 
            case 4: #PUEDE HABER MAS DE UNO ASI QUE ESTA MALETA
                #Maxima cantidad de unidades almacenadas
                indice = garage_con_mas_unidades(lista_autos_cantidades)
                obtener_existencias(indice)
                
            case 5:
                #Obtener recaudación
                bloqueo_opcion_1_3_4_6 = True
                lista_autos_ganancias = calcular_gananacias()
                print("La recaudación fue calculada con exito. Si desea tener más detalles sobre la recaudación, seleccione la Opción 1.")
            
            case 6:
                #Garajes con 6 o más unidades almacenadas
                if bloqueo_opcion_1_3_4_6 == False:
                    bloqueador("ejecutar la opción 5")
                else:
                    for j in range(len(lista_autos_cantidades)):
                        if lista_autos_cantidades[j] >= 6:
                            obtener_existencias(j)
                        
            case 7:
                if bloqueo_opcion_1_3_4_6 == False:
                    bloqueador("ejecutar la opción 5")
                else:
                    #A.Porcentajes:
                    total_unidades_almacenadas = calcular_unidades_almacenadas(lista_autos_cantidades)
                    lista_sin_repetidos = eliminar_elementos_repetidos_lista(lista_autos_marcas)
                    lista_totales_por_marca = [0]
                    for i in range(len(lista_sin_repetidos)):
                        for j in range(len(lista_autos_marcas)):
                            if lista_sin_repetidos[i] == lista_autos_marcas[j]:
                                #lista_totales_por_marca.append(0)
                                lista_totales_por_marca[i] += lista_autos_cantidades[j]
                                lista_totales_por_marca.append(0)
                    print(f"Chevrolet tiene {lista_totales_por_marca[0]}")
                    print(f"Toyota tiene {lista_totales_por_marca[1]}")
                    print(f"Fiat tiene {lista_totales_por_marca[2]}")
                    print(f"Renault tiene {lista_totales_por_marca[3]}")
                    print(f"Volkswagen tiene {lista_totales_por_marca[4]}")
                    print(f"Ford tiene {lista_totales_por_marca[5]}")
                    print(f"Audi tiene {lista_totales_por_marca[6]}")
                    print(f"Honda tiene {lista_totales_por_marca[7]}")
                    print(f"Nissan tiene {lista_totales_por_marca[8]}")
                    print(f"Peugeot tiene {lista_totales_por_marca[9]}")
                    #indice = garage_con_mas_unidades()
                    #obtener_existencias(indice)
                pass
            case 8:
                lista_autos_ganancias_ordenada = []
                for i in range(len(lista_autos_ganancias-1)):
                    for j in range(len(i+1,lista_autos_ganancias)):
                        auxiliar = lista_autos_ganancias[i]
                    
            case 9: 
                print("Se esta cerrando el programa. Hasta la proxima!")
                sistema = False
                
        os.system('pause')
        os.system('cls')
                
programa() #