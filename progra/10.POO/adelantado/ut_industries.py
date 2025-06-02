from main_heroes import matriz_super_heroes
from heroes import Heroes

class ComicStore:

    def __init__(self,nombre):
        self.__nombre = nombre
        self.__matriz_heroes = []
        self.__lista_comics_heroes = []

    def convertir_columna_en_fila(self, matriz : list[list], columna : int) -> list:
        """Esta función recibe por parametro una función y una columna, la columna la convierte
        en una fila.

        Args:
            matriz matriz (list[list]): _description_
            columna (int): Columna a convertir

        Returns:
            list: Retorna la columna convertida en una lista
        """
        fila = []
        for filas in range(len(matriz)):
            fila.append(matriz[filas][columna])
        return fila

    def trasponer_matriz(self,matriz : list[list]):
        """Recibe por parametro una matriz y convierte sus columnas en filas.

        Args:
            matriz (list[list]): Matriz a trasponer

        Returns:
            list[list]: Retorna la matriz traspuesta
        """
        matriz_traspuesta = []
        for columnas in range(len(matriz[0])):
            fila = self.convertir_columna_en_fila(matriz,columnas)
            matriz_traspuesta.append(fila)
        self.__matriz_heroes = matriz_traspuesta    

    def inicializar_comics_heroes(self):
        nueva_lista_heroes_obj = []
        self.trasponer_matriz(matriz_super_heroes)
        for i in self.__matriz_heroes:
            nuevo_heroe = Heroes(
                i[0],
                i[1],
                i[2],
                i[3],
                i[4])
            nueva_lista_heroes_obj.append(nuevo_heroe)

        self.__lista_comics_heroes = nueva_lista_heroes_obj

    def mostrar_heroes_de_comic(self):
        for heroe in self.__lista_comics_heroes:
            print(Heroes.presentarse())