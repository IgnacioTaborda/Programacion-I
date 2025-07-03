contador = 0
cant_masculino_IOT_IA_edad_25_a_50 = 0
cant_no_ia = 0
empleados_ingresados = 0
nombre_mayor_masculino = None
tecnologia_mayor_masculino = None
edad_mayor_masculino = 0


while contador < 10:
    nombre = input("Ingrese su nombre: ")

    edad = input("Ingrese su edad: ")
    edad = int(edad)
    while edad < 18 or edad > 110: 
        edad = input("Ingrese su edad: ")
        edad = int(edad)

    genero = input("Ingrese su genero (Masculino - Femenino - Otro): ")
    while genero != "Masculino" and genero != "Femenino" and genero != "Otro":
        genero = input("Ingrese la genero (Masculino - Femenino - Otro): ")

    tecnologia = input("Ingrese su tecnologia (IA - RV/RA - IOT): ")
    while tecnologia != "IA" and tecnologia != "RV/RA" and tecnologia != "IOT":
        tecnologia = input("Ingrese su tecnologia (IA - RV/RA - IOT): ")
        


    "Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad esté entre 25 y 50 años (inclusive)."
    if genero == "Masculino" and (tecnologia == "IA" or tecnologia == "IOT") and (edad >= 25 and edad <= 50):
        cant_masculino_IOT_IA_edad_25_a_50 += 1

    "Porcentaje de empleados que no votaron por IA, siempre y cuando su género no sea Femenino o su edad se encuentre entre los 33 y 40."
    if tecnologia != "IA" and (genero != "Femenino" or (edad > 33 and edad < 40)):
        cant_no_ia += 1
    empleados_ingresados = +1

    "Empleado masculino de mayor edad: Mostrar su nombre y la tecnología que votó."
    if genero == "Masculino" and edad > edad_mayor_masculino:
        nombre_mayor_masculino = nombre
        tecnologia_mayor_masculino = tecnologia
        edad_mayor_masculino = edad
    
    contador += 1

porcentaje_cant_no_ia = (cant_no_ia / empleados_ingresados) * 100


print(f"La cantidad de emleados de género masculino que votaron por IOT o IA, cuya edad esté entre 25 y 50 años inclusive es de: {cant_masculino_IOT_IA_edad_25_a_50}")
print(f"El porcentaje de empleados que no votaron por IA, siempre y cuando su género no sea Femenino o su edad se encuentre entre los 33 y 40 es de: {porcentaje_cant_no_ia}")
print(f"El nombre del señor más grande es {nombre_mayor_masculino} y la tecnologia que eligio es {tecnologia_mayor_masculino}")


    

