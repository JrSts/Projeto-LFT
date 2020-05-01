from Visitor import Visitor
from AbstrataClass import abstractmethod 
class SomaExp():
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, Visitor):
        Visitor.visitSomaExp(self)

class MulExp():
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, Visitor):
        Visitor.visitMulExp(self)

class PotExp():
    def __init__(self,exp2,exp3):
        self.exp2 = exp2
        self.exp3 = exp3
    def accept(self, Visitor):
        Visitor.visitPotExp(self) 

class CallExp():
    def __init__(self, call):
        self.call = call
    def accept(self, Visitor):
        Visitor.visitCallexp(self)
        
class AssignExp():
    def __init__(self,assign):
        self.assign = assign
    def accept(self,Visitor):
        Visitor.visitAssignExp(self)

class NumExp():
    def __init__(self,num):
        self.num = num
    def accept(self,Visitor):
        Visitor.visitorNumExp(self)
        
class IDExp ():
    def __init__(self,id):
        self.id = id
    def accept(self, Visitor):
        Visitor.visitIDExp(self)

class ParamsCall():
    def __init__(self,EXP,Params):
        self.EXP = EXP
        self.Params = Params
    def accept(self,Visitor):
        Visitor.visitParamsCall(self)
class SimplesCall():
    def __init__(self, ID):
        self.ID = ID
    def accept(self, Visitor):
        Visitor.visitSimplesCall(self)
class CompoundParams():
    def __init__(self,ID,Params):
        self.ID = ID
        self.Params = Params
    def accept(self,Visitor):
        Visitor.visitCompoundParams(self)
class SingleParam():
    def __init__(self, ID):
        self.ID = ID
    def accept(self, Visitor):
        Visitor.visitSingleParam(self)

class AssignExp():
    def __init__(self, ID,Exp):
        self.ID = ID
        self.Exp = Exp
    def accept(self , Visitor):
        Visitor.visitAssighExp(self)
###########################################################
class kotlinFile():
    def __init__(self):
        self
    def accept(self,visitor):
        visitor.visitkotlinFile(self)
###########################################################

class CompoundFunctionDeclaration(kotlinFile):
    def __init__(self, fd, kf):
        self.fd = fd
        self.kf = kf
    def accept(self, visitor):
        visitor.visitCompoundFunctionDeclaration(self)

class SimpleFunctionDeclaration(kotlinFile):
    def __init__(self, fd):
        self.fd = fd
    def accept(self, visitor):
        visitor.visitSimpleFunctionDeclaration(self)

class FunctionDeclaration(kotlinFile):
    def __init__(self, fun, SI, FVL, doisptype, block):
        self.fun=fun
        self.SI=SI
        self.FVL=FVL
        self.doisptype=doisptype
        self.block=block
    def accept(self,visitor):
        Visitor.visitFunctionDeclaration(self)
###########################################################

class SimpleFunctionBody(kotlinFile):
    def __init__(self, block):
        self.block = block
    def accept(self, visitor):
        Visitor.visitSimpleFunctionBody(self)

class CompoundFunctionBody(kotlinFile):
    def __init__(self, atribuicao, expression):
        self.atribuicao = atribuicao
        self.expression = expression
    def accept(self, visitor):
        Visitor.visitCompoundFunctionBody(self)
###########################################################

class SimpleFunctionValueParameters(kotlinFile):
    def __init__(self, lp, rp):
       self.rp = rp
       self.lp = lp
    def accept(self, visitor):
        visitor.visitSimpleFunctionValueParameters(self)

class CompoundFunctionValueParameters(kotlinFile):
    def __init__(self, lp, fvps, rp):
       self.rp = rp
       self.lp = lp
       self.fvps=fvps
    def accept(self, visitor):
        visitor.visitCompoundFunctionValueParameters(self)
################################################################

class SimpleFvps(SimpleFunctionValueParameters):
    def __init__(self, fvps):
        self.fvps=fvps
    def accept(self, visitor):
        visitor.visitSimpleFvps(self)

class COMMAFvps(CompoundFunctionValueParameters):
    def __init__(self, fvp,COMMA, fvps):
        self.fvp=fvp
        self.COMMA=COMMA
        self.fvps=fvps
    def accept(self, visitor):
        visitor.visitCompoundFvps(self)

class CompoundFvps(CompoundFunctionValueParameters):
    def __init__(self, fvp, fvps):
        self.fvp=fvp
        self.fvps=fvps
    def accept(self, visitor):
        visitor.visitCompoundFvps(self)
###################################################################

class SimpleFunctionValeuParameter(kotlinFile):
    def __init__(self, parameter):
        self.Parameter=parameter
    def accept(self,visitor):
        visitor.visitSimpleFunctionValueParameter(self)
        
class CompoundFunctionValeuParameter(kotlinFile):
    def __init__(self, parameter, atribuicao, exp):
        self.Parameter=parameter
        self.atribuicao=atribuicao
        self.exp=exp
    def accept(self,visitor):
        visitor.visitCompoundFunctionValueParameter(self)
#####################################################################

class SimpleVariableDeclaration(kotlinFile):
    def __init__(self, simpleIdentifier):
        self.simpleIdentifier = simpleIdentifier
    def accept(self, visitor):
        visitor.visitSimpleVariableDeclaration(self)

class CompoundVariableDeclaration(kotlinFile):
    def __init__(self, simpleIdentifier, DOISP, type):
        self.simpleIdentifier = simpleIdentifier
        self.DOISP=DOISP
        self.type=type
    def accept(self, visitor):
        visitor.visitvariableDeclaration(self)
#################################################################

class SimpleMultiVariableDeclaration(kotlinFile):
    def __init__(self, LP, RP):
        self.LP=LP
        self.RP=RP
    def accept(self, visitor):
        visitor.visitSimpleMultiVariableDeclaration(self)

class CompoundMultiVariableDeclaration(kotlinFile):
    def __init__(self, LP, mvd, RP):
        self.LP=LP
        self.RP=RP
        self.mvd=mvd
    def accept(self, visitor):
        visitor.visitCompoundMultiVariableDeclaration(self)
###################################################################

class SimpleMvd(SimpleMultiVariableDeclaration):
    def __init__(self, variableDeclaration):
        self.variableDeclaration=variableDeclaration
    def accept(self, visitor):
        visitor.visitSimpleMvd(self)

class CompoundMvd(CompoundMultiVariableDeclaration):
    def __init__(self, variableDeclaration, COMMA, mvd ):
        self.mvd=mvd
        self.COMMA=COMMA
        self.variableDeclaration=variableDeclaration
    def accept(self, visitor):
        visitor.visitCompoundMvd(self)
####################################################################

class Parameter(kotlinFile):
    def __init__(self,simpleIdentifier, DOISP, type ):
        self.simpleIdentifier= simpleIdentifier
        self.doisp= DOISP
        self.type=type
    def accept(self, visitor):
        visitor.visitParameter(self)
######################################################################
class  CompoundType(kotlinFile):
    def __init__(self,typeModifiers, optype ):
        self.typeModifiers=typeModifiers  
        self.optype=optype
    def accept(self, visitor):
        visitor.visitCompoundType(self)

class SimpleType(kotlinFile):
    def __init__(self,optype):
        self.optype=optype
    def accept (self, visitor):
        visitor.visitSimpleType(self)
#######################################################################

class CallParenthesizedType():
    def __init__(self, parenthesizedType):
        self.parenthesizedType =parenthesizedType
    def accept(self, visitor):
        Visitor.visitCallParenthesizedType(self)

class CallFunctionType():
    def __init__(self, functionType):
        self.functionType =functionType
    def accept(self, visitor):
        Visitor.visitCallFunctionType(self)

class CallUserType():
    def __init__(self, userType):
        self.userType =userType
    def accept(self, visitor):
        Visitor.visitCallUserType(self)
#######################################################################

class SimpleTypeModifiers(kotlinFile):
    def __init__ (self, typeModifier):
        self.typeModifier = typeModifier
    def accepr(self, visitor):
        Visitor.visitSimpleTypeModifiers(self)

class CompondTypeModifiers(kotlinFile):
    def __init__ (self, typeModifier, typeModifiers):
        self.typeModifier = typeModifier
        self.typeModifiers = typeModifiers
    def accepr(self, visitor):
        Visitor.visitCompoundTypeModifiers(self)
#########################################################################

class TypeModifiers(kotlinFile):
    def __init__ (self, suspend):
        self.suspend = suspend
    def accepr(self, visitor):
        Visitor.visitTypeModifier(self)
#########################################################################

class TypeProjectionModifier(kotlinFile):
    def __init__(self, varianceModifier):
        self.varianceModifier = varianceModifier
    def accept(self, visitor):
        Visitor.visitTypeProjectionModifier(self)
##########################################################################

class CallIn():
    def __init__(self, CallIn):
        self.CallIn = CallIn
    def accept(self, visitor):
        Visitor.visitCallIn(self)

class CallOut():
    def __init__(self, CallOut):
        self.CallOut = CallOut
    def accept(self, visitor):
        Visitor.visitCallOut(self)
########################################################################

class userType(kotlinFile):
    def __init__(self,simpleUserType):
        self.simpleUserType=simpleUserType
    def accept(self, visitor):
        visitor.visituserType(self)
##########################################################################

class SimpleSimpleUserType(userType):
    def __init__(self, simpleUserType):
        self.simpleUserType=simpleUserType
    def accept(self, visitor):
        visitor.visitSimpleSimpleUserType(self)

class CompoundSimpleUserType(userType):
    def __init__(self, simpleUserType,typeArguments):
        self.simpleUserType=simpleUserType
        self.typeArguments=typeArguments
    def accept(self, visitor):
        visitor.visitCompoundSimpleUserType(self)
##########################################################################

class SimpleTypeProjection(kotlinFile):
    def __init__(self, type):
        self.type=type
    def accept(self,visitor):
        visitor.visittypeSimpleProjection(self)

class CompoundTypeProjection(kotlinFile):
    def __init__(self, typeProjectionModifiers, type):
        self.typeProjectionModifiers= typeProjectionModifiers
        self.type=type
    def accept(self,visitor):
        visitor.visitCompoundTypeProjection(self)
########################################################################

class SimpleTypeProjectionModifiers(SimpleTypeProjection):
    def __init__(self, typeProjection):
        self.typeProjection=typeProjection
    def accept(self, visitor):
        visitor.visitSimpleTypeProjectionModifiers(self)

class CompoundTypeProjectionModifiers(CompoundTypeProjection):
    def __init__(self, typeProjectionModifier, typeProjectionModifiers):
        self.typeProjectionModifier =typeProjectionModifier
        self.typeProjectionModifiers=typeProjectionModifiers
    def accept(self, visitor):
        visitor.visitCompoundTypeProjectionModifiers(self)
########################################################################

class SimpleFunctionType(kotlinFile):
    def __init__(self, functionTypeParameters, SETA, type):
        self.functionTypeParameters=functionTypeParameters
        self.SETA=SETA
        self.type=type
    def accept(self, visitor):
        visitor.visitSimpleFunctionType(self)

class CompoundFunctionType(kotlinFile):
    def __init__(self, receiverType, PONTO, functionTypeParameters, SETA, type):
        self.receiverType= receiverType
        self.PONTO=PONTO
        self.functionTypeParameters=functionTypeParameters
        self.SETA=SETA
        self.type=type
    def accept(self, visitor):
        visitor.visitCompoundFunctionType(self)
########################################################################

class SimpleFunctionTypeParameters_p(kotlinFile):
    def __init__(self, lp, parameter, rp):
        self.lp = lp
        self.parameter = parameter
        self.rp = rp
    def accept(self, visitor):
        Visitor.visitSimpleFunctionTypeParameters_p()

class CompoundFunctionTypeParameters_p(kotlinFile):
    def __init__(self, lp, parameter, ftp, rp):
        self.lp = lp
        self.parameter = parameter
        self.ftp = ftp
        self.rp = rp
    def accept(self, visitor):
        Visitor.visitCompoundFunctionTypeParameters_p()
########################################################################

class SimpleFunctionTypeParameters_t(kotlinFile):
    def __init__(self, lp, type, rp):
        self.lp = lp
        self.type = type
        self.rp = rp
    def accept(self, visitor):
        Visitor.visitSimpleFunctionTypeParameters_t()

class CompoundFunctionTypeParameters_t(kotlinFile):
    def __init__(self, lp, type, ftp, rp):
        self.lp = lp
        self.type = type
        self.ftp = ftp
        self.rp = rp
    def accept(self, visitor):
        Visitor.visitCompoundFunctionTypeParameters_t()
########################################################################

class CallParameter():
    def __init__(self, CallParameter):
        self.CallParameter = CallParameter   
    def accept(self, visitor):
        Visitor.visitCallParameter(self)

class CallType():
    def __init__(self, CallType):
        self.CallType = CallType   
    def accept(self, visitor):
        Visitor.visitCallType(self)
########################################################################

class parenthesizedType(kotlinFile):
    def __init__(self, LPAREN, type,RPAREN ):
        self.LPAREN=LPAREN
        self.type=type
        self.RPAREN=RPAREN
    def accept(self, visitor):
        visitor.visitparenthesizedType(self)
########################################################################
        
class receiverType(kotlinFile):
    def __init__(self, typeModifier, rt):
        self.typeModifier=typeModifier
        self.rt=rt
    def accept(self, visitor):
        visitor.visitreceiverType(self)
########################################################################
       
class rt(receiverType):
    def __init__(self, parenthesizedType):
        self. parenthesizedType= parenthesizedType
    def accept(self, visitor):
        visitor.visitrt(self)
########################################################################

class SimpleStatements (kotlinFile):
    def __init__(self, statement):
        self.statement=statement
    def accept(self, visitor):
        visitor.visitSimpleStatemnts(self)

class CompoundStatements (kotlinFile):
    def __init__(self, statement, statments):
        self.statement=statement
        self.statments=statments
    def accept(self, visitor):
        visitor.visitCompoundStatemnts(self)
########################################################################

class CallFunctionDeclaration():
    def __init__(self, CallFunctionDeclaration):
        self.CallFunctionDeclaration = CallFunctionDeclaration
    def accept(self, visitor):
        Visitor.visitCallFunctionDeclaration(self)

class CallAssignment():
    def __init__(self, CallAssignment):
        self.CallAssignment = CallAssignment
    def accept(self, visitor):
        Visitor.visitCallAssignment(self)

class CallLoopStatement():
    def __init__(self, CallLoopStatement):
        self.CallLoopStatement = CallLoopStatement
    def accept(self, visitor):
        Visitor.visitCallLoopStatement(self)

class CallExpression():
    def __init__(self, CallExpression):
        self.CallExpression = CallExpression
    def accept(self, visitor):
        Visitor.visitCallExpression(self)
########################################################################

class CallBlock():
    def __init__(self, block):
        self.block = CallBlock
    def accept(self, visitor):
        Visitor.visitCallBlock(self)

class CallStatement():
    def __init__(self, statement):
        self.statement = statement
    def accept(self, visitor):
        Visitor.visitCallStatement(self)
########################################################################

class block(CallBlock, CallStatement):
    def __init__(self,LCHAVE, statements, RCHAVE):
        self.LCHAVE=LCHAVE
        self.statements=statements
        self.RCHAVE=RCHAVE
    def accept(self, visitor):
        visitor.visitblock(self)
########################################################################

class CallForStatement_MD():
    def __init__(self, forStatement):
        self.forStatement = forStatement
    def accept(self, visitor):
        Visitor.visitCallForStatement_MD(self)
       
class CallForStatement_VD():
    def __init__(self, forStatement):
        self.forStatement = forStatement
    def accept(self, visitor):
        Visitor.visitCallForStatement_VD(self)

class CallWhileStatement():
    def __init__(self, whileStatement):
        self.whileStatement = whileStatement
    def accept(self, visitor):
        Visitor.visitCallWhileStatementD(self)

class CallDoWhileStatement():
    def __init__(self, doWhileStatement):
        self.doWhileStatement = doWhileStatement
    def accept(self, visitor):
        Visitor.visitCallDoWhileStatement(self)
########################################################################

class SimpleForStatement_MD(CallForStatement_MD, CallForStatement_VD, CallWhileStatement, CallDoWhileStatement):
    def __init__(self, FOR, LPAREN, multiVariableDeclaration, IN, expression, RPAREN):
        self.FOR=FOR
        self.LPAREN=LPAREN
        self.multiVariableDeclaration=multiVariableDeclaration
        self.IN=IN
        self.expression=expression
        self.RPAREN=RPAREN
    def accept(self, visitor):
        visitor.visitSimpleForStatement_MD(self)

class CompoundForStatement_MD(CallForStatement_MD, CallForStatement_VD, CallWhileStatement, CallDoWhileStatement):
    def __init__(self, FOR, LPAREN, multiVariableDeclaration, IN, expression, RPAREN, controlStructureBody):
        self.FOR=FOR
        self.LPAREN=LPAREN
        self.multiVariableDeclaration=multiVariableDeclaration
        self.IN=IN
        self.expression=expression
        self.RPAREN=RPAREN
        self.controlStructureBody=controlStructureBody
    def accept(self, visitor):
        visitor.visitCompoundForStatement_MD(self)

class SimpleForStatement_VD(CallForStatement_MD, CallForStatement_VD, CallWhileStatement, CallDoWhileStatement):
    def __init__(self, FOR, LPAREN, variableDeclaration, IN, expression, RPAREN):
        self.FOR=FOR
        self.LPAREN=LPAREN
        self.variableDeclaration=variableDeclaration
        self.IN=IN
        self.expression=expression
        self.RPAREN=RPAREN
    def accept(self, visitor):
        visitor.visitSimpleForStatement_MD(self)

class CompoundForStatement_VD(CallForStatement_MD, CallForStatement_VD, CallWhileStatement, CallDoWhileStatement):
    def __init__(self, FOR, LPAREN, multiVariableDeclaration, IN, expression, RPAREN, controlStructureBody):
        self.FOR=FOR
        self.LPAREN=LPAREN
        self.variableDeclaration=variableDeclaration
        self.IN=IN
        self.expression=expression
        self.RPAREN=RPAREN
        self.controlStructureBody=controlStructureBody
    def accept(self, visitor):
        visitor.visitCompoundForStatement_MD(self)
########################################################################

class CallPv():
    def __init__(self, WHILE, LPAREN, expression, RPAREN, pv):
        self.WHILE=WHILE
        self.LPAREN=LPAREN
        self.expression=expression
        self.RPAREN=RPAREN
        self.pv = pv
    def accept(self, visitor):
        Visitor.visitCallPv(self)

class CallCSB():
    def __init__(self, WHILE, LPAREN, expression, RPAREN, csb):
        self.WHILE=WHILE
        self.LPAREN=LPAREN
        self.expression=expression
        self.RPAREN=RPAREN
        self.csb = csb
    def accept(self, visitor):
        Visitor.visitCallCSB(self)
########################################################################
        
class SimpleDoWhileStatement(CallForStatement_MD, CallForStatement_VD, CallWhileStatement, CallDoWhileStatement):
    def __init__(self,DO, WHILE ,LPAREN, expression, RPAREN): 
        self.do=DO
        self.WHILE=WHILE 
        self.LPAREN=LPAREN
        self.expression=expression
        self. RPAREN= RPAREN
    def accept(self, visitor):
        visitor.visitSimpleDoWhileStatement(self)

class CompoundDoWhileStatement(CallForStatement_MD, CallForStatement_VD, CallWhileStatement, CallDoWhileStatement):
    def __init__(self,DO, controlStructureBody, WHILE ,LPAREN, expression, RPAREN): 
        self.do=DO
        self.controlStructureBody=controlStructureBody
        self.WHILE=WHILE 
        self.LPAREN=LPAREN
        self.expression=expression
        self. RPAREN= RPAREN
    def accept(self, visitor):
        visitor.visitCompoundDoWhileStatement(self)
########################################################################
        
class CallIgualdade():
    def __init__(self,directlyAssignableExpression, igualdade, expression):
        def __init__(self,directlyAssignableExpression, IGUALDADE ,expression): 
            self.directlyAssignableExpression=directlyAssignableExpression
            self.expression=expression
            self.igualdade = igualdade
        def accept(self, visitor):
            Visitor.visitCallIgualdade(self)

class CallAssignmentAndOperator():
    def __init__(self, assignableExpression, assignmentAndOperator, expression):
        def __init__(self,directlyAssignableExpression, IGUALDADE ,expression): 
            self.assignmentAndOperator=assignmentAndOperator
            self.expression=expression
            self.assignableExpression = assignableExpression
        def accept(self, visitor):
            Visitor.visitCallAssignableExpression(self)
########################################################################
        
class Expression(kotlinFile):
    def __init__(self,disjunction ):
        self.disjunction =disjunction 
    def accept (self,visitor):
        visitor.visitExpression(self)
########################################################################
        
class SimpleDisjunction(Expression):
    def __init__(self,conjunction):
        self.conjunction=conjunction
    def accept (self,visitor):
        visitor.visitSimpleDisjunction(self)
       
class CompoundDisjunction(Expression):
    def __init__(self,conjunction ,OR, disjunction):
        self.conjunction=conjunction
        self.OR=OR
        self.disjunction=disjunction
    def accept (self,visitor):
        visitor.visitCompoundDisjunction(self)
########################################################################
        
class SimpleConjunction(SimpleDisjunction):
    def __init__(self,equality):
        self.equality=equality
    def accept (self,visitor):
        visitor.vistSimpleConjunction(self)

class CompoundConjunction(CompoundDisjunction):
    def __init__(self, equality, conjunction, AND):
        self.equality = equality
        self.conjunction = conjunction
        self.AND = AND
    def accept(self, visitor):
        visitor.vistCompoundConjunction(self)
########################################################################
        
class SimpleEquality(SimpleConjunction):
    def __init__(self,comparison):
        self.comparison=comparison
    def accept(self,visitor):
        visitor.visitSimpleEquality(self)

class CompoundEquality(CompoundConjunction):
    def __init__(self,comparison, equalityOperator, equality):
        self.comparison=comparison
        self.equalityOperator=equalityOperator
        self.equality=equality
    def accept(self,visitor):
        visitor.visitCompoundEquality(self)
########################################################################
        
class SimpleComparison(SimpleEquality):
    def __init__(self, infixOperation):
        self.infixOperation=infixOperation
    def accept (self,visitor):
        visitor.vistSimpleComparison(self)
    
class CompoundComparison(CompoundEquality):
    def __init__(self, infixOperation, comparisonOperator):
        self.infixOperation=infixOperation
        self.comparisonOperator=comparisonOperator
    def accept (self,visitor):
        visitor.vistCompoundComparison(self)
########################################################################
        
class SimpleInfixOperation(SimpleComparison,CompoundComparison):
    def __init__(self,elvisExpression):
        self.elvisExpression=elvisExpression
    def accept (self,visitor):
        visitor.visitSimpleInfixOperation(self)
        
class CompoundInfixOperation(SimpleComparison,CompoundComparison):
    def __init__(self,elvisExpression, io):
        self.elvisExpression=elvisExpression
        self.io=io
    def accept (self,visitor):
        visitor.visitCompoundInfixOperation(self)
########################################################################
        
class CallInOperator():
    def __init__(self, inOperator):
        self.isOperator = CallIsOperator        
        self.elvisExpression=elvisExpression    
    def accept(self, visitor):
        Visitor.visitCallInOperator(self)

class CallIsOperator():
    def __init__(self, isOperator):
        self.isOperator = CallIsOperator        
        self.type=type    
    def accept(self, visitor):
        Visitor.visitCallIsOperator(self)

class CallInOperator1():
    def __init__(self, inOperator, io):
        self.isOperator = CallIsOperator        
        self.elvisExpression=elvisExpression  
        self.io = io
    def accept(self, visitor):
        Visitor.visitCallInOperator1(self)

class CallIsOperator1():
    def __init__(self, isOperator, io):
        self.isOperator = CallIsOperator        
        self.type=type    
        self.io = io
    def accept(self, visitor):
        Visitor.visitCallIsOperator1(self)
########################################################################
    
class SimpleElvisExpression(io):
    def __init__(self,infixFunctionCall):
        self.infixFunctionCall=infixFunctionCall
    def accept(self,visitor):
        visitor.visitSimpleElvisExpression(self)

class CompoundElvisExpression(io):
    def __init__(self,infixFunctionCall, elvis, elvisExpression ):
        self.infixFunctionCall=infixFunctionCall
        self.elvis=elvis
        self.elvisExpression=elvisExpression
    def accept(self,visitor):
        visitor.visitCompoundElvisExpression(self)
########################################################################
    
class SimpleInfixFunctionCall(SimpleElvisExpression):
    def __init__(self,rangeExpression):
        self.rangeExpression=rangeExpression
    def accept (self,visitor):
        visitor.visitSimpleInfixFunctionCall(self)
        
class CompoundInfixFunctionCall(CompoundElvisExpression):
    def __init__(self,rangeExpression, simpleIdentifier, infixFunctionCall):
        self.rangeExpression=rangeExpression
        self.simpleIdentifier=simpleIdentifier
        self.infixFunctionCall=infixFunctionCall
    def accept (self,visitor):
        visitor.visitCompoundInfixFunctionCall(self)
########################################################################
        
class SimpleRangeExpression(SimpleInfixFunctionCall):
    def __init__(self,additiveExpression):
        self.additiveExpression=additiveExpression
    def accept(self, visitor):
        visitor.visitSimpleRangeExpression(self)
    
class CompoundRangeExpression(CompoundInfixFunctionCall):
    def __init__(self,additiveExpression, PONTOPONTO, rangeExpression):
        self.additiveExpression=additiveExpression
        self.PONTOPONTO=PONTOPONTO
        self.rangeExpression=rangeExpression
    def accept(self, visitor):
        visitor.visitCompoundRangeExpression(self)
########################################################################
        
class SimpleAdditiveExpression(SimpleRangeExpression):
    def __init__(self,multiplicativeExpression):
        self.multiplicativeExpression=multiplicativeExpression
    def accept (self,visitor):
        visitor.visitSimpleAdditiveExpression(self)
    
class CompoundAdditiveExpression(CompoundRangeExpression):
    def __init__(self,multiplicativeExpression ,additiveOperator, additiveExpression):
        self.multiplicativeExpression=multiplicativeExpression
        self.additiveOperator=additiveOperator
        self.additiveExpression=additiveExpression
    def accept (self,visitor):
        visitor.visitCompoundAdditiveExpression(self)
########################################################################
        
class SimpleMultiplicativeExpression(SimpleAdditiveExpression):
    def __init__(self,asExpression):
        self.asExpression=asExpression
    def accept(self, visitor):
        visitor.visitSimpleMultiplicativeExpression(self)
        
class CompoundMultiplicativeExpression(CompoundAdditiveExpression):
    def __init__(self,asExpression ,multiplicativeOperator, multiplicativeExpression):
        self.asExpression=asExpression
        self.multiplicativeOperator=multiplicativeOperator
        self.multiplicativeExpression=multiplicativeExpression
    def accept(self, visitor):
        visitor.visitCompoundMultiplicativeExpression(self)
########################################################################
        
class SimpleAsExpression(SimpleMultiplicativeExpression):
    def __init__(self,prefixUnaryExpression, asOperator, type):
        self.prefixUnaryExpression=prefixUnaryExpression
    def accept (self, visitor):
        visitor.visitSimpleAsExpression(self)
        
class CompoundAsExpression(CompoundMultiplicativeExpression):
    def __init__(self,prefixUnaryExpression, asOperator, type):
        self.prefixUnaryExpression=prefixUnaryExpression
        self.asOperator=asOperator
        self.type=type
    def accept (self, visitor):
        visitor.visitCompoundAsExpression(self)
########################################################################
        
class SimplePrefixUnaryExpression(SimpleAsExpression,CompoundAsExpression):
    def __init__(self, postfixUnaryExpression):
        self.postfixUnaryExpression=postfixUnaryExpression
    def accept(self,visitor):
        visitor.visitSimplePrefixUnaryExpression(self)

class SimplePrefixUnaryExpression(SimpleAsExpression,CompoundAsExpression):
    def __init__(self,preue, postfixUnaryExpression):
        self.preue=preue
        self.postfixUnaryExpression=postfixUnaryExpression
    def accept(self,visitor):
        visitor.visitCompoundPrefixUnaryExpression(self)
########################################################################
        
class SimplePreue(PrefixUnaryExpression):
    def __init__(self,unaryPrefix ,preue):
        self.unaryPrefix=unaryPrefix
    def accept(self, visitor):
        visitor.visitSimplePreue(self)

class CompoundPreue(PrefixUnaryExpression):
    def __init__(self,unaryPrefix ,preue):
        self.unaryPrefix=unaryPrefix
        self.preue=preue
    def accept(self, visitor):
        visitor.visitCompoundPreue(self)
########################################################################
        
class CallPrefixUnaryOperator():
    def __init__(self, prefixUnaryOperator):
        self.prefixUnaryOperator = prefixUnaryOperator
    def accept(self, visitor):
        Visitor.visitCallPrefixUnaryOperator(self)

class CallLabel():
    def __init__(self, label):
        self.label = label
    def accept(self, visitor):
        Visitor.visitCallLabel(self)
########################################################################

class Lable(kotlinFile):
    def __init__(self, simpleIdentifier):
        self.simpleIdentifier = simpleIdentifier
    def accept(self, visitor):
        Visitor.visitLable(self)
########################################################################

class SimplePostfixUnaryExpression(kotlinFile):
    def __init__(self,primaryExpression ,posue):
        self.primaryExpression=primaryExpression
    def accept(self, visitor):
        visitor.visitSimplePostfixUnaryExpression(self)
   
class CompoundPostfixUnaryExpression(kotlinFile):
    def __init__(self,primaryExpression ,posue):
        self.primaryExpression=primaryExpression
        self.posue=posue
    def accept(self, visitor):
        visitor.visitCompoundPostfixUnaryExpression(self)
########################################################################

class SinglePosue(SimplePostfixUnaryExpression):
    def __init__(self,postfixUnarySuffix):
        self.postfixUnarySuffix=postfixUnarySuffix
    def accept(self,visitor):
        visitor.visitSinglePosue(self)
        
class CompoundPosue(CompoundPostfixUnaryExpression):
    def __init__(self,postfixUnarySuffix, posue):
        self.postfixUnarySuffix=postfixUnarySuffix
        self.posue=posue
    def accept(self,visitor):
        visitor.visitCompoundPosue(self)
########################################################################

class CallPostfixUnaryOperator():
    def __init__(self, postfixUnaryOperator):
        self.postfixUnaryOperator =postfixUnaryOperator
    def accept(self, visitor):
        Visitor.visitCallPostfixUnaryOperator(self)

class CallTypeArguments():
    def __init__(self, typeArguments):
        self.typeArguments =typeArguments
    def accept(self, visitor):
        Visitor.visitCallTypeArguments(self)

class CallIndexingSuffix():
    def __init__(self, indexingSuffix):
        self.indexingSuffix =indexingSuffix
    def accept(self, visitor):
        Visitor.visitCallIndexingSuffix(self)

class CallNavigationSuffix():
    def __init__(self, navigationSuffix):
        self.navigationSuffix =navigationSuffix
    def accept(self, visitor):
        Visitor.visitCallNavigationSuffix(self)

class CallCallSuffix():
    def __init__(self, callSuffix):
        self.callSuffix =callSuffix
    def accept(self, visitor):
        Visitor.visitCallCallSuffix(self)
########################################################################

class CallSimpleIdentifier():
    def __init__(self, simpleIdentifier):
        self.simpleIdentifier = simpleIdentifier
    def accept(self, visitor):
        Visitor.visitCallSimpleIdentifier(self)

class CallParenthesizedDirectlyAssignableExpression():
    def __init__(self, CallParenthesizedDirectlyAssignableExpression):
        self.CallParenthesizedDirectlyAssignableExpression = CallParenthesizedDirectlyAssignableExpression
    def accept(self, visitor):
        Visitor.visitCallParenthesizedDirectlyAssignableExpression(self)

class SimpleDirectlyAssignableExpression(SimplePostfixUnaryExpression,CompoundPostfixUnaryExpression):
    def __init__(self,simpleIdentifier):
        self.simpleIdentifier=simpleIdentifier
    def accept(self, visitor):
        visitor.visitSimpleDirectlyAssignableExpression(self)
########################################################################
        
class ParenthesizedDirectlyAssignableExpression(directlyAssignableExpression):
    def __init__(self,LPAREN, directlyAssignableExpression, RPAREN):
        self.LPAREN=LPAREN
        self.directlyAssignableExpression=directlyAssignableExpression
        self.RPAREN=RPAREN
    def accept(self,visitor):
        visitor.visitParenthesizedDirectlyAssignableExpression(self)
########################################################################
        
class CallParenthesizedAssignableExpression():
    def __init__(self, parenthesizedAssignableExpression):
        self.parenthesizedAssignableExpression = parenthesizedAssignableExpression
    def accept(self, visitor):
        Visitor.visitCallParenthesizedAssignableExpression(self)

class CallPrefixUnaryExpression():
    def __init__(self, prefixUnaryExpression):
        self.prefixUnaryExpression = prefixUnaryExpression
    def accept(self, visitor):
        Visitor.visitCallPrefixUnaryExpression(self)
########################################################################
        
class ParenthesizedAssignableExpression(assignableExpression):
    def __init__(self, LPAREN, assignableExpression, RPAREN):
        self.LPAREN=LPAREN
        self.assignableExpression=assignableExpression
        self.RPAREN= RPAREN
    def accept(self, visitor):
        visitor.visitparenthesizedAssignableExpression(self)
########################################################################

class CallNavigationSuffix():
    def __init__(self, navigationSuffix):
        self.navigationSuffix = navigationSuffix
    def accept(self, visitor):
        Visitor.visitCallNavigationSuffix(self)

class CallTypeArguments():
    def __init__(self, typeArguments):
        self.typeArguments = typeArguments
    def accept(self, visitor):
        Visitor.visitCallTypeArguments(self)

class CallIndexingSuffix():
    def __init__(self, indexingSuffix):
        self.indexingSuffix = indexingSuffix
    def accept(self, visitor):
        Visitor.visitCallIndexingSuffix(self)
###########################################################duvida
 
class SimpleIndexingSuffix(kotlinFile):
    def __init__(self,LCCT, RCCT):
        self.LCCT=LCCT
        self.RCCT=RCCT
    def accept(self,visitor):
        visitor.visitSimpleIndexingSuffix(self)       

class CompoundIndexingSuffix(kotlinFile):
    def __init__(self,LCCT, isuf, RCCT):
        self.LCCT=LCCT
        self.isuf=isuf
        self.RCCT=RCCT
    def accept(self,visitor):
        visitor.visitCompoundIndexingSuffix(self)
########################################################################

class SimpleIsuf(IndexingSuffix):
    def __init__(self,expression ):
        self.expression=expression
    def accept(self,visitor):
        visitor.visitSimpleIsuf(self)
        
class CompoundIsuf(IndexingSuffix):
    def __init__(self,expression, COMMA, isuf ):
        self.expression=expression
        self.COMMA=COMMA
        self.isuf=isuf
    def accept(self,visitor):
        visitor.visitCompoundIsuf(self)
########################################################################
        
class CallParenthesizedExpression():
    def __init__(self, memberAccessOperator, parenthesizedExpression, CLASS):
        self.memberAccessOperator=memberAccessOperator
        self.parenthesizedExpression = parenthesizedExpression
        self.CLASS=CLASS
    def accept(self, visitor):
        Visitor.visitCallParenthesizedExpression(self)
########################################################################
        
class CallValueArguments1():
    def __init__(self, valueArguments):
        self.valueArguments = valueArguments
    def accept(self, visitor):
        Visitor.visitCallValueArguments1(self)

class CallValueArguments2():
    def __init__(self, valueArguments, annotatedLambda):
        self.valueArguments = valueArguments
        self.annotatedLambda = annotatedLambda
    def accept(self, visitor):
        Visitor.visitCallValueArguments2(self)

class CallValueArguments3():
    def __init__(self, typeArguments, valueArguments, annotatedLambda):
        self.valueArguments = valueArguments
        self.annotatedLambda = annotatedLambda
        self.typeArguments = typeArguments
    def accept(self, visitor):
        Visitor.visitCallValueArguments3(self)

class CallAnnotatedLambda():
    def __init__(self, annotatedLambda):
        self.annotatedLambda = annotatedLambda
    def accept(self, visitor):
        Visitor.visitCallAnnotatedLambda(self)

class CallAnnotatedLambda2():
    def __init__(self, typeArguments, annotatedLambda):
        self.typeArguments = typeArguments
        self.annotatedLambda = annotatedLambda
    def accept(self, visitor):
        Visitor.visitCallAnnotatedLambda2(self)
########################################################################

class AnnotatedLambda(kotlinFile):
    def __init__(self,lambdaLiteral):
        self.lambdaLiteral=lambdaLiteral
    def accept(self,visitor):
        visitor.visitannotatedLambda(self)
########################################################################
        
class SimpleTypeArguments(kotlinFile):
    def __init__(self,MENOR, MAIOR):
        self.MENOR=MENOR
        self.MAIOR=MAIOR
    def accept(self,visitor):
        visitor.visitSimpleTypeArguments(self)

class CompoundTypeArguments(kotlinFile):
    def __init__(self,MENOR ,ta, MAIOR):
        self.MENOR=MENOR
        self.ta=ta
        self.MAIOR=MAIOR
    def accept(self,visitor):
        visitor.visitCompoundTypeArguments(self)
########################################################################
        
class SimpleTa(TypeArguments):
    def __init_(self,typeProjection):
        self.typeProjection=typeProjection
        self.COMMA=COMMA
    def accept (self, visitor):
        visitor.visitSimpleTa(self)
        
class CompoundTa(TypeArguments):
    def __init_(self,typeProjection, COMMA, ta):
        self.typeProjection=typeProjection
        self.COMMA=COMMA
        self.ta=ta
    def accept (self, visitor):
        visitor.visitCompoundTa(self)
########################################################################
        
class SimpleValueArguments(kotlinFile):
    def __init__(self,LPAREN, RPAREN):
        self.LPAREN=LPAREN
        self.RPAREN=RPAREN
    def accept(self, visitor):
        visitor.visitSimpleValueArguments(self)
        
class CompoundValueArguments(kotlinFile):
    def __init__(self,LPAREN, vas, RPAREN):
        self.LPAREN=LPAREN
        self.vas=vas
        self.RPAREN=RPAREN
    def accept(self, visitor):
        visitor.visitCompoundValueArguments(self)
########################################################################
        
class SimpleVas(SimpleValueArguments):
    def __init__(self,valueArgument):
        self.valueArgument=valueArgument
    def accept(self,visitor):
        visitor.visitSimpleVas(self)
        
class CompoundVas(CompoundValueArguments):
    def __init__(self,valueArgument ,COMMA, vas):
        self.valueArgument=valueArgument
        self.COMMA=COMMA
        self.vas=vas
    def accept(self,visitor):
        visitor.visitCompoundVas(self)
########################################################################
        
class SimpleValueArgument(SimpleVas):
    def __init__(self,simpleIdentifier):
        self.simpleIdentifier=simpleIdentifier
    def accept(self,visitor):
        visitor.visitSimpleValueArgument(self)
        
class Compound1ValueArgument(CompoundVas):
    def __init__(self, simpleIdentifier, IGUALDADE, expression):
        self.simpleIdentifier=simpleIdentifier
        self.IGUALDADE=IGUALDADE
        self.expression=expression
    def accept(self,visitor):
        visitor.visitCompound1ValueArgument(self)
        
class Compound2ValueArgument(CompoundVas):
    def __init__(self, simpleIdentifier, IGUALDADE, MULT, expression):
        self.simpleIdentifier=simpleIdentifier
        self.IGUALDADE=IGUALDADE
        self.MULT=MULT
        self.expression=expression
    def accept(self,visitor):
        visitor.visitCompound2ValueArgument(self)
########################################################################

class CallLITERAL_STRING():
    def __init__(self, LITERAL_STRING):
        self.LITERAL_STRING=LITERAL_STRING
    def accept(self, visitor):
        Visitor.visitCallLITERAL_STRING(self)

class CallCallableReference():
    def __init__(self, callableReference):
        self.callableReference=callableReference
    def accept(self, visitor):
        Visitor.visitCallCallableReference(self)

class CallFunctionLiteral():
    def __init__(self, functionLiteral):
        self.functionLiteral=functionLiteral
    def accept(self, visitor):
        Visitor.visitCalFunctionLiteral(self)

class CallCollectionLiteral():
    def __init__(self, collectionLiteral):
        self.collectionLiteral=collectionLiteral
    def accept(self, visitor):
        Visitor.CallCollectionLiteral(self)

class CallIfExpression():
    def __init__(self, ifExpression):
        self.ifExpression=ifExpression
    def accept(self, visitor):
        Visitor.visitCallIfExpression(self)
        
class CallJumpExpression():
    def __init__(self, jumpExpression):
        self.jumpExpression=jumpExpression
    def accept(self, visitor):
        Visitor.visitCallJumpExpression(self)
########################################################################
        
class ParenthesizedExpression(kotlinFile):
    def __init__(self,LPAREN ,expression, RPAREN):
        self.LPAREN=LPAREN
        self.expression=expression
        self.RPAREN=RPAREN
    def accept(self,visitor):
        visitor.visitparenthesizedExpression(self)
########################################################################

class SimpleCollectionLiteral(kotlinFile):
    def __init__(self,LCCT, RCCT):
        self.LCCT=LCCT
        self.RCCT=RCCT
    def accept (self, visitor):
        visitor.visitSimpleCollectionLiteral(self)

class CompoundCollectionLiteral(kotlinFile):
    def __init__(self,LCCT, cl, RCCT):
        self.LCCT=LCCT
        self.cl=cl
        self.RCCT=RCCT
    def accept (self, visitor):
        visitor.visitCompoundCollectionLiteral(self)
########################################################################

class SimpleCl(SimpleCollectionLiteral):
    def __init__(self,expression):
        self.expression=expression
    def accept(self,visitor):
        visitor.visitSimpleCl(self)

class CompoundCl(CompoundCollectionLiteral):
    def __init__(self,expression, COMMA, cl):
        self.expression=expression
        self.COMMA=COMMA
        self.cl=cl
    def accept(self,visitor):
        visitor.visitCompoundCl(self)
########################################################################

class SimpleParametersWithOptionalType(kotlinFile):
    def __init__(self, LPAREN, RPAREN):
        self.LPAREN = LPAREN
        self.RPAREN = RPAREN
    def accept(self, visitor):
        Visitor.visitSimpleParametersWithOptionalType(self)

class CompoundParametersWithOptionalType(kotlinFile):
    def __init__(self, LPAREN, pwot, RPAREN):
        self.LPAREN = LPAREN
        self.pwot = pwot
        self.RPAREN = RPAREN
    def accept(self, visitor):
        Visitor.visitCompoundParametersWithOptionalType(self)
########################################################################

class SimplePwot(CompoundParametersWithOptionalType):
    def __init__(self, parameterWithOptionalType):
        self.parameterWithOptionalType = parameterWithOptionalType
    def accept(self, visitor):
        Visitor.visitSimplePwot(self)

class CompoundPwot(CompoundParametersWithOptionalType):
    def __init__(self, parameterWithOptionalType, COMMA, pwot):
        self.parameterWithOptionalType = parameterWithOptionalType
        self.COMMA = COMMA
        self.pwot = pwot
    def accept(self, visitor):
        Visitor.visitCompoundPwot(self)
########################################################################

#class 


class StringLiteral(kotlinFile):
    def __init__(self,lineStringLiteral,multiLineStringLiteral):
        self.lineStringLiteral=lineStringLiteral
        self.multiLineStringLiteral=multiLineStringLiteral
    def accept (self, visitor):
        visitor.visitstringLiteral(self)

class LambdaLiteral(kotlinFile):
    def _init__(self,RCHAVE, ll ,LCHAVE):
        self.RCHAVE=RCHAVE
        self.ll=ll
        self.LCHAVE=LCHAVE
    def accept (self,visitor):
        visitor.visitlambdaLiteral(self)

class SimpleLl(LambdaLiteral):
    def __init__(self, statements):
        self.statements=statements
    def accept(self,visitor):
        visitor.visitSimpleLl(self)

class Compound1Ll(LambdaLiteral):
    def __init__(self, SETA, statements):
        self.SETA=SETA
        self.statements=statements
    def accept(self,visitor):
        visitor.visitCompound1Ll(self)

class Compound2Ll(LambdaLiteral):
    def __init__(self,lambdaParameters, SETA, statements):
        self.lambdaParameters=lambdaParameters
        self.SETA=SETA
        self.statements=statements
    def accept(self,visitor):
        visitor.visitCompound2Ll(self)

class SimpleLambdaParameters(kotlinFile):
    def __init__(self,lambdaParameter, COMMA, lambdaParameters):
        self.lambdaParameter=lambdaParameter
    def accept(self,  visitor):
        visitor.visitSimpleLambdaParameters(self)

class CompoundLambdaParameters(kotlinFile):
    def __init__(self,lambdaParameter, COMMA, lambdaParameters):
        self.lambdaParameter=lambdaParameter
        self.COMMA=COMMA
        self.lambdaParameters=lambdaParameters
    def accept(self,  visitor):
        visitor.visitCompoundLambdaParameters(self)

class lambdaParameter(SimpleLambdaParameters,CompoundLambdaParameters):
    def __init__(self,variableDeclaration,multiVariableDeclaration, DOISP ,type):
        self.variableDeclaration=variableDeclaration
        self.multiVariableDeclaration=multiVariableDeclaration
        self.DOISP= DOISP
        self.type=type
    def accept(self,visitor):
        visitor.visitlambdaParameter(self)

class anonymousFunction(kotlinFile):
    def __init__(self,FUN ,af4 ,parametersWithOptionalType, af3 ,af2, af1):
        self.FUN=FUN
        self.af4=af4
        self.parametersWithOptionalType=parametersWithOptionalType
        self.af3=af3
        self.af2=af2
        self.af1=af1
    def accept(self, visitor):
        visitor.visitanonymousFunction(self)

class af1(anonymousFunction):
     def __init__(self,functionBody,null):
         self.functionBody=functionBody
         self.null=null
     def accept(self, visitor):
         visitor.visitaf1(self)

class af2(anonymousFunction):
     def __init__(self,typeConstraints,null):
         self.typeConstraints=typeConstraints
         self.null=null
     def accept(self, visitor):
         visitor.visitaf2(self)

class af3(anonymousFunction):
     def __init__(self,DOISP, type,null):
         self.DOISP=DOISP
         self.null=null
         self.type=type
     def accept(self, visitor):
         visitor.visitaf3(self)

class af4(anonymousFunction):
     def __init__(self,type, PONTO):
         self.PONTO=PONTO
         self.type=type
     def accept(self, visitor):
         visitor.visitaf4(self)

class FunctionLiteral(LambdaLiteral,anonymousFunction):
    def __init__(self,lambdaLiteral,anonymousFunction):
        self.lambdaLiteral=lambdaLiteral
        self.anonymousFunction=anonymousFunction
    def accept(self,visitor):
        visitor.visitfunctionLiteral(self)

class IfExpression(kotlinFile):
    def __init__(self,IF, LPAREN, expression, RPAREN, controlStructureBody, PV, ESLE):
        self.IF=IF
        self.LPAREN=LPAREN
        self.expression=expression
        self.RPAREN=RPAREN
        self.controlStructureBody=controlStructureBody
        self.PV=PV
        self.ESLE=ESLE
    def accept(self, visitor):
        visitor.visitifExpression(self)

class JumpExpression(kotlinFile):
    def __init__(self,THROW,RETURN, expression, RETURN_AT, CONTINUE,CONTINUE_AT,BREAK,BREAK_AT):
        self.RETURN=RETURN
        self.expression=expression
        self.RETURN_AT=RETURN_AT
        self.CONTINUE=CONTINUE
        self.CONTINUE_AT=CONTINUE_AT
        self.BREAK=BREAK
        self.BREAK_AT=BREAK_AT
    def accept(self,visitor):
        visitor.visitjumpExpression(self)

class SimpleCallableReference_SI(kotlinFile):
    def __init__(self, DOISP, simpleIdentifier ):
        self.DOISP=DOISP
        self.simpleIdentifier=simpleIdentifier
    def accept (self,visitor):
        visitor.visitSimpleCallableReference_SI(self)

class CompoundCallableReference_SI(kotlinFile):
    def __init__(self,receiverType, DOISP, simpleIdentifier ):
        self.receiverType=receiverType
        self.DOISP=DOISP
        self.simpleIdentifier=simpleIdentifier
    def accept (self,visitor):
        visitor.visitCompoundCallableReference_SI(self)

class SimpleCallableReference_Class(kotlinFile):
    def __init__(self, DOISP, CLASS ):
        self.DOISP=DOISP
        self.CLASS = CLASS
        self.simpleIdentifier=simpleIdentifier
    def accept (self,visitor):
        visitor.visitSimpleCallableReference_Class(self)

class CompoundCallableReference_Class(kotlinFile):
    def __init__(self,receiverType, DOISP, CLASS):
        self.receiverType=receiverType
        self.DOISP=DOISP
        self.CLASS=CLASS
    def accept (self,visitor):
        visitor.visitCompoundCallableReference_Class(self)

class AssignmentAndOperator(kotlinFile):
    def __init__(self,MAISIGUAL, MENOSIGUAL, MULTIGUAL, DIVIGUAL,MODIGUAL):
        self.MAISIGUAL=MAISIGUAL
        self.MENOSIGUAL=MENOSIGUAL
        self.MULTIGUAL=MULTIGUAL
        self.DIVIGUAL=DIVIGUAL
        self.MODIGUAL=MODIGUAL
    def accept(self,visitor):
        visitor.visitassignmentAndOperator(self)

class EqualityOperator(kotlinFile):
    def __init__(self,DIFERENTE,IDENTIDADE,IGUALDADE, SEMIDENTIDADE):
        self.DIFERENTE=DIFERENTE
        self.IDENTIDADE=IDENTIDADE
        self.IGUALDADE=IGUALDADE
        self.SEMIDENTIDADE=SEMIDENTIDADE
    def accept(self, visitor):
        visitor.visitequalityOperator(self)

class ComparisonOperator(kotlinFile):
    def __init__(self,MENOR, MAIOR, MENORIGUAL,MAIORIGUAL):
        self.MENOR=MENOR
        self.MAIOR=MAIOR
        self.MENORIGUAL=MENORIGUAL
        self.MAIORIGUAL=MAIORIGUAL
    def accept(self, visitor):
        visitor.visitcomparisonOperator(self)

class InOperator(kotlinFile):
    def __init__(self,IN, NOT_IN):
        self.IN=IN
        self.NOT_IN=NOT_IN
    def accept(self,visitor):
        visitor.visitinOperator(self)

class isOperator(kotlinFile):
    def __init__(self,IS, NOT_IS): 
        self.IS=IS
        self.NOT_IS=NOT_IS
    def accept(self, visitor):
        visitor.visitisOperator(self)

class additiveOperator(kotlinFile):
    def __init__(self,PLUS,MINUS):
        self.PLUS=PLUS
        self.MINUS=MINUS
    def accept (self, visitor):
        visitor.visitadditiveOperator(self)

class multiplicativeOperator(kotlinFile):
    def __init__(self,MULT,DIVIDE,MOD):
        self.MULT=MULT
        self.DIVIDE=DIVIDE
        self.MOD=MOD
    def accept(self,visitor):
        visitor.visitmultiplicativeOperator(self)

class SimpleAsOperator(kotlinFile):
    def __init__(self,AS):
        self.AS=AS
    def accept(self, visitor):
        visitor.visitSimpleAsOperator(self)

class CompoundAsOperator(kotlinFile):
    def __init__(self,AS, asOperator):
        self.AS=AS
        self.asOperator=asOperator
    def accept(self, visitor):
        visitor.visitCompoundAsOperator(self)

class prefixUnaryOperator(kotlinFile):
    def __init__(self,INCREMENTO,DECREMENTO, MINUS,PLUS,NOT):
        self.INCREMENTO=INCREMENTO
        self.DECREMENTO=DECREMENTO
        self.MINUS=MINUS
        self.PLUS=PLUS
        self.NOT=NOT
    def accept(self, visitor):
        visitor.visitprefixUnaryOperator(self)

class PostfixUnaryOperator(kotlinFile):
    def __init__(self,INCREMENTO,DECREMENTO, MINUS,PLUS,NOT):
        self.INCREMENTO=INCREMENTO
        self.DECREMENTO=DECREMENTO
    def accept(self, visitor):
        visitor.visitPostfixUnaryOperator(self)

class memberAccessOperator(kotlinFile):
    def __init__(self,PONTO,safeNav, COLONCOLON ):
        self.PONTO=PONTO
        self.safeNav=safeNav
        self.COLONCOLON=COLONCOLON
    def accept(self, visitor):
        visitor.visitmemberAccessOperator(self)

class safeNav(memberAccessOperator):
    def __init__(self,PONTO ):
        self.PONTO=PONTO 
    def accept(self,visitor):
        visitor.visitsafeNav(self)

