DICTIONARY inventory {"apple": 5, "banana": 3, "orange": 0}

INT a[2][2] {{1,inventory["apple"]}, {2,inventory["banana"] + 5}}

BOOL x {a[0][1] * 2 < inventory["banana"] + 5}

PRINT(x,a, a[0][0], inventory["banana"] + 5, a[0][0] < inventory["banana"] + 5)

FOR i IN inventory
{
   PRINT(i, inventory[i])
   IF (inventory[i] == 0)
   {
      PRINT("Producto agotado:", i)
   }
   ELIF (inventory[i] < 4)
   {
      PRINT("Producto por agotarse:", i)
   }
   ELSE
   {
      PRINT("Producto abundante:", i)
   }
}

//Nuevas entradas

INT new_apple {15}
INT new_banana {13 + new_apple + inventory["banana"]}
INT new_orange {12}

//Actualizacion del inventario

inventory["apple"] = new_apple
inventory["banana"] = new_banana
inventory["orange"] = new_orange

FOR i IN inventory
{
    PRINT(i, inventory[i])
   }

