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

    # def visitSimpleKotlinFile(self, SimpleKotlinFile):
    #     SimpleKotlinFile.functionDeclaration.accept(self)


    def visitKotlinFileConcrete(self,KotlinFile):
        KotlinFile.functionDeclaration.accept(self)
        KotlinFile.kotlinFile.accept(self)


    def visitFunctionDeclarationNoType(self, FunctionDeclaration):
        print('fun', end=' ')
        print(FunctionDeclaration.id, end=' ')
        FunctionDeclaration.functionValueParameters.accept(self)
        FunctionDeclaration.functionBody.accept(self)


    def visitFunctionDeclarationConcrete(self, FunctionDeclaration):
        print('fun',end=' ')
        print(FunctionDeclaration.id, end='')
        FunctionDeclaration.functionValueParameters.accept(self)
        print(':', end=' ')

        if type(FunctionDeclaration.type) in types:
            print(FunctionDeclaration.type, end='')
        else:
            FunctionDeclaration.type.accept(self)

        FunctionDeclaration.functionBody.accept(self)


    def visitFunctionValueParametersNoParams(self, FunctionValueParameters):
        FunctionValueParameters.accept(self)
        print('(',end=' ')
        print(')')


    def visitFunctionValueParametersConcrete(self,FunctionValueParameters):
        print('(',end='')
        FunctionValueParameters.parameters.accept(self)
        print(')')


    # def visitSimpleParameters(self, SimpleParameters):
    #     if type(SimpleParameters.parameter) in types:
    #         print(SimpleParameters.parameter, end='')
    #     else:
    #         SimpleParameters.parameter.accept(self)


    def visitParametersConcrete(self, Parameters):
        if type(Parameters.parameter) in types:
            print(Parameters.parameter, end='')
        else:
            Parameters.parameter.accept(self)

        print(',',end='')

        if type(Parameters.parameters) in types:
            print(Parameters.parameters, end='')
        else:
            Parameters.parameters.accept(self)


    def visitParameterConcrete(self, Parameter):
        print(Parameter.id,end=' ')
        print(':',end='')

        if type(Parameter.type) in types:
            print(Parameter.type,end='')
        else:
            Parameter.type.accept(self)


    # def visitCompoundParameter(self, CompoundParameter):
    #     print(CompoundParameter.id, end='')
    #     print(':',end='')
    #
    #     if type(CompoundParameter.type) in types:
    #         print(CompoundParameter.type,end='')
    #     else:
    #         CompoundParameter.type.accept(self)
    #
    #     print('=',end='')
    #
    #     if type(CompoundParameter.expression) in types:
    #         print(CompoundParameter.expression,end='')
    #     else:
    #         CompoundParameter.expression.accept(self)


    def visitParenthesizedTypeConcrete(self,ParenthesizedType):
        print('(',end='')

        if type(ParenthesizedType.type) in types:
            print(ParenthesizedType.type,end='')
        else:
            ParenthesizedType.type.accept(self)

        print(')',end='')


    # def visitSimpleFunctionBody(self, SimpleFunctionBody):
    #     SimpleFunctionBody.block.accept(self)
    

    def visitFunctionBodyConcrete(self, FunctionBody):
        print('=',end=' ')

        if type(FunctionBody.expression) in types:
            print(FunctionBody.expression,end='')
        else:
            FunctionBody.expression.accept(self)


    # def visitSimpleStatements(self,SimpleStatements):
    #     SimpleStatements.statement.accept(self)


    def visitStatementsConcrete(self,Statements):
        Statements.statement.accept(self)
        Statements.statements.accept(self)


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


    def visitAssignmentConcrete(self,Assignment):
        print(Assignment.id, end=' ')
        print('=',end=' ')

        if type(Assignment.expression) in types:
            print(Assignment.expression, end='')
        else:
            Assignment.expression.accept(self)
    

    def visitAssignmentAndOperatorConcrete(self,AssignmentAndOperator):
        print(AssignmentAndOperator.id, end=' ')
        AssignmentAndOperator.assignmentAndOperator.accept(self)

        if type(AssignmentAndOperator.expression) in types:
            print(AssignmentAndOperator.expression)
        else:
            AssignmentAndOperator.expression.accept(self)


    def visitBlockConcrete(self, Block):
        print('{')
        Block.statements.accept(self)
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


    def visitChamadaDeFuncaoNoParams(self, ChamadaDeFuncao):
        print(ChamadaDeFuncao.id, end='')
        print('(',end=' ')
        print(')')


    def visitChamadaDeFuncaoConcrete(self, ChamadaDeFuncao):
        print(ChamadaDeFuncao.id, end='')
        print('(',end='')
 
        if type(ChamadaDeFuncao.parametersFunction) in types:
            print(ChamadaDeFuncao.parametersFunction, end='')
        else:
            ChamadaDeFuncao.parametersFunction.accept(self)
 
        print(')')

 
    # def visitVariableDeclaration(self, VariableDeclaration):
    #     VariableDeclaration.variableDeclaration.accept(self)
    #
    #
    # def visitMultiVariableDeclaration(self, MultiVariableDeclaration):
    #     MultiVariableDeclaration.multiVariableDeclaration.accept(self)


    # def visitSimpleVariableDeclaration(self, SimpleVariableDeclaration):
    #     print(SimpleVariableDeclaration.id, end=' ')


    def visitVariableDeclarationConcrete(self, VariableDeclaration):
        print(VariableDeclaration.id, end=' ')
        print(':',end=' ')
        if type() in types:
            print(VariableDeclaration.type, end='')
        else:
            VariableDeclaration.type.accept(self)


    # def visitSimpleVariableDeclarations(self, SimpleVariableDeclarations):
    #     SimpleVariableDeclarations.variableDeclaration.accept(self)


    def visitVariableDeclarationsConcrete(self, VariableDeclarations):
        VariableDeclarations.variableDeclaration.accept(self)
        print(',',end='')
        VariableDeclarations.variableDeclarations.accept(self)


    def visitMultiVariableDeclarationNone(self, MultiVariableDeclaration):
        MultiVariableDeclaration.accept(self)
        print('(',end='')
        print(')',end='')


    def visitMultiVariableDeclarationConcrete(self, MultiVariableDeclaration):
        print('(',end='')
        MultiVariableDeclaration.variableDeclarations.accept(self)
        print(')',end='')


    # def visitSimpleParametersFunction(self, SimpleParametersFunction):
    #     if type(SimpleParametersFunction.primaryExpression) in types:
    #         print(SimpleParametersFunction.primaryExpression)
    #     else:
    #         SimpleParametersFunction.primaryExpression.accept(self)


    def visitParametersFunctionConcrete(self, ParametersFunction):
        ParametersFunction.primaryExpression.accept(self)
        print(',',end='')
        ParametersFunction.parametersFunction.accept(self)


    # def visitSimpleDisjunction(self, SimpleDisjunction):
    #     if type(SimpleDisjunction.conjunction) in types:
    #         print(SimpleDisjunction.conjunction, end='')
    #     else:
    #         SimpleDisjunction.conjunction.accept(self)


    def visitDisjunctionConcrete(self, Disjunction):
        if type(Disjunction.conjunction) in types:
            print(Disjunction.conjunction, end='')
        else:
            Disjunction.conjunction.accept(self)
        
        print('||',end='')
        
        if type(Disjunction.conjunction) in types:
            print(Disjunction.conjunction, end='')
        else:
            Disjunction.conjunction.accept(self)


    # def visitSimpleConjunction(self, SimpleConjunction):
    #     SimpleConjunction.equality.accept(self)


    def visitConjunctionConcrete(self, Conjunction):
        if type(Conjunction.equality) in types:
            print(Conjunction.equality, end='')
        else:
            Conjunction.equality.accept(self)
                
        print('&&',end='')

        if type(Conjunction.conjunction) in types:
            print(Conjunction.conjunction, end='')
        else:
            Conjunction.conjunction.accept(self)

  
    # def visitSimpleEquality(self, SimpleEquality):
    #     SimpleEquality.comparison.accept(self)


    def visitEqualityConcrete(self, Equality):
        if type(Equality.comparison) in types:
            print(Equality.comparison ,end=' ')
        else:
            Equality.comparison.accept(self)

        if type(Equality.equalityOperator) in types:
            print(Equality.equalityOperator, end=' ')
        else:
            Equality.equalityOperator.accept(self)
        
        if type(Equality.equality) in types:
            print(Equality.equality)
        else:
            Equality.equality.accept(self)


    # def visitSimpleComparison(self, SimpleComparison):
    #     print(SimpleComparison.infixOperation)


    def visitComparisonConcrete(self, Comparison):
        if type(Comparison.infixOperation) in types:
            print(Comparison.infixOperation, end=' ')
        else:
            Comparison.infixOperation.accept(self)
        
        if type(Comparison.comparisonOperator) in types:
            print(Comparison.comparisonOperator, end=' ')
        else:
            Comparison.comparisonOperator.accept(self)
        
        if type(Comparison.infixOperation2) in types:
            print(Comparison.infixOperation2)
        else:
            Comparison.infixOperation2.accept(self)


    def visitInfixOperation_In(self, InfixOperation):
        if type(InfixOperation.infixOperation) in types:
            print(InfixOperation.infixOperation, end=' ')
        else:
            InfixOperation.infixOperation.accept(self)
        
        if(InfixOperation.inOperator) in types:
            print(InfixOperation.inOperator, end=' ')
        else:
            InfixOperation.inOperator.accept(self)
        
        if type(InfixOperation.elvisExpression) in types:
            print(InfixOperation.elvisExpression)
        else:
            InfixOperation.elvisExpression.accept(self)


    def visitInfixOperation_Is(self, InfixOperation):
        if type(InfixOperation.infixOperation) in types:
            print(InfixOperation.infixOperation, end=' ')
        else:
            InfixOperation.infixOperation.accept(self)
        
        if(InfixOperation.isOperator) in types:
            print(InfixOperation.isOperator, end=' ')
        else:
            InfixOperation.isOperator.accept(self)
        
        if type(InfixOperation.type) in types:
            print(InfixOperation.type)
        else:
            InfixOperation.type.accept(self)


    # def visitSimpleElvisExpression(self, SimpleElvisExpression):
    #     SimpleElvisExpression.rangeExpression.accept(self)


    def visitElvisExpressionConcrete(self, ElvisExpression):
        if type(ElvisExpression.elvisExpression) in types:
            print(ElvisExpression.elvisExpression, end=' ')
        else:
            ElvisExpression.elvisExpression.accept(self)
        
        print('?:')
        
        if type(ElvisExpression.rangeExpression) in types:
            print(ElvisExpression.rangeExpression)
        else:
            ElvisExpression.rangeExpression.accept(self)


    # def visitSimpleRangeExpression(self, SimpleRangeExpression):
    #     SimpleRangeExpression.additiveExpression.accept(self)


    def visitRangeExpressionConcrete(self, CompoundRangeExpression):
        if type(CompoundRangeExpression.rangeExpression) in types:
            print(CompoundRangeExpression.rangeExpression, end='')
        else:
            CompoundRangeExpression.rangeExpression.accept(self)
        
        print('..', end='')

        if type(CompoundRangeExpression.additiveExpression) in types:
            print(CompoundRangeExpression.additiveExpression, end='')
        else:
            CompoundRangeExpression.additiveExpression.accept(self)


    # def visitSimpleAdditiveExpression(self, SimpleAdditiveExpression):
    #     SimpleAdditiveExpression.multiplicativeExpression.accept(self)


    def visitAdditiveExpressionConcrete(self, AdditiveExpression):
        if(AdditiveExpression.additiveExpression) in types:
            print(AdditiveExpression.additiveExpression, end=' ')
        else:
            AdditiveExpression.additiveExpression.accept(self)
        
        if type(AdditiveExpression.additiveOperator) in types:
            print(AdditiveExpression.additiveOperator, end=' ')
        else:
            AdditiveExpression.additiveOperator.accept(self)
        
        if type(AdditiveExpression.multiplicativeExpression) in types:
            print(AdditiveExpression.multiplicativeExpression)
        else:
            AdditiveExpression.multiplicativeExpression.accept(self)


    # def visitSimpleMultiplicativeExpression(self, SimpleMultiplicativeExpression):
    #     SimpleMultiplicativeExpression.asExpression.accept(self)


    def visitMultiplicativeExpressionConcrete(self, MultiplicativeExpression):
        if type(MultiplicativeExpression.multiplicativeExpression) in types:
            print(MultiplicativeExpression.multiplicativeExpression, end=' ')
        else:
            MultiplicativeExpression.multiplicativeExpression.accept(self)
        
        if type(MultiplicativeExpression.multiplicativeOperator) in types:
            print(MultiplicativeExpression.multiplicativeOperator, end=' ')
        else:
            MultiplicativeExpression.multiplicativeOperator.accept(self)
        
        if type(MultiplicativeExpression.asExpression) in types:
            print(MultiplicativeExpression.asExpression)
        else:
            MultiplicativeExpression.asExpression.accept(self)


    # def visitSimpleAsExpression(self, SimpleAsExpression):
    #     SimpleAsExpression.unaryExpression.accept(self)


    def visitAsExpressionConcrete(self, AsExpression):
        if type(AsExpression.unaryExpression) in types:
            print(AsExpression.unaryExpression, end=' ')
        else:
            AsExpression.unaryExpression.accept(self)
        
        if type(AsExpression.asOperator) in types:
            print(AsExpression.asOperator, end=' ')
        else:
            AsExpression.asOperator.accept(self)

        if type(AsExpression.type) in types:
            print(AsExpression.type)
        else:
            AsExpression.type.accept(self)


    def visitUnaryExpressionConcrete(self, UnaryExpression):
        if type(UnaryExpression.unaryOperator) in types:
            print(UnaryExpression.unaryOperator, end= '')
        else:
            UnaryExpression.unaryOperator.accept(self)
        
        if type(UnaryExpression.primaryExpression) in types:
            print(UnaryExpression.primaryExpression)
        else:
            UnaryExpression.primaryExpression.accept(self)


    def visitUnaryExpressionPostfixConcrete(self, UnaryExpression):
        if type(UnaryExpression.primaryExpression) in types:
            print(UnaryExpression.primaryExpression, end=' ')
        else:
            UnaryExpression.primaryExpression.accept(self)
        
        if type(UnaryExpression.postfixUnaryOperator) in types:
            print(UnaryExpression.postfixUnaryOperator)
        else:
            UnaryExpression.postfixUnaryOperator.accept(self)


    def visitReturnConcrete(self, Return):
        print('return')

        if type(Return.expression) in types:
            print(Return.expression, end='')
        else:
            Return.expression.accept(self)


    def visitParenthesizedExpressionConcrete(self, ParenthesizedExpression):
        print('(')

        if type(ParenthesizedExpression.expression) in types:
            print(ParenthesizedExpression.expression, end='')
        else:
            ParenthesizedExpression.expression.accept(self)

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


    def visitAsOperatorConcrete(self, CompoundAsOperator):
        print('as', end=' ')
        if type(CompoundAsOperator.asOperator) in types:
            print(CompoundAsOperator.asOperator)
        else:
            CompoundAsOperator.asOperator.accept(self)


    # def visitAsOperatorConcrete(self, AsOperator):
    #     AsOperator.accept(self)


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
