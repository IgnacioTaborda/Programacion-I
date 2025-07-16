import variables as var

def imprimir_menu():
    menu = '''
    ################################################
    #                                              # 
    #                DRAGON BALL Z TCG             # 
    #                                              # 
    #                    -Jugar-                   # 
    #                    -Ranking-                 # 
    #                    -Opciones-                #     
    #                    -Salir-                   # 
    #                                              # 
    ################################################
    '''
    print(menu)
    
def opciones_menu(opcion : str):
    match opcion:
        case "JUGAR":
            pantalla_actual = "jugar"
        case "RANKING":
            pantalla_actual = "ranking"
        case "OPCIONES":
            pantalla_actual = "opciones"
        case "SALIR":
            pantalla_actual = "salir"
            
    return pantalla_actual