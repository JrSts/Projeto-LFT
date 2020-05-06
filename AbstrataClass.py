from abc import abstractmethod
from abc import ABCMeta
import Visitor
from lex import tokens
class Exp(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
        pass

class Call(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class Params(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class Assign(metaclass=ABCMeta):
     @abstractmethod
     def accept(self, visitor):
        pass
################################

class kotlinFile(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class SimpleKotlinFile(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class CompoundKotlinFile(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class FunctionDeclaration(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class CompoundFunctionDeclaration(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass  
class SimpleFunctionDeclaration(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class SimpleFunctionBody(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
        pass
class CompoundFunctionBody(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
        pass 
class functionBody(metaclass=ABCMeta):
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
class functionValueParameter(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
        pass
class variableDeclaration(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
        pass
class multiVariableDeclaration(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
        pass
class mvd(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
        pass
class parameter(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
        pass  
class type(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
        pass 
class typeModifiers(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
        pass
class typeModifier(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
        pass
class typeProjectionModifier(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
        pass
class varianceModifier(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
        pass 
class userType(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
        pass 
class simpleUserType(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
        pass 
class typeProjection(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
        pass
class typeProjectionModifiers(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
        pass
class functionType(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
        pass
class functionTypeParameters_p(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
        pass
class functionTypeParameters_t(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
        pass
class ftp(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
        pass
class parenthesizedType(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
        pass
class receiverType(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
        pass
class rt(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
        pass
class Statements(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
        pass
class Statement(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
        pass

class LoopStatement(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
        pass
    
class controlStructureBody(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
        pass
class block(metaclass=ABCMeta):
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
class ParenthesizedType(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class FunctionType(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass 
class UserType(metaclass=ABCMeta):
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
class In(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class Out(metaclass=ABCMeta):
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
class simpleFunctionType(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class compoundFunctionType(metaclass=ABCMeta):
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
class Parameter(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass
class Type(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass
class parenthesizedType(metaclass= ABCMeta):
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
class FunctionDeclaration (metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class Assignment (metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass

class Expression(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class Statement (metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class Block(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class ForStatement_MD(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class ForStatement_VD(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class WhileStatement(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass

class DoWhileStatement(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class Annot(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
        pass
class PropertyDeclaration(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass

class MultiVariableDeclaration(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass

class VariableDeclaration(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass

class OpType(metaclass=ABCMeta):
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
class parenthesizedAssignableExpression(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class PrefixUnaryExpression(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class parenthesizedAssignableExpression(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class NavigationSuffix(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class TypeArguments(metaclass=ABCMeta):
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

class LoopStatement(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass

class IndexingSuffix(metaclass=ABCMeta):
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
class ParenthesizedExpression(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class ValueArguments1(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class ValueArguments2(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class ValueArguments3(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class AnnotatedLambda(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class AnnotatedLambda2(metaclass=ABCMeta):
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
class LITERAL_STRING(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class CallableReference(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass

class FunctionLiteral(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class CollectionLiteral(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class IfExpression(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class JumpExpression(metaclass=ABCMeta):
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
    
class CallableReference(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class AssignmentAndOperator(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class EqualityOperator(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class ComparisonOperator(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class InOperator(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class IsOperator(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class AdditiveOperator(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class MultiplicativeOperator(metaclass=ABCMeta):
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
class AsOperator(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class PrefixUnaryOperator(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class PostfixUnaryOperator(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class MemberAccessOperator(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class SafeNav(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass
class SimpleIdentifier(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass












