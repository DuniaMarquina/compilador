import re
import ply.lex as lex
"""
    Definition zone of Tokenizer
        Firts: Define an list with the simple tokens.
        Second: Define an list with the reserved words.
        Third: Define regular expresions to match by simple token or reserved word. 
        Four: Define regular expresions to complex tokens.
"""


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

reserved = {
   'INT': 'INT',
   'BOOL': 'BOOL',
   'TRUE': 'TRUE',
   'FALSE': 'FALSE',
   'STRING': 'STRING',
   'DICTIONARY': 'DICTIONARY',
   'OBJ': 'OBJ',
   'FOR': 'FOR',
   'IN': 'IN',
   'IF': 'IF',
   'ELIF': 'ELIF',
   'ELSE': 'ELSE',
   'PRINT': 'PRINT'
}

# List of token names. Always required.
tokens = simple_tokens + list(reserved.values())

# Regular expression rules for simple tokens
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_COMMENT = r'//.*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_RBRACKET = r'\['
t_LBRACKET = r'\]'
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

# A regular expression rule for floats
def t_FLOAT(t):
    r'\d*\.\d+|\d+\.\d*'
    t.value = float(t.value)    
    return t

# A regular expression rule for ints
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)    
    return t

# A regular expression rule for atributes
def t_ATRIBUTE(t):
    r'\.[a-zA-Z][a-zA-Z0-9]+'
    t.value = t.value[1:]
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
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value) # skip to next line

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print(f"Error: Ilegal character '{t.value[0]}' at line {t.lineno}, position {t.lexpos}")
    t.lexer.skip(len(t.value))

# Build the lexer
lexer = lex.lex()

with open('./examples/error_example.st', 'r') as source:
    f = False
    for line in source:
        # Give the lexer some input
        lexer.input(line)
        # Tokenize
        for tok in lexer:
            print(f'Token |{tok.value}| type: {tok.type}, line: {tok.lineno}, col: {tok.lexpos}')
