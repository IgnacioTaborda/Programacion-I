from heroes import Heroes
import utn_fra.datasets as UTN
from matrices_funciones import trasponer_matriz



heroe_1 = Heroes("Spiderman", "Tu amigable vecino","777", "1.78M", "Papu")
#print(heroe_1.presentarse())
#print(type(heroe_1))

matriz_super_heroes = [
    UTN.lista_nombres_heroes_small,
    UTN.lista_apodos_heroes_small,
    UTN.lista_poder_heroes_small,
    UTN.lista_alturas_heroes_small,
    UTN.lista_generos_heroes_small  
]

nueva_lista_heroes = []
matriz_super_heroes_traspuesta = trasponer_matriz(matriz_super_heroes)
#print(matriz_super_heroes_traspuesta[0:4])

for i in matriz_super_heroes_traspuesta:
    nuevo_heroe = Heroes(
        i[0],
        i[1],
        i[2],
        i[3],
        i[4])
    nueva_lista_heroes.append(nuevo_heroe)
    
    
for heroe in nueva_lista_heroes:
    print(heroe.get_nombre())
