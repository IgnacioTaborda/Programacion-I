import json

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

diccionario = {
    "nombres" : personas
}

with open('./progra/14.Archivos/hola.json',"w",encoding='utf-8') as file:
    json.dump(diccionario,file,indent=4)