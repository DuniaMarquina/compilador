import sys
import ply.yacc as yacc
import ply.lex as lex

import ast

"""
    Definition zone of Tokenizer
        Firts: Define an list with the simple tokens.
        Second: Define an list with the reserved words.
        Third: Define regular expresions to match by simple token or reserved word. 
        Four: Define regular expresions to complex tokens.
"""

entry_args = sys.argv

# List of simple token names.
simple_tokens = [
   'NUMBER',
 #  'PLUS',
 #  'MINUS',
 #  'TIMES',
 #  'DIVIDE',
   'LPAREN',
   'RPAREN',
#   'RBRACKET',
#   'LBRACKET',
   'LCURLY_BRACE',
   'RCURLY_BRACE',
   #'EQUAL',
#   'ASSINGMENT',
#   'LESS_EQUAL',
#   'LESS',
 #  'GREATER',
  # 'GREATER_EQUAL',
   #'COMMA',
   #'COLON',
   #'QUOTE',
#   'COMMENT',
    'ID',
    'R_STRING',
    'NEW_LINE'
]

reserved = {
   'INT': 'INT',
   'BOOL': 'BOOL',
   'TRUE': 'TRUE',
   'FALSE': 'FALSE',
   'STRING': 'STRING',
   #'DICTIONARY': 'DICTIONARY'
#   'FOR': 'FOR',
#   'IN': 'IN',
#   'IF': 'IF',
#   'ELIF': 'ELIF',
#   'ELSE': 'ELSE',
#   'PRINT': 'PRINT'
}

# List of token names. Always required.
tokens = simple_tokens + list(reserved.values())

# Regular expression rules for simple tokens
#t_PLUS    = r'\+'
#t_MINUS   = r'-'
#t_TIMES   = r'\*'
#t_COMMENT = r'//.*'
#t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
#t_RBRACKET = r'\['
#t_LBRACKET = r'\]'
t_LCURLY_BRACE = r'\{'
t_RCURLY_BRACE = r'\}'
"""t_EQUAL = r'=='
t_ASSINGMENT = r'='
t_LESS_EQUAL = r'<='
t_LESS = r'<'
t_GREATER = r'>'
t_GREATER_EQUAL = r'>='"""
#t_COMMA = r','
#t_COLON = r':'
#t_QUOTE = r'"'

# A regular expression rule for floats
"""def t_FLOAT(t):
    r'\d*\.\d+|\d+\.\d*'
    t.value = float(t.value)    
    return t"""

# A regular expression rule for ints
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)    
    return t

def t_R_STRING(t):
    r'"([^\\"]+|\\"|\\\\)*"'
    t.value = t.value[1:-1]
    return t

# A regular expression rule for ids
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value.lower() in reserved:
        print(f"Error: Reserved word '{t.value}' must be in uppercase at line {t.lineno}, position {t.lexpos}")
        t.lexer.skip(len(t.value))
    else:
        t.type = reserved.get(t.value,'ID') # Check for reserved words
    return t

# Define a rule so we can track line numbers
def t_NEW_LINE(t):
    r'\n'
    t.lexer.lineno += len(t.value) # skip to next line
    return t

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print(f"Error: Ilegal character '{t.value[0]}' at line {t.lineno}, position {t.lexpos}")
    t.lexer.skip(len(t.value))

"""
    Definition zone of Paser
"""

symbol_table = dict()

def p_code(p):
    """code : code expr
            | expr """
    print("CODEEEEEEEEEEEEEE", len(p))
    if len(p) > 2:
        p[0] = []
        if isinstance(p[1], list):
            p[0].extend(p[1])
        if isinstance(p[2], list):
            p[0].extend(p[2])
    elif isinstance(p[1], list):
        p[0] = p[1]

def p_expr(p):
    """expr : assig NEW_LINE
            | expr NEW_LINE
            | assig"""
    if len(p) < 2:
        p[0] = p[1]
    else:
        if isinstance(p[1], list):
            p[0] = p[1]
        else:    
            p[0] = [p[1]]

def p_assig(p):
    """assig : type ID LCURLY_BRACE r_value RCURLY_BRACE"""
    p[0] = ('asig', p[1], p[2], p[4])

def p_data_type(p):
    """type : STRING
            | INT
            | BOOL"""
    p[0] = ('type', p[1])

def p_r_value(p):
    """r_value : NUMBER
               | FALSE
               | TRUE
               | R_STRING"""
    p[0] = ('r_value',p[1])

def p_error(p):
    SyntaxError(p)

# Build the lexer
lexer = lex.lex()

# Build the parser
parser = yacc.yacc()

# Reading source code
source_code = '' 
with open('examples/struc_example.st', 'r') as source_file:
    for line in source_file.readlines():
        source_code += line

source_file.close()

def recursive_dump(root, dump_file):
    for exp in root:
        dump_file.write(str(exp))
        dump_file.write("\n\n")

    # Use with ast python module
    #for node in ast.iter_child_nodes(root):
        #dump_file.write(ast.dump(node))
        #dump_file.write("\n\n")

tree = parser.parse(source_code, debug=True, lexer=lexer)

with open('dumps/dump_example_struct.txt', 'w') as dump_file:
    recursive_dump(tree, dump_file)