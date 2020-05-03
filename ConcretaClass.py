from Visitor import Visitor
from AbstrataClass import *
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
    def accept(self, Visitor):
        Visitor.visitAssignExp(self)

class NumExp():
    def __init__(self,num):
        self.num = num
    def accept(self,Visitor):
        Visitor.visitorNumExp(self)
        
class IDExp():
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
    def __init__(self, ID, Exp):
        self.ID = ID
        self.Exp = Exp
    def accept(self , Visitor):
        Visitor.visitAssighExp(self)
###########################################################
class KotlinFile():
    def __init__(self):
        self
    def accept(self,visitor):
        Visitor.visitKotlinFile(self)

class SimpleKotlinFile():
    def __init__(self, functionDeclaration):
        self.functionDeclaration = functionDeclaration
    def accept(self, visitor):
        Visitor.visitSimpleKotlinFile(self)

class CompoundKotlinFile():
    def __init__(self, functionDeclaration, kotlinFile):
        self.functionDeclaration = functionDeclaration
        self.kotlinFile = kotlinFile
    def accept(self, visitor):
        Visitor.visitCompoundKotlinFile(self)
###########################################################

class FunctionDeclaration(KotlinFile):
    def __init__(self, fd1, simpleIdentifier, functionValueParameters, fd2, fd3):
        self.fd1 = fd1
        self.simpleIdentifier
        self.functionValueParameters
        self.fd2 = fd2
        self.fd3 = fd3
    def accept(self, visitor):
        Visitor.visitFuncrionDeclaration(self)

class Fd1(FunctionDeclaration):
    def __init__(self, simpleIdentifier):
        self.simpleIdentifier = simpleIdentifier
    def accept(self, visitor):
        Visitor.visitFd1(self)

class Fd2(FunctionDeclaration):
    def __init__(self, type):
        self.type = type
    def accept(self, visitor):
        Visitor.visitFd2(self)

class Fd3(FunctionDeclaration):
    def __init__(self, block):
        self.block = block
    def accept(self, visitor):
        Visitor.visitFd3(self)
###########################################################

class SimpleFunctionBody(FunctionDeclaration):
    def __init__(self, block):
        self.block = block
    def accept(self, visitor):
        Visitor.visitSimpleFunctionBody(self)

class CompoundFunctionBody(KotlinFile):
    def __init__(self, expression):
        self.expression = expression
    def accept(self, visitor):
        Visitor.visitCompoundFunctionBody(self)
###########################################################

class SimpleFunctionValueParameters(KotlinFile):
    def __init__(self):
       self
    def accept(self, visitor):
        Visitor.visitSimpleFunctionValueParameters(self)

class CompoundFunctionValueParameters(KotlinFile):
    def __init__(self, fvps):
       self.fvps=fvps
    def accept(self, visitor):
        Visitor.visitCompoundFunctionValueParameters(self)
################################################################

class SimpleFvps(SimpleFunctionValueParameters):
    def __init__(self, fvps):
        self.fvps=fvps
    def accept(self, visitor):
        Visitor.visitSimpleFvps(self)

class COMMAFvps(CompoundFunctionValueParameters):
    def __init__(self, fvp, fvps):
        self.fvp=fvp
        self.fvps=fvps
    def accept(self, visitor):
        Visitor.visitCompoundFvps(self)

class CompoundFvps(CompoundFunctionValueParameters):
    def __init__(self, fvp, fvps):
        self.fvp=fvp
        self.fvps=fvps
    def accept(self, visitor):
        Visitor.visitCompoundFvps(self)
###################################################################

class SimpleFunctionValueParameter(SimpleFunctionValueParameters):
    def __init__(self, parameter):
        self.Parameter=parameter
    def accept(self,visitor):
        Visitor.visitSimpleFunctionValueParameter(self)
        
class CompoundFunctionValeuParameter(CompoundFunctionValueParameters):
    def __init__(self, parameter, exp):
        self.parameter=parameter
        self.exp=exp
    def accept(self,visitor):
        Visitor.visitCompoundFunctionValueParameter(self)
#####################################################################

class SimpleVariableDeclaration(KotlinFile):
    def __init__(self, simpleIdentifier):
        self.simpleIdentifier = simpleIdentifier
    def accept(self, visitor):
        Visitor.visitSimpleVariableDeclaration(self)

class CompoundVariableDeclaration(KotlinFile):
    def __init__(self, simpleIdentifier, type):
        self.simpleIdentifier = simpleIdentifier
        self.type=type
    def accept(self, visitor):
        Visitor.visitvariableDeclaration(self)
#################################################################

class SimpleMultiVariableDeclaration(KotlinFile):
    def __init__(self):
        self
    def accept(self, visitor):
        Visitor.visitSimpleMultiVariableDeclaration(self)

class CompoundMultiVariableDeclaration(KotlinFile):
    def __init__(self, mvd):
        self.mvd=mvd
    def accept(self, visitor):
        Visitor.visitCompoundMultiVariableDeclaration(self)
###################################################################

class SimpleMvd(SimpleMultiVariableDeclaration):
    def __init__(self, variableDeclaration):
        self.variableDeclaration=variableDeclaration
    def accept(self, visitor):
        Visitor.visitSimpleMvd(self)

class CompoundMvd(CompoundMultiVariableDeclaration):
    def __init__(self, variableDeclaration, mvd ):
        self.mvd=mvd
        self.variableDeclaration=variableDeclaration
    def accept(self, visitor):
        Visitor.visitCompoundMvd(self)
####################################################################

class Parameter(SimpleFunctionValueParameter):
    def __init__(self,simpleIdentifier, type ):
        self.simpleIdentifier= simpleIdentifier
        self.type=type
    def accept(self, visitor):
        Visitor.visitParameter(self)
######################################################################
class  CompoundType(KotlinFile):
    def __init__(self,typeModifiers, optype ):
        self.typeModifiers=typeModifiers  
        self.optype=optype
    def accept(self, visitor):
        Visitor.visitCompoundType(self)

class SimpleType(KotlinFile):
    def __init__(self,optype):
        self.optype=optype
    def accept (self, visitor):
        Visitor.visitSimpleType(self)
#######################################################################

class OpType(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
        pass

class ParenthesizedType(OpType):
    def __init__(self, parenthesizedType):
        self.parenthesizedType = parenthesizedType
    def accept(self, visitor):
        Visitor.visitParenthesizedType(self)

class FunctionType(OpType):
    def __init__(self, functionType):
        self.functionType = functionType
    def accept(self, visitor):
        Visitor.visitFunctionType(self)

class UserType(OpType):
    def __init__(self, userType):
        self.userType = userType
    def accept(self, visitor):
        Visitor.visitUserType(self)
#######################################################################

class SimpleTypeModifiers(KotlinFile):
    def __init__ (self, typeModifier):
        self.typeModifier = typeModifier
    def accept(self, visitor):
        Visitor.visitSimpleTypeModifiers(self)

class CompondTypeModifiers(KotlinFile):
    def __init__ (self, typeModifier, typeModifiers):
        self.typeModifier = typeModifier
        self.typeModifiers = typeModifiers
    def accept(self, visitor):
        Visitor.visitCompoundTypeModifiers(self)
#########################################################################
class Type():
    def __init__(self, typerModifier,opType):
        self.typerModifier=typerModifier
        self.opType=opType
    def accept(self, visitor):
        visitor.visitType(self)

class TypeModifier(Type):
    def __init__ (self, suspend):
        self.suspend = suspend
    def accept(self, visitor):
        Visitor.visitTypeModifier(self)
#########################################################################

class TypeProjectionModifier(SimpleTypeModifiers,CompondTypeModifiers):
    def __init__(self, varianceModifier):
        self.varianceModifier = varianceModifier
    def accept(self, visitor):
        Visitor.visitTypeProjectionModifier(self)
##########################################################################

class VarianceModifier(TypeProjectionModifier):
    def __init__(self, IN, OUT):
        self.IN = IN
        self.OUT = OUT

class CallIn():
    def __init__(self):
        self
    def accept(self, visitor):
        Visitor.visitCallIn(self)
class CallOut():
    def __init__(self):
        self
    def accept(self, visitor):
        Visitor.visitCallOut(self)
########################################################################

class userType(KotlinFile):
    def __init__(self,simpleUserType):
        self.simpleUserType=simpleUserType
    def accept(self, visitor):
        Visitor.visituserType(self)
##########################################################################

class SimpleSimpleUserType(userType):
    def __init__(self, simpleUserType):
        self.simpleUserType=simpleUserType
    def accept(self, visitor):
        Visitor.visitSimpleSimpleUserType(self)

class CompoundSimpleUserType(userType):
    def __init__(self, simpleUserType, typeArguments):
        self.simpleUserType=simpleUserType
        self.typeArguments=typeArguments
    def accept(self, visitor):
        Visitor.visitCompoundSimpleUserType(self)
##########################################################################

class SimpleTypeProjection(KotlinFile):
    def __init__(self, type):
        self.type=type
    def accept(self,visitor):
        Visitor.visittypeSimpleProjection(self)

class CompoundTypeProjection(KotlinFile):
    def __init__(self, typeProjectionModifiers, type):
        self.typeProjectionModifiers= typeProjectionModifiers
        self.type=type
    def accept(self,visitor):
        Visitor.visitCompoundTypeProjection(self)
########################################################################

class SimpleTypeProjectionModifiers(SimpleTypeProjection):
    def __init__(self, typeProjection):
        self.typeProjection=typeProjection
    def accept(self, visitor):
        Visitor.visitSimpleTypeProjectionModifiers(self)

class CompoundTypeProjectionModifiers(CompoundTypeProjection):
    def __init__(self, typeProjectionModifier, typeProjectionModifiers):
        self.typeProjectionModifier =typeProjectionModifier
        self.typeProjectionModifiers=typeProjectionModifiers
    def accept(self, visitor):
        Visitor.visitCompoundTypeProjectionModifiers(self)
########################################################################

class SimpleFunctionType(KotlinFile):
    def __init__(self, functionTypeParameters, type):
        self.functionTypeParameters=functionTypeParameters
        self.type=type
    def accept(self, visitor):
        Visitor.visitSimpleFunctionType(self)

class CompoundFunctionType(KotlinFile):
    def __init__(self, receiverType, functionTypeParameters, type):
        self.receiverType= receiverType
        self.functionTypeParameters=functionTypeParameters
        self.type=type
    def accept(self, visitor):
        Visitor.visitCompoundFunctionType(self)
########################################################################

class SimpleFunctionTypeParameters_p(KotlinFile):
    def __init__(self, parameter):
        self.parameter = parameter
    def accept(self, visitor):
        Visitor.visitSimpleFunctionTypeParameters_p()

class CompoundFunctionTypeParameters_p(KotlinFile):
    def __init__(self, parameter, ftp):
        self.parameter = parameter
        self.ftp = ftp
    def accept(self, visitor):
        Visitor.visitCompoundFunctionTypeParameters_p()
########################################################################

class SimpleFunctionTypeParameters_t(KotlinFile):
    def __init__(self, type):
        self.type = type
    def accept(self, visitor):
        Visitor.visitSimpleFunctionTypeParameters_t()

class CompoundFunctionTypeParameters_t(KotlinFile):
    def __init__(self, type, ftp):
        self.type = type
        self.ftp = ftp
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

class ParenthesizedType(KotlinFile):
    def __init__(self, type):
        self.type=type
    def accept(self, visitor):
        Visitor.visitparenthesizedType(self)
########################################################################
        
class ReceiverType(FunctionType):
    def __init__(self, typeModifier, rt):
        self.typeModifier=typeModifier
        self.rt=rt
    def accept(self, visitor):
        Visitor.visitReceiverType(self)
########################################################################
       
class Rt(ReceiverType):
    def __init__(self, parenthesizedType):
        self. parenthesizedType= parenthesizedType
    def accept(self, visitor):
        Visitor.visitrt(self)
########################################################################

class SimpleStatements (KotlinFile):
    def __init__(self, statement):
        self.statement=statement
    def accept(self, visitor):
        Visitor.visitSimpleStatemnts(self)

class CompoundStatements (KotlinFile):
    def __init__(self, statement, statments):
        self.statement=statement
        self.statments=statments
    def accept(self, visitor):
        Visitor.visitCompoundStatemnts(self)
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
    def __init__(self, statements):
        self.statements=statements
    def accept(self, visitor):
        Visitor.visitblock(self)
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

class WhileStatement_PV():
    def __init__(self, expression):
        self.expression = expression
    def accept(self, visitor):
        Visitor.visitWhileStatement_PV(self)


class WhileStatement_CBS():
    def __init__(self, expression, controlStructureBody):
        self.expression = expression
        self.controlStructureBody = controlStructureBody
    def accept(self, visitor):
        Visitor.visitWhileStatement_CBS(self)

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
    def __init__(self, multiVariableDeclaration, expression):
        self.multiVariableDeclaration=multiVariableDeclaration
        self.expression=expression
    def accept(self, visitor):
        Visitor.visitSimpleForStatement_MD(self)

class CompoundForStatement_MD(CallForStatement_MD, CallForStatement_VD, CallWhileStatement, CallDoWhileStatement):

    def __init__(self, multiVariableDeclaration, expression, controlStructureBody):
        self.multiVariableDeclaration=multiVariableDeclaration
        self.expression=expression
        self.controlStructureBody=controlStructureBody
    def accept(self, visitor):
        Visitor.visitCompoundForStatement_MD(self)

class SimpleForStatement_VD(CallForStatement_MD, CallForStatement_VD, CallWhileStatement, CallDoWhileStatement):
    def __init__(self, variableDeclaration, expression):
        self.variableDeclaration=variableDeclaration
        self.expression=expression
    def accept(self, visitor):
        Visitor.visitSimpleForStatement_MD(self)

class CompoundForStatement_VD(CallForStatement_MD, CallForStatement_VD, CallWhileStatement, CallDoWhileStatement):
    def __init__(self, multiVariableDeclaration, expression, controlStructureBody):
        self.variableDeclaration=variableDeclaration
        self.expression=expression
        self.controlStructureBody=controlStructureBody
    def accept(self, visitor):
        Visitor.visitCompoundForStatement_MD(self)
########################################################################

class CallPv():
    def __init__(self, expression):
        self.expression=expression
    def accept(self, visitor):
        Visitor.visitCallPv(self)

class CallCSB():
    def __init__(self, expression, csb):
        self.expression=expression
        self.csb = csb
    def accept(self, visitor):
        Visitor.visitCallCSB(self)
########################################################################
        
class SimpleDoWhileStatement(CallForStatement_MD, CallForStatement_VD, CallWhileStatement, CallDoWhileStatement):
    def __init__(self, expression): 
        self.expression=expression
    def accept(self, visitor):
        Visitor.visitSimpleDoWhileStatement(self)

class CompoundDoWhileStatement(CallForStatement_MD, CallForStatement_VD, CallWhileStatement, CallDoWhileStatement):
    def __init__(self, controlStructureBody, expression):
        self.controlStructureBody=controlStructureBody
        self.expression=expression
    def accept(self, visitor):
        Visitor.visitCompoundDoWhileStatement(self)
########################################################################
        
class CallAtribuicao():
    def __init__(self,directlyAssignableExpression, expression):
        self.directlyAssignableExpression=directlyAssignableExpression
        self.expression=expression
    def accept(self, visitor):
        Visitor.visitCallAtribuicao(self)

class CallAssignmentAndOperator():
    def __init__(self,assignmentAndOperator, assignableExpression ,expression): 
        self.assignmentAndOperator=assignmentAndOperator
        self.expression=expression
        self.assignableExpression = assignableExpression
    def accept(self, visitor):
        Visitor.visitCallAssignableExpression(self)
########################################################################
        
class Expression(KotlinFile):
    def __init__(self, disjunction):
        self.disjunction = disjunction
    def accept (self,visitor):
        Visitor.visitExpression(self)
########################################################################
        
class SimpleDisjunction(Expression):
    def __init__(self, conjunction):
        self.conjunction = conjunction
    def accept (self,visitor):
        Visitor.visitSimpleDisjunction(self)
       
class CompoundDisjunction(Expression):
    def __init__(self, conjunction, disjunction):
        self.conjunction=conjunction
        self.disjunction=disjunction
    def accept (self,visitor):
        Visitor.visitCompoundDisjunction(self)
########################################################################
        
class SimpleConjunction(SimpleDisjunction):
    def __init__(self,equality):
        self.equality=equality
    def accept (self,visitor):
        Visitor.vistSimpleConjunction(self)

class CompoundConjunction(CompoundDisjunction):
    def __init__(self, equality, conjunction):
        self.equality = equality
        self.conjunction = conjunction
    def accept(self, visitor):
        Visitor.vistCompoundConjunction(self)
########################################################################
        
class SimpleEquality(SimpleConjunction):
    def __init__(self,comparison):
        self.comparison=comparison
    def accept(self,visitor):
        Visitor.visitSimpleEquality(self)

class CompoundEquality(CompoundConjunction):
    def __init__(self,comparison, equalityOperator, equality):
        self.comparison=comparison
        self.equalityOperator=equalityOperator
        self.equality=equality
    def accept(self,visitor):
        Visitor.visitCompoundEquality(self)
########################################################################
        
class SimpleComparison(SimpleEquality):
    def __init__(self, infixOperation):
        self.infixOperation=infixOperation
    def accept (self,visitor):
        Visitor.vistSimpleComparison(self)
    
class CompoundComparison(CompoundEquality):
    def __init__(self, infixOperation, comparisonOperator):
        self.infixOperation=infixOperation
        self.comparisonOperator=comparisonOperator
    def accept (self,visitor):
        Visitor.vistCompoundComparison(self)
########################################################################
        
class SimpleInfixOperation(SimpleComparison,CompoundComparison):
    def __init__(self,elvisExpression):
        self.elvisExpression=elvisExpression
    def accept (self,visitor):
        Visitor.visitSimpleInfixOperation(self)
        
class CompoundInfixOperation(SimpleComparison,CompoundComparison):
    def __init__(self,elvisExpression, io):
        self.elvisExpression=elvisExpression
        self.io=io
    def accept (self,visitor):
         Visitor.visitCompoundInfixOperation(self)
########################################################################
class io(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass    
class InOperator(io):
    def __init__(self, inOperator):
        self.isOperator = IsOperator        
        self.elvisExpression=elvisExpression    
    def accept(self, visitor):
        Visitor.visitInOperator(self)

class IsOperator(io):
    def __init__(self, isOperator):
        self.isOperator = IsOperator        
        self.type=type    
    def accept(self, visitor):
        Visitor.visitIsOperator(self)

########################################################################
    
class SimpleElvisExpression(io):
    def __init__(self,infixFunctionCall):
        self.infixFunctionCall=infixFunctionCall
    def accept(self,visitor):
        Visitor.visitSimpleElvisExpression(self)

class CompoundElvisExpression(io):
    def __init__(self, infixFunctionCall, elvisExpression):
        self.infixFunctionCall=infixFunctionCall
        self.elvisExpression=elvisExpression
    def accept(self, visitor):
        Visitor.visitCompoundElvisExpression(self)
########################################################################
    
class SimpleInfixFunctionCall(SimpleElvisExpression):
    def __init__(self,rangeExpression):
        self.rangeExpression=rangeExpression
    def accept (self,visitor):
        Visitor.visitSimpleInfixFunctionCall(self)
        
class CompoundInfixFunctionCall(CompoundElvisExpression):
    def __init__(self,rangeExpression, simpleIdentifier, infixFunctionCall):
        self.rangeExpression=rangeExpression
        self.simpleIdentifier=simpleIdentifier
        self.infixFunctionCall=infixFunctionCall
    def accept (self,visitor):
        Visitor.visitCompoundInfixFunctionCall(self)
########################################################################
        
class SimpleRangeExpression(SimpleInfixFunctionCall):
    def __init__(self,additiveExpression):
        self.additiveExpression=additiveExpression
    def accept(self, visitor):
        Visitor.visitSimpleRangeExpression(self)
    
class CompoundRangeExpression(CompoundInfixFunctionCall):
    def __init__(self,additiveExpression, rangeExpression):
        self.additiveExpression=additiveExpression
        self.rangeExpression=rangeExpression
    def accept(self, visitor):
        Visitor.visitCompoundRangeExpression(self)
########################################################################
        
class SimpleAdditiveExpression(SimpleRangeExpression):
    def __init__(self,multiplicativeExpression):
        self.multiplicativeExpression=multiplicativeExpression
    def accept (self,visitor):
        Visitor.visitSimpleAdditiveExpression(self)
    
class CompoundAdditiveExpression(CompoundRangeExpression):
    def __init__(self,multiplicativeExpression ,additiveOperator, additiveExpression):
        self.multiplicativeExpression=multiplicativeExpression
        self.additiveOperator=additiveOperator
        self.additiveExpression=additiveExpression
    def accept (self,visitor):
        Visitor.visitCompoundAdditiveExpression(self)
########################################################################
        
class SimpleMultiplicativeExpression(SimpleAdditiveExpression):
    def __init__(self,asExpression):
        self.asExpression=asExpression
    def accept(self, visitor):
        Visitor.visitSimpleMultiplicativeExpression(self)
        
class CompoundMultiplicativeExpression(CompoundAdditiveExpression):
    def __init__(self,asExpression ,multiplicativeOperator, multiplicativeExpression):
        self.asExpression=asExpression
        self.multiplicativeOperator=multiplicativeOperator
        self.multiplicativeExpression=multiplicativeExpression
    def accept(self, visitor):
        Visitor.visitCompoundMultiplicativeExpression(self)
########################################################################
        
class SimpleAsExpression(SimpleMultiplicativeExpression):
    def __init__(self,prefixUnaryExpression, asOperator, type):
        self.prefixUnaryExpression=prefixUnaryExpression
    def accept (self, visitor):
        Visitor.visitSimpleAsExpression(self)
        
class CompoundAsExpression(CompoundMultiplicativeExpression):
    def __init__(self,prefixUnaryExpression, asOperator, type):
        self.prefixUnaryExpression=prefixUnaryExpression
        self.asOperator=asOperator
        self.type=type
    def accept (self, visitor):
        Visitor.visitCompoundAsExpression(self)
########################################################################
        
class SimplePrefixUnaryExpression(SimpleAsExpression,CompoundAsExpression):
    def __init__(self, postfixUnaryExpression):
        self.postfixUnaryExpression=postfixUnaryExpression
    def accept(self,visitor):
        Visitor.visitSimplePrefixUnaryExpression(self)

class CompoundPrefixUnaryExpression(SimpleAsExpression,CompoundAsExpression):
    def __init__(self,preue, postfixUnaryExpression):
        self.preue=preue
        self.postfixUnaryExpression=postfixUnaryExpression
    def accept(self,visitor):
        Visitor.visitCompoundPrefixUnaryExpression(self)
########################################################################
        
class SimplePreue(SimplePrefixUnaryExpression):
    def __init__(self,unaryPrefix ,preue):
        self.unaryPrefix=unaryPrefix
    def accept(self, visitor):
        Visitor.visitSimplePreue(self)

class CompoundPreue(CompoundPrefixUnaryExpression):
    def __init__(self,unaryPrefix ,preue):
        self.unaryPrefix=unaryPrefix
        self.preue=preue
    def accept(self, visitor):
        Visitor.visitCompoundPreue(self)
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

class Lable(KotlinFile):
    def __init__(self, simpleIdentifier):
        self.simpleIdentifier = simpleIdentifier
    def accept(self, visitor):
        Visitor.visitLable(self)
########################################################################

class SimplePostfixUnaryExpression(KotlinFile):
    def __init__(self,primaryExpression ,posue):
        self.primaryExpression=primaryExpression
    def accept(self, visitor):
        Visitor.visitSimplePostfixUnaryExpression(self)
   
class CompoundPostfixUnaryExpression(KotlinFile):
    def __init__(self,primaryExpression ,posue):
        self.primaryExpression=primaryExpression
        self.posue=posue
    def accept(self, visitor):
        Visitor.visitCompoundPostfixUnaryExpression(self)
########################################################################

class SinglePosue(SimplePostfixUnaryExpression):
    def __init__(self,postfixUnarySuffix):
        self.postfixUnarySuffix=postfixUnarySuffix
    def accept(self,visitor):
        Visitor.visitSinglePosue(self)
        
class CompoundPosue(CompoundPostfixUnaryExpression):
    def __init__(self,postfixUnarySuffix, posue):
        self.postfixUnarySuffix=postfixUnarySuffix
        self.posue=posue
    def accept(self,visitor):
        Visitor.visitCompoundPosue(self)
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
        Visitor.visitSimpleDirectlyAssignableExpression(self)
########################################################################
        
class ParenthesizedDirectlyAssignableExpression(SimpleDirectlyAssignableExpression):
    def __init__(self, directlyAssignableExpression):
        self.directlyAssignableExpression=directlyAssignableExpression
    def accept(self,visitor):
        Visitor.visitParenthesizedDirectlyAssignableExpression(self)
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
class assignableExpression():
    def __init__(self, prefixUnaryExpression,parenthesizedAssignableExpression):
        self.prefixUnaryExpression=prefixUnaryExpression
        self.parenthesizedAssignableExpression=parenthesizedAssignableExpression
    def accept(self, visitor):
        visitor.visitassignableExpression(self)

class ParenthesizedAssignableExpression(assignableExpression):
    def __init__(self, assignableExpression):
        self.assignableExpression=assignableExpression
    def accept(self, visitor):
        Visitor.visitparenthesizedAssignableExpression(self)
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
 
class SimpleIndexingSuffix(KotlinFile):
    def __init__(self):
        self
    def accept(self,visitor):
        Visitor.visitSimpleIndexingSuffix(self)       

class CompoundIndexingSuffix(KotlinFile):
    def __init__(self,isuf):
        self.isuf=isuf
    def accept(self,visitor):
        Visitor.visitCompoundIndexingSuffix(self)
########################################################################

class SimpleIsuf(SimpleIndexingSuffix):
    def __init__(self,expression ):
        self.expression=expression
    def accept(self,visitor):
        Visitor.visitSimpleIsuf(self)
        
class CompoundIsuf(CompoundIndexingSuffix):
    def __init__(self,expression, isuf ):
        self.expression=expression
        self.isuf=isuf
    def accept(self,visitor):
        Visitor.visitCompoundIsuf(self)
########################################################################
        
class CallParenthesizedExpression():
    def __init__(self, memberAccessOperator, parenthesizedExpression):
        self.memberAccessOperator=memberAccessOperator
        self.parenthesizedExpression = parenthesizedExpression
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

class AnnotatedLambda(KotlinFile):
    def __init__(self,lambdaLiteral):
        self.lambdaLiteral=lambdaLiteral
    def accept(self,visitor):
        Visitor.visitannotatedLambda(self)
########################################################################
        
class SimpleTypeArguments(KotlinFile):
    def __init__(self):
        self
    def accept(self,visitor):
        Visitor.visitSimpleTypeArguments(self)

class CompoundTypeArguments(KotlinFile):
    def __init__(self, ta):
        self.ta=ta
    def accept(self,visitor):
        Visitor.visitCompoundTypeArguments(self)
########################################################################
        
class SimpleTa(SimpleTypeArguments):
    def __init_(self,typeProjection):
        self.typeProjection=typeProjection
    def accept (self, visitor):
        Visitor.visitSimpleTa(self)
        
class CompoundTa(CompoundTypeArguments):
    def __init_(self,typeProjection, ta):
        self.typeProjection=typeProjection
        self.ta=ta
    def accept (self, visitor):
        Visitor.visitCompoundTa(self)
########################################################################
        
class SimpleValueArguments(KotlinFile):
    def __init__(self):
        self
    def accept(self, visitor):
        Visitor.visitSimpleValueArguments(self)
        
class CompoundValueArguments(KotlinFile):
    def __init__(self, vas):
        self.vas=vas
    def accept(self, visitor):
        Visitor.visitCompoundValueArguments(self)
########################################################################
        
class SimpleVas(SimpleValueArguments):
    def __init__(self,valueArgument):
        self.valueArgument=valueArgument
    def accept(self,visitor):
        Visitor.visitSimpleVas(self)
        
class CompoundVas(CompoundValueArguments):
    def __init__(self,valueArgument , vas):
        self.valueArgument=valueArgument
        self.vas=vas
    def accept(self,visitor):
        Visitor.visitCompoundVas(self)
########################################################################
        
class SimpleValueArgument(SimpleVas):
    def __init__(self,simpleIdentifier):
        self.simpleIdentifier=simpleIdentifier
    def accept(self,visitor):
        Visitor.visitSimpleValueArgument(self)
        
class Compound1ValueArgument(CompoundVas):
    def __init__(self, simpleIdentifier, expression):
        self.simpleIdentifier=simpleIdentifier
        self.expression=expression
    def accept(self,visitor):
        Visitor.visitCompound1ValueArgument(self)
        
class Compound2ValueArgument(CompoundVas):
    def __init__(self, simpleIdentifier, expression):
        self.simpleIdentifier=simpleIdentifier
        self.expression=expression
    def accept(self,visitor):
        Visitor.visitCompound2ValueArgument(self)
########################################################################

class CallLITERAL_STRING():
    def __init__(self):
        self
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
        
class ParenthesizedExpression(KotlinFile):
    def __init__(self, expression):
        self.expression=expression
    def accept(self,visitor):
        Visitor.visitparenthesizedExpression(self)
########################################################################

class SimpleCollectionLiteral(KotlinFile):
    def __init__(self):
        self
    def accept (self, visitor):
        Visitor.visitSimpleCollectionLiteral(self)

class CompoundCollectionLiteral(KotlinFile):
    def __init__(self, cl):
        self.cl=cl
    def accept (self, visitor):
        Visitor.visitCompoundCollectionLiteral(self)
########################################################################

class SimpleCl(SimpleCollectionLiteral):
    def __init__(self,expression):
        self.expression=expression
    def accept(self,visitor):
        Visitor.visitSimpleCl(self)

class CompoundCl(CompoundCollectionLiteral):
    def __init__(self,expression, cl):
        self.expression=expression
        self.cl=cl
    def accept(self,visitor):
        Visitor.visitCompoundCl(self)
########################################################################

class SimpleParametersWithOptionalType(KotlinFile):
    def __init__(self):
        self
    def accept(self, visitor):
        Visitor.visitSimpleParametersWithOptionalType(self)

class CompoundParametersWithOptionalType(KotlinFile):
    def __init__(self, pwot):
        self.pwot = pwot
    def accept(self, visitor):
        Visitor.visitCompoundParametersWithOptionalType(self)
########################################################################

class SimplePwot(CompoundParametersWithOptionalType):
    def __init__(self, parameterWithOptionalType):
        self.parameterWithOptionalType = parameterWithOptionalType
    def accept(self, visitor):
        Visitor.visitSimplePwot(self)

class CompoundPwot(CompoundParametersWithOptionalType):
    def __init__(self, parameterWithOptionalType, pwot):
        self.parameterWithOptionalType = parameterWithOptionalType
        self.pwot = pwot
    def accept(self, visitor):
        Visitor.visitCompoundPwot(self)
########################################################################

class Compound1ParameterWithOptionalType():
    def __init__(self, simpleIdentifier, type):
        self.simpleIdentifier = CallSimpleIdentifier
        self.type = type
    def accept(self, visitor):
        Visitor.visitCompound1ParameterWithOptionalType(self)

class Compound2ParameterWithOptionalType():
    def __init__(self, parameterModifiers, simpleIdentifier, type):
        self.parameterModifiers = parameterModifiers
        self.simpleIdentifier = CallSimpleIdentifier
        self.type = type
    def accept(self, visitor):
        Visitor.visitCompound2ParameterWithOptionalType(self)
    
class Simple1ParameterWithOptionalType():
    def __init__(self, simpleIdentifier):
        self.simpleIdentifier = CallSimpleIdentifier
    def accept(self, visitor):
        Visitor.visitSimple1ParameterWithOptionalType(self)

class Simple2ParameterWithOptionalType():
    def __init__(self, parameterModifiers, simpleIdentifier):
        self.simpleIdentifier = CallSimpleIdentifier
    def accept(self, visitor):
        Visitor.visitSimple2ParameterWithOptionalType(self)
########################################################################

class CallVararg():
    def __init__(self):
        self
    def accept(self, visitor):
        Visitor.visitCallVararg(self)

class CallNoinline():
    def __init__(self):
        self
    def accept(self, visitor):
        Visitor.visitCallNoinline(self)

class CallCrossinline():
    def __init__(self):
        self
    def accept(self, visitor):
        Visitor.visitCallCrossinline(self)
########################################################################

class LambdaLiteral(KotlinFile):
    def _init__(self, ll):
        self.ll=ll
    def accept (self,visitor):
        Visitor.visitlambdaLiteral(self)
########################################################################

class SimpleLl(LambdaLiteral):
    def __init__(self, statements):
        self.statements=statements
    def accept(self,visitor):
        Visitor.visitSimpleLl(self)

class Compound1Ll(LambdaLiteral):
    def __init__(self, statements):
        self.statements=statements
    def accept(self,visitor):
        Visitor.visitCompound1Ll(self)

class Compound2Ll(LambdaLiteral):
    def __init__(self,lambdaParameters, statements):
        self.lambdaParameters=lambdaParameters
        self.statements=statements
    def accept(self,visitor):
        Visitor.visitCompound2Ll(self)
########################################################################

class SimpleLambdaParameters(KotlinFile):
    def __init__(self,lambdaParameter, lambdaParameters):
        self.lambdaParameter=lambdaParameter
    def accept(self,  visitor):
        Visitor.visitSimpleLambdaParameters(self)

class CompoundLambdaParameters(KotlinFile):
    def __init__(self,lambdaParameter, lambdaParameters):
        self.lambdaParameter=lambdaParameter
        self.lambdaParameters=lambdaParameters
    def accept(self,  visitor):
        Visitor.visitCompoundLambdaParameters(self)
########################################################################

class CallVariableDeclaration():
    def __init__(self, multiVariableDeclaration):
        self.multiVariableDeclaration = multiVariableDeclaration
    def accept(self, visitor):
        Visitor.visitCallVariableDeclaration(self)
    
class CallMultiVariableDeclaration():
    def __init__(self, multiVariableDeclaration):
        self.multiVariableDeclaration = multiVariableDeclaration
    def accept(self, visitor):
        Visitor.visitCallMultiVariableDeclaration(self)

class CompoundLambdaParameter(SimpleLambdaParameters,CompoundLambdaParameters):
    def __init__(self, variableDeclaration, multiVariableDeclaration, type):
        self.multiVariableDeclaration=multiVariableDeclaration
        self.variableDeclaration=variableDeclaration
        self.type=type
    def accept(self,visitor):
        Visitor.visitCompoundLambdaParameter(self)
############################Duvida############################################

class anonymousFunction(KotlinFile):
    def __init__(self ,af4 ,parametersWithOptionalType, af3 ,af2, af1):
        self.af4=af4
        self.parametersWithOptionalType=parametersWithOptionalType
        self.af3=af3
        self.af2=af2
        self.af1=af1
    def accept(self, visitor):
        Visitor.visitanonymousFunction(self)

class af1(anonymousFunction):
    def __init__(self,functionBody):
         self.functionBody=functionBody
    def accept(self, visitor):
        Visitor.visitaf1(self)

class af2(anonymousFunction):
    def __init__(self,typeConstraints):
         self.typeConstraints=typeConstraints
    def accept(self, visitor):
        Visitor.visitaf2(self)

class af3(anonymousFunction):
    def __init__(self,type):
        self.type=type
    def accept(self, visitor):
        Visitor.visitaf3(self)

class af4(anonymousFunction):
    def __init__(self,type):
        self.type=type
    def accept(self, visitor):
        Visitor.visitaf4(self)

########################################################################

class CallLambdaLiteral():
    def __init__(self, lambdaLiteral):
        self.lambdaLiteral = lambdaLiteral
    def accept(self, visitor):
        Visitor.visitCallLamdaLiteral(self)

class CallAnonymousFunction():
    def __init__(self, anonymousFunction):
        self.anonymousFunction = anonymousFunction
    def accept(self, visitor):
        Visitor.visitCallAnonymousFunction(self)
########################################################################

class TypeConstraint(LambdaLiteral,anonymousFunction):
    def __init__(self,simpleIdentifier, type):
        self.simpleIdentifier = simpleIdentifier
        self.type = type
    def accept(self,visitor):
        Visitor.visitTypeConstraint(self)
#################################Duvida#######################################
########################################################################

class IfExpression(KotlinFile):
    def __init__(self, expression, controlStructureBody ):
        self.expression=expression
        self.controlStructureBody=controlStructureBody
    def accept(self, visitor):
        Visitor.visitifExpression(self)
########################################################################
########################################################################

class CallReturn():
    def __init__(self, expression):
        self.expression = expression
    def accept(self, visitor):
        Visitor.visitCallReturn(self)

class CallReturnAt():
    def __init__(self, expression):
        self.expression = expression
    def accept(self, visitor):
        Visitor.visitCallReturnAt(self)

class CallContinue():
    def __init__(self):
        self
    def accept(self, visitor):
        Visitor.visitCallContinue(self)

class CallContinueAt():
    def __init__(self):
        self
    def accept(self, visitor):
        Visitor.visitCallContinueAt(self)

class CallBreak():
    def __init__(self):
        self
    def accept(self, visitor):
        Visitor.visitCallBreak(self)

class CallBreakAt():
    def __init__(self):
        self
    def accept(self, visitor):
        Visitor.visitCallBreakAt(self)
########################################################################

class SimpleCallableReference_SI(KotlinFile):
    def __init__(self, simpleIdentifier):
        self.simpleIdentifier=simpleIdentifier
    def accept (self,visitor):
        Visitor.visitSimpleCallableReference_SI(self)

class CompoundCallableReference_SI(KotlinFile):
    def __init__(self, receiverType, simpleIdentifier):
        self.receiverType = receiverType
        self.simpleIdentifier=simpleIdentifier
    def accept (self,visitor):
        Visitor.visitCompoundCallableReference_SI(self)
########################################################################

class SimpleCallableReference_Class(KotlinFile):
    def __init__(self):
        self
    def accept (self,visitor):
        Visitor.visitSimpleCallableReference_Class(self)

class CompoundCallableReference_Class(KotlinFile):
    def __init__(self, receiverType):
        self.receiverType=receiverType
    def accept (self,visitor):
        Visitor.visitCompoundCallableReference_Class(self)
########################################################################

class CallMAISIGUAL():
    def __init__(self):
        self
    def accept(self, visitor):
        Visitor.visitMAISIGUAL(self)

class CallMENOSIGUAL():
    def __init__(self):
        self
    def accept(self, visitor):
        Visitor.visitMENOSIGUAL(self)

class CallMULTIGUAL():
    def __init__(self):
        self
    def accept(self, visitor):
        Visitor.visitMULTIGUAL(self)

class CallDIVIGUAL():
    def __init__(self):
        self
    def accept(self, visitor):
        Visitor.visitDIVIGUAL(self)

class CallMODIGUAL():
    def __init__(self):
        self
    def accept(self, visitor):
        Visitor.visitMODIGUAL(self)       
########################################################################

class CallDiferente():
    def __init__(self):
        self
    def accept(self, visitor):
        Visitor.visitCallDiferente(self)

class CallIdentidade():
    def __init__(self):
        self
    def accept(self, visitor):
        Visitor.visitCallIdentidade(self)

class CallIgualdade():
    def __init__(self):
        self
    def accept(self, visitor):
        Visitor.visitCallIgualdade(self)

class CallSemIdentidade():
    def __init__(self):
        self
    def accept(self, visitor):
        Visitor.visitCallSemIdentidade(self)
########################################################################

class CallMenor():
    def __init__(self):
        self
    def accept(self, visitor):
        Visitor.visitCallMenor(self)

class CallMaior():
    def __init__(self):
        self
    def accept(self, visitor):
        Visitor.visitCallMAIOR(self)

class CallMenorIgual():
    def __init__(self):
        self
    def accept(self, visitor):
        Visitor.visitCallMenorIgual(self)

class CallMaiorIgual():
    def __init__(self):
        self
    def accept(self, visitor):
        Visitor.visitCallMaiorIgual(self)
########################################################################

class CallNotIn():
    def __init__(self):
        self
    def accept(self, visitor):
        Visitor.visitCallNotIn(self)
########################################################################

class CallNotIs():
    def __init__(self):
        self
    def accept(self, visitor):
        Visitor.visitCallNotIs(self)

class CallIs():
    def __init__(self):
        self
    def accept(self, visitor):
        Visitor.visitCallIS(self)
########################################################################

class CallPlus():
    def __init__(self):
        self
    def accept(self, visitor):
        Visitor.visitCallPlus(self)

class CallMinus():
    def __init__(self):
        self
    def accept(self, visitor):
        Visitor.visitCallMINUS(self)
########################################################################

class CallMult():
    def __init__(self):
        self
    def accept(self, visitor):
        Visitor.visitCallMult(self)

class CallMod():
    def __init__(self):
        self
    def accept(self, visitor):
        Visitor.visitCallMod(self)

class CallDivide():
    def __init__(self):
        self
    def accept(self, visitor):
        Visitor.visitCallDivide(self)
########################################################################

class SimpleAsOperator(KotlinFile):
    def __init__(self):
        self
    def accept(self, visitor):
        Visitor.visitSimpleAsOperator(self)

class CompoundAsOperator(KotlinFile):
    def __init__(self, asOperator):
        self.asOperator=asOperator
    def accept(self, visitor):
        Visitor.visitCompoundAsOperator(self)
########################################################################

class CallNot():
    def __init__(self):
        self
    def accept(self, visitor):
        Visitor.visitCallNot(self)

class CallIncremento():
    def __init__(self):
        self
    def accept(self, visitor):
        Visitor.visitCallIncremento(self)
        
class CallDecremento():
    def __init__(self):
        self
    def accept(self, visitor):
        Visitor.visitCallDecremento(self)
########################################################################

class CallPonto():
    def __init__(self):
        self
    def accept(self, visitor):
        Visitor.visitCallPonto(self)

class CallColonColon():
    def __init__(self):
        self
    def accept(self, visitor):
        Visitor.visitCallColonColon(self)

class CallSafenav():
    def __init__(self, safenav):
        self.safenav = safenav
    def accept(self, visitor):
        Visitor.visitCallSafenav(self)
