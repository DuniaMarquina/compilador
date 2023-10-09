// Example to test error handling
// Basic types
INT numElements {2}
-BOOL nedded {TRUE} // Error: minus before of reserved word

// Data colections
OBJ wishList[numElements] {{},{}}

DICTION{ARY inventory // Error: Curly brace inside of reserved word
{
    "Lollipop":?
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

I%NT i {0} // Error: Invalid character