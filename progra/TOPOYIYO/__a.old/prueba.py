import pygame as pg
import json

def leer_json(archivo : str) -> dict[dict]:
    with open(file=archivo, mode="r", encoding="utf-8") as archivo:
        jsoncito = json.load(archivo) 
    return jsoncito    

def sobrescribir_json(archivo_og, actualizacion):
    with open(file=archivo_og, mode="w", encoding="utf-8") as archivo:
        json.dump(obj=actualizacion, fp=archivo, indent=4)

mazo = leer_json("./progra/TOPOYIYO/__a.old/mazo.json")

#FITS ROUND
heroes = mazo.get("jugador")
villanos = mazo.get("enemigo")
mazo = {
    "heroes" : heroes,
    "villanos" : villanos
}


heroe_1 = heroes[0]
villano_1 = villanos[0]

restar_golpe = (villano_1.get("hp")) - (heroe_1.get("atk"))


villano_1["hp"] = restar_golpe

sobrescribir_json("./progra/TOPOYIYO/__a.old/mazo.json",mazo)


