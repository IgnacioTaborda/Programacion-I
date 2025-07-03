class Universidad:

    def __init__(self, nombre_universidad : str):
        self.__nombre_universidad = nombre_universidad
        
    def get_nombre(self) -> str:
        return self.__nombre_universidad

class Carrera:

    def __init__(self, especialidad_estudiante : str):
        self.__especialidad_estudiante = especialidad_estudiante

    def get_carrera(self):
        return self.__especialidad_estudiante

class Estudiante:

    def __init__(self, nombre : str, edad : int):
        self.__nombre = nombre
        self.__edad = edad

    def mostrar_info_estudiante(self, universidad : str, especialidad : str):
        mensaje = f'''
        El estudiante {self.__nombre} de {self.__edad} años. Esta estudiando {especialidad} en {universidad}
        '''
        return mensaje

facu = Universidad("UTN")
carrerubi = Carrera("Tecnicatura en programación")
alumno = Estudiante("Ignacio","20")

nombre_facu = facu.get_nombre()
nombre_carrera = carrerubi.get_carrera()

print(Estudiante.mostrar_info_estudiante(alumno,nombre_facu,nombre_carrera))