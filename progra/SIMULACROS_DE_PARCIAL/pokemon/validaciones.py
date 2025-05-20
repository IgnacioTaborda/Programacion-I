def validar_numero(num_min : int, num_max : max):
    opcion = input(f"Ingrese un num entre {num_min} - {num_max}: ")
    
    if opcion.isdigit() and (num_min <= int(opcion) <= num_max):
        opcion_int = int(opcion)
    else:
        print("Error")
        opcion_int = validar_numero(num_min,num_max)
    return opcion_int