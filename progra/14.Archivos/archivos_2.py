import variables as var
archivo = open(file=var.RUTA_ARCHIVO_TEXTO, mode="a+", encoding='utf-8') #sirve para codificar, hay una banda, este nos permite añadir "ñ" "ó" "BV"

texto = archivo.seek(5) 
nuevo_texto = "EL PANADERO CON EL PAN"
archivo.write(nuevo_texto)
xd = archivo.read()
print(xd)
archivo.close()

