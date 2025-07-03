import json

with open('./progra/14.Archivos/hola.json',"r",encoding='utf-8') as file:
    configs = json.load(file)
    
    
anecdotas = configs.get("anecdotas")
gastos = configs.get("gastos")
personas = configs.get("nombres")

personas.append({"nombre" : "Coqui", "apellido" : "Argento"})

with open('./progra/14.Archivos/hola.json',"w",encoding='utf-8') as file:
    json.dump(configs, file,indent=4)