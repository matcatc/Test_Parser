'''
This file contains the PLY.yacc parser to parse the tokens from JUnitLexer.

Used for parsing JUnit 3 and 4's output

@date Jul 4, 2010
@author Matthew A. Todd
'''

import ply.yacc as yacc             #@UnresolvedImport

class InvalidLine(Exception):
    '''
    For when the yaccer reads in a line it doesn't know how to handle.
    '''
    def __init__(self, line=None):
        self.line = line
    def __str__(self):
        if self.line is None:
            return "Invalid Line"
        else:
            return "Invalid Line: #%s" % self.line


# Get the token map from the lexer.  This is required.
from .JUnitLexer import tokens           #@UnusedImport

def p_start(p):
    '''
    start : status_line
            | exception_line
            | detail_line
    '''
    p[0] = p[1]
    

def p_status_line_junit4(p):
    'status_line : NUMBER RPAREN name LPAREN name RPAREN end'
    p[0] = ('status_line', {'testName' : p[3],
                            'suiteName' : p[5]})

def p_status_line_junit3(p):
    '''
    status_line : NUMBER RPAREN name LPAREN name RPAREN exception_line
    '''
    exception_lineData = p[7][1]
    p[0] = ('status_line_junit3', {'testName' : p[3],
                                    'suiteName' : p[5],
                                    'exception' : exception_lineData['exception'],
                                    'info' : exception_lineData['info']})

# TODO: return other relevant exception data (if applicable)
def p_exception_line(p):
    '''
    exception_line : exception COLON string end
                    | exception COLON end
                    | exception end
    '''
    if len(p) == 5:
        p[0] = ('exception_line', {'exception': p[1],
                                   'info' : p[3]})
    else:
        p[0] = ('exception_line', {'exception' : p[1],
                                   'info' : None})
    
    

# TODO: should exception be more precise?
# can it?
def p_exception(p):
    '''
    exception : name PERIOD name PERIOD name
    '''
    p[0] = p[1] + p[2] + p[3] + p[4] + p[5]



def p_detail_line(p):
    '''
    detail_line : AT class LPAREN filename COLON NUMBER RPAREN end
    '''
    p[0] = ('detail_line', {'class' : p[2],
                            'filename' : p[4],
                            'line' : p[6]})

# sometimes there is not COLON and NUMBER in detail line
def p_detail_line2(p):
    '''
    detail_line : AT class LPAREN filename RPAREN end
    '''
    p[0] = ('detail_line', {'class' : p[2],
                            'filename' : p[4],
                            'line' : None})


def p_class_rec(p):
    '''
    class : class PERIOD name
            | class DOLLAR NUMBER
    '''
    p[0] = p[1] + p[2] + str(p[3])

def p_class_bc(p):
    '''
    class : name
    '''
    p[0] = p[1]


def p_filename(p):
    '''
    filename : name PERIOD name
    '''
    p[0] = p[1] + p[2] + p[3]

def p_empty(p):
    'empty :'
    pass

# end of line (sometimes '\n' will be stripped...)
def p_end(p):
    '''
    end : empty
        | NEWLINE
    '''
    p[0] = p[1]

# b/c AT has higher precedence over NAME, if we have a name
# somewhere that is 'at', it will end up as AT instead of NAME
def p_name(p):
    '''
    name : NAME
        | AT
    '''
    p[0] = p[1]

def p_string(p):
    '''
    string : string char
            | char
    '''
    if len(p) == 3:
        p[0] = p[1] + ' ' + str(p[2])
    else:
        p[0] = p[1]

def p_char(p):
    '''
    char : COLON
        | PERIOD
        | NUMBER
        | UNUSED_CHAR
        | DOLLAR
        | name
    '''
    p[0] = p[1]

# Error rule for syntax errors
def p_error(p):
    ## Although this is bad style
    ## (using exceptions like this) it tremendulously simplifies
    ## the code, as we'd otherwise have to come up with rules
    ## that cover everything that isn't valid.
#    print("Syntax error in input!", p)
    if p is not None:
        raise InvalidLine(p)

# Build the parser
yaccer = yacc.yacc()




###### example:
#
#f = open('/home/matcat/Desktop/test_out')
#for line in f.read().split('\n'):
#    try:
#        print(parser.parse(line))
#    except InvalidLine:
#        pass

