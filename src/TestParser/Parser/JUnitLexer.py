'''
This file contains the lexer for JUnit (3 and 4)

Used with the appropriate yaccer.

@date Jul 4, 2010
@author Matthew A. Todd
'''


import ply.lex as lex       #@UnresolvedImport

reserved = {
   'at' : 'AT',
}

tokens = [
          'NUMBER',
          'LPAREN',
          'RPAREN',
          'NAME',
          'PERIOD',
          'COLON',
          'NEWLINE',
          'UNUSED_CHAR',
          'DOLLAR',
] + list(reserved.values())

# Regular expression rules for simple tokens
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_PERIOD = r'\.'
t_COLON = r':'
t_NEWLINE = r'\n+'
t_UNUSED_CHAR = r'[<>!,]'
t_DOLLAR = r'\$'


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_NAME(t):
    r'[a-zA-Z_][a-zA-z0-9_]*'
    # Check for reserved words
    if t.value in reserved:
        t.type = reserved[t.value]
    return t

# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'


# Error handling rule
def t_error(t):
    print ("Illegal character '%s'" % t.value[0])   # TODO: log?
    t.lexer.skip(1)



lexer = lex.lex()


