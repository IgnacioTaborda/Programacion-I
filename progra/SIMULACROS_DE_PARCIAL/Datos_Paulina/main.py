from lista_duracion import lista_duraciones_datos
from lista_nombres import lista_nombres_videos
from lista_views import lista_vistas_videos
from impresiones import menu_principal
from validaciones import (
    validar_numero, validar_rango_numerico
)
from funciones_auxiliares import(
    crear_matriz
)
import os

def programa():
    encendido = True
    while encendido:
        menu_principal()
        opcion = validar_numero()
        opcion = validar_rango_numerico(opcion,1,9)
        
        match opcion:
            case 1:
                largo_lista = len(lista_nombres_videos)
                matriz = crear_matriz(largo_lista,3)
                
            
            case 2:
                pass
            
            case 3:
                pass
            
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
                print("Gracias por usar el program. Hasta luego!")
                encendido = False
        
        os.system('pause')   
        os.system('cls')  
        
programa()        