INT sum {0}
INT i {1}
STRING PR {"hola"}

INT array[10] {1,2,3,4,5,6,7,8,9,10}
FOR i IN array {
    sum = sum + PR
}
PRINT("suma: ", sum)