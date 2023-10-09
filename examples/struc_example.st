// Basic types
INT numElements {2}
BOOL nedded {TRUE}

// Data colections
OBJ wishList[numElements] {{},{}}

DICTIONARY inventory
{
    "Lollipop":
        {
            INT quantity {16},
            STRING flavor {"Lemon"},
            STRING type {"flat"}
        },
    "Cookie":
        {
            INT quantity {5},
            string flavor {"chocolate"},
            BOOL byUnit {FALSE}
        }
}

INT i {0}

// Loops
FOR item IN inventory
{
    // Flow control
    IF item.value.flavor == "chocolate"
    {
        IF item.value.quantity > 3
        {
            INT quantity {3}

            // Update elements
            item.value.quantity = item.value.quantity - 3
            // Aux functions
            PRINT("You bought ", quantity, " of ", item.key)
            // Update array
            wishList[i] = {STRING name {item.key}, INT quantityToBuy {quantity}}
            i = i + 1
        }
    }
    ELSE
    {
        IF item.value.quantity > 1
        {
            INT quantity {1}
            
            // Update elements
            item.value.quantity = item.value.quantity - 1
            // Aux functions
            PRINT("You bought ", quantity, " of ", item.key)
            // Update array
            wishList[i] = {STRING name {item.key}, INT quantityToBuy {quantity}}
            i = i + 1
        }
    }
}