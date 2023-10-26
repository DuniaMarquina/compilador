INT factorial {1}
INT n {5}
INT array[5] {1,2,3,4,5} // no dejar el array vacio
INT i {1}

FOR i IN array {
    factorial = factorial * i
}
PRINT("Factorial de ",n, "es: ", factorial)