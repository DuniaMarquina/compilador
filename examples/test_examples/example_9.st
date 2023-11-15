STRING nombre_cliente {"Juan Perez"}
INT edad_cliente {50}

// TRUE si pertenece FAIL no pertenece
BOOL miembro_programa {TRUE}

INT porcentaje {100}
INT D1 {85}
INT D2 {90}
INT DES {0}

INT costo_comida {100}
INT descuento {0}
INT costo_final {0}

IF (edad_cliente >= 60) {
    PRINT("aplica descuento por edad ")
    descuento = D1 / porcentaje
} ELIF (miembro_programa) {
    PRINT("aplica descuento por membresia ")
    descuento = D2 / porcentaje
}

costo_final = costo_comida * descuento
DES = costo_final - costo_comida

PRINT("Bienvenido: , ", nombre_cliente)
PRINT("Costo de la comida: ", costo_comida, " $")
PRINT("Descuento: ", DES, " $")
PRINT("TOTAL A PAGAR: ", costo_final, " $")

