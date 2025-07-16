import os
import pantallas.pantalla_menu as pantalla_menu
import herramientas.validaciones as vali
import herramientas.inputs as inputs
import variables as var
import herramientas.funciones_archivos as archivos_fun
import pantallas.pantalla_ranking as pantalla_ranking
import personaje_base

def dragon_ball_tcg():
    encendido = True
    pantalla_actual = "menu"
    personajes = {
        "jugador" : personaje_base.personaje(),
        "enemigos" : personaje_base.personaje()
    }
    while encendido:
        match pantalla_actual:
            case "menu":
                pantalla_menu.imprimir_menu()
                opcion = inputs.elegir_opcion(var.MENSAJE_MENU)
                opcion = vali.validar_opcion(opcion,var.OPCIONES_MENU,var.MENSAJE_MENU)
                
                pantalla_actual = pantalla_menu.opciones_menu(opcion)
                
            case "jugar":
                print("jugandooo")
                
            case "ranking":
                matriz_ranking = archivos_fun.leer_csv(var.JSON)
                pantalla_ranking.imprimir_ranking(matriz_ranking)   
                
            case "opciones": #INGRESAR PUNTUACION
                print("opciones")
                
            case "salir":
                encendido = False
                print("Adios, Goku!")
                
        
        os.system('pause')
        os.system('cls')
    
dragon_ball_tcg()
        
