import os
import pantallas.pantalla_menu as pantalla_menu
import herramientas.validaciones as vali
import herramientas.inputs as inputs
import variables as var
import herramientas.funciones_archivos as archivos_fun
import pantallas.pantalla_ranking as pantalla_ranking
import personaje_base
import combatito
import cartas as card
import pygame as pg

pg.init()
pg.mixer.init()
pg.mixer_music.load(var.MUSICA_DE_FONDO)
pg.mixer.music.play(-1)
pg.mixer.music.set_volume(0.2)


def dragon_ball_tcg():
    encendido = True
    pantalla_actual = "menu"
    personajes = {
        "jugador" : personaje_base.personaje(),
        "enemigos" : personaje_base.personaje()
    }
    
    puntuacion_total = 0
    
    ranking = {
        "puntuacion" : puntuacion_total,
        "activar" : False
    }
    matriz_ranking = archivos_fun.leer_csv(var.CSV)
    
    while encendido:
        match pantalla_actual:
            case "menu":
                pantalla_menu.imprimir_menu()
                opcion = inputs.elegir_opcion(var.MENSAJE_MENU)
                opcion = vali.validar_opcion(opcion,var.OPCIONES_MENU,var.MENSAJE_MENU)
                
                pantalla_actual = pantalla_menu.opciones_menu(opcion)
                
            case "jugar":
                archivo_json = archivos_fun.leer_json(var.JSON)
                hero = card.armar_mazo_aleatorio(archivo_json.get("cantidades"), archivo_json.get("rutas_cartas"))
                villano = card.armar_mazo_aleatorio(archivo_json.get("cantidades"), archivo_json.get("rutas_cartas"))

                juego = combatito.combate(hero,villano)
                
                ranking["puntuacion"] = juego.get("puntuacion_total")
                pantalla_actual = juego.get("pantalla_actual")
                ranking["activar"] = True
                
            case "ranking":
                
                if ranking.get("activar") == True:
                    nombre = inputs.elegir_opcion("Ingrese su nombre: ")
                    matriz_ranking.append([nombre,ranking.get("puntuacion")])
                    archivos_fun.escribir_csv(var.CSV,matriz_ranking)
                    ranking["activar"] = False

                pantalla_ranking.imprimir_ranking(matriz_ranking) 
                opcion = inputs.elegir_opcion("Si desea regresar al menu, escriba 'menu': ")
                opcion = vali.validar_opcion(opcion,["MENU"],"Si desea regresar al menu, escriba 'menu': ")
                  
                
            case "opciones": #INGRESAR PUNTUACION
                print("opciones")
                
            case "salir":
                encendido = False
                print("Adios, Goku!")
                
        
        os.system('pause')
        os.system('cls')
    
dragon_ball_tcg()
        
