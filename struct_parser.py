import ast, sys, logging
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
   #'QUOTE',
    'COMMENT',
    'ID',
    'R_STRING'
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
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
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

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t\n'

# Error handling rule
def t_error(t):
    print(f"Error: Ilegal character '{t.value[0]}' at line {t.lineno}, position {t.lexpos}")
    t.lexer.skip(len(t.value))
    exit()

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
            | modification
            | d_block
            | comments"""
    if p[1]:
        p[0] = [p[1]]

def p_init_list(p):
    """init_list : init_list dict_value
                 | init_list value
                 | init_list sentence
                 | init_list condition
                 | init_list COMMA comments
                 | init_list COMMA
                 | dict_value
                 | value
                 | sentence
                 | condition"""
    if len(p) == 2:
        p[0] = [p[1]]
    elif p[1] and isinstance(p[2],tuple):
        p[1].append(p[2])  #se anaden lineas que se van procesando (sentancia clave-valor)
        p[0] = p[1] #p[0] retorno em .yacc
    else: # corresponde a los casos intermedios 
        p[0] = p[1]

def p_dict_value(p):
    """dict_value : key COLON suite_value"""
    p[0] = ('d_value', p[1], p[3])

def p_suite_value(p):
    """suite_value : condition
                   | sentence
                   | LCURLY_BRACE cplx_value"""
    if len(p) == 3:
        p[0] = p[2]
    else:
        p[0] = p[1]
        
        
def validate_type(p):
    if p[0] == 'int_asig':
        if type(p[3][1]) != int:
            print(f'TypeError in assignment of {p[2][1]}')
            exit()        
    elif p[0] == 'bool_asig':
        if p[3][1]== 'TRUE' or p[3][1] == 'FALSE':
            pass
        else:
            print(f'TypeError in assignment of {p[2][1]}')
            exit()
    elif p[0] == 'string_asig':
        if type(p[3][1]) != str:
            print(f'TypeError in assignment of {p[2][1]}')
            exit()
             
    elif p[0] == 'int_vector_asig' or p[0] == 'bool_vector_asig' or p[0] == 'string_vector_asig':
        if len(p[4]) == p[3][0][1]:
            if p[0] == 'int_vector_asig':
                aux = int
            elif p[0] == 'bool_vector_asig':
                aux = bool
            else:
                aux = str     
            for i in p[4]:       
                if aux != type(i[1]):
                    print(f'TypeError in assignment of value in {p[2][1]}')
                    exit()                    
        else:
            print(f'Error in vector size {p[2][1]}')
            
    elif p[0] == 'modification':
        if symbol_table.get(p[1][1]): 
            if symbol_table.get(p[1][1]) == 'INT':
                aux = int
            elif symbol_table.get(p[1][1]) == 'STRING':
                aux = str
            elif symbol_table.get(p[1][1]) == 'BOOL':
                aux = bool
            else:
                aux = 'DICTIONARY'
                
            if len(p) == 3:
                if type(p[2][1]) != aux:
                    print(f'TypeError in assignment of value in {p[1][1]}')
                    exit()
            else:
                if aux == 'DICTIONARY':
                    pass
                else:
                    if type(p[3][1]) != aux:
                        print(f'TypeError in assignment of value in {p[1][1]}')
                        exit()
        else:
            print(f'Undefined variable')
            exit()
            
    elif p[0] == 'for':
        if not symbol_table.get(p[2][1]):
            print(f'Error in FOR: Undefined variable {p[2][1]}')
            exit()
        
 
                   
def p_assig(p):
    """assig : type id LCURLY_BRACE condition RCURLY_BRACE
             | type id LCURLY_BRACE sentence RCURLY_BRACE
             | type id LCURLY_BRACE value RCURLY_BRACE
             | type id LCURLY_BRACE error RCURLY_BRACE
             | type id LCURLY_BRACE init_list RCURLY_BRACE
             | type id LCURLY_BRACE comments init_list RCURLY_BRACE
             | type id index h_level"""
    if symbol_table.get(p[2][1]): # Variable redefinition
        print(f'Redefinition of variable {p[2][1]}')
        exit()
    else:
        symbol_table[p[2][1]] = p[1][1] # Save id

    if len(p) == 5: #type id index h_level
        p[0] = (p[1][1].lower()+'_vector_asig', p[1], p[2], p[3], *p[4])
    elif len(p) == 6: #type id LCURLY_BRACE condition|sentence|value RCURLY_BRACE
        if isinstance(p[4],lex.LexToken): # Error production
            print('No empty init values')
            exit()
        p[0] = (p[1][1].lower()+'_asig', p[1], p[2], p[4])
    elif len(p) == 7: #type id LCURLY_BRACE comments init_list RCURLY_BRACE
        p[0] = (p[1][1].lower()+'_asig', p[1], p[2], p[5])

    validate_type(p[0])

def p_for(p):
    """for  : FOR id IN id LCURLY_BRACE code RCURLY_BRACE"""
    p[0] = ('for', p[2], p[4], p[6])
    symbol_table[p[2][1]] = 'INT'
    validate_type(p[0])

def p_des_block(p):
    """d_block : if elif else
               | if elif
               | if else
               | if empty"""
    if len(p) == 4: #if elif else
        p[0] = ('d_block', [p[1], *p[2], p[3]])
    elif isinstance(p[2], list): #if elif
        p[0] = ('d_block', [p[1], *p[2]])
    elif isinstance(p[2], tuple): #if else
        p[0] = ('d_block', [p[1], p[2]])
    else: #if
        p[0] = ('d_block', [p[1]])

def p_empty(p): # Auxiliar producction to handle alone if declaration
    """empty :"""
    pass

def p_if(p):
    """if : IF LPAREN condition RPAREN LCURLY_BRACE code RCURLY_BRACE
          | IF LPAREN value RPAREN LCURLY_BRACE code RCURLY_BRACE"""
    if(len(p) == 8): #condition
        p[0] = ('if', p[3], p[6])
    else: #id empty
        p[0] = ('if', p[3], p[7])

def p_elif(p):
    """
    elif : ELIF LPAREN condition RPAREN LCURLY_BRACE code RCURLY_BRACE
         | ELIF LPAREN value RPAREN LCURLY_BRACE code RCURLY_BRACE
         | elif elif
    """
    if len(p) == 8: #ELIF condition LCURLY_BRACE code RCURLY_BRACE
        p[0] = [('elif', p[3], p[6])]
    elif len(p) == 9:
        p[0] = [('elif', p[3], p[7])]
    else: #elif elif
        p[1].extend(p[2])
        p[0] = p[1]

def p_else(p):
    """ else : ELSE LCURLY_BRACE code RCURLY_BRACE """
    p[0] = ('else', p[3])

#Operaciones numéricas (revisar)
def p_sentence(p):
    """sentence : sentence PLUS term
                | sentence MINUS term
                | term"""
    if len(p) > 2:
        if p[2] == '+':
            p[0] = ('add', p[1], p[3])
        else:
            p[0] = ('substract', p[1], p[3])
    else:
        p[0] = p[1]

def p_term_mult(p):
    """term : term TIMES value
            | term DIVIDE value
            | value"""
    if len(p) > 2:
        if p[2] == '*':
            p[0] = ('multiply', p[1], p[3])
        else:
            p[0] = ('divide', p[1], p[3])
    else:
        p[0] = p[1]

def p_condition(p):
    """condition : sentence comp sentence"""
    p[0] = ('condition', p[1], p[2], p[3])

def p_comp(p):
    """comp : EQUAL
            | LESS_EQUAL
            | LESS
            | GREATER
            | GREATER_EQUAL"""
    if p[1] == '==':
        p[0] = ('equal', p[1])
    elif p[1] == '<=':
        p[0] = ('less_equal', p[1])
    elif p[1] == '<':
        p[0] = ('less', p[1])
    elif p[1] == '>':
        p[0] = ('greather', p[1])
    elif p[1] == '>=':
        p[0] = ('greather_equal', p[1])
    
def p_print(p):
    """print : PRINT LPAREN init_list RPAREN"""
    p[0] = ('print', p[3])


def p_high_level(p):
    """h_level : h_level COMMA comments l_level
               | h_level COMMA l_level
               | l_level """
    if len(p) == 2:
        p[0] = [p[1]]
    elif len(p) == 4:
        p[1].append(p[3])
        p[0] = p[1]
    else:
        p[1].append(p[4])
        p[0] = p[1]
                           
def p_lower_level(p):
    """l_level : sentence
               | condition
               | LCURLY_BRACE h_level RCURLY_BRACE
               | LCURLY_BRACE comments h_level RCURLY_BRACE"""
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 4:
        p[0] = p[2]
    else:
        p[0] = p[3]

def p_value(p):
    """value : r_value
             | load_cplx"""
    p[0] = p[1]

def p_modification(p):
    """modification : id ASSINGMENT sentence
                    | id index ASSINGMENT sentence"""
    if len(p) == 4:
        p[0] = ('modification', p[1], p[3])
    else:
        p[0] = ('modification', p[1], p[2], p[4])
        
    validate_type(p[0])

def p_load_cplx(p):
    """load_cplx : id empty
                 | id index"""
    if isinstance(p[2], list): #Matrix or Dicctionary
        p[0] = ('load_cplx', p[1], p[2])
    else: # Simple variable
        p[0] = p[1]

def p_index(p):
    """index : LBRACKET key RBRACKET
             | index LBRACKET key RBRACKET
             | LBRACKET pos RBRACKET
             | index LBRACKET pos RBRACKET
             | LBRACKET id RBRACKET
             | index LBRACKET id RBRACKET"""
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
    print(f'Syntax error at {p.value!r} in line {p.lineno}, position {p.lexpos}, Message: ')

"""
    Zone of parsing 
"""
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

tree = parser.parse(source_code, lexer=lexer, debug=logging.getLogger())

"""
    Zone to define translation an ast to another format
"""

# Function to translate generate AST to python AST 
def translate_to_python(node):
    # Helper to pass struct right values to python right values
    def parse_types(value):
        if isinstance(value, str):
            if value == 'TRUE':
                return True
            elif value == 'FALSE':
                return False
            else:
                return value
        else:
            return value
    
    # Helper function to create nodes of type ast.Constant or ast.Name:load
    # Valid entry nodes of type r_value, key, pos, add, substract, multiply, divide or id 
    def new_value_node(n):
        if n[0] == 'r_value':
            value = parse_types(n[1])
            a_n = ast.Constant(value)
        elif n[0] == 'key' or n[0] == 'pos':
            a_n = ast.Constant(n[1])
        elif n[0] == 'id':
            a_n = ast.Name(n[1], ast.Load())
        elif n[0] == 'condition':
            left_node = new_value_node(n[1])
            right_node = new_value_node(n[3])
            if n[2][0] == 'equal':
                op_node = ast.Eq()
            elif n[2][0] == 'less_equal':
                op_node = ast.LtE()
            elif n[2][0] == 'less':
                op_node = ast.Lt()
            elif n[2][0] == 'greather':
                op_node = ast.Gt()
            elif n[2][0] == 'greather_equal':
                op_node = ast.GtE()
            a_n = ast.Compare(left_node, [op_node], [right_node]) 
        elif n[0] == 'load_cplx':
            a_n = iterative_subs(n[1],n[2])
        else: # add, substract, multiply, divide
            left_node = new_value_node(n[1])
            right_node = new_value_node(n[2])
            if n[0] == 'add':
                op_node = ast.Add()
            elif n[0] == 'substract':
                op_node = ast.Sub()
            elif n[0] == 'multiply':
                op_node = ast.Mult()
            else:
                op_node = ast.Div()
            a_n = ast.BinOp(left_node, op_node, right_node)
        return a_n

    # Helper function to load matrix or dictionary values
    # Need variable name and a list of keys/index
    def iterative_subs(id, list_keys):
        subs = ast.Subscript(new_value_node(id), new_value_node(list_keys[0]), ast.Load())
        for key in list_keys[1:]:
            subs = ast.Subscript(subs, new_value_node(key), ast.Load())
        return subs
    
    # Helper function to create nodes given a list of nodes
    def process_body(list_expr):
        expr_body = [] # Variable to store all sentence in the body expression
        for expr in list_expr: # Iterate over setences inside of for body 
            expr_body.append(translate_to_python(expr))
        return  expr_body
    
    ast_node = None # Node to generate
    if node[0] == 'string_asig' or node[0] == 'int_asig' or node[0] == 'bool_asig': # Case: Incomming node is type asig
        ast_node = ast.Assign([ast.Name(node[2][1],ast.Store())], new_value_node(node[3]))
    elif node[0] == 'string_vector_asig' or node[0] == 'int_vector_asig' or node[0] == 'bool_vector_asig': # Case: Incomming node is type vector_asig
        def go_deep(level):
            list_values = [] #List of args for ast.List
            for item in level:
                if isinstance(item, list): # Append list
                    aux = go_deep(item)
                    list_values.append(ast.List(aux, ctx=ast.Load()))
                else: # Append ast.Name or ast.Constant
                    list_values.append(new_value_node(item))

            return list_values

        ast_node = ast.Assign([ast.Name(node[2][1], ctx=ast.Store())], ast.List(go_deep(node[4]), ctx=ast.Load()))
    elif node[0] == 'dictionary_asig': # Case: Incomming node is type dictionary_asig
        def recursive_ins_dict(n):
            keys = []
            values = []
            for dict_value in n:
                keys.append(new_value_node(dict_value[1]))
                if (isinstance(dict_value[2], list)):
                    values.append(recursive_ins_dict(dict_value[2]))
                else:
                    values.append(new_value_node(dict_value[2]))
        
            return ast.Dict(keys,values)
        ast_node = ast.Assign([ast.Name(node[2][1],ast.Store())], recursive_ins_dict(node[3]))
    elif node[0] == 'modification': # Case: Incomming node is type modification (modification != definition)
        if isinstance(node[2],list): # Dictionary or array/matrix modification
            subs_node = iterative_subs(node[1],node[2])
            subs_node.ctx = ast.Store()

            ast_node =  ast.Assign([subs_node],new_value_node(node[3]))
        else: # Another modification
            ast_node = ast.Assign([ast.Name(node[1][1],ast.Store())], new_value_node(node[2]))
    elif node[0] == 'print': # Case: Incomming node is type print
        l_ast_args = [] #List of args for ast.Call
        for arg in node[1]: # List f_args of print node
            l_ast_args.append(new_value_node(arg))
        ast_node = ast.Expr(ast.Call(ast.Name('print', ast.Load()), l_ast_args, []))
    elif node[0] == 'for': # Case: Incomming node is a for
        target = new_value_node(node[1])
        target.ctx = ast.Store()
        ast_node = ast.For(target,new_value_node(node[2]), process_body(node[3]),[])
        
    elif node[0] == 'd_block':
        root_if = ast.If(new_value_node(node[1][0][1]), process_body(node[1][0][2]), orelse=[])
        current_if = root_if # Attribute orelse must be setting if incomming elif's or an else 
        for if_tuple in node[1][1:]: # Iterate over elif's / else
            current_if.orelse = translate_to_python(if_tuple) # Setting orelse attribute of previos if/elif
            current_if = current_if.orelse[0] # Update pointer to new orelse attribute
        ast_node = root_if
    elif node[0] == 'elif':
        ast_node = [ast.If(new_value_node(node[1]), process_body(node[2]), [])]
    elif node[0] == 'else':
        ast_node = process_body(node[1])

    return ast_node

"""
    Zone to translate 
"""

# Translate our ast to python AST
l_ast_nodes = []
for node in tree:
    l_ast_nodes.append(translate_to_python(node))
ast_root = ast.Module(l_ast_nodes, []) # Creating python AST
ast.fix_missing_locations(ast_root) # Fill up some needed values
exec(compile(ast_root, filename="<ast>", mode="exec"))

"""
    Zone to dumps
"""

# Helper function to save dumps
def dump_to_file(node, dump_file):
    dump_file.write(str(node))
    dump_file.write("\n\n")

# Save parsing dump to a file
with open('dumps/dump_example_struct.txt', 'w') as dump_file:
    for node in tree:
        dump_to_file(node, dump_file)
dump_file.close()

# Save translation dump to a file
with open('dumps/dump_translation.txt','w') as dump_file:
    dump_file.write(ast.dump(ast_root, include_attributes=True, indent=4))   
dump_file.close()
