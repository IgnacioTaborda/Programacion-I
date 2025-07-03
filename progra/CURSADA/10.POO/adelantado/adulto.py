from poo_persona import Persona

class Adulto(Persona):
    def __init__(self, apellido, nombre, dni, direccion):
        super().__init__(apellido, nombre, dni, direccion)
        
    def saludar(self):
        mensaje = f"El salto del {self.nombre_persona}"
        print(mensaje)
