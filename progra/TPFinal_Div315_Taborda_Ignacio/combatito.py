import os
import pygame as pg
import personaje_base
import cartas as card
import herramientas.funciones_archivos as fun_archivos
import json
import variables as var
import os

archivo_json = fun_archivos.leer_json(var.JSON)

hero = card.armar_mazo_aleatorio(archivo_json.get("cantidades"), archivo_json.get("rutas_cartas"))
villano = card.armar_mazo_aleatorio(archivo_json.get("cantidades"), archivo_json.get("rutas_cartas"))


def combate(hero: dict, villano: dict):

    cartas_hero = card.unificar_cartas(hero)
    cartas_villano = card.unificar_cartas(villano)

    # Paso 2: Calcular HP total
    hero_stats = card.sumar_stats_totales(cartas_hero)
    villano_stats = card.sumar_stats_totales(cartas_villano)

    hero_hp_total = hero_stats["HP"]
    hero_hp_inicial = hero_hp_total
    villano_hp_total = villano_stats["HP"]

    rondas = len(cartas_hero)
    
    deseos_disponibles = {
        "HEAL": True,
        "SHIELD": True
    }
    

    print("=== COMBATE INICIADO ===")
    print(f"HP Total Heroe: {hero_hp_total}")
    print(f"HP Total Villano: {villano_hp_total}")
    print("========================")

    for i in range(rondas):
        carta_hero = cartas_hero[i]
        carta_villano = cartas_villano[i]
        
        atk_hero = int(carta_hero["ATK"])
        atk_villano = int(carta_villano["ATK"])

        print(f"\n--- RONDA {i + 1} ---")
        print(f"Heroe ATK: {atk_hero} vs Villano ATK: {atk_villano}")

        if atk_hero > atk_villano:
            villano_hp_total -= atk_hero
            print(f"Heroe gana la ronda. Villano pierde {atk_hero} HP")
        elif atk_villano > atk_hero:
            hero_hp_total -= atk_villano
            print(f"Villano gana la ronda. Heroe pierde {atk_villano} HP")
        else:
            print("Empate. Nadie pierde HP.")

        print(f"HP Heroe: {hero_hp_total}")
        print(f"HP Villano: {villano_hp_total}")

        # Chequeo de muerte
        if hero_hp_total <= 0:
            print("\n¡VILLANO GANA LA PARTIDA!")
            return "villano"
        elif villano_hp_total <= 0:
            print("\n¡HEROE GANA LA PARTIDA!")
            return "heroe"
        os.system('pause')

    print("\n=== FIN DEL COMBATE ===")
    if hero_hp_total > villano_hp_total:
        print("¡HEROE GANA POR PUNTAJE!")
        
    elif villano_hp_total > hero_hp_total:
        print("¡VILLANO GANA POR PUNTAJE!")
        
    else:
        print("¡EMPATE TOTAL!")
        
    
xd = combate(hero,villano)