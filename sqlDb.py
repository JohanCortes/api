import pyodbc
import pandas as pd
from datetime import datetime

class sqlDb:
    def __init__(self, connection_string):
        self.connection_string = connection_string
        self.conn = pyodbc.connect(connection_string)

    def consultar(self, query):
        ti = datetime.now()
        resultados = pd.read_sql("select * from heart where age = 49", self.conn).to_dict(orient="records")
        #resultados = pd.read_csv("heart.csv").to_dict(orient="records")
        tf = datetime.now()
        print(f"Tiempo de ejecución: {(tf-ti).total_seconds()} segundos")
        return resultados

    def modificar(self, query, values):
        cursor = self.conn.cursor()
        cursor.execute(query, values)
        self.conn.commit()
        return cursor.rowcount

    def cerrar_conexion(self):
        self.conn.close()
