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
###################################################################################
class kotlinFile():
    def __init__(self):
        self
    def accept(self,visitor):
        visitor.visitkotlinFile(self)

class CompoundFunctionDeclaration(kotlinFile):
    def __init__(self, fd, kf):
        self.fd = fd
        self.kf = kf
    def accept(self, visitor):
        visitor.visitCompoundFunctionDeclaration(self)

class SingleFunctionDeclaration(kotlinFile):
    def __init__(self, fd):
        self.fd = fd
    def accept(self, visitor):
        visitor.visitSingleFunctionDeclaration(self)

class FunctionDeclaration(kotlinFile):
    def __init__(self, fun, SI, FVL, doisp, type, block):
        self.fun=fun
        self.SI=SI
        self.FVL=FVL
        self.doisp=doisp
        self.tipe=type
        self.block=block
    def accept(self,visitor):
        Visitor.visitFunctionDeclaration(self)

class TypeParameters(kotlinFile):
    def __init__(self, menor, tps, maior):
       self.menor = menor
       self.tps = tps
       self.maior = maior
    def accept(self, visitor):
        visitor.visitTypeParameters(self)

class SimpleTps(kotlinFile):
    def __init__(self, tp):
       self.tp = tp
    def accept(self, visitor):
        visitor.visitSingleTps(self)

class CompoundTps(kotlinFile):
    def __init__(self, tp, COMMA, tps):
       self.tp = tp
       self.COMMA=COMMA
       self.tps=tps
    def accept(self, visitor):
        visitor.visitCompoundTps(self)

class CompoundTypeParameter(kotlinFile):
    def __init__(self, si, doisp, type):
       self.si = si
       self.doisp=doisp
       self.tipe=type
    def accept(self, visitor):
        visitor.visitCompoundTypeParameter(self)

class SingleTypeParameter(kotlinFile):
    def __init__(self, si, doisp, type):
       self.si = si
       self.doisp=doisp
       self.tipe=type
    def accept(self, visitor):
        visitor.visitSingleTypeParameter(self)

class SingleFunctionValueParameters(kotlinFile):
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

class SingleFvps(SingleFunctionValueParameters):
    def __init__(self, fvps):
        self.fvps=fvps
    def accept(self, visitor):
        visitor.visitSingleFvps(self)

class CompoundFvps(CompoundFunctionValueParameters):
    def __init__(self, fvp,COMMA, fvps):
        self.fvp=fvp
        self.COMMA=COMMA
        self.fvps=fvps
    def accept(self, visitor):
        visitor.visitCompoundFvps(self)

class SingleFunctionValeuParameter(kotlinFile):
    def __init__(self, parameter):
        self.Parameter=parameter
    def accept(self,visitor):
        visitor.visitSingleFunctionValueParameter(self)
        
class CompoundFunctionValeuParameter(kotlinFile):
    def __init__(self, parameter, atribuicao, exp):
        self.Parameter=parameter
        self.atribuicao=atribuicao
        self.exp=exp
    def accept(self,visitor):
        visitor.visitCompoundFunctionValueParameter(self)

class SimpleVariableDeclaration(kotlinFile):
    def __init__(self, simpleIdentifier):
        self.simpleIdentifier = simpleIdentifier
    def accept(self, visitor):
        visitor.visitvariableDeclaration(self)

class CompoundVariableDeclaration(kotlinFile):
    def __init__(self, simpleIdentifier, DOISP, type):
        self.simpleIdentifier = simpleIdentifier
        self.DOISP=DOISP
        self.type=type
    def accept(self, visitor):
        visitor.visitvariableDeclaration(self)

class MultiVariableDeclaration(kotlinFile):
    def __init__(self, LP, mvd, RP):
        self.LP=LP
        self.RP=RP
        self.mvd=mvd
    def accept(self, visitor):
        visitor.visitmltiVariableDeclaration(self)

class SingleMvd(MultiVariableDeclaration):
    def __init__(self, variableDeclaration):
        self.variableDeclaration=variableDeclaration
    def accept(self, visitor):
        visitor.visitSingleMvd(self)

class CompoundMvd(MultiVariableDeclaration):
    def __init__(self, variableDeclaration, COMMA, mvd ):
        self.mvd=mvd
        self.COMMA=COMMA
        self.variableDeclaration=variableDeclaration
    def accept(self, visitor):
        visitor.visitCompoundMvd(self)

class propertyDeclaration(kotlinFile):
    def __init__(self, VAR, VAL, multiVariableDeclaration, IGUALDADE, expression, PV):
        self.var=VAR
        self.val=VAL
        self.multiVariableDeclaration=multiVariableDeclaration
        self.igualdade=IGUALDADE
        self.expression=expression
    def accept(self, visitor):
        visitor.visitpropertyDeclaration(self)

class parameter(kotlinFile):
    def __init__(self,simpleIdentifier, DOISP, type ):
        self.simpleIdentifier= simpleIdentifier
        self.doisp= DOISP
        self.type=type
    def accept(self, visitor):
        visitor.visitparameter(self)

class  Compoundtype(kotlinFile):
    def __init__(self,typeModifiers, optype ):
        self.typeModifiers=typeModifiers  
        self.optype=optype
    def accept(self, visitor):
        visitor.visittype(self)
class SingleType(kotlinFile):
    def __init__(self,optype):
        self.optype=optype
    def accept (self, visitor):
        visitor.visitSingleType(self)
class opType(kotlinFile):
    def __init__(self,parenthesizedType , functionType , userType):
        self.parenthesizedType=parenthesizedType
        self.functionType=functionType 
        self.userType=userType
    def accept(self, visitor):
        visitor.visitopType(self)

class userType(kotlinFile):
    def __init__(self,simpleUserType):
        self.simpleUserType=simpleUserType
    def accept(self, visitor):
        visitor.visituserType(self)

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

class SimpleFunctionType(kotlinFile):
    def __init__(self, functionTypeParameters, SETA, type):
        self.functionTypeParameters=functionTypeParameters
        self.SETA=SETA
        self.type=type
    def accept(self, visitor):
        visitor.visitSimpleFunctionType(self)

class CompoundFunctionType(kotlinFile):
    def __init__(self, receiverType, PONTO, functionTypeParameters, SETA, type):
        self. receiverType= receiverType
        self.PONTO=PONTO
        self.functionTypeParameters=functionTypeParameters
        self.SETA=SETA
        self.type=type
    def accept(self, visitor):
        visitor.visitCompoundFunctionType(self)
        
class parenthesizedType(kotlinFile):
    def __init__(self, LPAREN, type,RPAREN ):
        self.LPAREN=LPAREN
        self.type=type
        self.RPAREN=RPAREN
    def accept(self, visitor):
        visitor.visitparenthesizedType(self)
        
class receiverType(kotlinFile):
    def __init__(self, typeModifier, rt):
        self.typeModifier=typeModifier
        self.rt=rt
    def accept(self, visitor):
        visitor.visitreceiverType(self)
        
class rt( receiverType):
    def __init__(self, parenthesizedType, nullableType, typeReference):
        self. parenthesizedType= parenthesizedType
        self.nullableType=nullableType
        self.typeReference=typeReference
    def accept(self, visitor):
        visitor.visitrt(self)
        
class parenthesizedUserType(kotlinFile):
    def __init__(self,LPAREN, userType, RPAREN,parenthesizedUserType):
        self.LPAREN=LPAREN
        self.userType=userType
        self.RPAREN=RPAREN
        self.parenthesizedUserType=parenthesizedUserType
    def accept(self, visitor):
        visitor.visitparenthesizedUserType(self)

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

class statement (SimpleStatements,CompoundStatements):
    def __init__(self, functionDeclaration, assignment ,loopStatement ,expression): 
        self.functionDeclaration=functionDeclaration
        self.assignment=assignment
        self.loopStatement=loopStatement
        self.expression=expression
    def accept(self, visitor):
        visitor.visitstatement(self)

class controlStructureBody(CompoundStatements):
    def __init__(self, block, statement):
        self.block=block
        self.statement=statement
    def accept(self, visitor):
        visitor.visitcontrolStructureBody(self)

class block(controlStructureBody):
    def __init__(self,LCHAVE, statements, RCHAVE):
        self.LCHAVE=LCHAVE
        self.statements=statements
        self.RCHAVE=RCHAVE
    def accept(self, visitor):
        visitor.visitblock(self)

class  loopStatement(statement):
    def __init__(self,forStatement, whileStatement, doWhileStatement):
        self.forStatement=forStatement
        self.whileStatement=whileStatement
        self.doWhileStatement=doWhileStatement
    def accept(self,visitor):
        visitor.visitloopStatement(self)

class SimpleForStatement_MD(loopStatement):
    def __init__(self, FOR, LPAREN, multiVariableDeclaration, IN, expression, RPAREN):
        self.FOR=FOR
        self.LPAREN=LPAREN
        self.multiVariableDeclaration=multiVariableDeclaration
        self.IN=IN
        self.expression=expression
        self.RPAREN=RPAREN
    def accept(self, visitor):
        visitor.visitSimpleForStatement_MD(self)

class CompoundForStatement_MD(loopStatement):
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

class SimpleForStatement_VD(loopStatement):
    def __init__(self, FOR, LPAREN, variableDeclaration, IN, expression, RPAREN):
        self.FOR=FOR
        self.LPAREN=LPAREN
        self.variableDeclaration=variableDeclaration
        self.IN=IN
        self.expression=expression
        self.RPAREN=RPAREN
    def accept(self, visitor):
        visitor.visitSimpleForStatement_MD(self)

class CompoundForStatement_VD(loopStatement):
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

class WhileStatement(loopStatement):
    def __init__(self,WHILE, LPAREN, expression, RPAREN, controlStructureBody):
        self.WHILE=WHILE
        self.LPAREN=LPAREN
        self.expression=expression
        self.RPAREN=RPAREN
        self.controlStructureBody=controlStructureBody
    def accept(self, visitor):
        visitor.visitwhileStatement(self)
        
class SimpleDoWhileStatement(loopStatement):
    def __init__(self,DO, WHILE ,LPAREN, expression, RPAREN): 
        self.do=DO
        self.WHILE=WHILE 
        self.LPAREN=LPAREN
        self.expression=expression
        self. RPAREN= RPAREN
    def accept(self, visitor):
        visitor.visitSimpleDoWhileStatement(self)

class CompoundDoWhileStatement(loopStatement):
    def __init__(self,DO, controlStructureBody, WHILE ,LPAREN, expression, RPAREN): 
        self.do=DO
        self.controlStructureBody=controlStructureBody
        self.WHILE=WHILE 
        self.LPAREN=LPAREN
        self.expression=expression
        self. RPAREN= RPAREN
    def accept(self, visitor):
        visitor.visitCompoundDoWhileStatement(self)
        
class assignment(statement):
    def __init__(self,directlyAssignableExpression, IGUALDADE ,expression): 
        self.directlyAssignableExpression=directlyAssignableExpression
        self.IGUALDADE=IGUALDADE
        self.expression=expression
    def accept(self, visitor):
        visitor.vistassignment(self)
        
class Semi(propertyDeclaration):
    def __init__(self, EOF):
        self.EOF=EOF
    def accept(self,visitor):
        visitor.visitWemi(self)
        
class Expression(kotlinFile):
    def __init__(self,disjunction ):
        self.disjunction =disjunction 
    def accept (self,visitor):
        visitor.visitExpression(self)
        
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
        
class infixOperation(SimpleComparison,CompoundComparison):
    def __init__(self,elvisExpression, io):
        self.elvisExpression=elvisExpression
        self.io=io
    def accept (self,visitor):
        visitor.visitinfixOperation(self)
        
class io(infixOperation):
    def __init__(self,inOperator, elvisExpression,type,null):
        self.inOperator=inOperator
        self.elvisExpression=elvisExpression
        self.type=type
        self.null=null
    def accept (self,visitor):
        visitor.visitio(self)
        
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
        
class rangeExpression(SimpleInfixFunctionCall,CompoundInfixFunctionCall):
    def __init__(self,additiveExpression, PONTOPONTO, rangeExpression):
        self.additiveExpression=additiveExpression
        self.PONTOPONTO=PONTOPONTO
        self.rangeExpression=rangeExpression
    def accept(self, visitor):
        visitor.visitrangeExpression(self)
        
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
        
class PrefixUnaryExpression(SimpleAsExpression,CompoundAsExpression):
    def __init__(self,preue, postfixUnaryExpression):
        self.preue=preue
        self.postfixUnaryExpression=postfixUnaryExpression
    def accept(self,visitor):
        visitor.visitPrefixUnaryExpression(self)
        
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
        
class unaryPrefix(SimplePreue,CompoundPreue):
    def __init__(self,annotation, label, prefixUnaryOperator):
        self.annotation=annotation
        self.label=label
        self.prefixUnaryOperator=prefixUnaryOperator
    def accept(self,visitor):
        visitor.vistunaryPrefix(self)

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

class postfixUnarySuffix(SinglePosue,CompoundPosue):
    def __init__(self,postfixUnaryOperator,typeArguments,callSuffix,indexingSuffix,navigationSuffix):
        self.postfixUnaryOperator=postfixUnaryOperator
        self.typeArguments=typeArguments
        self.callSuffix=callSuffix
        self.indexingSuffix=indexingSuffix
        self.navigationSuffix=navigationSuffix
    def accept(self, visitor):
        visitor.visitpostfixUnarySuffix(self)
        
class directlyAssignableExpression(SimplePostfixUnaryExpression,CompoundPostfixUnaryExpression):
    def __init__(self,postfixUnaryExpression, assignableSuffix,simpleIdentifier,parenthesizedDirectlyAssignableExpression):
        self.postfixUnaryExpression=postfixUnaryExpression
        self.assignableSuffix=assignableSuffix
        self.simpleIdentifier=simpleIdentifier
        self.parenthesizedDirectlyAssignableExpression=parenthesizedDirectlyAssignableExpression
    def accept(self, visitor):
        visitor.visitdirectlyAssignableExpression(self)
        
class parenthesizedDirectlyAssignableExpression(directlyAssignableExpression):
    def __init__(self,LPAREN, directlyAssignableExpression, RPAREN):
        self.LPAREN=LPAREN
        self.directlyAssignableExpression=directlyAssignableExpression
        self.RPAREN=RPAREN
    def accept(self,visitor):
        visitor.visitparenthesizedDirectlyAssignableExpression(self)
        
class assignableExpression(SimplePostfixUnaryExpression,CompoundPostfixUnaryExpression):
    def __init__(self,prefixUnaryExpression, parenthesizedAssignableExpression):
        self.prefixUnaryExpression=prefixUnaryExpression
        self.parenthesizedAssignableExpression=parenthesizedAssignableExpression
    def accept(self,visitor):
        visitor.visitassignableExpression(self)
        
class ParenthesizedAssignableExpression(assignableExpression):
    def __init__(self, LPAREN, assignableExpression, RPAREN):
        self.LPAREN=LPAREN
        self.assignableExpression=assignableExpression
        self.RPAREN= RPAREN
    def accept(self, visitor):
        visitor.visitparenthesizedAssignableExpression(self)
        
class AssignableSuffix(directlyAssignableExpression):
    def __init__(self,typeArguments, indexingSuffix, navigationSuffix):
        self.typeArguments=typeArguments
        self.indexingSuffix=indexingSuffix
        self.navigationSuffix=navigationSuffix
    def accept(self, visitor):
        visitor.visitassignableSuffix(self)
        
class IndexingSuffix(kotlinFile):
    def __init__(self,LCCT, isuf, RCCT):
        self.LCCT=LCCT
        self.isuf=isuf
        self.RCCT=RCCT
    def accept(self,visitor):
        visitor.visitindexingSuffix(self)
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
        
class NavigationSuffix(kotlinFile):
    def __init__(self, memberAccessOperator, simpleIdentifier, CLASS,parenthesizedExpression): 
        self.memberAccessOperator=memberAccessOperator
        self.simpleIdentifier=simpleIdentifier
        self.CLASS=CLASS
        self.parenthesizedExpression=parenthesizedExpression
    def accept(self, visitor):
        visitor.vistnavigationSuffix(self)
        
class CallSuffix(kotlinFile):
    def __init__(self,typeArguments, valueArguments, annotatedLambda):
        self.typeArguments=typeArguments
        self.valueArguments=valueArguments
        self.annotatedLambda=annotatedLambda
    def accept(self,visitor):
        visitor.visitcallSuffix(self) 
        
class AnnotatedLambda(kotlinFile):
    def __init__(self,lambdaLiteral):
        self.lambdaLiteral=lambdaLiteral
    def accept(self,visitor):
        visitor.visitannotatedLambda(self)
        
class TypeArguments(kotlinFile):
    def __init__(self,MENOR ,ta, MAIOR):
        self.MENOR=MENOR
        self.ta=ta
        self.MAIOR=MAIOR
    def accept(self,visitor):
        visitor.visittypeArguments(self)
        
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

class PrimaryExpression(kotlinFile):
    def __init__(self,parenthesizedExpression,simpleIdentifier,literalConstant,stringLiteral,callableReference,functionLiteral,objectLiteral,collectionLiteral,ifExpression,jumpExpressio):
        self.parenthesizedExpression=parenthesizedExpression
        self.simpleIdentifier=simpleIdentifier
        self.literalConstant=literalConstant
        self.stringLiteral=stringLiteral
        self.callableReference=callableReference
        self.functionLiteral=functionLiteral
        self.objectLiteral=objectLiteral
        self.collectionLiteral=collectionLiteral
        self.ifExpression=ifExpression
        self.jumpExpression=jumpExpression
    def accept(self,visitor):
        visitor.visitprimaryExpression(self)
        
class ParenthesizedExpression(kotlinFile):
    def __init__(self,LPAREN ,expression, RPAREN):
        self.LPAREN=LPAREN
        self.expression=expression
        self.RPAREN=RPAREN
    def accept(self,visitor):
        visitor.visitparenthesizedExpression(self)

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

class literalConstant(kotlinFile):
    def __init__(self,BooleanLiteral,IntegerLiteral,HexLiteral,BinLiteral,CharacterLiteral,RealLiteral,null,LongLiteral,UnsignedLiteral):
        self.BooleanLiteral=BooleanLiteral
        self.IntegerLiteral=IntegerLiteral
        self.HexLiteral=HexLiteral
        self.BinLiteral=BinLiteral
        self.CharacterLiteral=CharacterLiteral
        self.RealLiteral=RealLiteral
        self.null=null
        self.LongLiteral=LongLiteral
        self.UnsignedLiteral=UnsignedLiteral
    def accept(self, visitor):
        visitor.visitliteralConstant(self)

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

