#1.Desarrollar una función que permita crear un array de números con la cantidad de elementos que establezca el parámetro recibido.
def crear_array(numero:int) -> list:
     lista = [0] * numero
     return lista
#2.Escribir una función que permita ingresar la cantidad de números que reciba como parámetro.  Crear el array con la función del punto 1.
def crear_lista_numerica(numero:int):
    lista = crear_array(numero)
    for i in range(numero):
        numero_array = int(input(f"Ingrese un numero para la posición {i+1}: "))
        lista[i] = numero_array
    return lista
#3.Escribir una función que reciba una lista de enteros, la misma calculará y devolverá el promedio de todos los números.
def calcular_promedio_lista(lista:list) -> float:
    largo_lista = len(lista)
    total_lista = 0
    for i in range(largo_lista):
        total_lista += lista[i]
    promedio = total_lista / largo_lista
    return promedio
#4.Escribir una función parecida a la anterior, pero la misma deberá calcular y devolver el promedio de los números positivos.
def calcular_promedio_lista_positivos(lista:list) -> float:
    contador_positivo = 0
    acummulador_positivo = 0
    
    for i in range(len(lista)):
        if lista[i] > 0:
            contador_positivo += 1
            acummulador_positivo += lista[i]
            
    promedio_positivo = acummulador_positivo / contador_positivo
    return promedio_positivo
#8.Implementar una función llamada reemplazar_nombres que reciba los siguientes parámetros:
#     Una lista de nombres (lista_nombres).
#     Un nombre a buscar en la lista (nombre_antiguo).
#     Un nombre de reemplazo (nombre_nuevo).
def reemplazar_nombres(lista_nombres:list,nombre_antiguo,nombre_nuevo):
    for i in range(len(lista_nombres)):
        if lista_nombres[i] == nombre_antiguo:
            lista_nombres[i] = nombre_nuevo
    return lista_nombres
#9.Crear una función que reciba como parámetros dos arrays. La función deberá retornar un array con la intersección de los dos arrays.
def interseccion_de_arrays(lista_1:list,lista_2:list):
    lista_interseccion = []
    for i in range(len(lista_1)):
        for j in range(len(lista_2)):
            if lista_1[i] == lista_2[j]:
                lista_interseccion.append(lista_2[j])
    return lista_interseccion
m = ["a","c","b"]
n = ["b","g", "l","e"]
#11.Crear una función que reciba como parámetros dos arrays. La función deberá retornar un array con la diferencia de los dos arrays.
def diferencia_de_arrays(lista_1:list,lista_2:list):
    lista_diferencia = []
    for i in range(len(lista_1)):
        for j in range(len(lista_2)):
            if lista_1[i] != lista_2[j]:
                lista_diferencia.append(lista_1[i])
                break
    return lista_diferencia
m = ["a","c","b"]
n = ["b","g", "l","e"]

print(diferencia_de_arrays(m,n))