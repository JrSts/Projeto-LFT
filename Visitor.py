from AbstractVisitor import AbstractVisitor
class Visitor (AbstractVisitor):
    '''def visitSomaExp(self, somaExp):
        somaExp.exp1.accept(self)
        print('+')
        somaExp.exp2.accept(self)

    def visitMulExp(self, mulExp):
        mulExp.exp1.accept(self)
        print('*')
        mulExp.exp2.accept(self)
        
    def  visitPotExp(self, PotExp):
        PotExp.exp2.accept(self)
        print('^')
        PotExp.exp3.accept(self)

    def visitCallexp (self, CallExp):
        CallExp.call.accept(self)
        print('call')
    
    def visitAssignExp (self, AssignExp):
        AssignExp.assign.accept(self)
        print('assign')
    
    def visitNumExp (self,  NumExp ):
        NumExp.num.accept(self)
        print('num')
    
    def visitIDExp (self, IDExp):
        IDExp.id.accept(self)
        print('id')
    
    def visitParamsCall (self,  ParamsCall):
        ParamsCall.ID.accept(self)
        print('ID')
        ParamsCall.Params.accept(self)
        print('Params')

    def visitSimplesCall (self, SimplesCall):
        SimplesCall.ID.accept(self)
        print('ID')

    def visitCompoundParams (self, CompoudParams):
        CompoudParams.ID.accept(self)
        print('ID')
        CompoudParams.Params.accept(self)
        print('Params')

    def visitSingleParam (self, SingleParm):
        SingleParm.ID.accept(self)
        print('ID')

    def visitAssighExp(self, AssighExp):
        AssighExp.ID.accept(self)
        print('ID')
        AssighExp.Exp.accept(self)
        print('Exp')'''

    def visitSimpleKotlinFile(self, SimpleKotlinFile):
        print(SimpleKotlinFile.functionDeclaration)
        SimpleKotlinFile.functionDeclaration.accept(self)

    def visitCompoundKotlinFile(self,CompoundKotlinFile):
        CompoundKotlinFile.functionDeclaration.accept(self)
        CompoundKotlinFile.kotlinFile.accept(self)

    def visitSimpleFunctionDeclaration(self, SimpleFunctionDeclaration):
        print('fun', end='')
        SimpleFunctionDeclaration.simpleIdentifier.accept(self)
        SimpleFunctionDeclaration.functionValueParameters.accept(self)
        SimpleFunctionDeclaration.functionBody.accept(self)

    def visitCompoundFunctionDeclaration(self, CompoundFunctionDeclaration):
        print('fun',end='')
        CompoundFunctionDeclaration.simpleIdentifier.accept(self)
        CompoundFunctionDeclaration.functionValueParameters.accept(self)
        CompoundFunctionDeclaration.type.accept(self)
        CompoundFunctionDeclaration.functionBody.accept(self)

    def visitSimpleFunctionValueParameters(self, SimpleFunctionValueParameters):
        SimpleFunctionValueParameters.accept(self)
        print('(')
        print(')')

    def visitCompoundFunctionValueParameters(self,CompoundFunctionValueParameters):
        print('(')
        CompoundFunctionValueParameters.fvps.accept(self)
        print(')')

    def visitSimpleParameters(self, SimpleParameters):
        SimpleParameters.parameter.accept(self)

    def visitCompoundParameters(self, CompoundParameters):
        CompoundParameters.parameter.accept(self)
        print(',',end='')
        CompoundParameters.parameters.accept(self)

    def visitSimpleParameter(self, SimpleParameter):
        SimpleParameter.id.accept(self)
        print(':',end='')
        SimpleParameter.type.accept(self)

    def visitCompoundParameter(self, CompoundParameter):
        CompoundParameter.id.accept(self)
        print(':',end='')
        CompoundParameter.type.accept(self)
        print('=',end='')
        CompoundParameter.expression.accept(self)

    def visitParenthesizedTypeConcrete(self,ParenthesizedTypeConcrete):
        print('(',end='')
        ParenthesizedTypeConcrete.type.accept(self)
        print(')',end='')

    def visitSimpleFunctionBody(self, SimpleFunctionBody):
        SimpleFunctionBody.block.accept(self)
    
    def visitCompoundFunctionBody(self, CompoundFunctionBody):
        print('=',emd='')
        CompoundFunctionBody.expression.accept(self)

    def visitSimpleStatements(self,SimpleStatements):
        SimpleStatements.statement.accept(self)

    def visitCompoundStatements(self,CompoundStatements):
        CompoundStatements.statement.accept(self)
        CompoundStatements.statments.accept(self)
    
    def visitIf_statement(self, If_statement):
        If_statement.statement.accept(self)
        print('if(',end='')
        If_statement.expression.accept(self)
        print(')',end='')
    
    def visitIf_block(self, If_block):
        print('if(',end='')
        If_block.expression.accept(self)
        print(')',end='')
        If_block.block.accept(self)
        
    def visitSimpleIf_else(self, SimpleIf_else):
        SimpleIf_else.block.accept(self)
        print('else',end='')
        SimpleIf_else.expression.accept(self)
        SimpleIf_else.open_statement.accept(self)

    def visitCompoundIf_else(self, CompoundIf_else):
        CompoundIf_else.closed_statement.accept(self)
        print('(',end='')
        print('in',end='')
        CompoundIf_else.expression.accept(self)
        print(')',end='')
        CompoundIf_else.open_statement.accept(self)
    
    def visitWhile_Open_statement(self, While_Open_statement):
        While_Open_statement.open_statement.accept(self)
        While_Open_statement.expression.accept(self)

    def visitDoWhile_Open_statement(self, DoWhile_Open_statement):
        DoWhile_Open_statement.open_statement.accept(self)
        DoWhile_Open_statement.expression.accept(self)
    
    def visitFor_Open_statement(self, For_Open_statement):
        For_Open_statement.genericVariableDeclaration.accept(self)
        For_Open_statement.expression.accept(self)
        For_Open_statement.open_statement.accept(self)
    
    def visitIf_Blocks_Closed_statement(self, If_Blocks_Closed_statement):
        If_Blocks_Closed_statement.block.accept(self)
        If_Blocks_Closed_statement.expression.accept(self)
        If_Blocks_Closed_statement.block1.accept(self)

    def visitIf_Mix1_Closed_statement(self, If_Mix1_Closed_statement):
        If_Mix1_Closed_statement.block.accept(self)
        If_Mix1_Closed_statement.expression.accept(self)
        If_Mix1_Closed_statement.closed_statement.accept(self)

    def visitIf_Mix2_Closed_statement(self, If_Mix2_Closed_statement):
        If_Mix2_Closed_statement.closed_statement.accept(self)
        If_Mix2_Closed_statement.expression.accept(self)
        If_Mix2_Closed_statement.block.accept(self)

    def visitIf_Closeds_Closed_statement(self, If_Closeds_Closed_statement):
        If_Closeds_Closed_statement.closed_statement.accept(self)
        If_Closeds_Closed_statement.expression.accept(self)
        If_Closeds_Closed_statement.closed_statement1.accept(self)
    
    def visitFor_Closed_statement(self,For_Closed_statement):
        For_Closed_statement.closed_statement.accept(self)
        For_Closed_statement.expression.accept(self)
        For_Closed_statement.genericVariableDeclaration.accept(self)

    def visitWhile_Closed_statement(self, While_Closed_statement):
        While_Closed_statement.closed_statement.accept(self)
        While_Closed_statement.expression.accept(self)

    def visitDoWhile_Closed_statement(self, DoWhile_Closed_statement):
        DoWhile_Closed_statement.closed_statement.accept(self)
        DoWhile_Closed_statement.expression.accept(self)

    def visitFor_Non_if_statement_block(self, For_Non_if_statement_block):
        visitFor_Non_if_statement_block.genericVariableDeclaration.accept(self)
        visitFor_Non_if_statement_block.expression.accept(self)
        visitFor_Non_if_statement_block.block.accept(self)
    
    def visitWhile_Non_if_statement_block(self, While_Non_if_statement_block):
        While_Non_if_statement_block.expression.accept(self)
        While_Non_if_statement_block.block.accept(self)

    def visitDoWhile_Non_if_statement_block(self, DoWhile_Non_if_statement_block):
        DoWhile_Non_if_statement_block.expression.accept(self)
        DoWhile_Non_if_statement_block.block.accept(self)

    def visitAssignmentConcrete(self,AssignmentConcrete):
        AssignmentConcrete.simpleIdentifier.accept(self)
        print('=',end='')
        AssignmentConcrete.expression.accept(self)
    
    def visitAssignmentAndOperatorConcrete(self,AssignmentAndOperatorConcrete):
        AssignmentAndOperatorConcrete.assignmentAndOperator.accept(self)
        AssignmentAndOperatorConcrete.expression.accept(self)
        AssignmentAndOperatorConcrete.simpleIdentifier.accept(self)
    
    def visitBlockConcrete(self, BlockConcrete):
        print('(')
        BlockConcrete.statements.accept(self)
        print(')')

    def visitPropertyDeclarationStm_Var(self ,PropertyDeclarationStm_Var):
        print('var',end='')
        PropertyDeclarationStm_Var.genericVariableDeclaration.accept(self)
        print('=',end='')
        PropertyDeclarationStm_Var.expression.accept(self)
    
    def visitPropertyDeclarationStm_Val(self, PropertyDeclarationStm_Val):
        print('val',end='')
        PropertyDeclarationStm_Val.genericVariableDeclaration.accept(self)
        print('=',end='')
        PropertyDeclarationStm_Val.expression.accept(self)

    def visitSimpleChamadaDeFuncao(self, SimpleChamadaDeFuncao):
        SimpleChamadaDeFuncao.id.accept(self)
        print('(',end='')
        print(')',end='')

    def visitCompoundChamadaDeFuncao(self, CompoundChamadaDeFuncao):
        CompoundChamadaDeFuncao.id.accept(self)
        print('(',end='')
        CompoundChamadaDeFuncao.parametersFunction.accept(self)
        print(')',end='')

    def visitVariableDeclaration(self, VariableDeclaration):
        VariableDeclaration.variableDeclaration.accept(self)

    def visitMultiVariableDeclaration(self, MultiVariableDeclaration):
        MultiVariableDeclaration.multiVariableDeclaration.accpet(self)

    def visitSimpleVariableDeclaration(self, SimpleVariableDeclaration):
        SimpleVariableDeclaration.simpleIdentifier.accept(self)

    def visitCompoundVariableDeclaration(self, CompoundVariableDeclaration):
        CompoundVariableDeclaration.simpleIdentifier.accpet(self)
        print(':',end='')
        CompoundVariableDeclaration.type.accept(self)

    def visitSimpleVariableDeclarations(self, SimpleVariableDeclarations):
        SimpleVariableDeclarations.variableDeclaration.accpet(self)

    def visitCompoundVariableDeclarations(self, CompoundVariableDeclarations):
        CompoundVariableDeclarations.variableDeclaration.accpet(self)
        print(',',end='')
        CompoundVariableDeclarations.variableDeclarations.accept(self)

    def visitSimpleMultiVariableDeclaration(self, SimpleMultiVariableDeclaration):
        SimpleMultiVariableDeclaration.accept(self)
        print('(',end='')
        print(')',end='')

    def visitCompoundMultiVariableDeclaration(self, CompoundMultiVariableDeclaration):
        print('(',end='')
        CompoundMultiVariableDeclaration.variableDeclarations.accept(self)
        print(')',end='')

    def visitSimpleParametersFunction(self, SimpleParametersFunction):
        SimpleParametersFunction.primaryExpression.accept(self)

    def visitCompoundParametersFunction(self, CompoundParametersFunction):
        CompoundParametersFunction.primaryExpression.accept(self)
        print(',',end='')
        CompoundParametersFunction.parametersFunction.accept(self)

    def visitSimpleDisjunction(self, SimpleDisjunction):
        SimpleDisjunction.conjunction.accept(self)

    def visitCompoundDisjunction(self, CompoundDisjunction):
        CompoundDisjunction.conjunction.accept(self)
        print('||',end='')
        CompoundDisjunction.disjunction.accpet(self)

    def visitSimpleConjunction(self, SimpleConjunction):
        SimpleConjunction.equality.accept(self)
    
    def visitCompoundConjunction(self, CompoundConjunction):
        CompoundConjunction.equality.accept(self)
        print('&&',end='')
        CompoundConjunction.conjunction.accept(self)

    def visitSimpleEquality(self, SimpleEquality):
        SimpleEquality.comparison.accept(self)

    def visitCompoundEquality(self, CompoundEquality):
        CompoundEquality.comparison.accept(self)
        CompoundEquality.equalityOperator.accept(self)
        CompoundEquality.equality.accept(self)

    def vistSimpleComparison(self, SimpleComparison):
        SimpleComparison.infixOperation.accpet(self)

    def vistCompoundComparison(self, CompoundComparison):
        CompoundComparison.infixOperation.accept(self)
        CompoundComparison.comparisonOperator.accept(self)
        CompoundComparison.infixOperation2.accept(self)

    def visitSimpleInfixOperation(self, SimpleInfixOperation):
        SimpleInfixOperation.infixOperation.accept(self)
        SimpleInfixOperation.inOperator.accept(self)
        SimpleInfixOperation.elvisExpression.accept(self)

    def visitCompoundInfixOperation(self, CompoundInfixOperation):
        CompoundInfixOperation.infixOperation.accept(self)
        CompoundInfixOperation.isOperator.accept(self)
        CompoundInfixOperation.type.accept(self)

    def visitSimpleElvisExpression(self, SimpleElvisExpression):
        SimpleElvisExpression.rangeExpression.accept(self)

    def visitCompoundElvisExpression(self, CompoundElvisExpression):
        CompoundElvisExpression.elvisExpression.accept(self)
        print('?:')
        CompoundElvisExpression.rangeExpression.accept(self)

    def visitSimpleRangeExpression(self, SimpleRangeExpression):
        SimpleRangeExpression.additiveExpression.accept(self)

    def visitCompoundRangeExpression(self, CompoundRangeExpression):
        CompoundRangeExpression.rangeExpression.accept(self)
        print('..')
        CompoundRangeExpression.additiveExpression.accept(self)

    def visitSimpleAdditiveExpression(self, SimpleAdditiveExpression):
        SimpleAdditiveExpression.multiplicativeExpression.accept(self)

    def visitCompoundAdditiveExpression(self, CompoundAdditiveExpression):
        CompoundAdditiveExpression.additiveExpression.accept(self)
        CompoundAdditiveExpression.additiveOperator.accept(self)
        CompoundAdditiveExpression.multiplicativeExpression.accept(self)

    def visitSimpleMultiplicativeExpression(self, SimpleMultiplicativeExpression):
        SimpleMultiplicativeExpression.asExpression.accept(self)

    def visitCompoundMultiplicativeExpression(self, CompoundMultiplicativeExpression):
        CompoundMultiplicativeExpression.multiplicativeExpression.accept(self)
        CompoundMultiplicativeExpression.multiplicativeOperator.accept(self)
        CompoundMultiplicativeExpression.asExpression.accept(self)

    def visitSimpleAsExpression(self, SimpleAsExpression):
        SimpleAsExpression.unaryExpression.accept(self)

    def visitCompoundAsExpression(self, CompoundAsExpression):
        CompoundAsExpression.unaryExpression.accept(self)
        CompoundAsExpression.asOperator.accept(self)
        CompoundAsExpression.type.accept(self)

    def visitSimpleUnaryExpressionConcrete(self, SimpleUnaryExpressionConcrete):
        SimpleUnaryExpressionConcrete.unaryOperator.accept(self)
        SimpleUnaryExpressionConcrete.primaryExpression.accept(self)

    def visitCompoundUnaryExpressionConcrete(self, UnaryExpressionConcrete):
        UnaryExpressionConcrete.primaryExpression.accept(self)
        UnaryExpressionConcrete.postfixUnaryOperator.accept(self)

    def visitReturn(self, Return):
        print('return')
        Return.expression.accept(self)

    def visitParenthesizedExpressionConcrete(self, ParenthesizedExpressionConcrete):
        print('(')
        ParenthesizedExpressionConcrete.expression.accept(self)
        print(')')

    def visitMAISIGUAL(self, MAISIGUAL):
        MAISIGUAL.maisIgual.accept(self)
        print('+=')

    def visitMENOSIGUAL(self, MENOSIGUAL):
        MENOSIGUAL.menosIgual.accept(self)
        print('-=')

    def visitMULTIGUAL(self, MULTIGUAL):
        MULTIGUAL.multiIgual.accept(self)
        print('*=')

    def visitDIVIGUAL(self, DIVIGUAL):
        DIVIGUAL.divIgual.accept(self)
        print('/=')

    def visitMODIGUAL(self, MODIGUAL):
        MODIGUAL.modIgual.accept(self)
        print('%=')

    def visitDiferente(self, Diferente):
        Diferente.diferente.accept(self)
        print('!=')

    def visitIgualdade(self, Igualdade):
        Igualdade.igualdade.accept(self)
        print('==')

    def visitIdentidade(self, Identidade):
        Identidade.identidade.accept(self)
        print('===')

    def visitSemIdentidade(self, SemIdentidade):
        SemIdentidade.semIdentidade.accept(self)
        print('!==')

    def visitMaior(self, Maior):
        Maior.maior.accept(self)
        print('>')

    def visitMenor(self, Menor):
        Menor.menor.accept(self)
        print('<')

    def visitMenorIgual(self, MenorIgual):
        MenorIgual.menorIgual.accept(self)
        print('<=')

    def visitMaiorIgual(self, MaiorIgual):
        MaiorIgual.maiorIgual.accept(self)
        print('>=')

    def visitIn(self, In):
        In.In.accept(self)
        print('in')

    def visitNotIn(self, NotIn):
        NotIn.notIn.accept(self)
        print('!in')

    def visitIs(self, Is):
        Is.Is.accept(self)
        print('is')

    def visitNotIs(self, NotIs):
        NotIs.notIs.accept(self)
        print('!is')

    def visitMult(self, Mult):
        Mult.mult.accept(self)
        print('*')

    def visitMod(self, Mod):
        Mod.mod.accept(self)
        print('%')

    def visitDivide(self, Divide):
        Divide.divide.accept(self)
        print('/')

    def visitCompoundAsOperator(self, CompoundAsOperator):
        print('as')    
        CompoundAsOperator.asOperator.accept(self)

    def visitSimpleAsOperator(self, SimpleAsOperator):
        SimpleAsOperator.accept(self)

    def visitIncremento(self, Incremento):
        Incremento.incremento.accept(self)
        print('++')

    def visitDecremento(self, Decremento):
        Decremento.decremento.accept(self)
        print('--')

    def visitMinus(self, Minus):
        Minus.minus.accept(self)
        print('-')

    def visitPlus(self, Plus):
        Plus.plus.accept(self)
        print('+')

    def visitNot(self, Not):
        Not.Not.accept(self)
        print('!')

v= Visitor()

