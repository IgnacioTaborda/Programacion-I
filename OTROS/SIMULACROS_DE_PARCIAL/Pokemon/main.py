import os 
from utn_fra.datasets import (
    lista_poke_ids, lista_poke_nombres, lista_poke_tipos, lista_poke_poderes, lista_poke_condiciones
)
from impresiones import imprimir_menu
from validaciones import validar_numero,validar_rango_numerico
from matrices import crear_matriz_de_5_filas,crear_matriz_traspuesta
from calculos import calcular_promedio

def pokedex(lista_poke_ids, lista_poke_nombres, lista_poke_tipos, lista_poke_poderes, lista_poke_condiciones):
    activado = True
    opcion_1 = False
    while activado:
        imprimir_menu()
        opcion = validar_numero()
        opcion = validar_rango_numerico(opcion,1,7)
        
        match opcion:
            case 1:
                #1.Crear matriz
                poke_matriz = crear_matriz_de_5_filas(lista_poke_ids, lista_poke_nombres, lista_poke_tipos, lista_poke_poderes, lista_poke_condiciones)
                print("Pokematriz creda con exito!")
                opcion_1 = True
            
            case 2:
                #2.Recorrer la matriz y mostrar la info con formato: id,nombre,tipo,poder,condición
                if opcion_1 == True:
                    poke_matriz_traspuesta = crear_matriz_traspuesta(poke_matriz) 
                    poke_matriz_traspuesta_largo = len(poke_matriz_traspuesta)
                    for i in range(poke_matriz_traspuesta_largo):
                        print(poke_matriz_traspuesta[i])
            
            case 3:
                #3.Buscar y mostrar la info de los Pokémons que superen el promedio de poder.
                if opcion_1 == True:
                      promedio_poder = calcular_promedio(poke_matriz,3)
                      print(f"El poder promedio es de: {promedio_poder}")
                      
            
            case 4:
                if opcion_1 == True:
                    pass
            
            case 5:
                if opcion_1 == True:
                    pass
            
            case 6:
                if opcion_1 == True:
                    pass
            
            case 7:
                activado = False
                print("Gracias por usar esta pokedex. Hasta luego!")
                
        if opcion_1 == False:
            mensaje = "Para ejecutar las opciones 2 al 6 es necesario que se ejecute la opción 1 primero"
            print(mensaje)
            
        os.system('pause')
        os.system('cls')
                
pokedex(lista_poke_ids, lista_poke_nombres, lista_poke_tipos, lista_poke_poderes, lista_poke_condiciones)