lista_campos = ["nombre", "apellido", "puntaje", "estatus"]

def crear_diccionario(lista_str: list):
    dict = {}
    
    for indice_campo in range(len(lista_campos)):
        dict[lista_campos[indice_campo]] = lista_str[indice_campo]
    
    return dict
    
    
texto = []
texto_dict = []

with open("./progra/14.Archivos/personas.csv", "r", encoding="utf-8") as file:
    
    lista_lineas = file.readlines()
    for linea in lista_lineas:
        
        if lista_lineas.index(linea) == 0:
            continue
        
        contenido = linea.replace("\n", " ")
        
        contenido_linea = contenido.split(",")
        texto.append(contenido_linea)
        
        dict = crear_diccionario(contenido_linea)
        
        texto_dict.append(dict)
        
print(texto_dict)