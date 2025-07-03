def imprimir_menu() -> None:
    menu = f''' 
    1 - Estandarizar datos (Es necesario ejecutar esta opción para usar el programa)
    2 - Mostrar temas
    3 - Los videos se ordenarán por duración, de mayor a menor.
    4 - Se calculará y mostrará el promedio de vistas de todos los videos en millones.
    5 - Se listará el video (o los videos) con la mayor cantidad de vistas.
    6 - Se listará el video (o los videos) con la menor cantidad de vistas
    7 - El usuario ingresará un código de video y el programa mostrará todos los detalles asociados 
        a ese video.
    8 - El usuario ingresará el nombre de un colaborador (de una lista de colaboradores existentes) 
        y el programa mostrará todos los videos en los que haya participado.
    9 - El usuario ingresará un mes y se listarán todos los temas lanzados en ese mes, sin importar el año.
    10 - Salir
    '''
    print(menu)
    
def imprimir_temas(diccionario : dict, titulo : str, vistas : int, duracion : int) -> None:
    tema = f''' 
    {diccionario[titulo]} | {diccionario[vistas]} | {diccionario[duracion]}
    '''
    print(tema)