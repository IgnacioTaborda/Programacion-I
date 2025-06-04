import os
from lady_gaga import playlist_lady_gaga
from impresiones import imprimir_menu
from validaciones import pedir_numero, validar_rango_numerico
from diccionario import convertir_duracion_en_segundos


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
                Vistas (int): Cantidad de reproducciones en números enteros.
                Fecha de lanzamiento (date): Fecha de publicación del video.
                '''
                #Cantidad de reproducciones en números enteros
                

                #Duración del video en segundos
                for i in range(cant_canciones):
                    tiempo = convertir_duracion_en_segundos(playlist_lady_gaga[i],'Duracion')
                    playlist_lady_gaga[i]['Duracion'] = tiempo

                
                    
                primera_opcion_ejecutada = True
                
            
            case 2:
                if primera_opcion_ejecutada == True:
                    pass

            case 3:
                if primera_opcion_ejecutada == True:
                    pass

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