# README.md
## Descripción
Esta es una aplicación de Python que permite leer una tabla CSV en este caso se usa el archivo `heart.csv` que es utilizado como base de datos. Además, proporciona funcionalidades para ejecutar consultas y modificar datos en el archivo CSV. Esta aplicación es un API que ofrece endpoints para crear, consultar, actualizar y eliminar filas del archivo CSV, además, de visualizar los datos mediante gráficas.

## Instalación
- Clone el repositorio
- Instale las dependencias con `pip install -r requirements.txt`

## Uso
- Para interactuar con el API, ejecute el servidor con el comando `uvicorn API:app --reload` y acceda a `localhost:8000/docs`.
- Para filtrar resultados en los endpoints `filtrar_filas`, `scatter`, `bar` y `pie` ingresar en el campo `columnas` el nombre de las columnas separadas por coma, en el campo `operadores` la condición correspondiente a cada columna y en `valores` el valor a comparar con la condición correspondiente.
- Para las peticiones `POST` y `PUT` manejar el formato diccionario con los nombres exactos de las variables.
