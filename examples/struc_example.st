// Basic types
STRING a {"Hola mundo!"}

// Data colections
DICTIONARY inventory {"apple": 5, "banana": 3, "orange": 2}
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
        PRINT(dataCl, "")
    }
}

PRINT(a, "Hola mundo!")

a = "Hola universo!" // Break?
inventory["apple"] = 80 // Doble break?
complex_dict["apple"]["colour"] = "Green"

INT x = 10

INT array[4] {1,2,3,4}

INT arr2[2][2][2] {
    { {3, 3}, {x, 4} },
    { {5, 5}, {6, 6} }
}

arr[2][3][1] = 4
