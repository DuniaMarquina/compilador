# Compilador
Compilador para el lenguaje Struct

# Struct Language

Struct es un lenguaje orientado por objetos y fuertemente tipado, cuyo principal objetivo es modelar datos, a través, de un alto nivel de abstracción que soporte las siguientes estructuras de datos conocidas: Diccionarios, vectores, objetos. Con el manejo de tipos de datos básicos (cadenas, enteros, booleanos)

Además, con el propósito en mente que el programador solo tenga que usar llamados a funciones, propias de cada estructura para la manipulación de los datos, es decir, cada estructura debe soportar: Ingreso de nuevos datos, modificación, consultas, eliminación de datos.

# ¿Cómo usar?

1. Descargue el repositorio:
```sh
$ git clone URLREPO
```
2. Cree un entorno virtual de python:
```sh
$ python3 -m venv .venv
```
3. Active el entorno virtual:
```sh
$ source .venv/bin/activate
```
4. Instale las dependencias:
```sh
(.venv)$ pip install -r requirements.txt
```
5. Para ejecutar el intérprete de STRUCT necesita pasarle la ubicación y nombre del archivo que contiene el código fuente de su programa, como se ve a continuación:
```sh
(.venv)$ python3 struct_interpreter.py path_to_code/name_of_file.st
```