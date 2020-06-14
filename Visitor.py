from AbstractVisitor import AbstractVisitor

types = [int, str, float, bool]

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
        print(SimpleFunctionDeclaration.id, end=' ')
        SimpleFunctionDeclaration.functionValueParameters.accept(self)
        SimpleFunctionDeclaration.functionBody.accept(self)


    def visitCompoundFunctionDeclaration(self, CompoundFunctionDeclaration):
        print('fun',end=' ')
        print(CompoundFunctionDeclaration.id, end='')
        CompoundFunctionDeclaration.functionValueParameters.accept(self)
        print(':', end=' ')

        if type(CompoundFunctionDeclaration.type) in types:
            print(CompoundFunctionDeclaration.type, end='')
        else:
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
        if type(SimpleParameters.parameter) in types:
            print(SimpleParameters.parameter, end='')
        else:
            SimpleParameters.parameter.accept(self)


    def visitCompoundParameters(self, CompoundParameters):
        if type(CompoundParameters.parameter) in types:
            print(CompoundParameters.parameter, end='')
        else:
            CompoundParameters.parameter.accept(self)

        print(',',end='')

        if type(CompoundParameters.parameters) in types:
            print(CompoundParameters.parameters, end='')
        else:
            CompoundParameters.parameters.accept(self)


    def visitSimpleParameter(self, SimpleParameter):
        print(SimpleParameter.id,end=' ')
        print(':',end='')

        if type(SimpleParameter.type) in types:
            print(SimpleParameter.type,end='')
        else:
            SimpleParameter.type.accept(self)


    def visitCompoundParameter(self, CompoundParameter):
        print(CompoundParameter.id, end='')
        print(':',end='')

        if type(CompoundParameter.type) in types:
            print(CompoundParameter.type,end='')
        else:
            CompoundParameter.type.accept(self)

        print('=',end='')

        if type(CompoundParameter.expression) in types:
            print(CompoundParameter.expression,end='')
        else:
            CompoundParameter.expression.accept(self)


    def visitParenthesizedTypeConcrete(self,ParenthesizedTypeConcrete):
        print('(',end='')

        if type(ParenthesizedTypeConcrete.type) in types:
            print(ParenthesizedTypeConcrete.type,end='')
        else:
            ParenthesizedTypeConcrete.type.accept(self)

        print(')',end='')


    def visitSimpleFunctionBody(self, SimpleFunctionBody):
        SimpleFunctionBody.block.accept(self)
    

    def visitCompoundFunctionBody(self, CompoundFunctionBody):
        print('=',end=' ')

        if type(CompoundFunctionBody.expression) in types:
            print(CompoundFunctionBody.expression,end='')
        else:
            CompoundFunctionBody.expression.accept(self)


    def visitSimpleStatements(self,SimpleStatements):
        SimpleStatements.statement.accept(self)


    def visitCompoundStatements(self,CompoundStatements):
        CompoundStatements.statement.accept(self)
        CompoundStatements.statements.accept(self)


    def visitIf_statement(self, If_statement):
        print('if(',end='')

        if type(If_statement.expression) in types:
            print(If_statement.expression, end='')
        else:
            If_statement.expression.accept(self)

        print(')')
        If_statement.statement.accept(self)


    def visitIf_block(self, If_block):
        print('if(',end='')

        if type(If_block.expression) in types:
            print(If_block.expression, end='')
        else:
            If_block.expression.accept(self)

        print(')',end='')
        If_block.block.accept(self)
        

    def visitSimpleIf_else(self, SimpleIf_else):
        print('if(',end='')

        if type(SimpleIf_else.expression) in types:
            print(SimpleIf_else.expression, end='')
        else:
            SimpleIf_else.expression.accept(self)

        print(')')
        SimpleIf_else.block.accept(self)
        print('else')
        SimpleIf_else.open_statement.accept(self)


    def visitCompoundIf_else(self, CompoundIf_else):
        print('if(',end='')

        if type(CompoundIf_else.expression) in types:
            print(CompoundIf_else.expression, end='')
        else:
            CompoundIf_else.expression.accept(self)

        print(')')
        CompoundIf_else.closed_statement.accept(self)
        print('else')
        CompoundIf_else.open_statement.accept(self)
    

    def visitWhile_Open_statement(self, While_Open_statement):
        print('while (', end= '')

        if type(While_Open_statement.expression) in types:
            print(While_Open_statement.expression, end='')
        else:
            While_Open_statement.expression.accept(self)

        print(')')
        While_Open_statement.open_statement.accept(self)


    def visitDoWhile_Open_statement(self, DoWhile_Open_statement):
        print('do')
        DoWhile_Open_statement.open_statement.accept(self)
        print('while(', end='')

        if type(DoWhile_Open_statement.expression) in types:
            print(DoWhile_Open_statement.expression, end='')
        else:
            DoWhile_Open_statement.expression.accept(self)

        print(')')


    def visitFor_Open_statement(self, For_Open_statement):
        print('for (', end='')
        For_Open_statement.genericVariableDeclaration.accept(self)
        print('in')

        if type(For_Open_statement.expression) in types:
            print(For_Open_statement.expression, end='')
        else:
            For_Open_statement.expression.accept(self)

        print(')')
        For_Open_statement.open_statement.accept(self)


    def visitIf_Blocks_Closed_statement(self, If_Blocks_Closed_statement):
        print('if (', end='')

        if type(If_Blocks_Closed_statement.expression) in types:
            print(If_Blocks_Closed_statement.expression, end='')
        else:
            If_Blocks_Closed_statement.expression.accept(self)

        print(')')
        If_Blocks_Closed_statement.block.accept(self)
        print('else')
        If_Blocks_Closed_statement.block1.accept(self)


    def visitIf_Mix1_Closed_statement(self, If_Mix1_Closed_statement):
        print('if (', end='')

        if type(If_Mix1_Closed_statement.expression) in types:
            print(If_Mix1_Closed_statement.expression, end='')
        else:
            If_Mix1_Closed_statement.expression.accept(self)

        print(')')
        If_Mix1_Closed_statement.block.accept(self)
        print('else')
        If_Mix1_Closed_statement.closed_statement.accept(self)


    def visitIf_Mix2_Closed_statement(self, If_Mix2_Closed_statement):
        print('if (', end= '')

        if type(If_Mix2_Closed_statement.expression) in types:
            print(If_Mix2_Closed_statement.expression, end='')
        else:
            If_Mix2_Closed_statement.expression.accept(self)

        print(')')
        If_Mix2_Closed_statement.closed_statement.accept(self)
        print('else')
        If_Mix2_Closed_statement.block.accept(self)


    def visitIf_Closeds_Closed_statement(self, If_Closeds_Closed_statement):
        print('if (', end= '')

        if type(If_Closeds_Closed_statement.expression) in types:
            print(If_Closeds_Closed_statement.expression, end='')
        else:
            If_Closeds_Closed_statement.expression.accept(self)

        print(')')
        If_Closeds_Closed_statement.closed_statement.accept(self)
        print('else')
        If_Closeds_Closed_statement.closed_statement1.accept(self)
    

    def visitFor_Closed_statement(self,For_Closed_statement):
        print('for (', end='')
        For_Closed_statement.genericVariableDeclaration.accept(self)
        print('in')

        if type(For_Closed_statement.expression) in types:
            print(For_Closed_statement.expression, end='')
        else:
            For_Closed_statement.expression.accept(self)

        print(')')
        For_Closed_statement.closed_statement.accept(self)


    def visitWhile_Closed_statement(self, While_Closed_statement):
        print('while (', end='')

        if type(While_Closed_statement.expression) in types:
            print(While_Closed_statement.expression, end='')
        else:
            While_Closed_statement.expression.accept(self)

        print(')')
        While_Closed_statement.closed_statement.accept(self)


    def visitDoWhile_Closed_statement(self, DoWhile_Closed_statement):
        print('do')
        DoWhile_Closed_statement.closed_statement.accept(self)
        print('while (', end='')

        if type(DoWhile_Closed_statement.expression) in types:
            print(DoWhile_Closed_statement.expression, end='')
        else:
            DoWhile_Closed_statement.expression.accept(self)

        print(')')


    def visitFor_Non_if_statement_block(self, For_Non_if_statement_block):
        print('for (', end='')

        if type(For_Non_if_statement_block.genericVariableDeclaration) in types:
            print(For_Non_if_statement_block.genericVariableDeclaration, end=' ')
        else:
            For_Non_if_statement_block.genericVariableDeclaration.accept(self)

        print('in', end=' ')

        if type(For_Non_if_statement_block.expression) in types:
            print(For_Non_if_statement_block.expression, end=' ')
        else:
            For_Non_if_statement_block.expression.accept(self)

        print(')')
        For_Non_if_statement_block.block.accept(self)
    

    def visitWhile_Non_if_statement_block(self, While_Non_if_statement_block):
        print('while (', end='')

        if type(While_Non_if_statement_block.expression) in types:
            print(While_Non_if_statement_block.expression, end='')
        else:
            While_Non_if_statement_block.expression.accept(self)

        print(')')
        While_Non_if_statement_block.block.accept(self)


    def visitDoWhile_Non_if_statement_block(self, DoWhile_Non_if_statement_block):
        print('do')
        DoWhile_Non_if_statement_block.block.accept(self)
        print('while (', end='')

        if type(DoWhile_Non_if_statement_block.expression) in types:
            print(DoWhile_Non_if_statement_block.expression, end='')
        else:
            DoWhile_Non_if_statement_block.expression.accept(self)

        print(')')


    def visitAssignmentConcrete(self,AssignmentConcrete):
        print(AssignmentConcrete.id, end=' ')
        print('=',end=' ')

        if type(AssignmentConcrete.expression) in types:
            print(AssignmentConcrete.expression, end='')
        else:
            AssignmentConcrete.expression.accept(self)
    

    def visitAssignmentAndOperatorConcrete(self,AssignmentAndOperatorConcrete):
        print(AssignmentAndOperatorConcrete.id, end=' ')
        AssignmentAndOperatorConcrete.assignmentAndOperator.accept(self)

        if type(AssignmentAndOperatorConcrete.expression) in types:
            print(AssignmentAndOperatorConcrete.expression)
        else:
            AssignmentAndOperatorConcrete.expression.accept(self)


    def visitBlockConcrete(self, BlockConcrete):
        print('{')
        BlockConcrete.statements.accept(self)
        print('}')


    def visitPropertyDeclarationStm_Var(self, PropertyDeclarationStm_Var):
        print('var',end=' ')

        if type(PropertyDeclarationStm_Var.genericVariableDeclaration) in types:
            print(PropertyDeclarationStm_Var.genericVariableDeclaration, end=' ')
        else:
            PropertyDeclarationStm_Var.genericVariableDeclaration.accept(self)

        print('=', end=' ')

        if type(PropertyDeclarationStm_Var.expression) in types:
            print(PropertyDeclarationStm_Var.expression)
        else:
            PropertyDeclarationStm_Var.expression.accept(self)


    def visitPropertyDeclarationStm_Val(self, PropertyDeclarationStm_Val):
        print('val',end=' ')

        if type(PropertyDeclarationStm_Val.genericVariableDeclaration) in types:
            print(PropertyDeclarationStm_Val.genericVariableDeclaration, end=' ')
        else:
            PropertyDeclarationStm_Val.genericVariableDeclaration.accept(self)

        print('=',end=' ')

        if type(PropertyDeclarationStm_Val.expression) in types:
            print(PropertyDeclarationStm_Val.expression)
        else:
            PropertyDeclarationStm_Val.expression.accept(self)


    def visitSimpleChamadaDeFuncao(self, SimpleChamadaDeFuncao):
        print(SimpleChamadaDeFuncao.id, end='')
        print('(',end=' ')
        print(')')


    def visitCompoundChamadaDeFuncao(self, CompoundChamadaDeFuncao):
        print(CompoundChamadaDeFuncao.id, end='')
        print('(',end='')
 
        if type(CompoundChamadaDeFuncao.parametersFunction) in types:
            print(CompoundChamadaDeFuncao.parametersFunction, end='')
        else:
            CompoundChamadaDeFuncao.parametersFunction.accept(self)
 
        print(')')

 
    def visitVariableDeclaration(self, VariableDeclaration):
        VariableDeclaration.variableDeclaration.accept(self)

 
    def visitMultiVariableDeclaration(self, MultiVariableDeclaration):
        MultiVariableDeclaration.multiVariableDeclaration.accept(self)


    def visitSimpleVariableDeclaration(self, SimpleVariableDeclaration):
        print(SimpleVariableDeclaration.id, end=' ')


    def visitCompoundVariableDeclaration(self, CompoundVariableDeclaration):
        print(CompoundVariableDeclaration.id, end=' ')
        print(':',end=' ')
        if type() in types:
            print(CompoundVariableDeclaration.type, end='')
        else:
            CompoundVariableDeclaration.type.accept(self)


    def visitSimpleVariableDeclarations(self, SimpleVariableDeclarations):
        SimpleVariableDeclarations.variableDeclaration.accept(self)


    def visitCompoundVariableDeclarations(self, CompoundVariableDeclarations):
        CompoundVariableDeclarations.variableDeclaration.accept(self)
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
        if type(SimpleParametersFunction.primaryExpression) in types:
            print(SimpleParametersFunction.primaryExpression)
        else:
            SimpleParametersFunction.primaryExpression.accept(self)


    def visitCompoundParametersFunction(self, CompoundParametersFunction):
        CompoundParametersFunction.primaryExpression.accept(self)
        print(',',end='')
        CompoundParametersFunction.parametersFunction.accept(self)


    def visitSimpleDisjunction(self, SimpleDisjunction):
        if type(SimpleDisjunction.conjunction) in types:
            print(SimpleDisjunction.conjunction, end='')
        else:
            SimpleDisjunction.conjunction.accept(self)


    def visitCompoundDisjunction(self, CompoundDisjunction):
        if type(CompoundDisjunction.conjunction) in types:
            print(CompoundDisjunction.conjunction, end='')
        else:
            CompoundDisjunction.conjunction.accept(self)        
        
        print('||',end='')
        
        if type(CompoundDisjunction.conjunction) in types:
            print(CompoundDisjunction.conjunction, end='')
        else:
            CompoundDisjunction.conjunction.accept(self)


    def visitSimpleConjunction(self, SimpleConjunction):
        SimpleConjunction.equality.accept(self)


    def visitCompoundConjunction(self, CompoundConjunction):
        if type(CompoundConjunction.equality) in types:
            print(CompoundConjunction.equality, end='')
        else:
            CompoundConjunction.equality.accept(self)        
                
        print('&&',end='')

        if type(CompoundConjunction.conjunction) in types:
            print(CompoundConjunction.conjunction, end='')
        else:
            CompoundConjunction.conjunction.accept(self)   

  
    def visitSimpleEquality(self, SimpleEquality):
        SimpleEquality.comparison.accept(self)


    def visitCompoundEquality(self, CompoundEquality):
        if type(CompoundEquality.comparison) in types:
            print(CompoundEquality.comparison ,end=' ')
        else:
            CompoundEquality.comparison.accept(self)

        if type(CompoundEquality.equalityOperator) in types:
            print(CompoundEquality.equalityOperator, end=' ')
        else:
            CompoundEquality.equalityOperator.accept(self)
        
        if type(CompoundEquality.equality) in types:
            print(CompoundEquality.equality)
        else:
            CompoundEquality.equality.accept(self)


    def visitSimpleComparison(self, SimpleComparison):
        print(SimpleComparison.infixOperation)


    def visitCompoundComparison(self, CompoundComparison):
        if type(CompoundComparison.infixOperation) in types:
            print(CompoundComparison.infixOperation, end=' ')
        else:
            CompoundComparison.infixOperation.accept(self)
        
        if type(CompoundComparison.comparisonOperator) in types:
            print(CompoundComparison.comparisonOperator, end=' ')
        else:
            CompoundComparison.comparisonOperator.accept(self)
        
        if type(CompoundComparison.infixOperation2) in types:
            print(CompoundComparison.infixOperation2)
        else:
            CompoundComparison.infixOperation2.accept(self)


    def visitSimpleInfixOperation(self, SimpleInfixOperation):
        if type(SimpleInfixOperation.infixOperation) in types:
            print(SimpleInfixOperation.infixOperation, end=' ')
        else:
            SimpleInfixOperation.infixOperation.accept(self)
        
        if(SimpleInfixOperation.inOperator) in types:
            print(SimpleInfixOperation.inOperator, end=' ')
        else:
            SimpleInfixOperation.inOperator.accept(self)
        
        if type(SimpleInfixOperation.elvisExpression) in types:
            print(SimpleInfixOperation.elvisExpression)
        else:
            SimpleInfixOperation.elvisExpression.accept(self)


    def visitCompoundInfixOperation(self, CompoundInfixOperation):
        if type(CompoundInfixOperation.infixOperation) in types:
            print(CompoundInfixOperation.infixOperation, end=' ')
        else:
            CompoundInfixOperation.infixOperation.accept(self)
        
        if(CompoundInfixOperation.isOperator) in types:
            print(CompoundInfixOperation.isOperator, end=' ')
        else:
            CompoundInfixOperation.isOperator.accept(self)
        
        if type(CompoundInfixOperation.type) in types:
            print(CompoundInfixOperation.type)
        else:
            CompoundInfixOperation.type.accept(self)


    def visitSimpleElvisExpression(self, SimpleElvisExpression):
        SimpleElvisExpression.rangeExpression.accept(self)


    def visitCompoundElvisExpression(self, CompoundElvisExpression):
        if type(CompoundElvisExpression.elvisExpression) in types:
            print(CompoundElvisExpression.elvisExpression, end=' ')
        else:
            CompoundElvisExpression.elvisExpression.accept(self)
        
        print('?:')
        
        if type(CompoundElvisExpression.rangeExpression) in types:
            print(CompoundElvisExpression.rangeExpression)
        else:
            CompoundElvisExpression.rangeExpression.accept(self)


    def visitSimpleRangeExpression(self, SimpleRangeExpression):
        SimpleRangeExpression.additiveExpression.accept(self)


    def visitCompoundRangeExpression(self, CompoundRangeExpression):
        if type(CompoundRangeExpression.additiveExpression) in types:
            print(CompoundRangeExpression.additiveExpression, end='')
        else:
            CompoundRangeExpression.additiveExpression.accept(self)

        print('..', end='')

        if type(CompoundRangeExpression.rangeExpression) in types:
            print(CompoundRangeExpression.rangeExpression, end='')
        else:
            CompoundRangeExpression.rangeExpression.accept(self)


    def visitSimpleAdditiveExpression(self, SimpleAdditiveExpression):
        SimpleAdditiveExpression.multiplicativeExpression.accept(self)


    def visitCompoundAdditiveExpression(self, CompoundAdditiveExpression):
        if(CompoundAdditiveExpression.additiveExpression) in types:
            print(CompoundAdditiveExpression.additiveExpression, end=' ')
        else:
            CompoundAdditiveExpression.additiveExpression.accept(self)
        
        if type(CompoundAdditiveExpression.additiveOperator) in types:
            print(CompoundAdditiveExpression.additiveOperator, end=' ')
        else:
            CompoundAdditiveExpression.additiveOperator.accept(self)
        
        if type(CompoundAdditiveExpression.multiplicativeExpression) in types:
            print(CompoundAdditiveExpression.multiplicativeExpression)
        else:
            CompoundAdditiveExpression.multiplicativeExpression.accept(self)


    def visitSimpleMultiplicativeExpression(self, SimpleMultiplicativeExpression):
        SimpleMultiplicativeExpression.asExpression.accept(self)


    def visitCompoundMultiplicativeExpression(self, CompoundMultiplicativeExpression):
        if type(CompoundMultiplicativeExpression.multiplicativeExpression) in types:
            print(CompoundMultiplicativeExpression.multiplicativeExpression, end=' ')
        else:
            CompoundMultiplicativeExpression.multiplicativeExpression.accept(self)
        
        if type(CompoundMultiplicativeExpression.multiplicativeOperator) in types:
            print(CompoundMultiplicativeExpression.multiplicativeOperator, end=' ')
        else:
            CompoundMultiplicativeExpression.multiplicativeOperator.accept(self)
        
        if type(CompoundMultiplicativeExpression.asExpression) in types:
            print(CompoundMultiplicativeExpression.asExpression)
        else:
            CompoundMultiplicativeExpression.asExpression.accept(self)


    def visitSimpleAsExpression(self, SimpleAsExpression):
        SimpleAsExpression.unaryExpression.accept(self)


    def visitCompoundAsExpression(self, CompoundAsExpression):
        if type(CompoundAsExpression.unaryExpression) in types:
            print(CompoundAsExpression.unaryExpression, end=' ')
        else:
            CompoundAsExpression.unaryExpression.accept(self)
        
        if type(CompoundAsExpression.asOperator) in types:
            print(CompoundAsExpression.asOperator, end=' ')
        else:
            CompoundAsExpression.asOperator.accept(self)

        if type(CompoundAsExpression.type) in types:
            print(CompoundAsExpression.type)
        else:
            CompoundAsExpression.type.accept(self)


    def visitSimpleUnaryExpressionConcrete(self, SimpleUnaryExpressionConcrete):
        if type(SimpleUnaryExpressionConcrete.unaryOperator) in types:
            print(SimpleUnaryExpressionConcrete.unaryOperator, end= '')
        else:
            SimpleUnaryExpressionConcrete.unaryOperator.accept(self)
        
        if type(SimpleUnaryExpressionConcrete.primaryExpression) in types:
            print(SimpleUnaryExpressionConcrete.primaryExpression)
        else:
            SimpleUnaryExpressionConcrete.primaryExpression.accept(self)


    def visitCompoundUnaryExpressionConcrete(self, UnaryExpressionConcrete):
        if type(UnaryExpressionConcrete.primaryExpression) in types:
            print(UnaryExpressionConcrete.primaryExpression, end=' ')
        else:
            UnaryExpressionConcrete.primaryExpression.accept(self)
        
        if type(UnaryExpressionConcrete.postfixUnaryOperator) in types:
            print(UnaryExpressionConcrete.postfixUnaryOperator)
        else:
            UnaryExpressionConcrete.postfixUnaryOperator.accept(self)


    def visitReturn(self, Return):
        print('return')

        if type(Return.expression) in types:
            print(Return.expression, end='')
        else:
            Return.expression.accept(self)


    def visitParenthesizedExpressionConcrete(self, ParenthesizedExpressionConcrete):
        print('(')

        if type(ParenthesizedExpressionConcrete.expression) in types:
            print(ParenthesizedExpressionConcrete.expression, end='')
        else:
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
        if type(CompoundAsOperator.asOperator) in types:
            print(CompoundAsOperator.asOperator)
        else:
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
