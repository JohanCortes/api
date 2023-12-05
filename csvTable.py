from dotenv import load_dotenv
#import os
import pandas as pd
#import pyodbc

class csvTable:
    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo
        try:
            self.tabla = pd.read_csv(nombre_archivo)
        except FileNotFoundError:
            self.tabla = pd.DataFrame()

    def obtener_filas(self):
        tabla = self.tabla.copy()
        tabla.insert(0, "ind", tabla.index)
        return tabla.to_dict(orient="records")
    
    def obtener_fila(self, indice):
        if indice not in self.tabla.index:
            return {'message': "No se encontraron resultados"}
        tabla = self.tabla.copy()
        tabla.insert(0, "ind", tabla.index)
        return tabla.loc[indice].to_dict()

    def filtrar_filas(self, columnas, valores, operadores):
        tabla = self.tabla.copy()
        tabla.insert(0, "ind", tabla.index)
        [columnas, valores, operadores] = [columnas.split(","), valores.split(","), operadores.split(",")]
        if len(columnas) != len(valores) or len(columnas) != len(operadores):
            return {'message': "Error en los parámetros"}
        query = " & ".join([f"{columna} {operador} {valor}" for columna, valor, operador in zip(columnas, valores, operadores)])
        return tabla.query(query).to_dict(orient="records")

    def crear_fila(self, datos_nuevos):
        nueva_fila = pd.DataFrame(datos_nuevos, index=[0])
        self.tabla = pd.concat([self.tabla, nueva_fila], ignore_index=True)
        self.tabla.to_csv(self.nombre_archivo, index=False)
        return self.obtener_fila(self.tabla.index[-1])

    def actualizar_fila(self, indice, nuevos_datos):
        self.tabla.loc[indice] = nuevos_datos
        self.tabla.to_csv(self.nombre_archivo, index=False)
        return self.obtener_fila(indice)

    def eliminar_fila(self, indice):
        self.tabla = self.tabla.drop(index=indice)
        self.tabla.to_csv(self.nombre_archivo, index=False)
        return True