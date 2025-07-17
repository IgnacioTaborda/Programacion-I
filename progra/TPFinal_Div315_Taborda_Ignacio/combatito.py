import os
import pygame as pg
import personaje_base
import cartas as card
import herramientas.funciones_archivos as fun_archivos
import json
import variables as var
import os



def combate(hero: dict, villano: dict):

    cartas_hero = card.unificar_cartas(hero)
    cartas_villano = card.unificar_cartas(villano)

    hero_stats = card.sumar_stats_totales(cartas_hero)
    villano_stats = card.sumar_stats_totales(cartas_villano)

    hero_hp_total = hero_stats["HP"]
    villano_hp_total = villano_stats["HP"]
    hero_hp_inicial = hero_hp_total  # Para HEAL

    deseos_disponibles = {
        "HEAL": True,
        "SHIELD": True
    }

    rondas = len(cartas_hero)
    
    puntuacion_heroe = 0

    print("=== COMBATE INICIADO ===")
    print(f"HP Total Heroe: {hero_hp_total}")
    print(f"HP Total Villano: {villano_hp_total}")
    print("========================")

    for i in range(rondas):
        carta_hero = cartas_hero[i]
        carta_villano = cartas_villano[i]

        atk_hero = int(carta_hero["ATK"])
        bonus_hero = int(carta_hero["Bonus"])
        atk_hero_total = int(atk_hero * (1 + bonus_hero / 100))

        atk_villano = int(carta_villano["ATK"])
        bonus_villano = int(carta_villano["Bonus"])
        atk_villano_total = int(atk_villano * (1 + bonus_villano / 100))

        print(f"\n--- RONDA {i + 1} ---")
        print(f"Heroe ATK: {atk_hero_total} (bonus {bonus_hero}%) vs Villano ATK: {atk_villano_total} (bonus {bonus_villano}%)")

        # Mostrar deseos disponibles
        disponibles = []
        for deseo in deseos_disponibles:
            if deseos_disponibles[deseo] == True:
                disponibles.append(deseo)

        if disponibles:
            print(f"Deseos disponibles: {', '.join(disponibles)}")
            deseo = input("¿Querés usar un deseo? (HEAL/SHIELD/N): ").strip().upper()
            print("####################")
            

            if deseo == "HEAL" and deseos_disponibles["HEAL"]:
                hero_hp_total = hero_hp_inicial
                deseos_disponibles["HEAL"] = False
                print("🧬 Usaste HEAL: HP restaurado.")

            elif deseo == "SHIELD" and deseos_disponibles["SHIELD"]:
                deseos_disponibles["SHIELD"] = "EN USO"
                print("🛡️ Activaste SHIELD para esta ronda.")

            else:
                print("No se usó ningún deseo.")
        else:
            print("No quedan deseos disponibles.")

        # Resolver el combate
        if atk_hero_total > atk_villano_total:
            villano_hp_total -= atk_hero_total
            puntuacion_heroe += 250
            print(f"Heroe gana la ronda. Villano pierde {atk_hero_total} HP")

        elif atk_villano_total > atk_hero_total:
            if deseos_disponibles["SHIELD"] == "EN USO":
                print("🛡️ SHIELD activado: el daño se refleja al enemigo.")
                villano_hp_total -= atk_villano_total
                deseos_disponibles["SHIELD"] = False
            else:
                hero_hp_total -= atk_villano_total
                puntuacion_heroe -= 150
                print(f"Villano gana la ronda. Heroe pierde {atk_villano_total} HP")

        else:
            print("Empate. Nadie pierde HP.")
            
        if hero_hp_total <= 0:
            print("\n❌ ¡VILLANO GANA LA PARTIDA!")
            break
        elif villano_hp_total <= 0:
            print("\n✅ ¡HEROE GANA LA PARTIDA!")
            break


        print(f"HP Heroe: {hero_hp_total}")
        print(f"HP Villano: {villano_hp_total}")

        # Chequear si alguien perdió
        if hero_hp_total <= 0:
            print("\n❌ ¡VILLANO GANA LA PARTIDA!")
            
        elif villano_hp_total <= 0:
            print("\n✅ ¡HEROE GANA LA PARTIDA!")
            

        os.system("pause")
        
    combate_retorno = {
        "pantalla_actual" : "ranking",
        "puntuacion_total" : puntuacion_heroe 
    }

    # Resultado final
    print("\n=== FIN DEL COMBATE ===")
    if hero_hp_total > villano_hp_total:
        print("✅ ¡HEROE GANA POR PUNTAJE!")
    elif villano_hp_total > hero_hp_total:
        print("❌ ¡VILLANO GANA POR PUNTAJE!")
    else:
        print("⚖️ ¡EMPATE TOTAL!")
        
    return combate_retorno
        
    
