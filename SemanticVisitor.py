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


    def visitKotlinFileConcrete(self,KotlinFile):
        KotlinFile.functionDeclaration.accept(self)
        KotlinFile.kotlinFile.accept(self)


    def visitFunctionDeclarationNoType(self, FunctionDeclaration):
        params = {}
        typeFunction = 'undefined'
        if FunctionDeclaration.functionValueParameters != None:
            params = FunctionDeclaration.functionValueParameters.accept(self)
            st.addFunction(FunctionDeclaration.id, params, typeFunction)
        else:
            st.addFunction(FunctionDeclaration.id, params, typeFunction)
        st.beginScope(FunctionDeclaration.id)
        
        for k in range(0, len(params), 2):
            st.addVar(params[k], params[k + 1])

        FunctionDeclaration.functionBody.accept(self)


    def visitFunctionDeclarationConcrete(self, FunctionDeclaration):
        params = {}
        st.beginScope(FunctionDeclaration.id)
        if FunctionDeclaration.functionValueParameters != None:
            params = FunctionDeclaration.functionValueParameters.accept(self)
            st.addFunction(FunctionDeclaration.id, params, FunctionDeclaration.type)
        else:
            st.addFunction(FunctionDeclaration.id, params, FunctionDeclaration.type)

        for k in range(0, len(params), 2):
            st.addVar(params[k], params[k + 1])


        FunctionDeclaration.functionBody.accept(self)


    def visitFunctionValueParametersNoParams(self, FunctionValueParameters):
        return FunctionValueParameters.accept(self)


    def visitFunctionValueParametersConcrete(self,FunctionValueParameters):
        return FunctionValueParameters.parameters.accept(self)


    def visitParametersConcrete(self, Parameters):
        return Parameters.parameter.accept(self) + Parameters.parameters.accept(self)


    def visitParameterConcrete(self, Parameter):
        return [Parameter.id, Parameter.type]


    def visitParenthesizedTypeConcrete(self,ParenthesizedType):
        return ParenthesizedType.type


    def visitFunctionBodyConcrete(self, FunctionBody):
        return FunctionBody.expression.accept(self)


    def visitStatementsConcrete(self,Statements):
        Statements.statement.accept(self)
        Statements.statements.accept(self)


    def visitIf_statement(self, If_statement):
        if If_statement.expression.accept(self) != st.BOOL:
            print('type', If_statement.expression.accept(self))
            If_statement.expression.accept(self.printer)
            print('\n\t[ERRO] A expressao deveria ser do tipo boolean')
        If_statement.statement.accept(self)

    def visitIf_block(self, If_block):
        if If_block.expression.accept(self) != st.BOOL:
            print('\n\t[ERRO] A expressao deveria ser do tipo boolean')
        If_block.block.accept(self)


    def visitSimpleIf_else(self, SimpleIf_else):
        if SimpleIf_else.expression.accept(self) != st.BOOL:
            print('\n\t[ERRO] A expressao deveria ser do tipo boolean')
        SimpleIf_else.block.accept(self)
        SimpleIf_else.open_statement.accept(self)


    def visitCompoundIf_else(self, CompoundIf_else):
        if CompoundIf_else.expression.accept(self) != st.BOOL:
            print('\n\t[ERRO] A expressao deveria ser do tipo boolean')
        CompoundIf_else.closed_statement.accept(self)
        CompoundIf_else.open_statement.accept(self)

    def visitWhile_Open_statement(self, While_Open_statement):
        if While_Open_statement.expression.accept(self) != st.BOOL:
            print('\n\t[ERRO] A expressao deveria ser do tipo boolean')
        While_Open_statement.expression.accept(self)
        While_Open_statement.open_statement.accept(self)


    def visitDoWhile_Open_statement(self, DoWhile_Open_statement):
        if DoWhile_Open_statement.expression.accept(self) != st.BOOL:
            print('\n\t[ERRO] A expressao deveria ser do tipo boolean')
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
            print('\n\t[ERRO] A expressao deveria ser do tipo boolean')
        If_Blocks_Closed_statement.block.accept(self)
        If_Blocks_Closed_statement.block1.accept(self)

    def visitIf_Mix1_Closed_statement(self, If_Mix1_Closed_statement):
        if If_Mix1_Closed_statement.expression == st.BOOL:
            If_Mix1_Closed_statement.block.accept(self)
            If_Mix1_Closed_statement.closed_statement.accept(self)
        else:
            print('\n\t[ERRO] A expressao deveria ser do tipo boolean')

    def visitIf_Mix2_Closed_statement(self, If_Mix2_Closed_statement):
        if If_Mix2_Closed_statement.expression == st.BOOL:
            If_Mix2_Closed_statement.closed_statement.accept(self)
            If_Mix2_Closed_statement.block.accept(self)
        else:
            print('\n\t[ERRO] A expressao deveria ser do tipo boolean')

    def visitIf_Closeds_Closed_statement(self, If_Closeds_Closed_statement):
        if If_Closeds_Closed_statement.expression == st.BOOL:
            If_Closeds_Closed_statement.closed_statement.accept(self)
            If_Closeds_Closed_statement.closed_statement.accept(self)
        else:
            print('\n\t[ERRO] A expressao deveria ser do tipo boolean')

    def visitFor_Closed_statement(self, For_Closed_statement):
        st.beginScope('for')
        nome = For_Closed_statement.genericVariableDeclaration
        st.addVar(nome, st.INT)
        For_Closed_statement.expression.accept(self.printer)
        For_Closed_statement.closed_statement.accept(self)
        st.endScope()


    def visitWhile_Closed_statement(self, While_Closed_statement):
        if While_Closed_statement.expression != st.BOOL:
            print('\n\t[ERRO] A expressao deveria ser do tipo boolean')
        While_Closed_statement.closed_statement.accept(self)


    def visitDoWhile_Closed_statement(self, DoWhile_Closed_statement):
        if DoWhile_Closed_statement.expression != st.BOOL:
            print('\n\t[ERRO] A expressao deveria ser do tipo boolean')
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
            print('\n\t[ERRO] A expressao deveria ser do tipo boolean')


    def visitDoWhile_Non_if_statement_block(self, DoWhile_Non_if_statement_block):
        if DoWhile_Non_if_statement_block.expression == st.BOOL:
            DoWhile_Non_if_statement_block.block.accept(self)
        else:
            print('\n\t[ERRO] A expressao deveria ser do tipo boolean')

    def visitAssignmentConcrete(self, Assignment):
        typeVar = conversao(Assignment.expression)
        if typeVar != None:
            st.addVar(Assignment.id, typeVar)
            return typeVar
        return None

    def visitAssignmentAndOperatorConcrete(self, AssignmentAndOperator):
        typeVar = conversao(AssignmentAndOperator.expression)
        if typeVar != None:
            st.addVar(AssignmentAndOperator.id, typeVar)
            return typeVar
        return None


    def visitBlockConcrete(self, Block):
        Block.statements.accept(self)


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

    def visitChamadaDeFuncaoConcrete(self, ChamadaDeFuncao):
        bindable = st.getBindable(ChamadaDeFuncao.id)
        if (bindable != None and bindable[st.BINDABLE] == st.FUNCTION):
            typeParams = ChamadaDeFuncao.params.accept(self)
            if (list(bindable[st.PARAMS][1::2]) == typeParams):
                return bindable[st.TYPE]
            ChamadaDeFuncao.accept(self.printer)
            print("\n\t[Erro] Chamada de funcao invalida. Tipos passados na chamada sao:", typeParams)
            print('\tenquanto que os tipos definidos no metodo sao:', bindable[st.PARAMS][1::2], '\n')
        else:
            print("\n\t[Erro] Chamada de funcao invalida. O id", ChamadaDeFuncao.id,
                  "nao eh de uma funcao, nao foi definido ou foi definido apos esta funcao\n")
        return None

    def visitChamadaDeFuncaoNoParams(self, ChamadaDeFuncao):
        bindable = st.getBindable(ChamadaDeFuncao.id)
        if (bindable != None and bindable[st.BINDABLE] == st.FUNCTION):
            return bindable[st.TYPE]
        print("\n\t[Erro] Chamada de funcao invalida. O id", ChamadaDeFuncao.id, "nao eh de uma funcao, nao foi definido ou foi definido apos esta funcao\n")
        return None

    def visitCompoundParams(self, compoundParams):
        return [compoundParams.exp.accept(self)] + compoundParams.params.accept(self)

    def visitSingleParam(self, singleParam):
        return [singleParam.exp.accept(self)]

    def visitVariableDeclarationConcrete(self, VariableDeclaration):
        typeVar = conversao(VariableDeclaration.type)
        if VariableDeclaration.id != None:
            st.addVar(VariableDeclaration.id, typeVar)
            return typeVar
        return None


    def visitVariableDeclarationsConcrete(self, VariableDeclarations):
        VariableDeclarations.variableDeclaration.accept(self)
        VariableDeclarations.variableDeclarations.accept(self)


    def visitMultiVariableDeclarationNone(self, MultiVariableDeclaration):
        return MultiVariableDeclaration.accept(self)


    def visitMultiVariableDeclarationConcrete(self, MultiVariableDeclaration):
        return MultiVariableDeclaration.variableDeclarations.accept(self)


    def visitParametersFunctionConcrete(self, ParametersFunction):
        ParametersFunction.primaryExpression.accept(self)
        ParametersFunction.parametersFunction.accept(self)


    def visitDisjunctionConcrete(self, Disjunction):
        type1 = Disjunction.conjunction.accept(self)
        type2 = Disjunction.disjunction.accept(self)
        if type1 == type2:
            return type1
        else:
            print('[ERRO] - Disjunction')
            return None


    def visitConjunctionConcrete(self, Conjunction):
        type1 = Conjunction.equality.accept(self)
        type2 = Conjunction.conjunction.accept(self)
        if type1 == type2:
            return type1
        else:
            print('[ERRO] - Conjunction')
            return None

    def visitEqualityConcrete(self, Equality):
        type1 = conversao(Equality.comparison)
        type2 = conversao(Equality.equality)
        if type1 == type2:
            return type1
        else:
            print('[ERRO] - Equality')
            return None

    def visitComparisonConcrete(self, Comparison):
        type1 = conversao(Comparison.infixOperation)
        Comparison.comparisonOperator
        type2 = conversao(Comparison.infixOperation)
        c = coercion(type1, type2)
        if c == None:
            print('[ERRO] - Comparison')
            return None
        return st.BOOL

    def visitInfixOperation_In(self, InfixOperation):
        type1 = conversao(InfixOperation.infixOperation)
        SimpleInfixOperation.inOperator
        type2 = conversao(InfixOperation.elvisExpression)
        print(type1, type2)
        if type1 == type2:
            print('[ERRO] - infix Esperava um tipo inteiro')
            return None
        return type1

    def visitInfixOperation_Is(self, InfixOperation):
        type1 = InfixOperation.infixOperation.accept(self)
        InfixOperation.isOperator
        type2 = InfixOperation.type.accept(self)
        print(type1, type2)
        c = coercion(type1, type2)
        if c == None:
            print('[ERRO] - cInfixOperation')
            return None
        return c

    def visitElvisExpressionConcrete(self, ElvisExpression):
        type1 = ElvisExpression.elvisExpression.acceept(self)
        type2 = ElvisExpression.rangeExpression.acceept(self)
        print(type1, type2)
        c = coercion(type1, type2)
        if c == None:
            print('[ERRO] - elvis')
            return None
        return c

    def visitRangeExpressionConcrete(self, RangeExpression):
        type1 = conversao(RangeExpression.rangeExpression)
        type2 = conversao(RangeExpression.additiveExpression)
        c = coercion(type1, type2)
        if c == None:
            print('[ERRO] - range Esperava um tipo inteiro')
            return None
        return c


    def visitAdditiveExpressionConcrete(self, AdditiveExpression):
        type1 = conversao(AdditiveExpression.additiveExpression)
        AdditiveExpression.additiveOperator
        type2 = conversao(AdditiveExpression.multiplicativeExpression)
        c = coercion(type1, type2)
        if c == None:
            print('[ERRO] - additive')
            return None
        return c

    def visitMultiplicativeExpressionConcrete(self, MultiplicativeExpression):
        type1 = conversao(MultiplicativeExpression.multiplicativeExpression)
        MultiplicativeExpression.multiplicativeOperator
        type2 = conversao(MultiplicativeExpression.asExpression)
        c = coercion(type1, type2)
        if c == None:
            print('[ERRO] - multiplicative')
            return None
        return c


    def visitAsExpressionConcrete(self, AsExpression):
        AsExpression.unaryExpression.accept(self)
        AsExpression.asOperator
        AsExpression.type.accept(self)


    def visitUnaryExpressionConcrete(self, UnaryExpression):
        UnaryExpression.unaryOperator.accept(self)
        UnaryExpression.primaryExpression


    def visitUnaryExpressionPostfixConcrete(self, UnaryExpression):
        conversao(UnaryExpression.primaryExpression)
        conversao(UnaryExpression.postfixUnaryExpression)


    def visitReturnConcrete(self, Return):
        type = Return.expression
        if type == st.TRUE:
            scope = st.symbolTable[-1][st.SCOPE]
            bindable = st.getBindable(scope)
            if type != bindable[st.TYPE]:
                Return.accept(self.printer)
                print('Tipo de retorno Invalido, Esperava um ', bindable[st.TYPE])
            st.endScope()
        else:
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
        
    # def visitCompoundAsOperator(self, CompoundAsOperator):
    #     return CompoundAsOperator.asOperator.accept(self)
    
    def visitAsOperatorConcrete(self, SimpleAsOperator):
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