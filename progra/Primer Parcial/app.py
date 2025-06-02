import os
from utn_fra.datasets import (
    lista_bzrp_nombres, lista_bzrp_vistas, lista_bzrp_duracion
)
from impresiones import imprimir_menu, imprimir_datos_matriz, imprimir_datos_matriz_traspuesta
from validaciones import validar_numero, validar_rango_numerico
from matrices import crear_matriz, trasponer_matriz, encontrar_valor, ordenar_fila_matriz_descendente
from calculos import calcular_promedio_matriz

def aplicacion(lista_bzrp_nombres, lista_bzrp_vistas, lista_bzrp_duracion):
    encendido = True
    
    while encendido:
        imprimir_menu()
        opciones = validar_numero()
        opciones = validar_rango_numerico(opciones,1,6)
        
        matriz_bzrp = crear_matriz(lista_bzrp_nombres, lista_bzrp_vistas, lista_bzrp_duracion)
        cant_columnas_matriz_bzrp = len(matriz_bzrp[0])
        
        match opciones:
            case 1:
                #1.Mostrar datos (nombre | vistas | duración) -- Matriz
                if cant_columnas_matriz_bzrp > 0:
                    for columnas in range(cant_columnas_matriz_bzrp):
                        imprimir_datos_matriz(matriz_bzrp, columnas)           
                    
            case 2:
                #2.Mostrar videos que superen el promedio de views y también el promedio de duración
                if cant_columnas_matriz_bzrp > 0:
                    promedio_views = calcular_promedio_matriz(matriz_bzrp,1)
                    promedio_duracion = calcular_promedio_matriz(matriz_bzrp,2)
                    
                    print(f"El promedio de visitas es de: {promedio_views}")
                    print(f"El promedio de duración es de: {promedio_duracion}")
                    
                    print("Los videos que superan el promedio de visitas y el promedio de duración son:")
                    
                    for columnas in range(cant_columnas_matriz_bzrp):
                        if (promedio_duracion < matriz_bzrp[2][columnas]) and (promedio_views < matriz_bzrp[1][columnas]):
                            imprimir_datos_matriz(matriz_bzrp, columnas)  
            
            case 3:
                #3.Ordenar la matriz por views DES de todos los videos
                if cant_columnas_matriz_bzrp > 0:    
                    ordenar_fila_matriz_descendente(matriz_bzrp,1)
                    for columnas in range(cant_columnas_matriz_bzrp):
                            imprimir_datos_matriz(matriz_bzrp, columnas) 
            
            case 4:
                #4.Filtrar en la matriz todos los videos en cuyo nombre haya un numeral y mostrarlo
                if cant_columnas_matriz_bzrp > 0:
                    lista_de_videos_filtrada = encontrar_valor(matriz_bzrp,0,"#")
                    for i in range(len(lista_de_videos_filtrada)):
                        imprimir_datos_matriz(matriz_bzrp,lista_de_videos_filtrada[i])
            
            case 5:
                #5.Mostrar datos (nombre | vistas | duración) -- Matriz Traspuesta 
                if cant_columnas_matriz_bzrp > 0:
                    matriz_bzrp_traspuesta = trasponer_matriz(matriz_bzrp)
                    for i in range(len(matriz_bzrp_traspuesta)):
                        imprimir_datos_matriz_traspuesta(matriz_bzrp_traspuesta,i)
            
            case 6:
                #6.Salir
                encendido = False
                mensaje = "Gracias por usar el programa. Hasta luego!"
                print(mensaje)
        
        if cant_columnas_matriz_bzrp == 0:
            print("No es posible ejecutar esta opción, la matriz esta vacia. Ingrese una matriz con contenido")       
        
        os.system('pause')
        os.system('cls')
    
aplicacion(lista_bzrp_nombres, lista_bzrp_vistas, lista_bzrp_duracion)