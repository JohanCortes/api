import pyodbc

class sqlDb:
    def __init__(self, connection_string):
        self.connection_string = connection_string
        self.conn = pyodbc.connect(connection_string)

    def consultar(self, query):
        cursor = self.conn.cursor()
        cursor.execute(query)
        column_names = [column[0] for column in cursor.description]
        resultados = []
        for row in cursor.fetchall():
            fila_dict = {column_names[i]: row[i] for i in range(len(column_names))}
            resultados.append(fila_dict)
        return resultados

    def modificar(self, query, values):
        cursor = self.conn.cursor()
        cursor.execute(query, values)
        self.conn.commit()
        return cursor.rowcount

    def cerrar_conexion(self):
        self.conn.close()
