from abc import abstractmethod
from abc import ABCMeta
import Visitor
from lex import tokens

class KotlinFile(metaclass=ABCMeta):

    @abstractmethod
    def accept(self, visitor):
        pass


class FunctionDeclaration(metaclass=ABCMeta):

    @abstractmethod
    def accept(self, visitor):
        pass


class FunctionValueParameters(metaclass=ABCMeta):

    @abstractmethod
    def accept(self, Visitor):
        pass


class Parameters(metaclass=ABCMeta):

    @abstractmethod
    def accept(self, Visitor):
        pass


class Parameter(metaclass=ABCMeta):

    @abstractmethod
    def accept(self, Visitor):
        pass



class Type(metaclass=ABCMeta):

    @abstractmethod
    def accept(self, Visitor):
        pass


class ParenthesizedType(metaclass=ABCMeta):

    @abstractmethod
    def accept(self, Visitor):
        pass


class FunctionBody(metaclass=ABCMeta):

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


class Open_statement(metaclass=ABCMeta):

    @abstractmethod
    def accept(self, Visitor):
        pass


class Closed_statement(metaclass=ABCMeta):

    @abstractmethod
    def accept(self, Visitor):
        pass


class Non_if_statement(metaclass=ABCMeta):

    @abstractmethod
    def accept(self, Visitor):
        pass


class Assignment(metaclass=ABCMeta):

    @abstractmethod
    def accept(self):
        pass



class Block(metaclass=ABCMeta):

    @abstractmethod
    def accept(self):
        pass


class PropertyDeclarationStm(metaclass=ABCMeta):

    @abstractmethod
    def accept(self, visitor):
        pass


class ChamadaDeFuncao(metaclass=ABCMeta):

    @abstractmethod
    def accept(self, Visitor):
        pass



class GenericVariableDeclaration(metaclass=ABCMeta):

    @abstractmethod
    def accept(self, Visitor):
        pass



class VariableDeclaration(metaclass=ABCMeta):

    @abstractmethod
    def accept(self, Visitor):
        pass


class VariableDeclarations(metaclass=ABCMeta):

    @abstractmethod
    def accept(self, Visitor):
        pass


class MultiVariableDeclaration(metaclass=ABCMeta):

    @abstractmethod
    def accept(self, Visitor):
        pass


class ParametersFunction(metaclass=ABCMeta):

    @abstractmethod
    def accept(self, Visitor):
        pass


class Expression(metaclass=ABCMeta):

    @abstractmethod
    def accept(self):
        pass



class Disjunction(metaclass=ABCMeta):

    @abstractmethod
    def accept(self):
        pass



class Conjunction(metaclass=ABCMeta):

    @abstractmethod
    def accept(self):
        pass



class Equality(metaclass=ABCMeta):

    @abstractmethod
    def accept(self):
        pass



class Comparison(metaclass=ABCMeta):

    @abstractmethod
    def accept(self):
        pass



class InfixOperation(metaclass=ABCMeta):

    @abstractmethod
    def accept(self):
        pass



class ElvisExpression(metaclass=ABCMeta):

    @abstractmethod
    def accept(self):
        pass



class RangeExpression(metaclass=ABCMeta):

    @abstractmethod
    def accept(self):
        pass


class AdditiveExpression(metaclass=ABCMeta):

    @abstractmethod
    def accept(self):
        pass



class MultiplicativeExpression(metaclass=ABCMeta):

    @abstractmethod
    def accept(self):
        pass



class AsExpression(metaclass=ABCMeta):

    @abstractmethod
    def accept(self):
        pass



class UnaryExpression(metaclass=ABCMeta):

    @abstractmethod
    def accept(self):
        pass



class PostfixUnaryOperator(metaclass=ABCMeta):

    @abstractmethod
    def accept(self, Visitor):
        pass



class PrimaryExpression(metaclass=ABCMeta):

    @abstractmethod
    def accept(self):
        pass


class JumpExpression(metaclass=ABCMeta):

    @abstractmethod
    def accept(self):
        pass


class ParenthesizedExpression(metaclass=ABCMeta):

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



class AsOperator(metaclass=ABCMeta):

    @abstractmethod
    def accept(self):
        pass


class UnaryOperator(metaclass=ABCMeta):

    @abstractmethod
    def accept(self):
        pass




#
# class Exp(metaclass=ABCMeta):
#     @abstractmethod
#     def accept(self, Visitor):
#         pass
#
# class Call(metaclass=ABCMeta):
#     @abstractmethod
#     def accept(self, visitor):
#         pass
#
# class Params(metaclass=ABCMeta):
#     @abstractmethod
#     def accept(self, visitor):
#         pass
#
# class Assign(metaclass=ABCMeta):
#      @abstractmethod
#      def accept(self, visitor):
#         pass
# #######################################################################
#
#
# class PropertyDeclarationPV(metaclass=ABCMeta):
#     @abstractmethod
#     def accept(self, visitor):
#         pass
# class TypeParameters(metaclass=ABCMeta):
#     @abstractmethod
#     def accept(self, visitor):
#         pass
# class TypeParamenter(metaclass=ABCMeta):
#     @abstractmethod
#     def accept(self, visitor):
#         pass
#
#
# class FunctionValueParametersRecursive(metaclass=ABCMeta):
#     @abstractmethod
#     def accept(self, Visitor):
#         pass
#
#
# class FunctionValueParameter(metaclass=ABCMeta):
#     @abstractmethod
#     def accept(self, Visitor):
#         pass
#
# class mvd(metaclass=ABCMeta):
#     @abstractmethod
#     def accept(self, Visitor):
#         pass
#
# class OpType(metaclass=ABCMeta):
#     @abstractmethod
#     def accept(self):
#         pass
# class TypeModifiers(metaclass=ABCMeta):
#     @abstractmethod
#     def accept(self, Visitor):
#         pass
# class TypeModifier(metaclass=ABCMeta):
#     @abstractmethod
#     def accept(self, Visitor):
#         pass
# class TypeProjectionModifier(metaclass=ABCMeta):
#     @abstractmethod
#     def accept(self, Visitor):
#         pass
# class VarianceModifier(metaclass=ABCMeta):
#     @abstractmethod
#     def accept(self, Visitor):
#         pass
# class UserType(metaclass=ABCMeta):
#     @abstractmethod
#     def accept(self, Visitor):
#         pass
# class SimpleUserType(metaclass=ABCMeta):
#     @abstractmethod
#     def accept(self, Visitor):
#         pass
# class TypeProjection(metaclass=ABCMeta):
#     @abstractmethod
#     def accept(self, Visitor):
#         pass
# class TypeProjectionModifiers(metaclass=ABCMeta):
#     @abstractmethod
#     def accept(self, Visitor):
#         pass
# class FunctionType(metaclass=ABCMeta):
#     @abstractmethod
#     def accept(self, Visitor):
#         pass
# class FunctionTypeParametersConcrete(metaclass=ABCMeta):
#     @abstractmethod
#     def accept(self, Visitor):
#         pass
# class InfixoperationRecursive(metaclass=ABCMeta):
#     @abstractmethod
#     def accept(self, Visitor):
#         pass
#
# class InOrIs(metaclass=ABCMeta):
#     @abstractmethod
#     def accept(self, Visitor):
#         pass
# class ElvisOrType(metaclass=ABCMeta):
#     @abstractmethod
#     def accept(self, Visitor):
#         pass
# class RageExpression(metaclass=ABCMeta):
#     @abstractmethod
#     def accept(self, Visitor):
#         pass
# class ControlStructureBody(metaclass=ABCMeta):
#     @abstractmethod
#     def accept(self, Visitor):
#         pass
# class ParameterOrTypeRecursive(metaclass=ABCMeta):
#     @abstractmethod
#     def accept(self, Visitor):
#         pass
# class PrefixUnaryExpressionRecursive(metaclass=ABCMeta):
#     @abstractmethod
#     def accept(self, Visitor):
#         pass
#
# class Label(metaclass=ABCMeta):
#     @abstractmethod
#     def accept(self, Visitor):
#         pass
# class OptionsLambdaLiteral(metaclass=ABCMeta):
#     @abstractmethod
#     def accept(self, Visitor):
#         pass
#
# class TypeArgumentsRecursive(metaclass=ABCMeta):
#     @abstractmethod
#     def accept(self, Visitor):
#         pass
# class ParenthesizedAssignableExpression(metaclass=ABCMeta):
#     @abstractmethod
#     def accept(self, Visitor):
#         pass
# class ParametersWithOptionalTypeRecursive(metaclass=ABCMeta):
#     @abstractmethod
#     def accept(self, Visitor):
#         pass
# class OptionalParameterModifiers(metaclass=ABCMeta):
#     @abstractmethod
#     def accept(self, Visitor):
#         pass
# class IndexingSuffixRecursive(metaclass=ABCMeta):
#     @abstractmethod
#     def accept(self, Visitor):
#         pass
# class ValueArgumentsRecursive(metaclass=ABCMeta):
#     @abstractmethod
#     def accept(self, Visitor):
#         pass
# class CollectionLiteralRecursive(metaclass=ABCMeta):
#     @abstractmethod
#     def accept(self, Visitor):
#         pass
#
# class ReceiverType(metaclass=ABCMeta):
#     @abstractmethod
#     def accept(self, Visitor):
#         pass
# class rt(metaclass=ABCMeta):
#     @abstractmethod
#     def accept(self, Visitor):
#         pass
#
# class controlStructureBody(metaclass=ABCMeta):
#     @abstractmethod
#     def accept(self, Visitor):
#         pass
#
# class LoopStatement(metaclass=ABCMeta):
#     @abstractmethod
#     def accept(self, Visitor):
#         pass
#
#
# class ForStatement_MD(metaclass=ABCMeta):
#     @abstractmethod
#     def accept(self, Visitor):
#         pass
# class ForStatement_VD(metaclass=ABCMeta):
#     @abstractmethod
#     def accept(self, Visitor):
#         pass
# class WhileStatement(metaclass=ABCMeta):
#     @abstractmethod
#     def accept(self):
#         pass
# class DoWhileStatement(metaclass=ABCMeta):
#     @abstractmethod
#     def accept(self):
#         pass
#
#
# class Io(metaclass=ABCMeta):
#     @abstractmethod
#     def accept(self):
#         pass
#
# class InfixFunctionCall(metaclass=ABCMeta):
#     @abstractmethod
#     def accept(self):
#         pass
#
#
# class Preue(metaclass=ABCMeta):
#     @abstractmethod
#     def accept(self):
#         pass
# class UnaryPrefix(metaclass=ABCMeta):
#     @abstractmethod
#     def accept(self):
#         pass
# class postfixUnaryExpression(metaclass=ABCMeta):
#     @abstractmethod
#     def accept(self):
#         pass
#
# class optionalTypePonto(metaclass=ABCMeta):
#     @abstractmethod
#     def accept(self):
#         pass
# class Posue(metaclass=ABCMeta):
#     @abstractmethod
#     def accept(self):
#         pass
# class VarOrVal(metaclass=ABCMeta):
#     @abstractmethod
#     def accept(self):
#         pass
# class PostfixUnarySuffix(metaclass=ABCMeta):
#     @abstractmethod
#     def accept(self):
#         pass
# class DirectlyAssignableExpression(metaclass=ABCMeta):
#     @abstractmethod
#     def accept(self):
#         pass
# class ParenthesizedDirectlyAssignableExpression(metaclass=ABCMeta):
#     @abstractmethod
#     def accept(self):
#         pass
# class AssignableExpression(metaclass=ABCMeta):
#     @abstractmethod
#     def accept(self, Visitor):
#         pass
# class parenthesizedAssignableExpression(metaclass=ABCMeta):
#     @abstractmethod
#     def accept(self):
#         pass
# class AssignableSuffix(metaclass=ABCMeta):
#     @abstractmethod
#     def accept(self, Visitor):
#         pass
# class IndexingSuffix(metaclass=ABCMeta):
#     @abstractmethod
#     def accept(self):
#         pass
# class Isuf(metaclass=ABCMeta):
#     @abstractmethod
#     def accept(self, Visitor):
#         pass
# class NavigationSuffix(metaclass=ABCMeta):
#     @abstractmethod
#     def accept(self):
#         pass
# class CallSuffix(metaclass=ABCMeta):
#     @abstractmethod
#     def accept(self):
#         pass
# class AnnotatedLambda(metaclass=ABCMeta):
#     @abstractmethod
#     def accept(self):
#         pass
# class TypeArguments(metaclass=ABCMeta):
#     @abstractmethod
#     def accept(self):
#         pass
# class Ta(metaclass=ABCMeta):
#     @abstractmethod
#     def accept(self):
#         pass
# class ValueArguments(metaclass=ABCMeta):
#     @abstractmethod
#     def accept(self):
#         pass
# class Vas(metaclass=ABCMeta):
#     @abstractmethod
#     def accept(self):
#         pass
# class ValueArgument(metaclass=ABCMeta):
#     @abstractmethod
#     def accept(self):
#         pass
#
#
# class CollectionLiteral(metaclass=ABCMeta):
#     @abstractmethod
#     def accept(self):
#         pass
# class cl(metaclass=ABCMeta):
#     @abstractmethod
#     def accept(self):
#         pass
# class ParametersWithOptionalType(metaclass=ABCMeta):
#     @abstractmethod
#     def accept(self, Visitor):
#         pass
# class Pwot(metaclass=ABCMeta):
#     @abstractmethod
#     def accept(self, Visitor):
#         pass
# class ParameterWithOptionalType(metaclass=ABCMeta):
#     @abstractmethod
#     def accept(self, Visitor):
#         pass
# class ParameterModifiers(metaclass=ABCMeta):
#     @abstractmethod
#     def accept(self, Visitor):
#         pass
# class LambdaLiteral(metaclass=ABCMeta):
#     @abstractmethod
#     def accept(self):
#         pass
# class Ll(metaclass=ABCMeta):
#     @abstractmethod
#     def accept(self):
#         pass
# class LambdaParameters(metaclass=ABCMeta):
#     @abstractmethod
#     def accept(self):
#         pass
# class LambdaParameter(metaclass=ABCMeta):
#     @abstractmethod
#     def accept(self):
#         pass
# class AnonymousFunction(metaclass=ABCMeta):
#     @abstractmethod
#     def accept(self):
#         pass
# class FunctionLiteral(metaclass=ABCMeta):
#     @abstractmethod
#     def accept(self):
#         pass
# class TypeConstraint(metaclass=ABCMeta):
#     @abstractmethod
#     def accept(self, Visitor):
#         pass
# class IfExpression(metaclass=ABCMeta):
#     @abstractmethod
#     def accept(self):
#         pass
#
# class CallableReference(metaclass=ABCMeta):
#     @abstractmethod
#     def accept(self):
#         pass
# class CallableReference_Class(metaclass=ABCMeta):
#     @abstractmethod
#     def accept(self):
#         pass
#
# class PrefixUnaryOperator(metaclass=ABCMeta):
#     @abstractmethod
#     def accept(self):
#         pass
# class PostfixUnaryOperator(metaclass=ABCMeta):
#     @abstractmethod
#     def accept(self):
#         pass
# class MemberAccessOperator(metaclass=ABCMeta):
#     @abstractmethod
#     def accept(self):
#         pass
# class SafeNav(metaclass=ABCMeta):
#     @abstractmethod
#     def accept(self):
#         pass
# class SimpleIdentifier(metaclass=ABCMeta):
#     @abstractmethod
#     def accept(self):
#         pass