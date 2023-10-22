INT a {1}
INT b {10}
STRING message_true {"Verdadero!"}
STRING message_false {"Falso!"}

IF (a < b) {
    PRINT(message_true)
}
ELIF (a == b)
{
    BOOL b {FALSE}
}
ELIF (a > b)
{
    BOOL b {TRUE}
}
ELSE {
    PRINT(message_false)
}