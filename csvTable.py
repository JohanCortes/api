from dotenv import load_dotenv
import os
import pandas as pd
import pyodbc

class csvTable:
    def __init__(self, nombre_archivo, sql_connection_string):
        self.nombre_archivo = nombre_archivo
        self.connection_string = sql_connection_string
        try:
            self.tabla = pd.read_csv(nombre_archivo)
        except FileNotFoundError:
            self.tabla = pd.DataFrame()

    def obtener_filas(self):
        return self.tabla

    def filtrar_filas(self, columna, valor):
        return self.tabla[self.tabla[columna] == valor]

    def crear_fila(self, datos_nuevos):
        nueva_fila = pd.DataFrame([datos_nuevos], columns=self.tabla.columns)
        self.tabla = pd.concat([self.tabla, nueva_fila], ignore_index=True)
        self.tabla.to_csv(self.nombre_archivo, index=False)

    def actualizar_fila(self, indice, nuevos_datos):
        self.tabla.loc[indice] = nuevos_datos
        self.tabla.to_csv(self.nombre_archivo, index=False)

    def eliminar_fila(self, indice):
        self.tabla = self.tabla.drop(index=indice)
        self.tabla.to_csv(self.nombre_archivo, index=False)

    def exportar_sql(self, nombre_tabla):
        try:
            conn = pyodbc.connect(self.connection_string)
            cursor = conn.cursor()

            cursor.execute(f"""IF OBJECT_ID(N'{nombre_tabla}', 'U') IS NULL CREATE TABLE {nombre_tabla} (
                           ind int primary key identity(1,1),
                           age tinyint,
                           sex tinyint,
                           cp tinyint,
                           trestbps smallint,
                           chol smallint,
                           fbs tinyint,
                           restecg tinyint,
                           thalach smallint,
                           exang tinyint,
                           oldpeak numeric(4,2),
                           slope tinyint,
                           ca tinyint,
                           thal tinyint,
                           target tinyint)""")
            conn.commit()

            cursor.execute(f"DELETE FROM {nombre_tabla}")
            conn.commit()

            for _, row in self.tabla.iterrows():
                valores = tuple(row)
                placeholders = ",".join(["?"] * len(valores))
                insert_query = f"INSERT INTO {nombre_tabla} VALUES ({placeholders})"
                print(insert_query, valores)
                cursor.execute(insert_query, valores)
                conn.commit()

            conn.close()
            print("Exportación exitosa a SQL Server.")

        except Exception as e:
            print(f"Error al exportar a SQL Server: {str(e)}")

nombre_archivo = "heart.csv"
load_dotenv()
Server = os.getenv("Server")
print(Server)
sql_connection_string = "Driver={SQL Server};Server=%s;Database=Heart;Trusted_Connection=yes;", Server

tabla = csvTable(nombre_archivo, sql_connection_string)
res = tabla.filtrar_filas("age", 63)
print(res)
#tabla.exportar_sql("heart")