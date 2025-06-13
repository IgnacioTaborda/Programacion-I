import os
from utn_fra.datasets import lista_diccionario_heroes_small
from diccionario_heroes import lista_heroes
from impresiones import imprimir_menu, imprimr_nombre_genero
from validaciones import validar_opcion
from diccionario import es_dato, calcular_max_raza, calcular_min_raza


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
                        
                mensaje = f"El Heroe, de raza Symbiote, más alto es {diccionario_min_desconocido['nombre']}, midiendo {diccionario_min_desconocido['altura_mts']}."
                print(mensaje)

            case 'F':
                #F.Determinar cuál es el personaje más bajo  de raza “Mutant”
                diccionario_min_desconocido = calcular_min_raza(diccionario_heroes,'altura_mts','raza', 'Mutant')
                diccionario_min_desconocido = diccionario_heroes[diccionario_min_desconocido]
                        
                mensaje = f"El Heroe, de raza Mutant, más alto es {diccionario_min_desconocido['nombre']}, midiendo {diccionario_min_desconocido['altura_mts']}."
                print(mensaje)

            case 'G':
                #G.Determinar la altura promedio de los  personajes de empresa “DC Comics”
                pass

            case 'H':
                #H.Determinar la altura promedio de los  personajes de empresa “Marvel Comics”
                pass

            case 'I':
                #I.Informar cual es el Nombre del personaje asociado a cada uno de los indicadores 
                #anteriores (ítems C a F)
                pass

            case 'J':
                #J.Determinar cuántos personajes tienen cada tipo de color de ojos.
                pass

            case 'K':
                #K.Determinar cuántos personajes tienen cada tipo de color de pelo.
                pass

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