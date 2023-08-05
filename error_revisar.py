import re
import ply.lex as lex

# List of simple token names.
simple_tokens = [
   'NUMBER',
   'PLUS',
   'MINUS',
   'TIMES',
   'DIVIDE',
   'LPAREN',
   'RPAREN',
   'RBRACKET',
   'LBRACKET',
   'LCURLY_BRACE',
   'RCURLY_BRACE',
   'EQUAL',
   'ASSINGMENT',
   'LESS_EQUAL',
   'LESS',
   'GREATER',
   'GREATER_EQUAL',
   'COMMA',
   'COLON',
   'QUOTE',
   'COMMENT'
]

# List of token names. Always required.
tokens = simple_tokens

# Regular expression rules for simple tokens
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_COMMENT = r'//.*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_RBRACKET = r'\]'
t_LBRACKET = r'\['
t_LCURLY_BRACE = r'\{'
t_RCURLY_BRACE = r'\}'
t_EQUAL = r'=='
t_ASSINGMENT = r'='
t_LESS_EQUAL = r'<='
t_LESS = r'<'
t_GREATER = r'>'
t_GREATER_EQUAL = r'>='
t_COMMA = r','
t_COLON = r':'
t_QUOTE = r'"'

#Regla para el token de número
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

#Regla para manejar los identificadores
def t_ID(t):
    r'[a-zA-Z_]\w*'
    return t

#Regla para manejar espacios en blanco (ojo- son ignorados)
def t_WHITESPACE(t):
    r'\s+'
    pass

#Regla para manejar los errores léxicos
def t_error(t):
    print(f"Error léxico: Carácter inesperado '{t.value[0]}' en la línea {t.lineno}, posición {t.lexpos + 1}")
    t.lexer.skip(1)

#Constructor de  'lexer'
lexer = lex.lex()

#Prueba del tokenizador
if __name__ == "__main__":
    source_code = """
    INT x = 42
    STR y = "Hello"
    IF x > 10:
        PRINT y
    """
    lexer.input(source_code)
    for token in lexer:
        print(token)
