import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

class draw:
    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo
        try:
            self.tabla = pd.read_csv(nombre_archivo)
        except FileNotFoundError:
            self.tabla = pd.DataFrame()

    async def scatter_graph(self, colx, coly, nombre, columnas = None, valores = None, operadores = None):
        if columnas == None or valores == None or operadores == None:
            tabla = self.tabla
        else:
            [columnas, valores, operadores] = [columnas.split(","), valores.split(","), operadores.split(",")]
            if len(columnas) != len(valores) or len(columnas) != len(operadores):
                return False
            query = " & ".join([f"{columna} {operador} {valor}" for columna, valor, operador in zip(columnas, valores, operadores)])
            tabla = self.tabla.query(query)
        x = tabla[colx]
        y = tabla[coly]
        plt.scatter(x, y)
        plt.xlabel(colx)
        plt.ylabel(coly)
        plt.title(nombre)
        plt.savefig('./images/' + nombre + ".png")
        plt.show(block=False)
        plt.close()
        return './images/' + nombre + ".png"
    
    async def bar_graph(self, col, rango, nombre, columnas = None, valores = None, operadores = None):
        if columnas == None or valores == None or operadores == None:
            tabla = self.tabla
        else:
            [columnas, valores, operadores] = [columnas.split(","), valores.split(","), operadores.split(",")]
            if len(columnas) != len(valores) or len(columnas) != len(operadores):
                return False
            query = " & ".join([f"{columna} {operador} {valor}" for columna, valor, operador in zip(columnas, valores, operadores)])
            tabla = self.tabla.query(query)
        rangos = np.arange(tabla[col].min() - (tabla[col].min()%rango), tabla[col].max() + rango, rango)
        x = pd.cut(tabla[col], rangos).value_counts(sort=False)
        rangos = rangos[:-1].astype(str)
        plt.bar(rangos, x.values)
        plt.xlabel(col)
        plt.ylabel("Frecuencia")
        plt.title(nombre)
        plt.savefig('./images/' + nombre + ".png")
        plt.show(block=False)
        plt.close()
        return './images/' + nombre + ".png"
    
    async def pie_graph(self, col, rango, nombre, columnas = None, valores = None, operadores = None):
        if columnas == None or valores == None or operadores == None:
            tabla = self.tabla
        else:
            [columnas, valores, operadores] = [columnas.split(","), valores.split(","), operadores.split(",")]
            if len(columnas) != len(valores) or len(columnas) != len(operadores):
                return False
            query = " & ".join([f"{columna} {operador} {valor}" for columna, valor, operador in zip(columnas, valores, operadores)])
            tabla = self.tabla.query(query)
        rangos = np.arange(tabla[col].min() - (tabla[col].min()%rango), tabla[col].max() + rango, rango)
        x = pd.cut(tabla[col], rangos).value_counts(sort=False)
        rangos = rangos[:-1].astype(str)
        plt.pie(x.values, labels=rangos, autopct='%1.2f%%', shadow=True, startangle=90)
        plt.title(nombre)
        plt.savefig('./images/' + nombre + ".png")
        plt.show(block=False)
        plt.close()
        return './images/' + nombre + ".png"