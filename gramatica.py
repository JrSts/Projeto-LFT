import ply.lex as lex
import ply.yacc as yacc
from lex import tokens
#from AbstrataClass import abstractmethod

from Visitor import Visitor
import AbstrataClass as ac
import ConcretaClass as cc
import os
import SemanticVisitor as sv
def p_kotlinFile(p):
    ''' kotlinFile : functionDeclaration kotlinFile
				   | functionDeclaration '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = cc.CompoundKotlinFile(p[1], p[2])


def p_functionDeclaration(p):
    ''' functionDeclaration : FUN ID functionValueParameters functionBody
                            | FUN ID functionValueParameters DOISP type functionBody '''
    if len(p) == 5:
        p[0] = cc.SimpleFunctionDeclaration(p[2], p[3], p[4])
    else:
        p[0] = cc.CompoundFunctionDeclaration(p[2], p[3], p[5], p[6])


def p_functionValueParameters(p):
    ''' functionValueParameters : LPAREN parameters RPAREN
                                | LPAREN RPAREN '''
    if len(p) == 3:
        p[0] = cc.SimpleFunctionValueParameters()
    else:
        p[0] = cc.CompoundFunctionValueParameters(p[2])

def p_parameters(p):
    ''' parameters : parameter
                   | parameter COMMA parameters  '''

    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = cc.CompoundParameters(p[1], p[3])

def p_parameter(p):
    ''' parameter : ID DOISP type '''

    p[0] = cc.SimpleParameter(p[1], p[3])


def p_type(p):
    ''' type : parenthesizedType
             | ID '''

    p[0] = p[1]

def p_parenthesizedType(p):
    ''' parenthesizedType : LPAREN type RPAREN '''
    p[0] = cc.ParenthesizedTypeConcrete(p[2])


def p_functionBody(p):
    ''' functionBody : block
                     | ATRIBUICAO expression '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = cc.CompoundFunctionBody(p[2])


def p_statements(p):
    ''' statements : statement
                   | statement statements '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = cc.CompoundStatements(p[1], p[2])


def p_statement(p):
    ''' statement : open_statement
                  | closed_statement
    '''
    p[0] = p[1]

def p_open_statement(p):
    ''' open_statement : IF LPAREN expression RPAREN block
                       | IF LPAREN expression RPAREN statement
                       | IF LPAREN expression RPAREN block ELSE open_statement
                       | IF LPAREN expression RPAREN closed_statement ELSE open_statement
                       | FOR LPAREN genericVariableDeclaration IN expression RPAREN open_statement
                       | WHILE LPAREN expression RPAREN open_statement
                       | DO open_statement WHILE LPAREN expression RPAREN '''

    if len(p) == 6 and isinstance(p[5], ac.Statement):
        p[0] = cc.If_statement(p[3], p[5])
    elif len(p) == 6 and p[1] == 'if':
        p[0] = cc.If_block(p[3], p[5])
    elif len(p) == 6 and p[1] == 'while':
        p[0] = cc.While_Open_statement(p[3], p[5])
    elif len(p) == 8 and isinstance(p[5], ac.Block):
        p[0] = cc.SimpleIf_else(p[3], p[5], p[7])
    elif len(p) == 8:
        p[0] = cc.CompoundIf_else(p[3], p[5], p[7])
    elif p[1] == 'for':
        p[0] = cc.For_Open_statement(p[3], p[5], p[7])
    else:
        p[0] = cc.DoWhile_Open_statement(p[2], p[5])


def p_closed_statement(p):
    '''closed_statement : non_if_statement_block
                        | IF LPAREN expression RPAREN block ELSE block
                        | IF LPAREN expression RPAREN closed_statement ELSE block
                        | IF LPAREN expression RPAREN block ELSE closed_statement
                        | IF LPAREN expression RPAREN closed_statement ELSE closed_statement
                        | FOR LPAREN genericVariableDeclaration IN expression RPAREN closed_statement
                        | WHILE LPAREN expression RPAREN closed_statement
                        | DO closed_statement WHILE LPAREN expression RPAREN '''
    if len(p) == 2:
        p[0] = p[1]
    elif isinstance(p[5], ac.Block) and isinstance(p[7], ac.Block):
        p[0] = cc.If_Blocks_Closed_statement(p[3], p[5], p[7])
    elif isinstance(p[5], ac.Closed_statement) and isinstance(p[7], ac.Block):
        p[0] = cc.If_Mix1_Closed_statement(p[3], p[5], p[7])
    elif isinstance(p[5], ac.Block) and isinstance(p[7], ac.Closed_statement):
        p[0] = cc.If_Mix2_Closed_statement(p[3], p[5], p[7])
    elif isinstance(p[5], ac.Closed_statement) and isinstance(p[7], ac.Closed_statement):
        p[0] = cc.If_Closeds_Closed_statement(p[3], p[5], p[7])
    elif p[1] == 'for':
        p[0] = cc.For_Closed_statement(p[3], p[5], p[7])
    elif p[1] == 'while':
        p[0] = cc.While_Closed_statement(p[3], p[5])
    else:
        p[0] = cc.DoWhile_Closed_statement(p[2], p[5])



def p_non_if_statement(p):
    '''non_if_statement_block : FOR LPAREN genericVariableDeclaration IN expression RPAREN block
                              | WHILE LPAREN expression RPAREN block
                              | DO block WHILE LPAREN expression RPAREN
                              | PV
                              | propertyDeclarationStm
                              | assignment
                              | chamadaDeFuncao
                              | jumpExpression '''
    if p[1] == 'for':
        p[0] = cc.For_Non_if_statement_block(p[3], p[5], p[7])
    elif p[1] == 'while':
        p[0] = cc.While_Non_if_statement_block(p[3], p[5])
    elif p[1] == 'do':
        p[0] = cc.DoWhile_Non_if_statement_block(p[2], p[5])
    else:
        p[0] = p[1]

def p_assignment(p):
    '''assignment : ID ATRIBUICAO expression
                  | ID assignmentAndOperator expression '''
    if p[2] == '=':
        p[0] = cc.AssignmentConcrete(p[1], p[3])
    else:
        p[0] = cc.AssignmentAndOperatorConcrete(p[1], p[2], p[3])

def p_block(p):
    '''block : LCHAVE statements RCHAVE '''
    p[0] = cc.BlockConcrete(p[2])

def p_propertyDeclarationStm(p):
    ''' propertyDeclarationStm : VAR genericVariableDeclaration ATRIBUICAO expression
                               | VAL genericVariableDeclaration ATRIBUICAO expression
'''
    if p[1] == 'var':
        p[0] = cc.PropertyDeclarationStm_Var(p[2], p[4])
    else:
        p[0] = cc.PropertyDeclarationStm_Val(p[2], p[4])

def p_chamadaDeFuncao(p):
    ''' chamadaDeFuncao : ID LPAREN RPAREN
                        | ID LPAREN parametersFunction RPAREN '''
    if len(p) == 4:
        p[0] = cc.SimpleChamadaDeFuncao(p[1])
    else:
        p[0] = cc.CompoundChamadaDeFuncao(p[1], p[3])

def p_genericVariableDeclaration(p):
    ''' genericVariableDeclaration : multiVariableDeclaration
                                   | variableDeclaration '''
    p[0] = p[1]

def p_variableDeclaration(p):
    '''variableDeclaration : ID DOISP type
                           | ID '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = cc.CompoundVariableDeclaration(p[1], p[3])

def p_variableDeclarations(p):
    '''variableDeclarations : variableDeclaration
                            | variableDeclaration COMMA variableDeclarations '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = cc.CompoundVariableDeclarations(p[1], p[3])

def p_multiVariableDeclaration(p):
    ''' multiVariableDeclaration : LPAREN variableDeclarations RPAREN
                                 | LPAREN RPAREN '''
    if len(p) == 3:
        p[0] = cc.SimpleMultiVariableDeclaration()
    else:
        p[0] = cc.CompoundMultiVariableDeclaration(p[2])

def p_parametersFunction(p):
    ''' parametersFunction : primaryExpression
                           | primaryExpression COMMA parametersFunction '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = cc.CompoundParametersFunction(p[1], p[3])


def p_expression(p):
    ''' expression : disjunction '''
    p[0] = p[1]


def p_disjunction(p):
    ''' disjunction : conjunction
                    | disjunction  OR  conjunction'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = cc.CompoundDisjunction(p[1], p[3])


def p_conjunction(p):
    '''conjunction : equality
                   | conjunction  AND  equality'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = cc.CompoundConjunction(p[1], p[3])


def p_equality(p):
    ''' equality : comparison
                 | equality equalityOperator comparison  '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = cc.CompoundEquality(p[1], p[2], p[3])


def p_comparison(p):
    ''' comparison : infixOperation
                   | infixOperation comparisonOperator infixOperation '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = cc.CompoundComparison(p[1], p[2], p[3])


def p_infixOperation(p):
    '''infixOperation : infixOperation inOperator elvisExpression
                      | infixOperation isOperator type
                      | elvisExpression '''
    if len(p) == 2:
        p[0] = p[1]
    elif isinstance(p[2], ac.InOperator):
        p[0] = cc.SimpleInfixOperation(p[1], p[2], p[3])
    else:
        p[0] = cc.CompoundInfixOperation(p[1], p[2], p[3])

def p_elvisExpression(p):
    ''' elvisExpression : rangeExpression
                        | elvisExpression  ELVIS rangeExpression  '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = cc.CompoundElvisExpression(p[1],  p[3])

def p_rangeExpression(p):
    ''' rangeExpression : additiveExpression
						| rangeExpression PONTOPONTO additiveExpression  '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = cc.CompoundRangeExpression(p[1], p[3])


def p_additiveExpression(p):
    ''' additiveExpression : multiplicativeExpression
                           | additiveExpression  additiveOperator  multiplicativeExpression'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = cc.CompoundAdditiveExpression(p[1], p[2], p[3])


def p_multiplicativeExpression(p):
    ''' multiplicativeExpression : asExpression
                                 | multiplicativeExpression  multiplicativeOperator asExpression '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = cc.CompoundMultiplicativeExpression(p[1], p[2], p[3])


def p_asExpression(p):
    ''' asExpression : unaryExpression
                     | unaryExpression asOperator type '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = cc.CompoundAsExpression(p[1], p[2], p[3])


def p_unaryExpression(p):
    ''' unaryExpression : unaryOperator primaryExpression
                        | primaryExpression
                        | primaryExpression postfixUnaryOperator
                      '''
    if len(p) == 2:
        p[0] = p[1]
    elif isinstance(p[1], ac.UnaryOperator):
        p[0] = cc.SimpleUnaryExpressionConcrete(p[1], p[2])
    else:
        p[0] = cc.CompoundUnaryExpressionConcrete(p[1], p[2])

def p_postfixUnaryOperator(p):
    ''' postfixUnaryOperator : INCREMENTO
                             | DECREMENTO '''
    p[0] = p[1]


def p_primaryExpression(p):
    ''' primaryExpression : NULL
                          | TRUE
                          | FALSE
                          | NUMBER
                          | LITERAL_STRING
                          | ID
                          | chamadaDeFuncao
                          | parenthesizedExpression
    '''
    p[0] = p[1]


def p_jumpExpression(p):
    ''' jumpExpression : RETURN expression
                       | CONTINUE
                       | BREAK'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = cc.Return(p[2])

def p_parenthesizedExpression(p):
    ''' parenthesizedExpression : LPAREN expression RPAREN '''
    p[0] = cc.ParenthesizedExpressionConcrete(p[2])



def p_assignmentAndOperator(p):
    ''' assignmentAndOperator :  MAISIGUAL
                               | MENOSIGUAL
                               | MULTIGUAL
                               | DIVIGUAL
                               | MODIGUAL	'''
    if p[1] =='+=':
        p[0] = cc.MAISIGUAL(p[1])
    elif p[1] =='-=':
        p[0] = cc.MENOSIGUAL(p[1])
    elif p[1] == '*=':
        p[0] = cc.MULTIGUAL(p[1])
    elif p[1] == '/=':
        p[0] = cc.DIVIGUAL(p[1])
    elif p[1] == '%=':
        p[0] = cc.MODIGUAL(p[1])
    #p[0] = p[1]

def p_equalityOperator(p):
    ''' equalityOperator : DIFERENTE
                         | IDENTIDADE
                         | IGUALDADE
                         | SEMIDENTIDADE	'''
    if p[1] == '==':
        p[0] = cc.Igualdade(p[1])
    elif p[1] == '===':
        p[0] = cc.Identidade(p[1])
    elif p[1] == '!=':
        p[0] = cc.Diferente(p[1])
    elif p[1] == '!==':
        p[0] = cc.SemIdentidade(p[1])
    #p[0] = p[1]

def p_comparisonOperator(p):
    ''' comparisonOperator : MENOR
                           | MAIOR
                           | MENORIGUAL
                           | MAIORIGUAL '''

    if p[1] == '<':
        p[0] = cc.Menor(p[1])
    elif p[1] == '>':
        p[0] = cc.Maior(p[1])
    elif p[1] == '<=':
        p[0] = cc.MenorIgual(p[1])
    elif p[1] == '>=':
        p[0] = cc.MaiorIgual(p[1])
    #p[0] = p[1]

def p_inOperator(p):
    ''' inOperator : IN
                   | NOT_IN '''
    if p[1] == 'in':
        p[0] = cc.In(p[1])
    elif p[1] == '!in':
        p[0] = cc.NotIn(p[1])

    #p[0] = p[1]
def p_isOperator(p):
    '''isOperator : IS
				  | NOT_IS '''
    if p[1] == 'is':
        p[0] = cc.Is(p[1])
    elif p[1] == '!is':
        p[0] = cc.NotIs(p[1])

    #p[0] = p[1]
def p_additiveOperator(p):
    ''' additiveOperator : PLUS
                         | MINUS	'''
    if p[1] == '/+':
        p[0] = cc.Plus(p[1])
    elif p[1] == '-':
        p[0] = cc.Minus(p[1])
    #p[0] = p[1]

def p_multiplicativeOperator(p):
    ''' multiplicativeOperator : MULT
                               | DIVIDE
                               | MOD '''
    if p[1] == '*':
        p[0] = cc.Mult(p[1])
    elif p[1] == '/':
        p[0] = cc.Mod(p[1])
    elif p[1] == '%':
        p[0] = cc.Divide(p[1])
    #p[0] = p[1]

def p_asOperator(p):
    ''' asOperator : AS
                   | AS asOperator '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = cc.CompoundAsOperator(p[2])

def p_unaryOperator(p):
    ''' unaryOperator : INCREMENTO
                      | DECREMENTO
                      | MINUS
                      | PLUS
                      | NOT'''
    if p[1] == '++':
        p[0] = cc.Incremento(p[1])
    elif p[1] == '--':
        p[0] = cc.Decremento(p[1])
    elif p[1] == '-':
        p[0] = cc.Minus(p[1])
    elif p[1] == '/+':
        p[0] = cc.Plus(p[1])
    elif p[1] == '!':
        p[0] = cc.Not(p[1])

    #p[0] = p[1]
def p_error(p):
    print ("Erro Sintático: ", p)


parser = yacc.yacc()
result = parser.parse(debug=False)
#v = Visitor()
vs = sv.SemanticVisitor()
result.accept(vs)
