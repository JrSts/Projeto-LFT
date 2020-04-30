#liveshare
import ply.lex as lex
import ply.yacc as yacc
from lex import tokens

from lex import tokens
import AbstrataClass as abstrat
import os

def p_kotlinFile(p) :
    '''kotlinFile : functionDeclaration kotlinFile
					| functionDeclaration'''

	if len(p) = 2
		p[0] = p[1] 
	else 
		p[0] = KotlinFile(p[1]+p[2])

def p_functionDeclaration(p) :
    '''functionDeclaration : FUN simpleIdentifier functionValueParameters LPAREN DOISP type RPAREN block
							| FUN simpleIdentifier functionValueParameters LPAREN DOISP type RPAREN 
							| FUN simpleIdentifier functionValueParameters LPAREN DOISP RPAREN block
							| FUN simpleIdentifier functionValueParameters LPAREN DOISP RPAREN '''
    
def p_typeParameters(p) :
    '''typeParameters : MENOR tps MAIOR'''

def p_tps(p) : 
	'''tps : typeParameter 
			| typeParameter 
			LPAREN COMMA typeParameter RPAREN'''

def p_typeParameter(p) :
  '''typeParameter : simpleIdentifier LPAREN DOISP type RPAREN 
					| simpleIdentifier LPAREN DOISP RPAREN'''

def p_functionValueParameters(p) :
	'''functionValueParameters : LPAREN fvps RPAREN'''

def p_fvps(p) :
	''' fvps : functionValueParameter 
				| functionValueParameter COMMA fvps
				| '''

def p_functionValueParameter(p) :
  ''' functionValueParameter : parameter IGUALDADE expression
								| parameter '''

def p_variableDeclaration(p) : 
	'''variableDeclaration :  annot simpleIdentifier DOISP type
							| annot simpleIdentifier '''

							
def p_annot(p) :
	'''annot : annotation
				| annotation annot
				| '''

def p_multiVariableDeclaration(p) : 
	''' LPAREN mvd RPAREN'''


def p_mvd(p) :
	'''mvd : variableDeclaration 
			|  variableDeclaration COMMA mvd 
			| '''

def p_propertyDeclaration(p) :
	'''propertyDeclaration : VAR multiVariableDeclaration IGUALDADE expression PV
							|VAR multiVariableDeclaration IGUALDADE expression
							|VAR multiVariableDeclaration PV
							|VAR multiVariableDeclaration 
							|VAL multiVariableDeclaration IGUALDADE expression PV
							|VAL multiVariableDeclaration IGUALDADE expression
							|VAL multiVariableDeclaration PV
							|VAL multiVariableDeclaration 
							|VAR VariableDeclaration IGUALDADE expression PV
							|VAR VariableDeclaration IGUALDADE expression
							|VAR VariableDeclaration PV
							|VAR VariableDeclaration 
							|VAL VariableDeclaration IGUALDADE expression PV
							|VAL VariableDeclaration IGUALDADE expression
							|VAL VariableDeclaration PV
							|VAL VariableDeclaration '''

def p_parameter(p) : 
	''' parameter : simpleIdentifier DOISP type '''
							
def p_type(p) :
  '''type : typeModifiers optype 
			| optype '''

def p_opType(p) : '''optype : parenthesizedType | functionType | userType '''

def p_userType(p) :
  ''' userType : simpleUserType '''

def p_simpleUserType(p) :
    ''' simpleUserType : simpleIdentifier typeArguments
					 | simpleIdentifier '''

def p_typeProjection(p) : 
  '''typeProjection : typeProjectionModifiers type
					| type '''

def p_typeProjectionModifiers(p) : 
   '''typeProjectionModifiers : typeProjectionModifier
								| typeProjectionModifier typeProjectionModifiers '''

def p_functionType(p) :
  '''functionType : receiverType PONTO functionTypeParameters SETA type
					| functionTypeParameters SETA type '''
  


#  def p_functionTypeParameters(p) :
#    ''' functionTypeParameters :
#          LPAREN parameter ftp RPAREN|LPAREN parameter ftp RPAREN
#    '''
#
#  def p_ftp(p) :
#	  ''' ftp : COMMA parameter
#		  	  | COMMA type
#			  | '''

def p_parenthesizedType(p) : 
  '''parenthesizedType : COMMA type COMMA '''

def p_receiverType(p) :
  '''receiverType : typeModifier rt '''

def p_rt(p) :
	'''rt : parenthesizedType 
			| nullableType 
			| typeReference'''

def p_parenthesizedUserType(p) :
  '''parenthesizedUserType : LPAREN userType RPAREN
						 | LPAREN parenthesizedUserType RPAREN '''

def p_statements(p) : 
  '''statements : statement 
				| statement statments
				| '''

def p_statement(p) : 
  '''statement : functionDeclaration 
				| assignment 
				| loopStatement 
				| expression '''

def p_controlStructureBody(p) :
  '''controlStructureBody : block
						| statement'''

def p_block(p) :
  '''block : LCHAVE statements RCHAVE '''

def p_loopStatement(p) :
	'''loopStatement : forStatement
					| whileStatement
					| doWhileStatement '''

def p_forStatement(p) :
  '''forStatement : FOR LPAREN multiVariableDeclaration IN expression RPAREN controlStructureBody
					|FOR LPAREN variableDeclaration IN expression RPAREN controlStructureBody
					|FOR LPAREN multiVariableDeclaration IN expression RPAREN 
					|FOR LPAREN variableDeclaration IN expression RPAREN '''


def p_whileStatement(p) :
  ''' whileStatement : WHILE LPAREN expression RPAREN controlStructureBody
					|  WHILE LPAREN expression RPAREN PV '''

def p_doWhileStatement(p) :
  ''' doWhileStatement: DO controlStructureBody WHILE LPAREN expression RPAREN
						|DO WHILE LPAREN expression RPAREN '''

def p_assignment(p) : 
  '''assignment : directlyAssignableExpression IGUALDADE expression
				| assignableExpression assignmentAndOperator expression '''

def p_semi (p) :
  ''' semi : EOF '''

def p_expression(p) :
   ''' expression : disjunction '''

def p_disjunction(p) : 
   ''' disjunction : conjunction 
					| conjunction OR disjunction '''


def p_conjunction(p) :
  '''conjunction : equality 
				|equality && conjunction '''
 

def p_equality(p) :
  ''' equality : comparison 
				| comparison equalityOperator equality '''

def p_comparison(p) : 
   ''' comparison : infixOperation 
					| infixOperation comparisonOperator infixOperation '''
					 
def p_infixOperation(p) :
  '''infixOperation : elvisExpression io '''
  
def p_io(p) :
	'''io : inOperator elvisExpression
			| isOperator type
			| '''

def p_elvisExpression(p) :
  ''' elvisExpression : infixFunctionCall
						| infixFunctionCall elvis elvisExpression 
						| '''
  
# def p_elvis(p) :
#   ''' elvis : DOISP
#				| '''
  
def p_infixFunctionCall(p) :
  '''infixFunctionCall : rangeExpression 
						| rangeExpression simpleIdentifier infixFunctionCall '''
  
# MAIS UM OPERADOR '..' PONTOPONTO (PESQUISAR SOBRE)
def p_rangeExpression(p) :
    ''' rangeExpression : additiveExpression
							| additiveExpression PONTOPONTO rangeExpression '''

def p_additiveExpression(p) :
   ''' additiveExpression : multiplicativeExpression 
                            | multiplicativeExpression additiveOperator additiveExpression ''' 

def p_multiplicativeExpression(p) :
  ''' multiplicativeExpression : asExpression 
								| asExpression multiplicativeOperator multiplicativeExpression '''

def p_asExpression(p) :
   ''' asExpression : prefixUnaryExpression
                      | prefixUnaryExpression asOperator type '''

def p_prefixUnaryExpression(p) :
  ''' prefixUnaryExpression : preue postfixUnaryExpression '''

def p_preue(p) :
	''' preue : unaryPrefix
			| unaryPrefix preue
			| '''
  
def p_unaryPrefix(p) :
   ''' unaryPrefix : annotation
					  | label
					  | prefixUnaryOperator '''

def p_postfixUnaryExpression(p) :
   ''' postfixUnaryExpression : primaryExpression
								| primaryExpression posue '''

def p_posue(p) :
	''' posue : postfixUnarySuffix
				| postfixUnarySuffix posue '''

def p_postfixUnarySuffix(p) :
   ''' postfixUnarySuffix : postfixUnaryOperator
							  | typeArguments
							  | callSuffix
							  | indexingSuffix
							  | navigationSuffix '''
  
def p_directlyAssignableExpression(p) :
   ''' directlyAssignableExpression : postfixUnaryExpression assignableSuffix
									  | simpleIdentifier
									  | parenthesizedDirectlyAssignableExpression '''

def p_parenthesizedDirectlyAssignableExpression(p) :
   ''' parenthesizedDirectlyAssignableExpression : LPAREN directlyAssignableExpression RPAREN '''

def p_assignableExpression(p) :
   ''' assignableExpression : prefixUnaryExpression
							 | parenthesizedAssignableExpression '''

def p_parenthesizedAssignableExpression(p) :
   ''' parenthesizedAssignableExpression : LPAREN assignableExpression RPAREN '''

def p_assignableSuffix(p) :
  ''' assignableSuffix : typeArguments
						  | indexingSuffix
						  | navigationSuffix'''

# NOVO TOKEN '[', ']' LCCT E RCCT
def p_indexingSuffix(p) :
   ''' indexingSuffix : LCCT isuf RCCT '''

def p_isuf(p) : 
    ''' isuf : expression
				| expression COMMA isuf 
				| '''

def p_navigationSuffix(p) : 
   ''' navigationSuffix : memberAccessOperator simpleIdentifier CLASS
						| memberAccessOperator parenthesizedExpression CLASS '''
  
def p_callSuffix(p) : 
   '''callSuffix : typeArguments valueArguments annotatedLambda
					|  valueArguments annotatedLambda
					|  typeArguments  annotatedLambda
					|  annotatedLambda
					| typeArguments valueArguments
					| valueArguments '''
 
def p_annotatedLambda(p) :
   ''' annotatedLambda : lambdaLiteral '''
 
def p_typeArguments(p) :
	''' typeArguments : MENOR ta MAIOR'''

def p_ta(p) :
	''' ta : typeProjection
			| typeProjection COMMA ta 
			| '''

def p_valueArguments(p) :
   '''valueArguments : LPAREN RPAREN
					| LPAREN vas RPAREN '''
  

def p_vas(p) :
   ''' vas : valueArgument 
			| valueArgument COMMA vas '''

def p_valueArgument(p) :
   ''' valueArgument : annotation simpleIdentifier IGUALDADE MULT expression
					 | annotation simpleIdentifier IGUALDADE expression
					 | annotation expression
					 | simpleIdentifier IGUALDADE MULT expression
					 | simpleIdentifier IGUALDADE expression
					 | expression  '''

def p_primaryExpression(p) :
   ''' primaryExpression : parenthesizedExpression
						  | simpleIdentifier
						  | literalConstant
						  | stringLiteral
						  | callableReference
						  | functionLiteral
						  | objectLiteral
						  | collectionLiteral
						  | ifExpression
						  | jumpExpression '''
  
def p_parenthesizedExpression(p) :
 ''' parenthesizedExpression : LPAREN expression RPAREN '''
  

def p_collectionLiteral(p) :
   ''' collectionLiteral : LCCT cl RCCT
							| LCCT RCCT '''
  
def p_cl(p) :
	''' cl : expression 
			| expression COMMA cl '''

def p_literalConstant(p) :
   ''' literalConstant : BooleanLiteral
						  | IntegerLiteral
						  | HexLiteral
						  | BinLiteral
						  | CharacterLiteral
						  | RealLiteral
						  | 'null'
						  | LongLiteral
						  | UnsignedLiteral '''

def p_stringLiteral(p) :
   ''' stringLiteral : lineStringLiteral
					| multiLineStringLiteral '''

def p_lambdaLiteral(p) :
   ''' lambdaLiteral : RCHAVE ll LCHAVE	'''

def p_ll(p) : 
	''' ll : statements
			| lambdaParameters SETA statements
			| SETA statements'''

def p_lambdaParameters(p) :
  ''' lambdaParameters : lambdaParameter
						| lambdaParameter COMMA lambdaParameters '''

def p_lambdaParameter(p) :
   ''' lambdaParameter : variableDeclaration
					| multiVariableDeclaration DOISP type
					| multiVariableDeclaration '''

def p_anonymousFunction(p) :
	''' anonymousFunction : FUN af4 parametersWithOptionalType af3 af2 af1 '''

def p_af1(p) : 
    ''' af1 : functionBody
				| ''' 

def p_af2(p) :
	''' af2 : typeConstraints
			| '''

def p_af3(p) :
	''' af3 : DOISP type
			| '''

def p_af4(p) : 
	''' af4 : type PONTO
			| '''

def p_functionLiteral(p) :
   ''' functionLiteral : lambdaLiteral
						| anonymousFunction '''
 
def p_ifExpression(p) :
   ''' ifExpression : IF LPAREN expression RPAREN controlStructureBody PV
						| IF LPAREN expression RPAREN controlStructureBody
						| IF LPAREN expression RPAREN controlStructureBody PV ESLE controlStructureBody PV
						| IF LPAREN expression RPAREN controlStructureBody PV ESLE controlStructureBody
						| IF LPAREN expression RPAREN controlStructureBody ESLE controlStructureBody PV
						| IF LPAREN expression RPAREN controlStructureBody ESLE controlStructureBody 
						| IF LPAREN expression RPAREN PV ESLE controlStructureBody PV
						| IF LPAREN expression RPAREN PV ESLE controlStructureBody
						| IF LPAREN expression RPAREN ESLE controlStructureBody PV
						| IF LPAREN expression RPAREN ESLE controlStructureBody '''

# VERIFICAR TOKENS
def p_jumpExpression(p) :
   ''' jumpExpression : THROW expression
						| RETURN expression
						| RETURN_AT expression 
						| expression
						| CONTINUE
					    | CONTINUE_AT
						| BREAK
						| BREAK_AT'''
  
def p_callableReference(p) :
   ''' callableReference : receiverType DOISP DOISP simpleIdentifier 
						| DOISP DOISP simpleIdentifier
						| receiverType DOISP DOISP CLASS 
						| DOISP DOISP CLASS'''
  
# VERIFICAT TOKENS
def p_assignmentAndOperator(p) : 
   ''' assignmentAndOperator : MAISIGUAL	# +=
							  | MENOSIGUAL	# -=
							  | MULTIGUAL	# *=
							  | DIVIGUAL	# /=
							  | MODIGUAL	# %=	'''
  
def p_equalityOperator(p) :
   ''' equalityOperator : DIFERENTE			# !=
						| IDENTIDADE		# ===
						| IGUALDADE			# ==
						| SEMIDENTIDADE		# !==		'''
  
def p_comparisonOperator(p) :
   ''' comparisonOperator : MENOR
						  | MAIOR
						  | MENORIGUAL
						  | MAIORIGUAL '''
						  
def p_inOperator(p) :
   ''' inOperator : IN
				| NOT_IN '''
  
def p_isOperator(p) :
    '''isOperator : IS
				| NOT_IS '''
  
def p_additiveOperator(p) :
   ''' additiveOperator : PLUS
						| MINUS	'''
  
def p_multiplicativeOperator(p) :
	''' multiplicativeOperator : MULT
								| DIVIDE
								| MOD '''
  
  #duvida
def p_asOperator(p) :
   ''' asOperator : AS
				| AS asOperator '''
  #DUVIDA
def p_prefixUnaryOperator(p) :
   ''' prefixUnaryOperator : INCREMENTO
  | DECREMENTO
  | MINUS
  | PLUS
  | excl'''
 #Duvida  
def p_postfixUnaryOperator(p) :
   ''' postfixUnaryOperator : INCREMENTO
							| DECREMENTO
  | '!' excl
  ;
excl (p)
  : '!'
  | EXCL_WS
  ;'''

def p_memberAccessOperator(p) :
   ''' memberAccessOperator : PONTO
							| safeNav
							| COLONCOLON     '''

def p_safeNav(p) :
   ''' safeNav : PONTO  '''

# Identifiers
# olhar tokens
def p_simpleIdentifier(p) :
   ''' simpleIdentifier : Identifier
					  | 'abstract'
					  | 'annotation'
					  | 'by'
					  | 'catch'
					  | 'companion'
					  | 'constructor'
					  | 'crossinline'
					  | 'data'
					  | 'dynamic'
					  | 'enum'
					  | 'external'
					  | 'final'
					  | 'finally'
					  | 'get'
					  | 'import'
					  | 'infix'
					  | 'init'
					  | 'inline'
					  | 'inner'
					  | 'internal'
					  | 'lateinit'
					  | 'noinline'
					  | 'open'
					  | 'operator'
					  | 'out'
					  | 'override'
					  | 'private'
					  | 'protected'
					  | 'public'
					  | 'reified'
					  | 'sealed'
					  | 'tailrec'
					  | 'set'
					  | 'vararg'
					  | 'where'
					  | 'field'
					  | 'property'
					  | 'receiver'
					  | 'param'
					  | 'setparam'
					  | 'delegate'
					  | 'file'
					  | 'expect'
					  | 'actual'
					  | 'const'
					  | 'suspend'  '''
  
def p_identifier(p) :
   ''' identifier : simpleIdentifier
					| simpleIdentifier PONTO identifier '''
  

class AnalisadorSintatico():
    def __init__(self):

        self.arquivo_entrada = "ProgramaKotlin_entrada.txt" #L�xico
        self.arquivo_saida = "ProgramaKotlin_saida.txt"		#Sint�tico

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

    def next_token (self):
        self.i += 1
        self.linha_atual = self.tokens[self.i] [self.tokens[self.i].find('\n'|';')+2: -1]
    def conteudo_token(self):
        return self.tokens[self.i][ : self.tokens[self.i].find('->')]

#Iniciar(kotlinFile -> (functionDeclaration* EOF)) 
    def start(self):
        if("Erro Lexico" in self.tokens[self.i]):
            self.i +=1
        self.FunctionDeclaration()
        if(self.tem_erro_sintatico):
            print("Verifique os erros sintaticos e tente compilar novamente")
            self.arquivo_saida.write("Verifique os erros sintaticos e tente compilar novamente\n")
        else:
            if("$" in self.tokens[self.i]):
                print("Cadeia de tokens na analise sintatica reconhecida com sucesso")
                self.arquivo_saida.write("Cadeia de tokens reconhecida com sucesso\n")
            else:
                print("Fim de Programa Nao Encontrado!")
                self.arquivo_saida.write("Fim de Programa Nao Encontrado!")
        self.arquivo_saida.close()
    def FunctionDeclaration (self):
        if("Erro Lexico" in self.tokens[self.i]):
            self.i += 1
        if('NUMER' in self.tokens[self.i]):
            self.next_token()
        if('PLUS' in self.tokens[self.i]):
            self.next_token()
        if('MINUS' in self.tokens[self.i]):
            self.next_token()
        if('MULT' in self.tokens[self.i]):
            self.next_token() 
        if('DIVIDE' in self.tokens[self.i]):
            self.next_token() 
        if('LPAREN' in self.tokens[self.i]):
            self.next_token() 
        if('RPAREN' in self.tokens[self.i]):
            self.next_token() 
        if('IF' in self.tokens[self.i]):
            self.next_token() 
        if('IMPORT' in self.tokens[self.i]):
            self.next_token() 
        if('NULLABLE' in self.tokens[self.i]):
            self.next_token() 
        if('VAR' in self.tokens[self.i]):
            self.next_token() 
        if('VAL' in self.tokens[self.i]):
            self.next_token() 
        if('FUN' in self.tokens[self.i]):
            self.next_token() 
        if('STRING' in self.tokens[self.i]):
            self.next_token() 
        if('ARRAY' in self.tokens[self.i]):
            self.next_token() 
        if('OBJECT' in self.tokens[self.i]):
            self.next_token() 
        if('THIS' in self.tokens[self.i]):
            self.next_token() 
        if('CHAR' in self.tokens[self.i]):
            self.next_token() 
        if('WHILE' in self.tokens[self.i]):
            self.next_token() 
        if('NULL' in self.tokens[self.i]):
            self.next_token() 
        if('WHEN' in self.tokens[self.i]):
            self.next_token() 
        if('FLOAT' in self.tokens[self.i]):
            self.next_token() 
        if('RETURN' in self.tokens[self.i]):
            self.next_token() 
        if('CONST' in self.tokens[self.i]):
            self.next_token() 
        if('OPERATOR' in self.tokens[self.i]):
            self.next_token() 
        if('INT' in self.tokens[self.i]):
            self.next_token() 
        if('CLASS' in self.tokens[self.i]):
            self.next_token() 
        if('CONSTRUCTOR' in self.tokens[self.i]):
            self.next_token() 
        if('DOUBLE' in self.tokens[self.i]):
            self.next_token() 
        if('SMARTCAST' in self.tokens[self.i]):
            self.next_token() 
        if('BOOLEAN' in self.tokens[self.i]):
            self.next_token() 
        if('FUNCTION' in self.tokens[self.i]):
            self.next_token() 
        if('FOR' in self.tokens[self.i]):
            self.next_token() 
        if('FALSE' in self.tokens[self.i]):
            self.next_token() 
        if('MOD' in self.tokens[self.i]):
            self.next_token() 
        if('PLUSPLUS' in self.tokens[self.i]):
            self.next_token()
        if('DECREMENTO' in self.tokens[self.i]):
            self.next_token()
        if('ATRIBUICAO' in self.tokens[self.i]):
            self.next_token()
        if('IGUALDADE' in self.tokens[self.i]):
            self.next_token()
        if('DIFERENTE' in self.tokens[self.i]):
            self.next_token()
        if('NOT' in self.tokens[self.i]):
            self.next_token()
        if('MENORIGUAL' in self.tokens[self.i]):
            self.next_token()
        if('MAIORIGUAL' in self.tokens[self.i]):
            self.next_token()
        if('MAIOR' in self.tokens[self.i]):
            self.next_token()
        if('MENOR' in self.tokens[self.i]):
            self.next_token()
        if('AND' in self.tokens[self.i]):
            self.next_token()
        if('OR' in self.tokens[self.i]):
            self.next_token()
        if('LCHAVE' in self.tokens[self.i]):
            self.next_token()
        if('RCHAVE' in self.tokens[self.i]):
            self.next_token()
        if('TRUE'in self.tokens[self.i]):
            self.next_token()
        if('ELSE' in self.tokens[self.i]):
            self.next_token()
        if('IDENT' in self.tokens[self.i]):
            self.next_token()
        if('DEDENT' in self.tokens[self.i]):
            self.next_token()
        else:
            print("Erro sintatico na linha: " +self.linha_atual+"\n")

