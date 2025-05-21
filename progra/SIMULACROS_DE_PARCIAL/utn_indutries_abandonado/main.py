import os
from utn_fra.datasets import matriz_data_heroes,lista_alturas_heroes,lista_poder_heroes,lista_alturas_heroes,lista_generos_heroes
from impresiones import mostrar_menu_principal, imprimir_datos
from validaciones import validar_numero, validar_rango_numerico
from funciones_auxiliares import (
    buscar_mayor_valor, buscar_menor_valor,encontrar_indice_por_valor,calcular_promedio_lista,crear_matriz_traspuesta
)


def programa_super_heroes():
    encendido = True
    verificador_10 = False
    while encendido:
        mostrar_menu_principal()
        opciones = validar_numero()
        opciones = validar_rango_numerico(opciones,1,16)
        cant_filas = len(matriz_data_heroes)
        cant_columnas = len(matriz_data_heroes[0])
        matriz_traspuesta = crear_matriz_traspuesta(matriz_data_heroes)
        
        match opciones:
            case 1:
                #1.Imprimir nombre
                for i in range(cant_columnas):
                    print(f"El nombre del personaje numero {i+1} es {matriz_data_heroes[0][i]}")
            
            case 2:
                #2.nombre + altura
                for i in range(cant_columnas):
                    print(f"El nombre del personaje numero {i+1} es {matriz_data_heroes[0][i]} y mide {matriz_data_heroes[5][i]} cm")
                    
            case 3:
                #3.Personaje más debil
                menor_poder = buscar_menor_valor(matriz_data_heroes[4])
                lista_menores = encontrar_indice_por_valor(matriz_data_heroes[4],menor_poder)
                
                for i in range(len(lista_menores)):
                    imprimir_datos(lista_menores[i])  
                
            case 4:
                #4.Personaje más fuerte
                mayor_poder = buscar_mayor_valor(matriz_data_heroes[4])
                lista_mayor = encontrar_indice_por_valor(matriz_data_heroes[4],mayor_poder)
                
                for i in range(len(lista_mayor)):
                    imprimir_datos(lista_mayor[i])
            
            case 5:
                #5.Determinar la altura promedio de los personajes
                altura_promedio = calcular_promedio_lista(lista_alturas_heroes)
                print(f"La altura promedio de los personajes es de {altura_promedio}")
            
            case 6:
                #6.Determinar LA MITAD DEL PROMEDIO de poder de los personajes
                poder_promedio = calcular_promedio_lista(lista_poder_heroes)
                mitad_promedio = poder_promedio / 2
                mitad_promedio = round(mitad_promedio,2)
                print(f"La mitad del promedio de poderes es de {mitad_promedio}")
                
            case 7:
                #7.Informar cual es el personaje más y menos alto
                altura_max = buscar_mayor_valor(lista_alturas_heroes)
                altura_min = buscar_menor_valor(lista_alturas_heroes)
                
                print("El/Los personaje/s más alto/s son: ")
                for i in range(len(lista_alturas_heroes)):
                    if lista_alturas_heroes[i] == altura_max:
                        imprimir_datos(i)
                
                print("El/Los personaje/s más bajo/s son: ")    
                for i in range(len(lista_alturas_heroes)):
                    if lista_alturas_heroes[i] == altura_min:
                        imprimir_datos(i)
            
            case 8:
                #8.Determinar el promedio de nivel de poder de todos los personajes e informar qué personaje/s están por encima de ese promedio.
                poder_promedio = calcular_promedio_lista(lista_poder_heroes)
                
                for i in range(cant_columnas):
                    if lista_poder_heroes[i] >= poder_promedio:
                        imprimir_datos(i)
                        
            case 9:
                #9.Cantidad total de personajes
                print(f"Hay {cant_columnas} personajes.")
            
            case 10:
                #10. Calcular e informar cuántos personajes son de género Femenino, cuantos Masculino y cuantos No-Binario
                contador_male = encontrar_indice_por_valor(lista_generos_heroes,'Masculino')
                cantidad_male = len(contador_male)
                contador_female = encontrar_indice_por_valor(lista_generos_heroes,'Femenino')
                cantidad_female = len(contador_female)
                contador_no_bi = encontrar_indice_por_valor(lista_generos_heroes,'No-Binario')
                cantidad_no_bi = len(contador_no_bi)
                
                mensaje = f'''
                -Hay {cantidad_male} personajes Masculinos.
                -Hay {cantidad_female} personajes Femeninos.
                -Hay {cantidad_no_bi} personajes No-Binarios.
                '''
                
                print(mensaje)
                verificador_10 = True
            
            case 11:
                pass
            
            case 12:
                pass
            
            case 13:
                #13.Determinar el promedio de poder de todos los personajes MASCULINOS e informar qué personaje/s FEMENINOS están por encima de ese promedio.
                if verificador_10 == True:
                    promedio_poder_male = 0
                    
                    for i in range(cantidad_male):
                        promedio_poder_male += lista_poder_heroes[contador_male[i]]
                    promedio_poder_male = promedio_poder_male / cantidad_male
                    promedio_poder_male = round(promedio_poder_male,2)
                    
                    for i in range(cantidad_female):
                        if lista_poder_heroes[contador_female[i]] > promedio_poder_male:
                            print(f"{matriz_data_heroes[5][contador_female[i]]} esta por encima de los hombres")
                    
                        
                else:
                    print("Primero se debe ejecutar la opción 10")
            
            case 14:
                if verificador_10 == True:
                    pass
                else:
                    print("Primero se debe ejecutar la opción 10")
            
            case 15:
                if verificador_10 == True:
                    pass
                else:
                    print("Primero se debe ejecutar la opción 10")
            
            case 16:
                #16.Salir
                print("Gracias por usar el programa! Hasta luego.")
                encendido = False
       
        os.system('pause')      
        os.system('cls')    
        
programa_super_heroes()
#print(matriz_data_heroes)