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
    
    
with open('./progra/14.Archivos/hola.json',"r",encoding='utf-8') as file:
    datos = json.load(file)
    
nombres_2 = [
    {
        "nombre" : "Dardo",
        "apellido" : "Fuseneco"
    },
    {
        "nombre" : "Maria Elena",
        "apellido" : "Fuseneco"
    },
    {
        "nombre" : "La Nena",
        "apellido" : "Fuseneco"
    }
]

datos["nombres"].extend(nombres_2)
datos["gastos"] = [2,5,7,1]
datos["anecdotas"] = "Este mes me la patine todaaaa"

with open('./progra/14.Archivos/hola.json',"w",encoding='utf-8') as file:
    json.dump(datos,file,indent=4)