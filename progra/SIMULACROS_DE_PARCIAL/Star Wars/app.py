import os
from utn_fra.datasets import (
    lista_sw_nombres, lista_sw_generos, lista_sw_alturas, lista_sw_pesos
)
from impresiones import imprimir_menu,imprimir_datos_de_personaje
from validaciones import validar_numero, validar_rango_numerico
from matrices import crear_matriz_de_4_filas,trasponer_matriz, parsear_strings_a_int
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
                parsear_altura = parsear_strings_a_int(matriz_star_wars,3)
                promedio_altura = calcular_promedio_matriz(matriz_star_wars,3)
                parsear_peso = parsear_strings_a_int(matriz_star_wars,4)
                promedio_peso = calcular_promedio_matriz(matriz_star_wars,4)
                print(f"La altura promedio es {promedio_altura}")
                print(f"El peso promedio es {promedio_peso}")
                
                #TENES Q PARSEAR
                
            case 3:
                pass
            
            case 4:
                pass
            
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