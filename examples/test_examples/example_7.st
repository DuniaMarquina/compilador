STRING nombre {"Juan"}
INT edad {66}
INT contador {0}
INT array[10] {1,2,3,4,5,6,7,8,9,10}

PRINT("Bienvenido ", nombre)
PRINT("Tu edad es ", edad, " años")

//FOR contador IN array {
//    PRINT("Contador", contador)
//}

IF (edad < 18) {
    PRINT(nombre, " tienes" ,edad , " eres menor de edad")
} ELIF (edad >= 18) {
    IF (edad <= 65) {
        PRINT(nombre," tienes ",edad, " eres un adulto")
    }ELSE {
        PRINT(nombre," tienes ",edad, " eres un adulto mayor")
    }
} 
STRING mensaje_final {"Gracias por usar este programa."}
PRINT(mensaje_final)