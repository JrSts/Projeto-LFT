# ------------------------------------------------------------
# lex.py
#
# 
# ------------------------------------------------------------
import ply.lex as lex
from builtins import int, print
# List of token names. This is always required
tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'MULT',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'IF',
    'IMPORT',
    'NULLABLE',
    'VAR',
    'VAL',
    'FUN',
    'STRING',
    'ARRAY',
    'OBJECT',
    'THIS',
    'CHAR',
    'WHILE',
    'NULL',
    'WHEN',
    'FLOAT',
    'RETURN',
    'CONST',
    'OPERATOR',
    'INT',
    'CLASS',
    'CONSTRUCTOR',
    'DOUBLE',
    'SMARTCAST',
    'BOOLEAN',
    'FUNCTION',
    'FOR',
    'FALSE',
    'MOD',
    'PLUSPLUS',
    'DECREMENTO',
    'ATRIBUICAO',
    'IGUALDADE',
    'DIFERENTE',
    'NOT',
    'MENORIGUAL',
    'MAIORIGUAL',
    'MAIOR',
    'MENOR',
    'AND',
    'OR',
    'LCHAVE',
    'RCHAVE',
    'TRUE',
    'ELSE',
    'IDENT',
    'DEDENT'
)
# Regular expression rules for simple tokens
t_PLUS = r'\+'
t_PLUSPLUS = r'\++'
t_MINUS = r'-'
t_DECREMENTO = r'--'
t_MOD = r'%'
t_ATRIBUICAO = r'='
t_IGUALDADE = r'=='
t_DIFERENTE = r'!='
t_MULT = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LCHAVE = r'{'
t_RCHAVE = r'}'
t_IF = r'if'
t_IMPORT = r'import'
t_NULLABLE = r'nullable'
t_VAR = r'var'
t_VAL = r'val'
t_FUN = r'fun'
t_STRING = r'String'
t_ARRAY = r'array'
t_OBJECT = r'object'
t_THIS = r'this'
t_CHAR = r'char'
t_WHILE = r'while'
t_NULL = r'null'
t_WHEN = r'when'
t_FLOAT = r'Float'
t_RETURN = r'return'
t_CONST = r'const'
t_OPERATOR = r'operator'
t_INT = r'Int'
t_CLASS = r'class'
t_CONSTRUCTOR = r'constructor'
t_DOUBLE = r'Double'
t_SMARTCAST = r'Smartcast'
t_BOOLEAN = r'Boolean'
t_FUNCTION = r'function'
t_FOR = r'for'
t_FALSE = r'false'
t_MAIOR = r'>'
t_MENOR = r'<'
t_MAIORIGUAL = r'>='
t_MENORIGUAL = r'<='
t_OR = r'\|\|'
t_AND = r'&&'
t_NOT = r'!'
t_TRUE = r'true'
t_ELSE = r'else'

#def contador(t):
 #   i , contador = 0
  #  while (t[i] == ' '):
   #     i+=1
   # lista[] = i
   # return i

#def t_IDENT(t):

# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t
# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'
# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
# Build the lexer
lexer = lex.lex()
# Test it out
data = '''
if
 '''
# Give the lexer some input
lexer.input(data)
# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break # No more input
    print(tok)
