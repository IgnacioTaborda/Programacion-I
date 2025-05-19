import os
from utn_fra.datasets import matriz_data_heroes_small
from impresiones import mostrar_menu_principal, imprimir_datos
from validaciones import validar_numero, validar_rango_numerico


def programa_super_heroes():
    encendido = True
    while encendido:
        mostrar_menu_principal()
        opciones = validar_numero()
        opciones = validar_rango_numerico(opciones,1,16)
        
        match opciones:
            case 1:
                #1.Imprimir nombre
                for i in range(len(matriz_data_heroes_small[0])):
                    print(f"El nombre del personaje numero {i+1} es {matriz_data_heroes_small[0][i]}")
            
            case 2:
                #2.nombre + altura
                for i in range(len(matriz_data_heroes_small[0])):
                    print(f"El nombre del personaje numero {i+1} es {matriz_data_heroes_small[0][i]} y mide {matriz_data_heroes_small[5][i]} cm")
                    
            case 3:
                #3.Personaje más debil
                menor = None
                for i in range(len(matriz_data_heroes_small[0])):
                    if menor == None or menor > matriz_data_heroes_small[4][i]:
                        menor = matriz_data_heroes_small[4][i]
                        indice = i
                
                imprimir_datos(matriz_data_heroes_small,4,indice)
            
            case 4:
                pass
            
            case 5:
                pass
            
            case 6:
                pass
            
            case 7:
                pass
            
            case 8:
                pass
            
            case 9:
                pass
            
            case 10:
                pass
            
            case 11:
                pass
            
            case 12:
                pass
            
            case 13:
                pass
            
            case 14:
                pass
            
            case 15:
                pass
            
            case 16:
                #16.Salir
                print("Gracias por usar el programa! Hasta luego.")
                encendido = False
       
        os.system('pause')      
        os.system('cls')    
        
programa_super_heroes()