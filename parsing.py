import ply.yacc as yacc
import struct_interpreter

tokens = struct_interpreter.tokens

def p_expression(p):
    '''EXPRESSION : ASSIGNMENT EXPRESSION
                  | MODIFICATION EXPRESSION
                  | DEF_FOR EXPRESSION
                  | DEF_DICT EXPRESSION
                  | DEF_VEC EXPRESSION
                  | MOD_DICT EXPRESSION
                  | MOD_VEC EXPRESSION
                  | PRINT EXPRESSION
                  | IF_STAMENT EXPRESSION'''
 

def p_assignment(p):
    '''ASSIGNMENT  : INT ID LCURLY_BRACE literal RCURLY_BRACE
                   | STRING ID LCURLY_BRACE literal RCURLY_BRACE
                   | BOOL LCURLY_BRACE literal RCURLY_BRACE'''
    if isinstance(p[4], int):
        p[0] = ('assingment_int:', p[1], p[2], p[3])
    elif isinstance(p[4], string):
        p[0] = ('assignment_str:', p[1], p[2], p[3])
        if symbol_table [p[2]]:
            print("Error: Redefición de una variable en '%s'" %p.value)
    elif isinstance(p[4], bool):
        p[0] = ('assignment_bool:', p[1], p[2], p[3])


def p_modification(p):
    '''MODIFICATION  : ID EQUAL literal'''
    if symbol_table[p[1]]:
        if isinstance(p[3], int):
            if symbol_table[p[1]].type == int:
                p[0] = ('modification_int:', p[1], p[2], p[3])
            else:
                print("Error: No es de tipo entero en '%s'" %p.value)
        elif isinstance(p[3], string):
            if symbol_table[p[1]].type == string:
                p[0] = ('modification_int:', p[1], p[2], p[3])
            else:
                print("Error: No es de tipo cadena en '%s'" %p.value)
        elif isinstance(p[3], bool):
            if symbol_table[p[1]].type == bool:
                p[0] = ('modification_int:', p[1], p[2], p[3])
            else:
                print("Error: No es de tipo booleano en '%s'" %p.value)
    else:
        print("Error: Identificador desconocido en '%s'" %p.value)


def p_def_dictionary(p):
    '''DEF_DICTIONARY : DICTIONARY ID LBRACE TUPLE RBRACE'''
    if symbol_table[p[2]]:
        print("Error: Redefinición de ID en '%s'" %p.value)
    else:
        p[0] = ('def_dictionary:', p[2], p[4])

def p_tuple(p):
    '''TUPLE : KEY COLON ELEM COMMA TUPLE
             | KEY COLON ELEM'''
    p[0] = ('tuple:', p[1], p[3])


def p_def_vector(p):
    '''DEF_VECTOR : INT ID LBRACKET NUMBER RBRACKET EQUAL LBRACE ELEM_NUMBER RBRACE
                  | BOOL ID LBRACKET NUMBER RBRACKET EQUAL LBRACE ELEM_BOOL RBRACE 
                  | STRING ID LBRACKET NUMBER RBRACKET EQUAL LBRACE ELEM_STRING RBRACE'''
    p[0] =  ('def_vector:', p[1], p[2], p[4], p[8] )

def p_elements(p):
    '''ELEMENTS : ELEMENTS COLON ELEM
                | ELEM'''
    if len(p) > 1:
        p[1].append(p[3])
        p[0] = p[1]
    else:
        p[0] = P[1]


def p_elem(p):
    '''ELEM : NUMBER 
             | TRUE
             | FALSE
             | CADENA'''
    if isinstance(p[1], type(p[0])):
        p[0] = p[1]
    else:
        print("Error: Los elementos no son del mismo tipo '%s'" %p.value)


def p_key(p):
    '''KEY : NUMBER
            | CADENA'''
    p[0] = ('key:', p[1])


def p_mod_complex_type(p):
    '''MOD_COMPLEX_TYPE : ID LBRACKET KEY RBRACKET EQUAL ELEM
                        | ID LBRACKET QUOTE KEY QUOTE RBRACKET EQUAL ELEM'''
    if len(p) > 6:  
        if symbol_table[p[1]]:
            if isinstance(ELEM.value, symbol_table[p[1]].type):
                p[0] = ('mod_vector:', p[1], p[3], p[6])
            else: 
                print("Error: Los elementos no son del mismo tipo '%s'" %p.value)
        else:
            print("Error: ID indefinido '%s'" %p.value)
    else:
        if symbol_table[p[1]]:
            if symbol_table[p[1]][p[4]]:
                if isinstance(ELEM.value, symbol_table[p[1]][p[4]].type):
                    p[0] = ('mod_dict:', p[1], p[4], p[8])
                else: 
                    print("Error: Los elementos no son del mismo tipo '%s'" %p.value)
            else:
                print("Error: clave inválida'%s'" %p.value)
        else:
            print("Error: ID indefinido '%s'" %p.value)


def p_query_complex_type(p):
    '''QUERY_COMPLEX_TYPE  : ID LBRACKET QUOTE KEY QUOTE RBRACKET
                           | ID LBRACKET KEY RBRACKET'''
    if len(p) > 4:
        if symbol_table[p[1]][p[4]]:
            p[0] = ('query_dict:', p[1], p[4])
        else:
            print("Error: La clave no existe'%s'" %p.value)
    else:
        if symbol_table[p[1]][p[4]]:
            p[0] = ('query_vect:', p[1], p[3])
        else:
            print("Error: La clave no existe '%s'" %p.value)


def p_def_for(p):
    '''DEF_FOR  : FOR ID IN ID LCURLY_BRACE EXPRESSION RCURLY_BRACE'''
    p[0] = ('for', p[3], p[5], p[7])

# validar sentencia principal del if, elseif, else
def p_if(p):
    '''IF_STAMENT : IF ID COMP ID LCURLY_BRACE EXPRESSION RCURLY_BRACE
                  | IF ID COMP literal LCURLY_BRACE EXPRESSION RCURLY_BRACE
                  | IF literal COMP ID LCURLY_BRACE EXPRESSION RCURLY_BRACE'''
    if symbol_table[p[2]]:
        if symbol_table[p[4]]:
            if symbol_table[p[2]].type == symbol_table[p[4]].type:
                p[0] = ('if:', p[1], p[2], p[3], p[4])
            else:
                print("Error: Operandos diferentes '%s'" %p.value)
        else:
            print("Error: ID derecho indefinido '%s'" %p.value)
    else:
        print("Error: ID izquierdo indefinido '%s'" %p.value)


def p_elseif(p):
    '''ELIF_STAMENT : ELIF ID COMP ID LCURLY_BRACE EXPRESSION RCURLY_BRACE
                    | ELIF ID COMP literal LCURLY_BRACE EXPRESSION RCURLY_BRACE
                    | ELIF literal COMP ID LCURLY_BRACE EXPRESSION RCURLY_BRACE'''
    if symbol_table[p[2]]:
        if symbol_table[p[4]]:
            if symbol_table[p[2]].type == symbol_table[p[4]].type:
                p[0] = ('elif:', p[1], p[2], p[3], p[4])
            else:
                print("Error: Operandos diferentes '%s'" %p.value)
        else:
            print("Error: ID derecho indefinido '%s'" %p.value)
    else:
        print("Error: ID izquierdo indefinido '%s'" %p.value)


def p_else(p): 
    '''ELSE_STAMENT : ELSE ID COMP ID LCURLY_BRACE EXPRESSION RCURLY_BRACE'''
    p[0] = ('else:', p[1])


def p_comp(p):
    '''COMP : EQUAL
            | LESS_EQUAL
            | LESS
            | GREATER
            | GREATER_EQUAL'''
    if p[0] == '==':
        p[0] = ('equal:', p[1])
    elif p[0] == '>':
        p[0] = ('greater:', p[1])
    elif p[0] == '<':
        p[0] = ('less:', p[1])
    elif p[0] == '>=':
        p[0] = ('greater_equal:', p[1])
    else:
        p[0] = ('less_equal:', p[1])


def p_print(p):
    '''PRINT_STAMENT  : PRINT LPAREN P_VALUE RPAREN'''
    p[0] = ('print:', p[3])


def p_p_value(p):
    '''P_VALUE : ID
               | literal
               | P_VALUE COLON ID
               | P_VALUE COLON literal'''


def p_error(p):
    if p:
        print("Error sintáctico en '%s'" %p.value)
        #print(f"Error: en '{p.value[0]}' at line {p.lineno}, position {p.lexpos}")
    else:
        print("Error sintáctico ...")


parser = yacc.yacc()

while True:
    try:
        s = input('test > ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)

