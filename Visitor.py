class Visitor:
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

    def visitFuncrionDeclaration(self, FunctionDeclaration):
        print('fun', end='')
        FunctionDeclaration.simpleIdentifier.accept(self)
        FunctionDeclaration.functionValueParameters.accept(self)
        FunctionDeclaration.optinalType.accept(self)
        FunctionDeclaration.optionalBlock.accept(self)

    def visitOptinalType(self,OptinalType):
        OptinalType.type.accept(self)

    def visitOptionalBlock(self,OptionalBlock):
        print('{')
        OptionalBlock.block.accept(self)
        print('}')

    def visitPropertyDeclaration(self, PropertyDeclarationConcrete):
        PropertyDeclarationConcrete.varOrVal.accept(self)
        PropertyDeclarationConcrete.MvOrV.accept(self)
        PropertyDeclarationConcrete.optionalTypeParameters.accept(self)
        PropertyDeclarationConcrete.optionalPv.accept(self)
        PropertyDeclarationConcrete.expression.accept(self)

    def visitMultiVariableDeclaration(self,MultiVariableDeclaration):
        MultiVariableDeclaration.multiVariableDeclaration.accept(self)

    def visitVariableDeclaration(self,VariableDeclaration):
        VariableDeclaration.variableDeclaration.accept(self)

    def visitPd1_var(self,Var):
        Var.var.accept(self)
        print('var')

    def visitPd1_val(self,Val):
        Val.val.accept(self)
        print('val')

    def visitOptionalTypeParameters(self,OptionalTypeParameters):
        OptionalTypeParameters.typeParameters.accept(self)


    def visitOptionalPv(self,OptionalPv):
        OptionalPv.pv.accept(self)
        print(';')

    def visitTypePatameters(self,TypeParametersConcrete):
        TypeParametersConcrete.typeParameter.accept(self)
        TypeParametersConcrete.typeParametersRecursive.accept(self)
        TypeParametersConcrete.optionalCOMMA.accept(self)

    def visitSimpleTypeParameterRecursive(self,SimpleTypeParametersRecursive):
        SimpleTypeParametersRecursive.typeParameter.accept(self)

    def visitCompoundTypeParametersRecursive(self,CompoundTypeParametersRecursive):
        CompoundTypeParametersRecursive.typeParameter.accept(self)
        CompoundTypeParametersRecursive.typeParametersRecursive.accept(self)

    def visitOptionalCOMMA(self,OptionalCOMMA):
        OptionalCOMMA.COMMA.accept(self)

    def visitSimpleTypePatameter(self,SimpleTypeParameter):
        SimpleTypeParameter.simpleIdentifier.accept(self)

    def visitCompoundTypePatameter (self,  CompoundTypeParameter):
        CompoundTypeParameter.type.accept(self)
        CompoundTypeParameter.simpleIdentifier.accept(self)

    def visitSimpleFunctionBody(self, SimpleFunctionBody):
        print('{')
        SimpleFunctionBody.block.accept(self)
        print('}')
    def visitCompoundFunctionBody(self, CompoundFunctionBody):
        CompoundFunctionBody.expression.accept(self)

    def visitSimpleFunctionValueParameters(self,SimpleFunctionValueParameters):
        SimpleFunctionValueParameters.accept(self)

    def visitCompoundFunctionValueParameters(self,CompoundFunctionValueParameters):
        CompoundFunctionValueParameters.fvps.accept(self)

    def visitSimpleFunctionValueParametersRecursive(self,SimpleFunctionValueParametersRecursive):
        SimpleFunctionValueParametersRecursive.fvp.accept(self)
        SimpleFunctionValueParametersRecursive.optionalCOMMA.accept(self)

    def visitCompoundFunctionValueParametersRecursive(self,CompoundFunctionValueParametersRecursive):
        CompoundFunctionValueParametersRecursive.fvp.accept(self)
        CompoundFunctionValueParametersRecursive.functionValueParametersRecursive.accept(self)

    def visitSimpleFunctionValueParameter(self,SimpleFunctionValueParameter):
        SimpleFunctionValueParameter.parameter.accept(self)

    def visitCompoundFunctionValueParameter(self,CompoundFunctionValueParameter):
        CompoundFunctionValueParameter.parameter.accept(self)
        CompoundFunctionValueParameter.exp.accept(self)

    def visitSimpleMultiVariableDeclaration(self,SimpleMultiVariableDeclaration):
        SimpleMultiVariableDeclaration.accept(self)

    def visitCompoundMultiVariableDeclaration(self,CompoundMultiVariableDeclaration):
        CompoundMultiVariableDeclaration.mvd.accept(self)

    def visitSimpleVariableDeclaration(self,SimpleVariableDeclaration):
        SimpleVariableDeclaration.simpleIdentifier.accept(self)

    def visitCompoundVariableDeclaration(self,CompoundVariableDeclaration):
        CompoundVariableDeclaration.simpleIdentifier.accept(self)
        CompoundVariableDeclaration.type.accept(self)

    def visitSimpleMultiVariableDeclarationRecursive(self,SimpleMultiVariableDeclarationRecursive):
        SimpleMultiVariableDeclarationRecursive.variableDeclaration.accept(self)

    def visitCompoundMultiVariableDeclarationRecursive(self,CompoundMultiVariableDeclarationRecursive):
        CompoundMultiVariableDeclarationRecursive.mvd.accept(self)
        CompoundMultiVariableDeclarationRecursive.variableDeclaration.accept(self)

    def visitParameter(self,ParameterConcrete):
        ParameterConcrete.simpleIdentifier.accept(self)
        ParameterConcrete.type.accept(self)

    def visitTypeConcrete(self,TypeConcrete):
        TypeConcrete.optionalTypeModifiers.accept(self)
        TypeConcrete.optype.accept(self)

    def visitOptionalTypeModifiersConcrete(self,OptionalTypeModifiersConcrete):
        OptionalTypeModifiersConcrete.typeModifiers.accept(self)

    def visitParenthesizedType(self,ParenthesizedTypeConcrete):
        ParenthesizedTypeConcrete.type.accept(self)

    def visitFunctionType(self,FunctionType):
        FunctionType.functionType.accept(self)

    def visitUserType(self,UserType):
        UserType.simpleUserType.accept(self)

    def visitSimpleTypeModifiers(self,SimpleTypeModifiers):
        SimpleTypeModifiers.typeModifier.accept(self)

    def visitCompoundTypeModifiers(self, CompondTypeModifiers):
        CompondTypeModifiers.typeModifier.accept(self)
        CompondTypeModifiers.typeModifiers.accept(self)

    def visitTypeModifierConcrete(self, TypeModifierConcrete):
        TypeModifierConcrete.suspend.accept(self)
        print('suspend')

    def visitTypeProjectionModifierConcrete(self,TypeProjectionModifierConcrete):
        TypeProjectionModifierConcrete.varianceModifier.accept(self)

    def visitVariaceModifierIn(self, In):
        In.IN.accept(self)
        print('in')

    def visitVariaceModifierOut(self, Out):
        Out.out.accept(self)
        print('out')

    def visitSimpleSimpleUserType(self, SimpleUserTypeConcrete):
        SimpleUserTypeConcrete.accept(self)

    def visitSimpleSimpleUserType(self,SimpleSimpleUserType):
        SimpleSimpleUserType.simpleIdentifier.accept(self)

    def visitCompoundSimpleUserType(self, CompoundSimpleUserType):
        CompoundSimpleUserType.simpleIdentifier.accept(self)
        CompoundSimpleUserType.typeArguments.accept(self)

    def visittypeSimpleProjection(self, SimpleTypeProjection):
        SimpleTypeProjection.type.accept(self)

    def visitCompoundTypeProjection(self,CompoundTypeProjection):
        CompoundTypeProjection.typeProjectionModifiers.accept(self)
        CompoundTypeProjection.type.accept(self)

    def visitSimpleTypeProjectionModifiers(self,SimpleTypeProjectionModifiers):
        SimpleTypeProjectionModifiers.typeProjection.accept(self)

    def visitCompoundTypeProjectionModifiers(self,CompoundTypeProjectionModifiers):
        CompoundTypeProjectionModifiers.typeProjectionModifier.accept(self)
        CompoundTypeProjectionModifiers.typeProjectionModifiers.accept(self)

    def visitSimpleFunctionType(self,SimpleFunctionType):
        SimpleFunctionType.functionTypeParameters.accept(self)

    def visitCompoundFunctionType(self, CompoundFunctionType):
        CompoundFunctionType.receiverType.accept(self)
        CompoundFunctionType.functionTypeParameters.accept(self)
        CompoundFunctionType.type.accept(self)

    def visitFunctionTypeParametersConcrete(self,FunctionTypeParametersConcrete):
        FunctionTypeParametersConcrete.optionalParameterOrType.accept(self)
        FunctionTypeParametersConcrete.parameterOrTypeRecursive.accept(self)
        FunctionTypeParametersConcrete.optionalCOMMA.accept(self)

    def visitSimpleParameterOrTypeRecursive(self,SimpleParameterOrTypeRecursive):
        SimpleParameterOrTypeRecursive.optionalParameterOrType.accept(self)

    def visitCompoundParameterOrTypeRecursive(self, CompoundParameterOrTypeRecursive):
        CompoundParameterOrTypeRecursive.optionalParameterOrType.accept(self)
        CompoundParameterOrTypeRecursive.parameterOrTypeRecursive.accept(self)

    def visitReceiverTypeConcrete(self, ReceiverTypeConcrete):
        ReceiverTypeConcrete.typeModifier.accept(self)
        ReceiverTypeConcrete.parenthesizedType.accept(self)

    def visitSimpleStatemnts(self,SimpleStatements):
        SimpleStatements.statement.accept(self)

    def visitCompoundStatemnts(self,CompoundStatements):
        CompoundStatements.statement.accept(self)
        CompoundStatements.statments.accept(self)

    def visitFunctionDeclaration(self, FunctionDeclaration):
        FunctionDeclaration.accept(self)

    def visitAssignment(self,Assignment):
        Assignment.accept(self)

    def visitLoopStatement(self,LoopStatement):
        LoopStatement.accept(self)

    def visitExpression(self,Expression):
        Expression.accept(self)

    def visitBlock(self,Block):
        Block.accept(self)

    def visitBlock(self,StatementConcrete):
        StatementConcrete.accept(self)

    def visitForStatement_MD(self,ForStatement_MD):
        print('for(', end='')
        ForStatement_MD.forStatement.accept(self)
        print(')', end='')

    def visitForStatement_VD(self, ForStatement_VD):
        ForStatement_VD.forStatement.accept(self)
        print('forStatement')

    def visitWhileStatement_PV(self,WhileStatement_PV):
        print('while (', end='')
        WhileStatement_PV.expression.accept(self)
        print(')', end='')

    def visitWhileStatement_CBS(self,WhileStatement_CBS):
        print('while (', end='')
        WhileStatement_CBS.expression.accept(self)
        print(')', end='')
        WhileStatement_CBS.controlStructureBody.accept(self)

    def visitWhileStatementD(self,WhileStatement):
        WhileStatement.whileStatement.acccept(self)

    def visitDoWhileStatement(self, DoWhileStatement):
        DoWhileStatement.doWhileStatement.accept(self)

    def visitSimpleForStatement_MD(self,SimpleForStatement_MD):
        SimpleForStatement_MD.multiVariableDeclaration.accept(self)
        SimpleForStatement_MD.expression.accept('expression')

    def visitCompoundForStatement_MD(self, CompoundForStatement_MD):
        CompoundForStatement_MD.multiVariableDeclaration.accept(self)
        CompoundForStatement_MD.expression.accept(self)
        CompoundForStatement_MD.controlStructureBody.accept(self)

    def visitSimpleForStatement_VD(self,SimpleForStatement_VD):
        SimpleForStatement_VD.variableDeclaration.accept(self)
        SimpleForStatement_VD.expression.accept(self)

    def visitCompoundForStatement_VD(self,CompoundForStatement_VD):
        CompoundForStatement_VD.variableDeclaration.accept(self)
        CompoundForStatement_VD.expression.accept(self)
        CompoundForStatement_VD.controlStructureBody.accept(self)

    def visitSimpleDoWhileStatement(self, SimpleDoWhileStatement):
        SimpleDoWhileStatement.expression.accept(self)

    def visitCompoundDoWhileStatement(self,CompoundDoWhileStatement):
        CompoundDoWhileStatement.controlStructureBody.accept(self)
        CompoundDoWhileStatement.expression.accept(self)

    def visitAssignmentConcrete(self,AssignmentConcrete):
        AssignmentConcrete.directlyAssignableExpression.accept(self)
        AssignmentConcrete.expression.accept(self)

    def visitAssignmentAndOperatorConcrete(self,AssignmentAndOperatorConcrete):
        AssignmentAndOperatorConcrete.assignmentAndOperator.accept(self)
        AssignmentAndOperatorConcrete.expression.accept(self)
        AssignmentAndOperatorConcrete.assignableExpression.accept(self)

    def visitDisjunctionConcrete(self,DisjunctionConcrete):
        DisjunctionConcrete.accept(self)

    def visitSimpleDisjunction(self,SimpleDisjunction):
        SimpleDisjunction.conjunction.accept(self)

    def visitCompoundDisjunction(self,CompoundDisjunction):
        CompoundDisjunction.conjunction.accept(self)
        CompoundDisjunction.disjunction.accept(self)

    def vistSimpleConjunction(self, SimpleConjunction):
        SimpleConjunction.equality.accept(self)

    def vistCompoundConjunction(self,CompoundConjunction):
        CompoundConjunction.equality.accept(self)
        CompoundConjunction.conjunction.accept(self)

    def visitSimpleEquality(self,SimpleEquality):
        SimpleEquality.comparison.accept(self)

    def visitCompoundEquality(self,CompoundEquality):
        CompoundEquality.comparison.accept(self)
        CompoundEquality.equalityOperator.accept(self)
        CompoundEquality.equality.accept(self)

    def vistSimpleComparison(self,SimpleComparison):
        SimpleComparison.infixOperation.accept(self)

    def vistCompoundComparison(self,CompoundComparison):
        CompoundComparison.infixOperation.accept(self)
        CompoundComparison.comparisonOperator.accept(self)

    def visitSimpleInfixOperation(self,SimpleInfixOperation):
        SimpleInfixOperation.elvisExpression.accept(self)

    def visitCompoundInfixOperation(self,CompoundInfixOperation):
        CompoundInfixOperation.elvisExpression.accept(self)
        CompoundInfixOperation.infixOperationRecursive.accept(self)

    def visitSimpleInfixOperationRecursive(self,SimpleInfixOperationRecursive):
        SimpleInfixOperationRecursive.inOrIs.accept(self)
        SimpleInfixOperationRecursive.elvisOrType.accept(self)

    def visitCompoundInfixOperationRecursive(self, CompoundInfixOperationRecursive):
        CompoundInfixOperationRecursive.inOrIs.accept(self)
        CompoundInfixOperationRecursive.elvisOrType.accept(self)
        CompoundInfixOperationRecursive.infixOperationRecursive.accept(self)

    def visitInOperator(self, InOperator):
        InOperator.In.accept(self)
        print('in')

    def visitIsOperator(self,IsOperator):
        IsOperator.Is.accept(self)
        print('is')

    def visitElvisExpressionConcrete(self,ElvisExpressionConcrete):
        ElvisExpressionConcrete.elvisExpression.accept(self)

    def visitSimpleElvisExpression(self,SimpleElvisExpression):
        SimpleElvisExpression.infixFunctionCall.accept(self)

    def visitCompoundElvisExpression(self,CompoundElvisExpression):
        CompoundElvisExpression.infixFunctionCall.accept(self)
        CompoundElvisExpression.elvisExpression.accept(self)

    def visitSimpleInfixFunctionCall(self,SimpleInfixFunctionCall):
        SimpleInfixFunctionCall.rangeExpression.accept(self)

    def visitCompoundInfixFunctionCall(self, CompoundInfixFunctionCall):
        CompoundInfixFunctionCall.rangeExpression.accept(self)
        CompoundInfixFunctionCall.simpleIdentifier.accept(self)
        CompoundInfixFunctionCall.infixFunctionCall.accept(self)

    def visitSimpleRangeExpression(self, SimpleRangeExpression):
        SimpleRangeExpression.additiveExpression.accept(self)

    def visitCompoundRangeExpression(self,CompoundRangeExpression):
        CompoundRangeExpression.additiveExpression.accept(self)
        CompoundRangeExpression.rangeExpression.accept(self)

    def visitSimpleAdditiveExpression(self,SimpleAdditiveExpression):
        SimpleAdditiveExpression.multiplicativeExpression.accept(self)

    def visitCompoundAdditiveExpression(self,CompoundAdditiveExpression):
        CompoundAdditiveExpression.multiplicativeExpression.accept(self)
        CompoundAdditiveExpression.additiveOperator.accept(self)
        CompoundAdditiveExpression.additiveExpression.accept(self)

    def visitSimpleMultiplicativeExpression(self,SimpleMultiplicativeExpression):
        SimpleMultiplicativeExpression.asExpression.accept(self)

    def visitCompoundMultiplicativeExpression(self,CompoundMultiplicativeExpression):
        CompoundMultiplicativeExpression.asExpression.accept(self)
        CompoundMultiplicativeExpression.multiplicativeOperator.accept(self)
        CompoundMultiplicativeExpression.multiplicativeExpression.accept(self)

    def visitSimpleAsExpression(self,SimpleAsExpression):
        SimpleAsExpression.prefixUnaryExpression.accept(self)

    def visitCompoundAsExpression(self,CompoundAsExpression):
        CompoundAsExpression.prefixUnaryExpression.accept(self)
        CompoundAsExpression.asOperator.accept(self)
        CompoundAsExpression.type.accept(self)

    def visitSimplePrefixUnaryExpression(self,SimplePrefixUnaryExpression):
        SimplePrefixUnaryExpression.postfixUnaryExpression.accept(self)

    def visitCompoundPrefixUnaryExpression(self,CompoundPrefixUnaryExpression):
        CompoundPrefixUnaryExpression.prefixUnaryExpressionRecursive.accept(self)
        CompoundPrefixUnaryExpression.postfixUnaryExpression.accept(self)

    def visitSimplePrefixUnaryExpressionRecursive(self,SimplePrefixUnaryExpressionRecursive):
        SimplePrefixUnaryExpressionRecursive.unaryPrefix.accept(self)

    def visitCompoundPrefixUnaryExpressionRecursive(self,CompoundPrefixUnaryExpressionRecursive):
        CompoundPrefixUnaryExpressionRecursive.unaryPrefix.accept(self)
        CompoundPrefixUnaryExpressionRecursive.prefixUnaryExpressionRecursive.accept(self)

    def visitPrefixUnaryOperatorConcrete(self,PrefixUnaryOperatorConcrete):
        PrefixUnaryOperatorConcrete.prefixUnaryOperator.accept(self)

    def visitLabelConcrete(self,LabelConcrete):
        LabelConcrete.label.accept(self)

    def visitSimplePostfixUnaryExpression(self,SimplePostfixUnaryExpression):
        SimplePostfixUnaryExpression.primaryExpression.accept(self)

    def visitCompoundPostfixUnaryExpression(self,CompoundPostfixUnaryExpression):
        CompoundPostfixUnaryExpression.primaryExpression.accept(self)
        CompoundPostfixUnaryExpression.postfixUnaryExpressionRecursive.accept(self)

    def visitSinglePostfixUnaryExpressionRecursive(self,SinglePostfixUnaryExpressionRecursive):
        SinglePostfixUnaryExpressionRecursive.postfixUnarySuffix.accept(self)

    def visitCompoundPostfixUnaryExpressionRecursive(self,CompoundPostfixUnaryExpressionRecursive):
        CompoundPostfixUnaryExpressionRecursive.postfixUnarySuffix.accept(self)
        CompoundPostfixUnaryExpressionRecursive.postfixUnaryExpression.accept(self)

    def visitPostfixUnaryOperatorConcrete(self,PostfixUnaryOperatorConcrete):
        PostfixUnaryOperatorConcrete.postfixUnaryOperator.accept(self)

    def visitTypeArgumentsConcrete(self,TypeArgumentsConcrete):
        TypeArgumentsConcrete.typeArguments.accept(self)

    def visitCallSuffixConcrete(self,CallSuffixConcrete):
        CallSuffixConcrete.callSuffix.accept(self)

    def visitIndexingSuffixConcrete(self,IndexingSuffixConcrete):
        IndexingSuffixConcrete.indexingSuffix.accept(self)

    def visitNavigationSuffixConcrete(self,NavigationSuffixConcrete):
        NavigationSuffixConcrete.navigationSuffix.accept(self)

    def visitIncremento(self,Incremento):
        Incremento.incremento.accept(self)
        print('++')

    def visitDecremento(self,Decremento):
        Decremento.decremento.accept(self)
        print('--')

    def visitSimpleTypeArguments(self,SimpleTypeArguments):
        SimpleTypeArguments.accept(self)

    def visitTa(self,Ta):
        Ta.ta.accept(self)
        Ta.typePtojection.accept(self)

    def visitIndexingSuffix(self,IndexingSuffix):
        IndexingSuffix.indexingSuffix.accept(self)

    def visitCallSuffix(self,CallSuffix):
        CallSuffix.callSuffix.accept(self)

    def visitSimpleIdentifier(self,SimpleIdentifier):
        SimpleIdentifier.simpleIdentifier.accept(self)

    def visitParenthesizedDirectlyAssignableExpression(self,ParenthesizedDirectlyAssignableExpression):
        ParenthesizedDirectlyAssignableExpression.ParenthesizedDirectlyAssignableExpression.accept(self)

    def visitSimpleDirectlyAssignableExpression(self,SimpleDirectlyAssignableExpression):
        SimpleDirectlyAssignableExpression.simpleIdentifier.accept(self)

    def visitParenthesizedDirectlyAssignableExpressionConcrete(self,ParenthesizedDirectlyAssignableExpressionConcrete):
        ParenthesizedDirectlyAssignableExpressionConcrete.directlyAssignableExpression.accept(self)

    def visitParenthesizedAssignableExpressionConcrete(self,ParenthesizedAssignableExpressionConcrete):
        ParenthesizedAssignableExpressionConcrete.parenthesizedAssignableExpression.accept(self)

    def visitPrefixUnaryExpressionConcrete(self,PrefixUnaryExpressionConcrete):
        PrefixUnaryExpressionConcrete.prefixUnaryExpression.accept(self)

    def visitAssignableExpressionConcrete(self,AssignableExpressionConcrete):
        AssignableExpressionConcrete.assignableExpression.accept(self)

    def visitSimpleIndexingSuffix(self,SimpleIndexingSuffix):
        SimpleIndexingSuffix.accept(self)

    def visitCompoundIndexingSuffix(self,CompoundIndexingSuffix):
        CompoundIndexingSuffix.indexingSuffix.accept(self)

    def visitSimpleIndexingSuffixRecursive(self,SimpleIndexingSuffixRecursive):
        SimpleIndexingSuffixRecursive.expression.accept(self)

    def visitCompoundIndexingSuffixRecursive(self,CompoundIndexingSuffixRecursive):
        CompoundIndexingSuffixRecursive.expression.accept(self)
        CompoundIndexingSuffixRecursive.indexingSuffix.accept(self)

    def visitparenthesizedExpressionConcrete(self,ParenthesizedExpressionConcrete):
        ParenthesizedExpressionConcrete.expression.accept(self)

    def visitSimpleCallSuffixConcrete(self,SimpleCallSuffixConcrete):
        SimpleCallSuffixConcrete.optionalTypeArguments.accept(self)
        SimpleCallSuffixConcrete.optionalValueArguments.accept(self)

    def visitCompoundCallSuffixConcrete(self,CompoundCallSuffixConcrete):
        CompoundCallSuffixConcrete.optionalTypeArguments.accept(self)
        CompoundCallSuffixConcrete.optionalValueArguments.accept(self)
        CompoundCallSuffixConcrete.annotatedLambda.accept(self)

    def visitValueArgumentsConcrete(self,ValueArgumentsConcrete):
        ValueArgumentsConcrete.valueArguments.accept(self)

    def visitAnnotatedLambdaConcrete(self,TypeArgumentsConcrete):
        TypeArgumentsConcrete.typeArguments.accept(self)
        TypeArgumentsConcrete.valueArguments.accept(self)
        TypeArgumentsConcrete.annotatedLambda.accept(self)

    def visitLambdaLiteralConcrete(self,LambdaLiteralConcrete):
        LambdaLiteralConcrete.lambdaLiteral.accept(self)

    def visitSimpleTypeArguments(self,SimpleTypeArguments):
        SimpleTypeArguments.accept(self)

    def visitCompoundTypeArguments(self,CompoundTypeArguments):
        CompoundTypeArguments.typeArgumentsRecursive.accept(self)

    def visitSimpleTypeArgumentsRecursive(self,SimpleTypeArgumentsRecursive):
        SimpleTypeArgumentsRecursive.typeProjection.accept(self)

    def visitCompoundCompoundTypeArgumentsRecursive(self,CompoundTypeArgumentsRecursive):
        CompoundTypeArgumentsRecursive.typeProjection.accept(self)
        CompoundTypeArgumentsRecursive.typeArgumentsRecursive.accept(self)

    def visitSimpleValueArguments(self,SimpleValueArguments):
        SimpleValueArguments.accept(self)

    def visitCompoundValueArguments(self,CompoundValueArguments):
        CompoundValueArguments.valueArgumentsRecursive.accept(self)

    def visitSimpleValueArgumentsRecursive(self,SimpleValueArgumentsRecursive):
        SimpleValueArgumentsRecursive.valueArgument.accept(self)

    def visitCompoundValueArgumentsRecursive(self,CompoundValueArgumentsRecursive):
        CompoundValueArgumentsRecursive.valueArgument.accept(self)
        CompoundValueArgumentsRecursive.valueArgumentsRecursive.accept(self)

    def visitSimpleValueArgument(self,SimpleValueArgument):
        SimpleValueArgument.simpleIdentifier.accept(self)

    def visitCompound1ValueArgument(self,Compound1ValueArgument):
        Compound1ValueArgument.simpleIdentifier.accept(self)
        Compound1ValueArgument.expression.accept(self)

    def visitCompound2ValueArgument(self,Compound2ValueArgument):
        Compound2ValueArgument.simpleIdentifier.accept(self)
        Compound2ValueArgument.expression.accept(self)

    def visitLITERAL_STRINGConcrete(self,LITERAL_STRINGConcrete):
        LITERAL_STRINGConcrete.LITERAL_STRING.accept(self)

    def visitableReferenceConcrete(self,CallableReferenceConcrete):
        CallableReferenceConcrete.callableReference.accept(self)

    def visitFunctionLiteralConcrete(self,FunctionLiteralConcrete):
        FunctionLiteralConcrete.functionLiteral.accept(self)

    def visitCollectionLiteralConcrete(self,CollectionLiteralConcrete):
        CollectionLiteralConcrete.collectionLiteral.accept(self)

    def visitIfExpressionConcrete(self,IfExpressionConcrete):
        IfExpressionConcrete.ifExpression.accept(self)

    def visitJumpExpressionConcrete(self,JumpExpressionConcrete):
        JumpExpressionConcrete.jumpExpression.accept(self)

    def visitSimpleCollectionLiteral(self,SimpleCollectionLiteral):
        SimpleCollectionLiteral.accept(self)

    def visitCompoundCollectionLiteral(self,CompoundCollectionLiteral):
        CompoundCollectionLiteral.collectionLiteralRecursive.accept(self)

    def visitSimpleCollectionLiteralRecursive(self,SimpleCollectionLiteralRecursive):
        SimpleCollectionLiteralRecursive.expression.accept(self)

    def visitCompoundCollectionLiteralRecursive(self,CompoundCollectionLiteralRecursive):
        CompoundCollectionLiteralRecursive.expression.accept(self)
        CompoundCollectionLiteralRecursive.collectionLiteralRecursive.accept(self)

    def visitSimpleParametersWithOptionalType(self,SimpleParametersWithOptionalType):
        SimpleParametersWithOptionalType.accept(self)

    def visitCompoundParametersWithOptionalType(self,CompoundParametersWithOptionalType):
        CompoundParametersWithOptionalType.parametersWithOptionalTypeRecursive.accept(self)

    def visitSimpleParametersWithOptionalTypeRecursive(self,SimpleParametersWithOptionalTypeRecursive):
        SimpleParametersWithOptionalTypeRecursive.parameterWithOptionalType.accept(self)

    def visitCompoundParametersWithOptionalTypeRecursive(self,CompoundPwot):
        CompoundPwot.parameterWithOptionalType.accept(self)
        CompoundPwot.parametersWithOptionalTypeRecursive.accept(self)

    def visitParameterWithOptionalTypeConcrete(self,ParameterWithOptionalTypeConcrete):
        ParameterWithOptionalTypeConcrete.simpleIdentifier.accept(self)
        ParameterWithOptionalTypeConcrete.optionalParameterModifiers.accept(self)
        ParameterWithOptionalTypeConcrete.optionalType.accept(self)

    def visitOptionalParameterModifiersConcrete(self,OptionalParameterModifiersConcrete):
        OptionalParameterModifiersConcrete.parameterModifiers.acccept(self)

    def visitVararg(self,VarargConcrete):
        VarargConcrete.accept(self)

    def visitNoinline(self,NoinlineConcrete):
        NoinlineConcrete.accept(self)

    def visitCrossinline(self,CrossinlineConcrete):
        CrossinlineConcrete.accept(self)

    def visitlambdaLiteral(self,LambdaLiteral):
        LambdaLiteral.optionsLambdaLiteral.accept(self)

    def visitSimpleOptionsLambdaLiteral(self,SimpleOptionsLambdaLiteral):
        SimpleOptionsLambdaLiteral.statements.accept(self)

    def visitCompound1OptionsLambdaLiteral(self,Compound1OptionsLambdaLiteral):
        Compound1OptionsLambdaLiteral.statements.accept(self)

    def visitCompound2OptionsLambdaLiteral(self,Compound2OptionsLambdaLiteral):
        Compound2OptionsLambdaLiteral.lambdaParameters.accept(self)
        Compound2OptionsLambdaLiteral.statements.accept(self)

    def visitSimpleLambdaParameters(self,SimpleLambdaParameters):
        SimpleLambdaParameters.lambdaParameter.accept(self)

    def visitCompoundLambdaParameters(self,CompoundLambdaParameters):
        CompoundLambdaParameters.lambdaParameter.accept(self)
        CompoundLambdaParameters.lambdaParameters.accept(self)

    def visitVariableDeclaration(self,VariableDeclarationConcrete):
        VariableDeclarationConcrete.multiVariableDeclaration.accept(self)

    def visitCompoundLambdaParameter(self,MultiVariableDeclarationConcrete):
        MultiVariableDeclarationConcrete.multiVariableDeclaration.accept(self)
        MultiVariableDeclarationConcrete.optionalType.accept(self)

    def visitAnonymousFunctionConcrete(self,AnonymousFunctionConcrete):
        AnonymousFunctionConcrete.optinalTypePonto.accept(self)
        AnonymousFunctionConcrete.parametersWithOptionalType.accept(self)
        AnonymousFunctionConcrete.optionalType.accept(self)
        AnonymousFunctionConcrete.optionalTypeConstraints.accept(self)
        AnonymousFunctionConcrete.optionalFunctionBody.accept(self)

    def visitOptinalTypePontoConcrete(self,OptinalTypePontoConcrete):
        OptinalTypePontoConcrete.type.accept(self)

    def visitOptionalTypeConstraintsConcrete(self,OptionalTypeConstraintsConcrete):
        OptionalTypeConstraintsConcrete.typeConstraints.accept(self)

    def visitOptionalFunctionBodyConcrete(self,OptionalFunctionBodyConcrete):
        OptionalFunctionBodyConcrete.functionBody.accept(self)

    def visitTypeConstraint(self,TypeConstraintConcrete):
        TypeConstraintConcrete.simpleIdentifier.accept(self)
        TypeConstraintConcrete.type.accept(self)

    def visitSimpleIfExpression(self,SimpleIfExpression):
        print('if(', end='')
        SimpleIfExpression.expression.accept(self)
        print(')', end='')
        SimpleIfExpression.controlStructureBodyOrPV.accept(self)

    def visitCompoundIfExpression(self,CompoundIfExpression):
        print('if(', end='')
        CompoundIfExpression.expression.accept(self)
        print(')', end='')
        CompoundIfExpression.controlStructureBodyOrPV.accept(self)
        CompoundIfExpression.optionalPV.accept(self)
        CompoundIfExpression.optionalControlStructureBody.accept(self)

    def visitPV(self,PV):
        PV.PV.accept(self)
        print(';')

    def visitControlStructureBody(self,ControlStructureBody):
        ControlStructureBody.controlStructureBody.accept(self)

    def visitReturnConcrete(self,ReturnConcrete):
        ReturnConcrete.expression.accept(self)
        print('Return')

    def visitReturnAtConcrete(self,ReturnAtConcrete):
        ReturnAtConcrete.expression.accept(self)
        print('Return_At')

    def visitContinueConcrete(self,ContinueConcrete):
        ContinueConcrete.accept(self)
        print('Continue')

    def visitContinueAtConcrete(self,ContinueAtConcrete):
        ContinueAtConcrete.accept(self)
        print('Continue_At')

    def visitBreakConcrete(self,BreakConcrete):
        BreakConcrete.accept(self)
        print('Break')

    def visitBreakAtConcrete(self,BreakAtConcrete):
        BreakAtConcrete.accept(self)
        print('Break_At')

    def visitCallableReferenceConcrete(self,CallableReferenceConcrete):
        CallableReferenceConcrete.optionalReceiverType.accept(self)
        CallableReferenceConcrete.simpleIdentifierOrClass.accept(self)

    def visitOptionalReceiverType(self,OptionalReceiverType):
        OptionalReceiverType.receiverType.accept(self)

    def visitClassConcrete(self,ClassConcrete):
        ClassConcrete.CLASS.accept(self)

    def visitMAISIGUAL(self,MAISIGUAL):
        MAISIGUAL.maisIgual.accept(self)
        print('+=')

    def visitMENOSIGUAL(self,MENOSIGUAL):
        MENOSIGUAL.menosIgual.accept(self)
        print('-=')

    def visitMULTIGUAL(self,MULTIGUAL):
        MULTIGUAL.multiIgual.accept(self)
        print('*=')

    def visitDIVIGUAL(self,DIVIGUAL):
        DIVIGUAL.divIgual.accept(self)
        print('/=')

    def visitMODIGUAL(self,MODIGUAL):
        MODIGUAL.modIgual.accept(self)
        print('%=')

    def visitDiferente(self,Diferente):
        Diferente.diferente.accept(self)
        print('!=')

    def visitIdentidade(self,Identidade):
        Identidade.identidade.acccept(self)
        print('===')

    def visitIgualdade(self,Igualdade):
        Igualdade.igualdade.accept(self)
        print('==')

    def visitSemIdentidade(self,SemIdentidade):
        SemIdentidade.semIdentidade.accept(self)
        print('!==')

    def visitMenor(self,Menor):
        Menor.accept(self)
        print('<')

    def visitMAIOR(self,Maior):
        Maior.accept(self)
        print('>')

    def visitMenorIgual(self,MenorIgual):
        MenorIgual.accept(self)
        print('<=')

    def visitMaiorIgual(self,MaiorIgual):
        MaiorIgual.accept(self)
        print('>=')

    def visitIn(self,In):
        In.In.accept(self)
        print('in')

    def visitNotIn(self,NotIn):
        NotIn.notIn.accept(self)
        print('!in')

    def visitNotIs(self,NotIs):
        NotIs.notIs.accept(self)
        print('!is')

    def visitIs(self,Is):
        Is.Is.accept(self)
        print('is')

    def visitPlus(self,Plus):
        Plus.plus.accept(self)
        print('+')

    def visitMINUS(self,Minus):
        Minus.minus.accept(self)
        print('-')

    def visitMult(self,Mult):
        Mult.mult.accept(self)
        print('*')

    def visitMod(self,Mod):
        Mod.mod.accept(self)
        print('%')

    def visitDivide(self,Divide):
        Divide.divide.accept(self)
        print('/')

    def visitSimpleAsOperator(self,SimpleAsOperator):
        SimpleAsOperator.accept(self)

    def visitCompoundAsOperator(self,CompoundAsOperator):
        CompoundAsOperator.asOperator.accept(self)
        print('asOperator')

    def visitNot(self,Not):
        Not.NOT.accept(self)
        print('!')

    def visitIncremento(self,Incremento):
        Incremento.incremento.accept(self)
        print('++')

    def visitDecremento(self,Decremento):
        Decremento.decremento.accept(self)
        print('--')

    def visitPonto(self,Ponto):
        Ponto.ponto.accept(self)
        print('.')

    def visitColonColon(self,ColonColon):
        ColonColon.colonColon.accept(self)
        print('::')

    def visitSafeNavConcrete(self,SafeNavConcrete):
        SafeNavConcrete.safeNav.accept(self)
        print('safeNav')
    









    
    



    

