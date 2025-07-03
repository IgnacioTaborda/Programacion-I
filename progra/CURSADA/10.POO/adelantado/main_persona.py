from poo_persona import Persona
from adulto import Adulto
from estudiantes import Estudiante

ser_humano_1 = Adulto("Taborda","Ignacio", 46354556, "goku 616")
ser_humano_2 = Persona("China","Mimu", 46464646, "goku 717")
ser_humano_3 = Estudiante("Sapo","Pepe", 77777777, "goku 717",1262,3)

personajes = [
   ser_humano_1, ser_humano_2, ser_humano_3
]

for personaje in personajes:
    print(personaje.nombre_persona)
