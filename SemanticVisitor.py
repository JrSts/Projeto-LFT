from AbstractVisitor import AbstractVisitor
import SymbolTable as st
from Visitor import Visitor
from lex import lex
import re
import ConcretaClass as co
import AbstrataClass as ac

def coercion(type1, type2):
    if (type1 in st.Number and type2 in st.Number):
        #print('passei aqui')
        if type1 == st.FLOAT or type2 == st.FLOAT:
            #print('passei')
            return st.FLOAT
        else:
            #print('nao passei')
            return st.INT
    else:
        return None


def conversao(type):
    if isinstance(type, int):
        return st.INT
    elif isinstance(type, float):
        return st.FLOAT
    elif type == st.TRUE or type == st.FALSE:
        return st.BOOL
    elif type[0] == '\"':
        return st.STRING
    else:
        type = st.getBindable(type)
        if (type != None):
            return type[st.TYPE]
        return type

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
        st.beginScope(CompoundFunctionDeclaration.id)
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
        return CompoundParameters.parameter.accept(self) + CompoundParameters.parameters.accept(self)


    def visitSimpleParameter(self, SimpleParameter):
        return [SimpleParameter.id, SimpleParameter.type]


    def visitParenthesizedTypeConcrete(self,ParenthesizedTypeConcrete):
        return ParenthesizedTypeConcrete.type


    def visitCompoundFunctionBody(self, CompoundFunctionBody):
        return CompoundFunctionBody.expression.accept(self)


    def visitCompoundStatements(self,CompoundStatements):
        CompoundStatements.statement.accept(self)
        CompoundStatements.statements.accept(self)


    def visitIf_statement(self, If_statement):
        if If_statement.expression.accept(self) != st.BOOL:
            print('type', If_statement.expression.accept(self))
            If_statement.expression.accept(self.printer)
            print("\n\t[ERRO] A expressao ",
                  If_statement.expression.accept(self.printer),
                  ' eh ', type, ' Deveria ser boolean')
        If_statement.statement.accept(self)

    def visitIf_block(self, If_block):
        if If_block.expression.accept(self) != st.BOOL:
            print('type', If_block.expression.accept(self))
            If_block.expression.accept(self.printer)
            print("\n\t[ERRO] A expressao ",
                  If_block.expression.accept(self.printer),
                  ' eh ', type, ' Deveria ser boolean')
        If_block.block.accept(self)


    def visitSimpleIf_else(self, SimpleIf_else):
        if SimpleIf_else.expression.accept(self) != st.BOOL:
            print('type', SimpleIf_else.expression.accept(self))
            SimpleIf_else.expression.accept(self.printer)
            print("\n\t[ERRO] A expressao ",
                  SimpleIf_else.expression.accept(self.printer),
                  ' eh ', type, ' Deveria ser boolean')
        SimpleIf_else.block.accept(self)
        SimpleIf_else.open_statement.accept(self)


    def visitCompoundIf_else(self, CompoundIf_else):
        if CompoundIf_else.expression.accept(self) != st.BOOL:
            print('type', CompoundIf_else.expression.accept(self))
            CompoundIf_else.expression.accept(self.printer)
            print("\n\t[ERRO] A expressao ",
                  CompoundIf_else.expression.accept(self.printer),
                  ' eh ', type, ' Deveria ser boolean')
        CompoundIf_else.closed_statement.accept(self)
        CompoundIf_else.open_statement.accept(self)

    def visitWhile_Open_statement(self, While_Open_statement):
        if While_Open_statement.expression.accept(self) != st.BOOL:
            print('type', While_Open_statement.expression.accept(self))
            While_Open_statement.expression.accept(self.printer)
            print("\n\t[ERRO] A expressao ",
                  While_Open_statement.expression.accept(self.printer),
                  ' eh ', type, ' Deveria ser boolean')
        While_Open_statement.expression.accept(self)
        While_Open_statement.open_statement.accept(self)


    def visitDoWhile_Open_statement(self, DoWhile_Open_statement):
        if DoWhile_Open_statement.expression.accept(self) != st.BOOL:
            print('type', DoWhile_Open_statement.expression.accept(self))
            DoWhile_Open_statement.expression.accept(self.printer)
            print("\n\t[ERRO] A expressao ",
                 DoWhile_Open_statement.expression.accept(self.printer),
                 ' eh ', type, ' Deveria ser boolean')
        DoWhile_Open_statement.open_statement.accept(self)


    def visitFor_Open_statement(self, For_Open_statement):
        st.beginScope('for')
        nome = For_Open_statement.genericVariableDeclaration
        st.addVar(nome, st.INT)
        For_Open_statement.expression.accept(self.printer)
        For_Open_statement.open_statement.accept(self)
        st.endScope()


    def visitIf_Blocks_Closed_statement(self, If_Blocks_Closed_statement):
        if If_Blocks_Closed_statement.expression.accept(self) != st.BOOL:
            If_Blocks_Closed_statement.expression.accept(self.printer)
            print("\n\t[ERRO] A expressao ",
                  If_Blocks_Closed_statement.expression.accept(self.printer),
                  ' eh ', type, ' Deveria ser boolean')
        If_Blocks_Closed_statement.block.accept(self)
        If_Blocks_Closed_statement.block1.accept(self)

    def visitIf_Mix1_Closed_statement(self, If_Mix1_Closed_statement):
        if If_Mix1_Closed_statement.expression == st.BOOL:
            If_Mix1_Closed_statement.block.accept(self)
            If_Mix1_Closed_statement.closed_statement.accept(self)
        else:
            If_Mix1_Closed_statement.expression.accept(self.printer)
            print("\n\t[ERRO] A expressao ", 
            If_Mix1_Closed_statement.expression.accept(self.printer),
            ' eh ', type, ' Deveria ser boolean')


    def visitIf_Mix2_Closed_statement(self, If_Mix2_Closed_statement):
        if If_Mix2_Closed_statement.expression == st.BOOL:
            If_Mix2_Closed_statement.closed_statement.accept(self)
            If_Mix2_Closed_statement.block.accept(self)
        else:
            If_Mix2_Closed_statement.expression.accept(self.printer)
            print("\n\t[ERRO] A expressao ",
              If_Mix2_Closed_statement.expression.accept(self.printer),
              ' eh ', type, ' Deveria ser boolean')

    def visitIf_Closeds_Closed_statement(self, If_Closeds_Closed_statement):
        if If_Closeds_Closed_statement.expression == st.BOOL:
            If_Closeds_Closed_statement.closed_statement.accept(self)
            If_Closeds_Closed_statement.closed_statement.accept(self)
        else:
            If_Closeds_Closed_statement.expression.accept(self.printer)
            print("\n\t[ERRO] A expressao ",
                If_Closeds_Closed_statement.expression.accept(self.printer),
                ' eh ', type, ' Deveria ser boolean')


    def visitFor_Closed_statement(self, For_Closed_statement):
        st.beginScope('for')
        nome = For_Closed_statement.genericVariableDeclaration
        st.addVar(nome, st.INT)
        For_Closed_statement.expression.accept(self.printer)
        For_Closed_statement.closed_statement.accept(self)
        st.endScope()


    def visitWhile_Closed_statement(self, While_Closed_statement):
        if While_Closed_statement.expression != st.BOOL:
            While_Closed_statement.expression.accept(self.printer)
            print("\n\t[ERRO] A expressao ",
                While_Closed_statement.expression.accept(self.printer),
                ' eh ', type, ' Deveria ser boolean')
        While_Closed_statement.closed_statement.accept(self)


    def visitDoWhile_Closed_statement(self, DoWhile_Closed_statement):
        if DoWhile_Closed_statement.expression != st.BOOL:
            DoWhile_Closed_statement.expression.accept(self.printer)
            print("\n\t[ERRO] A expressao ",
                DoWhile_Closed_statement.expression.accept(self.printer),
                ' eh ', type, ' Deveria ser boolean')
        DoWhile_Closed_statement.closed_statement.accept(self)


    def visitFor_Non_if_statement_block(self, For_Non_if_statement_block):
        st.beginScope('for')
        nome = For_Non_if_statement_block.genericVariableDeclaration
        st.addVar(nome, st.INT)
        For_Non_if_statement_block.expression.accept(self)
        For_Non_if_statement_block.block.accept(self)
        st.endScope()


    def visitWhile_Non_if_statement_block(self, While_Non_if_statement_block):
        if While_Non_if_statement_block.expression == st.BOOL:
            While_Non_if_statement_block.block.accept(self)
        else:
            While_Non_if_statement_block.expression.accept(self.printer)
            print("\n\t[ERRO] A expressao ",
                While_Non_if_statement_block.expression.accept(self.printer),
                ' eh ', type, ' Deveria ser boolean')


    def visitDoWhile_Non_if_statement_block(self, DoWhile_Non_if_statement_block):
        if DoWhile_Non_if_statement_block.expression == st.BOOL:
            DoWhile_Non_if_statement_block.block.accept(self)
        else:
            DoWhile_Non_if_statement_block.expression.accept(self.printer)
            print("\n\t[ERRO] A expressao ",
                DoWhile_Non_if_statement_block.expression.accept(self.printer),
                ' eh ', type, ' Deveria ser boolean')

    def visitAssignmentConcrete(self, AssignmentConcrete):
        typeVar = conversao(AssignmentConcrete.expression)
        if typeVar != None:
            st.addVar(AssignmentConcrete.id, typeVar)
            return typeVar
        return None

    def visitAssignmentAndOperatorConcrete(self, AssignmentAndOperatorConcrete):
        typeVar = conversao(AssignmentAndOperatorConcrete.expression)
        if typeVar != None:
            st.addVar(AssignmentAndOperatorConcrete.id, typeVar)
            return typeVar
        return None


    def visitBlockConcrete(self, BlockConcrete):
        BlockConcrete.statements.accept(self)


    def visitPropertyDeclarationStm_Var(self, PropertyDeclarationStm_Var):
        typeVar = PropertyDeclarationStm_Var.expression
        if type(typeVar) == int or type(typeVar) == bool or type(typeVar) == str:
            typeVar = conversao(typeVar)
            st.addVar(PropertyDeclarationStm_Var.genericVariableDeclaration, typeVar)
        else:
            typeVar = PropertyDeclarationStm_Var.expression.accept(self)
            st.addVar(PropertyDeclarationStm_Var.genericVariableDeclaration, typeVar)
        return typeVar


    def visitPropertyDeclarationStm_Val(self, PropertyDeclarationStm_Val):
        typeVal = PropertyDeclarationStm_Val.expression
        if type(typeVal) == int:
            typeVal = conversao(typeVal)
            st.addVal(PropertyDeclarationStm_Val.genericVariableDeclaration, typeVal)
        else:
            typeVal = PropertyDeclarationStm_Val.expression.accept(self)
            st.addVal(PropertyDeclarationStm_Val.genericVariableDeclaration, typeVal)
        return typeVal

    def visitCompoundChamadaDeFuncao(self, CompoundChamadaDeFuncao):
        bindable = st.getBindable(CompoundChamadaDeFuncao.id)
        if (bindable != None and bindable[st.BINDABLE] == st.FUNCTION):
            typeParams = CompoundChamadaDeFuncao.params.accept(self)
            if (list(bindable[st.PARAMS][1::2]) == typeParams):
                return bindable[st.TYPE]
            CompoundChamadaDeFuncao.accept(self.printer)
            print("\n\t[Erro] Chamada de funcao invalida. Tipos passados na chamada sao:", typeParams)
            print('\tenquanto que os tipos definidos no metodo sao:', bindable[st.PARAMS][1::2], '\n')
        else:
            CompoundChamadaDeFuncao.parametersFunction
            print("\n\t[Erro] Chamada de funcao invalida. O id", CompoundChamadaDeFuncao.id,
                  "nao eh de uma funcao, nao foi definido ou foi definido apos esta funcao\n")
        return None

    def visitSimpleChamadaDeFuncao(self, SimpleChamadaDeFuncao):
        bindable = st.getBindable(SimpleChamadaDeFuncao.id)
        if (bindable != None and bindable[st.BINDABLE] == st.FUNCTION):
            return bindable[st.TYPE]
        SimpleChamadaDeFuncao.accept(self.printer)
        print("\n\t[Erro] Chamada de funcao invalida. O id", SimpleChamadaDeFuncao.id, "nao eh de uma funcao, nao foi definido ou foi definido apos esta funcao\n")
        return None

    def visitCompoundParams(self, compoundParams):
        return [compoundParams.exp.accept(self)] + compoundParams.params.accept(self)

    def visitSingleParam(self, singleParam):
        return [singleParam.exp.accept(self)]

    def visitCompoundVariableDeclaration(self, CompoundVariableDeclaration):
        typeVar = conversao(CompoundVariableDeclaration.type)
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
        if type1 == type2:
            return type1
        else:
            print('[ERRO] - Disjunction')
            return None


    def visitCompoundConjunction(self, CompoundConjunction):
        type1 = CompoundConjunction.equality.accept(self)
        type2 = CompoundConjunction.conjunction.accept(self)
        if type1 == type2:
            return type1
        else:
            print('[ERRO] - Conjunction')
            return None

    def visitCompoundEquality(self, CompoundEquality):
        type1 = conversao(CompoundEquality.comparison)
        type2 = conversao(CompoundEquality.equality)
        if type1 == type2:
            return type1
        else:
            print('[ERRO] - Equality')
            return None

    def visitCompoundComparison(self, CompoundComparison):
        type1 = conversao(CompoundComparison.infixOperation)
        CompoundComparison.comparisonOperator
        type2 = conversao(CompoundComparison.infixOperation)
        c = coercion(type1, type2)
        if c == None:
            print('[ERRO] - Comparison')
            return None
        return st.BOOL

    def visitSimpleInfixOperation(self, SimpleInfixOperation):
        type1 = conversao(SimpleInfixOperation.infixOperation)
        SimpleInfixOperation.inOperator
        type2 = conversao(SimpleInfixOperation.elvisExpression)
        print(type1, type2)
        if type1 == type2:
            print('[ERRO] - infix Esperava um tipo inteiro')
            return None
        return type1

    def visitCompoundInfixOperation(self, CompoundInfixOperation):
        type1 = CompoundInfixOperation.infixOperation.accept(self)
        CompoundInfixOperation.isOperator
        type2 = CompoundInfixOperation.type.accept(self)
        print(type1, type2)
        c = coercion(type1, type2)
        if c == None:
            print('[ERRO] - cInfixOperation')
            return None
        return c

    def visitCompoundElvisExpression(self, CompoundElvisExpression):
        type1 = CompoundElvisExpression.elvisExpression.acceept(self)
        type2 = CompoundElvisExpression.rangeExpression.acceept(self)
        print(type1, type2)
        c = coercion(type1, type2)
        if c == None:
            print('[ERRO] - elvis')
            return None
        return c

    def visitCompoundRangeExpression(self, CompoundRangeExpression):
        type1 = conversao(CompoundRangeExpression.rangeExpression)
        type2 = conversao(CompoundRangeExpression.additiveExpression)
        c = coercion(type1, type2)
        if c == None:
            print('[ERRO] - range Esperava um tipo inteiro')
            return None
        return c


    def visitCompoundAdditiveExpression(self, CompoundAdditiveExpression):
        print('visitCompoundAdditiveExpression')
        type1 = conversao(CompoundAdditiveExpression.additiveExpression)
        CompoundAdditiveExpression.additiveOperator
        type2 = conversao(CompoundAdditiveExpression.multiplicativeExpression)
        c = coercion(type1, type2)
        if c == None:
            print('[ERRO] - additive')
            return None
        return c

    def visitCompoundMultiplicativeExpression(self, CompoundMultiplicativeExpression):
        type1 = conversao(CompoundMultiplicativeExpression.multiplicativeExpression)
        CompoundMultiplicativeExpression.multiplicativeOperator
        type2 = conversao(CompoundMultiplicativeExpression.asExpression)
        c = coercion(type1, type2)
        if c == None:
            print('[ERRO] - multiplicative')
            return None
        return c


    def visitCompoundAsExpression(self, CompoundAsExpression):
        CompoundAsExpression.unaryExpression.accept(self)
        CompoundAsExpression.asOperator


    def visitSimpleUnaryExpressionConcrete(self, SimpleUnaryExpressionConcrete):
        SimpleUnaryExpressionConcrete.unaryOperator.accept(self)
        SimpleUnaryExpressionConcrete.primaryExpression


    def visitCompoundUnaryExpressionConcrete(self, CompoundUnaryExpressionConcrete):
        conversao(CompoundUnaryExpressionConcrete.primaryExpression)
        conversao(CompoundUnaryExpressionConcrete.postfixUnaryExpression)



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