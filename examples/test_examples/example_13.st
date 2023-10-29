DICTIONARY personas {
    "persona1": {
        "nombre": "Dunia Marquina",
        "edad": 26,
        "profesion": "Estudiante"
        "Ciudad": "Merida"
    }
    "persona2": {
        "nombre": "Kevin Marquez",
        "edad": 26,
        "profesion": "Estudiante"
        "Ciudad": "Merida"
    }
    "persona3": {
        "nombre": "Daniel Monsalve",
        "edad": 24,
        "profesion": "Estudiante"
        "Ciudad": "Merida"
    }
    "persona4": {
        "nombre": "Jesus Valero",
        "edad": 23,
        "profesion": "Dev"
        "Ciudad": "Merida"
    }
    "persona5": {
        "nombre": "Luis Cortes",
        "edad": 23,
        "profesion": "Dev"
        "Ciudad": "Merida"
    }
}
INT contador {0}
INT i {0}
FOR contador IN personas {
    i = i + 1
    PRINT("persona",i,": ", personas[contador])
}


