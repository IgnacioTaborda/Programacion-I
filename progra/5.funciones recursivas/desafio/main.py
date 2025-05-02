import random
import os
from impresion import menu, impresion_de_opcion
from validaciones import validar_numero_entre, validar_ganador_ronda
from partida import determinar_al_ganador


def programa():
    ejecutando = True
    puntos_jugador = 0
    puntos_maquina = 0
    ronda_actual = 1
    
    
    while ejecutando:
        print(f"La ronda actual es {ronda_actual}")
        menu()
        numero = input("Ingrese una opcion: ")
        opcion_jugador = validar_numero_entre(numero,1,3)
       
       #OPCION JUGADOR EN CONSOLA
        impresion_de_opcion(opcion_jugador,"Jugador")
                
        #OPCION MAQUINA + OPCION MAQUINA EN CONSOLA
        opcion_maquina = random.randint(1, 3)
        impresion_de_opcion(opcion_maquina,"Maquina")
        
        #VERIFICAR GANADOR 
        resultado_de_la_ronda =  validar_ganador_ronda(opcion_jugador, opcion_maquina)
        
        #ASIGNACION DE PUNTOS 
        match resultado_de_la_ronda:
            case "Jugador":
                print("GANO EL JUGADOR")
                puntos_jugador +=1
            case "Maquina":
                puntos_maquina +=1
                print("GANO LA MAQUINA")
            case "Empate":
                print("EMPATE")
        
        #CONTADOR DE RONDAS        
        if resultado_de_la_ronda:
            continue
        else:
            ronda_actual +=1
        
          
        #VERIFICAR GANADOR (INCOMPLETA)
        if ronda_actual == 5:
            resultado_final = determinar_al_ganador(puntos_jugador,puntos_maquina)
            break
        
        print(f"El jugador tiene {puntos_jugador} puntos")
        print(f"La maquina tiene {puntos_maquina} puntos")
            
        os.system('pause')
        os.system('cls')
    return resultado_final
        
    
        
        
x=programa()
print(f"El ganador final es {x}")