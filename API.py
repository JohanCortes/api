from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlDb import sqlDb

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class FilaNueva(BaseModel):
    age: int
    sex: int
    cp: int
    trestbps: int
    chol: int
    fbs: int
    restecg: int
    thalach: int
    exang: int
    oldpeak: float
    slope: int
    ca: int
    thal: int
    target: int

db = sqlDb("Driver={SQL Server};Server=DESKTOP-D7N1NE2;Database=Heart;Trusted_Connection=yes;")

@app.get("/filtrar_filas/{columna}/{valor}")
def filtrar_filas(columna: str, valor: float):
    query = f"SELECT * FROM heart WHERE {columna} = {valor}"
    resultados = db.consultar(query)
    if not resultados:
        raise HTTPException(status_code=404, detail="No se encontraron resultados")
    return resultados

@app.get("/obtener_filas/")
def obtener_filas():
    query = "SELECT * FROM heart"
    resultados = db.consultar(query)
    print(resultados)
    if not resultados:
        raise HTTPException(status_code=404, detail="No se encontraron resultados")
    return resultados

@app.get("/obtener_filas/{indice}")
def obtener_fila(indice: int):
    query = f"SELECT * FROM heart WHERE ind = {indice}"
    resultados = db.consultar(query)
    if not resultados:
        raise HTTPException(status_code=404, detail="No se encontraron resultados")
    return resultados[0]

@app.on_event("shutdown")
def cerrar_conexion():
    db.cerrar_conexion()

@app.post("/crear_fila/")
def crear_fila(fila: FilaNueva):
    valores = fila.dict()
    placeholders = ",".join(["?"] * len(valores))
    query = f"INSERT INTO heart VALUES ({placeholders})"
    db.modificar(query, list(valores.values()))
    return {"mensaje": "Fila creada exitosamente"}

@app.put("/actualizar_fila/{indice}")
def actualizar_fila(indice: int, fila: FilaNueva):
    valores = fila.dict()
    placeholders = ",".join([f"{columna} = ?" for columna in valores.keys()])
    query = f"UPDATE heart SET {placeholders} WHERE ind = {indice}"
    db.modificar(query, list(valores.values()))
    return {"mensaje": "Fila actualizada exitosamente"}

@app.delete("/eliminar_fila/{indice}")
def eliminar_fila(indice: int):
    query = f"DELETE FROM heart WHERE ind = {indice}"
    db.modificar(query, [])
    return {"mensaje": "Fila eliminada exitosamente"}