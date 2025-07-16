def leer_csv(archivo : str) -> list[list]:
    """Recibe un archivo CSV por parametro y retonar una matriz
    con la informacion

    Args:
        archivo (str): _description_

    Returns:
        list[list]: Retorno el archivo en una matriz, donde
        cada lista representa un renglon.
    """
    ranking = []
    with open(file=archivo, mode="r", encoding="utf-8") as archivo:
        for i in archivo.readlines():
            renglon = i.replace("\n","")
            separador = ","
            lista = renglon.split(separador)
            lista[1] = int(lista[1]) 
            ranking.append(lista)  
    return ranking   

def escribir_csv(csv: str, datos: list[list]):
    """Recibe una matriz y la escribe en un archivo CSV

    Args:
        csv (str): Archivo CSV en donde se escribiran los datos
        datos (list[list]): Matriz con los datos a escribir
    """
    with open(file=csv, mode="w", encoding="utf-8") as archivo:
        largo_matriz = len(datos)
        largo_fila = len(datos[0])
        
        for i in range(largo_matriz):
            linea = ""
            for j in range(largo_fila):     
                linea += str(datos[i][j])
                if j == 0:
                    linea += ","
            archivo.write(linea + "\n")