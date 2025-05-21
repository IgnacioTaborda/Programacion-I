def validar_numero() -> int:
    numero = input("Ingrese un número: ")
    if numero.isdigit():
        numero = int(numero)
        return numero
    else:
        return validar_numero()
    
def validar_rango_numerico(numero : int, num_min : int, num_max : int):
    if num_max >= numero >= num_min:
        return numero
    else:
        numero = validar_numero()
        return validar_rango_numerico(numero, num_min, num_max)
    