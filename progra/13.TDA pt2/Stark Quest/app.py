import os
from utn_fra.datasets import lista_diccionario_heroes_small
from diccionario_heroes import lista_heroes
from impresiones import imprimir_menu, imprimr_nombre_genero
from validaciones import validar_opcion
from diccionario import es_dato, calcular_max_raza, calcular_min_raza, calcular_promedio_valor


def stark_quest(diccionario_heroes : dict):
    encendido = True

    while encendido:
        imprimir_menu()
        lista_de_opciones = [
        'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q'
        ]
        opciones = input("Ingrese una opción [A - Q]: ")
        opciones = validar_opcion(opciones, lista_de_opciones)

        largo_diccionario = len(diccionario_heroes)

        match opciones:
            case 'A':
                #A.Imprimir el nombre de cada personaje de género Masculino
                for i in range(largo_diccionario):
                    es_masculino = es_dato(diccionario_heroes[i],'genero','Masculino')
                    if es_masculino == True:
                        imprimr_nombre_genero(diccionario_heroes[i],'nombre','genero')

            case 'B':
                #B.Imprimir el nombre de cada personaje de género Femenino
                for i in range(largo_diccionario):
                    es_femenino = es_dato(diccionario_heroes[i],'genero','Femenino')
                    if es_femenino == True:
                        imprimr_nombre_genero(diccionario_heroes[i],'nombre','genero')

            case 'C':
                #C.Determinar cuál es el personaje más alto de raza “Human”
                diccionario_max_human = calcular_max_raza(diccionario_heroes,'altura_mts','raza', 'Human')
                diccionario_max_human = diccionario_heroes[diccionario_max_human]
                        
                mensaje = f"El Heroe, de la raza humana, más alto es {diccionario_max_human['nombre']}, midiendo {diccionario_max_human['altura_mts']}."
                print(mensaje)

            case 'D': 
                #D.Determinar cuál es el personaje más alto de raza “Desconocido”
                diccionario_max_desconocido = calcular_max_raza(diccionario_heroes,'altura_mts','raza', 'Desconocido')
                diccionario_max_desconocido = diccionario_heroes[diccionario_max_desconocido]
                        
                mensaje = f"El Heroe, de raza desconocida, más alto es {diccionario_max_desconocido['nombre']}, midiendo {diccionario_max_desconocido['altura_mts']}."
                print(mensaje)

            case 'E':
                #E.Determinar cuál es el personaje más bajo  de raza “Symbiote” 
                diccionario_min_desconocido = calcular_min_raza(diccionario_heroes,'altura_mts','raza', 'Symbiote')
                diccionario_min_desconocido = diccionario_heroes[diccionario_min_desconocido]
                        
                mensaje = f"El Heroe, de raza Symbiote, más bajo es {diccionario_min_desconocido['nombre']}, midiendo {diccionario_min_desconocido['altura_mts']}."
                print(mensaje)

            case 'F':
                #F.Determinar cuál es el personaje más bajo  de raza “Mutant”
                diccionario_min_desconocido = calcular_min_raza(diccionario_heroes,'altura_mts','raza', 'Mutant')
                diccionario_min_desconocido = diccionario_heroes[diccionario_min_desconocido]
                        
                mensaje = f"El Heroe, de raza Mutant, más bajo es {diccionario_min_desconocido['nombre']}, midiendo {diccionario_min_desconocido['altura_mts']}."
                print(mensaje)

            case 'G':
                #G.Determinar la altura promedio de los  personajes de empresa “DC Comics”
                diccionario_dc_comic = []
                for i in range(largo_diccionario):
                    empresa = es_dato(diccionario_heroes[i],'empresa',"DC Comics")
                    if empresa == True:
                        diccionario_dc_comic.append(diccionario_heroes[i])
                      
                promedio = calcular_promedio_valor(diccionario_dc_comic,"altura_mts")
                mensaje = f"La altura promedio de los personajes de DC Comics es de {promedio} mts."
                print(mensaje)

            case 'H':
                #H.Determinar la altura promedio de los  personajes de empresa “Marvel Comics”
                diccionario_marvel_comic = []
                for i in range(largo_diccionario):
                    empresa = es_dato(diccionario_heroes[i],'empresa',"Marvel Comics")
                    if empresa == True:
                        diccionario_marvel_comic.append(diccionario_heroes[i])
                      
                promedio = calcular_promedio_valor(diccionario_marvel_comic,"altura_mts")
                mensaje = f"La altura promedio de los personajes de Marvel Comics es de {promedio} mts."
                print(mensaje)

            case 'I':
                #I.Informar cual es el Nombre del personaje asociado a cada uno de los indicadores 
                #anteriores (ítems C a F)
                pass

            case 'J':
                #J.Determinar cuántos personajes tienen cada tipo de color de ojos.
                lista_tipos = []
                for i in range(largo_diccionario):
                    diccionario = diccionario_heroes[i]
                    colores = diccionario["color_pelo"]
                    
                
            case 'K':
                #K.Determinar cuántos personajes tienen cada tipo de color de pelo.
                for i in range(largo_diccionario):
                    diccionario = diccionario_heroes[i]
                    colores = diccionario["color_pelo"]
                    diccionario_peluquin = {
                        'No Hair' : 0, 
                        'Black' : 0, 
                        'Blond' : 0, 
                        'Brown' : 0, 
                        '-' : 0, 
                        'White' : 0, 
                        'Purple' : 0, 
                        'Orange' : 0
                        
                    }
                    
                    match colores:
                        case "No Hair":
                            diccionario_peluquin['No Hair'] += 1
                        case "Black":
                            diccionario_peluquin['Black'] += 1
                        case "Blond":
                            diccionario_peluquin['Blond'] += 1
                        case "Brown":
                            diccionario_peluquin['Brown'] += 1
                        case "White":
                            diccionario_peluquin['White'] += 1
                        case "Purple":
                            diccionario_peluquin['Purple'] += 1
                        case "Orange":
                            diccionario_peluquin['Orange'] += 1
                        case "-":
                            diccionario_peluquin['-'] += 1

                

            case 'L':
                #Determinar cuántos personajes tienen cada tipo de alineación (En caso de no tener 
                #ningún tipo de alineación [o tener un string vacío], Inicializarlo con ‘No Tiene’)
                pass

            case 'M':
                #M.Listar todos los personajes agrupados por color de ojos.
                pass

            case 'N':
                #N.Listar todos los personajes agrupados por color de pelo.S
                pass

            case 'O':
                #O.Listar todos los personajes agrupados por empresa
                pass

            case 'P':
                #P.MUCHO TEXTO
                pass

            case 'Q':
                #Q.Salir
                encendido = False
                print("Gracias por usar el programa! Hasta luego.")

        os.system('pause')
        os.system('cls')


stark_quest(lista_heroes)