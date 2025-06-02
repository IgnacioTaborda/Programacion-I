class Persona:
    def __init__(self, apellido : str, nombre :str, dni : int, direccion : str):
        self.apellido_persona = apellido
        self.nombre_persona = nombre
        self.dni_persona = dni
        self.direccion_persona = direccion

    def saludar(self) -> None:
        mensaje = f"Hola, me llamo {self.nombre_persona} {self.apellido_persona} !"
        print(mensaje)





#ser_humano_1 = Adulto("Taborda","Ignacio", 46354556, "goku 616")
ser_humano_2 = Persona("China","Mimu", 46464646, "goku 717")
#ser_humano_3 = Estudiante("Sapo","Pepe", 77777777, "goku 717",1262,3)

#personajes = [
#    ser_humano_1, ser_humano_2, ser_humano_3
#]

# for personaje in personajes:
#     print(personaje.nombre_persona)

