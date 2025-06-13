import variables as var
archivo = open(file=var.RUTA_ARCHIVO_TEXTO, mode="r", encoding='utf-8') #sirve para codificar, hay una banda, este nos permite añadir "ñ" "ó" "BV"

texto = archivo.read() #devuelve un string
                #readlines --> lista con los elementos + barra n
var.informacion['data'] = texto 

archivo.close()

print(f"Mensaje = {var.informacion.get('data')}") #REVISAR CLASE GRABADA
