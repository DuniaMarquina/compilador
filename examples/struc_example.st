INT b {4}
INT array_int[2][2] {{1,2},{3,b}}
STRING array_str[2] {"Hola", "Mundo!"}
BOOL pixel_to_draw[3][2][3] {
    {{TRUE,TRUE,TRUE},{FALSE,FALSE,FALSE}},
    {{TRUE,FALSE,FALSE},{FALSE,TRUE,TRUE}},
    {{FALSE,TRUE,TRUE},{FALSE,TRUE,FALSE}}
}

PRINT(array_int, array_str, pixel_to_draw, "Constant node")