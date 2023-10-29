STRING nombre {"Daniel"}
INT edad {25}
STRING genero {"Hombre"}
STRING profesion {"Estudiante"}

INT numeros[10] {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

DICTIONARY informacion_personal {
    "Nombre": "Daniel",
    "Edad": 24,
    "Genero": "Hombre"
    "Profesion": "Estudiante"
}

INT suma {0}

FOR num IN numeros {
    suma = suma + num
}

PRINT("Información Personal:")
PRINT("--Nombre: ", informacion_personal["Nombre"])
PRINT("--Edad: ", informacion_personal["Edad"])
PRINT("--Genero: ", informacion_personal["Genero"])
PRINT("--Profesion: ", informacion_personal["Profesion"])

IF ( informacion_personal["Edad"] < 18 ) {
    PRINT(informacion_personal["Nombre"], " eres menor de edad")
} ELIF ( informacion_personal["Edad"] >= 65 ) {
        PRINT(informacion_personal["Nombre"], " eres un adulto mayor")
} ELSE {
    PRINT(informacion_personal["Nombre"], "eres un adulto ")
}

PRINT("Números:", numeros)
PRINT("La suma de los números es: ", suma)
