STRING nombre {"Daniel Monsalve"}
INT dia_nacimiento {6}
INT mes_nacimiento {8}
INT anio_nacimiento {1998}

INT dia_actual {26}
INT mes_actual {10}
INT anio_actual {2023}

INT diferencia_anios {0}
INT edad {0}

diferencia_anios = anio_actual - anio_nacimiento

IF (mes_actual < mes_nacimiento) {
    edad = diferencia_anios - 1
    PRINT("si llega")
}ELIF (mes_actual == mes_nacimiento) {
    IF (dia_actual < dia_nacimiento) {
        edad = diferencia_anios - 1    
        PRINT("si llega")
    }
    PRINT("si llega")
} ELSE {
    edad = diferencia_anios
}

PRINT("Bienvenido, ", nombre)
PRINT("Fecha de nacimiento: ", dia_nacimiento, "/", mes_nacimiento, "/", anio_nacimiento)
PRINT("Tienes ", edad, " años de edad.")
