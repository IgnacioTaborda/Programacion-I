import herramientas.inputs as inputs

def validar_opcion(opcion, opciones, mensaje):
    if opcion in opciones:
        return opcion
    else:
        opcion = inputs.elegir_opcion(mensaje)
        return validar_opcion(opcion, opciones,mensaje)