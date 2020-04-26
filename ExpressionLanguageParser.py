import ply.yacc as yacc
import ply.lex as lex
from ExpressionLanguageLex import *
from ConcretaClass import *
from Visitor import Visitor

def p_exp_soma(p):
    '''exp : exp SOMA exp1
         | exp1'''

    if len(p) == 2:
         p[0]=p[1]
    else:
       p[0] = SomaExp(p[1],p[3])
def p_exp1_vezes(p):
    '''exp1 : exp1 VEZES exp2
            | exp2'''
    if len(p)==2:
        p[0]=p[1] 
    else:
        p[0] = MulExp(p[1] , p[3])
def p_expe2_pot(p):
    '''exp2: exp3 TOP exp2 
            |exp3'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = PotExp(p[1], p[3])
def p_exp3_barra(p):
    '''exp3: call 
            | assign 
            | num
            | id'''
    if isinstance(p[1], CallExp):
        p[0] = CallExp(p[1])
    elif isinstance(p[1], AssignExp):
        p[0] = AssignExp(p[1])
    elif isinstance(p[1], int):
        p[0] = NumExp(p[1])
    else:
        p[0] = IDExp(p[1])
def p_call(p):
    '''call: id LPAREN params RPAREN 
            | num id LPAREN RPAREN '''
    if len(p) == 5:
        p[0] = ParamsCall(p[1], p[3])
    else:
        p[0] = SimplesCall(p[1])
def p_params(p):
    ''' params: exp COMMA params 
            | exp '''
    if len(p) == 2:
        p[0] = SingleParam(p[1])
    elif len(p) == 4:
        p[0] = CompoundParams(p[1], p[3])
def p_assign(p):
    '''assign: id IGUAL exp '''
    p[0] = AssignExp(p[1], p[3])

def p_error(p):
    print("Syntax error in input!")  

parser = yacc.yacc()

result = parser.parse(debug=True)
