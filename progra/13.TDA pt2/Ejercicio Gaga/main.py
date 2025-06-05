import os
from lady_gaga import playlist_lady_gaga
from impresiones import imprimir_menu, imprimir_temas
from validaciones import pedir_numero, validar_rango_numerico, determinar_si_un_caracter_existe
from diccionario import (
    convertir_duracion_en_segundos, convertir_reproduciones_str_a_int, añadir_colaboradores
)


def aplicacion_gaga(): 
    encendido = True
    primera_opcion_ejecutada = False

    while encendido:
        imprimir_menu()
        opciones = pedir_numero()
        opciones = validar_rango_numerico(opciones,1,10)
        cant_canciones = len(playlist_lady_gaga)

        match opciones:
            case 1:
                '''
                Fecha de lanzamiento (date): Fecha de publicación del video.
                '''
                #Colaboradores
                for i in range(len(playlist_lady_gaga)):
                    verificador = determinar_si_un_caracter_existe(playlist_lady_gaga[i],'Tema','|')
                    if verificador == True:
                        colaboradores = añadir_colaboradores(playlist_lady_gaga[i],'Tema')
                        playlist_lady_gaga[i]['colaboradores'] = colaboradores
                
                
                #Cantidad de reproducciones en números enteros
                for i in range(len(playlist_lady_gaga)):
                    vistas = convertir_reproduciones_str_a_int(playlist_lady_gaga[i],"Vistas")
                    playlist_lady_gaga[i]["Vistas"] = vistas

                #Duración del video en segundos
                for i in range(cant_canciones):
                    tiempo = convertir_duracion_en_segundos(playlist_lady_gaga[i],'Duracion')
                    playlist_lady_gaga[i]['Duracion'] = tiempo
                    
                primera_opcion_ejecutada = True
            
            case 2:
                if primera_opcion_ejecutada == True:
                    for i in range(cant_canciones):
                        imprimir_temas(playlist_lady_gaga[i],'Tema','Vistas','Duracion')

            case 3:
                if primera_opcion_ejecutada == True:
                    print(playlist_lady_gaga)

            case 4:
                if primera_opcion_ejecutada == True:
                    pass

            case 5:
                if primera_opcion_ejecutada == True:
                    pass

            case 6:
                if primera_opcion_ejecutada == True:
                    pass

            case 7:
                if primera_opcion_ejecutada == True:
                    pass

            case 8:
                if primera_opcion_ejecutada == True:
                    pass

            case 9:
                if primera_opcion_ejecutada == True:
                    pass

            case 10:
                encendido = False
                print("Gracias por usar el programa. Hasta la proxima!")

        if primera_opcion_ejecutada == False:
            print(f"Para poder ejecutar la opción {opciones} primero se debe ejecutar la opción 1")

        os.system('pause')
        os.system('cls')        

        

aplicacion_gaga()