'''
This file contains the lexer for JUnit (3 and 4)

Used with the appropriate yaccer.

@date Jul 4, 2010
@author Matthew A. Todd

This file is part of Test Parser
by Matthew A. Todd

Test Parser is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Test Parser is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Test Parser.  If not, see <http://www.gnu.org/licenses/>.
'''
import sys

try:
    import ply.lex as lex       #@UnresolvedImport
except:
    sys.exit("Failed to import PLY. JUnit framework requires PLY, so please install.")

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
    from TestParser.Common.Constants import CONSTANTS
    CONSTANTS.logger.warning("JUnitLexer: Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)



lexer = lex.lex()


