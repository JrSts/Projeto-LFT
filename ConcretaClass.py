import AbstrataClass as ac

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
        Visitor.visitCallExp(self)
        
class AssignExp():
    def __init__(self,assign):
        self.assign = assign
    def accept(self, Visitor):
        Visitor.visitAssignExp(self)

class NumExp():
    def __init__(self, num):
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
class SimpleKotlinFile(ac.KotlinFile):
    def __init__(self, functionDeclaration):
        self.functionDeclaration = functionDeclaration
    def accept(self, Visitor):
        Visitor.visitSimpleKotlinFile(self)

class CompoundKotlinFile(ac.KotlinFile):
    def __init__(self, functionDeclaration, kotlinFile):
        self.functionDeclaration = functionDeclaration
        self.kotlinFile = kotlinFile
    def accept(self, Visitor):
        Visitor.visitCompoundKotlinFile(self)
###########################################################
class SimpleFunctionDeclaration(ac.FunctionDeclaration):
    def __init__(self, simpleIdentifier, functionValueParameters, functionBody):
        self.simpleIdentifier = simpleIdentifier
        self.functionValueParameters = functionValueParameters
        self.functionBody = functionBody
    def accept(self, Visitor):
        Visitor.visitFuncrionDeclaration(self)

class CompoundFunctionDeclaration(ac.FunctionDeclaration):
    def __init__(self, simpleIdentifier, functionValueParameters, optionalType, functionBody):
        self.simpleIdentifier = simpleIdentifier
        self.functionValueParameters = functionValueParameters
        self.optionalType = optionalType
        self.functionBody = functionBody
    def accept(self, Visitor):
        Visitor.visitFuncrionDeclaration(self)

class OptionalType(ac.FunctionDeclaration, ac.ParameterWithOptionalType, ac.LambdaParameter, ac.AnonymousFunction):
    def __init__(self, type):
        self.type = type
    def accept(self, Visitor):
        Visitor.visitOptionalType(self)
###########################################################

class PropertyDeclarationConcrete(ac.PropertyDeclaration, ac.Statement):
    def __init__(self, varOrVal, optionalTypeParameters, MvOrV, expression, optionalPv):
        self.varOrVal = varOrVal
        self.MvOrV = MvOrV
        self.optionalTypeParameters = optionalTypeParameters
        self.optionalPv = optionalPv
        self.expression = expression
    def accept(self, Visitor):
        Visitor.visitPropertyDeclaration(self)

class MultiVariableDeclaration(ac.GenericVariableDeclaration):
    def __init__(self, multiVariableDeclaration):
        self.multiVariableDeclaration = multiVariableDeclaration
    def accept(self, Visitor):
        Visitor.visitMultiVariableDeclaration(self)

class VariableDeclaration(ac.GenericVariableDeclaration):
    def __init__(self, variableDeclaration):
        self.variableDeclaration = variableDeclaration
    def accept(self, Visitor):
        Visitor.visitVariableDeclaration(self)

class Var(ac.VarOrVal):
    def __init__(self, var):
        self.var = var
    def accept(self, Visitor):
        Visitor.visitVar(self)

class Val(ac.VarOrVal):
    def __init__(self, val):
        self.val = val
    def accept(self, Visitor):
        Visitor.visitVal(self)

class OptionalTypeParameters(ac.PropertyDeclaration):
    def __init__(self, typeParameters):
        self.typeParameters = typeParameters
    def accept(self, Visitor):
        Visitor.visitOptionalTypeParameters(self)

class OptionalPv(ac.PropertyDeclaration):
    def __init__(self, pv):
        self.pv = pv
    def accept(self, Visitor):
        Visitor.visitOptionalPv(self)

###########################################################
class TypeParametersConcrete(ac.TypeParameters):
    def __init__(self, typeParameter, typeParametersRecursive, optionalCOMMA):
        self.typeParameter = typeParameter
        self.typeParametersRecursive = typeParametersRecursive
        self.optionalCOMMA = optionalCOMMA
    def accept(self, Visitor):
        Visitor.visitTypePatameters(self)

class SimpleTypeParametersRecursive(ac.TypeParameters):
    def __init__(self, typeParameter):
        self.typeParameter = typeParameter
    def accept(self, Visitor):
        Visitor.visitSimpleTypeParameterRecursive(self)

class CompoundTypeParametersRecursive(ac.TypeParameters):
    def __init__(self, typeParameter, typeParametersRecursive):
        self.typeParameter = typeParameter
        self.typeParametersRecursive = typeParametersRecursive
    def accept(self, Visitor):
        Visitor.visitCompoundTypeParametersRecursive(self)
 
class OptionalCOMMA(ac.TypeParameters):
    def __init__(self, COMMA):
        self.COMMA = COMMA
    def accept(self, Visitor):
        Visitor.visitOptionalCOMMA(self)
##################################################################
class SimpleTypeParameter(ac.TypeParameters):
    def __init__(self, simpleIdentifier):
        self.simpleIdentifier = simpleIdentifier
    def accept(self, Visitor):
        Visitor.visitSimpleTypePatameter(self)

class CompoundTypeParameter(ac.TypeParameters):
    def __init__(self, simpleIdentifier, type):
        self.type = type
        self.simpleIdentifier = simpleIdentifier
    def accept(self, Visitor):
        Visitor.visitCompoundTypePatameter(self)
###########################################################
class SimpleFunctionBody(ac.FunctionDeclaration):
    def __init__(self, block):
        self.block = block
    def accept(self, Visitor):
        Visitor.visitSimpleFunctionBody(self)

class CompoundFunctionBody(ac.FunctionDeclaration):
    def __init__(self, expression):
        self.expression = expression
    def accept(self, Visitor):
        Visitor.visitCompoundFunctionBody(self)
###########################################################
class SimpleFunctionValueParameters(ac.KotlinFile):
    def __init__(self):
       self
    def accept(self, Visitor):
        Visitor.visitSimpleFunctionValueParameters(self)

class CompoundFunctionValueParameters(ac.KotlinFile):
    def __init__(self, fvps):
       self.fvps=fvps
    def accept(self, Visitor):
        Visitor.visitCompoundFunctionValueParameters(self)
################################################################
class SimpleFunctionValueParametersRecursive(ac.FunctionValueParametersRecursive):
    def __init__(self, fvp, optionalCOMMA):
        self.fvp=fvp
        self.optionalCOMMA = optionalCOMMA
    def accept(self, Visitor):
        Visitor.visitSimpleFunctionValueParametersRecursive(self)

class CompoundFunctionValueParametersRecursive(ac.FunctionValueParametersRecursive):
    def __init__(self, fvp, functionValueParametersRecursive):
        self.fvp = fvp 
        self.functionValueParametersRecursive = functionValueParametersRecursive
    def accept(self, Visitor):
        Visitor.visitCompoundFunctionValueParametersRecursive(self)
###################################################################
class SimpleFunctionValueParameter(ac.FunctionValueParameter):
    def __init__(self, parameter):
        self.parameter = parameter
    def accept(self,Visitor):
        Visitor.visitSimpleFunctionValueParameter(self)
        
class CompoundFunctionValueParameter(ac.FunctionValueParameter):
    def __init__(self, parameter, exp):
        self.parameter=parameter
        self.exp=exp
    def accept(self,Visitor):
        Visitor.visitCompoundFunctionValueParameter(self)
#################################################################
class SimpleMultiVariableDeclaration(ac.GenericVariableDeclaration):
    def __init__(self):
        self
    def accept(self, Visitor):
        Visitor.visitSimpleMultiVariableDeclaration(self)

class CompoundMultiVariableDeclaration(ac.GenericVariableDeclaration):
    def __init__(self, mvd):
        self.mvd=mvd
    def accept(self, Visitor):
        Visitor.visitCompoundMultiVariableDeclaration(self)
#####################################################################
class SimpleVariableDeclaration(ac.GenericVariableDeclaration):
    def __init__(self, simpleIdentifier):
        self.simpleIdentifier = simpleIdentifier
    def accept(self, Visitor):
        Visitor.visitSimpleVariableDeclaration(self)

class CompoundVariableDeclaration(ac.GenericVariableDeclaration):
    def __init__(self, simpleIdentifier, type):
        self.simpleIdentifier = simpleIdentifier
        self.type = type
    def accept(self, Visitor):
        Visitor.visitCompoundVariableDeclaration(self)
###################################################################
class SimpleMultiVariableDeclarationRecursive(ac.GenericVariableDeclaration):
    def __init__(self, variableDeclaration):
        self.variableDeclaration=variableDeclaration
    def accept(self, Visitor):
        Visitor.visitSimpleMultiVariableDeclarationRecursive(self)

class CompoundMultiVariableDeclarationRecursive(ac.GenericVariableDeclaration):
    def __init__(self, variableDeclaration, mvd):
        self.mvd = mvd
        self.variableDeclaration = variableDeclaration
    def accept(self, Visitor):
        Visitor.visitCompoundMultiVariableDeclarationRecursive(self)
####################################################################
class ParameterConcrete(ac.Parameter):
    def __init__(self, simpleIdentifier, type):
        self.simpleIdentifier = simpleIdentifier
        self.type = type
    def accept(self, Visitor):
        Visitor.visitParameter(self)
######################################################################
class TypeConcrete(ac.Type):
    def __init__(self,optionalTypeModifiers, optype):
        self.optionalTypeModifiers = optionalTypeModifiers
        self.optype = optype
    def accept(self, Visitor):
        Visitor.visitTypeConcrete(self)

class OptionalTypeModifiersConcrete(ac.Type):
    def __init__(self, typeModifiers):
        self.typeModifiers = typeModifiers
    def accept(self, Visitor):
        Visitor.visitOptionalTypeModifiersConcrete(self)
#######################################################################
# class OpTypeConcrete(ac.Type):
#     def __init__(self, typeModifiers):
#         self.typeModifiers = typeModifiers
#     def accept(self, Visitor):
#         Visitor.visitOpTypeConcrete(self)
#######################################################################
class ParenthesizedTypeConcrete(ac.OpType):
    def __init__(self, type):
        self.type = type
    def accept(self, Visitor):
        Visitor.visitParenthesizedType(self)

class FunctionType(ac.OpType):
    def __init__(self, functionType):
        self.functionType = functionType
    def accept(self, Visitor):
        Visitor.visitFunctionType(self)

class UserType(ac.OpType):
    def __init__(self,simpleUserType):
        self.simpleUserType = simpleUserType
    def accept(self, Visitor):
        Visitor.visitUserType(self)
#######################################################################
class SimpleTypeModifiers(ac.TypeModifiers):
    def __init__(self, typeModifier):
        self.typeModifier = typeModifier
    def accept(self, Visitor):
        Visitor.visitSimpleTypeModifiers(self)

class CompondTypeModifiers(ac.TypeModifiers):
    def __init__ (self, typeModifier, typeModifiers):
        self.typeModifier = typeModifier
        self.typeModifiers = typeModifiers
    def accept(self, Visitor):
        Visitor.visitCompoundTypeModifiers(self)
#########################################################################
class TypeModifierConcrete(ac.TypeModifier):
    def __init__ (self, suspend):
        self.suspend = suspend
    def accept(self, Visitor):
        Visitor.visitTypeModifierConcrete(self)
#########################################################################
class TypeProjectionModifierConcrete(ac.TypeProjectionModifier):
    def __init__(self, varianceModifier):
        self.varianceModifier = varianceModifier
    def accept(self, Visitor):
        Visitor.visitTypeProjectionModifierConcrete(self)
#########################################################################
class In(ac.VarianceModifier):
    def __init__(self, IN):
        self.IN = IN
    def accept(self, Visitor):
        Visitor.visitVariaceModifierIn(self)

class Out(ac.VarianceModifier):
    def __init__(self, out):
        self.out = out
    def accept(self, Visitor):
        Visitor.visitVariaceModifierOut(self)
########################################################################
# class SimpleUserTypeConcrete(ac.UserType):
#     def __init__(self):
#         self
#     def accept(self, Visitor):
#         Visitor.visitSimpleSimpleUserType(self)

class SimpleSimpleUserType(ac.UserType):
    def __init__(self, simpleIdentifier):
        self.simpleIdentifier = simpleIdentifier
    def accept(self, Visitor):
        Visitor.visitSimpleSimpleUserType(self)

class CompoundSimpleUserType(ac.UserType):
    def __init__(self, simpleIdentifier, typeArguments):
        self.simpleIdentifier = simpleIdentifier
        self.typeArguments = typeArguments
    def accept(self, Visitor):
        Visitor.visitCompoundSimpleUserType(self)
##########################################################################
class SimpleTypeProjection(ac.TypeProjection):
    def __init__(self, type):
        self.type=type
    def accept(self,Visitor):
        Visitor.visittypeSimpleProjection(self)

class CompoundTypeProjection(ac.TypeProjection):
    def __init__(self, typeProjectionModifiers, type):
        self.typeProjectionModifiers= typeProjectionModifiers
        self.type=type
    def accept(self,Visitor):
        Visitor.visitCompoundTypeProjection(self)
########################################################################
class SimpleTypeProjectionModifiers(CompoundTypeProjection, SimpleTypeProjection):
    def __init__(self, typeProjection):
        self.typeProjection=typeProjection
    def accept(self, Visitor):
        Visitor.visitSimpleTypeProjectionModifiers(self)

class CompoundTypeProjectionModifiers(CompoundTypeProjection, SimpleTypeProjection):
    def __init__(self, typeProjectionModifier, typeProjectionModifiers):
        self.typeProjectionModifier =typeProjectionModifier
        self.typeProjectionModifiers=typeProjectionModifiers
    def accept(self, Visitor):
        Visitor.visitCompoundTypeProjectionModifiers(self)
########################################################################
class SimpleFunctionType(ac.FunctionType):
    def __init__(self, functionTypeParameters, type):
        self.functionTypeParameters=functionTypeParameters
        self.type = type
    def accept(self, Visitor):
        Visitor.visitSimpleFunctionType(self)

class CompoundFunctionType(ac.FunctionType):
    def __init__(self, receiverType, functionTypeParameters, type):
        self.receiverType = receiverType
        self.functionTypeParameters = functionTypeParameters
        self.type = type
    def accept(self, Visitor):
        Visitor.visitCompoundFunctionType(self)
########################################################################

class FunctionTypeParametersConcrete(ac.FunctionTypeParametersConcrete):
    def __init__(self, optionalParameterOrType, parameterOrTypeRecursive, optionalCOMMA):
        self.optionalParameterOrType = optionalParameterOrType
        self.parameterOrTypeRecursive = parameterOrTypeRecursive
        self.optionalCOMMA = optionalCOMMA
    def accept(self, Visitor):
        Visitor.visitFunctionTypeParametersConcrete(self)

class SimpleParameterOrTypeRecursive(ac.ParameterOrTypeRecursive):
    def __init__(self, optionalParameterOrType):
        self.optionalParameterOrType = optionalParameterOrType
    def accept(self, Visitor):
        Visitor.visitSimpleParameterOrTypeRecursive(self)

class CompoundParameterOrTypeRecursive(ac.ParameterOrTypeRecursive):
    def __init__(self, optionalParameterOrType, parameterOrTypeRecursive):
        self.optionalParameterOrType = optionalParameterOrType
        self.parameterOrTypeRecursive = parameterOrTypeRecursive
    def accept(self, Visitor):
        Visitor.visitCompoundParameterOrTypeRecursive(self)
########################################################################
class ReceiverTypeConcrete(ac.ReceiverType):
    def __init__(self, typeModifier, parenthesizedType):
        self.typeModifier = typeModifier
        self.parenthesizedType = parenthesizedType
    def accept(self, Visitor):
        Visitor.visitReceiverTypeConcrete(self)
########################################################################
class SimpleStatements(ac.Statements):
    def __init__(self, statement):
        self.statement=statement
    def accept(self, Visitor):
        Visitor.visitSimpleStatemnts(self)

class CompoundStatements(ac.Statements):
    def __init__(self, statement, statments):
        self.statement=statement
        self.statments=statments
    def accept(self, Visitor):
        Visitor.visitCompoundStatemnts(self)
##########################################################################

class Assignment(ac.Statement):
    def __init__(self):
        self
    def accept(self, Visitor):
        Visitor.visitAssignment(self)

class LoopStatement(ac.Statement):
    def __init__(self):
        self
    def accept(self, Visitor):
        Visitor.visitLoopStatement(self)

class Expression(ac.Statement):
    def __init__(self):
        self
    def accept(self, Visitor):
        Visitor.visitExpression(self)
########################################################################
class Block(ac.ControlStructureBody):
    def __init__(self, statements):
        self.statements = statements
    def accept(self, Visitor):
        Visitor.visitBlock(self)

class StatementConcrete(ac.ControlStructureBody):
    def __init__(self):
        self
    def accept(self, Visitor):
        Visitor.visitBlock(self)
########################################################################

class SimpleForStatementConcrete(ac.LoopStatement):
    def __init__(self, genericVariableDeclaration, expression):
        self.genericVariableDeclaration = genericVariableDeclaration
        self.expression = expression
    def accept(self, Visitor):
        Visitor.visitSimpleForStatementConcrete(self)

class CompoundForStatementConcrete(ac.LoopStatement):
    def __init__(self, genericVariableDeclaration, expression, optionalControlStructureBody):
        self.genericVariableDeclaration = genericVariableDeclaration
        self.expression = expression
        self.optionalControlStructureBody = optionalControlStructureBody
    def accept(self, Visitor):
        Visitor.visitCompoundForStatementConcrete(self)

class WhileStatement_PV(ac.LoopStatement):
    def __init__(self, expression):
        self.expression = expression
    def accept(self, Visitor):
        Visitor.visitWhileStatement_PV(self)

class WhileStatement_CBS(ac.LoopStatement):
    def __init__(self, expression, controlStructureBody):
        self.expression = expression
        self.controlStructureBody = controlStructureBody
    def accept(self, Visitor):
        Visitor.visitWhileStatement_CBS(self)

########################################################################
class SimpleDoWhileStatement(ac.LoopStatement):
    def __init__(self, expression):
        self.expression=expression
    def accept(self, Visitor):
        Visitor.visitSimpleDoWhileStatement(self)

class CompoundDoWhileStatement(ac.LoopStatement):
    def __init__(self, controlStructureBody, expression):
        self.controlStructureBody=controlStructureBody
        self.expression=expression
    def accept(self, Visitor):
        Visitor.visitCompoundDoWhileStatement(self)
########################################################################
class SimpleChamadaDeFuncao(ac.ChamadaDeFuncao):
    def __init__(self, id):
        self.id = id
    def accept(self, Visitor):
        Visitor.visitSimpleChamadaDeFuncao(self)

class CompoundChamadaDeFuncao(ac.ChamadaDeFuncao):
    def __init__(self, id, parametersFunction):
        self.id = id
        self.parametersFunction = parametersFunction
    def accept(self, Visitor):
        Visitor.visitCompoundChamadaDeFuncao(self)

class SimpleParametersFunction(ac.ChamadaDeFuncao):
    def __init__(self, primaryExpression):
        self.primaryExpression = primaryExpression
    def accept(self, Visitor):
        Visitor.visitSimpleParametersFunction(self)

class CompoundParametersFunction(ac.ChamadaDeFuncao):
    def __init__(self, primaryExpression, parametersFunction):
        self.primaryExpression = primaryExpression
        self.parametersFunction = parametersFunction
    def accept(self, Visitor):
        Visitor.visitCompoundParametersFunction(self)
########################################################################
class AssignmentConcrete(ac.Assignment):
    def __init__(self,directlyAssignableExpression, expression):
        self.directlyAssignableExpression=directlyAssignableExpression
        self.expression=expression
    def accept(self, Visitor):
        Visitor.visitAssignmentConcrete(self)

class AssignmentAndOperatorConcrete(ac.AssignmentAndOperator):
    def __init__(self,assignmentAndOperator, assignableExpression ,expression): 
        self.assignmentAndOperator=assignmentAndOperator
        self.expression=expression
        self.assignableExpression = assignableExpression
    def accept(self, Visitor):
        Visitor.visitAssignmentAndOperatorConcrete(self)
########################################################################
class DisjunctionConcrete(ac.Disjunction):
    def __init__(self):
        self
    def accept (self,Visitor):
        Visitor.visitDisjunctionConcrete(self)
########################################################################
class SimpleDisjunction(ac.Disjunction):
    def __init__(self, conjunction):
        self.conjunction = conjunction
    def accept (self,Visitor):
        Visitor.visitSimpleDisjunction(self)
       
class CompoundDisjunction(ac.Disjunction):
    def __init__(self, conjunction, disjunction):
        self.conjunction=conjunction
        self.disjunction=disjunction
    def accept (self,Visitor):
        Visitor.visitCompoundDisjunction(self)
########################################################################
class SimpleConjunction(ac.Conjunction):
    def __init__(self,equality):
        self.equality=equality
    def accept (self,Visitor):
        Visitor.vistSimpleConjunction(self)

class CompoundConjunction(ac.Conjunction):
    def __init__(self, equality, conjunction):
        self.equality = equality
        self.conjunction = conjunction
    def accept(self, Visitor):
        Visitor.vistCompoundConjunction(self)
########################################################################
class SimpleEquality(ac.Conjunction):
    def __init__(self,comparison):
        self.comparison=comparison
    def accept(self,Visitor):
        Visitor.visitSimpleEquality(self)

class CompoundEquality(ac.Conjunction):
    def __init__(self,comparison, equalityOperator, equality):
        self.comparison=comparison
        self.equalityOperator=equalityOperator
        self.equality=equality
    def accept(self,Visitor):
        Visitor.visitCompoundEquality(self)
########################################################################
class SimpleComparison(ac.Equality):
    def __init__(self, infixOperation):
        self.infixOperation=infixOperation
    def accept (self,Visitor):
        Visitor.vistSimpleComparison(self)
    
class CompoundComparison(ac.Equality):
    def __init__(self, infixOperation, comparisonOperator):
        self.infixOperation=infixOperation
        self.comparisonOperator=comparisonOperator
    def accept (self,Visitor):
        Visitor.vistCompoundComparison(self)
########################################################################
class SimpleInfixOperation(ac.InfixOperation):
    def __init__(self,elvisExpression):
        self.elvisExpression=elvisExpression
    def accept (self,Visitor):
        Visitor.visitSimpleInfixOperation(self)
        
class CompoundInfixOperation(ac.InfixOperation):
    def __init__(self,elvisExpression, infixOperationRecursive):
        self.elvisExpression = elvisExpression
        self.infixOperationRecursive = infixOperationRecursive
    def accept (self,Visitor):
         Visitor.visitCompoundInfixOperation(self)
########################################################################

class SimpleInfixOperationRecursive(ac.InfixoperationRecursive):
    def __init__(self,inOrIs, elvisOrType):
        self.inOrIs = inOrIs
        self.elvisOrType = elvisOrType
    def accept (self,Visitor):
         Visitor.visitSimpleInfixOperationRecursive(self)

class CompoundInfixOperationRecursive(ac.InfixoperationRecursive):
    def __init__(self,inOrIs, elvisOrType, infixOperationRecursive):
        self.inOrIs = inOrIs
        self.elvisOrType = elvisOrType
        self.infixOperationRecursive = infixOperationRecursive
    def accept (self,Visitor):
         Visitor.visitCompoundInfixOperationRecursive(self)


class InOperator(ac.InOrIs):
    def __init__(self, In):
        self.In = In
    def accept(self, Visitor):
        Visitor.visitInOperator(self)

class IsOperator(ac.InOrIs):
    def __init__(self, Is):
        self.Is = Is
    def accept(self, Visitor):
        Visitor.visitIsOperator(self)

class ElvisExpressionConcrete(ac.ElvisOrType):
    def __init__(self, elvisExpression):
        self.elvisExpression = elvisExpression
    def accept(self, Visitor):
        Visitor.visitElvisExpressionConcrete(self)
########################################################################
class SimpleElvisExpression(ac.ElvisExpression):
    def __init__(self, infixFunctionCall):
        self.infixFunctionCall = infixFunctionCall
    def accept(self,Visitor):
        Visitor.visitSimpleElvisExpression(self)

class CompoundElvisExpression(ac.ElvisExpression):
    def __init__(self, infixFunctionCall, elvisExpression):
        self.infixFunctionCall = infixFunctionCall
        self.elvisExpression = elvisExpression
    def accept(self, Visitor):
        Visitor.visitCompoundElvisExpression(self)
########################################################################
class SimpleInfixFunctionCall(ac.InfixFunctionCall):
    def __init__(self, rangeExpression):
        self.rangeExpression = rangeExpression
    def accept (self,Visitor):
        Visitor.visitSimpleInfixFunctionCall(self)
        
class CompoundInfixFunctionCall(ac.InfixFunctionCall):
    def __init__(self,rangeExpression, simpleIdentifier, infixFunctionCall):
        self.rangeExpression = rangeExpression
        self.simpleIdentifier = simpleIdentifier
        self.infixFunctionCall = infixFunctionCall
    def accept (self,Visitor):
        Visitor.visitCompoundInfixFunctionCall(self)
########################################################################
class SimpleRangeExpression(ac.RageExpression):
    def __init__(self, additiveExpression):
        self.additiveExpression = additiveExpression
    def accept(self, Visitor):
        Visitor.visitSimpleRangeExpression(self)
    
class CompoundRangeExpression(ac.RageExpression):
    def __init__(self, additiveExpression, rangeExpression):
        self.additiveExpression = additiveExpression
        self.rangeExpression = rangeExpression
    def accept(self, Visitor):
        Visitor.visitCompoundRangeExpression(self)
########################################################################
class SimpleAdditiveExpression(ac.AdditiveExpression):
    def __init__(self,multiplicativeExpression):
        self.multiplicativeExpression = multiplicativeExpression
    def accept (self,Visitor):
        Visitor.visitSimpleAdditiveExpression(self)
    
class CompoundAdditiveExpression(ac.AdditiveExpression):
    def __init__(self,multiplicativeExpression ,additiveOperator, additiveExpression):
        self.multiplicativeExpression = multiplicativeExpression
        self.additiveOperator = additiveOperator
        self.additiveExpression = additiveExpression
    def accept (self,Visitor):
        Visitor.visitCompoundAdditiveExpression(self)
########################################################################
class SimpleMultiplicativeExpression(ac.MultiplicativeExpression):
    def __init__(self,asExpression):
        self.asExpression = asExpression
    def accept(self, Visitor):
        Visitor.visitSimpleMultiplicativeExpression(self)
        
class CompoundMultiplicativeExpression(ac.MultiplicativeExpression):
    def __init__(self,asExpression ,multiplicativeOperator, multiplicativeExpression):
        self.asExpression = asExpression
        self.multiplicativeOperator = multiplicativeOperator
        self.multiplicativeExpression = multiplicativeExpression
    def accept(self, Visitor):
        Visitor.visitCompoundMultiplicativeExpression(self)
########################################################################
        
class SimpleAsExpression(ac.AsExpression):
    def __init__(self, prefixUnaryExpression):
        self.prefixUnaryExpression = prefixUnaryExpression
    def accept (self, Visitor):
        Visitor.visitSimpleAsExpression(self)
        
class CompoundAsExpression(ac.AsExpression):
    def __init__(self,prefixUnaryExpression, asOperator, type):
        self.prefixUnaryExpression = prefixUnaryExpression
        self.asOperator = asOperator
        self.type = type
    def accept (self, Visitor):
        Visitor.visitCompoundAsExpression(self)
########################################################################
class SimplePrefixUnaryExpression(ac.PrefixUnaryExpression):
    def __init__(self, postfixUnaryExpression):
        self.postfixUnaryExpression = postfixUnaryExpression
    def accept(self,Visitor):
        Visitor.visitSimplePrefixUnaryExpression(self)

class CompoundPrefixUnaryExpression(ac.PrefixUnaryExpression):
    def __init__(self, prefixUnaryExpressionRecursive, postfixUnaryExpression):
        self.prefixUnaryExpressionRecursive = prefixUnaryExpressionRecursive
        self.postfixUnaryExpression = postfixUnaryExpression
    def accept(self,Visitor):
        Visitor.visitCompoundPrefixUnaryExpression(self)
########################################################################
class SimplePrefixUnaryExpressionRecursive(ac.PrefixUnaryExpressionRecursive):
    def __init__(self, unaryPrefix):
        self.unaryPrefix = unaryPrefix
    def accept(self, Visitor):
        Visitor.visitSimplePrefixUnaryExpressionRecursive(self)

class CompoundPrefixUnaryExpressionRecursive(ac.PrefixUnaryExpressionRecursive):
    def __init__(self, unaryPrefix, prefixUnaryExpressionRecursive):
        self.unaryPrefix = unaryPrefix
        self.prefixUnaryExpressionRecursive = prefixUnaryExpressionRecursive
    def accept(self, Visitor):
        Visitor.visitCompoundPrefixUnaryExpressionRecursive(self)
########################################################################
class PrefixUnaryOperatorConcrete(ac.UnaryPrefix):
    def __init__(self, prefixUnaryOperator):
        self.prefixUnaryOperator = prefixUnaryOperator
    def accept(self, Visitor):
        Visitor.visitPrefixUnaryOperatorConcrete(self)

class LabelConcrete(ac.UnaryPrefix):
    def __init__(self, label):
        self.label = label
    def accept(self, Visitor):
        Visitor.visitLabelConcrete(self)
########################################################################
class SimplePostfixUnaryExpression(ac.PostfixUnaryExpression):
    def __init__(self,primaryExpression):
        self.primaryExpression = primaryExpression
    def accept(self, Visitor):
        Visitor.visitSimplePostfixUnaryExpression(self)
   
class CompoundPostfixUnaryExpression(ac.PostfixUnaryExpression):
    def __init__(self,primaryExpression , postfixUnaryExpressionRecursive):
        self.primaryExpression = primaryExpression
        self.postfixUnaryExpressionRecursive = postfixUnaryExpressionRecursive
    def accept(self, Visitor):
        Visitor.visitCompoundPostfixUnaryExpression(self)
########################################################################
class SinglePostfixUnaryExpressionRecursive(SimplePostfixUnaryExpression):
    def __init__(self,postfixUnarySuffix):
        self.postfixUnarySuffix = postfixUnarySuffix
    def accept(self,Visitor):
        Visitor.visitSinglePostfixUnaryExpressionRecursive(self)
        
class CompoundPostfixUnaryExpressionRecursive(CompoundPostfixUnaryExpression):
    def __init__(self, postfixUnarySuffix, postfixUnaryExpression):
        self.postfixUnarySuffix = postfixUnarySuffix
        self.postfixUnaryExpression = postfixUnaryExpression
    def accept(self,Visitor):
        Visitor.visitCompoundPostfixUnaryExpressionRecursive(self)
########################################################################
class PostfixUnaryOperatorConcrete(ac.PostfixUnarySuffix):
    def __init__(self, postfixUnaryOperator):
        self.postfixUnaryOperator = postfixUnaryOperator
    def accept(self, Visitor):
        Visitor.visitPostfixUnaryOperatorConcrete(self)

class TypeArgumentsConcrete(ac.PostfixUnarySuffix):
    def __init__(self, typeArguments):
        self.typeArguments = typeArguments
    def accept(self, Visitor):
        Visitor.visitTypeArgumentsConcrete(self)

# class TypeArguments(ac.AssignableSuffix):
#     def __init__(self, typeArguments):
#         self.typeArguments = typeArguments
#     def accept(self, Visitor):
#         Visitor.visitTypeArguments(self)

class CallSuffixConcrete(ac.PostfixUnarySuffix):
    def __init__(self, callSuffix):
        self.callSuffix = callSuffix
    def accept(self, Visitor):
        Visitor.visitCallSuffixConcrete(self)

class IndexingSuffixConcrete(ac.PostfixUnarySuffix):
    def __init__(self, indexingSuffix):
        self.indexingSuffix = indexingSuffix
    def accept(self, Visitor):
        Visitor.visitIndexingSuffixConcrete(self)

#
# class IndexingSuffix(ac.AssignableSuffix):
#     def __init__(self, indexingSuffix):
#         self.indexingSuffix = indexingSuffix
#     def accept(self, Visitor):
#         Visitor.visitIndexingSuffix(self)

class NavigationSuffixConcrete(ac.PostfixUnarySuffix):
    def __init__(self, navigationSuffix):
        self.navigationSuffix = navigationSuffix
    def accept(self, Visitor):
        Visitor.visitNavigationSuffixConcrete(self)

# class NavigationSuffixConcrete(ac.AssignableSuffix):
#     def __init__(self, navigationSuffix):
#         self.navigationSuffix =navigationSuffix
#     def accept(self, Visitor):
#         Visitor.visitNavigationSuffix(self)
# ########################################################################
class Incremento(ac.PostfixUnaryOperator):
    def __init__(self, incremento):
        self.incremento = incremento
    def accept(self, Visitor):
        Visitor.visitIncremento(self)

class Decremento(ac.PostfixUnaryOperator):
    def __init__(self, decremento):
        self.decremento = decremento
    def accept(self, Visitor):
        Visitor.visitDecremento(self)
########################################################################
class SimpleTypeArguments(ac.TypeArguments):
    def __init__(self):
        self
    def accept(self, Visitor):
        Visitor.visitSimpleTypeArguments(self)

class Ta(ac.TypeArguments):
    def __init__(self, typePtojection, ta):
        self.ta = ta
        self.typePtojection = typePtojection
    def accept(self, Visitor):
        Visitor.visitTa(self)

class IndexingSuffix():
    def __init__(self, indexingSuffix):
        self.indexingSuffix =indexingSuffix
    def accept(self, Visitor):
        Visitor.visitIndexingSuffix(self)

class CallSuffix():
    def __init__(self, callSuffix):
        self.callSuffix =callSuffix
    def accept(self, Visitor):
        Visitor.visitCallSuffix(self)
########################################################################
class SimpleIdentifier(ac.DirectlyAssignableExpression):
    def __init__(self, simpleIdentifier):
        self.simpleIdentifier = simpleIdentifier
    def accept(self, Visitor):
        Visitor.visitSimpleIdentifier(self)

class ParenthesizedDirectlyAssignableExpression(ac.DirectlyAssignableExpression):
    def __init__(self, ParenthesizedDirectlyAssignableExpression):
        self.ParenthesizedDirectlyAssignableExpression = ParenthesizedDirectlyAssignableExpression
    def accept(self, Visitor):
        Visitor.visitParenthesizedDirectlyAssignableExpression(self)

class SimpleDirectlyAssignableExpression(ac.DirectlyAssignableExpression):
    def __init__(self,simpleIdentifier):
        self.simpleIdentifier=simpleIdentifier
    def accept(self, Visitor):
        Visitor.visitSimpleDirectlyAssignableExpression(self)
########################################################################
class ParenthesizedDirectlyAssignableExpressionConcrete(ac.ParenthesizedDirectlyAssignableExpression):
    def __init__(self, directlyAssignableExpression):
        self.directlyAssignableExpression = directlyAssignableExpression
    def accept(self, Visitor):
        Visitor.visitParenthesizedDirectlyAssignableExpressionConcrete(self)
########################################################################
class ParenthesizedAssignableExpressionConcrete(ac.AssignableExpression):
    def __init__(self, parenthesizedAssignableExpression):
        self.parenthesizedAssignableExpression = parenthesizedAssignableExpression
    def accept(self, Visitor):
        Visitor.visitParenthesizedAssignableExpressionConcrete(self)

class PrefixUnaryExpressionConcrete(ac.AssignableExpression):
    def __init__(self, prefixUnaryExpression):
        self.prefixUnaryExpression = prefixUnaryExpression
    def accept(self, Visitor):
        Visitor.visitPrefixUnaryExpressionConcrete(self)
########################################################################
class AssignableExpressionConcrete(ac.ParenthesizedAssignableExpression):
    def __init__(self, assignableExpression):
        self.assignableExpression = assignableExpression
    def accept(self, Visitor):
        Visitor.visitAssignableExpressionConcrete(self)
########################################################################
class SimpleIndexingSuffix(ac.IndexingSuffix):
    def __init__(self):
        self
    def accept(self,Visitor):
        Visitor.visitSimpleIndexingSuffix(self)       

class CompoundIndexingSuffix(ac.IndexingSuffix):
    def __init__(self,indexingSuffix):
        self.indexingSuffix = indexingSuffix
    def accept(self,Visitor):
        Visitor.visitCompoundIndexingSuffix(self)
########################################################################
class SimpleIndexingSuffixRecursive(ac.IndexingSuffixRecursive):
    def __init__(self,expression ):
        self.expression = expression
    def accept(self,Visitor):
        Visitor.visitSimpleIndexingSuffixRecursive(self)
        
class CompoundIndexingSuffixRecursive(ac.IndexingSuffixRecursive):
    def __init__(self, expression, indexingSuffix):
        self.expression=expression
        self.indexingSuffix = indexingSuffix
    def accept(self,Visitor):
        Visitor.visitCompoundIndexingSuffixRecursive(self)
########################################################################
# class ParenthesizedExpressionConcrete(ac.NavigationSuffix):
#     def __init__(self, expression):
#         self.expression=expression
#     def accept(self, Visitor):
#         Visitor.visitParenthesizedExpressionConcrete(self)

class ParenthesizedExpressionConcrete(ac.PrimaryExpression, ac.NavigationSuffix):
    def __init__(self, expression):
        self.expression = expression
    def accept(self, Visitor):
        Visitor.visitparenthesizedExpressionConcrete(self)
########################################################################

class SimpleCallSuffixConcrete(ac.CallSuffix):
    def  __init__(self, optionalTypeArguments, optionalValueArguments):
        self.optionalTypeArguments = optionalTypeArguments
        self.optionalValueArguments = optionalValueArguments
    def accept(self, Visitor):
        Visitor.visitSimpleCallSuffixConcrete(self)

class CompoundCallSuffixConcrete(ac.CallSuffix):
    def  __init__(self, optionalTypeArguments, optionalValueArguments, annotatedLambda):
        self.optionalTypeArguments = optionalTypeArguments
        self.optionalValueArguments = optionalValueArguments
        self.annotatedLambda = annotatedLambda
    def accept(self, Visitor):
        Visitor.visitCompoundCallSuffixConcrete(self)

class ValueArgumentsConcrete(ac.CallSuffix):
    def __init__(self, valueArguments):
        self.valueArguments = valueArguments
    def accept(self, Visitor):
        Visitor.visitValueArgumentsConcrete(self)

class TypeArgumentsConcrete(ac.CallSuffix):
    def __init__(self, typeArguments, valueArguments, annotatedLambda):
        self.typeArguments = typeArguments
        self.valueArguments = valueArguments
        self.annotatedLambda = annotatedLambda
    def accept(self, Visitor):
        Visitor.visitAnnotatedLambdaConcrete(self)
########################################################################
class LambdaLiteralConcrete(ac.AnnotatedLambda):
    def __init__(self, lambdaLiteral):
        self.lambdaLiteral = lambdaLiteral
    def accept(self,Visitor):
        Visitor.visitLambdaLiteralConcrete(self)
########################################################################
class SimpleTypeArguments(ac.TypeArguments):
    def __init__(self):
        self
    def accept(self,Visitor):
        Visitor.visitSimpleTypeArguments(self)

class CompoundTypeArguments(ac.TypeArguments):
    def __init__(self, typeArgumentsRecursive):
        self.typeArgumentsRecursive = typeArgumentsRecursive
    def accept(self,Visitor):
        Visitor.visitCompoundTypeArguments(self)
########################################################################
class SimpleTypeArgumentsRecursive(ac.TypeArgumentsRecursive):
    def __init__(self, typeProjection):
        self.typeProjection = typeProjection
    def accept (self, Visitor):
        Visitor.visitSimpleTypeArgumentsRecursive(self)
        
class CompoundTypeArgumentsRecursive(ac.TypeArgumentsRecursive):
    def __init__(self, typeProjection, typeArgumentsRecursive):
        self.typeProjection=typeProjection
        self.typeArgumentsRecursive = typeArgumentsRecursive
    def accept (self, Visitor):
        Visitor.visitCompoundCompoundTypeArgumentsRecursive(self)
########################################################################
class SimpleValueArguments(ac.ValueArguments):
    def __init__(self):
        self
    def accept(self, Visitor):
        Visitor.visitSimpleValueArguments(self)
        
class CompoundValueArguments(ac.ValueArguments):
    def __init__(self, vas):
        self.valueArgumentsRecursive = valueArgumentsRecursive
    def accept(self, Visitor):
        Visitor.visitCompoundValueArguments(self)
########################################################################
        
class SimpleValueArgumentsRecursive(ac.ValueArgumentsRecursive):
    def __init__(self,valueArgument):
        self.valueArgument = valueArgument
    def accept(self,Visitor):
        Visitor.visitSimpleValueArgumentsRecursive(self)
        
class CompoundValueArgumentsRecursive(ac.ValueArgumentsRecursive):
    def __init__(self, valueArgument, valueArgumentsRecursive):
        self.valueArgument = valueArgument
        self.valueArgumentsRecursive = valueArgumentsRecursive
    def accept(self,Visitor):
        Visitor.visitCompoundValueArgumentsRecursive(self)
########################################################################
class SimpleValueArgument(ac.ValueArgument):
    def __init__(self,simpleIdentifier):
        self.simpleIdentifier = simpleIdentifier
    def accept(self,Visitor):
        Visitor.visitSimpleValueArgument(self)
        
class Compound1ValueArgument(ac.ValueArgument):
    def __init__(self, simpleIdentifier, expression):
        self.simpleIdentifier=simpleIdentifier
        self.expression=expression
    def accept(self,Visitor):
        Visitor.visitCompound1ValueArgument(self)
        
class Compound2ValueArgument(ac.ValueArgument):
    def __init__(self, simpleIdentifier, expression):
        self.simpleIdentifier=simpleIdentifier
        self.expression=expression
    def accept(self,Visitor):
        Visitor.visitCompound2ValueArgument(self)
########################################################################
class LITERAL_STRINGConcrete(ac.PrimaryExpression):
    def __init__(self, LITERAL_STRING):
        self.LITERAL_STRING = LITERAL_STRING
    def accept(self, Visitor):
        Visitor.visitLITERAL_STRINGConcrete(self)

class CallableReferenceConcrete(ac.PrimaryExpression):
    def __init__(self, callableReference):
        self.callableReference = callableReference
    def accept(self, Visitor):
        Visitor.visitableReferenceConcrete(self)

class FunctionLiteralConcrete(ac.PrimaryExpression):
    def __init__(self, functionLiteral):
        self.functionLiteral = functionLiteral
    def accept(self, Visitor):
        Visitor.visitFunctionLiteralConcrete(self)

class CollectionLiteralConcrete(ac.PrimaryExpression):
    def __init__(self, collectionLiteral):
        self.collectionLiteral=collectionLiteral
    def accept(self, Visitor):
        Visitor.CollectionLiteralConcrete(self)

class IfExpressionConcrete(ac.PrimaryExpression):
    def __init__(self, ifExpression):
        self.ifExpression = ifExpression
    def accept(self, Visitor):
        Visitor.visitIfExpressionConcrete(self)
        
class JumpExpressionConcrete(ac.PrimaryExpression):
    def __init__(self, jumpExpression):
        self.jumpExpression = jumpExpression
    def accept(self, Visitor):
        Visitor.visitJumpExpressionConcrete(self)
########################################################################
class SimpleCollectionLiteral(ac.CollectionLiteral):
    def __init__(self):
        self
    def accept (self, Visitor):
        Visitor.visitSimpleCollectionLiteral(self)

class CompoundCollectionLiteral(ac.CollectionLiteral):
    def __init__(self, collectionLiteralRecursive):
        self.collectionLiteralRecursive=collectionLiteralRecursive
    def accept (self, Visitor):
        Visitor.visitCompoundCollectionLiteral(self)
########################################################################
class SimpleCollectionLiteralRecursive(ac.CollectionLiteralRecursive):
    def __init__(self,expression):
        self.expression=expression
    def accept(self,Visitor):
        Visitor.visitSimpleCollectionLiteralRecursive(self)

class CompoundCollectionLiteralRecursive(ac.CollectionLiteralRecursive):
    def __init__(self,expression, collectionLiteralRecursive):
        self.expression=expression
        self.collectionLiteralRecursive=collectionLiteralRecursive
    def accept(self,Visitor):
        Visitor.visitCompoundCollectionLiteralRecursive(self)
########################################################################
class SimpleParametersWithOptionalType(ac.ParametersWithOptionalType):
    def __init__(self):
        self
    def accept(self, Visitor):
        Visitor.visitSimpleParametersWithOptionalType(self)

class CompoundParametersWithOptionalType(ac.ParametersWithOptionalType):
    def __init__(self, parametersWithOptionalTypeRecursive):
        self.parametersWithOptionalTypeRecursive = parametersWithOptionalTypeRecursive
    def accept(self, Visitor):
        Visitor.visitCompoundParametersWithOptionalType(self)
########################################################################

class SimpleParametersWithOptionalTypeRecursive(ac.ParametersWithOptionalTypeRecursive):
    def __init__(self, parameterWithOptionalType):
        self.parameterWithOptionalType = parameterWithOptionalType
    def accept(self, Visitor):
        Visitor.visitSimpleParametersWithOptionalTypeRecursive(self)

class CompoundPwot(ac.ParametersWithOptionalTypeRecursive):
    def __init__(self, parameterWithOptionalType, parametersWithOptionalTypeRecursive):
        self.parameterWithOptionalType = parameterWithOptionalType
        self.parametersWithOptionalTypeRecursive = parametersWithOptionalTypeRecursive
    def accept(self, Visitor):
        Visitor.visitCompoundParametersWithOptionalTypeRecursive(self)
########################################################################
class ParameterWithOptionalTypeConcrete(ac.ParameterWithOptionalType):
    def __init__(self, optionalParameterModifiers, simpleIdentifier, optionalType):
        self.simpleIdentifier = simpleIdentifier
        self.optionalParameterModifiers = optionalParameterModifiers
        self.optionalType = optionalType
    def accept(self, Visitor):
        Visitor.visitParameterWithOptionalTypeConcrete(self)

class OptionalParameterModifiersConcrete(ac.OptionalParameterModifiers):
    def __init__(self, parameterModifiers):
        self.parameterModifiers = parameterModifiers
    def accept(self, Visitor):
        Visitor.visitOptionalParameterModifiersConcrete(self)
########################################################################
class VarargConcrete(ac.ParameterModifiers):
    def __init__(self):
        self
    def accept(self, Visitor):
        Visitor.visitVararg(self)

class NoinlineConcrete(ac.ParameterModifiers):
    def __init__(self):
        self
    def accept(self, Visitor):
        Visitor.visitNoinline(self)

class CrossinlineConcrete(ac.ParameterModifiers):
    def __init__(self):
        self
    def accept(self, Visitor):
        Visitor.visitCrossinline(self)
########################################################################
class LambdaLiteral(ac.LambdaLiteral):
    def _init__(self, optionsLambdaLiteral):
        self.optionsLambdaLiteral = optionsLambdaLiteral
    def accept (self,Visitor):
        Visitor.visitlambdaLiteral(self)
########################################################################
class SimpleOptionsLambdaLiteral(ac.OptionsLambdaLiteral):
    def __init__(self, statements):
        self.statements=statements
    def accept(self,Visitor):
        Visitor.visitSimpleOptionsLambdaLiteral(self)

class Compound1OptionsLambdaLiteral(ac.OptionsLambdaLiteral):
    def __init__(self, statements):
        self.statements=statements
    def accept(self,Visitor):
        Visitor.visitCompound1OptionsLambdaLiteral(self)

class Compound2OptionsLambdaLiteral(ac.OptionsLambdaLiteral):
    def __init__(self,lambdaParameters, statements):
        self.lambdaParameters=lambdaParameters
        self.statements=statements
    def accept(self,Visitor):
        Visitor.visitCompound2OptionsLambdaLiteral(self)
########################################################################
class SimpleLambdaParameters(ac.LambdaParameters):
    def __init__(self,lambdaParameter):
        self.lambdaParameter=lambdaParameter
    def accept(self,  Visitor):
        Visitor.visitSimpleLambdaParameters(self)

class CompoundLambdaParameters(ac.LambdaParameters):
    def __init__(self,lambdaParameter, lambdaParameters):
        self.lambdaParameter=lambdaParameter
        self.lambdaParameters=lambdaParameters
    def accept(self,  Visitor):
        Visitor.visitCompoundLambdaParameters(self)
########################################################################
class VariableDeclarationConcrete(ac.LambdaParameter):
    def __init__(self, multiVariableDeclaration):
        self.multiVariableDeclaration = multiVariableDeclaration
    def accept(self, Visitor):
        Visitor.visitVariableDeclaration(self)

class MultiVariableDeclarationConcrete(ac.LambdaParameter):
    def __init__(self, multiVariableDeclaration, optionalType):
        self.multiVariableDeclaration = multiVariableDeclaration
        self.optionalType = optionalType
    def accept(self,Visitor):
        Visitor.visitCompoundLambdaParameter(self)
########################################################################
class AnonymousFunctionConcrete(ac.AnonymousFunction):
    def __init__(self ,optionalTypePonto ,parametersWithOptionalType, optionalType ,optionalTypeConstraints, optionalFunctionBody):
        self.optionalTypePonto=optionalTypePonto
        self.parametersWithOptionalType=parametersWithOptionalType
        self.optionalType=optionalType
        self.optionalTypeConstraints=optionalTypeConstraints
        self.optionalFunctionBody=optionalFunctionBody
    def accept(self, Visitor):
        Visitor.visitAnonymousFunctionConcrete(self)

class OptionalTypePontoConcrete(ac.AnonymousFunction):
    def __init__(self, type):
         self.type = type
    def accept(self, Visitor):
        Visitor.visitOptionalTypePontoConcrete(self)

class OptionalTypeConstraintsConcrete(ac.AnonymousFunction):
    def __init__(self, typeConstraints):
         self.typeConstraints = typeConstraints
    def accept(self, Visitor):
        Visitor.visitOptionalTypeConstraintsConcrete(self)

class OptionalFunctionBodyConcrete(ac.AnonymousFunction):
    def __init__(self, functionBody):
        self.functionBody = functionBody
    def accept(self, Visitor):
        Visitor.visitOptionalFunctionBodyConcrete(self)
########################################################################
class TypeConstraintConcrete(ac.TypeConstraint):
    def __init__(self,simpleIdentifier, type):
        self.simpleIdentifier = simpleIdentifier
        self.type = type
    def accept(self,Visitor):
        Visitor.visitTypeConstraint(self)
########################################################################
class SimpleIfExpression(ac.IfExpression):
    def __init__(self, expression, controlStructureBodyOrPV):
        self.expression=expression
        self.controlStructureBodyOrPV=controlStructureBodyOrPV
    def accept(self, Visitor):
        Visitor.visitSimpleIfExpression(self)

class CompoundIfExpression(ac.IfExpression):
    def __init__(self, expression, optionalControlStructureBody, optionalPV, controlStructureBodyOrPV):
        self.expression = expression
        self.controlStructureBodyOrPV = controlStructureBodyOrPV
        self.optionalPV = optionalPV
        self.optionalControlStructureBody = optionalControlStructureBody
    def accept(self, Visitor):
        Visitor.visitCompoundIfExpression(self)

class PV(ac.IfExpression):
    def __init__(self, PV):
        self.PV = PV
    def accept(self, Visitor):
        Visitor.visitPV(self)

class ControlStructureBody(ac.IfExpression):
    def __init__(self, controlStructureBody):
        self.controlStructureBody = controlStructureBody
    def accept(self, Visitor):
        Visitor.visitControlStructureBody(self)
########################################################################
class ReturnConcrete(ac.JumpExpression):
    def __init__(self, expression):
        self.expression = expression
    def accept(self, Visitor):
        Visitor.visitReturnConcrete(self)

class ReturnAtConcrete(ac.JumpExpression):
    def __init__(self, expression):
        self.expression = expression
    def accept(self, Visitor):
        Visitor.visitReturnAtConcrete(self)

class ContinueConcrete(ac.JumpExpression):
    def __init__(self):
        self
    def accept(self, Visitor):
        Visitor.visitContinueConcrete(self)

class ContinueAtConcrete(ac.JumpExpression):
    def __init__(self):
        self
    def accept(self, Visitor):
        Visitor.visitContinueAtConcrete(self)

class BreakConcrete(ac.JumpExpression):
    def __init__(self):
        self
    def accept(self, Visitor):
        Visitor.visitBreakConcrete(self)

class BreakAtConcrete(ac.JumpExpression):
    def __init__(self):
        self
    def accept(self, Visitor):
        Visitor.visitBreakAtConcrete(self)
########################################################################
class CallableReferenceConcrete(ac.CallableReference):
    def __init__(self, optionalReceiverType, simpleIdentifierOrClass):
        self.optionalReceiverType = optionalReceiverType
        self.simpleIdentifierOrClass = simpleIdentifierOrClass
    def accept (self,Visitor):
        Visitor.visitCallableReferenceConcrete(self)

class OptionalReceiverType(ac.CallableReference):
    def __init__(self, receiverType):
        self.receiverType = receiverType
    def accept(self, Visitor):
        Visitor.visitOptionalReceiverType(self)

class ClassConcrete(ac.CallableReference):
    def __init__(self, CLASS):
        self.CLASS = CLASS
    def accept(self, Visitor):
        Visitor.visitClassConcrete(self)
########################################################################
class MAISIGUAL(ac.AssignmentAndOperator):
    def __init__(self, maisIgual):
        self.maisIgual = maisIgual
    def accept(self, Visitor):
        Visitor.visitMAISIGUAL(self)

class MENOSIGUAL(ac.AssignmentAndOperator):
    def __init__(self, menosIgual):
        self.menosIgual = menosIgual
    def accept(self, Visitor):
        Visitor.visitMENOSIGUAL(self)

class MULTIGUAL(ac.AssignmentAndOperator):
    def __init__(self, multiIgual):
        self.multiIgual = multiIgual
    def accept(self, Visitor):
        Visitor.visitMULTIGUAL(self)

class DIVIGUAL(ac.AssignmentAndOperator):
    def __init__(self, divIgual):
        self.divIgual = divIgual
    def accept(self, Visitor):
        Visitor.visitDIVIGUAL(self)

class MODIGUAL(ac.AssignmentAndOperator):
    def __init__(self, modIgual):
        self.modIgual = modIgual
    def accept(self, Visitor):
        Visitor.visitMODIGUAL(self)       
########################################################################
class Diferente(ac.EqualityOperator):
    def __init__(self, diferente):
        self.diferente = diferente
    def accept(self, Visitor):
        Visitor.visitDiferente(self)

class Identidade(ac.EqualityOperator):
    def __init__(self, identidade):
        self.identidade = identidade
    def accept(self, Visitor):
        Visitor.visitIdentidade(self)

class Igualdade(ac.EqualityOperator):
    def __init__(self, igualdade):
        self.igualdade = igualdade
    def accept(self, Visitor):
        Visitor.visitIgualdade(self)

class SemIdentidade(ac.EqualityOperator):
    def __init__(self, semIdentidade):
        self.semIdentidade = semIdentidade
    def accept(self, Visitor):
        Visitor.visitSemIdentidade(self)
########################################################################
class Menor(ac.ComparisonOperator):
    def __init__(self):
        self
    def accept(self, Visitor):
        Visitor.visitMenor(self)

class Maior(ac.ComparisonOperator):
    def __init__(self):
        self
    def accept(self, Visitor):
        Visitor.visitMAIOR(self)

class MenorIgual(ac.ComparisonOperator):
    def __init__(self):
        self
    def accept(self, Visitor):
        Visitor.visitMenorIgual(self)

class MaiorIgual(ac.ComparisonOperator):
    def __init__(self):
        self
    def accept(self, Visitor):
        Visitor.visitMaiorIgual(self)
########################################################################
class In(ac.InOperator):
    def __init__(self, In):
        self.In = In
    def accept(self, Visitor):
        Visitor.visitIn(self)

class NotIn(ac.InOperator):
    def __init__(self, notIn):
        self.notIn = notIn
    def accept(self, Visitor):
        Visitor.visitNotIn(self)
########################################################################
class NotIs(ac.IsOperator):
    def __init__(self, notIs):
        self.notIs = notIs
    def accept(self, Visitor):
        Visitor.visitNotIs(self)

class Is(ac.IsOperator):
    def __init__(self, Is):
        self.Is = Is
    def accept(self, Visitor):
        Visitor.visitIs(self)
########################################################################
class Plus(ac.AdditiveOperator):
    def __init__(self, plus):
        self.plus = plus
    def accept(self, Visitor):
        Visitor.visitPlus(self)

class Minus(ac.AdditiveOperator):
    def __init__(self, minus):
        self.minus = minus
    def accept(self, Visitor):
        Visitor.visitMINUS(self)
########################################################################
class Mult(ac.MultiplicativeOperator):
    def __init__(self, mult):
        self.mult = mult
    def accept(self, Visitor):
        Visitor.visitMult(self)

class Mod(ac.MultiplicativeOperator):
    def __init__(self, mod):
        self.mod = mod
    def accept(self, Visitor):
        Visitor.visitMod(self)

class Divide(ac.MultiplicativeOperator):
    def __init__(self, divide):
        self.divide = divide
    def accept(self, Visitor):
        Visitor.visitDivide(self)
########################################################################
class SimpleAsOperator(ac.AsOperator):
    def __init__(self):
        self
    def accept(self, Visitor):
        Visitor.visitSimpleAsOperator(self)

class CompoundAsOperator(ac.AsOperator):
    def __init__(self, asOperator):
        self.asOperator=asOperator
    def accept(self, Visitor):
        Visitor.visitCompoundAsOperator(self)
########################################################################
class Not(ac.PrefixUnaryOperator):
    def __init__(self, NOT):
        self.NOT = NOT
    def accept(self, Visitor):
        Visitor.visitNot(self)

class Incremento(ac.PrefixUnaryOperator):
    def __init__(self, incremento):
        self.incremento = incremento
    def accept(self, Visitor):
        Visitor.visitIncremento(self)
        
class Decremento(ac.PrefixUnaryOperator):
    def __init__(self, decremento):
        self.decremento = decremento
    def accept(self, Visitor):
        Visitor.visitDecremento(self)
########################################################################
class Ponto(ac.SafeNav):
    def __init__(self, ponto):
        self.ponto = ponto
    def accept(self, Visitor):
        Visitor.visitPonto(self)

class ColonColon(ac.MemberAccessOperator):
    def __init__(self, colonColon):
        self.colonColon = colonColon
    def accept(self, Visitor):
        Visitor.visitColonColon(self)

class SafeNavConcrete(ac.MemberAccessOperator):
    def __init__(self, safeNav):
        self.safeNav = safeNav
    def accept(self, Visitor):
        Visitor.visitSafeNavConcrete(self)
