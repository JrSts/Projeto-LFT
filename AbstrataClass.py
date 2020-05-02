from abc import abstractmethod
from abc import ABCMeta
from Visitor import Visitor
from gramatica import *
class Exp(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
        pass

class Call(metaclass=ABCMeta):
    @abstractmethod
    def accept(self,Visitor):
        pass

class Params(metaclass=ABCMeta):
    @abstractmethod
    def accept(self,Visitor):
        pass

class Assign(metaclass=ABCMeta):
     @abstractmethod
     def accept(self,Visitor):
        pass
################################

class kotlinFile(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
        pass
class CompoundFunctionDeclaration(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
        pass
class SimpleFunctionDeclaration(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
        pass
class FunctionDeclaration(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
        pass
class SimpleFunctionBody(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
        pass
class CompoundFunctionBody(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
        pass  
class SimpleFunctionValueParameters(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
        pass
class CompoundFunctionValueParameters(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
        pass 
class SimpleFvps(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
        pass
class COMMAFvps(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
        pass
class CompoundFvps(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
        pass
class SimpleFunctionValeuParameter(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
        pass
class CompoundFunctionValeuParameter(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
        pass
class SimpleVariableDeclaration(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
        pass
class CompoundVariableDeclaration(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
        pass
class SimpleMultiVariableDeclaration(metaclass=ABCMeta):
    @abstractmethod
    def accept(self,Visitor):
        pass
class CompoundMultiVariableDeclaration(metaclass=ABCMeta):
    @abstractmethod
    def accept(self,Visitor):
        pass
class SimpleMvd (metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class CompoundMvd (metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class parameter(metaclass= ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class TypeParameters(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
        pass

class tps(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
        pass
class typeParameter(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
        pass
class  CompoundType(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class SingleType(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class CallParenthesizedType(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class CallFunctionType(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass 
class CallUserType(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass

class SimpleTypeModifiers(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class CompondTypeModifiers(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class TypeModifiers(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class typeProjectionModifiers(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class CallIn(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class CallOut(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass

class userType(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class SimpleSimpleUserType(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class CompoundSimpleUserType(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class SimpleTypeProjection(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class CompoundTypeProjection(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class SimpleTypeProjectionModifiers(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class CompoundTypeProjectionModifiers(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class SimpleFunctionType(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class CompoundFunctionType(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class SimpleFunctionTypeParameters_p(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class CompoundFunctionTypeParameters_p(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class SimpleFunctionTypeParameters_t(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class CompoundFunctionTypeParameters_t(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class CallParameter(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
        pass
class CallType(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
        pass
class parenthesizedType(metaclass= ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class receiverType(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class rt(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class SimpleStatements (metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class CompoundStatements (metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class CallFunctionDeclaration (metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class CallAssignment (metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class  CallLoopStatement(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class  CallExpression(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class Callblock(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class CallStatement (metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class block(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class CallForStatement_MD(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class CallForStatement_VD(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class CallWhileStatement(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class CallDoWhileStatement(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class annot(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
        pass
class propertyDeclaration(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class opType(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class simpleUserType(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class parenthesizedUserType(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class controlStructureBody(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class whileStatement(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass

class assignment(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class semi (metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass     
class expression(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass 
class disjunction(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class conjunction(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass

class equality(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class comparison(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class infixOperation(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class io(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class elvisExpression(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class infixFunctionCall(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass

class rangeExpression(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class additiveExpression(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class multiplicativeExpression(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class asExpression(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class prefixUnaryExpression(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class preue(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class unaryPrefix(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class postfixUnaryExpression(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class posue(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class postfixUnarySuffix(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass

class directlyAssignableExpression(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class parenthesizedDirectlyAssignableExpression(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class CallparenthesizedAssignableExpression(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class CallPrefixUnaryExpression(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class parenthesizedAssignableExpression(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class CallNavigationSuffix(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class CallTypeArguments(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class CallIndexingSuffix(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass

class SimpleIndexingSuffix(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class CompoundIndexingSuffix(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class SimpleIsuf(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass 
class CompoundIsuf(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass 
class navigationSuffix(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass 
class callSuffix(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass 
class CallParenthesizedExpression(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class CallValueArguments1(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class CallValueArguments2(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class CallValueArguments3(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class CallAnnotatedLambda(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class CallAnnotatedLambda2(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class annotatedLambda(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass

class SimpleTypeArguments(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class CompoundTypeArguments(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class SimpleTa(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class CompoundTa(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class SimpleValueArguments(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class CompoundValueArguments(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class SimpleVas(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class CompoundVas(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class valueArgument(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class primaryExpression(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class SimpleValueArgument(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class Compound1ValueArgument(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class Compound2ValueArgument(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class CallLITERAL_STRING(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class CallCallableReference(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass

class CallFunctionLiteral(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class CallCollectionLiteral(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class CallIfExpression(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class CallJumpExpression(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass

class parenthesizedExpression(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class CollectionLiteral(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class SimpleCollectionLiteral(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class CompoundCollectionLiteral(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class cl(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class SimpleCl(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class CompoundCl(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class literalConstant(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass

class SimpleParametersWithOptionalType(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class CompoundParametersWithOptionalType(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class SimplePwot(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class CompoundPwot(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class stringLiteral(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class lambdaLiteral(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class SimpleLl(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class Compound1Ll(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class Compound2Ll(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass

class ll(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class SimpleLambdaParameters(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class CompoundLambdaParameters(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass 
class lambdaParameters(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class lambdaParameter(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class anonymousFunction(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class af1(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass 
class af2(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass 
class af3(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass 
class af4(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass 
class functionLiteral(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class ifExpression(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class jumpExpression(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class SimpleCallableReference_SI(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass

class CompoundCallableReference_SI(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class SimpleCallableReference_Class(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class CompoundCallableReference_Class(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
    
class callableReference(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class assignmentAndOperator(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class equalityOperator(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class comparisonOperator(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class inOperator(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class isOperator(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class additiveOperator(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class multiplicativeOperator(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class SimpleAsOperator(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class CompoundAsOperator(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class asOperator(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class prefixUnaryOperator(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class PostfixUnaryOperator(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class memberAccessOperator(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class safeNav(metaclass=ABCMeta):
    @abstractmethod
    def accept(sel):
        pass













