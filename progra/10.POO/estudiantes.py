from poo_persona import Persona

class Estudiante(Persona):
    def __init__(self, apellido, nombre, dni, direccion, legajo, cant_materias):
        super().__init__(apellido, nombre, dni, direccion)
        
        self.legajo_estudiante = legajo
        self.cant_materias_estudiante = cant_materias
        
    def saludar(self):
        mensaje = f"El estudiante {self.nombre_persona} esta estudiando {self.cant_materias_estudiante} materias y su legajo es {self.legajo_estudiante}"
        print(mensaje)
