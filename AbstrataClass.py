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
class functionDeclaration(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
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

class functionValueParameters(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
        pass
class fvps(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
        pass
class FunctionValueParametr(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
        pass
class variableDeclaration(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
        pass
class annot(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
        pass
class multiVariableDeclaration(metaclass=ABCMeta):
    @abstractmethod
    def accept(self,Visitor):
        pass
class mvd (metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class propertyDeclaration(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class parameter(metaclass= ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class  Compoundtype(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class SingleType(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass

class opType(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class userType(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class simpleUserType(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class typeProjection(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class typeProjectionModifiers(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class functionType(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
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
class parenthesizedUserType(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class statements (metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class statement (metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class controlStructureBody(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class block(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class  loopStatement(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class forStatement(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class whileStatement(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class doWhileStatement(metaclass=ABCMeta):
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
class assignableExpression(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class parenthesizedAssignableExpression(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class assignableSuffix(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class indexingSuffix(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class SimpleIsuf(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass 
class CompoundIsufIsuf(metaclass=ABCMeta):
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
class annotatedLambda(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass

class typeArguments(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class ta(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class valueArguments(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class vas(metaclass=ABCMeta):
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
class stringLiteral(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class lambdaLiteral(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass

class ll(metaclass=ABCMeta):
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
class asOperator(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class prefixUnaryOperator(metaclass=ABCMeta):
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













