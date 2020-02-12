import ply.yacc as yacc
import ply.lex as lex
from ExpressionLanguageLex import tokens

def p_exp_soma(p):
    '''exp : exp SOMA exp1
         | exp1'''

def p_exp1_vezes(p):
    '''exp1 : exp1 VEZES exp2
            | exp2'''
def p_expe2_pot(p):
    '''exp2: exp3 TOP exp2 
            |exp3'''
def p_exp3_barra(p):
    '''exp3: call 
            | assign 
            | num
            | id'''
def p_call(p):
    '''call: id LPAREN params RPAREN 
            | num id LPAREN RPAREN '''
def p_params(p):
    ''' params: id COMMA params 
            | id '''
def p_assign(p):
    '''assign: id IGUAL exp '''
parser = yacc.yacc()

result = parser.parse(debug=True)
