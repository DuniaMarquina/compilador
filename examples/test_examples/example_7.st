STRING nombre {"Juan"}
INT edad {25}
INT contador {0}
INT array[10] {1,2,3,4,5,6,7,8,9,10}

PRINT("Bienvenido, ", nombre)
PRINT("Tu edad es ", edad, " años")

FOR contador IN array {
    PRINT("Contador", contador)
}

//IF (edad < 18) {
//    PRINT("Eres menor de edad.")
//} ELSE IF (edad >= 18 AND edad < 60) {
//    PRINT("Eres un adulto.")
//} ELSE {
//    PRINT("Eres un adulto mayor.")
//}



STRING mensaje_final {"Gracias por usar este programa."}
PRINT(mensaje_final)