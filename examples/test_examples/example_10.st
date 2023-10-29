STRING nombre {"Dunia"}
STRING genero {"Mujer"}

IF (genero == "Hombre") {
    PRINT("Bienvenido Sr. ", nombre)
} ELSE IF (genero == "Mujer") {
    PRINT("Bienvenida Sra. ", nombre)
} ELSE {
    PRINT("Bienvenidx, ", nombre)
}
