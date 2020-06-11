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
        SimpleKotlinFile.functionDeclaration.accept(self)

    def visitCompoundKotlinFile(self,CompoundKotlinFile):
        CompoundKotlinFile.functionDeclaration.accept(self)
        CompoundKotlinFile.kotlinFile.accept(self)

    def visitSimpleFunctionDeclaration(self, SimpleFunctionDeclaration):
        print('fun', end=' ')
        print(SimpleFunctionDeclaration.id,end=' ')
        SimpleFunctionDeclaration.functionValueParameters.accept(self)
        SimpleFunctionDeclaration.functionBody.accept(self)

    def visitCompoundFunctionDeclaration(self, CompoundFunctionDeclaration):
        print('fun',end=' ')
        print(CompoundFunctionDeclaration.id,end='')
        CompoundFunctionDeclaration.functionValueParameters.accept(self)
        print(':', end=' ')
        CompoundFunctionDeclaration.type.accept(self)
        CompoundFunctionDeclaration.functionBody.accept(self)

    def visitSimpleFunctionValueParameters(self, SimpleFunctionValueParameters):
        SimpleFunctionValueParameters.accept(self)
        print('(',end=' ')
        print(')')

    def visitCompoundFunctionValueParameters(self,CompoundFunctionValueParameters):
        print('(',end='')
        CompoundFunctionValueParameters.parameters.accept(self)
        print(')')

    def visitSimpleParameters(self, SimpleParameters):
        SimpleParameters.parameter.accept(self)

    def visitCompoundParameters(self, CompoundParameters):
        CompoundParameters.parameter.accept(self)
        print(',',end='')
        CompoundParameters.parameters.accept(self)

    def visitSimpleParameter(self, SimpleParameter):
        print(SimpleParameter.id,end=' ')
        print(':',end='')
        print(SimpleParameter.type,end='')

    def visitCompoundParameter(self, CompoundParameter):
        print(CompoundParameter.id, end='')
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
        print('=',emd=' ')
        CompoundFunctionBody.expression.accept(self)

    def visitSimpleStatements(self,SimpleStatements):
        SimpleStatements.statement.accept(self)

    def visitCompoundStatements(self,CompoundStatements):
        CompoundStatements.statement.accept(self)
        CompoundStatements.statements.accept(self)
    
    def visitIf_statement(self, If_statement):
        print('if(',end='')
        If_statement.expression.accept(self)
        print(')')
        If_statement.statement.accept(self)

    def visitIf_block(self, If_block):
        print('if(',end='')
        If_block.expression.accept(self)
        print(')',end='')
        If_block.block.accept(self)
        
    def visitSimpleIf_else(self, SimpleIf_else):
        print('if(',end='')
        SimpleIf_else.expression.accept(self)
        print(')')
        SimpleIf_else.block.accept(self)
        print('else')
        SimpleIf_else.open_statement.accept(self)

    def visitCompoundIf_else(self, CompoundIf_else):
        print('if(',end='')
        CompoundIf_else.expression.accept(self)
        print(')')
        CompoundIf_else.closed_statement.accept(self)
        print('else')
        CompoundIf_else.open_statement.accept(self)
    
    def visitWhile_Open_statement(self, While_Open_statement):
        print('while (', end= '')
        While_Open_statement.expression.accept(self)
        print(')')
        While_Open_statement.open_statement.accept(self)

    def visitDoWhile_Open_statement(self, DoWhile_Open_statement):
        print('do')
        DoWhile_Open_statement.open_statement.accept(self)
        print('while(', end='')
        DoWhile_Open_statement.expression.accept(self)
        print(')')
    
    def visitFor_Open_statement(self, For_Open_statement):
        print('for (', end='')
        For_Open_statement.genericVariableDeclaration.accept(self)
        print('in')
        For_Open_statement.expression.accept(self)
        print(')')
        For_Open_statement.open_statement.accept(self)

    def visitIf_Blocks_Closed_statement(self, If_Blocks_Closed_statement):
        print('if (', end='')
        If_Blocks_Closed_statement.expression.accept(self)
        print(')')
        If_Blocks_Closed_statement.block.accept(self)
        print('else')
        If_Blocks_Closed_statement.block1.accept(self)

    def visitIf_Mix1_Closed_statement(self, If_Mix1_Closed_statement):
        print('if (', end='')
        If_Mix1_Closed_statement.expression.accept(self)
        print(')')
        If_Mix1_Closed_statement.block.accept(self)
        print('else')
        If_Mix1_Closed_statement.closed_statement.accept(self)

    def visitIf_Mix2_Closed_statement(self, If_Mix2_Closed_statement):
        print('if (', end= '')
        If_Mix2_Closed_statement.expression.accept(self)
        print(')')
        If_Mix2_Closed_statement.closed_statement.accept(self)
        print('else')
        If_Mix2_Closed_statement.block.accept(self)

    def visitIf_Closeds_Closed_statement(self, If_Closeds_Closed_statement):
        print('if (', end= '')
        If_Closeds_Closed_statement.expression.accept(self)
        print(')')
        If_Closeds_Closed_statement.closed_statement.accept(self)
        print('else')
        If_Closeds_Closed_statement.closed_statement1.accept(self)
    
    def visitFor_Closed_statement(self,For_Closed_statement):
        print('for (', end='')
        For_Closed_statement.genericVariableDeclaration.accept(self)
        print('in')
        For_Closed_statement.expression.accept(self)
        print(')')
        For_Closed_statement.closed_statement.accept(self)

    def visitWhile_Closed_statement(self, While_Closed_statement):
        print('while (', end='')
        While_Closed_statement.expression.accept(self)
        print(')')
        While_Closed_statement.closed_statement.accept(self)

    def visitDoWhile_Closed_statement(self, DoWhile_Closed_statement):
        print('do')
        DoWhile_Closed_statement.closed_statement.accept(self)
        print('while (', end='')
        DoWhile_Closed_statement.expression.accept(self)
        print(')')

    def visitFor_Non_if_statement_block(self, For_Non_if_statement_block):
        print('for (', end='')
        For_Non_if_statement_block.genericVariableDeclaration.accept(self)
        print('in', end=' ')
        For_Non_if_statement_block.expression.accept(self)
        print(')')
        For_Non_if_statement_block.block.accept(self)
    
    def visitWhile_Non_if_statement_block(self, While_Non_if_statement_block):
        print('while (', end='')
        While_Non_if_statement_block.expression.accept(self)
        print(')')
        While_Non_if_statement_block.block.accept(self)

    def visitDoWhile_Non_if_statement_block(self, DoWhile_Non_if_statement_block):
        print('do')
        DoWhile_Non_if_statement_block.block.accept(self)
        print('while (', end='')
        DoWhile_Non_if_statement_block.expression.accept(self)
        print(')')


    def visitAssignmentConcrete(self,AssignmentConcrete):
        print(AssignmentConcrete.id, end=' ')
        print('=',end=' ')
        AssignmentConcrete.expression.accept(self)
    
    def visitAssignmentAndOperatorConcrete(self,AssignmentAndOperatorConcrete):
        print(AssignmentAndOperatorConcrete.id, end=' ')
        AssignmentAndOperatorConcrete.assignmentAndOperator.accept(self)
        AssignmentAndOperatorConcrete.expression.accept(self)

    def visitBlockConcrete(self, BlockConcrete):
        print('{')
        BlockConcrete.statements.accept(self)
        print('}')

    def visitPropertyDeclarationStm_Var(self, PropertyDeclarationStm_Var):
        print('var',end=' ')
        PropertyDeclarationStm_Var.genericVariableDeclaration.accept(self)
        print('=',end=' ')
        PropertyDeclarationStm_Var.expression.accept(self)
    
    def visitPropertyDeclarationStm_Val(self, PropertyDeclarationStm_Val):
        print('val',end=' ')
        PropertyDeclarationStm_Val.genericVariableDeclaration.accept(self)
        print('=',end=' ')
        PropertyDeclarationStm_Val.expression.accept(self)

    def visitSimpleChamadaDeFuncao(self, SimpleChamadaDeFuncao):
        print(SimpleChamadaDeFuncao.id, end='')
        print('(',end='')
        print(')')

    def visitCompoundChamadaDeFuncao(self, CompoundChamadaDeFuncao):
        print(CompoundChamadaDeFuncao.id, end='')
        print('(',end='')
        CompoundChamadaDeFuncao.parametersFunction.accept(self)
        print(')')

    def visitVariableDeclaration(self, VariableDeclaration):
        VariableDeclaration.variableDeclaration.accept(self)

    def visitMultiVariableDeclaration(self, MultiVariableDeclaration):
        MultiVariableDeclaration.multiVariableDeclaration.accpet(self)

    def visitSimpleVariableDeclaration(self, SimpleVariableDeclaration):
        print(SimpleVariableDeclaration.id, end=' ')

    def visitCompoundVariableDeclaration(self, CompoundVariableDeclaration):
        print(CompoundVariableDeclaration.id, end=' ')
        print(':',end=' ')
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
        print(SimpleParametersFunction.primaryExpression, end=' ')

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

    def visitSimpleComparison(self, SimpleComparison):
        print(SimpleComparison.infixOperation)

    def visitCompoundComparison(self, CompoundComparison):
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
        print(MAISIGUAL.maisIgual, end=' ')

    def visitMENOSIGUAL(self, MENOSIGUAL):
        print(MENOSIGUAL.menosIgual, end=' ')

    def visitMULTIGUAL(self, MULTIGUAL):
        print(MULTIGUAL.multiIgual, end=' ')


    def visitDIVIGUAL(self, DIVIGUAL):
        print(DIVIGUAL.divIgual, end=' ')


    def visitMODIGUAL(self, MODIGUAL):
        print(MODIGUAL.modIgual, end=' ')


    def visitDiferente(self, Diferente):
        print(Diferente.diferente, end=' ')

    def visitIgualdade(self, Igualdade):
        print(Igualdade.igualdade, end=' ')

    def visitIdentidade(self, Identidade):
        print(Identidade.identidade, end=' ')

    def visitSemIdentidade(self, SemIdentidade):
        print(SemIdentidade.semIdentidade, end=' ')

    def visitMaior(self, Maior):
        print(Maior.maior, end=' ')

    def visitMenor(self, Menor):
        print(Menor.menor, end=' ')

    def visitMenorIgual(self, MenorIgual):
        print(MenorIgual.menorIgual, end=' ')

    def visitMaiorIgual(self, MaiorIgual):
        print(MaiorIgual.maiorIgual, end=' ')

    def visitIn(self, In):
        print(In.IN, end=' ')

    def visitNotIn(self, NotIn):
        print(NotIn.notIn, end=' ')

    def visitIs(self, Is):
        print(Is.IS, end=' ')

    def visitNotIs(self, NotIs):
        print(NotIs.NotIs, end=' ')

    def visitMult(self, Mult):
        print(Mult.mult, end=' ')

    def visitMod(self, Mod):
        print(Mod.mod, end=' ')

    def visitDivide(self, Divide):
        print(Divide.divide, end=' ')

    def visitCompoundAsOperator(self, CompoundAsOperator):
        print('as', end=' ')
        CompoundAsOperator.asOperator.accept(self)

    def visitSimpleAsOperator(self, SimpleAsOperator):
        SimpleAsOperator.accept(self)

    def visitIncremento(self, Incremento):
        print(Incremento.incremento, end=' ')

    def visitDecremento(self, Decremento):
        print(Decremento.decremento, end=' ')

    def visitMinus(self, Minus):
        print(Minus.minus, end=' ')

    def visitPlus(self, Plus):
        print(Plus.plus, end=' ')

    def visitNot(self, Not):
        print(Not.NOT, end=' ')

v= Visitor()

