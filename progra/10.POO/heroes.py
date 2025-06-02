

class Heroes:
    
    def __init__(self, nombre, apodo, poder, altura, genero):
        self.__nombre = nombre
        self.__apodo = apodo
        self.__poder = poder
        self.__altura = altura
        self.__genero = genero
        
    def __poner_en_mayuculas(self, texto : str) -> str:
        return texto.upper()
    
    def presentarse(self) -> int:
        mensaje = f'''
        Mi nombre es {self.__nombre}
        Mi poder es de {self.__poder}
        Mi genero es {self.__genero}
        '''
        mensaje = self.__poner_en_mayuculas(mensaje)
        return mensaje
    
    def get_nombre(self):
        return self.__nombre
    
    def get_apodo(self):
        return self.__apodo
    
    def get_poder(self):
        return self.__poder
    
    def get_altura(self):
        return self.__altura
    
    def get_genero(self):
        return self.__genero
    
    def __validar_poder(self, nuevo_poder : int, num_min : int, num_max) -> bool:
        resultado = False
        if num_max > nuevo_poder > num_min:
            resultado = True
        return resultado
    
    def set_poder(self,nuevo_poder : int):
        resultado = self.__validar_poder(nuevo_poder,0,101)
        if resultado == True:
            self.__poder = nuevo_poder