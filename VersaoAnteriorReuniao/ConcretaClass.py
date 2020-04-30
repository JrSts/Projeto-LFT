from Visitor import Visitor
from AbstrataClass import abstractmethod 
class SomaExp(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, Visitor):
        Visitor.visitSomaExp(self)

class MulExp(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, Visitor):
        Visitor.visitMulExp(self)

class PotExp(Exp):
    def __init__(self,exp2,exp3):
        self.exp2 = exp2
        self.exp3 = exp3
    def accept(self, Visitor):
        Visitor.visitPotExp(self) 

class CallExp(Call):
    def __init__(self, call):
        self.call = call
    def accept(self, Visitor):
        Visitor.visitCallexp(self)
        
class AssignExp(Assign):
    def __init__(self,assign):
        self.assign = assign
    def accept(self,Visitor):
        Visitor.visitAssignExp(self)

class NumExp(num):
    def __init__(self,num):
        self.num = num
    def accept(self,Visitor):
        Visitor.visitorNumExp(self)
        
class IDExp (Id):
    def __init__(self,id):
        self.id = id
    def accept(self, Visitor):
        Visitor.visitIDExp(self)

class ParamsCall(Call):
    def __init__(self,EXP,Params):
        self.EXP = EXP
        self.Params = Params
    def accept(self,Visitor):
        Visitor.visitParamsCall(self)
class SimplesCall(Call):
    def __init__(self, ID):
        self.ID = ID
    def accept(self, Visitor):
        Visitor.visitSimplesCall(self)
class CompoundParams(Params):
    def __init__(self,ID,Params):
        self.ID = ID
        self.Params = Params
    def accept(self,Visitor):
        Visitor.visitCompoundParams(self)
class SingleParam(params):
    def __init__(self, ID):
        self.ID = ID
    def accept(self, Visitor):
        Visitor.visitSingleParam(self)

class AssignExp(Assign):
    def __init__(self, ID,Exp):
        self.ID = ID
        self.Exp = Exp
    def accept(self , Visitor):
        Visitor.visitAssighExp(self)
#############################################

class CompoundFunctionDeclaration(KotlinFile):
    def __init__(self, fd, kf):
        self.fd = fd
        self.kf = kf
    def accept(self, visitor):
        visitor.visitCompoundFunctionDeclaration(self)

class FunctionDeclaration(KotlinFile):
    def __init__(self, fun, SI, FVL, LP, RP,doisp, type, block):
        self.fun=fun
        self.SI=SI
        self.FVL=FVL
        self.LP=LP
        self.RP=RP
        self.doisp=doisp
        self.tipe=type
        self.block=block
    def accept(self,visitor):
        Visitor.visitfunctionDeclaration(self)

class TypeParameters(KotlinFile):
    def __init__(self, menor, tps, maior):
       self.menor = menor
       self.tps = tps
       self.maior = maior
    def accept(self, visitor):
        visitor.visitTypeParameters(self)

class Tps(KotlinFile):
    def __init__(self, tp, lp,rp, COMMA):
       self.tp = tp
       self.lp = lp
       self.rp = rp
       self.COMMA=COMMA
    def accept(self, visitor):
        visitor.visitTps(self)

class TypeParameter(KotlinFile):
    def __init__(self, si, lp,rp, doisp, type):
       self.si = si
       self.lp = lp
       self.rp = rp
       self.doisp=doisp
       self.tipe=type
    def accept(self, visitor):
        visitor.visitTypeParameter(self)

class functionValueParameters(KotlinFile):
    def __init__(self, lp,rp, fvps):
       self.si = si
       self.lp = lp
       self.fvps=fvps
    def accept(self, visitor):
        visitor.visitfunctionValueParameters(self)
class fvps(functionValueParameters):
    def __init__(self, fvp,COMMA, fvps):
        self.fvp=fvp
        self.COMMA=COMMA
        self.fvps=fvps
    def accept(self, visitor):
        visitor.visitfvps(self)

class FunctionValeuParametr(KotlinFile):
    def __init__(self, parameter, iguadade, exp):
        self.Parameter=parameter
        self.iguadade=iguadade
        self.exp=exp
    def accept(self,visitor):
        visitor.visitFunctionValueParameter(self)

class variableDeclaration(KotlinFile):
    def __init__(self, annot, simpleIdentifier, DOISP, type):
        self.annnot=annot
        self.simpleIdentifier = simpleIdentifier
        self.DOISP=DOISP
        self.type=type
    def accept(self, visitor):
        visitor.visitvariableDeclaration(self)

class annot(variableDeclaration):
    def __init__(self, annotation, annot):
        self.annot=annot
        self.annotation=annotation
    def accept(self, visitor):
        visitor.visitannot(self)

class multiVariableDeclaration(KotlinFile):
    def __init__(self, LP, mvd, RP):
        self.LP=LP
        self.RP=RP
        self.mvd=mvd
    def accept(self, visitor):
        visitor.visitmltiVariableDeclaration(self)

class mvd(multiVariableDeclaration):
    def __init__(self, variableDeclaration, COMMA, mvd ):
        self.mvd=mvd
        self.COMMA=COMMA
        self.variableDeclaration=variableDeclaration
    def accept(self, visitor):
        visitor.visitmvd(self)

class propertyDeclaration(KotlinFile):
    def __init__(self, VAR, VAL, multiVariableDeclaration, IGUALDADE, expression, PV):
        self.var=VAR
        self.val=VAL
        self.multiVariableDeclaration=multiVariableDeclaration
        self.igualdade=IGUALDADE
        self.expression=expression
    def accept(self, visitor):
        visitor.visitpropertyDeclaration(self)

class parameter(KotlinFile):
    def __init__(self,simpleIdentifier, DOISP, type ):
        self.simpleIdentifier= simpleIdentifier
        self.doisp= DOISP
        self.type=type
    def accept(self, visitor):
        visitor.visitparameter(self)
class type(KotlinFile):
    def __init__(self,typeModifiers, optype ):
        self.typeModifiers=typeModifiers  
        self.optype=optype
    def accept(self, visitor):
        visitor.visittype(self) 
class opType(KotlinFile):
    def __init__(self,parenthesizedType , functionType , userType):
        self.parenthesizedType=parenthesizedType
        self.functionType=functionType 
        self.userType=userType
    def accept(self, visitor):
        visitor.visitopType(self)
class userType(KotlinFile):
    def __init__(self,simpleUserType):
        self.simpleUserType=simpleUserType
    def accept(self, visitor):
        visitor.visituserType(self)
class simpleUserType(userType):
    def __init__(self, simpleUserType,typeArguments):
        self.simpleUserType=simpleUserType
        self.typeArguments=typeArguments
    def accept(self, visitor):
        visitor.visitsimpleUserType(self)
class typeProjection(KotlinFile):
    def __init__(self, typeProjectionModifiers, type):
        self.typeProjectionModifiers= typeProjectionModifiers
        self.type=type
    def accept(self,visitor):
        visitor.visittypeProjection(self)
class typeProjectionModifiers(typeProjection):
    def __init__(self, typeProjectionModifier, typeProjectionModifiers):
        self.typeProjectionModifier =typeProjectionModifier 
        self.typeProjectionModifiers=typeProjectionModifiers
    def accept(self, visitor):
        visitor.visittypeProjectionModifiers(self)

class functionType(KotlinFile):
    def __init__(self, receiverType, PONTO, functionTypeParameters, SETA, type):
        self. receiverType= receiverType
        self.PONTO=PONTO
        self.functionTypeParameters=functionTypeParameters
        self.SETA=SETA
        self.type=type
    def accept(self, visitor):
        visitor.visitfunctionType(self)
class parenthesizedType(KotlinFile):
    def __init__(self, COMMA, type):
        self.COMMA=COMMA
        self,type=type
    def accept(self, visitor):
        visitor.visitparenthesizedType(self)
class receiverType(KotlinFile):
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
class parenthesizedUserType(KotlinFile):
    def __init__(self,LPAREN, userType, RPAREN,parenthesizedUserType):
        self.LPAREN=LPAREN
        self.userType=userType
        self.RPAREN=RPAREN
        self.parenthesizedUserType=parenthesizedUserType
    def accept(self, visitor):
        visitor.visitparenthesizedUserType(self)
class statements (KotlinFile):
    def __init__(self, statement, statments): 
        self.statement=statement  
        self.statments=statments
    def accept(self, visitor):
        visitor.visitstatemnts(self)
class statement (statements):
    def __init__(self, functionDeclaration, assignment ,loopStatement ,expression): 
        self.functionDeclaration=functionDeclaration
        self.assignment=assignment
        self.loopStatement=loopStatement
        self.expression=expression
    def accept(self, visitor):
        visitor.visitstatement(self)
class controlStructureBody(KotlinFile,statement):
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
class forStatement(loopStatement):
    def __init__(self, FOR, LPAREN, multiVariableDeclaration, IN, expression, RPAREN, controlStructureBody):
        self.FOR=FOR
        self.LPAREN=LPAREN
        self. multiVariableDeclaration= multiVariableDeclaration
        self.IN=IN
        self.expression=expression
        self.RPAREN=RPAREN
        self.controlStructureBody=controlStructureBody
    def accept(self, visitor):
        visitor.visitforStatement(self)
class whileStatement(loopStatement):
    def __init__(self,WHILE, LPAREN, expression, RPAREN, controlStructureBody):
        self.WHILE=WHILE
        self.LPAREN=LPAREN
        self.expression=expression
        self.RPAREN=RPAREN
        self.controlStructureBody=controlStructureBody
    def accept(self, visitor):
        visitor.visitwhileStatement(self)
class doWhileStatement(loopStatement):
    def __init__(self,DO, controlStructureBody, WHILE ,LPAREN, expression, RPAREN): 
        self.do=DO
        self.controlStructureBody=controlStructureBody
        self.WHILE=WHILE 
        self.LPAREN=LPAREN
        self.expression=expression
        self. RPAREN= RPAREN
    def accept(self, visitor):
        visitor.visitdoWhileStatement(self)
class assignment(statement):
    def __init__(self,directlyAssignableExpression, IGUALDADE ,expression): 
        self.directlyAssignableExpression=directlyAssignableExpression
        self.IGUALDADE=IGUALDADE
        self.expression=expression
    def accept(self, visitor):
        visitor.vistassignment(self)
class semi(propertyDeclaration):
    def __init__(self, EOF):
        self.EOF=EOF
    def accept(self,visitor):
        visitor.visitsemi(self)
class expression(KotlinFile):
    def __init__(self,disjunction ):
        self.disjunction =disjunction 
    def accept (self,visitor):
        visitor.visitexpression(self)
class disjunction(expression):
    def __init__(self,conjunction ,OR, disjunction):
        self.conjunction=conjunction
        self.OR=OR
        self.disjunction=disjunction
    def accept (self,visitor):
        visitor.visitdisjunction(self)
class conjunction(disjunctuon):
    def __init__(self,equality,conjunction,ecomecial):
        self.equality=equality
        self.conjunction=conjunction
        self.ecomecial=ecomecial
    def accept (self,visitor):
        visitor.vistconjunction(self)
class equality(conjuction):
    def __init__(self,comparison, equalityOperator, equality):
        self.comparison=comparison
        self.equalityOperator=equalityOperator
        self.equality=equality
    def accept(self,visitor):
        visitor.visitequality(self)
class comparison(equality):
    def __init__(self, infixOperation, comparisonOperator):
        self.infixOperation=infixOperation
        self.comparisonOperator=comparisonOperator
    def accept (self,visitor):
        visitor.vistcomparison(self)
class infixOperation(comparison):
    def __init__(self,elvisExpression, io):
        self.elvisExpression=elvisExpression
        self.io=io
    def accept (self,visitor):
        visitor.visitinfixOperation(self)
class io(KotlinFile,infixOperation):
    def __init__(self,inOperator, elvisExpression,type,null):
        self.inOperator=inOperator
        self.elvisExpression=elvisExpression
        self.type=type
        self.null=null
    def accept (self,visitor):
        visitor.visitio(self)
class elvisExpression(io):
    def __init__(self,infixFunctionCall, elvis, elvisExpression ):
        self.infixFunctionCall=infixFunctionCall
        self.elvis=elvis
        self.elvisExpression=elvisExpression
    def accept(self,visitor):
        visitor.visitelvisExpression(self)
class infixFunctionCall(elvisExpression):
    def __init__(self,rangeExpression, simpleIdentifier, infixFunctionCall):
        self.rangeExpression=rangeExpression
        self.simpleIdentifier=simpleIdentifier
        self.infixFunctionCall=infixFunctionCall
    def accept (self,visitor):
        visitor.visitinfixFunctionCall(self)
class rangeExpression(infixFunctionCall):
    def __init__(self,additiveExpression, PONTOPONTO, rangeExpression):
        self.additiveExpression=additiveExpression
        self.PONTOPONTO=PONTOPONTO
        self.rangeExpression=rangeExpression
    def accept(self, visitor):
        visitor.visitrangeExpression(self)
class additiveExpression(rangeExpression):
    def __init__(self,multiplicativeExpression ,additiveOperator, additiveExpression):
        self.multiplicativeExpression=multiplicativeExpression
        self.additiveOperator=additiveOperator
        self.additiveExpression=additiveExpression
    def accept (self,visitor):
        visitor.visitadditiveExpression(self)
class multiplicativeExpression(additiveExpression):
    def __init__(self,asExpression ,multiplicativeOperator, multiplicativeExpression):
        self.asExpression=asExpression
        self.multiplicativeOperator=multiplicativeOperator
        self.multiplicativeExpression=multiplicativeExpression
    def accept(self, visitor):
        visitor.visitmultiplicativeExpression(self)
class asExpression(multiplicativeExpression):
    def __init__(self,prefixUnaryExpression, asOperator, type):
        self.prefixUnaryExpression=prefixUnaryExpression
        self.asOperator=asOperator
        self.type=type
    def accept (self, visitor):
        visitor.visitasExpression(self)
class prefixUnaryExpression(asExpression):
    def __init__(self,preue, postfixUnaryExpression):
        self.preue=preue
        self.postfixUnaryExpression=postfixUnaryExpression
    def accept(self,visitor):
        visitor.visitprefixUnaryExpression(self)
class preue(prefixUnaryExpression):
    def __init__(self,unaryPrefix ,preue):
        self.unaryPrefix=unaryPrefix
        self.preue=preue
    def accept(self, visitor):
        visitor.visitpreue(self)
class unaryPrefix(preue):
    def __init__(self,annotation, label, prefixUnaryOperator):
        self.annotation=annotation
        self.label=label
        self.prefixUnaryOperator=prefixUnaryOperator
    def accept(self,visitor):
        visitor.vistunaryPrefix(self)
class postfixUnaryExpression(KotlinFile):
    def __init__(self,primaryExpression ,posue):
        self.primaryExpression=primaryExpression
        self.posue=posue
    def accept(self, visitor):
        visitor.visitpostfixUnaryExpression(self)
class posue(postfixUnaryExpression):
    def __init__(self,postfixUnarySuffix, posue):
        self.postfixUnarySuffix=postfixUnarySuffix
        self.posue=posue
    def accept(self,visitor):
        visitor.visitposue(self)
class postfixUnarySuffix(posue):
    def __init__(self,postfixUnaryOperator,typeArguments,callSuffix,indexingSuffix,navigationSuffix):
        self.postfixUnaryOperator=postfixUnaryOperator
        self.typeArguments=typeArguments
        self.callSuffix=callSuffix
        self.indexingSuffix=indexingSuffix
        self.navigationSuffix=navigationSuffix
    def accept(self, visitor):
        visitor.visitpostfixUnarySuffix(self)
class directlyAssignableExpression(postfixUnaryExpression):
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
class assignableExpression(postfixUnaryExpression):
    def __init__(self,prefixUnaryExpression, parenthesizedAssignableExpression):
        self.prefixUnaryExpression=prefixUnaryExpression
        self.parenthesizedAssignableExpression=parenthesizedAssignableExpression
    def accept(self,visitor):
        visitor.visitassignableExpression(self)
class parenthesizedAssignableExpression(assignableExpression):
    def __init__(self, LPAREN, assignableExpression, RPAREN):
        self.LPAREN=LPAREN
        self.assignableExpression=assignableExpression
        self.RPAREN= RPAREN
    def accept(self, visitor):
        visitor.visitparenthesizedAssignableExpression(self)
class assignableSuffix(directlyAssignableExpression):
    def __init__(self,typeArguments, indexingSuffix, navigationSuffix):
        self.typeArguments=typeArguments
        self.indexingSuffix=indexingSuffix
        self.navigationSuffix=navigationSuffix
    def accept(self, visitor):
        visitor.visitassignableSuffix(self)
class indexingSuffix(KotlinFile):
    def __init__(self,LCCT, isuf, RCCT):
        self.LCCT=LCCT
        self.isuf=isuf
        self.RCCT=RCCT
    def accept(self,visitor):
        visitor.visitindexingSuffix(self)
class isuf(indexingSuffix):
    def __init__(self,expression, COMMA, isuf ):
        self.expression=expression
        self.COMMA=COMMA
        self.isuf=isuf
    def accept(self,visitor):
        visitor.visitisuf(self)
class navigationSuffix(KotlinFile):
    def __init__(self, memberAccessOperator, simpleIdentifier, CLASS,parenthesizedExpression): 
        self.memberAccessOperator=memberAccessOperator
        self.simpleIdentifier=simpleIdentifier
        self.CLASS=CLASS
        self.parenthesizedExpression=parenthesizedExpression
    def accept(self, visitor):
        visitor.vistnavigationSuffix(self)
class callSuffix(KotlinFile):
    def __init__(self,typeArguments, valueArguments, annotatedLambda):
        self.typeArguments=typeArguments
        self.valueArguments=valueArguments
        self.annotatedLambda=annotatedLambda
    def accept(self,visitor):
        visitor.visitcallSuffix(self) 
class annotatedLambda(KotlinFile):
    def __init__(self,lambdaLiteral):
        self.lambdaLiteral=lambdaLiteral
    def accept(self,visitor):
        visitor.visitannotatedLambda(self)
class typeArguments(KotlinFile):
    def __init__(self,MENOR ,ta, MAIOR):
        self.MENOR=MENOR
        self.ta=ta
        self.MAIOR=MAIOR
    def accept(self,visitor):
        visitor.visittypeArguments(self)
class ta(typeArguments):
    def __init_(self,typeProjection, COMMA, ta, null):
        self.typeProjection=typeProjection
        self.COMMA=COMMA
        self.ta=ta
        self.null=null
    def accept (self, visitor):
        visitor.visitta(self)
class valueArguments(KotlinFile):
    def __init__(self,LPAREN, vas, RPAREN):
        self.LPAREN=LPAREN
        self.vas=vas
        self.RPAREN=RPAREN
    def accept(self, visitor):
        visitor.visitvalueArguments(self)
class vas(valueArguments):
    def __init__(self,valueArgument ,COMMA, vas):
        self.valueArgument=valueArgument
        self.COMMA=COMMA
        self.vas=vas
    def accept(self,visitor):
        visitor.visitvas(self)
class valueArgument(vas):
    def __init__(self,annotation, simpleIdentifier, IGUALDADE, MULT, expression):
        self.annotation=annotation
        self.simpleIdentifier=simpleIdentifier
        self.IGUALDADE=IGUALDADE
        self.MULT=MULT
        self.expression=expression
    def accept(self,visitor):
        visitor.visitvalueArgument(self)

class primaryExpression(KotlinFile):
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
class parenthesizedExpression(KotlinFile):
    def __init__(self,LPAREN ,expression, RPAREN):
        self.LPAREN=LPAREN
        self.expression=expression
        self.RPAREN=RPAREN
    def accept(self,visitor):
        visitor.visitparenthesizedExpression(self)
class collectionLiteral(KotlinFile):
    def __init__(self,LCCT, cl, RCCT):
        self.LCCT=LCCT
        self.cl=cl
        self.RCCT=RCCT
    def accept (self, visitor):
        visitor.visitcollectionLiteral(self)
class cl(collectionLiteral):
    def __init__(self,expression, COMMA, cl):
        self.expression=expression
        self.COMMA=COMMA
        self.cl=cl
    def accept(self,visitor):
        visitor.visitcl(self)
class literalConstant(KotlinFile):
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
class stringLiteral(KotlinFile):
    def __init__(self,lineStringLiteral,multiLineStringLiteral):
        self.lineStringLiteral=lineStringLiteral
        self.multiLineStringLiteral=multiLineStringLiteral
    def accept (self, visitor):
        visitor.visitstringLiteral(self)
class lambdaLiteral(KotlinFile):
    def _init__(self,RCHAVE, ll ,LCHAVE):
        self.RCHAVE=RCHAVE
        self.ll=ll
        self.LCHAVE=LCHAVE
    def accept (self,visitor):
        visitor.visitlambdaLiteral(self)
class ll(lambdaLiteral):
    def __init__(self,lambdaParameters, SETA, statements):
        self.lambdaParameters=lambdaParameters
        self.SETA=SETA
        self.statements=statements
    def accept(self,visitor):
        visitor.visitll(self)
class lambdaParameters(KotlinFile):
    def __init__(self,lambdaParameter, COMMA, lambdaParameters):
        self.lambdaParameter=lambdaParameter
        self.COMMA=COMMA
        self.lambdaParameters=lambdaParameters
    def accept(self,  visitor):
        visitor.visitlambdaParameters(self)
class lambdaParameter(lambdaParameters):
    def __init__(self,variableDeclaration,multiVariableDeclaration, DOISP ,type):
        self.variableDeclaration=variableDeclaration
        self.multiVariableDeclaration=multiVariableDeclaration
        self.DOISP= DOISP
        self.type=type
    def accept(self,visitor):
        visitor.visitlambdaParameter(self)
class anonymousFunction(KotlinFile):
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
     def __init__(self,type, PONTO,null):
         self.PONTO=PONTO
         self.null=null
         self.type=type
     def accept(self, visitor):
         visitor.visitaf4(self)
class functionLiteral(lambdaLiteral,anonymousFunction):
    def __init__(self,lambdaLiteral,anonymousFunction):
        self.lambdaLiteral=lambdaLiteral
        self.anonymousFunction=anonymousFunction
    def accept(self,visitor):
        visitor.visitfunctionLiteral(self)
class ifExpression(KotlinFile):
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
class jumpExpression(KotlinFile):
    def __init__(self,THROW,RETURN, expression, RETURN_AT, CONTINUE,CONTINUE_AT,BREAK,BREAK_AT):
        self.THROW=THROW
        self.RETURN=RETURN
        self.expression=expression
        self.RETURN_AT=RETURN_AT
        self.CONTINUE=CONTINUE
        self.CONTINUE_AT=CONTINUE_AT
        self.BREAK=BREAK
        self.BREAK_AT=BREAK_AT
    def accept(self,visitor):
        visitor.visitjumpExpression(self)
class callableReference(KotlinFile):
    def __init__(self,receiverType, DOISP, simpleIdentifier ):
        self.receiverType=receiverType
        self.DOISP=DOISP
        self.simpleIdentifier=simpleIdentifier
    def accept (self,visitor):
        visitor.visitcallableReference(self)
class assignmentAndOperator(KotlinFile):
    def __init__(self,MAISIGUAL, MENOSIGUAL, MULTIGUAL, DIVIGUAL,MODIGUAL):
        self.MAISIGUAL=MAISIGUAL
        self.MENOSIGUAL=MENOSIGUAL
        self.MULTIGUAL=MULTIGUAL
        self.DIVIGUAL=DIVIGUAL
        self.MODIGUAL=MODIGUAL
    def accept(self,visitor):
        visitor.visitassignmentAndOperator(self)
class equalityOperator(KotlinFile):
    def __init__(self,DIFERENTE,IDENTIDADE,IGUALDADE, SEMIDENTIDADE):
        self.DIFERENTE=DIFERENTE
        self.IDENTIDADE=IDENTIDADE
        self.IGUALDADE=IGUALDADE
        self.SEMIDENTIDADE=SEMIDENTIDADE
    def accept(self, visitor):
        visitor.visitequalityOperator(self)
class comparisonOperator(KotlinFile):
    def __init__(self,MENOR, MAIOR, MENORIGUAL,MAIORIGUAL):
        self.MENOR=MENOR
        self.MAIOR=MAIOR
        self.MENORIGUAL=MENORIGUAL
        self.MAIORIGUAL=MAIORIGUAL
    def accept(self, visitor):
        visitor.visitcomparisonOperator(self)
class inOperator(KotlinFile):
    def __init__(self,IN, NOT_IN):
        self.IN=IN
        self.NOT_IN=NOT_IN
    def accept(self,visitor):
        visitor.visitinOperator(self)
class isOperator(KotlinFile):
    def __init__(self,IS, NOT_IS): 
        self.IS=IS
        self.NOT_IS=NOT_IS
    def accept(self, visitor):
        visitor.visitisOperator(self)       
class additiveOperator(KotlinFile):
    def __init__(self,PLUS,MINUS):
        self.PLUS=PLUS
        self.MINUS=MINUS
    def accept (self, visitor):
        visitor.visitadditiveOperator(self)
class multiplicativeOperator(KotlinFile):
    def __init__(self,MULT,DIVIDE,MOD):
        self.MULT=MULT
        self.DIVIDE=DIVIDE
        self.MOD=MOD
    def accept(self.visitor):
        visitor.visitmultiplicativeOperator(self)
class asOperator(KotlinFile):
    def __init__(self,AS, asOperator):
        self.AS=AS
        self.asOperator=asOperator
    def accept(self, visitor):
        visitor.visitasOperator(self)
class prefixUnaryOperator(KotlinFile):
    def __init__(self,INCREMENTO,DECREMENTO, MINUS,PLUS,excl):
        self.INCREMENTO=INCREMENTO
        self.DECREMENTO=DECREMENTO
        self.MINUS=MINUS
        self.PLUS=PLUS
        self.excl=excl
    def accept(self, visitor):
        visitor.visitprefixUnaryOperator(self)
class memberAccessOperator(KotlinFile):
    def __init__(self,PONTO,safeNav, COLONCOLON ):
        self.PONTO=PONTO
        self.safeNav=safeNav
        self.COLONCOLON=COLONCOLON
    def accept(self, visitor):
        visitor,visitmemberAccessOperator(self)
class safeNav(memberAccessOperator):
    def __init__(self,PONTO ):
        self.PONTO=PONTO 
    def accept(self,visitor):
        visitor.visitsafeNav(self)







        












































