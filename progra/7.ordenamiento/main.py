import os
from impresiones import mostrar_menu, obtener_existencias, imprimir_porcentaje_de_unidades
from fuciones_auxiliares import (
    validar_numero, calcular_unidades_almacenadas, garage_con_menor_unidades, garage_con_mas_unidades,
    calcular_gananacias, regla_de_3_simples, total_autos_por_marca
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
                    print("Primero debe obtener la recaudación (Opción 5)")
                else:
                    for i in range(len(lista_autos_cantidades)):
                        obtener_existencias(i)
                    
            case 2:
                #Cantidad total de unidades almacenadas
                total_unidades_almacenadas = calcular_unidades_almacenadas()
                print(f"El total de unidades almacenadas es de {total_unidades_almacenadas}.")
                
            case 3: #PUEDE HABER MAS DE UNO ASI QUE ESTA MALETA.
                #Minima cantidad de unidades almacenadas
                indice = garage_con_menor_unidades()
                obtener_existencias(indice)
                 
            case 4: #PUEDE HABER MAS DE UNO ASI QUE ESTA MALETA
                #Maxima cantidad de unidades almacenadas
                indice = garage_con_mas_unidades()
                obtener_existencias(indice)
                
            case 5:
                #Obtener recaudación
                bloqueo_opcion_1_3_4_6 = True
                lista_autos_ganancias = calcular_gananacias()
                print("La recaudación fue calculada con exito. Si desea tener más detalles sobre la recaudación, seleccione la Opción 1.")
            
            case 6:
                #Garajes con 6 o más unidades almacenadas
                if bloqueo_opcion_1_3_4_6 == False:
                    print("Primero debe obtener la recaudación (Opción 5)")
                else:
                    for j in range(len(lista_autos_cantidades)):
                        if lista_autos_cantidades[j] >= 6:
                            obtener_existencias(j)
                        
            case 7:
                if bloqueo_opcion_1_3_4_6 == False:
                    print("Primero debe obtener la recaudación (Opción 5)")
                else:
                    #A.Porcentajes:
                    total_unidades_almacenadas = calcular_unidades_almacenadas()
                    total_chevrolet = regla_de_3_simples(total_autos_por_marca("Chevrolet"),total_unidades_almacenadas)
                    total_toyota = regla_de_3_simples(total_autos_por_marca("Toyota"),total_unidades_almacenadas)
                    total_fiat = regla_de_3_simples(total_autos_por_marca("Fiat"),total_unidades_almacenadas)
                    total_renault = regla_de_3_simples(total_autos_por_marca("Renault"),total_unidades_almacenadas)
                    total_volkswagen = regla_de_3_simples(total_autos_por_marca("Volkswagen"),total_unidades_almacenadas)
                    total_ford = regla_de_3_simples(total_autos_por_marca("Ford"),total_unidades_almacenadas)
                    total_audi = regla_de_3_simples(total_autos_por_marca("Audi"),total_unidades_almacenadas)
                    total_honda = regla_de_3_simples(total_autos_por_marca("Honda"),total_unidades_almacenadas)
                    total_nissan = regla_de_3_simples(total_autos_por_marca("Nissan"),total_unidades_almacenadas)
                    total_peugeot = regla_de_3_simples(total_autos_por_marca("Peugeot"),total_unidades_almacenadas)

                    imprimir_porcentaje_de_unidades(total_chevrolet, "Chevrolet")
                    imprimir_porcentaje_de_unidades(total_toyota, "Toyota")
                    imprimir_porcentaje_de_unidades(total_fiat, "Fiat")
                    imprimir_porcentaje_de_unidades(total_renault, "Renault")
                    imprimir_porcentaje_de_unidades(total_volkswagen, "Volkswagen")
                    imprimir_porcentaje_de_unidades(total_ford, "Ford")
                    imprimir_porcentaje_de_unidades(total_audi, "Audi")
                    imprimir_porcentaje_de_unidades(total_honda, "Honda")
                    imprimir_porcentaje_de_unidades(total_nissan, "Nissan")
                    imprimir_porcentaje_de_unidades(total_peugeot, "Peugeot")
                    #B.Datos del maximo vehiculos alamacenados
                    #indice = garage_con_mas_unidades()
                    #obtener_existencias(indice)
                pass
            case 8:
                pass
            case 9: 
                print("Se esta cerrando el programa. Hasta la proxima!")
                sistema = False
                
        os.system('pause')
        os.system('cls')
                
programa()