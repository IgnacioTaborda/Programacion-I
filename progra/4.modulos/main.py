from console_output import *
from paquete.validar import * #TIRA ERROR PQ MAIN NO ESTA EN EL MISMO NIVEL QUE PAQUETE
import os

def aplicacion():
    ejecutando = True
    
    while ejecutando:
        mostrar_menu()
        numero = input("Ingrese una opcion: ")
        opcion = validar_numero_entre(numero,1,4)
        
        match opcion:
            case 1:
                pass
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
        os.system('pause')
        os.system('cls')
        
aplicacion()