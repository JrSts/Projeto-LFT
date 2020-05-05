import ply.lex as lex
import ply.yacc as yacc
from lex import tokens
import ConcretaClass
import AbstrataClass
import os

###########################################################
def p_kotlinFile(p):
    '''kotlinFile : functionDeclaration kotlinFile
					| functionDeclaration'''
    if len(p) == 2:
        p[0] = SimpleKotlinFile(p[1])
    else:
        p[0] = CompoundKotlinFile(p[1], p[2])
###########################################################

def p_functionDeclaration(p):
    ''' functionDeclaration : FUN simpleIdentifier functionValueParameters fd2 fd3 '''
    p[0] = FunctionDeclaration(p[2], p[3], p[4], p[5], p[6])

# def p_fd1(p):
#     '''fd1 : simpleIdentifier
#            | '''
#     p[0] = Fd1(p[1])

def p_fd2(p):     
    '''fd2 : DOISP type   
            | '''    
    if len(p) == 3:        
        p[0] = Fd2(p[2])
    else:         
        p[0]: Fd2(None)

def p_fd3(p):     
    '''fd3 : block   
            | '''    
    if len(p) == 2:        
        p[0] = Fd3(p[1])     
    else:         
        p[0] = Fd3(None)

###########################################################

def p_propertyDeclaration(p):
    ''' propertyDeclaration : pd1 pd2 pd3 ATRIBUICAO expression pd4'''
    p[0] = PropertyDeclaration(p[2], p[3], p[5], p[6])

def p_pd1(p):
    ''' pd1 : VAR
           | VAL '''
    p[0] = p[1]

def p_pd2(p):
    ''' pd2 : typeParameters
            | '''
    if len(p) == 2:
        p[0] = Pd2(p[1])
    else:
        p[0]: Pd2(None)

def p_pd3(p):
    ''' pd3 : multiVariableDeclaration
            | variableDeclaration '''
    p[0] = p[1]

def p_pd4(p):
    ''' pd4 : PV
            | '''
    if len(p) == 2:
        p[0] = Pd4(p[1])
    else:
        p[0]: Pd4(None)

def p_typeParameters(p):
    ''' typeParameters : MENOR typeParameter tps2 MAIOR
                        | MENOR typeParameter tps1 tps2 MAIOR '''

    if len(p) == 5:
        p[0] = SimpleTypeParameters(p[2], p[3])
    else:
        p[0] = CmpoundTypeParameters(p[2], p[3], p[4])

def p_tps1(p):
        ''' tps1 : COMMA typeParameter
                | COMMA typeParameter tps1'''
        if len(p) == 3:
            p[0] = TypeParameters(p[2])
        else:
            p[0] = TypeParameters(p[2], p[3])

def p_tps2(p):
    ''' tps2 : COMMA
            | '''
    if len(p) == 3:
        p[0] = Tps2(p[2])
    else:
        p[0] = Tps2(None)

def p_typeParameter(p):
    ''' typeParameter : simpleIdentifier
                    | simpleIdentifier DOISP type'''
    if len(p) == 2:
        p[0] = TypeParameter(p[1], p[3])
    else:
        p[0] = p[1]

def p_functionBody(p):
    ''' functionBody : block
                    | ATRIBUICAO expression '''
    if len(p) == 2:
        p[0] = SimpleFunctionBody(p[1])
    else:
         p[0] = CompoundFunctionBody(p[2])

###########################################################

def p_functionValueParameters(p): 
    '''functionValueParameters : LPAREN fvps RPAREN
                                | LPAREN RPAREN '''
    if len(p) == 3:
        p[0] = SimpleFunctionValueParameters()
    else:
        p[0] = CompoundFunctionValueParameters(p[2])

def p_fvps(p):
    ''' fvps : functionValueParameter
                | functionValueParameter COMMA fvps 
                | functionValueParameter fvps '''
    if len(p) == 2:
        p[0] = SimpleFvps(p[1])
    elif len(p) == 3:
        p[0] = CompoundFvps(p[1], p[2])
    else:
        p[0] = COMMAFvps(p[1], p[3])

#########################################################################
def p_functionValueParameter(p):
    ''' functionValueParameter : parameter ATRIBUICAO expression
                                  | parameter '''
    if len(p) == 2:
        p[0] = SimpleFunctionValueParameter(p[1])
    else:
        p[0] = CompoundFunctionValeuParameter(p[1], p[3])
########################################################################
def p_variableDeclaration(p):
    '''variableDeclaration :  simpleIdentifier DOISP type
                            | simpleIdentifier '''

    if len(p) == 2:
        p[0] = SimpleVariableDeclaration(p[1])
    else:
        p[0] = CompoundVariableDeclaration(p[1], p[3])
#####################################################################
def p_multiVariableDeclaration(p):
    ''' multiVariableDeclaration : LPAREN mvd RPAREN
                                | LPAREN RPAREN'''
    if len(p) == 3:
        p[0] = SimpleMultiVariableDeclaration()
    else:
        p[0] = CompoundMultiVariableDeclaration(p[2])
#####################################################################

def p_mvd(p):
    '''mvd : variableDeclaration
            |  variableDeclaration COMMA mvd'''
    if len(p) == 2:
        p[0] = SimpleMvd(p[1])
    else:
        p[0] = CompoundMvd(p[1], p[3])
#######################################################################

def p_parameter(p):

    ''' parameter : simpleIdentifier DOISP type '''
    p[0] = Parameter(p[1], p[3])
######################################################################
def p_type(p):
    '''type : typeModifiers optype
              | optype '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = CompoundType(p[1], p[2])
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
        p[0] = SimpleTypeModifiers(p[1])
    else:
        p[0] = CompondTypeModifiers(p[1], p[2])
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
        p[0] = VarianceModifier(p[1])
    elif p[1] == 'out':
        p[0] = VarianceModifier(p[1])

########################################################################

def p_userType(p):
    ''' userType : simpleUserType '''
    p[0] = p[1]
########################################################################

def p_simpleUserType(p):
    ''' simpleUserType : simpleIdentifier typeArguments
					 | simpleIdentifier '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = SimpleUserType(p[1], p[2])
########################################################################

def p_typeProjection(p):
    '''typeProjection : typeProjectionModifiers type
                      | type '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = CompoundTypeProjection(p[1], p[2])
########################################################################

def p_typeProjectionModifiers(p):
    '''typeProjectionModifiers : typeProjection
                                 | typeProjectionModifier typeProjectionModifiers '''
    if len(p) == 2:
        p[0] = SimpleTypeProjectionModifiers(p[1])
    else:
        p[0] = CompoundTypeProjectionModifiers(p[1], p[2])
########################################################################

def p_functionType(p):
    '''functionType : receiverType PONTO functionTypeParameters SETA type
                    | functionTypeParameters SETA type
    '''
    if len(p) == 4:
        p[0] = SimpleFunctionType(p[1], p[3])
    else:
        p[0] = CompoundFunctionType(p[1], p[3], p[5])
########################################################################

def p_functionTypeParameters(p):
    '''functionTypeParameters : functionTypeParameters_p
                            | functionTypeParameters_t'''

def p_functionTypeParameters_p(p):
    '''functionTypeParameters_p : LPAREN parameter ftp RPAREN
                                 | LPAREN parameter RPAREN '''
    if len(p) == 4:
        p[0] = SimpleFunctionTypeParameters_p(p[2])
    else:
        p[0] = CompoundFunctionTypeParameters_p(p[2], p[3])
########################################################################

def p_functionTypeParameters_t(p):
    '''functionTypeParameters_t : LPAREN type RPAREN
                                 | LPAREN type ftp RPAREN '''
    if len(p) == 4:
        p[0] = SimpleFunctionTypeParameters_t(p[2])
    else:
        p[0] = CompoundFunctionTypeParameters_t(p[2], p[3])
########################################################################

def p_ftp(p) :
    ''' ftp : COMMA parameter
		    | COMMA type
		    | COMMA parameter ftp
		    | COMMA type ftp'''

    if isinstance(p[2], Parameter):
        p[0] = Parameter(p[2])
    elif isinstance(p[2], type):
        p[0] = type(p[2])
########################################################################

def p_parenthesizedType(p):
    '''parenthesizedType : LPAREN type RPAREN '''
    p[0] = ParenthesizedType(p[2])
########################################################################

def p_receiverType(p):
    '''receiverType : typeModifier rt '''
    p[0] = receiverType(p[1], p[2])
########################################################################

def p_rt(p):
    '''rt : parenthesizedType'''
    p[0] = rt(p[1])
########################################################################

def p_statements(p):
    '''statements : statement
                  | statement statements '''
    if len(p) == 2:
        p[0] = SimpleStatements(p[1])
    else:
        p[0] = CompoundStatements(p[1], p[2])
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
                          | statement'''
    p[0] = p[1]
########################################################################

def p_block(p):
    '''block : LCHAVE statements RCHAVE '''
    p[0] = block(p[2])
########################################################################
#este tipo de padrao ocorrem quando um variavel vai para outro tipos de variareis 
def p_loopStatement(p):
    '''loopStatement : forStatement_MD
                    | forStatement_VD
                    | whileStatement
                    | doWhileStatement '''
    p[0] = p[1]
########################################################################

def p_forStatement_MD(p):
    '''forStatement_MD : FOR LPAREN multiVariableDeclaration IN expression RPAREN controlStructureBody
                      | FOR LPAREN multiVariableDeclaration IN expression RPAREN'''
    if len(p) == 7:
        p[0] = SimpleForStatement_MD(p[3], p[5])
    else:
        p[0] = CompoundForStatement_MD(p[3], p[5], p[7])
########################################################################

def p_forStatement_VD(p):
    '''forStatement_VD :  FOR LPAREN variableDeclaration IN expression RPAREN controlStructureBody
                      | FOR LPAREN variableDeclaration IN expression RPAREN '''
    if len(p) == 7:
        p[0] = SimpleForStatement_VD(p[3], p[5])
    else:
        p[0] = CompoundForStatement_VD(p[3], p[5], p[7])

########################################################################
def p_whileStatement(p):
    ''' whileStatement : WHILE LPAREN expression RPAREN controlStructureBody
                      |  WHILE LPAREN expression RPAREN PV '''

    if p[5] == ';':
        p[0] = WhileStatement_PV(p[3])
    else:
        p[0] = WhileStatement_CBS(p[3], p[5])
########################################################################
def p_doWhileStatement(p):
    ''' doWhileStatement : DO controlStructureBody WHILE LPAREN expression RPAREN
                          | DO WHILE LPAREN expression RPAREN '''
    if len(p) == 6:
        p[0] = SimpleDoWhileStatement(p[4])
    else:
        p[0] = CompoundDoWhileStatement(p[2], p[5])

########################################################################

def p_assignment(p):
    '''assignment : directlyAssignableExpression IGUALDADE expression
                  | assignableExpression assignmentAndOperator expression '''
    if p[2] == '=':
        p[0] = CallIgualdade(p[1], p[3])
    else:
         p[0] = CallAssignmentAndOperator(p[1], p[2], p[3])
########################################################################

def p_expression(p):
    ''' expression : disjunction '''
    p[0] = p[1]
########################################################################

def p_disjunction(p):
    ''' disjunction : conjunction
                     | conjunction OR disjunction '''
    if len(p) == 2:
        p[0] = SimpleDisjunction(p[1])
    else:
        p[0] = CompoundDisjunction(p[1], p[3])
########################################################################

def p_conjunction(p):
    '''conjunction : equality
                  | equality AND conjunction '''
    if len(p) == 2:
        p[0] = SimpleConjunction(p[1])
    else:
        p[0] = CompoundConjunction(p[1], p[3])
########################################################################

def p_equality(p):
    ''' equality : comparison
                  | comparison equalityOperator equality '''
    if len(p) == 2:
        p[0] = SimpleEquality(p[1])
    else:
        p[0] = CompoundEquality(p[1], p[2], p[3])
########################################################################

def p_comparison(p):
    ''' comparison : infixOperation
                     | infixOperation comparisonOperator infixOperation '''
    if len(p) == 2:
        p[0] = SimpleComparison(p[1])
    else:
        p[0] = CompoundComparison(p[1], p[2], p[3])
########################################################################

def p_infixOperation(p):
    '''infixOperation : elvisExpression io 
                        | elvisExpression'''
    if len(p) == 2:
        p[0] = SimpleInfixOperation(p[1])
    else:
        p[0] = CompoundInfixOperation(p[1], p[2])
########################################################################

def p_io(p):
    '''io : inOperator elvisExpression
            | inOperator elvisExpression io
            | isOperator type 
            | isOperator type io '''
    if len(p) == 3 and isinstance(p[1], IsOperator):
        p[0] = IsOperator(p[1],p[2])
    elif len(p) == 3 and isinstance(p[1], InOperator):
        p[0] = InOperator(p[1],p[2])
    elif len(p) == 4 and isinstance(p[1], IsOperator):
        p[0] = IsOperator(p[1],p[2], p[3])
    elif len(p) == 4 and isinstance(p[1], InOperator):
        p[0] = InOperator(p[1],p[2], p[3])
########################################################################

def p_elvisExpression(p):
    ''' elvisExpression : infixFunctionCall
                          | infixFunctionCall ELVIS elvisExpression '''
    if len(p) == 2:
        SimpleElvisExpression(p[1])
    else:
        CompoundElvisExpression(p[1],  p[3])
########################################################################

def p_infixFunctionCall(p):
    '''infixFunctionCall : rangeExpression
                          | rangeExpression simpleIdentifier infixFunctionCall '''
    if len(p) == 2:
        SimpleInfixFunctionCall(p[1])
    else:
        CompoundInfixFunctionCall(p[1], p[2], p[3])
########################################################################

def p_rangeExpression(p):
    ''' rangeExpression : additiveExpression
						| additiveExpression PONTOPONTO rangeExpression '''
    if len(p) == 2:
        SimpleRangeExpression(p[1])
    else:
        CompoundRangeExpression(p[1], p[3])
########################################################################

def p_additiveExpression(p):
    ''' additiveExpression : multiplicativeExpression
                             | multiplicativeExpression additiveOperator additiveExpression '''
    if len(p) == 2:
        SimpleAdditiveExpression(p[1])
    else:
        CompoundAdditiveExpression(p[1], p[2], p[3])
########################################################################

def p_multiplicativeExpression(p):
    ''' multiplicativeExpression : asExpression
                                  | asExpression multiplicativeOperator multiplicativeExpression '''
    if len(p) == 2:
        SimpleMultiplicativeExpression(p[1])
    else:
        CompoundMultiplicativeExpression(p[1], p[2], p[3])
########################################################################

def p_asExpression(p):
    ''' asExpression : prefixUnaryExpression
                       | prefixUnaryExpression asOperator type '''
    if len(p) == 2:
        SimpleAsExpression(p[1])
    else:
        CompoundAsExpression(p[1], p[2], p[3])
########################################################################

def p_prefixUnaryExpression(p):
    ''' prefixUnaryExpression : preue postfixUnaryExpression 
                                | postfixUnaryExpression '''
    if len(p) == 2:
        p[0] = SimplePrefixUnaryExpression(p[1])
    else:
        p[0] = CompoundPrefixUnaryExpression(p[1], p[2])
########################################################################

def p_preue(p):
    ''' preue : unaryPrefix
            | unaryPrefix preue '''
    if len(p) == 2:
        SimplePreue(p[1])
    else:
        CompoundPreue(p[1], p[2])

####################################################################

def p_unaryPrefix(p):
    ''' unaryPrefix : label
                    | prefixUnaryOperator '''
    p[0] = p[1]
########################################################################      

def p_label(p):
    ''' label : simpleIdentifier'''
    p[0] = p[1]
########################################################################

def p_postfixUnaryExpression(p):
    ''' postfixUnaryExpression : primaryExpression
                               | primaryExpression posue '''
    if len(p) == 2:
        SimplePostfixUnaryExpression(p[1])
    else:
        CompoundPostfixUnaryExpression(p[1], p[2])
########################################################################

def p_posue(p):
    ''' posue : postfixUnarySuffix
              | postfixUnarySuffix posue '''
    if len(p) == 2:
        SinglePosue(p[1])
    else:
        CompoundPosue(p[1], p[2])
########################################################################

def p_postfixUnarySuffix(p):
    ''' postfixUnarySuffix : postfixUnaryOperator
                           | typeArguments
                           | callSuffix
                           | indexingSuffix
                           | navigationSuffix '''
    p[0] = p[1]  
    # if isinstance(p[1], CallPostfixUnaryOperator):
    #     p[0] = CallPostfixUnaryOperator(p[1])
    # elif isinstance(p[1], CallTypeArguments):
    #     p[0] = CallTypeArguments(p[1])
    # elif isinstance(p[1], CallCallSuffix):
    #     p[0] = CallCallSuffix(p[1])
    # elif isinstance(p[1], CallNavigationSuffix):
    #     p[0] = CallNavigationSuffix(p[1])
    # elif isinstance(p[1], CallIndexingSuffix):
    #     p[0] = CallIndexingSuffix(p[1])
########################################################################
        
def p_directlyAssignableExpression(p):
    ''' directlyAssignableExpression : postfixUnaryExpression assignableSuffix
                                       | simpleIdentifier
                                       | parenthesizedDirectlyAssignableExpression '''
    if len(p) == 3:
        p[0] = SimpleDirectlyAssignableExpression(p[1], p[2])
    elif isinstance(p[1], CallSimpleIdentifier):
        p[0] = CallSimpleIdentifier(p[1])
    else:
        p[0] = parenthesizedDirectlyAssignableExpression(p[1])
########################################################################


def p_parenthesizedDirectlyAssignableExpression(p):
    ''' parenthesizedDirectlyAssignableExpression : LPAREN directlyAssignableExpression RPAREN '''
    p[0] = ParenthesizedDirectlyAssignableExpression(p[2])

########################################################################

def p_assignableExpression(p):
    ''' assignableExpression : prefixUnaryExpression
                              | parenthesizedAssignableExpression '''
    if isinstance(p[1], CallPrefixUnaryExpression):
        p[0] = CallPrefixUnaryExpression(p[1])
    elif isinstance(p[1], CallParenthesizedAssignableExpression):
        p[0] = CallParenthesizedAssignableExpression(p[1])
########################################################################

def p_parenthesizedAssignableExpression(p):
    ''' parenthesizedAssignableExpression : LPAREN assignableExpression RPAREN '''
    p[0] = ParenthesizedAssignableExpression(p[2])

###########################################################duvida
def p_assignableSuffix(p):
    ''' assignableSuffix : typeArguments
                         | indexingSuffix
                         | navigationSuffix '''
    p[0] = p[1]
    # if isinstance(p[1], CallTypeArguments):
    #     p[0] = CallTypeArguments(p[1])
    # elif isinstance(p[1], CallIndexingSuffix):
    #     p[0] = CallIndexingSuffix(p[1])
    # if isinstance(p[1], CallNavigationSuffix):
    #     p[0] = CallNavigationSuffix(p[1])
########################################################################

def p_indexingSuffix(p):
    ''' indexingSuffix : LCCT isuf RCCT 
                        | LCCT RCCT'''
    if len(p) == 3:
        p[0] = SimpleIndexingSuffix()
    else:
        p[0] = CompoundIndexingSuffix(p[2])
########################################################################

def p_isuf(p):
    ''' isuf : expression
				| expression COMMA isuf '''
    if len(p) == 2:
        SimpleIsuf(p[1])
    else:
        CompoundIsuf(p[1], p[3])

##########################################################duvida
def p_navigationSuffix(p):
    ''' navigationSuffix : memberAccessOperator simpleIdentifier CLASS
                         | memberAccessOperator parenthesizedExpression CLASS '''
    if isinstance(p[2], CallSimpleIdentifier):
        p[0] = CallSimpleIdentifier(p[1], p[2])
    elif isinstance(p[2], CallParenthesizedExpression):
        p[0] = CallSimpleIdentifier(p[1], p[2])
########################################################################

def p_callSuffix(p):
    '''callSuffix : typeArguments valueArguments annotatedLambda
                     | valueArguments annotatedLambda
                     | typeArguments  annotatedLambda
                     | annotatedLambda
                     | typeArguments valueArguments
                     | valueArguments '''
    if isinstance(p[2], CallValueArguments3) and len(p) == 4:
        p[0] = CallValueArguments3(p[1], p[2], p[3])
    elif isinstance(p[2], CallValueArguments2)  and len(p) == 3:
        p[0] = CallValueArguments2(p[1], p[2])
    elif isinstance(p[1], CallValueArguments2)  and len(p) == 3:
        p[0] = CallValueArguments2(p[1], p[2])
    elif isinstance(p[2], CallValueArguments1)  and len(p) == 2:
        p[0] = CallValueArguments1(p[1])
    elif isinstance(p[1], CallAnnotatedLambda)  and len(p) == 2:
        p[0] = CallAnnotatedLambda(p[1])
    elif isinstance(p[2], CallAnnotatedLambda2)  and len(p) == 3:
        p[0] = CallAnnotatedLambda2(p[1], p[2])
########################################################################

def p_annotatedLambda(p):
    ''' annotatedLambda : lambdaLiteral '''
    p[0] = p[1]
########################################################################

def p_typeArguments(p):
    ''' typeArguments : MENOR ta MAIOR
                        | MENOR MAIOR'''
    if len(p) == 3:
        p[0] = SimpleTypeArguments()
    else:
        p[0] = CompoundTypeArguments(p[2])
########################################################################

def p_ta(p):
    ''' ta : typeProjection
            | typeProjection COMMA ta '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = CompoundTa(p[1], p[3])
########################################################################

def p_valueArguments(p):
    '''valueArguments : LPAREN RPAREN
                     | LPAREN vas RPAREN '''
    if len(p) == 3:
        p[0] = SimpleValueArguments()
    else:
        p[0] = CompoundValueArguments(p[2])
########################################################################

def p_vas(p):
    ''' vas : valueArgument
             | valueArgument COMMA vas '''
    if len(p) == 2:
        p[0] = SimpleVas(p[1])
    else:
        p[0] = CompoundVas(p[1], p[3])
########################################################################

def p_valueArgument(p):
    ''' valueArgument : simpleIdentifier IGUALDADE MULT expression
                      | simpleIdentifier IGUALDADE expression
                      | expression  '''
    if len(p) == 2:
        p[0] = SimpleValueArgument(p[1])
    elif len(p) == 4:
        p[0] = Compound1ValueArgument(p[1], p[3])
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
    
    # if isinstance(p[1], CallParenthesizedExpression):
    #     p[0] = CallParenthesizedExpression(p[1])
    # 
    # if isinstance(p[1], CallSimpleIdentifier):
    #     p[0] = CallSimpleIdentifier(p[1])
    # 
    # if isinstance(p[1], CallLITERAL_STRING):
    #     p[0] = CallLITERAL_STRING(p[1])
    # 
    # if isinstance(p[1], CallFunctionLiteral):
    #     p[0] = CallFunctionLiteral(p[1])
    # 
    # if isinstance(p[1], CallCallableReference):
    #     p[0] = CallCallableReference(p[1])
    # 
    # if isinstance(p[1], CallCollectionLiteral):
    #     p[0] = CallCollectionLiteral(p[1])
    # 
    # if isinstance(p[1], CallIfExpression):
    #     p[0] = CallIfExpression(p[1])
    # 
    # if isinstance(p[1], CallJumpExpression):
    #     p[0] = CallJumpExpression(p[1])
########################################################################

def p_parenthesizedExpression(p):
    ''' parenthesizedExpression : LPAREN expression RPAREN '''
    p[0] = ParenthesizedExpression(p[2])
########################################################################

def p_collectionLiteral(p):
    ''' collectionLiteral : LCCT cl RCCT
                             | LCCT RCCT '''
    if len(p) == 3:
       p[0]= SimpleCollectionLiteral()
    else:
       p[0]= CompoundCollectionLiteral(p[2])
########################################################################

def p_cl(p):
    ''' cl : expression
            | expression COMMA cl '''
    if len(p) == 2:
        p[0] = SimpleCl(p[1])
    else:
        p[0] = CompoundCl(p[1], p[2])
########################################################################


def p_parametersWithOptionalType(p):
    ''' parametersWithOptionalType : LPAREN pwot RPAREN
                                    | LPAREN RPAREN '''
    if len(p) == 3:
        p[0] = SimpleParametersWithOptionalType()
    else:
         p[0] = CompoundParametersWithOptionalType(p[2])
########################################################################
    
def p_pwot(p):
    ''' pwot : parameterWithOptionalType 
            | parameterWithOptionalType COMMA pwot COMMA '''
    if len(p) == 2:
        p[0] = SimplePwot(p[1])
    else:
        p[0] = CompoundPwot(p[1], p[3])
########################################################################

def p_parameterWithOptionalType(p):
    ''' parameterWithOptionalType : parameterModifiers simpleIdentifier DOISP type
                                    | simpleIdentifier DOISP type
                                    | parameterModifiers simpleIdentifier
                                    | simpleIdentifier '''
    if len(p) == 2:
        p[0] = Simple1ParameterWithOptionalType(p[1])
    elif len(p) == 3:
        p[0] = Simple2ParameterWithOptionalType(p[1], p[2])
    elif len(p) == 4:
        p[0] = Compound1ParameterWithOptionalType(p[1], p[3])
    elif len(p) == 5:
        p[0] = Compound2ParameterWithOptionalType(p[1], p[2], p[4])   
########################################################################

def p_parameterModifiers(p):
    ''' parameterModifiers :  VARARG
                            | NOINLINE
                            | CROSSINLINE '''
    p[0] = p[1]  
    # if isinstance(p[1], CallVararg):
    #     p[0] = CallVararg(p[1])
    # if isinstance(p[1], CallNoinline):
    #     p[0] = CallNoinline(p[1])
    # if isinstance(p[1], CallVararg):
    #     p[0] = CallCrossinline(p[1])
########################################################################
    
def p_lambdaLiteral(p):
    ''' lambdaLiteral : RCHAVE ll LCHAVE	'''
    p[0] = LambdaLiteral(p[2])
########################################################################

def p_ll(p):
    ''' ll : statements
            | lambdaParameters SETA statements
            | SETA statements'''
    if len(p) == 2:
        p[0] = SimpleLl(p[1])
    elif len(p) == 3:
        p[0] = Compound1Ll(p[2])
    else :
        p[0] = Compound2Ll(p[1], p[3])
########################################################################
        
def p_lambdaParameters(p):
    ''' lambdaParameters : lambdaParameter
                          | lambdaParameter COMMA lambdaParameters '''
    if len(p) == 2:
        p[0] = SimpleLambdaParameters(p[1])
    else :
        p[0] = CompoundLambdaParameters(p[1], p[3])
########################################################################
        
def p_lambdaParameter(p):
    ''' lambdaParameter : variableDeclaration
                     | multiVariableDeclaration DOISP type
                     | multiVariableDeclaration '''
    if isinstance(p[1], CallVariableDeclaration):
        p[0] = CallVariableDeclaration(p[1])
    elif len(p) == 2:
        p[0] = CallMultiVariableDeclaration(p[1])
    elif len(p) == 4:
        p[0] = CompoundLambdaParameter(p[1], p[2])
########################################################################

def p_anonymousFunction(p):
    ''' anonymousFunction : FUN type PONTO parametersWithOptionalType DOISP type typeConstraint functionBody
                          | FUN parametersWithOptionalType DOISP type typeConstraint functionBody
                          | FUN type PONTO parametersWithOptionalType typeConstraint functionBody
                          | FUN type PONTO parametersWithOptionalType DOISP type functionBody                     
                          | FUN type PONTO parametersWithOptionalType DOISP type typeConstraint
                          | FUN parametersWithOptionalType typeConstraint functionBody
                          | FUN parametersWithOptionalType DOISP type functionBody
                          | FUN parametersWithOptionalType DOISP type typeConstraint
                          | FUN type PONTO parametersWithOptionalType functionBody
                          | FUN type PONTO parametersWithOptionalType typeConstraint 
                          | FUN type PONTO parametersWithOptionalType DOISP type
                          | FUN parametersWithOptionalType functionBody
                          | FUN parametersWithOptionalType typeConstraint
                          | FUN type PONTO parametersWithOptionalType 
                          | FUN parametersWithOptionalType '''
########################################################################

def p_functionLiteral(p):
    ''' functionLiteral : lambdaLiteral
                        | anonymousFunction '''
    p[0] = p[1]
########################################################################

def p_typeConstraint(p):
    ''' typeConstraint : simpleIdentifier DOISP type '''
    p[0] = TypeConstraint(p[1], p[3])
########################################################################

def p_ifExpression(p):
    ''' ifExpression : IF LPAREN expression RPAREN if1 if2 ELSE if1 if2 '''

def p_if1(p):
    ''' if1 : controlStructureBody
            | '''

def p_if2(p):
    ''' if2 : PV
            | '''

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
    # if isinstance(p[1], CallReturn):
    #     p[0] = CallReturn(p[1], p[2])
    # elif isinstance(p[1], CallReturnAt):
    #     p[0] = CallReturnAt(p[1], p[2])
    # elif isinstance(p[1], CallExpression):
    #     p[0] = CallExpression(p[1])
    # elif isinstance(p[1], CallContinue):
    #     p[0] = CallContinue(p[1])
    # elif isinstance(p[1], CallContinueAt):
    #     p[0] = CallContinueAt(p[1])
    # elif isinstance(p[1], CallBreak):
    #     p[0] = CallBreak(p[1])
    # elif isinstance(p[1], CallBreakAt):
    #     p[0] = CallBreakAt(p[1])
########################################################################        

def p_callableReference_SI(p):
    ''' callableReference : receiverType COLONCOLON simpleIdentifier
                         | COLONCOLON simpleIdentifier '''
    if len(p) == 4:
        p[0] = SimpleCallableReference_SI(p[3])
    else:
        p[0] = CompoundCallableReference_SI(p[1], p[4])
########################################################################        
        
def p_callableReference_Class(p):
    ''' callableReference : receiverType COLONCOLON CLASS
                         | COLONCOLON CLASS'''
    if len(p) == 4:
        p[0] = SimpleCallableReference_Class(p[3])
    else:
        p[0] = CompoundCallableReference_Class(p[1], p[4])
########################################################################

def p_assignmentAndOperator(p):
    ''' assignmentAndOperator :  MAISIGUAL
                               | MENOSIGUAL
                               | MULTIGUAL
                               | DIVIGUAL
                               | MODIGUAL	'''
    if  p[1] =='+=':
        P[0] = assignmentAndOperator(p[1])
    elif p[1] =='-=':
        P[0] = assignmentAndOperator(p[1])
    elif p[1] == '*=':
        P[0] = assignmentAndOperator(p[1])
    elif p[1] == '/=':
        P[0] = assignmentAndOperator(p[1])
    elif p[1] == '%=':
        P[0] = assignmentAndOperator(p[1])

########################################################################

def p_equalityOperator(p):
    ''' equalityOperator : DIFERENTE
                         | IDENTIDADE
                         | IGUALDADE
                         | SEMIDENTIDADE	'''
    if p[1] == '==':
        P[0] = equalityOperator(p[1])
    elif p[1] == '===':
        P[0] = equalityOperator(p[1])
    elif p[1] == '!=':
        P[0] = equalityOperator(p[1])
    elif p[1] == '!==':
        P[0] = equalityOperator(p[1])
########################################################################

def p_comparisonOperator(p):
    ''' comparisonOperator : MENOR
                           | MAIOR
                           | MENORIGUAL
                           | MAIORIGUAL '''

    if p[1] == '<':
        P[0] = comparisonOperator(p[1])
    elif p[1] == '>':
        P[0] = comparisonOperator(p[1])
    elif p[1] == '<=':
        P[0] = comparisonOperator(p[1])
    elif p[1] == '>=':
        P[0] = comparisonOperator(p[1])
########################################################################

def p_inOperator(p):
    ''' inOperator : IN
                 | NOT_IN '''
    if p[1] == 'in':
        P[0] = inOperator(p[1])
    elif p[1] == '!in':
        P[0] = inOperator(p[1])
########################################################################

def p_isOperator(p):
    '''isOperator : IS
				| NOT_IS '''
    if p[1] == 'is':
        P[0] = isOperator(p[1])
    elif p[1] == '!is':
        P[0] = isOperator(p[1])
########################################################################

def p_additiveOperator(p):
    ''' additiveOperator : PLUS
                         | MINUS	'''
    if p[1] == '/+':
        P[0] = additiveOperator(p[1])
    elif p[1] == '-':
        P[0] = additiveOperator(p[1])
########################################################################

def p_multiplicativeOperator(p):
    ''' multiplicativeOperator : MULT
                                | DIVIDE
                                | MOD '''
    if p[1] == '*':
        P[0] = multiplicativeOperator(p[1])
    elif p[1] == '/':
        P[0] = multiplicativeOperator(p[1])
    elif p[1] == '%':
        P[0] = multiplicativeOperator(p[1])
########################################################################

def p_asOperator(p):
    ''' asOperator : AS
                 | AS asOperator '''
    if len(p) == 2:
        p[0] = SimpleAsOperator(p[1])
    else:
        p[0] = CompoundAsOperator(p[1], p[2])
########################################################################

def p_prefixUnaryOperator(p):
    ''' prefixUnaryOperator : INCREMENTO
                            | DECREMENTO
                            | MINUS
                            | PLUS
                            | NOT'''
    if p[1] == '++':
        P[0] = prefixUnaryOperator(p[1])
    elif p[1] == '--':
        P[0] = prefixUnaryOperator(p[1])
    elif p[1] == '-':
        P[0] = prefixUnaryOperator(p[1])
    elif p[1] == '/+':
        P[0] = prefixUnaryOperator(p[1])
    elif p[1] == '!':
        P[0] = prefixUnaryOperator(p[1])

########################################################################

def p_postfixUnaryOperator(p):
    ''' postfixUnaryOperator : INCREMENTO
                             | DECREMENTO '''
    if p[1] == '++':
        P[0] = CallPostfixUnaryOperator(p[1])
    elif p[1] == '--':
        P[0] = CallPostfixUnaryOperator(p[1])
########################################################################

def p_memberAccessOperator(p):
    ''' memberAccessOperator : safeNav
                             | COLONCOLON     '''
    if p[1] == '::':
        P[0] = memberAccessOperator(p[1])
    else:
        P[0] = memberAccessOperator(p[1])
########################################################################

def p_safeNav(p):
    ''' safeNav : PONTO  '''
    p[0] = p[1]
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
                        | INT
                        | FLOAT
                        | BOOLEAN
                        | STRING
                        | ARRAY
                        | CHAR
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
                        | DOUBLE
                        | WHEN
                        | LONG'''
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