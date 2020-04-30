# liveshare
import ply.lex as lex
import ply.yacc as yacc
from lex import tokens

from lex import tokens
import AbstrataClass as abstrat
import os

def p_kotlinFile(p):
    '''kotlinFile : functionDeclaration kotlinFile
					| functionDeclaration'''

    if len(p) == 2:
        p[0] = SingleFunctionDeclaration(p[1])
    else:
        p[0] = CompoundFunctionDeclaration(p[1], p[2])

def p_functionDeclaration(p):
  ''' functionDeclaration : FUN fd1 fd2 simpleIdentifier functionValueParameters fd3 fd5 '''

def p_fd1(p):
    ''' fd1 : typeParameters
            | '''

def p_fd2(p):
    ''' fd2 : receiverType PONTO
            | '''

def p_fd3(p):
    ''' fd3 : DOISP type
            | '''

def p_fd5(p):
    ''' fd5 : functionBody
            | '''
def p_typeParameters(p):
    '''typeParameters : MENOR tps MAIOR'''
    p[0] = TypeParameter(p[1], p[2], p[3])

def p_tps(p):
    '''tps : typeParameter
            | typeParameter COMMA tps
            | '''
    if len(p) == 2:
        p[0] = SingleTps(p[1])
    else:
        p[0] = CompoundTps(p[1], p[2], p[3])

def p_typeParameter(p):
    '''typeParameter : simpleIdentifier DOISP type
                      | simpleIdentifier'''
    if len(p) == 2:
        p[0] = SingleTypeParameter(p[1])
    else:
        p[0] = CompoundTypeParameter(p[1], p[2], p[3])

def p_functionBody(p):
    ''' functionBody : block
                    | ATRIBUICAO expression '''

def p_functionValueParameters(p):
    '''functionValueParameters : LPAREN fvps RPAREN
                                | LPAREN RPAREN'''
    if len(p) == 3:
        p[0] = SimpleFuncitionValueParameters(p[1], p[2])
    else:
        p[0] = CompoundFuncitionValueParameters(p[1], p[2], p[3])

def p_fvps(p):
    ''' fvps : functionValueParameter
                | functionValueParameter COMMA fvps
                | '''
    if len(p) == 2:
        p[0] = SingleFvps(p[1])
    else:
        p[0] = CompoundFvps(p[1], p[2], p[3])

def p_functionValueParameter(p):
    ''' functionValueParameter : parameter ATRIBUICAO expression
                                  | parameter '''
    if len(p) == 2:
        p[0] = SingleFunctionValueParameter(p[1])
    else:
        p[0] = CompoundFunctionValueParameter(p[1], p[2], p[3])

def p_variableDeclaration(p):
    '''variableDeclaration :  simpleIdentifier DOISP type
                            | simpleIdentifier '''

    if len(p) == 2:
        p[0] = SimpleVariableDeclaration(p[1])
    else:
        p[0] = CompoundVariebleDeclaration(p[1], p[2], p[3])

def p_multiVariableDeclaration(p):
    ''' multiVariableDeclaration : LPAREN mvd RPAREN'''
    
    p[0] = MultiVariableDeclaration(p[1], p[2], p[3])

def p_mvd(p):
    '''mvd : variableDeclaration
            |  variableDeclaration COMMA mvd
            | '''

    if leg(p) == 2:
        p[0] = SilgleMvd(p[1])
    else:
        p[0] = CompoundMvd(p[1], p[2], p[3])

def p_parameter(p):
    ''' parameter : simpleIdentifier DOISP type '''
    p[0] = Parameter(p[1], p[2], p[3])

def p_type(p):
    '''type : typeModifiers optype
              | optype '''
    if leng(p) == 2:
        p[0] = SingleType(p[1])
    else:
        p[0] = CompoundType(p[1], p[2])

##############################################Duvida
def p_opType(p):
    '''optype : parenthesizedType
                | functionType
                | userType '''
    

def p_typeModifiers(p) : 
  '''typeModifiers : typeModifier
                    | typeModifier typeModifiers '''
  
def p_typeModifier(p):
    ''' typeModifier : SUSPEND '''

 
def p_typeProjectionModifier(p):
    ''' typeProjectionModifier : varianceModifier '''


def p_varianceModifier(p): 
    ''' varianceModifier : IN
                        | OUT '''


def p_userType(p):
    ''' userType : simpleUserType '''
    p[0] = UserType(p[1])

def p_simpleUserType(p):
    ''' simpleUserType : simpleIdentifier typeArguments
					 | simpleIdentifier '''
    if len(p) == 2:
        p[0] = SimpleSimpleUserType(p[1])
    else:
        p[0] = CompoundSimpleUserType(p[1], p[2])

def p_typeProjection(p):
    '''typeProjection : typeProjectionModifiers type
                      | type '''
    if len(p) == 2:
        p[0] = SimpleTypeProjection(p[1])
    else:
        p[0] = CompoundTypeProjection(p[1], p[2])

def p_typeProjectionModifiers(p):
    '''typeProjectionModifiers : typeProjection
                                 | typeProjectionModifier typeProjectionModifiers '''
    if len(p) == 2:
        p[0] = SimpleTypeProjectionModifiers(p[1])
    else:
        p[0] = CompoundTypeProjectionModifiers(p[1], p[2])

def p_functionType(p):
    '''functionType : receiverType PONTO functionTypeParameters SETA type
                      | functionTypeParameters SETA type '''
    if len(p) == 4:
        p[0] = SimpleFunctionType(p[1], p[2], p[3])
    else:
        p[0] = CompoundFunctionType(p[1], p[2], p[3], p[4], p[5])

def p_functionTypeParameters(p):
    ''' functionTypeParameters : LPAREN parameter ftp RPAREN
                                | LPAREN parameter ftp COMMA RPAREN
                                | LPAREN type ftp RPAREN
                                | LPAREN type ftp COMMA RPAREN  '''

def p_ftp(p) :
	  ''' ftp : COMMA parameter
		  	  | COMMA type
			  | '''

def p_parenthesizedType(p):
    '''parenthesizedType : LPAREN type RPAREN '''
    p[0] = ParenthesizedType(p[1], p[2], p[3])

def p_receiverType(p):
    '''receiverType : typeModifier rt '''
    p[0] = ReceiverType(p[1], p[2])
##########################################################Duvida
def p_rt(p):
    '''rt : parenthesizedType'''

def p_statements(p):
    '''statements : statement
                  | statement statements
                  | '''
    if len(p) == 2:
        p[0] = SimpleStatements(p[1])
    else:
        p[0] = CompoundStatements(p[1], p[2])

##########################################################Duvida
def p_statement(p):
    '''statement : functionDeclaration
                  | assignment
                  | loopStatement
                  | expression '''


def p_controlStructureBody(p):
    '''controlStructureBody : block
                          | statement'''


def p_block(p):
    '''block : LCHAVE statements RCHAVE '''
    p[0] = Block(p[1], p[2], p[3])

##########################################################Duvida

def p_loopStatement(p):
    '''loopStatement : forStatement_MD
                    | forStatement_VD
                    | whileStatement
                    | doWhileStatement '''

def p_forStatement_MD(p):
    '''forStatement_MD : FOR LPAREN multiVariableDeclaration IN expression RPAREN controlStructureBody
                      | FOR LPAREN multiVariableDeclaration IN expression RPAREN'''
    if len(p) == 7:
        p[0] = SimpleForStatement_MD(p[1], p[2], p[3], p[4], p[5], p[6])
    else:
        p[0] = CompoundForStatement_MD(p[1], p[2], p[3], p[4], p[5], p[6], p[7])

def p_forStatement_VD(p):
    '''forStatement_VD :  FOR LPAREN variableDeclaration IN expression RPAREN controlStructureBody
                      | FOR LPAREN variableDeclaration IN expression RPAREN '''
    if len(p) == 7:
        p[0] = SimpleForStatement_MV(p[1], p[2], p[3], p[4], p[5], p[6])
    else:
        p[0] = CompoundForStatement_MV(p[1], p[2], p[3], p[4], p[5], p[6], p[7])

#############################################Duvida
def p_whileStatement(p):
    ''' whileStatement : WHILE LPAREN expression RPAREN controlStructureBody
                      |  WHILE LPAREN expression RPAREN PV '''


def p_doWhileStatement(p):
    ''' doWhileStatement : DO controlStructureBody WHILE LPAREN expression RPAREN
                          | DO WHILE LPAREN expression RPAREN '''
    if len(p) == 6:
        p[0] = SimpleDoWhileStatement(p[1], p[2], p[3], p[4], p[5])
    else:
        p[0] = CompoundDoWhileStatement(p[1], p[2], p[3], p[4], p[5], p[6])

#############################################Duvida

def p_assignment(p):
    '''assignment : directlyAssignableExpression IGUALDADE expression
                  | assignableExpression assignmentAndOperator expression '''


def p_expression(p):
    ''' expression : disjunction '''
    p[0] = Expression(p[1])

def p_disjunction(p):
    ''' disjunction : conjunction
                     | conjunction OR disjunction '''
    if len(p) == 2:
        p[0] = SimpleDisjuntion(p[1])
    else:
        p[0] = CompoundDisjuntion(p[1], p[2], p[3])

def p_conjunction(p):
    '''conjunction : equality
                  | equality AND conjunction '''
    if len(p) == 2:
        p[0] = SimpleConjunction(p[1])
    else:
        p[0] = CompoundConjunction(p[1], p[2], p[3])

def p_equality(p):
    ''' equality : comparison
                  | comparison equalityOperator equality '''
    if len(p) == 2:
        p[0] = SimpleEquality(p[1])
    else:
        p[0] = CompoundEquality(p[1], p[2], p[3])

def p_comparison(p):
    ''' comparison : infixOperation
                     | infixOperation comparisonOperator infixOperation '''
    if len(p) == 2:
        p[0] = SimpleComparison(p[1])
    else:
        p[0] = CompoundComparison(p[1], p[2], p[3])

def p_infixOperation(p):
    '''infixOperation : elvisExpression io '''
    p[0] = InfixOperation(p[1], p[2])

######################################################Duvida
def p_io(p):
    '''io : inOperator elvisExpression
            | isOperator type
            | '''

def p_elvisExpression(p):
    ''' elvisExpression : infixFunctionCall
                          | infixFunctionCall ELVIS elvisExpression
                          | '''
    if len(p) == 2:
        SimpleElvisExpression(p[1])
    else:
        CompoundElvisExpression(p[1], p[2], p[3])


def p_infixFunctionCall(p):
    '''infixFunctionCall : rangeExpression
                          | rangeExpression simpleIdentifier infixFunctionCall '''
    if len(p) == 2:
        SimpleInfixFunctionCall(p[1])
    else:
        CompoundInfixFunctionCall(p[1], p[2], p[3])


# MAIS UM OPERADOR '..' PONTOPONTO (PESQUISAR SOBRE)
def p_rangeExpression(p):
    ''' rangeExpression : additiveExpression
						| additiveExpression PONTOPONTO rangeExpression '''
    if len(p) == 2:
        SimpleRangeExpression(p[1])
    else:
        CompoundRangeExpression(p[1], p[2], p[3])

def p_additiveExpression(p):
    ''' additiveExpression : multiplicativeExpression
                             | multiplicativeExpression additiveOperator additiveExpression '''
    if len(p) == 2:
        SimpleAdditiveExpression(p[1])
    else:
        CompoundAdditiveExpression(p[1], p[2], p[3])

def p_multiplicativeExpression(p):
    ''' multiplicativeExpression : asExpression
                                  | asExpression multiplicativeOperator multiplicativeExpression '''
    if len(p) == 2:
        SimpleMultiplicativeExpression(p[1])
    else:
        CompoundMultiplicativeExpression(p[1], p[2], p[3])

def p_asExpression(p):
    ''' asExpression : prefixUnaryExpression
                       | prefixUnaryExpression asOperator type '''
    if len(p) == 2:
        SimpleAsExpression(p[1])
    else:
        CompoundAsExpression(p[1], p[2], p[3])

def p_prefixUnaryExpression(p):
    ''' prefixUnaryExpression : preue postfixUnaryExpression '''
    p[0] = PrefixUnaryExpression(p[0], p[1])

def p_preue(p):
    ''' preue : unaryPrefix
            | unaryPrefix preue
            | '''
    if len(p) == 2:
        SimplePreue(p[1])
    else:
        CompoundPreue(p[1], p[2])

#############################################################duvida
def p_unaryPrefix(p):
    ''' unaryPrefix : label
                       | prefixUnaryOperator '''

def p_label(p):
    ''' label : simpleIdentifier'''

def p_postfixUnaryExpression(p):
    ''' postfixUnaryExpression : primaryExpression
                                 | primaryExpression posue '''
    if len(p) == 2:
        SimplePostfixUnaryExpression(p[1])
    else:
        CompoundPostfixUnaryExpression(p[1], p[2])

def p_posue(p):
    ''' posue : postfixUnarySuffix
                | postfixUnarySuffix posue '''
    if len(p) == 2:
        SimplePosue(p[1])
    else:
        CompoundPosue(p[1], p[2])

#####################################################duvida
def p_postfixUnarySuffix(p):
    ''' postfixUnarySuffix : postfixUnaryOperator
                               | typeArguments
                               | callSuffix
                               | indexingSuffix
                               | navigationSuffix '''


def p_directlyAssignableExpression(p):
    ''' directlyAssignableExpression : postfixUnaryExpression assignableSuffix
                                       | simpleIdentifier
                                       | parenthesizedDirectlyAssignableExpression '''


def p_parenthesizedDirectlyAssignableExpression(p):
    ''' parenthesizedDirectlyAssignableExpression : LPAREN directlyAssignableExpression RPAREN '''
    p[0] = ParenthesizedDirectlyAssignableExpression(p[1], p[2], p[3])

###########################################################duvida
def p_assignableExpression(p):
    ''' assignableExpression : prefixUnaryExpression
                              | parenthesizedAssignableExpression '''

def p_parenthesizedAssignableExpression(p):
    ''' parenthesizedAssignableExpression : LPAREN assignableExpression RPAREN '''
    p[0] = ParenthesizedAssignableExpression(p[1], p[2], p[3])

###########################################################duvida
def p_assignableSuffix(p):
    ''' assignableSuffix : typeArguments
                            | indexingSuffix
                            | navigationSuffix'''

# NOVO TOKEN '[', ']' LCCT E RCCT
def p_indexingSuffix(p):
    ''' indexingSuffix : LCCT isuf RCCT '''
    p[0] = IndexingSuffix(p[1], p[2], p[3])

def p_isuf(p):
    ''' isuf : expression
				| expression COMMA isuf
				| '''
    if len(p) == 2:
        SimpleIsuf(p[1])
    else:
        CompoundIsuf(p[1], p[2], p[3])

##########################################################duvida
def p_navigationSuffix(p):
    ''' navigationSuffix : memberAccessOperator simpleIdentifier CLASS
                         | memberAccessOperator parenthesizedExpression CLASS '''


def p_callSuffix(p):
    '''callSuffix : typeArguments valueArguments annotatedLambda
                     | valueArguments annotatedLambda
                     | typeArguments  annotatedLambda
                     | annotatedLambda
                     | typeArguments valueArguments
                     | valueArguments '''


def p_annotatedLambda(p):
    ''' annotatedLambda : lambdaLiteral '''
    p[0] = AnnotatedLambda(p[1])

def p_typeArguments(p):
    ''' typeArguments : MENOR ta MAIOR'''
    p[0] = TypeArguments(p[1], p[2], p[3])

def p_ta(p):
    ''' ta : typeProjection
            | typeProjection COMMA ta
            | '''
    if len(p) == 2:
        SimpleTa(p[1])
    else:
        CompoundTa(p[1], p[2], p[3])

def p_valueArguments(p):
    '''valueArguments : LPAREN RPAREN
                     | LPAREN vas RPAREN '''
    if len(p) == 3:
        SimpleValueArguments(p[1], p[2])
    else:
        CompoundValueArguments(p[1], p[2], p[3])

def p_vas(p):
    ''' vas : valueArgument
             | valueArgument COMMA vas '''
    if len(p) == 2:
        SimpleVas(p[1])
    else:
        CompoundVas(p[1], p[2], p[3])

def p_valueArgument(p):
    ''' valueArgument : simpleIdentifier IGUALDADE MULT expression
                      | simpleIdentifier IGUALDADE expression
                      | expression  '''
    if len(p) == 2:
        SimpleValueArgument(p[1])
    elif len(p) == 4:
        Compound1ValueArgument(p[1], p[2].p[3])
    else:
        Compound2ValueArgument(p[1], p[2], p[3], p[4])

###############################################duvida
def p_primaryExpression(p):
    ''' primaryExpression : parenthesizedExpression
                           | simpleIdentifier
                           | LITERAL_STRING
                           | callableReference
                           | functionLiteral
                           | collectionLiteral
                           | ifExpression
                           | jumpExpression '''


def p_parenthesizedExpression(p):
    ''' parenthesizedExpression : LPAREN expression RPAREN '''
    p[0] = ParenthesizedExpression(p[1], p[2], p[3])

def p_collectionLiteral(p):
    ''' collectionLiteral : LCCT cl RCCT
                             | LCCT RCCT '''
    if len(p) == 3:
        SimpleColetionLiteral(p[1], p[2])
    else:
        CompoundColetionLiteral(p[1], p[2], p[3])

def p_cl(p):
    ''' cl : expression
            | expression COMMA cl '''
    if len(p) == 2:
        SimpleCl(p[1])
    else:
        CompoundCol(p[1], p[2])


def p_parametersWithOptionalType(p):
    ''' parametersWithOptionalType : LPAREN pwot RPAREN'''
    
def p_pwot(p):
    ''' pwot : parameterWithOptionalType 
            | parameterWithOptionalType COMMA pwot COMMA
            | '''

def p_parameterWithOptionalType(p):
    ''' parameterWithOptionalType : parameterModifiers simpleIdentifier DOISP type
                                    | simpleIdentifier DOISP type
                                    | parameterModifiers simpleIdentifier
                                    | simpleIdentifier '''

def p_parameterModifiers(p):
    ''' parameterModifiers :  VARARG
                            | NOINLINE
                            | CROSSINLINE '''

########################################duvida
    
def p_lambdaLiteral(p):
    ''' lambdaLiteral : RCHAVE ll LCHAVE	'''
    p[0] = LambdaLiteral(p[1], p[2], p[3])

def p_ll(p):
    ''' ll : statements
            | lambdaParameters SETA statements
            | SETA statements'''
    if len(p) == 2:
        p[0] = SimpleLl(p[1])
    elif len(p) == 3:
        p[0] = Compound1Ll(p[1], p[2])
    else :
        p[0] = Compound2Ll(p[1], p[2], p[3])
        
def p_lambdaParameters(p):
    ''' lambdaParameters : lambdaParameter
                          | lambdaParameter COMMA lambdaParameters '''
    if len(p) == 2:
        p[0] = SimpleLambdaParameters(p[1])
    else :
        p[0] = CompoundLambdaParameters(p[1], p[2], p[3])
        
def p_lambdaParameter(p):
    ''' lambdaParameter : variableDeclaration
                     | multiVariableDeclaration DOISP type
                     | multiVariableDeclaration '''

################################################duvida
def p_anonymousFunction(p):
    ''' anonymousFunction : FUN af4 parametersWithOptionalType af3 af1 '''

def p_af1(p):
    ''' af1 : functionBody
				| '''

def p_p_anonymousFunction(p):
    ''' anonymousFunction : WHERE af'''

def p_af(p):
    ''' af : typeConstraint
            | typeConstraint COMMA af '''

def p_typeConstraint(p):
    ''' typeConstraint : simpleIdentifier DOISP type '''

def p_af3(p):
    ''' af3 : DOISP type
            | '''


def p_af4(p):
    ''' af4 : type PONTO
            | '''


def p_functionLiteral(p):
    ''' functionLiteral : lambdaLiteral
                         | anonymousFunction '''

def p_ifExpression(p):
    ''' ifExpression : IF LPAREN expression RPAREN controlStructureBody PV
                         | IF LPAREN expression RPAREN controlStructureBody
                         | IF LPAREN expression RPAREN controlStructureBody PV ELSE controlStructureBody PV
                         | IF LPAREN expression RPAREN controlStructureBody PV ELSE controlStructureBody
                         | IF LPAREN expression RPAREN controlStructureBody ELSE controlStructureBody PV
                         | IF LPAREN expression RPAREN controlStructureBody ELSE controlStructureBody
                         | IF LPAREN expression RPAREN PV ELSE controlStructureBody PV
                         | IF LPAREN expression RPAREN PV ELSE controlStructureBody
                         | IF LPAREN expression RPAREN ELSE controlStructureBody PV
                         | IF LPAREN expression RPAREN ELSE controlStructureBody '''

# VERIFICAR TOKENS
def p_jumpExpression(p):
    ''' jumpExpression :  RETURN expression
                         | RETURN_AT expression
                         | expression
                         | CONTINUE
                         | CONTINUE_AT
                         | BREAK
                         | BREAK_AT'''


def p_callableReference_SI(p):
    ''' callableReference : receiverType DOISP DOISP simpleIdentifier
                         | DOISP DOISP simpleIdentifier '''
    if len(p) == 4:
        p[0] = SimpleCallableReference_SI(p[1], p[2], p[3])
    else:
        p[0] = CompoundCallableReference_SI(p[1], p[2], p[3], p[4])
        
def p_callableReference_Class(p):
    ''' callableReference : receiverType DOISP DOISP CLASS
                         | DOISP DOISP CLASS'''
    if len(p) == 4:
        p[0] = SimpleCallableReference_Class(p[1], p[2], p[3])
    else:
        p[0] = CompoundCallableReference_Class(p[1], p[2], p[3], p[4])
        
# VERIFICAT TOKENS
def p_assignmentAndOperator(p):
    ''' assignmentAndOperator : MAIORIGUAL
                               | MENORIGUAL
                               | MULTIGUAL
                               | DIVIGUAL
                               | MODIGUAL	'''


def p_equalityOperator(p):
    ''' equalityOperator : DIFERENTE
                         | IDENTIDADE
                         | IGUALDADE
                         | SEMIDENTIDADE	'''


def p_comparisonOperator(p):
    ''' comparisonOperator : MENOR
                           | MAIOR
                           | MENORIGUAL
                           | MAIORIGUAL '''


def p_inOperator(p):
    ''' inOperator : IN
                 | NOT_IN '''


def p_isOperator(p):
    '''isOperator : IS
				| NOT_IS '''


def p_additiveOperator(p):
    ''' additiveOperator : PLUS
                         | MINUS	'''


def p_multiplicativeOperator(p):
    ''' multiplicativeOperator : MULT
                                | DIVIDE
                                | MOD '''


# duvida
def p_asOperator(p):
    ''' asOperator : AS
                 | AS asOperator '''
    if len(p) == 2:
        p[0] = SimpleAsOperation(p[1])
    else:
        p[0] = CompoundAsOperation(p[1], p[2])
        
# DUVIDA
def p_prefixUnaryOperator(p):
    ''' prefixUnaryOperator : INCREMENTO
   | DECREMENTO
   | MINUS
   | PLUS
   | NOT'''



# Duvida
def p_postfixUnaryOperator(p):
    ''' postfixUnaryOperator : INCREMENTO
                             | DECREMENTO'''


def p_memberAccessOperator(p):
    ''' memberAccessOperator : PONTO
                             | safeNav
                             | COLONCOLON     '''


def p_safeNav(p):
    ''' safeNav : PONTO  '''
    p[0] = SafeNav(p[1])

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
                        | WHERE  '''


def p_error(p):
    print ("Erro Sintático")

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