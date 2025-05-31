class Persona:
    def __init__(self, apellido : str, nombre :str, dni : int, direccion : str):
        self.apellido_persona = apellido
        self.nombre_persona = nombre
        self.dni_persona = dni
        self.direccion_persona = direccion

    def saludar(self,) -> None:
        mensaje = f"Hola, me llamo {self.nombre_persona} {self.apellido_persona} !"
        print(mensaje)

ser_humano_1 = Persona("Taborda","Ignacio", 46354556, "goku 616")
ser_humano_2 = Persona("China","Mimu", 46464646, "goku 717")

personajes = [
    ser_humano_1, ser_humano_2
]

for personaje in personajes:
    personaje.saludar()