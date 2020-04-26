#liveshare

import ply.lex as lex
import ply.yacc as yacc

from lex import tokens
import AbstrataClass as abstrat

def kotlinFile():
    '''kotlinFile: functionDeclaration kotlinFile
					| functionDeclaration'''

def functionDeclaration():
    '''functionDeclaration: FUN simpleIdentifier functionValueParameters LPAREN DOISP type RPAREN block
							| FUN simpleIdentifier functionValueParameters LPAREN DOISP type RPAREN 
							| FUN simpleIdentifier functionValueParameters LPAREN DOISP RPAREN block
							| FUN simpleIdentifier functionValueParameters LPAREN DOISP RPAREN '''
    
def typeParameters():
    '''typeParameters: MENOR tps MAIOR'''

def tps(): 
	'''tps: typeParameter 
			| typeParameter 
			LPAREN COMMA typeParameter RPAREN'''

def typeParameter():
  '''typeParameter: simpleIdentifier LPAREN DOISP type RPAREN 
					| simpleIdentifier LPAREN DOISP RPAREN'''

def functionValueParameters():
	'''functionValueParameters: LPAREN fvps RPAREN'''

def fvps():
	''' fvps: functionValueParameter 
				| functionValueParameter COMMA fvps
				| '''

def functionValueParameter():
  ''' functionValueParameter: parameter IGUALDADE expression
								| parameter '''

def variableDeclaration(): 
	'''variableDeclaration:  annot simpleIdentifier DOISP type
							| annot simpleIdentifier '''

							
def annot():
	'''annot: annotation
				| annotation annot
				| '''

def multiVariableDeclaration(): 
	''' LPAREN mvd RPAREN'''


def mvd():
	'''mvd: variableDeclaration 
			|  variableDeclaration COMMA mvd 
			| '''

def propertyDeclaration():
	'''propertyDeclaration: VAR multiVariableDeclaration IGUALDADE expression PV
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

def parameter(): 
	''' parameter: simpleIdentifier DOISP type '''
							
def type():
  '''type : typeModifiers optype 
			| optype '''

def opType(): '''optype: parenthesizedType | functionType | userType '''

def userType():
  ''' userType : simpleUserType '''

def simpleUserType()
  ''' simpleUserType: simpleIdentifier typeArguments
						| simpleIdentifier '''

def typeProjection(): 
  '''typeProjection: typeProjectionModifiers type
					| type '''

def typeProjectionModifiers():
   '''typeProjectionModifiers: typeProjectionModifier
								| typeProjectionModifier typeProjectionModifiers '''

def functionType():
  '''functionType: receiverType PONTO functionTypeParameters SETA type
					| functionTypeParameters SETA type '''
  


#  def functionTypeParameters():
#    ''' functionTypeParameters:
#          LPAREN parameter ftp RPAREN|LPAREN parameter ftp RPAREN
#    '''
#
#  def ftp():
#	  ''' ftp: COMMA parameter
#		  	  | COMMA type
#			  | '''

def parenthesizedType(): 
  '''parenthesizedType: COMMA type COMMA '''

def receiverType():
  '''receiverType: typeModifier rt '''

def rt():
	'''rt: parenthesizedType 
			| nullableType 
			| typeReference

def parenthesizedUserType():
  '''parenthesizedUserType: LPAREN userType RPAREN
						 | LPAREN parenthesizedUserType RPAREN '''

def statements (): 
  '''statements: statement 
				| statement statments
				| '''

def statement (): 
  '''statement : functionDeclaration 
				| assignment 
				| loopStatement 
				| expression '''

def controlStructureBody():
  '''controlStructureBody : block
						| statement'''

def block():
  '''block : LCHAVE statements RCHAVE '''

def loopStatement():
	'''loopStatement : forStatement
					| whileStatement
					| doWhileStatement '''

def forStatement():
  '''forStatement: FOR LPAREN multiVariableDeclaration IN expression RPAREN controlStructureBody
					|FOR LPAREN variableDeclaration IN expression RPAREN controlStructureBody
					|FOR LPAREN multiVariableDeclaration IN expression RPAREN 
					|FOR LPAREN variableDeclaration IN expression RPAREN '''


def whileStatement():
  ''' whileStatement: WHILE LPAREN expression RPAREN controlStructureBody
					|  WHILE LPAREN expression RPAREN PV '''

def doWhileStatement():
  ''' doWhileStatement: DO controlStructureBody WHILE LPAREN expression RPAREN
						|DO WHILE LPAREN expression RPAREN '''

def assignment(): 
  '''assignment: directlyAssignableExpression IGUALDADE expression
				| assignableExpression assignmentAndOperator expression '''

def semi ():
  ''' semi: EOF '''

def expression():
   ''' expression : disjunction '''

def disjunction(): 
   ''' disjunction: conjunction 
					| conjunction OR disjunction '''


def conjunction():
  '''conjunction: equality 
				|equality && conjunction '''
 

def equality():
  ''' equality : comparison 
				| comparison equalityOperator equality '''

def comparison(): 
   ''' comparison : infixOperation 
					| infixOperation comparisonOperator infixOperation '''

def infixOperation():
  '''infixOperation : elvisExpression io '''
  
def io():
	'''io: inOperator elvisExpression
			| isOperator type
			| '''

def elvisExpression()
  ''' elvisExpression : infixFunctionCall
						| infixFunctionCall elvis elvisExpression 
						| '''
  
# def elvis():
#   ''' elvis : DOISP
#				| '''
  
def infixFunctionCall():
  '''infixFunctionCall : rangeExpression 
						| rangeExpression simpleIdentifier infixFunctionCall '''
  
# MAIS UM OPERADOR '..' PONTOPONTO (PESQUISAR SOBRE)
def rangeExpression():
    ''' rangeExpression : additiveExpression
							| additiveExpression PONTOPONTO rangeExpression '''

def additiveExpression():
   ''' additiveExpression : multiplicativeExpression 
                            | multiplicativeExpression additiveOperator additiveExpression ''' 

def multiplicativeExpression():
  ''' multiplicativeExpression : asExpression 
								| asExpression multiplicativeOperator multiplicativeExpression '''

def asExpression():
   ''' asExpression : prefixUnaryExpression
                      | prefixUnaryExpression asOperator type '''

def prefixUnaryExpression():
  ''' prefixUnaryExpression : preue postfixUnaryExpression '''

def preue():
	''' preue : unaryPrefix
			| unaryPrefix preue
			| '''
  
def unaryPrefix():
   ''' unaryPrefix : annotation
					  | label
					  | prefixUnaryOperator '''

def postfixUnaryExpression():
   ''' postfixUnaryExpression : primaryExpression
								| primaryExpression posue '''

def posue():
	''' posue: postfixUnarySuffix
				| postfixUnarySuffix posue '''

def postfixUnarySuffix():
   ''' postfixUnarySuffix : postfixUnaryOperator
							  | typeArguments
							  | callSuffix
							  | indexingSuffix
							  | navigationSuffix '''
  
def directlyAssignableExpression():
   ''' directlyAssignableExpression : postfixUnaryExpression assignableSuffix
									  | simpleIdentifier
									  | parenthesizedDirectlyAssignableExpression '''

def parenthesizedDirectlyAssignableExpression():
   ''' parenthesizedDirectlyAssignableExpression : LPAREN directlyAssignableExpression RPAREN '''

def assignableExpression():
   ''' assignableExpression : prefixUnaryExpression
							 | parenthesizedAssignableExpression '''

def parenthesizedAssignableExpression()
   ''' parenthesizedAssignableExpression : LPAREN assignableExpression RPAREN '''

def assignableSuffix():
  ''' assignableSuffix : typeArguments
						  | indexingSuffix
						  | navigationSuffix'''

# NOVO TOKEN '[', ']' LCCT E RCCT
def indexingSuffix():
   ''' indexingSuffix : LCCT isuf RCCT '''

def isuf(): 
    ''' isuf : expression
				| expression COMMA isuf 
				| '''

def navigationSuffix(): 
   ''' navigationSuffix : memberAccessOperator simpleIdentifier CLASS
						| memberAccessOperator parenthesizedExpression CLASS '''
  
def callSuffix(): 
   '''callSuffix : typeArguments valueArguments annotatedLambda
					|  valueArguments annotatedLambda
					|  typeArguments  annotatedLambda
					|  annotatedLambda
					| typeArguments valueArguments
					| valueArguments '''
 
def annotatedLambda():
   ''' annotatedLambda : lambdaLiteral '''
 
def typeArguments():
	''' typeArguments : MENOR ta MAIOR'''

def ta():
	''' ta : typeProjection
			| typeProjection COMMA ta 
			| '''

def valueArguments():
   '''valueArguments : LPAREN RPAREN
					| LPAREN vas RPAREN '''
  

def vas():
   ''' vas: valueArgument 
			| valueArgument COMMA vas '''

def valueArgument():
   ''' valueArgument : annotation simpleIdentifier IGUALDADE MULT expression
					 | annotation simpleIdentifier IGUALDADE expression
					 | annotation expression
					 | simpleIdentifier IGUALDADE MULT expression
					 | simpleIdentifier IGUALDADE expression
					 | expression  '''

def primaryExpression():
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
  
def parenthesizedExpression():
 ''' parenthesizedExpression : LPAREN expression RPAREN '''
  

def collectionLiteral():
   ''' collectionLiteral : LCCT cl RCCT
							| LCCT RCCT '''
  
def cl():
	''' cl : expression 
			| expression COMMA cl '''

def literalConstant():
   ''' literalConstant : BooleanLiteral
						  | IntegerLiteral
						  | HexLiteral
						  | BinLiteral
						  | CharacterLiteral
						  | RealLiteral
						  | 'null'
						  | LongLiteral
						  | UnsignedLiteral '''

def stringLiteral():
   ''' stringLiteral: lineStringLiteral
					| multiLineStringLiteral '''

def lambdaLiteral():
   ''' lambdaLiteral : RCHAVE ll LCHAVE	'''

def ll(): 
	''' ll : statements
			| lambdaParameters SETA statements
			| SETA statements'''

def lambdaParameters():
  ''' lambdaParameters : lambdaParameter
						| lambdaParameter COMMA lambdaParameters '''

def lambdaParameter():
   ''' lambdaParameter : variableDeclaration
					| multiVariableDeclaration DOISP type
					| multiVariableDeclaration '''

def anonymousFunction():
	''' anonymousFunction : FUN af4 parametersWithOptionalType af3 af2 af1 

def af1(): 
    ''' af1 : functionBody
				| ''' 

def af2():
	''' af2 : typeConstraints
			| '''

def af3():
	''' af3: DOISP type
			| '''

def af4(): 
	''' af4 : type PONTO
			| '''

def functionLiteral():
   ''' functionLiteral : lambdaLiteral
						| anonymousFunction '''
 
def ifExpression():
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
def jumpExpression():
   ''' jumpExpression : THROW expression
						| RETURN expression
						| RETURN_AT expression 
						| expression
						| CONTINUE
					    | CONTINUE_AT
						| BREAK
						| BREAK_AT
  
def callableReference():
   ''' callableReference: receiverType DOISP DOISP simpleIdentifier 
						| DOISP DOISP simpleIdentifier
						| receiverType DOISP DOISP CLASS 
						| DOISP DOISP CLASS
  
# VERIFICAT TOKENS
def assignmentAndOperator(): 
   ''' assignmentAndOperator : MAISIGUAL	# +=
							  | MENOSIGUAL	# -=
							  | MULTIGUAL	# *=
							  | DIVIGUAL	# /=
							  | MODIGUAL	# %=	'''
  
def equalityOperator():
   ''' equalityOperator : DIFERENTE			# !=
						| IDENTIDADE		# ===
						| IGUALDADE			# ==
						| SEMIDENTIDADE		# !==		'''
  
def comparisonOperator():
   ''' comparisonOperator : MENOR
						  | MAIOR
						  | MENORIGUAL
						  | MAIORIGUAL '''
						  
def inOperator():
   ''' inOperator : IN
				| NOT_IN '''
  
def isOperator():
    '''isOperator : IS
				| NOT_IS '''
  
def additiveOperator():
   ''' additiveOperator : PLUS
						| MINUS	'''
  
def multiplicativeOperator():
	''' multiplicativeOperator : MULT
								| DIVIDE
								| MOD '''
  
  #duvida
def asOperator():
   ''' asOperator : AS
				| AS asOperator '''
  #DUVIDA
def prefixUnaryOperator():
   ''' prefixUnaryOperator : INCREMENTO
  | DECREMENTO
  | MINUS
  | PLUS
  | excl
  
def postfixUnaryOperator():
   ''' postfixUnaryOperator : INCREMENTO
							| DECREMENTO
  | '!' excl
  ;
excl (used by prefixUnaryOperator, postfixUnaryOperator)
  : '!'
  | EXCL_WS
  ;

def memberAccessOperator():
   ''' memberAccessOperator : PONTO
							| safeNav
							| COLONCOLON     '''

def safeNav():
   ''' safeNav : PONTO  '''

# Identifiers
# olhar tokens
def simpleIdentifier():
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
  
def identifier():
   ''' identifier : simpleIdentifier
					| simpleIdentifier PONTO identifier '''
  
