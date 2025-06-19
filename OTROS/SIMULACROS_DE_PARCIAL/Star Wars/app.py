import os
from utn_fra.datasets import (
    lista_sw_nombres, lista_sw_generos, lista_sw_alturas, lista_sw_pesos 
)
from impresiones import imprimir_menu,imprimir_datos_de_personaje
from validaciones import validar_numero, validar_rango_numerico
from matrices import crear_matriz_de_4_filas,trasponer_matriz, parsear_int,selection_sort_ascendente
from calculos import calcular_promedio_matriz

def aplicacion(lista_sw_nombres, lista_sw_generos, lista_sw_alturas, lista_sw_pesos):
    encendido = True
    
    while encendido:
        imprimir_menu()
        matriz_star_wars = crear_matriz_de_4_filas(lista_sw_nombres, lista_sw_generos, lista_sw_alturas, lista_sw_pesos)
        cant_columnas_matriz = len(matriz_star_wars[0])
        cant_filas_matriz = len(matriz_star_wars)
        opciones = validar_numero()
        opciones = validar_rango_numerico(opciones,1,6)
        
        match opciones:
            case 1:
                #1.Mostrar datos
                for i in range(cant_columnas_matriz):
                    imprimir_datos_de_personaje(matriz_star_wars,i)
            
            case 2:
                #2.Mostrar personajes que no superen el promedio de altura ni de peso
                parsear_altura = parsear_int(matriz_star_wars,2)
                promedio_altura = calcular_promedio_matriz(matriz_star_wars,2)
                parsear_peso = parsear_int(matriz_star_wars,3)
                promedio_peso = calcular_promedio_matriz(matriz_star_wars,3)
                
                
                for i in range(cant_columnas_matriz):
                    if (matriz_star_wars[2][i] <= promedio_altura) and (matriz_star_wars[3][i] <= promedio_peso):
                        imprimir_datos_de_personaje(matriz_star_wars,i)
                
            case 3:
                #3.Ordenar matriz por peso (ASC)
                d = selection_sort_ascendente(matriz_star_wars,3)
                print(matriz_star_wars[3])
                                
            
            case 4:
                #4.Mostrar personajes N/A
                for i in range(cant_columnas_matriz):
                    if matriz_star_wars[1][i] == "n/a":
                        imprimir_datos_de_personaje(matriz_star_wars,i)
            
            case 5:
                #5.Trasponer datos
                matriz_star_wars_traspuesta = trasponer_matriz(matriz_star_wars)
                print(matriz_star_wars_traspuesta)
            
            case 6:
                encendido = False
                print("Gracias por usar el programa. Que la fuerza te acompañe!")
        
        os.system('pause')
        os.system('cls')
        
        
aplicacion(lista_sw_nombres, lista_sw_generos, lista_sw_alturas, lista_sw_pesos)