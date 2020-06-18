# ------------------------------------------------------------
# lex.py
#
# 
# ------------------------------------------------------------
import ply.lex as lex
import ply.yacc as yacc
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
    'VAR',
    'VAL',
    'FUN',
    'WHILE',
    'NULL',
    'RETURN',
    'FOR',
    'FALSE',
    'MOD',
    'INCREMENTO',
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
    'PV',
    'ID',
    'COMMA',
    'LITERAL_STRING',
    'PONTOPONTO',
    'IN',
    'DO',
    'CONTINUE',
    'IDENTIDADE',
    'SEMIDENTIDADE',
    'MODIGUAL',
    'MULTIGUAL',
    'DIVIGUAL',
    'DOISP',
    'AS',
    'NOT_IN',
    'NOT_IS',
    'IS',
    'BREAK',
    'ELVIS',
    'MAISIGUAL',
    'MENOSIGUAL',
)
# Regular expression rules for simple tokens
#t_ARRAY = r'Array'
t_ELVIS = r'\?:'
t_IS = r'is'
t_BREAK = r'break'
t_NOT_IN = r'not_in'
t_NOT_IS = r'not_is'
t_MODIGUAL = r'%='
t_MULTIGUAL = r'\*='
t_DIVIGUAL = r'/='
t_DOISP = r':'
t_AS = r'as'
t_IDENTIDADE = r'==='
t_SEMIDENTIDADE = r'!=='
t_CONTINUE = r'continue'
t_DO = r'do'
t_IN = r'in'
t_PONTOPONTO = r'\.\.'
t_COMMA = r','
t_PLUS = r'\+'
t_INCREMENTO = r'\+\+'
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
t_VAR = r'var'
t_VAL = r'val'
t_FUN = r'fun'
t_WHILE = r'while'
t_NULL = r'null'
t_RETURN = r'return'
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
t_PV = r';'
t_MAISIGUAL=r'\+='
t_MENOSIGUAL=r'-='
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


def t_LITERAL_STRING(t):
    r'\"([^\\\n]|(\\.))*?\"'
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    if (t.value.upper() in tokens):
        t.type = t.value.upper()
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n'
    t.lexer.lineno += len(t.value)  # A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Test it out
data = r'''

fun soma (a:int, b:int): int {
    return a + b
}

fun main(args: Array) {

    var num = 5
    val factorial = 1
    for (i in 1..num) { 
        factorial *= 10
    }
    
    var a = 3
    var b = 6
    var v = true 
    soma(a,c)
    
    if (a > b) { 
        b += a
    }
    else {
        b *= a
    }
    var c = a * b
    print()
    println("Factorial of $num = $factorial")
    
}
 '''
# Give the lexer some input
lexer.input(data)

# Tokenize

# while True:
#     tok = lexer.token()
#     if not tok:
#         break # No more input
#     print(tok)
