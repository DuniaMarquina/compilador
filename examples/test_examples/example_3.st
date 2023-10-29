INT a {5}
INT b {3}
INT c {2}
INT result {0}
INT res1 {0}
INT res2 {0}
INT res3 {0}
INT RESULT {0}

res1 = a + b
res2 = a - c
res3 = res1 - res2
RESULT = res3 / b

result = a + b * a - c / b
PRINT("respuesta de a + b * a - c / b : ", result)
PRINT("respuesta de ((a + b) * (a - c)) / b: ", RESULT)
