# README.md
## Descripción
Esta es una aplicación de Python que permite leer una tabla CSV en este caso se usa el archivo `heart.csv` y la exporta a SQL Server. Además, proporciona funcionalidades para ejecutar consultas y modificar datos en la tabla de SQL Server. Esta aplicación está diseñada para ser utilizada por una API que puede crear, consultar, actualizar y eliminar filas.

## Instalación
Clone el repositorio
Instale las dependencias con pip install -r requirements.txt
Crear una base de datos Sql Server con el nombre `Heart`
## Uso
- Para exportar una tabla CSV a SQL Server, utilice la clase csvTable.
- Para ejecutar consultas y modificar datos en la tabla de SQL Server, utilice la clase SqlDb.
- Para interactuar con la API, ejecute el servidor con el comando `uvicorn API:app --reload` y acceda a `localhost:8000/docs`.