import os
from utn_fra.datasets import(
    lista_poke_ids, lista_poke_nombres,lista_poke_tipos,lista_poke_poderes,lista_poke_condiciones
)
from impresiones import mostrar_menu
from validaciones import(
    validar_numero
)
from matrices import crear_matriz, mostrar_matriz,filtrar_matriz_poder_superior

def aplicacion(lista_poke_ids,lista_poke_nombres, lista_poke_tipos,lista_poke_poderes,lista_poke_condiciones):
    
    corriendo = True
    matriz_pokemons = []
    matriz_cargadoa = False
    
    while corriendo:
        mostrar_menu()
        opcion = validar_numero(1,7)
        
        match opcion:
            case 1:
                matriz_pokemons = crear_matriz(lista_poke_ids,lista_poke_nombres, lista_poke_tipos,lista_poke_poderes,lista_poke_condiciones)
                print("Matriz creada con exito!")
                matriz_cargadoa = True
                
            case 2:
                if matriz_cargadoa == True:
                    mostrar_matriz(matriz_pokemons)
                
            case 3:
                if matriz_cargadoa == True:
                    filtrada = filtrar_matriz_poder_superior(matriz_cargadoa,3)
                    mostrar_matriz(filtrada)
                
            case 4:
                if matriz_cargadoa == True:
                    pass
                
            case 5:
                if matriz_cargadoa == True:
                    pass
                
            case 6:
                if matriz_cargadoa == True:
                    pass
                 
                    
            case 7:
                corriendo = False
                print("Gracias por usar el programa! Hasta luego")
                
        if not matriz_cargadoa:
            print("Primero se debe ejecutar la opción 1")
            
        os.system('pause')
        os.system('cls')