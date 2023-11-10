// Basic types
STRING a {"Hola mundo!"}

// Data collections
DICTIONARY inventory {"apple": 5, "banana": 3, "orange": 2}
PRINT(inventory)
DICTIONARY complex_dict { // Nested DICTIONARY
    "fruits": {
        "apple": {
            "colour": "red",
            "seed": TRUE
            },
        "banana": {
            "colour": "yellow", // More comments
            // HARD TESTING 
            "seed": TRUE // And more comments
            } // Another comment
        },
    "vegetables": {
        "onnion": {
            "colour": "white",
            "seed": FALSE
            },
        "potato": {
            "colour": "red",
            "seed": TRUE
            }
        }, // More test comments
    }

// Comment just comment
// Let's try again  

FOR item IN complex_dict
{
    DICTIONARY client {
        "name": "Charles",
        "lastName": "Perez",
        "id": 55555555
    }
    client["lastName"] = "Leclerc" 
    // Some comments for here
    // Ha!, lets due it
    FOR dataCl IN client {
        BOOL stillWaiting {FALSE} // Let's break this parser
        PRINT(dataCl,client[dataCl], "")
    }
}

PRINT(a, "Hola mundo!")

a = "Hola universo!" // Break?
inventory["apple"] = 80 // Doble break?
complex_dict["fruits"]["apple"]["seed"] = FALSE
PRINT(a)
PRINT(inventory)
PRINT(complex_dict)


INT array[3] {1,2,3}

PRINT(array)

array[2] = 4