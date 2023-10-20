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
        },
    }
