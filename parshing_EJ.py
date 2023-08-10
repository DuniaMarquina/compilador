import ply.yacc as yacc
from struct_interpreter import tokens  #'struct_interpreter'

# Reglas de análisis sintáctico
def p_statement_assignment(p):
    'statement : ID ASSINGMENT expression'
    print("Assignment:", p[1], "=", p[3])

def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression'''
    print("Binary Operation:", p[2])
    p[0] = None  # Debes definir la lógica para evaluar la expresión y asignar el resultado a p[0]

def p_expression_number(p):
    'expression : NUMBER'
    print("Number:", p[1])
    p[0] = p[1]

def p_expression_id(p):
    'expression : ID'
    print("Identifier:", p[1])
    p[0] = p[1]

def p_error(p):
    print("Syntax error at", p.value)

# Construir el parser
parser = yacc.yacc()

# Entrada de ejemplo (debes proporcionar tu propio archivo de entrada)
input_text = '''
x = 5
y = 3
result = x + y * 2
'''

# Analizar la entrada
parser.parse(input_text)