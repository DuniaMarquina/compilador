import sys, logging
import ply.yacc as yacc
import ply.lex as lex

"""
    Config logger to yacc.yacc().parse
"""

logging.basicConfig(
    level=logging.DEBUG, # Flag
    filename='dumps/parser_debug.txt', # File to store debug messages
    filemode="w", # Mode to open debug file
    format="%(message)s" # Format of message report
)

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
   'RBRACKET',
   'LBRACKET',
   'LCURLY_BRACE',
   'RCURLY_BRACE',
   #'EQUAL',
   'ASSINGMENT',
#   'LESS_EQUAL',
#   'LESS',
 #  'GREATER',
  # 'GREATER_EQUAL',
   'COMMA',
   'COLON',
   #'QUOTE',
    'COMMENT',
    'ID',
    'R_STRING',
    #'NEW_LINE'
]

reserved = {
   'INT': 'INT',
   'BOOL': 'BOOL',
   'TRUE': 'TRUE',
   'FALSE': 'FALSE',
   'STRING': 'STRING',
   'DICTIONARY': 'DICTIONARY',
   'FOR': 'FOR',
   'IN': 'IN',
#   'IF': 'IF',
#   'ELIF': 'ELIF',
#   'ELSE': 'ELSE',
   'PRINT': 'PRINT'
}

# List of token names. Always required.
tokens = simple_tokens + list(reserved.values())

# Regular expression rules for simple tokens
#t_PLUS    = r'\+'
#t_MINUS   = r'-'
#t_TIMES   = r'\*'
t_COMMENT = r'//.*'
#t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LCURLY_BRACE = r'\{'
t_RCURLY_BRACE = r'\}'
#t_EQUAL = r'=='
t_ASSINGMENT = r'='
#t_LESS_EQUAL = r'<='
#t_LESS = r'<'
#t_GREATER = r'>'
#t_GREATER_EQUAL = r'>='
t_COMMA = r','
t_COLON = r':'
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
# def t_NEW_LINE(t):
#     r'\n'
#     t.lexer.lineno += len(t.value) # skip to next line
#     return t

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t\n'

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
    if len(p) > 2:
        p[0] = []
        if isinstance(p[1], list):
            p[0].extend(p[1])
        if isinstance(p[2], list):
            p[0].extend(p[2])
    elif isinstance(p[1], list):
        p[0] = p[1]

def p_expr(p):
    """expr : assig comments
            | assig
            | for comments
            | for
            | print comments
            | print
            | modification comments
            | modification"""
    p[0] = [p[1]]

def p_init_list(p):
    """init_list : init_list dict_value
                 | init_list arg
                 | init_list COMMA comments
                 | init_list COMMA
                 | dict_value
                 | arg"""
    if len(p) == 2:
        p[0] = [p[1]]
    elif p[1] and isinstance(p[2],tuple):
        p[1].append(p[2])
        p[0] = p[1]
    else:
        p[0] = p[1]

def p_dict_value(p):
    """dict_value : key COLON suite_value"""
    if len(p) == 5:
        p[0] = ('d_value', p[2], p[4])
    else:
        p[0] = ('d_value', p[1], p[3])

def p_suite_value(p):
    """suite_value : r_value
                   | LCURLY_BRACE cplx_value"""
    if len(p) == 3:
        p[0] = p[2]
    else:
        p[0] = p[1]

def p_assig(p):
    """assig : type id LCURLY_BRACE value RCURLY_BRACE
             | type id LCURLY_BRACE init_list RCURLY_BRACE
             | type id LCURLY_BRACE comments init_list RCURLY_BRACE
             | type id index h_level"""
    if len(p) == 5: #type id index h_level
        p[0] = (p[1][1].lower()+'_vector_asig', p[1], p[2], p[3], p[4])
    elif len(p) == 6:
        if isinstance(p[4], tuple): #type id LCURLY_BRACE value RCURLY_BRACE
            p[0] = (p[1][1].lower()+'_asig', p[1], p[2], p[4])
        elif isinstance(p[4],list): #type id LCURLY_BRACE init_list RCURLY_BRACE
            p[0] = (p[1][1].lower()+'_asig', p[1], p[2], p[4])
    elif len(p) == 7: #type id LCURLY_BRACE comments init_list RCURLY_BRACE
        p[0] = (p[1][1].lower()+'_asig', p[1], p[2], p[5])

def p_for(p):
    """for  : FOR id IN id LCURLY_BRACE code RCURLY_BRACE"""
    p[0] = ('for', p[2], p[4], p[6])

def p_print(p):
    """print : PRINT LPAREN init_list RPAREN"""
    p[0] = ('print:', p[3])

def p_high_level(p):
    """h_level : h_level COMMA l_level 
               | l_level """
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[1].append(p[3])
        p[0] = p[1]
                           
def p_lower_level(p):
    """l_level : value
               | LCURLY_BRACE h_level RCURLY_BRACE"""
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = ('level',p[2])

def p_value(p):
    """value : r_value
             | id"""
    p[0] = p[1]

def p_modification(p):
    """modification : id ASSINGMENT r_value
                    | id index ASSINGMENT r_value"""
    if len(p) == 4:
        p[0] = ('modification', p[1], p[3])
    else:
        p[0] = ('modification', p[1], p[2], p[4])

def p_index(p):
    """index : LBRACKET key RBRACKET
             | index LBRACKET key RBRACKET
             | LBRACKET pos RBRACKET
             | index LBRACKET pos RBRACKET"""
    if len(p) == 4:
        p[0] = [p[2]]
    else:
        p[1].append(p[3])
        p[0] = p[1]

def p_key(p):
    """key : R_STRING"""
    p[0] = ('key', p[1])

def p_pos(p):
    """ pos : NUMBER"""
    p[0] = ('pos', p[1])

def p_arg(p):
    """arg : r_value
           | id"""
    p[0] = ('f_arg', p[1])

def p_id(p):
    """id : ID"""
    p[0] = ('id', p[1])

def p_data_type(p):
    """type : STRING
            | INT
            | BOOL
            | DICTIONARY"""
    p[0] = ('type', p[1])

def p_r_value(p):
    """r_value : NUMBER
               | FALSE
               | TRUE
               | R_STRING
               | NUMBER comments
               | FALSE comments
               | TRUE comments
               | R_STRING comments"""
    p[0] = ('r_value',p[1])

def p_cplx_value(p):
    """cplx_value : init_list RCURLY_BRACE
                  | init_list RCURLY_BRACE comments
                  | init_list"""
    p[0] = p[1]

def p_commets(p):
    """comments : comments COMMENT
                | COMMENT"""

def p_error(p):
    SyntaxError(p)

# Build the lexer
lexer = lex.lex()
# Build the parser
parser = yacc.yacc()

# Reading source code
source_file = entry_args[1] if len(entry_args) > 1 else 'examples/struc_example.st' 
source_code = '' # string to store all source file
with open(source_file, 'r') as source_file:
    for line in source_file.readlines(): # Reading all source file
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

tree = parser.parse(source_code, lexer=lexer, debug=logging.getLogger())
with open('dumps/dump_example_struct.txt', 'w') as dump_file:
    recursive_dump(tree, dump_file)
