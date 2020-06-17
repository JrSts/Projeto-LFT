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
        
        typeFunction = 'undefined'
        if SimpleFunctionDeclaration.functionValueParameters != None:
            params = SimpleFunctionDeclaration.functionValueParameters.accept(self)
            st.addFunction(SimpleFunctionDeclaration.Id, params, typeFunction)
        else:
            st.addFunction(SimpleFunctionDeclaration.Id, params, typeFunction)
        st.beginScope(SimpleFunctionDeclaration.Id)
        
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
        return SimpleFunctionValueParameters.accept(self)


    def visitCompoundFunctionValueParameters(self,CompoundFunctionValueParameters):
        return CompoundFunctionValueParameters.parameters.accept(self)


    def visitCompoundParameters(self, CompoundParameters):
        return [CompoundParameters.id, CompoundParameters.type] + CompoundParameters.parameters.accept(self)


    def visitSimpleParameter(self, SimpleParameter):
        return [SimpleParameter.id, SimpleParameter.type]


    def visitParenthesizedTypeConcrete(self,ParenthesizedTypeConcrete):
        return ParenthesizedTypeConcrete.type.accept(self)


    def visitCompoundFunctionBody(self, CompoundFunctionBody):
        CompoundFunctionBody.expression.accept(self)


    def visitCompoundStatements(self,CompoundStatements):
        CompoundStatements.statement.accept(self)
        CompoundStatements.statements.accept(self)


    def visitIf_statement(self, If_statement):
        if If_statement.expression == sv.BOOLEAN:
            If_statement.statement.accept(self)
        else:
            If_statement.expression.accept(self.printer)
            print("\n\t[ERRO] A expressao ",
                  If_statement.expression.accept(self.printer),
                  ' eh ', type, ' Deveria ser boolean')


    def visitIf_block(self, If_block):
        if If_block.expression == sv.BOOLEAN:
            If_block.block.accept(self)
        else:
            If_block.expression.accept(self.printer)
            print("\n\t[ERRO] A expressao ",
                  If_block.expression.accept(self.printer),
                  ' eh ', type, ' Deveria ser boolean')


    def visitSimpleIf_else(self, SimpleIf_else):
        if SimpleIf_else.expression == sv.BOOLEAN:
            SimpleIf_else.block.accept(self)
            SimpleIf_else.open_statement.accept(self)
        else:
            SimpleIf_else.expression.accept(self.printer)
            print("\n\t[ERRO] A expressao ",
                  SimpleIf_else.expression.accept(self.printer),
                  ' eh ', type, ' Deveria ser boolean')


    def visitCompoundIf_else(self, CompoundIf_else):
        if CompoundIf_else.expression == sv.BOOLEAN:
            CompoundIf_else.closed_statement.accept(self)
            CompoundIf_else.open_statement.accept(self)
        else:
            CompoundIf_else.expression.accept(self.printer)
            print("\n\t[ERRO] A expressao ",
                  CompoundIf_else.expression.accept(self.printer),
                  ' eh ', type, ' Deveria ser boolean')


    def visitWhile_Open_statement(self, While_Open_statement):
        While_Open_statement.expression.accept(self)
        While_Open_statement.open_statement.accept(self)


    def visitDoWhile_Open_statement(self, DoWhile_Open_statement):
        if DoWhile_Open_statement.expression == st.BOOL:
            DoWhile_Open_statement.open_statement.accept(self)
        else:
            DoWhile_Open_statement.expression.accept(self.printer)
            print("\n\t[ERRO] A expressao ",
                  DoWhile_Open_statement.expression.accept(self.printer),
                  ' eh ', type, ' Deveria ser boolean')


    def visitFor_Open_statement(self, For_Open_statement):
        nome = For_Open_statement.genericVariableDeclaration
        print(nome)
        if isinstance(nome, st.STRING):
            if nome[0] != '\'':
                st.addVar(nome, 'int')
            else:
                print('ERRO - For')
        else:
            print('erro')
        For_Open_statement.open_statement.accept(self)
        For_Open_statement.expression.accept(self.printer)
        


    def visitIf_Blocks_Closed_statement(self, If_Blocks_Closed_statement):
        if If_Blocks_Closed_statement.expression == bool:
            If_Blocks_Closed_statement.block.accept(self)
            If_Blocks_Closed_statement.block1.accept(self)
        else:
            If_Blocks_Closed_statement.expression.accept(self.printer)
            print("\n\t[ERRO] A expressao ",
                  If_Blocks_Closed_statement.expression.accept(self.printer),
                  ' eh ', type, ' Deveria ser boolean')


    def visitIf_Mix1_Closed_statement(self, If_Mix1_Closed_statement):
        if If_Mix1_Closed_statement.expression == bool:
            If_Mix1_Closed_statement.block.accept(self)
            If_Mix1_Closed_statement.closed_statement.accept(self)
        else:
            If_Mix1_Closed_statement.expression.accept(self.printer)
            print("\n\t[ERRO] A expressao ", 
            If_Mix1_Closed_statement.expression.accept(self.printer),
            ' eh ', type, ' Deveria ser boolean')


    def visitIf_Mix2_Closed_statement(self, If_Mix2_Closed_statement):
        if If_Mix2_Closed_statement.expression == bool:
            If_Mix2_Closed_statement.closed_statement.accept(self)
            If_Mix2_Closed_statement.block.accept(self)
        else:
            If_Mix2_Closed_statement.expression.accept(self.printer)
            print("\n\t[ERRO] A expressao ",
              If_Mix2_Closed_statement.expression.accept(self.printer),
              ' eh ', type, ' Deveria ser boolean')

    def visitIf_Closeds_Closed_statement(self, If_Closeds_Closed_statement):
        if If_Closeds_Closed_statement.expression == bool:
            If_Closeds_Closed_statement.closed_statement.accept(self)
            If_Closeds_Closed_statement.closed_statement.accept(self)
        else:
            If_Closeds_Closed_statement.expression.accept(self.printer)
            print("\n\t[ERRO] A expressao ",
                If_Closeds_Closed_statement.expression.accept(self.printer),
                ' eh ', type, ' Deveria ser boolean')


    def visitFor_Closed_statement(self, For_Closed_statement):
        For_Closed_statement.genericVariableDeclaration.accept(self)
        if For_Closed_statement.expression == st.BOOL:
            For_Closed_statement.closed_statement.accept(self)
        else:
            For_Closed_statement.expression.accept(self.printer)
            print("\n\t[ERRO] A expressao ",
                For_Closed_statement.expression.accept(self.printer),
                ' eh ', type, ' Deveria ser boolean')

    def visitWhile_Closed_statement(self, While_Closed_statement):
        if While_Closed_statement.expression == bool:
            While_Closed_statement.closed_statement.accept(self)
        else:
            While_Closed_statement.expression.accept(self.printer)
            print("\n\t[ERRO] A expressao ",
                While_Closed_statement.expression.accept(self.printer),
                ' eh ', type, ' Deveria ser boolean')


    def visitDoWhile_Closed_statement(self, DoWhile_Closed_statement):
        if DoWhile_Closed_statement.expression == bool:
            DoWhile_Closed_statement.closed_statement.accept(self)
        else:
            DoWhile_Closed_statement.expression.accept(self.printer)
            print("\n\t[ERRO] A expressao ",
                DoWhile_Closed_statement.expression.accept(self.printer),
                ' eh ', type, ' Deveria ser boolean')


    def visitFor_Non_if_statement_block(self, For_Non_if_statement_block):
        For_Non_if_statement_block.genericVariableDeclaration
        For_Non_if_statement_block.expression.accept(self)
        For_Non_if_statement_block.block.accept(self)


    def visitWhile_Non_if_statement_block(self, While_Non_if_statement_block):
        if While_Non_if_statement_block.expression == bool:
            While_Non_if_statement_block.block.accept(self)
        else:
            While_Non_if_statement_block.expression.accept(self.printer)
            print("\n\t[ERRO] A expressao ",
                While_Non_if_statement_block.expression.accept(self.printer),
                ' eh ', type, ' Deveria ser boolean')


    def visitDoWhile_Non_if_statement_block(self, DoWhile_Non_if_statement_block):
        if DoWhile_Non_if_statement_block.expression == bool:
            DoWhile_Non_if_statement_block.block.accept(self)
        else:
            DoWhile_Non_if_statement_block.expression.accept(self.printer)
            print("\n\t[ERRO] A expressao ",
                DoWhile_Non_if_statement_block.expression.accept(self.printer),
                ' eh ', type, ' Deveria ser boolean')

    def visitAssignmentConcrete(self, AssignmentConcrete):
        typeVar = AssignmentConcrete.expression.accept(self)
        if typeVar != None:
            st.addVar(AssignmentConcrete.id, typeVar)
            return typeVar
        return None

    def visitAssignmentAndOperatorConcrete(self, AssignmentAndOperatorConcrete):
        typeVar = AssignmentAndOperatorConcrete.expression
        if typeVar != None:
            st.addVar(AssignmentAndOperatorConcrete.id, typeVar)
            return typeVar
        return None


    def visitBlockConcrete(self, BlockConcrete):
        BlockConcrete.statements.accept(self)


    def visitPropertyDeclarationStm_Var(self, PropertyDeclarationStm_Var):
       typeVar = PropertyDeclarationStm_Var.expression
       st.addVar(PropertyDeclarationStm_Var.genericVariableDeclaration, typeVar)
       return typeVar


    def visitPropertyDeclarationStm_Val(self, PropertyDeclarationStm_Val):
       typeVar = PropertyDeclarationStm_Val.expression
       st.addVar(PropertyDeclarationStm_Val.genericVariableDeclaration, typeVar)
       return typeVar

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
        return SimpleMultiVariableDeclaration.accept(self)


    def visitCompoundMultiVariableDeclaration(self, CompoundMultiVariableDeclaration):
        return CompoundMultiVariableDeclaration.variableDeclarations.accept(self)


    def visitCompoundParametersFunction(self, CompoundParametersFunction):
        CompoundParametersFunction.primaryExpression.accept(self)
        CompoundParametersFunction.parametersFunction.accept(self)


    def visitCompoundDisjunction(self, CompoundDisjunction):
        type1 = CompoundDisjunction.conjunction.accept(self)
        type2 = CompoundDisjunction.disjunction.accept(self)
        c = coercion(type1, type2)
        if c == None:
            print('[ERRO] - disjunction')
        return c


    def visitCompoundConjunction(self, CompoundConjunction):
        type1 = CompoundConjunction.equality.accept(self)
        type2 = CompoundConjunction.conjunction.accept(self)
        c = coercion(type1, type2)
        if c == None:
            print('[ERRO] - conjunction')
        return c


    def visitCompoundEquality(self, CompoundEquality):
        type1 = CompoundEquality.comparison.accept(self)
        type2 = CompoundEquality.equality.accept(self)
        c = coercion(type1, type2)
        if c == None:
            print('[ERRO] - equality')
        return c

    def visitCompoundComparison(self, CompoundComparison):
        type1 = CompoundComparison.infixOperation.accept(self)
        CompoundComparison.comparisonOperator.accept(self)
        type2 = CompoundComparison.infixOperation1.accept(self)
        c = coercion(type1, type2)
        if c == None:
            print('[ERRO] - Comparison')
        return c

    def visitSimpleInfixOperation(self, SimpleInfixOperation):
        type1 = SimpleInfixOperation.infixOperation.accept(self)
        SimpleInfixOperation.inOperator.accept(self)
        type2 = SimpleInfixOperation.elvisExpression.accept(self)
        c = coercion(type1, type2)
        if c == None:
            print('[ERRO] - sInfixOperation')
        return c

    def visitCompoundInfixOperation(self, CompoundInfixOperation):
        type1 = CompoundInfixOperation.infixOperation.accept(self)
        CompoundInfixOperation.isOperator.accept(self)
        type2 = CompoundInfixOperation.type.accept(self)
        c = coercion(type1, type2)
        if c == None:
            print('[ERRO] - cInfixOperation')
        return c

    def visitCompoundElvisExpression(self, CompoundElvisExpression):
        type1 = CompoundElvisExpression.elvisExpression.acceept(self)
        type2 = CompoundElvisExpression.rangeExpression.acceept(self)
        c = coercion(type1, type2)
        if c == None:
            print('[ERRO] - elvis')
        return c

    def visitCompoundRangeExpression(self, CompoundRangeExpression):
        tipo1 = CompoundRangeExpression.additiveExpression
        tipo2 = CompoundRangeExpression.rangeExpression
        c = coercion(tipo1, tipo2)
        if (type(c) != int):
            print('[ERRO] - range Esperava um tipo inteiro')
        return c



    def visitCompoundAdditiveExpression(self, CompoundAdditiveExpression):
        type1 = CompoundAdditiveExpression.additiveExpression.accept(self)
        CompoundAdditiveExpression.additiveOperator.accept(self)
        type2 = CompoundAdditiveExpression.multiplicativeExpression.accept(self)
        c = coercion(type1, type2)
        if c == None:
            print('[ERRO] - additive')
        return c

    def visitCompoundMultiplicativeExpression(self, CompoundMultiplicativeExpression):
        type1 = CompoundMultiplicativeExpression.multiplicativeExpression.accept(self)
        CompoundMultiplicativeExpression.multiplicativeOperator.accept(self)
        type2 = CompoundMultiplicativeExpression.asExpression.accept(self)
        c = coercion(type1, type2)
        if c == None:
            print('[ERRO] - multiplicative')
        return c


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

    
    def visitParenthesizedExpressionConcrete(self, ParenthesizedExpressionConcrete):
        return ParenthesizedExpressionConcrete.expression.accept(self)

    
    def visitMAISIGUAL(self, MAISIGUAL):
        return MAISIGUAL.maisIgual
        
    def visitMENOSIGUAL(self, MENOSIGUAL):
        return MENOSIGUAL.menosIgual

    def visitMULTIGUAL(self, MULTIGUAL):
        return MULTIGUAL.multiIgual
    
    def visitDIVIGUAL(self, DIVIGUAL):
        return DIVIGUAL.divIgual

    def visitMODIGUAL(self, MODIGUAL):
        return MODIGUAL.modIgual

    def visitDiferente(self, Diferente):
        return Diferente.diferente

    def visitIgualdade(self, Igualdade):
        return Igualdade.igualdade

    def visitIdentidade(self, Identidade):
        return Identidade.identidade

    def visitSemIdentidade(self, SemIdentidade):
        return SemIdentidade.semIdentidade

    def visitMaior(self, Maior):
        return Maior.maior

    def visitMenor(self, Menor):
        return Menor.menor
    
    def visitMenorIgual(self, MenorIgual):
        return MenorIgual.menorIgual

    def visitMaiorIgual(self, MaiorIgual):
        return MaiorIgual.maiorIgual

    def visitIn(self, In):
        return In.IN

    def visitNotIn(self, NotIn):
        return NotIn.notIn

    def visitIs(self, Is):
        return Is.IS

    def visitNotIs(self, NotIs):
        return NotIs.NotIs
        
    def visitMult(self, Mult):
        return Mult.mult

    def visitMod(self, Mod):
        return Mod.mod
    
    def visitDivide(self, Divide):
        return Divide.divide
        
    def visitCompoundAsOperator(self, CompoundAsOperator):
        return CompoundAsOperator.asOperator.accept(self)
    
    def visitSimpleAsOperator(self, SimpleAsOperator):
        return SimpleAsOperator
                
    def visitIncremento(self, Incremento):
        return Incremento.incremento
    
    def visitDecremento(self, Decremento):
        return Decremento.decremento

    def visitMinus(self, Minus):
        return Minus.minus

    def visitPlus(self, Plus):
        return Plus.plus

    def visitNot(self, Not):
        return Not.NOT