DICTIONARY inventory {"apple": 5, "banana": 3, "orange": 2}


FOR i in inventory
{
   IF i.key == "apple"
   {
      IF i.value > 3
      {
         i["apple"] = i["apple"] -1
      }
   }
   elif i.key == "banana"
   {
      IF i.value > 3
      {
         i["banana"] = i["banana"]-1
      }
   }
   ELIF i.key == "orange"
   {
      if i.value > 3
      {
         i["orange"] = i["orange"]-1
      }
   }
   ELSE
   {
      PRINT(i.key," not found in inventory")
   }

}

for i IN inventory
{
    PRINT(i.key, i.value)
}

//Nuevas entradas

INT new_apple {5}
int new_banana {3}
INT new_orange {2}

//Actualizacion del inventario

inventory[apple] = new_apple
inventory["banana"] = new_banana
inventory["orange"] = new_orange

For i IN inventori
{
    PRINT(i.key, i.value)
}

