import ply.lex as lex
import ply.yacc as yacc
from lex import tokens
from AbstrataClass import abstractmethod
import AbstrataClass as ac
import ConcretaClass as cc
import os
from ConcretaClass import Compound2ValueArgument, CompoundCallSuffixConcrete, SimpleCallSuffixConcrete

###########################################################
def p_kotlinFile(p):
    '''kotlinFile : functionDeclaration kotlinFile
				  | functionDeclaration'''
    if len(p) == 2:
        p[0] = cc.SimpleKotlinFile(p[1])
    else:
        p[0] = cc.CompoundKotlinFile(p[1], p[2])
###########################################################

def p_optionalType(p):
    ''' optionalType : DOISP type
                     | '''
    if len(p) == 3:
        p[0] = cc.OptionalType(p[2])
    else:
        p[0] = cc.OptionalType(None)

def p_optionalBlock(p):
    ''' optionalBlock : block
                      | '''
    if len(p) == 2:
        p[0] = cc.OptionalBlock(p[1])
    else:
        p[0] = cc.OptionalBlock(None)

def p_functionDeclaration(p):
    ''' functionDeclaration : FUN simpleIdentifier functionValueParameters optionalType optionalBlock '''
    p[0] = cc.FunctionDeclaration(p[2], p[3], p[4], p[5])
###########################################################
def p_optionalPv(p):
    ''' optionalPv : PV
                   | '''
    if len(p) == 2:
        p[0] = cc.OptionalPv(p[1])
    else:
        p[0]: cc.OptionalPv(None)
###########################################################
def p_genericVariableDeclaration(p):
    ''' genericVariableDeclaration : multiVariableDeclaration
                                   | variableDeclaration '''
    if isinstance(p[1], ac.MultiVariableDeclaration):
        p[0] = cc.MultiVariableDeclaration(p[1])
    else:
        p[0] = cc.VariableDeclaration(p[1])
########################################################################

def p_expression(p):
    ''' expression : disjunction '''
    p[0] = p[1]
###########################################################
def p_varOrVal(p):
    ''' varOrVal : VAR
                 | VAL '''
    if p[0] == 'var':
        p[0] = cc.Var(p[1])
    else:
        p[0] = cc.Val(p[1])

def p_optionalTypeParameters(p):
    ''' optionalTypeParameters : typeParameters
                                | '''
    if len(p) == 2:
        p[0] = cc.OptionalTypeParameters(p[1])
    else:
        p[0]: cc.OptionalTypeParameters(None)
###########################################################
def p_propertyDeclaration(p):
    ''' propertyDeclaration : varOrVal optionalTypeParameters genericVariableDeclaration ATRIBUICAO expression optionalPv'''
    p[0] = cc.PropertyDeclarationConcrete(p[1], p[2], p[3], p[5], p[6])
###########################################################

def p_typeParameters(p):
    ''' typeParameters : MENOR typeParameter typeParametersRecursive optionalCOMMA MAIOR '''
    p[0] = cc.TypeParameters(p[2], p[3], p[4])
###########################################################
def p_typeParametersRecursive(p):
    ''' typeParametersRecursive : COMMA typeParameter
                               | COMMA typeParameter typeParametersRecursive '''
    if len(p) == 3:
        p[0] = cc.SimpleTypeParametersRecursive(p[2])
    else:
        p[0] = cc.SimpleTypeParametersRecursive(p[2], p[3])
###########################################################
def p_optionalCOMMA(p):
    ''' optionalCOMMA : COMMA
                      | '''
    if len(p) == 3:
        p[0] = cc.OptionalCOMMA(p[2])
    else:
        p[0] = cc.OptionalCOMMA(None)
###########################################################
def p_typeParameter(p):
    ''' typeParameter : simpleIdentifier
                    | simpleIdentifier DOISP type'''
    if len(p) == 2:
        p[0] = cc.CompoundTypeParameter(p[1], p[3])
    else:
        p[0] = cc.SimpleTypeParameter(p[1])
###########################################################
def p_functionBody(p):
    ''' functionBody : block
                    | ATRIBUICAO expression '''
    if len(p) == 2:
        p[0] = cc.SimpleFunctionBody(p[1])
    else:
        p[0] = cc.CompoundFunctionBody(p[2])
###########################################################
def p_functionValueParameters(p): 
    '''functionValueParameters : LPAREN functionValueParametersRecursive RPAREN
                                | LPAREN RPAREN '''
    if len(p) == 3:
        p[0] = cc.SimpleFunctionValueParameters()
    else:
        p[0] = cc.CompoundFunctionValueParameters(p[2])

def p_functionValueParametersRecursive(p):
    ''' functionValueParametersRecursive : functionValueParameter optionalCOMMA
                                        | functionValueParameter COMMA functionValueParametersRecursive  '''

    if len(p) == 3:
        p[0] = cc.SimpleFunctionValueParametersRecursive(p[1], p[2])
    else:
        p[0] = cc.CompoundFunctionValueParametersRecursive(p[1], p[3])

#########################################################################
def p_functionValueParameter(p):
    ''' functionValueParameter : parameter ATRIBUICAO expression
                               | parameter '''
    if len(p) == 2:
        p[0] = cc.SimpleFunctionValueParameter(p[1])
    else:
        p[0] = cc.CompoundFunctionValueParameter(p[1], p[3])
########################################################################
def p_variableDeclaration(p):
    '''variableDeclaration :  simpleIdentifier DOISP type
                            | simpleIdentifier '''
    if len(p) == 2:
        p[0] = cc.SimpleVariableDeclaration(p[1])
    else:
        p[0] = cc.CompoundVariableDeclaration(p[1], p[3])
#####################################################################
def p_multiVariableDeclaration(p):
    ''' multiVariableDeclaration : LPAREN multiVariableDeclarationRecursive RPAREN
                                | LPAREN RPAREN'''
    if len(p) == 3:
        p[0] = cc.SimpleMultiVariableDeclaration()
    else:
        p[0] = cc.CompoundMultiVariableDeclaration(p[2])
#####################################################################
def p_multiVariableDeclarationRecursive(p):
    '''multiVariableDeclarationRecursive : variableDeclaration
                                         | variableDeclaration COMMA multiVariableDeclarationRecursive '''
    if len(p) == 2:
        p[0] = cc.SimpleMultiVariableDeclarationRecursive(p[1])
    else:
        p[0] = cc.CompoundMultiVariableDeclarationRecursive(p[1], p[3])
#######################################################################
def p_parameter(p):
    ''' parameter : simpleIdentifier DOISP type '''
    p[0] = cc.ParameterConcrete(p[1], p[3])
######################################################################
def p_type(p):
    ''' type : optionalTypeModifiers optype'''
    p[0] = cc.TypeConcrete(p[1], p[2])

def p_optionalTypeModifiers(p):
    '''optionalTypeModifiers : typeModifiers
                             | '''
    if len(p) == 2:
        p[0] = cc.OptionalTypeModifiersConcrete(p[1])
    else:
        p[0] = cc.OptionalTypeModifiersConcrete(None)
#####################################################################
def p_opType(p):
    '''optype : parenthesizedType
                | functionType
                | userType '''
    p[0] = p[1]
######################################################################
def p_typeModifiers(p) : 
    '''typeModifiers : typeModifier
                    | typeModifier typeModifiers '''
    if len(p) == 2:
        p[0] = cc.SimpleTypeModifiers(p[1])
    else:
        p[0] = cc.CompondTypeModifiers(p[1], p[2])
########################################################################
def p_typeModifier(p):
    ''' typeModifier : SUSPEND '''
    p[0] = p[1]
########################################################################
def p_typeProjectionModifier(p):
    ''' typeProjectionModifier : varianceModifier '''
    p[0] = p[1]
########################################################################
def p_varianceModifier(p): 
    ''' varianceModifier : IN
                        | OUT '''
    if p[1] == 'in':
        p[0] = cc.In(p[1])
    elif p[1] == 'out':
        p[0] = cc.Out(p[1])
########################################################################
def p_userType(p):
    ''' userType : simpleUserType '''
    p[0] = p[1]
########################################################################
def p_simpleUserType(p):
    ''' simpleUserType : simpleIdentifier typeArguments
					   | simpleIdentifier '''
    if len(p) == 2:
        p[0] = cc.SimpleSimpleUserType(p[1])
    else:
        p[0] = cc.CompoundSimpleUserType(p[1], p[2])
########################################################################
def p_typeProjection(p):
    '''typeProjection : typeProjectionModifiers type
                      | type '''
    if len(p) == 2:
        p[0] = cc.SimpleTypeProjection(p[1])
    else:
        p[0] = cc.CompoundTypeProjection(p[1], p[2])
########################################################################
def p_typeProjectionModifiers(p):
    '''typeProjectionModifiers : typeProjection
                                 | typeProjectionModifier typeProjectionModifiers '''
    if len(p) == 2:
        p[0] = cc.SimpleTypeProjectionModifiers(p[1])
    else:
        p[0] = cc.CompoundTypeProjectionModifiers(p[1], p[2])
########################################################################
def p_functionType(p):
    '''functionType : receiverType PONTO functionTypeParameters SETA type
                    | functionTypeParameters SETA type
    '''
    if len(p) == 4:
        p[0] = cc.SimpleFunctionType(p[1], p[3])
    else:
        p[0] = cc.CompoundFunctionType(p[1], p[3], p[5])
########################################################################
def p_optionalParameterOrType(p):
    ''' optionalParameterOrType : parameter
                               | type
                               | '''
    if len(p) == 2 and isinstance(p[1], ac.Parameter):
        p[0] = cc.ParameterConcrete(p[1])
    elif len(p) == 2:
        p[0] = cc.TypeConcrete(p[1])
    else:
        p[0] = cc.TypeConcrete(None)

def p_parameterOrTypeRecursive(p):
    ''' parameterOrTypeRecursive : COMMA optionalParameterOrType
                                 | COMMA optionalParameterOrType parameterOrTypeRecursive
                                 | '''
    if len(p) == 3:
        p[0] = cc.SimpleParameterOrTypeRecursive(p[2])
    else:
        p[0] = cc.CompoundParameterOrTypeRecursive(p[2], p[3])

def p_functionTypeParameters(p):
    '''functionTypeParameters : LPAREN optionalParameterOrType parameterOrTypeRecursive optionalCOMMA RPAREN '''
    p[0] = cc.FunctionTypeParametersConcrete(p[2], p[3], p[4])
########################################################################
def p_parenthesizedType(p):
    '''parenthesizedType : LPAREN type RPAREN '''
    p[0] = cc.ParenthesizedTypeConcrete(p[2])
########################################################################

def p_receiverType(p):
    '''receiverType : typeModifier parenthesizedType '''
    p[0] = cc.ReceiverTypeConcrete(p[1], p[2])
########################################################################

def p_statements(p):
    '''statements : statement
                  | statement statements '''
    if len(p) == 2:
        p[0] = cc.SimpleStatements(p[1])
    else:
        p[0] = cc.CompoundStatements(p[1], p[2])
########################################################################

def p_statement(p):
    '''statement : functionDeclaration
                  | assignment
                  | loopStatement
                  | expression
                  | propertyDeclaration '''
    p[0] = p[1]
########################################################################

def p_controlStructureBody(p):
    '''controlStructureBody : block
                            | statement '''
    p[0] = p[1]
########################################################################

def p_block(p):
    '''block : LCHAVE statements RCHAVE '''
    p[0] = cc.block(p[2])
########################################################################
#este tipo de padrao ocorrem quando um variavel vai para outro tipos de variareis 
def p_loopStatement(p):
    '''loopStatement : forStatement
                     | whileStatement
                     | doWhileStatement '''
    p[0] = p[1]

########################################################################
def p_optionalControlStructureBody(p):
    ''' optionalControlStructureBody : controlStructureBody
                                     | '''
    if len(p) == 2:
        p[0] = cc.ControlStructureBody(p[1])
    else:
        p[0] = cc.ControlStructureBody(None)
########################################################################

def p_forStatement(p):
    ''' forStatement : FOR LPAREN genericVariableDeclaration IN expression RPAREN optionalControlStructureBody '''
    p[0] = cc.ForStatementConcrete(p[3], p[5], p[7])
########################################################################
def p_whileStatement(p):
    ''' whileStatement : WHILE LPAREN expression RPAREN controlStructureBody
                      |  WHILE LPAREN expression RPAREN PV '''

    if p[5] == ';':
        p[0] = cc.WhileStatement_PV(p[3])
    else:
        p[0] = cc.WhileStatement_CBS(p[3], p[5])
########################################################################
def p_doWhileStatement(p):
    ''' doWhileStatement : DO controlStructureBody WHILE LPAREN expression RPAREN
                         | DO WHILE LPAREN expression RPAREN '''
    if len(p) == 6:
        p[0] = cc.SimpleDoWhileStatement(p[4])
    else:
        p[0] = cc.CompoundDoWhileStatement(p[2], p[5])

########################################################################

def p_assignment(p):
    '''assignment : directlyAssignableExpression ATRIBUICAO expression
                  | assignableExpression assignmentAndOperator expression '''
    if p[2] == '=':
        p[0] = cc.AssignmentConcrete(p[1], p[3])
    else:
        p[0] = cc.AssignmentAndOperator(p[1], p[2], p[3])

########################################################################

def p_disjunction(p):
    ''' disjunction : conjunction
                     | conjunction OR disjunction '''
    if len(p) == 2:
        p[0] = cc.SimpleDisjunction(p[1])
    else:
        p[0] = cc.CompoundDisjunction(p[1], p[3])
########################################################################

def p_conjunction(p):
    '''conjunction : equality
                  | equality AND conjunction '''
    if len(p) == 2:
        p[0] = cc.SimpleConjunction(p[1])
    else:
        p[0] = cc.CompoundConjunction(p[1], p[3])
########################################################################

def p_equality(p):
    ''' equality : comparison
                  | comparison equalityOperator equality '''
    if len(p) == 2:
        p[0] = cc.SimpleEquality(p[1])
    else:
        p[0] = cc.CompoundEquality(p[1], p[2], p[3])
########################################################################

def p_comparison(p):
    ''' comparison : infixOperation
                     | infixOperation comparisonOperator infixOperation '''
    if len(p) == 2:
        p[0] = cc.SimpleComparison(p[1])
    else:
        p[0] = cc.CompoundComparison(p[1], p[2], p[3])
########################################################################
def p_infixOperation(p):
    '''infixOperation : elvisExpression infixOperationRecursive
                      | elvisExpression'''
    if len(p) == 2:
        p[0] = cc.SimpleInfixOperation(p[1])
    else:
        p[0] = cc.CompoundInfixOperation(p[1], p[2])
########################################################################
def p_infixOperationRecursive(p):
    ''' infixOperationRecursive : inOrIs elvisOrType
                                | inOrIs elvisOrType infixOperationRecursive '''
    if len(p) == 3:
        p[0] = cc.SimpleInfixOperationRecursive(p[1], p[2])
    if len(p) == 3:
        p[0] = cc.CompoundInfixOperationRecursive(p[1], p[2], p[3])

def p_inOrIs(p):
    '''inOrIs : inOperator
              | isOperator '''
    if isinstance(p[1], ac.InOperator):
        p[0] = cc.InOperator(p[1])
    else:
        p[0] = cc.IsOperator(p[1])

def p_elvisOrType(p):
    ''' elvisOrType : elvisExpression
                    | type '''
    if isinstance(ac.ElvisExpression):
        p[0] = cc.ElvisExpressionConcrete(p[1])
    else:
        p[0] = cc.TypeConcrete(p[1])
########################################################################
def p_elvisExpression(p):
    ''' elvisExpression : infixFunctionCall
                          | infixFunctionCall ELVIS elvisExpression '''
    if len(p) == 2:
        p[0] = cc.SimpleElvisExpression(p[1])
    else:
        p[0] = cc.CompoundElvisExpression(p[1],  p[3])
########################################################################
def p_infixFunctionCall(p):
    '''infixFunctionCall : rangeExpression
                          | rangeExpression simpleIdentifier infixFunctionCall '''
    if len(p) == 2:
        p[0] = cc.SimpleInfixFunctionCall(p[1])
    else:
        p[0] = cc.CompoundInfixFunctionCall(p[1], p[2], p[3])
########################################################################
def p_rangeExpression(p):
    ''' rangeExpression : additiveExpression
						| additiveExpression PONTOPONTO rangeExpression '''
    if len(p) == 2:
        p[0] = cc.SimpleRangeExpression(p[1])
    else:
        p[0] = cc.CompoundRangeExpression(p[1], p[3])
########################################################################
def p_additiveExpression(p):
    ''' additiveExpression : multiplicativeExpression
                             | multiplicativeExpression additiveOperator additiveExpression '''
    if len(p) == 2:
        p[0] = cc.SimpleAdditiveExpression(p[1])
    else:
        p[0] = cc.CompoundAdditiveExpression(p[1], p[2], p[3])
########################################################################
def p_multiplicativeExpression(p):
    ''' multiplicativeExpression : asExpression
                                  | asExpression multiplicativeOperator multiplicativeExpression '''
    if len(p) == 2:
        p[0] = cc.SimpleMultiplicativeExpression(p[1])
    else:
        p[0] = cc.CompoundMultiplicativeExpression(p[1], p[2], p[3])
########################################################################
def p_asExpression(p):
    ''' asExpression : prefixUnaryExpression
                       | prefixUnaryExpression asOperator type '''
    if len(p) == 2:
        p[0] = cc.SimpleAsExpression(p[1])
    else:
        p[0] = cc.CompoundAsExpression(p[1], p[2], p[3])
########################################################################
def p_prefixUnaryExpression(p):
    ''' prefixUnaryExpression : prefixUnaryExpressionRecursive postfixUnaryExpression
                              | postfixUnaryExpression '''
    if len(p) == 2:
        p[0] = cc.SimplePrefixUnaryExpression(p[1])
    else:
        p[0] = cc.CompoundPrefixUnaryExpression(p[1], p[2])
########################################################################
def p_unaryPrefix(p):
    ''' unaryPrefix : label
                    | prefixUnaryOperator '''
    if isinstance(p[1], ac.Lable):
        p[0] = cc.LabelConcrete(p[1])
    else:
        p[0] = cc.PrefixUnaryOperatorConcrete(p[1])
########################################################################
def p_prefixUnaryExpressionRecursive(p):
    ''' prefixUnaryExpressionRecursive : unaryPrefix
                                       | unaryPrefix prefixUnaryExpressionRecursive '''
    if len(p) == 2:
        p[0] = cc.SimplePrefixUnaryExpressionRecursive(p[1])
    else:
        p[0] = cc.CompoundPrefixUnaryExpressionRecursive(p[1], p[2])
####################################################################

def p_label(p):
    ''' label : simpleIdentifier'''
    p[0] = p[1]
########################################################################
def p_postfixUnaryExpressionRecursive(p):
    ''' postfixUnaryExpressionRecursive : postfixUnarySuffix
                                        | postfixUnarySuffix postfixUnaryExpressionRecursive '''
    if len(p) == 2:
        p[0] = cc.SinglePostfixUnaryExpressionRecursive(p[1])
    else:
        p[0] = cc.CompoundPostfixUnaryExpressionRecursive(p[1], p[2])
#####################################################################
def p_postfixUnaryExpression(p):
    ''' postfixUnaryExpression : primaryExpression
                               | primaryExpression postfixUnaryExpressionRecursive '''
    if len(p) == 2:
        p[0] = cc.SimplePostfixUnaryExpression(p[1])
    else:
        p[0] = cc.CompoundPostfixUnaryExpression(p[1], p[2])
########################################################################
def p_postfixUnarySuffix(p):
    ''' postfixUnarySuffix : postfixUnaryOperator
                           | typeArguments
                           | callSuffix
                           | indexingSuffix
                           | navigationSuffix '''
    if isinstance(p[1], ac.PostfixUnaryOperator):
        p[0] = cc.PostfixUnaryOperatorConcrete(p[1])
    elif isinstance(p[1], ac.TypeArguments):
        p[0] = cc.TypeArgumentsConcrete(p[1])
    elif isinstance(p[1], ac.CallSuffix):
        p[0] = cc.CallSuffixConcrete(p[1])
    elif isinstance(p[1], ac.IndexingSuffix):
        p[0] = cc.IndexingSuffixConcrete(p[1])
    elif isinstance(p[1], ac.NavigationSuffix):
        p[0] = cc.NavigationSuffix(p[1])
    # p[0] = p[1]

########################################################################


def p_directlyAssignableExpression(p):
    ''' directlyAssignableExpression : postfixUnaryExpression assignableSuffix
                                       | simpleIdentifier
                                       | parenthesizedDirectlyAssignableExpression '''
    if len(p) == 3:
        p[0] = cc.SimpleDirectlyAssignableExpression(p[1], p[2])
    elif isinstance(p[1], ac.SimpleIdentifier):
        p[0] = cc.SimpleIdentifier(p[1])
    else:
        p[0] = cc.ParenthesizedDirectlyAssignableExpression(p[1])
########################################################################
def p_parenthesizedDirectlyAssignableExpression(p):
    ''' parenthesizedDirectlyAssignableExpression : LPAREN directlyAssignableExpression RPAREN '''
    p[0] = cc.ParenthesizedDirectlyAssignableExpressionConcrete(p[2])
########################################################################
def p_assignableExpression(p):
    ''' assignableExpression : prefixUnaryExpression
                             | parenthesizedAssignableExpression '''
    if isinstance(p[1], ac.PrefixUnaryExpression):
        p[0] = cc.PrefixUnaryExpression(p[1])
    elif isinstance(p[1], ac.ParenthesizedAssignableExpression):
        p[0] = cc.ParenthesizedAssignableExpressionConcrete(p[1])
########################################################################

def p_parenthesizedAssignableExpression(p):
    ''' parenthesizedAssignableExpression : LPAREN assignableExpression RPAREN '''
    p[0] = cc.AssignableExpressionConcrete(p[2])

###########################################################duvida
def p_assignableSuffix(p):
    ''' assignableSuffix : typeArguments
                         | indexingSuffix
                         | navigationSuffix '''
    p[0] = p[1]
    # if isinstance(p[1], ac.TypeArguments):
    #     p[0] = TypeArgumentsConcrete(p[1])
    # elif isinstance(p[1], ac.IndexingSuffix):
    #     p[0] = IndexingSuffix(p[1])
    # if isinstance(p[1], ac.NavigationSuffix):
    #     p[0] = NavigationSuffix(p[1])
########################################################################

def p_indexingSuffix(p):
    ''' indexingSuffix : LCCT indexingSuffixRecursive RCCT
                        | LCCT RCCT'''
    if len(p) == 3:
        p[0] = cc.SimpleIndexingSuffix()
    else:
        p[0] = cc.CompoundIndexingSuffix(p[2])
########################################################################
def p_indexingSuffixRecursive(p):
    ''' indexingSuffixRecursive : expression
				                | expression COMMA indexingSuffixRecursive '''
    if len(p) == 2:
        p[0] = cc.SimpleIndexingSuffixRecursive(p[1])
    else:
        p[0] = cc.CompoundIndexingSuffixRecursive(p[1], p[3])
##########################################################duvida
def p_navigationSuffix(p):
    ''' navigationSuffix : memberAccessOperator simpleIdentifier CLASS
                         | memberAccessOperator parenthesizedExpression CLASS '''
    if isinstance(p[2], ac.SimpleIdentifier):
        p[0] = cc.SimpleIdentifier(p[1], p[2])
    elif isinstance(p[2], ac.ParenthesizedExpression):
        p[0] = cc.SimpleIdentifier(p[1], p[2])
########################################################################
def p_callSuffix(p):
    '''callSuffix : optionalTypeArguments optionalValueArguments annotatedLambda
                  | optionalTypeArguments optionalValueArguments '''

    if len(p) == 4:
        p[0] = CompoundCallSuffixConcrete(p[1], p[2], p[3])
    else:
        p[0] = SimpleCallSuffixConcrete(p[1], p[2])

def p_optionalTypeArguments(p):
    ''' optionalTypeArguments : typeArguments
                              | '''
    if len(p) == 2:
        p[0] = cc.TypeArgumentsConcrete(p[1])
    else:
        p[0] = cc.TypeArgumentsConcrete(None)

def p_optionalValueArguments(p):
    '''optionalValueArguments : valueArguments
                              | '''
    if len(p) == 2:
        p[0] = cc.ValueArgumentsConcrete(p[1])
    else:
        p[0] = cc.ValueArgumentsConcrete(None)
########################################################################
def p_annotatedLambda(p):
    ''' annotatedLambda : lambdaLiteral '''
    p[0] = cc.LambdaLiteralConcrete(p[1])
########################################################################

def p_typeArguments(p):
    ''' typeArguments : MENOR typeArgumentsRecursive MAIOR
                        | MENOR MAIOR'''
    if len(p) == 3:
        p[0] = cc.SimpleTypeArguments()
    else:
        p[0] = cc.CompoundTypeArguments(p[2])
########################################################################

def p_typeArgumentsRecursive(p):
    ''' typeArgumentsRecursive : typeProjection
                               | typeProjection COMMA typeArgumentsRecursive '''
    if len(p) == 2:
        p[0] = cc.SimpleTypeArgumentsRecursive(p[1])
    else:
        p[0] = cc.CompoundTypeArgumentsRecursive(p[1], p[3])

########################################################################
def p_valueArgumentsRecursive(p):
    ''' valueArgumentsRecursive : valueArgument
                                | valueArgument COMMA valueArgumentsRecursive '''
    if len(p) == 2:
        p[0] = cc.SimpleValueArgumentsRecursive(p[1])
    else:
        p[0] = cc.CompoundValueArgumentsRecursive(p[1], p[3])

########################################################################
def p_valueArguments(p):
    '''valueArguments : LPAREN RPAREN
                     | LPAREN valueArgumentsRecursive RPAREN '''
    if len(p) == 3:
        p[0] = cc.SimpleValueArguments()
    else:
        p[0] = cc.CompoundValueArguments(p[2])
########################################################################

def p_valueArgument(p):
    ''' valueArgument : simpleIdentifier ATRIBUICAO MULT expression
                      | simpleIdentifier ATRIBUICAO expression
                      | expression  '''
    if len(p) == 2:
        p[0] = cc.SimpleValueArgument(p[1])
    elif len(p) == 4:
        p[0] = cc.Compound1ValueArgument(p[1], p[3])
    else:
        p[0] = Compound2ValueArgument(p[1], p[4])
########################################################################
def p_primaryExpression(p):
    ''' primaryExpression : parenthesizedExpression
                           | simpleIdentifier
                           | LITERAL_STRING
                           | callableReference
                           | functionLiteral
                           | collectionLiteral
                           | ifExpression
                           | jumpExpression '''
    p[0] = p[1]
    
    # if isinstance(p[1], ParenthesizedExpression):
    #     p[0] = ParenthesizedExpression(p[1])
    # 
    # if isinstance(p[1], SimpleIdentifier):
    #     p[0] = SimpleIdentifier(p[1])
    # 
    # if isinstance(p[1], LITERAL_STRING):
    #     p[0] = LITERAL_STRING(p[1])
    # 
    # if isinstance(p[1], FunctionLiteral):
    #     p[0] = FunctionLiteral(p[1])
    # 
    # if isinstance(p[1], CallableReference):
    #     p[0] = CallableReference(p[1])
    # 
    # if isinstance(p[1], CollectionLiteral):
    #     p[0] = CollectionLiteral(p[1])
    # 
    # if isinstance(p[1], IfExpression):
    #     p[0] = IfExpression(p[1])
    # 
    # if isinstance(p[1], JumpExpression):
    #     p[0] = JumpExpression(p[1])
########################################################################
def p_parenthesizedExpression(p):
    ''' parenthesizedExpression : LPAREN expression RPAREN '''
    p[0] = cc.ParenthesizedExpressionConcrete(p[2])
########################################################################
def p_collectionLiteral(p):
    ''' collectionLiteral : LCCT collectionLiteralRecursive RCCT
                             | LCCT RCCT '''
    if len(p) == 3:
       p[0] = cc.SimpleCollectionLiteral()
    else:
       p[0] = cc.CompoundCollectionLiteral(p[2])
########################################################################
def p_collectionLiteralRecursive(p):
    ''' collectionLiteralRecursive : expression
                                   | expression COMMA collectionLiteralRecursive '''
    if len(p) == 2:
        p[0] = cc.SimpleCollectionLiteralRecursive(p[1])
    else:
        p[0] = cc.CompoundCollectionLiteralRecursive(p[1], p[3])
########################################################################
def p_parametersWithOptionalType(p):
    ''' parametersWithOptionalType : LPAREN parametersWithOptionalTypeRecursive RPAREN
                                    | LPAREN RPAREN '''
    if len(p) == 3:
        p[0] = cc.SimpleParametersWithOptionalType()
    else:
        p[0] = cc.CompoundParametersWithOptionalType(p[2])
########################################################################
def p_parametersWithOptionalTypeRecursive(p):
    ''' parametersWithOptionalTypeRecursive : parameterWithOptionalType
                                            | parameterWithOptionalType COMMA parametersWithOptionalTypeRecursive COMMA '''
    if len(p) == 2:
        p[0] = cc.SimpleParametersWithOptionalTypeRecursive(p[1])
    else:
        p[0] = cc.CompoundParametersWithOptionalTypeRecursive(p[1], p[3])
########################################################################
def p_parameterWithOptionalType(p):
    ''' parameterWithOptionalType : optionalParameterModifiers simpleIdentifier optionalType '''
    p[0] = cc.ParameterWithOptionalTypeConcrete(p[1], p[2], p[3])

def p_optionalParameterModifiers(p):
    ''' optionalParameterModifiers : parameterModifiers
                                    | '''
    if len(p) == 2:
        p[0] = cc.OptionalParameterModifiersConcrete(p[1])
    else:
        p[0] = cc.OptionalParameterModifiersConcrete(None)
########################################################################
def p_parameterModifiers(p):
    ''' parameterModifiers : VARARG
                           | NOINLINE
                           | CROSSINLINE '''
    p[0] = p[1]  
    # if isinstance(p[1], Vararg):
    #     p[0] = Vararg(p[1])
    # if isinstance(p[1], Noinline):
    #     p[0] = Noinline(p[1])
    # if isinstance(p[1], Vararg):
    #     p[0] = Crossinline(p[1])
########################################################################
def p_lambdaLiteral(p):
    ''' lambdaLiteral : RCHAVE optionsLambdaLiteral LCHAVE	'''
    p[0] = cc.LambdaLiteral(p[2])
########################################################################
def p_optionsLambdaLiteral(p):
    ''' optionsLambdaLiteral : statements
                             | lambdaParameters SETA statements
                             | SETA statements'''
    if len(p) == 2:
        p[0] = cc.SimpleOptionsLambdaLiteral(p[1])
    elif len(p) == 3:
        p[0] = cc.Compound1OptionsLambdaLiteral(p[2])
    else :
        p[0] = cc.Compound2OptionsLambdaLiteral(p[1], p[3])
########################################################################
def p_lambdaParameters(p):
    ''' lambdaParameters : lambdaParameter
                         | lambdaParameter COMMA lambdaParameters '''
    if len(p) == 2:
        p[0] = cc.SimpleLambdaParameters(p[1])
    else:
        p[0] = cc.CompoundLambdaParameters(p[1], p[3])
########################################################################
def p_lambdaParameter(p):
    ''' lambdaParameter : variableDeclaration
                        | multiVariableDeclaration optionalType '''

    if len(p) == 1:
        p[0] = cc.VariableDeclarationConcrete(p[1])
    else:
        p[0] = cc.MultiVariableDeclarationConcrete(p[1], p[2])
########################################################################

def p_optionalTypePonto(p):
    ''' optionalTypePonto : type PONTO
                         | '''
    if len(p) == 2:
        p[0] = cc.OptionalTypePontoConcrete(p[1])
    else:
        p[0] = cc.OptionalTypePontoConcrete(None)

def p_optionalTypeConstraints(p):
    ''' optionalTypeConstraints : typeConstraints
                               | '''
    if len(p) == 2:
        p[0] = cc.OptionalTypeConstraintsConcrete(p[1])
    else:
        p[0] = cc.OptionalTypeConstraintsConcrete(None)

def p_optionalFunctionBody(p):
    ''' optionalFunctionBody : functionBody
                             | '''
    if len(p) == 2:
        p[0] = cc.OptionalFunctionBodyConcrete(p[1])
    else:
        p[0] = cc.OptionalFunctionBodyConcrete(None)

def p_anonymousFunction(p):
    ''' anonymousFunction : FUN optionalTypePonto parametersWithOptionalType optionalType optionalTypeConstraints optionalFunctionBody '''
    p[0] = cc.AnonimousFunction(p[2], p[3], p[4], p[5], p[6])

########################################################################
def p_functionLiteral(p):
    ''' functionLiteral : lambdaLiteral
                        | anonymousFunction '''
    p[0] = p[1]
########################################################################
def p_typeConstraints(p):
    ''' typeConstraints : simpleIdentifier DOISP type '''
    p[0] = cc.TypeConstraintConcrete(p[1], p[3])
########################################################################

def p_ifExpression(p):
    ''' ifExpression : IF LPAREN expression RPAREN controlStructureBodyOrPV
                     | IF LPAREN expression RPAREN optionalControlStructureBody optionalPV ELSE controlStructureBodyOrPV '''
    if len(p) == 6:
        p[0] = cc.SimpleIfExpression(p[3], p[5])
    else:
        p[0] = cc.CompoundIfExpression(p[3], p[5], p[6], p[8])

def p_controlStructureBodyOrPV(p):
    ''' controlStructureBodyOrPV : controlStructureBody
                                 | PV'''
    if p[1] == ';':
        p[0] = cc.PV(p[1])
    else:
        p[0] = cc.ControlStructureBody(p[1])



def p_optionalPV(p):
    ''' optionalPV : PV
                  | '''
    if len(p) == 2:
        p[0] = cc.PV(p[1])
    else:
        p[0] = cc.PV(None)

########################################################################

# VERIFICAR Expression 
def p_jumpExpression(p):
    ''' jumpExpression :  RETURN expression
                         | RETURN_AT expression
                         | expression
                         | CONTINUE
                         | CONTINUE_AT
                         | BREAK
                         | BREAK_AT'''
    p[0] = p[1]
    # if isinstance(p[1], ac.Return):
    #     p[0] = cc.ReturnConcrete(p[1], p[2])
    # elif isinstance(p[1], ac.ReturnAt):
    #     p[0] = cc.ReturnAtConcrete(p[1], p[2])
    # elif isinstance(p[1], ac.Expression):
    #     p[0] = cc.ExpressionConcrete(p[1])
    # elif isinstance(p[1], ac.Continue):
    #     p[0] = cc.ContinueConcrete(p[1])
    # elif isinstance(p[1], ac.ContinueAt):
    #     p[0] = cc.ContinueAtConcrete(p[1])
    # elif isinstance(p[1], ac.Break):
    #     p[0] = cc.BreakConcrete(p[1])
    # elif isinstance(p[1], ac.BreakAt):
    #     p[0] = cc.BreakAtConcrete(p[1])
########################################################################
def p_callableReference(p):
    ''' callableReference : optionalReceiverType COLONCOLON simpleIdentifierOrClass '''
    p[0] = cc.CallableReferenceConcrete(p[1], p[3])

def p_optionalReceiverType(p):
    ''' optionalReceiverType : receiverType
                             | '''
    if len(p) == 2:
        p[0] = cc.OptionalReceiverType(p[1])
    else:
        p[0] = cc.OptionalReceiverType(None)

def p_simpleIdentifierOrClass(p):
    ''' simpleIdentifierOrClass : simpleIdentifier
                                | CLASS '''
    if p[1] == 'Class':
        p[0] = cc.ClassConcrete(p[3])
    else:
        p[0] = cc.SimpleIdentifier(p[1])
########################################################################
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
########################################################################
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
########################################################################
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
########################################################################
def p_inOperator(p):
    ''' inOperator : IN
                 | NOT_IN '''
    if p[1] == 'in':
        p[0] = cc.In(p[1])
    elif p[1] == '!in':
        p[0] = cc.NotIn(p[1])
########################################################################
def p_isOperator(p):
    '''isOperator : IS
				| NOT_IS '''
    if p[1] == 'is':
        p[0] = cc.Is(p[1])
    elif p[1] == '!is':
        p[0] = cc.NotIs(p[1])
########################################################################
def p_additiveOperator(p):
    ''' additiveOperator : PLUS
                         | MINUS	'''
    if p[1] == '/+':
        p[0] = cc.Plus(p[1])
    elif p[1] == '-':
        p[0] = cc.Minus(p[1])
########################################################################
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
########################################################################
def p_asOperator(p):
    ''' asOperator : AS
                 | AS asOperator '''
    if len(p) == 2:
        p[0] = cc.SimpleAsOperator(p[1])
    else:
        p[0] = cc.CompoundAsOperator(p[1], p[2])
########################################################################
def p_prefixUnaryOperator(p):
    ''' prefixUnaryOperator : INCREMENTO
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
########################################################################
def p_postfixUnaryOperator(p):
    ''' postfixUnaryOperator : INCREMENTO
                             | DECREMENTO '''
    if p[1] == '++':
        p[0] = cc.Incremento(p[1])
    elif p[1] == '--':
        p[0] = cc.Decremento(p[1])
########################################################################

def p_memberAccessOperator(p):
    ''' memberAccessOperator : safeNav
                             | COLONCOLON '''
    if p[1] == '::':
        p[0] = cc.ColonColon(p[1])
    else:
        p[0] = cc.SafeNavConcrete(p[1])
########################################################################

def p_safeNav(p):
    ''' safeNav : PONTO  '''
    p[0] = cc.Ponto(p[1])
########################################################################

# Identifiers
# olhar tokens
def p_simpleIdentifier(p):
    ''' simpleIdentifier : ID 
                        | CROSSINLINE
                        | IMPORT
                        | INIT
                        | NOINLINE
                        | OUT
                        | VARARG
                        | WHERE
                        | OBJECT
                        | CONST
                        | CONSTRUCTOR
                        | EOF
                        | FALSE
                        | FUNCTION
                        | NULL
                        | NULLABLE
                        | NUMBER
                        | OPERATOR
                        | SMARTCAST
                        | THIS
                        | TRUE
                        | VAL
                        | VAR
                        | WHEN
                        | LONG
                        | ARRAY '''
    p[0] = p[1]

def p_error(p):
    print ("Erro Sintático: ", p)

class AnalisadorSintatico():
    def __init__(self):

        self.arquivo_entrada = "ProgramaKotlin_entrada.txt"  # L�xico
        self.arquivo_saida = "ProgramaKotlin_saida.txt"  # Sint�tico

        self.tem_erro_sintatico = False

        self.arquivo_saida = open(self.arquivo_saida, 'w')

        # Verifica se o arquivo de entrada existe no diretorio em questao
        if not os.path.exists(self.arquivo_entrada):
            print("Arquivo de entrada inexistente")
            self.arquivo_saida.write("Arquivo de entrada inexistente")
            return

        self.arquivo = open(self.arquivo_entrada, 'r')
        self.tokens = self.arquivo.readlines()
        self.arquivo.close()
        self.i = 0
        self.j = 0
        self.linha_atual = ""

    def next_token(self):
        self.i += 1
        self.linha_atual = self.tokens[self.i][self.tokens[self.i].find('\n' | ';') + 2: -1]

    def conteudo_token(self):
        return self.tokens[self.i][: self.tokens[self.i].find('->')]

    # Iniciar(kotlinFile -> (functionDeclaration* EOF))
    def start(self):
        if ("Erro Lexico" in self.tokens[self.i]):
            self.i += 1
        self.FunctionDeclaration()
        if (self.tem_erro_sintatico):
            print("Verifique os erros sintaticos e tente compilar novamente")
            self.arquivo_saida.write("Verifique os erros sintaticos e tente compilar novamente\n")
        else:
            if ("$" in self.tokens[self.i]):
                print("Cadeia de tokens na analise sintatica reconhecida com sucesso")
                self.arquivo_saida.write("Cadeia de tokens reconhecida com sucesso\n")
            else:
                print("Fim de Programa Nao Encontrado!")
                self.arquivo_saida.write("Fim de Programa Nao Encontrado!")
        self.arquivo_saida.close()

    def FunctionDeclaration(self):
        if ("Erro Lexico" in self.tokens[self.i]):
            self.i += 1
        if ('NUMER' in self.tokens[self.i]):
            self.next_token()
        if ('PLUS' in self.tokens[self.i]):
            self.next_token()
        if ('MINUS' in self.tokens[self.i]):
            self.next_token()
        if ('MULT' in self.tokens[self.i]):
            self.next_token()
        if ('DIVIDE' in self.tokens[self.i]):
            self.next_token()
        if ('LPAREN' in self.tokens[self.i]):
            self.next_token()
        if ('RPAREN' in self.tokens[self.i]):
            self.next_token()
        if ('IF' in self.tokens[self.i]):
            self.next_token()
        if ('IMPORT' in self.tokens[self.i]):
            self.next_token()
        if ('NULLABLE' in self.tokens[self.i]):
            self.next_token()
        if ('VAR' in self.tokens[self.i]):
            self.next_token()
        if ('VAL' in self.tokens[self.i]):
            self.next_token()
        if ('FUN' in self.tokens[self.i]):
            self.next_token()
        if ('STRING' in self.tokens[self.i]):
            self.next_token()
        if ('ARRAY' in self.tokens[self.i]):
            self.next_token()
        if ('OBJECT' in self.tokens[self.i]):
            self.next_token()
        if ('THIS' in self.tokens[self.i]):
            self.next_token()
        if ('CHAR' in self.tokens[self.i]):
            self.next_token()
        if ('WHILE' in self.tokens[self.i]):
            self.next_token()
        if ('NULL' in self.tokens[self.i]):
            self.next_token()
        if ('WHEN' in self.tokens[self.i]):
            self.next_token()
        if ('FLOAT' in self.tokens[self.i]):
            self.next_token()
        if ('RETURN' in self.tokens[self.i]):
            self.next_token()
        if ('CONST' in self.tokens[self.i]):
            self.next_token()
        if ('OPERATOR' in self.tokens[self.i]):
            self.next_token()
        if ('INT' in self.tokens[self.i]):
            self.next_token()
        if ('CLASS' in self.tokens[self.i]):
            self.next_token()
        if ('CONSTRUCTOR' in self.tokens[self.i]):
            self.next_token()
        if ('DOUBLE' in self.tokens[self.i]):
            self.next_token()
        if ('SMARTCAST' in self.tokens[self.i]):
            self.next_token()
        if ('BOOLEAN' in self.tokens[self.i]):
            self.next_token()
        if ('FUNCTION' in self.tokens[self.i]):
            self.next_token()
        if ('FOR' in self.tokens[self.i]):
            self.next_token()
        if ('FALSE' in self.tokens[self.i]):
            self.next_token()
        if ('MOD' in self.tokens[self.i]):
            self.next_token()
        if ('PLUSPLUS' in self.tokens[self.i]):
            self.next_token()
        if ('DECREMENTO' in self.tokens[self.i]):
            self.next_token()
        if ('ATRIBUICAO' in self.tokens[self.i]):
            self.next_token()
        if ('IGUALDADE' in self.tokens[self.i]):
            self.next_token()
        if ('DIFERENTE' in self.tokens[self.i]):
            self.next_token()
        if ('NOT' in self.tokens[self.i]):
            self.next_token()
        if ('MENORIGUAL' in self.tokens[self.i]):
            self.next_token()
        if ('MAIORIGUAL' in self.tokens[self.i]):
            self.next_token()
        if ('MAIOR' in self.tokens[self.i]):
            self.next_token()
        if ('MENOR' in self.tokens[self.i]):
            self.next_token()
        if ('AND' in self.tokens[self.i]):
            self.next_token()
        if ('OR' in self.tokens[self.i]):
            self.next_token()
        if ('LCHAVE' in self.tokens[self.i]):
            self.next_token()
        if ('RCHAVE' in self.tokens[self.i]):
            self.next_token()
        if ('TRUE' in self.tokens[self.i]):
            self.next_token()
        if ('ELSE' in self.tokens[self.i]):
            self.next_token()
        if ('IDENT' in self.tokens[self.i]):
            self.next_token()
        if ('DEDENT' in self.tokens[self.i]):
            self.next_token()
        else:
            print("Erro sintatico na linha: " + self.linha_atual + "\n")

parser = yacc.yacc()

result = parser.parse(debug=True)