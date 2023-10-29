STRING nombre {"Kevin"}
STRING genero {"Hombre"}

IF (genero == "Hombre") {
    PRINT("Bienvenido Sr. ", nombre)
} ELIF (genero == "Mujer") {
    PRINT("Bienvenida Sra. ", nombre)
} ELSE {
    PRINT("Bienvenidx, ", nombre)
}
