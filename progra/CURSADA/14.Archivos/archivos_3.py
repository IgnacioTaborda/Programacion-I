personas = [
    {
        "nombre" : "Pepe",
        "apellido" : "Argento"
    },
    {
        "nombre" : "Moni",
        "apellido" : "Argento"
    },
    {
        "nombre" : "Fatiga",
        "apellido" : "Perrito"
    }
]

lista_textos = []

for i in range(len(personas)):
    texto = f"{personas[i].get("nombre")},{personas[i].get("apellido")}"
    lista_textos.append(texto)
    
contenido = "\n".join(lista_textos)
contenido = "Nombre,Apellido\n" + contenido

with open("./progra/14.Archivos/personas.csv","w",encoding="utf-8") as file:
    file.write(contenido)