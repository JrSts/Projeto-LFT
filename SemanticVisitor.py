from AbstractVisitor import AbstractVisitor
import SymbolTable as st
from Visitor import Visitor
from lex import lex
import ConcretaClass as co
import AbstrataClass as ac

def coercion(type1, type2):
    if (type1 in st.Number and type2 in st.Number):
        if (type1 == st.FLOAT or type2 == st.FLOAT):
            return st.FLOAT
        else:
            return st.INT
    else:
        return None

class SemanticVisitor(AbstractVisitor):

    def __init__(self):
        self.printer = Visitor()
        st.beginScope('Start')


    def visitCompoundKotlinFile(self,CompoundKotlinFile):
        CompoundKotlinFile.functionDeclaration.accept(self)
        CompoundKotlinFile.kotlinFile.accept(self)  


    def visitSimpleFunctionDeclaration(self, SimpleFunctionDeclaration):
        params = {}
        if SimpleFunctionDeclaration.functionValueParameters != None:
            params = SimpleFunctionDeclaration.functionValueParameters.accept(self)
            st.addFunction(SimpleFunctionDeclaration.id, params, None)
        else:
            st.addFunction(SimpleFunctionDeclaration.id, params, None)
        st.beginScope(SimpleFunctionDeclaration.id)

        for k in range(0, len(params), 2):
            st.addVar(params[k], params[k + 1])

        SimpleFunctionDeclaration.functionBody.accept(self)


    def visitCompoundFunctionDeclaration(self, CompoundFunctionDeclaration):
        params = {}
        if CompoundFunctionDeclaration.functionValueParameters != None:
            params = CompoundFunctionDeclaration.functionValueParameters.accept(self)
            st.addFunction(CompoundFunctionDeclaration.id, params, CompoundFunctionDeclaration.type)
        else:
            st.addFunction(CompoundFunctionDeclaration.id, params, CompoundFunctionDeclaration.type)

        for k in range(0, len(params), 2):
            st.addVar(params[k], params[k + 1])

        CompoundFunctionDeclaration.functionBody.accept(self)


    def visitSimpleFunctionValueParameters(self, SimpleFunctionValueParameters):
        SimpleFunctionValueParameters.accept(self)


    def visitCompoundFunctionValueParameters(self,CompoundFunctionValueParameters):
        CompoundFunctionValueParameters.parameters.accept(self)


    def visitCompoundParameters(self, CompoundParameters):
        return [CompoundParameters.id, CompoundParameters.type] + CompoundParameters.parameters.accept(self)


    def visitSimpleParameter(self, SimpleParameter):
        return [SimpleParameter.id, SimpleParameter.type]


    def visitParenthesizedTypeConcrete(self,ParenthesizedTypeConcrete):
        ParenthesizedTypeConcrete.type.accept(self)


    def visitCompoundFunctionBody(self, CompoundFunctionBody):
        CompoundFunctionBody.expression.accept(self)


    def visitCompoundStatements(self,CompoundStatements):
        CompoundStatements.statement.accept(self)
        CompoundStatements.statements.accept(self)


    def visitIf_statement(self, If_statement):
        if If_statement.expresison == bool:
            If_statement.statement.accept(self)
        else:
            If_statement.expresison.accept(self.printer)
            print("\n\t[ERRO] A expressao ",
                  If_statement.expresison.accept(self.printer),
                  ' eh ', type, ' Deveria ser boolean')


    def visitIf_block(self, If_block):
        if If_block.expresison == bool:
            If_block.block.accept(self)
        else:
            If_block.expresison.accept(self.printer)
            print("\n\t[ERRO] A expressao ",
                  If_block.expresison.accept(self.printer),
                  ' eh ', type, ' Deveria ser boolean')


    def visitSimpleIf_else(self, SimpleIf_else):
        if SimpleIf_else.expresison == bool:
            SimpleIf_else.block.accept(self)
            SimpleIf_else.open_statement.accept(self)
        else:
            SimpleIf_else.expresison.accept(self.printer)
            print("\n\t[ERRO] A expressao ",
                  SimpleIf_else.expresison.accept(self.printer),
                  ' eh ', type, ' Deveria ser boolean')


    def visitCompoundIf_else(self, CompoundIf_else):
        if CompoundIf_else.expresison == bool:
            CompoundIf_else.closed_statement.accept(self)
            CompoundIf_else.open_statement.accept(self)
        else:
            CompoundIf_else.expresison.accept(self.printer)
            print("\n\t[ERRO] A expressao ",
                  CompoundIf_else.expresison.accept(self.printer),
                  ' eh ', type, ' Deveria ser boolean')


    def visitWhile_Open_statement(self, While_Open_statement):
        if While_Open_statement.expresison == bool:
            While_Open_statement.open_statement.accept(self)
        else:
            While_Open_statement.expresison.accept(self.printer)
            print("\n\t[ERRO] A expressao ",
                  While_Open_statement.expresison.accept(self.printer),
                  ' eh ', type, ' Deveria ser boolean')


    def visitDoWhile_Open_statement(self, DoWhile_Open_statement):
        if DoWhile_Open_statement.expresison == bool:
            DoWhile_Open_statement.open_statement.accept(self)
        else:
            DoWhile_Open_statement.expresison.accept(self.printer)
            print("\n\t[ERRO] A expressao ",
                  DoWhile_Open_statement.expresison.accept(self.printer),
                  ' eh ', type, ' Deveria ser boolean')


    def visitFor_Open_statement(self, For_Open_statement):
        if For_Open_statement.expresison == bool:
            For_Open_statement.genericVariableDeclaration.accept(self)
            For_Open_statement.open_statement.accept(self)
        else:
            For_Open_statement.expresison.accept(self.printer)
            print("\n\t[ERRO] A expressao ",
                  For_Open_statement.expresison.accept(self.printer),
                  ' eh ', type, ' Deveria ser boolean')


    def visitIf_Blocks_Closed_statement(self, If_Blocks_Closed_statement):
        if If_Blocks_Closed_statement.expresison == bool:
            If_Blocks_Closed_statement.block.accept(self)
            If_Blocks_Closed_statement.block1.accept(self)
        else:
            If_Blocks_Closed_statement.expresison.accept(self.printer)
            print("\n\t[ERRO] A expressao ",
                  If_Blocks_Closed_statement.expresison.accept(self.printer),
                  ' eh ', type, ' Deveria ser boolean')


    def visitIf_Mix1_Closed_statement(self, If_Mix1_Closed_statement):
        if If_Mix1_Closed_statement.expresison == bool:
            If_Mix1_Closed_statement.block.accept(self)
            If_Mix1_Closed_statement.closed_statement.accept(self)
        else:
            If_Mix1_Closed_statement.expresison.accept(self.printer)
            print("\n\t[ERRO] A expressao ",
                  If_Mix1_Closed_statement.expresison.accept(self.printer),
                  ' eh ', type, ' Deveria ser boolean')


def visitIf_Mix2_Closed_statement(self, If_Mix2_Closed_statement):
    if If_Mix2_Closed_statement.expresison == bool:
        If_Mix2_Closed_statement.closed_statement.accept(self)
        If_Mix2_Closed_statement.block.accept(self)
    else:
        If_Mix2_Closed_statement.expresison.accept(self.printer)
        print("\n\t[ERRO] A expressao ",
              If_Mix2_Closed_statement.expresison.accept(self.printer),
              ' eh ', type, ' Deveria ser boolean')

def visitIf_Closeds_Closed_statement(self, If_Closeds_Closed_statement):
    if If_Closeds_Closed_statement.expresison == bool:
        If_Closeds_Closed_statement.closed_statement.accept(self)
        If_Closeds_Closed_statement.closed_statement.accept(self)
    else:
        If_Closeds_Closed_statement.expresison.accept(self.printer)
        print("\n\t[ERRO] A expressao ",
              If_Closeds_Closed_statement.expresison.accept(self.printer),
              ' eh ', type, ' Deveria ser boolean')


def visitFor_Closed_statement(self, For_Closed_statement):
    if For_Closed_statement.expresison == bool:
        For_Closed_statement.genericVariableDeclaration.accept(self)
        For_Closed_statement.closed_statement.accept(self)
    else:
        For_Closed_statement.expresison.accept(self.printer)
        print("\n\t[ERRO] A expressao ",
              For_Closed_statement.expresison.accept(self.printer),
              ' eh ', type, ' Deveria ser boolean')

def visitWhile_Closed_statement(self, While_Closed_statement):
    if While_Closed_statement.expresison == bool:
        While_Closed_statement.closed_statement.accept(self)
    else:
        While_Closed_statement.expresison.accept(self.printer)
        print("\n\t[ERRO] A expressao ",
              While_Closed_statement.expresison.accept(self.printer),
              ' eh ', type, ' Deveria ser boolean')


def visitDoWhile_Closed_statement(self, DoWhile_Closed_statement):
    if DoWhile_Closed_statement.expresison == bool:
        DoWhile_Closed_statement.closed_statement.accept(self)
    else:
        DoWhile_Closed_statement.expresison.accept(self.printer)
        print("\n\t[ERRO] A expressao ",
              DoWhile_Closed_statement.expresison.accept(self.printer),
              ' eh ', type, ' Deveria ser boolean')


def visitFor_Non_if_statement_block(self, For_Non_if_statement_block):
    if For_Non_if_statement_block.expresison == bool:
        For_Non_if_statement_block.genericVariableDeclaration.accept(self)
        For_Non_if_statement_block.block.accept(self)
    else:
        For_Non_if_statement_block.expresison.accept(self.printer)
        print("\n\t[ERRO] A expressao ",
              For_Non_if_statement_block.expresison.accept(self.printer),
              ' eh ', type, ' Deveria ser boolean')


def visitWhile_Non_if_statement_block(self, While_Non_if_statement_block):
    if While_Non_if_statement_block.expresison == bool:
        While_Non_if_statement_block.block.accept(self)
    else:
        While_Non_if_statement_block.expresison.accept(self.printer)
        print("\n\t[ERRO] A expressao ",
              While_Non_if_statement_block.expresison.accept(self.printer),
              ' eh ', type, ' Deveria ser boolean')


def visitDoWhile_Non_if_statement_block(self, DoWhile_Non_if_statement_block):
    if DoWhile_Non_if_statement_block.expresison == bool:
        DoWhile_Non_if_statement_block.block.accept(self)
    else:
        DoWhile_Non_if_statement_block.expresison.accept(self.printer)
        print("\n\t[ERRO] A expressao ",
              DoWhile_Non_if_statement_block.expresison.accept(self.printer),
              ' eh ', type, ' Deveria ser boolean')

def visitAssignmentConcrete(self, AssignmentConcrete):
    typeVar = AssignmentConcrete.expression.accept(self)
    if typeVar != None:
        st.addVar(AssignmentConcrete.id, typeVar)
        return typeVar
    return None

def visitAssignmentAndOperatorConcrete(self, AssignmentAndOperatorConcrete):
    typeVar = AssignmentAndOperatorConcrete.expression.accept(self)
    if typeVar != None:
        st.addVar(AssignmentAndOperatorConcrete.id, typeVar)
        return typeVar
    return None


def visitBlockConcrete(self, BlockConcrete):
    BlockConcrete.statements.accept(self)


def visitPropertyDeclarationStm_Var(self, PropertyDeclarationStm_Var):
    typeVar = PropertyDeclarationStm_Var.expression.accept(self)
    if typeVar != None:
        st.addVar(PropertyDeclarationStm_Var.id, typeVar)
        return typeVar
    return None


def visitPropertyDeclarationStm_Val(self, PropertyDeclarationStm_Val):
    typeVar = PropertyDeclarationStm_Val.expression.accept(self)
    if typeVar != None:
        st.addVar(PropertyDeclarationStm_Val.id, typeVar)
        return typeVar
    return None


def visitSimpleChamadaDeFuncao(self, SimpleChamadaDeFuncao):
    bindable = st.getBindable(SimpleChamadaDeFuncao.id)
    if bindable != None and bindable[st.BINDABLE] == [st.FUNCTION]:
        return bindable[st.TYPE]
    else:
        SimpleChamadaDeFuncao.accept(self.printer)
        print('\n\t[ERRO] Chamada de Funcao Invalida, ',
              SimpleChamadaDeFuncao.id, 'nao é uma funcao, '
                                        'nao foi definida,'
                                        'ou foi chamada antes de '
                                        'sua declaracao.')
    return None


def visitCompoundChamadaDeFuncao(self, CompoundChamadaDeFuncao):
    bindable = st.getBindable(CompoundChamadaDeFuncao.id)
    if bindable != None and bindable[st.BINDABLE] == [st.FUNCTION]:
        typeParams = CompoundChamadaDeFuncao.parametersFunction.accept(self)
        if list(bindable[st.PARAMS][1::2]) == typeParams:
            return bindable[st.TYPE]
        CompoundChamadaDeFuncao.accept(self.printer)
        print('\n\t[ERRO] Chamada de Funcao Invalida, ',
            CompoundChamadaDeFuncao.id, 'nao é uma funcao, '
                                        'nao foi definida,'
                                        'ou foi chamada antes de '
                                        'sua declaracao.')
    return None


def visitCompoundVariableDeclaration(self, CompoundVariableDeclaration):
    typeVar = CompoundVariableDeclaration.type
    if CompoundVariableDeclaration.id != None:
        st.addVar(CompoundVariableDeclaration.id, typeVar)
        return typeVar
    return None


def visitCompoundVariableDeclarations(self, CompoundVariableDeclarations):
    CompoundVariableDeclarations.variableDeclaration.accept(self)
    CompoundVariableDeclarations.variableDeclarations.accept(self)


def visitSimpleMultiVariableDeclaration(self, SimpleMultiVariableDeclaration):
    SimpleMultiVariableDeclaration.accept(self)


def visitCompoundMultiVariableDeclaration(self, CompoundMultiVariableDeclaration):
    CompoundMultiVariableDeclaration.variableDeclarations.accept(self)


def visitCompoundParametersFunction(self, CompoundParametersFunction):
    CompoundParametersFunction.primaryExpression.accept(self)
    CompoundParametersFunction.parametersFunction.accept(self)


def visitCompoundDisjunction(self, CompoundDisjunction):
    CompoundDisjunction.conjunction.accept(self)
    CompoundDisjunction.disjunction.accept(self)


def visitCompoundConjunction(self, CompoundConjunction):
    CompoundConjunction.equality.accept(self)
    CompoundConjunction.conjunction.accept(self)


def visitCompoundEquality(self, CompoundEquality):
    CompoundEquality.comparison.accept(self)
    CompoundEquality.equality.accept(self)


def visitCompoundComparison(self, CompoundComparison):
    CompoundComparison.infixOperation.accept(self)
    CompoundComparison.comparisonOperator.accept(self)
    CompoundComparison.infixOperation1.accept(self)


def visitSimpleInfixOperation(self, SimpleInfixOperation):
    SimpleInfixOperation.infixOperation.accept(self)
    SimpleInfixOperation.inOperator.accept(self)
    SimpleInfixOperation.elvisExpression.accept(self)


def visitCompoundInfixOperation(self, CompoundInfixOperation):
    CompoundInfixOperation.infixOperation.accept(self)
    CompoundInfixOperation.isOperator.accept(self)
    CompoundInfixOperation.type.accept(self)


def visitCompoundElvisExpression(self, CompoundElvisExpression):
    CompoundElvisExpression.elvisExpression.acceept(self)
    CompoundElvisExpression.rangeExpression.acceept(self)


def visitCompoundRangeExpression(self, CompoundRangeExpression):
    CompoundRangeExpression.additiveExpression.accept(self)
    CompoundRangeExpression.rangeExpression.accept(self)


def visitCompoundAdditiveExpression(self, CompoundAdditiveExpression):
    CompoundAdditiveExpression.additiveExpression.accept(self)
    CompoundAdditiveExpression.additiveOperator.accept(self)
    CompoundAdditiveExpression.multiplicativeExpression.accept(self)


def visitCompoundMultiplicativeExpression(self, CompoundMultiplicativeExpression):
    CompoundMultiplicativeExpression.multiplicativeExpression.accept(self)
    CompoundMultiplicativeExpression.multiplicativeOperator.accept(self)
    CompoundMultiplicativeExpression.asExpression.accept(self)


def visitCompoundAsExpression(self, CompoundAsExpression):
    CompoundAsExpression.unaryExpression.accept(self)
    CompoundAsExpression.asOperator.accept(self)


def visitSimpleUnaryExpressionConcrete(self, SimpleUnaryExpressionConcrete):
    SimpleUnaryExpressionConcrete.unaryOperator.accept(self)
    SimpleUnaryExpressionConcrete.primaryExpression.accept(self)


def visitCompoundUnaryExpressionConcrete(self, CompoundUnaryExpressionConcrete):
    CompoundUnaryExpressionConcrete.primaryExpression.accept(self)
    CompoundUnaryExpressionConcrete.postfixUnaryExpression.accept(self)


def visitReturn(self, Return):
    type = Return.expression.accept(self)
    scope = st.symbolTable[-1][st.SCOPE]
    bindable = st.getBindable(scope)
    if type != bindable[st.TYPE]:
        Return.accept(self.printer)
        print('Tipo de retorno Invalido, Esperava um ', bindable[st.TYPE])
    st.endScope()

















