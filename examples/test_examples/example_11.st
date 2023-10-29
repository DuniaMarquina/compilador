DICTIONARY producto {
    "nombre": "Laptop",
    "precio": 1000,
    "descuento": 100
}
INT precio_final {0}
precio_final = producto["precio"] - producto["descuento"]

PRINT("Nombre del producto: ", producto["nombre"])
PRINT("Precio original: ", producto["precio"])
PRINT("Descuento aplicado: ", producto["descuento"])
PRINT("Precio final: ", precio_final)
