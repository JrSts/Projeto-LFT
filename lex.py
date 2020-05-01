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
    'LCCT',
    'RCCT',
    'TRUE',
    'ELSE',
    'PV',
    'ID',
    'COMMA',
    'PONTO',
    'LITERAL_STRING',
	'PONTOPONTO',
    'SETA',
    'IN',
    'DO',
    'EOF',
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
    'COLONCOLON',
    'BREAK_AT',
    'CONTINUE_AT',
    'BREAK',
    'RETURN_AT',
    'SUSPEND',
    'OUT',
    'ELVIS',
    'WHERE',
    'INIT',
    'NOINLINE',
    'VARARG',
    'CROSSINLINE',
)
# Regular expression rules for simple tokens
t_INIT = r'init'
t_NOINLINE = r'noinline'
t_VARARG = r'vararg'
t_CROSSINLINE = r'crossinline'
t_WHERE = r'where'
t_ELVIS = r'\?:'
t_OUT = r'out'
t_SUSPEND = r'suspend'
t_IS = r'is'
t_BREAK = r'break'
t_RETURN_AT = r'return_at'
t_CONTINUE_AT = r'continue_at'
t_BREAK_AT = r'break_at'
t_COLONCOLON = r'::'
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
t_EOF = r'eof'
t_DO = r'do'
t_IN = r'in'
t_SETA = r'-\>'
t_PONTO = r'\.'
t_PONTOPONTO = r'\.\.'
t_COMMA = r','
t_PLUS = r'\+'
t_LCCT = r'\['
t_RCCT = r'\]'
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
t_PV = r';'
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
    r'\n+'
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
fun main (Int argc, palavra argv[] ){
    Int i,j,t
    Char a[n]
    var palavra
    palavra= argv[1]
    for (i=0 in n-1..i++)
    if ((t = fgetc(stdin)) = java.io.EOFException)
        a[i] = t
    a[i] = 0
    for (i= 0 in a[i]!=0..i++)
    for (j= 0 in a[j]!=0..j++)
    if (a[i+j]!=palavra[j])
        if (palavra[j]==0) print("",i)
    
    print("\n")
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
