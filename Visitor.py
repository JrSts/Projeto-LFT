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
        print('functionDeclaration')
    def visitCompoundKotlinFile(self,CompoundKotlinFile ):
        CompoundKotlinFile.functionDeclaration.accept(self)
        print('functionDeclaration')
        CompoundKotlinFile.kotlinFile.accept(self)
        print('kotlinFile')
    def visitFuncrionDeclaration(self, FunctionDeclaration):
        FunctionDeclaration.simpleIdentifier.accept(self)
        print('simpleIdentifier')
        FunctionDeclaration.functionValueParameters.accept(self)
        print('functionValueParameters')
        FunctionDeclaration.optinalType.accept(self)
        print('optinalType')
        FunctionDeclaration.optionalBlock.accept(self)
        print('optionalBlock')
    def visitOptinalType(self,OptinalType):
        OptinalType.type.accept(self)
        print('type')
    def visitOptionalBlock(self,OptionalBlock):
        OptionalBlock.block.accept(self)
        print('block')
    def visitPropertyDeclaration(self, PropertyDeclarationConcrete):
        PropertyDeclarationConcrete.varOrVal.accept(self)
        print('varOrVal')
        PropertyDeclarationConcrete.MvOrV.accept(self)
        print('MvOrV')
        PropertyDeclarationConcrete.optionalTypeParameters.accept(self)
        print('optionalTypeParameters')
        PropertyDeclarationConcrete.optionalPv.accept(self)
        print('optionalPv')
        PropertyDeclarationConcrete.expression.accept(self)
        print('expression')
    def visitMultiVariableDeclaration(self,MultiVariableDeclaration):
        MultiVariableDeclaration.multiVariableDeclaration.accept(self)
        print('multiVariableDeclaration')
    def visitVariableDeclaration(self,VariableDeclaration):
        VariableDeclaration.variableDeclaration.accept(self)
        print('variableDeclaration')
    def visitPd1_var(self,Var):
        Var.var.accept(self)
        print('var')
    def visitPd1_val(self,Val):
        Val.val.accept(self)
        print('val')
    def visitOptionalTypeParameters(self,OptionalTypeParameters):
        OptionalTypeParameters.typeParameters.accept(self)
        print('typeParameters')
    def visitOptionalPv(self,OptionalPv):
        OptionalPv.pv.accept(self)
        print('pv')
    def visitTypePatameters(self,TypeParametersConcrete):
        TypeParametersConcrete.typeParameter.accept(self)
        print('typeParameter')
        TypeParametersConcrete.typeParametersRecursive.accept(self)
        print('typeParametersRecursive')
        TypeParametersConcrete.optionalCOMMA.accept(self)
        print('optionalCOMMA')
    def visitSimpleTypeParameterRecursive(self,SimpleTypeParametersRecursive):
        SimpleTypeParametersRecursive.typeParameter.accept(self)
        print('typeParameter')
    def visitCompoundTypeParametersRecursive(self,CompoundTypeParametersRecursive):
        CompoundTypeParametersRecursive.typeParameter.accept(self)
        print('typeParameter')
        CompoundTypeParametersRecursive.typeParametersRecursive.accept(self)
        print('typeParametersRecursive')
    def visitOptionalCOMMA(self,OptionalCOMMA):
        OptionalCOMMA.COMMA.accept(self)
        print('COMMA')
    def visitSimpleTypePatameter(self,SimpleTypeParameter):
        SimpleTypeParameter.simpleIdentifier.accept(self)
        print('simpleIdentifier')
    def visitCompoundTypePatameter (self,  CompoundTypeParameter):
        CompoundTypeParameter.type.accept(self)
        print('type')
        CompoundTypeParameter.simpleIdentifier.accept(self)
        print('simpleIdentifier')
    def visitSimpleFunctionBody(self, SimpleFunctionBody):
        SimpleFunctionBody.block.accept(self)
        print('block')
    def visitCompoundFunctionBody(self, CompoundFunctionBody):
        CompoundFunctionBody.expression.accept(self)
        print('expression')
    def visitSimpleFunctionValueParameters(self,SimpleFunctionValueParameters):
        SimpleFunctionValueParameters.accept(self)
    def visitCompoundFunctionValueParameters(self,CompoundFunctionValueParameters):
        CompoundFunctionValueParameters.fvps.accept(self)
        print('fvps')
    def visitSimpleFunctionValueParametersRecursive(self,SimpleFunctionValueParametersRecursive):
        SimpleFunctionValueParametersRecursive.fvp.accept(self)
        print('fvp')
        SimpleFunctionValueParametersRecursive.optionalCOMMA.accept(self)
        print('optionalCOMMA')
    def visitCompoundFunctionValueParametersRecursive(self,CompoundFunctionValueParametersRecursive):
        CompoundFunctionValueParametersRecursive.fvp.accept(self)
        print('fvp')
        CompoundFunctionValueParametersRecursive.functionValueParametersRecursive.accept(self)
        print('functionValueParametersRecursive')
    def visitSimpleFunctionValueParameter(self,SimpleFunctionValueParameter):
        SimpleFunctionValueParameter.parameter.accept(self)
        print('parameter')
    def visitCompoundFunctionValueParameter(self,CompoundFunctionValueParameter):
        CompoundFunctionValueParameter.parameter.accept(self)
        print('parameter')
        CompoundFunctionValueParameter.exp.accept(self)
        print('exp')
    def visitSimpleMultiVariableDeclaration(self,SimpleMultiVariableDeclaration):
        SimpleMultiVariableDeclaration.accept(self)
    def visitCompoundMultiVariableDeclaration(self,CompoundMultiVariableDeclaration):
        CompoundMultiVariableDeclaration.mvd.accept(self)
        print('mvd')
    def visitSimpleVariableDeclaration(self,SimpleVariableDeclaration):
        SimpleVariableDeclaration.simpleIdentifier.accept(self)
        print('simpleIdentifier')
    def visitCompoundVariableDeclaration(self,CompoundVariableDeclaration):
        CompoundVariableDeclaration.simpleIdentifier.accept(self)
        print('simpleIdentifier')
        CompoundVariableDeclaration.type.accept(self)
        print('type')
    def visitSimpleMultiVariableDeclarationRecursive(self,SimpleMultiVariableDeclarationRecursive):
        SimpleMultiVariableDeclarationRecursive.variableDeclaration.accept(self)
        print('variableDeclaration')
    def visitCompoundMultiVariableDeclarationRecursive(self,CompoundMultiVariableDeclarationRecursive):
        CompoundMultiVariableDeclarationRecursive.mvd.accept(self)
        print('mvd')
        CompoundMultiVariableDeclarationRecursive.variableDeclaration.accept(self)
        print('variableDeclaration')
    def visitParameter(self,ParameterConcrete):
        ParameterConcrete.simpleIdentifier.accept(self)
        print('simpleIdentifier')
        ParameterConcrete.type.accept(self)
        print('type')
    def visitTypeConcrete(self,TypeConcrete):
        TypeConcrete.optionalTypeModifiers.accept(self)
        print('optionalTypeModifiers')
        TypeConcrete.optype.accept(self)
        print('optype')
    def visitOptionalTypeModifiersConcrete(self,OptionalTypeModifiersConcrete):
        OptionalTypeModifiersConcrete.typeModifiers.accept(self)
        print('typeModifiers')
    def visitParenthesizedType(self,ParenthesizedTypeConcrete):
        ParenthesizedTypeConcrete.type.accept(self)
        print('type')
    def visitFunctionType(self,FunctionType):
        FunctionType.functionType.accept(self)
        print('functionType')
    def visitUserType(self,UserType):
        UserType.simpleUserType.accept(self)
        print('simpleUserType')
    def visitSimpleTypeModifiers(self,SimpleTypeModifiers):
        SimpleTypeModifiers.typeModifier.accept(self)
        print('typeModifier')
    def visitCompoundTypeModifiers(self, CompondTypeModifiers):
        CompondTypeModifiers.typeModifier.accept(self)
        print('typeModifier')
        CompondTypeModifiers.typeModifiers.accept(self)
        print('typeModifiers')
    def visitTypeModifierConcrete(self, TypeModifierConcrete):
        TypeModifierConcrete.suspend.accept(self)
        print('suspend')
    def visitTypeProjectionModifierConcrete(self,TypeProjectionModifierConcrete):
        TypeProjectionModifierConcrete.varianceModifier.accept(self)
        print('varianceModifier')
    def visitVariaceModifierIn(self, In):
        In.IN.accept(self)
        print('IN')
    def visitVariaceModifierOut(self, Out):
        Out.out.accept(self)
        print('out')
    def visitSimpleSimpleUserType(self, SimpleUserTypeConcrete):
        SimpleUserTypeConcrete.accept(self)
    def visitSimpleSimpleUserType(self,SimpleSimpleUserType):
        SimpleSimpleUserType.simpleIdentifier.accept(self)
        print('simpleIdentifier')
    def visitCompoundSimpleUserType(self, CompoundSimpleUserType):
        CompoundSimpleUserType.simpleIdentifier.accept(self)
        print('simpleIdentifier')
        CompoundSimpleUserType.typeArguments.accept(self)
        print('typeArguments')
    def visittypeSimpleProjection(self, SimpleTypeProjection):
        SimpleTypeProjection.type.accept(self)
        print('type')
    def visitCompoundTypeProjection(self,CompoundTypeProjection):
        CompoundTypeProjection.typeProjectionModifiers.accept(self)
        print('typeProjectionModifiers')
        CompoundTypeProjection.type.accept(self)
        print('type')
    def visitSimpleTypeProjectionModifiers(self,SimpleTypeProjectionModifiers):
        SimpleTypeProjectionModifiers.typeProjection.accept(self)
        print('typeProjection')
    def visitCompoundTypeProjectionModifiers(self,CompoundTypeProjectionModifiers):
        CompoundTypeProjectionModifiers.typeProjectionModifier.accept(self)
        print('typeProjectionModifier')
        CompoundTypeProjectionModifiers.typeProjectionModifiers.accept(self)
        print('typeProjectionModifiers')
    def visitSimpleFunctionType(self,SimpleFunctionType):
        SimpleFunctionType.functionTypeParameters.accept(self)
        print('functionTypeParameters')
    def visitCompoundFunctionType(self, CompoundFunctionType):
        CompoundFunctionType.receiverType.accept(self)
        print('receiverType')
        CompoundFunctionType.functionTypeParameters.accept(self)
        print('functionTypeParameters')
        CompoundFunctionType.type.accept(self)
        print('type')
    def visitSFunctionTypeParametersConcrete(self,FunctionTypeParametersConcrete):
        FunctionTypeParametersConcrete.optionalParameterOrType.accept(self)
        print('optionalParameterOrType')
        FunctionTypeParametersConcrete.parameterOrTypeRecursive.accept(self)
        print('parameterOrTypeRecursive')
        FunctionTypeParametersConcrete.optionalCOMMA.accept(self)
        print('optionalCOMMA')
    def visitSimpleParameterOrTypeRecursive(self,SimpleParameterOrTypeRecursive):
        SimpleParameterOrTypeRecursive.optionalParameterOrType.accept(self)
        print('optionalParameterOrType')
    def visitCompoundParameterOrTypeRecursive(self, CompoundParameterOrTypeRecursive):
        CompoundParameterOrTypeRecursive.optionalParameterOrType.accept(self)
        print('optionalParameterOrType')
        CompoundParameterOrTypeRecursive.parameterOrTypeRecursive.accept(self)
        print('parameterOrTypeRecursive')
    def visitReceiverTypeConcrete(self, ReceiverTypeConcrete):
        ReceiverTypeConcrete.typeModifier.accept(self)
        print('typeModifier')
        ReceiverTypeConcrete.parenthesizedType.accept(self)
        print('parenthesizedType')
    def visitSimpleStatemnts(self,SimpleStatements):
        SimpleStatements.statement.accept(self)
        print('statement')
    def visitCompoundStatemnts(self,CompoundStatements):
        CompoundStatements.statement.accept(self)
        print('statement')
        CompoundStatements.statments.accept(self)
        print('statments')
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
        ForStatement_MD.forStatement.accept(self)
        print('forStatement')
    def visitForStatement_VD(self, ForStatement_VD):
        ForStatement_VD.forStatement.accept(self)
        print('forStatement')
    def visitWhileStatement_PV(self,WhileStatement_PV):
        WhileStatement_PV.expression.accept(self)
        print('expression')
    def visitWhileStatement_CBS(self,WhileStatement_CBS):
        WhileStatement_CBS.expression.accept(self)
        print('expression')
        WhileStatement_CBS.controlStructureBody.accept(self)
        print('controlStructureBody')
    def visitWhileStatementD(self,WhileStatement):
        WhileStatement.whileStatement.acccept(self)
        print('whileStatement')
    def visitDoWhileStatement(self, DoWhileStatement):
        DoWhileStatement.doWhileStatement.accept(self)
        print('doWhileStatement')
    def visitSimpleForStatement_MD(self,SimpleForStatement_MD):
        SimpleForStatement_MD.multiVariableDeclaration.accept(self)
        print('multiVariableDeclaration')
        SimpleForStatement_MD.expression.accept('expression')
        print('expression')
    def visitCompoundForStatement_MD(self, CompoundForStatement_MD):
        CompoundForStatement_MD.multiVariableDeclaration.accept(self)
        print('multiVariableDeclaration')
        CompoundForStatement_MD.expression.accept(self)
        print('expression')
        CompoundForStatement_MD.controlStructureBody.accept(self)
        print('controlStructureBody')
    def visitSimpleForStatement_VD(self,SimpleForStatement_VD):
        SimpleForStatement_VD.variableDeclaration.accept(self)
        print('variableDeclaration')
        SimpleForStatement_VD.expression.accept(self)
        print('expression')
    def visitCompoundForStatement_MD(self,CompoundForStatement_VD):
        CompoundForStatement_VD.variableDeclaration.accept(self)
        print('variableDeclaration')
        CompoundForStatement_VD.expression.accept(self)
        print('expression')
        CompoundForStatement_VD.controlStructureBody.accept(self)
        print('controlStructureBody')
    def visitSimpleDoWhileStatement(self, SimpleDoWhileStatement):
        SimpleDoWhileStatement.expression.accept(self)
        print('expression')
    def visitCompoundDoWhileStatement(self,CompoundDoWhileStatement):
        CompoundDoWhileStatement.controlStructureBody.accept(self)
        print('controlStructureBody')
        CompoundDoWhileStatement.expression.accept(self)
        print('expression')
    def visitAssignmentConcrete(self,AssignmentConcrete):
        AssignmentConcrete.directlyAssignableExpression.accept(self)
        print('directlyAssignableExpression')
        AssignmentConcrete.expression.accept(self)
        print('expression')
    def visitAssignmentAndOperatorConcrete(self,AssignmentAndOperatorConcrete):
        AssignmentAndOperatorConcrete.assignmentAndOperator.accept(self)
        print('assignmentAndOperator')
        AssignmentAndOperatorConcrete.expression.accept(self)
        print('expression')
        AssignmentAndOperatorConcrete.assignableExpression.accept(self)
        print('assignableExpression')
    def visitDisjunctionConcrete(self,DisjunctionConcrete):
        DisjunctionConcrete.accept(self)
    def visitSimpleDisjunction(self,SimpleDisjunction):
        SimpleDisjunction.conjunction.accept(self)
        print('conjunction')
    def visitCompoundDisjunction(self,CompoundDisjunction):
        CompoundDisjunction.conjunction.accept(self)
        print('conjunction')
        CompoundDisjunction.disjunction.accept(self)
        print('disjunction')
    def vistSimpleConjunction(self, SimpleConjunction):
        SimpleConjunction.equality.accept(self)
        print('equality')
    def vistCompoundConjunction(self,CompoundConjunction):
        CompoundConjunction.equality.accept(self)
        print('equality')
        CompoundConjunction.conjunction.accept(self)
        print('conjunction')
    def visitSimpleEquality(self,SimpleEquality):
        SimpleEquality.comparison.accept(self)
        print('comparison')
    def visitCompoundEquality(self,CompoundEquality):
        CompoundEquality.comparison.accept(self)
        print('comparison')
        CompoundEquality.equalityOperator.accept(self)
        print('equalityOperator')
        CompoundEquality.equality.accept(self)
        print('equality')
    def vistSimpleComparison(self,SimpleComparison):
        SimpleComparison.infixOperation.accept(self)
        print('infixOperation')
    def vistCompoundComparison(self,CompoundComparison):
        CompoundComparison.infixOperation.accept(self)
        print('infixOperation')
        CompoundComparison.comparisonOperator.accept(self)
        print('comparisonOperator')
    def visitSimpleInfixOperation(self,SimpleInfixOperation):
        SimpleInfixOperation.elvisExpression.accept(self)
        print('elvisExpression')
    def visitCompoundInfixOperation(self,CompoundInfixOperation):
        CompoundInfixOperation.elvisExpression.accept(self)
        print('elvisExpression')
        CompoundInfixOperation.infixOperationRecursive.accept(self)
        print('infixOperationRecursive')
    def visitSimpleInfixOperationRecursive(self,SimpleInfixOperationRecursive):
        SimpleInfixOperationRecursive.inOrIs.accept(self)
        print('inOrIs')
        SimpleInfixOperationRecursive.elvisOrType.accept(self)
        print('elvisOrType')
    def visitCompoundInfixOperationRecursive(self, CompoundInfixOperationRecursive):
        CompoundInfixOperationRecursive.inOrIs.accept(self)
        print('inOrIs')
        CompoundInfixOperationRecursive.elvisOrType.accept(self)
        print('elvisOrType')
        CompoundInfixOperationRecursive.infixOperationRecursive.accept(self)
        print('infixOperationRecursive')
    def visitInOperator(self, InOperator):
        InOperator.In.accept(self)
        print('In')
    def visitIsOperator(self,IsOperator):
        IsOperator.Is.accept(self)
        print('Is')
    def visitElvisExpressionConcrete(self,ElvisExpressionConcrete):
        ElvisExpressionConcrete.elvisExpression.accept(self)
        print('elvisExpression')
    def visitSimpleElvisExpression(self,SimpleElvisExpression):
        SimpleElvisExpression.infixFunctionCall.accept(self)
        print('infixFunctionCall')
    def visitCompoundElvisExpression(self,CompoundElvisExpression):
        CompoundElvisExpression.infixFunctionCall.accept(self)
        print('infixFunctionCall')
        CompoundElvisExpression.elvisExpression.accept(self)
        print('elvisExpression')
    def visitSimpleInfixFunctionCall(self,SimpleInfixFunctionCall):
        SimpleInfixFunctionCall.rangeExpression.accept(self)
        print('rangeExpression')
    def visitCompoundInfixFunctionCall(self, CompoundInfixFunctionCall):
        CompoundInfixFunctionCall.rangeExpression.accept(self)
        print('rangeExpression')
        CompoundInfixFunctionCall.simpleIdentifier.accept(self)
        print('simpleIdentifier')
        CompoundInfixFunctionCall.infixFunctionCall.accept(self)
        print('infixFunctionCall')
    def visitSimpleRangeExpression(self, SimpleRangeExpression):
        SimpleRangeExpression.additiveExpression.accept(self)
        print('additiveExpression')
    def visitCompoundRangeExpression(self,CompoundRangeExpression):
        CompoundRangeExpression.additiveExpression.accept(self)
        print('additiveExpression')
        CompoundRangeExpression.rangeExpression.accept(self)
        print('rangeExpression')
    def visitSimpleAdditiveExpression(self,SimpleAdditiveExpression):
        SimpleAdditiveExpression.multiplicativeExpression.accept(self)
        print('multiplicativeExpression')
    def visitCompoundAdditiveExpression(self,CompoundAdditiveExpression):
        CompoundAdditiveExpression.multiplicativeExpression.accept(self)
        print('multiplicativeExpression')
        CompoundAdditiveExpression.additiveOperator.accept(self)
        print('additiveOperator')
        CompoundAdditiveExpression.additiveExpression.accept(self)
        print('additiveExpression')
    def visitSimpleMultiplicativeExpression(self,SimpleMultiplicativeExpression):
        SimpleMultiplicativeExpression.asExpression.accept(self)
        print('asExpression')
    def visitCompoundMultiplicativeExpression(self,CompoundMultiplicativeExpression):
        CompoundMultiplicativeExpression.asExpression.accept(self)
        print('asExpression')
        CompoundMultiplicativeExpression.multiplicativeOperator.accept(self)
        print('multiplicativeOperator')
        CompoundMultiplicativeExpression.multiplicativeExpression.accept(self)
        print('multiplicativeExpression')
    def visitSimpleAsExpression(self,SimpleAsExpression):
        SimpleAsExpression.prefixUnaryExpression.accept(self)
        print('prefixUnaryExpression')
    def visitCompoundAsExpression(self,CompoundAsExpression):
        CompoundAsExpression.prefixUnaryExpression.accept(self)
        print('prefixUnaryExpression')
        CompoundAsExpression.asOperator.accept(self)
        print('asOperator')
        CompoundAsExpression.type.accept(self)
        print('type')
    def visitSimplePrefixUnaryExpression(self,SimplePrefixUnaryExpression):
        SimplePrefixUnaryExpression.postfixUnaryExpression.accept(self)
        print('postfixUnaryExpression')
    def visitCompoundPrefixUnaryExpression(self,CompoundPrefixUnaryExpression):
        CompoundPrefixUnaryExpression.prefixUnaryExpressionRecursive.accept(self)
        print('prefixUnaryExpressionRecursive')
        CompoundPrefixUnaryExpression.postfixUnaryExpression.accept(self)
        print('postfixUnaryExpression')
    def visitSimplePrefixUnaryExpressionRecursive(self,SimplePrefixUnaryExpressionRecursive):
        SimplePrefixUnaryExpressionRecursive.unaryPrefix.accept(self)
        print('unaryPrefix')
    def visitCompoundPrefixUnaryExpressionRecursive(self,CompoundPrefixUnaryExpressionRecursive):
        CompoundPrefixUnaryExpressionRecursive.unaryPrefix.accept(self)
        print('unaryPrefix')
        CompoundPrefixUnaryExpressionRecursive.prefixUnaryExpressionRecursive.accept(self)
        print('prefixUnaryExpressionRecursive')
    def visitPrefixUnaryOperatorConcrete(self,PrefixUnaryOperatorConcrete):
        PrefixUnaryOperatorConcrete.prefixUnaryOperator.accept(self)
        print('prefixUnaryOperator')
    def visitLabelConcrete(self,LabelConcrete):
        LabelConcrete.label.accept(self)
        print('label')
    def visitSimplePostfixUnaryExpression(self,SimplePostfixUnaryExpression):
        SimplePostfixUnaryExpression.primaryExpression.accept(self)
        print('primaryExpression')
    def visitCompoundPostfixUnaryExpression(self,CompoundPostfixUnaryExpression):
        CompoundPostfixUnaryExpression.primaryExpression.accept(self)
        print('primaryExpression')
        CompoundPostfixUnaryExpression.postfixUnaryExpressionRecursive.accept(self)
        print('postfixUnaryExpressionRecursive')
    def visitSinglePostfixUnaryExpressionRecursive(self,SinglePostfixUnaryExpressionRecursive):
        SinglePostfixUnaryExpressionRecursive.postfixUnarySuffix.accept(self)
        print('postfixUnarySuffix')
    def visitCompoundPostfixUnaryExpressionRecursive(self,CompoundPostfixUnaryExpressionRecursive):
        CompoundPostfixUnaryExpressionRecursive.postfixUnarySuffix.accept(self)
        print('postfixUnarySuffix')
        CompoundPostfixUnaryExpressionRecursive.postfixUnaryExpression.accept(self)
        print('postfixUnaryExpression')
    def visitPostfixUnaryOperatorConcrete(self,PostfixUnaryOperatorConcrete):
        PostfixUnaryOperatorConcrete.postfixUnaryOperator.accept(self)
        print('postfixUnaryOperator')
    def visitTypeArgumentsConcrete(self,TypeArgumentsConcrete):
        TypeArgumentsConcrete.typeArguments.accept(self)
        print('typeArguments')
    def visitCallSuffixConcrete(self,CallSuffixConcrete):
        CallSuffixConcrete.callSuffix.accept(self)
        print('callSuffix')
    def visitIndexingSuffixConcrete(self,IndexingSuffixConcrete):
        IndexingSuffixConcrete.indexingSuffix.accept(self)
        print('indexingSuffix')
    def visitNavigationSuffixConcrete(self,NavigationSuffixConcrete):
        NavigationSuffixConcrete.navigationSuffix.accept(self)
        print('navigationSuffix')
    def visitIncremento(self,Incremento):
        Incremento.incremento.accept(self)
        print('incremento')
    def visitDecremento(self,Decremento):
        Decremento.decremento.accept(self)
        print('decremento')
    def visitSimpleTypeArguments(self,SimpleTypeArguments):
        SimpleTypeArguments.accept(self)
    def visitTa(self,Ta):
        Ta.ta.accept(self)
        print('ta')
        Ta.typePtojection.accept(self)
        print('typePtojection')
    def visitIndexingSuffix(self,IndexingSuffix):
        IndexingSuffix.indexingSuffix.accept(self)
        print('indexingSuffix')
    def visitCallSuffix(self,CallSuffix):
        CallSuffix.callSuffix.accept(self)
        print('callSuffix')
    def visitSimpleIdentifier(self,SimpleIdentifier):
        SimpleIdentifier.simpleIdentifier.accept(self)
        print('simpleIdentifier')
    def visitParenthesizedDirectlyAssignableExpression(self,ParenthesizedDirectlyAssignableExpression):
        ParenthesizedDirectlyAssignableExpression.ParenthesizedDirectlyAssignableExpression.accept(self)
        print('ParenthesizedDirectlyAssignableExpression')
    def visitSimpleDirectlyAssignableExpression(self,SimpleDirectlyAssignableExpression):
        SimpleDirectlyAssignableExpression.simpleIdentifier.accept(self)
        print('simpleIdentifier')
    def visitParenthesizedDirectlyAssignableExpressionConcrete(self,ParenthesizedDirectlyAssignableExpressionConcrete):
        ParenthesizedDirectlyAssignableExpressionConcrete.directlyAssignableExpression.accept(self)
        print('directlyAssignableExpression')
    def visitParenthesizedAssignableExpressionConcrete(self,ParenthesizedAssignableExpressionConcrete):
        ParenthesizedAssignableExpressionConcrete.parenthesizedAssignableExpression.accept(self)
        print('parenthesizedAssignableExpression')
    def visitPrefixUnaryExpressionConcrete(self,PrefixUnaryExpressionConcrete):
        PrefixUnaryExpressionConcrete.prefixUnaryExpression.accept(self)
        print('prefixUnaryExpression')
    def visitAssignableExpressionConcrete(self,AssignableExpressionConcrete):
        AssignableExpressionConcrete.assignableExpression.accept(self)
        print('assignableExpression')
    def visitSimpleIndexingSuffix(self,SimpleIndexingSuffix):
        SimpleIndexingSuffix.accept(self)
    def visitCompoundIndexingSuffix(self,CompoundIndexingSuffix):
        CompoundIndexingSuffix.indexingSuffix.accept(self)
        print('indexingSuffix')
    def visitSimpleIndexingSuffixRecursive(self,SimpleIndexingSuffixRecursive):
        SimpleIndexingSuffixRecursive.expression.accept(self)
        print('expression')
    def visitSimpleIndexingSuffixRecursive(self,CompoundIndexingSuffixRecursive):
        CompoundIndexingSuffixRecursive.expression.accept(self)
        print('expression')
        CompoundIndexingSuffixRecursive.indexingSuffix.accept(self)
        print('indexingSuffix')
    def visitparenthesizedExpressionConcrete(self,ParenthesizedExpressionConcrete):
        ParenthesizedExpressionConcrete.expression.accept(self)
        print('expression')
    def visitSimpleCallSuffixConcrete(self,SimpleCallSuffixConcrete):
        SimpleCallSuffixConcrete.optionalTypeArguments.accept(self)
        print('optionalTypeArguments')
        SimpleCallSuffixConcrete.optionalValueArguments.accept(self)
        print('optionalValueArguments')
    def visitCompoundCallSuffixConcrete(self,CompoundCallSuffixConcrete):
        CompoundCallSuffixConcrete.optionalTypeArguments.accept(self)
        print('optionalTypeArguments')
        CompoundCallSuffixConcrete.optionalValueArguments.accept(self)
        print('optionalValueArguments')
        CompoundCallSuffixConcrete.annotatedLambda.accept(self)
        print('annotatedLambda')
    def visitValueArgumentsConcrete(self,ValueArgumentsConcrete):
        ValueArgumentsConcrete.valueArguments.accept(self)
        print('valueArguments')
    def visitAnnotatedLambdaConcrete(self,TypeArgumentsConcrete):
        TypeArgumentsConcrete.typeArguments.accept(self)
        print('typeArguments')
        TypeArgumentsConcrete.valueArguments.accept(self)
        print('valueArguments')
        TypeArgumentsConcrete.annotatedLambda.accept(self)
        print('annotatedLambda')
    def visitLambdaLiteralConcrete(self,LambdaLiteralConcrete):
        LambdaLiteralConcrete.lambdaLiteral.accept(self)
        print('lambdaLiteral')
    def visitSimpleTypeArguments(self,SimpleTypeArguments):
        SimpleTypeArguments.accept(self)
    def visitCompoundTypeArguments(self,CompoundTypeArguments):
        CompoundTypeArguments.typeArgumentsRecursive.accept(self)
        print('typeArgumentsRecursive')
    def visitSimpleTypeArgumentsRecursive(self,SimpleTypeArgumentsRecursive):
        SimpleTypeArgumentsRecursive.typeProjection.accept(self)
        print('typeProjection')
    def visitCompoundCompoundTypeArgumentsRecursive(self,CompoundTypeArgumentsRecursive):
        CompoundTypeArgumentsRecursive.typeProjection.accept(self)
        print('typeProjection')
        CompoundTypeArgumentsRecursive.typeArgumentsRecursive.accept(self)
        print('typeArgumentsRecursive')
    def visitSimpleValueArguments(self,SimpleValueArguments):
        SimpleValueArguments.accept(self)
    def visitCompoundValueArguments(self,CompoundValueArguments):
        CompoundValueArguments.valueArgumentsRecursive.accept(self)
        print('valueArgumentsRecursive')
    def visitSimpleValueArgumentsRecursive(self,SimpleValueArgumentsRecursive):
        SimpleValueArgumentsRecursive.valueArgument.accept(self)
        print('valueArgument')
    def visitCompoundValueArgumentsRecursive(self,CompoundValueArgumentsRecursive):
        CompoundValueArgumentsRecursive.valueArgument.accept(self)
        print('valueArgument')
        CompoundValueArgumentsRecursive.valueArgumentsRecursive.accept(self)
        print('valueArgumentsRecursive')
    def visitSimpleValueArgument(self,SimpleValueArgument):
        SimpleValueArgument.simpleIdentifier.accept(self)
        print('simpleIdentifier')
    def visitCompound1ValueArgument(self,Compound1ValueArgument):
        Compound1ValueArgument.simpleIdentifier.accept(self)
        print('simpleIdentifier')
        Compound1ValueArgument.expression.accept(self)
        print('expression')
    def visitCompound2ValueArgument(self,Compound2ValueArgument):
        Compound2ValueArgument.simpleIdentifier.accept(self)
        print('simpleIdentifier')
        Compound2ValueArgument.expression.accept(self)
        print('expression')
    def visitLITERAL_STRINGConcrete(self,LITERAL_STRINGConcrete):
        LITERAL_STRINGConcrete.LITERAL_STRING.accept(self)
        print('LITERAL_STRING')
    def visitableReferenceConcrete(self,CallableReferenceConcrete):
        CallableReferenceConcrete.callableReference.accept(self)
        print('callableReference')
    def visitFunctionLiteralConcrete(self,FunctionLiteralConcrete):
        FunctionLiteralConcrete.functionLiteral.accept(self)
        print('functionLiteral')
    def CollectionLiteralConcrete(self,CollectionLiteralConcrete):
        CollectionLiteralConcrete.collectionLiteral.accept(self)
        print('collectionLiteral')
    def visitIfExpressionConcrete(self,IfExpressionConcrete):
        IfExpressionConcrete.ifExpression.accept(self)
        print('ifExpression')
    def visitJumpExpressionConcrete(self,JumpExpressionConcrete):
        JumpExpressionConcrete.jumpExpression.accept(self)
        print('jumpExpression')
    def visitSimpleCollectionLiteral(self,SimpleCollectionLiteral):
        SimpleCollectionLiteral.accept(self)
    def visitCompoundCollectionLiteral(self,CompoundCollectionLiteral):
        CompoundCollectionLiteral.collectionLiteralRecursive.accept(self)
        print('collectionLiteralRecursive')
    def visitSimpleCollectionLiteralRecursive(self,SimpleCollectionLiteralRecursive):
        SimpleCollectionLiteralRecursive.expression.accept(self)
        print('expression')
    def visitCompoundCollectionLiteralRecursive(self,CompoundCollectionLiteralRecursive):
        CompoundCollectionLiteralRecursive.expression.accept(self)
        print('expression')
        CompoundCollectionLiteralRecursive.collectionLiteralRecursive.accept(self)
        print('collectionLiteralRecursive')
    def visitSimpleParametersWithOptionalType(self,SimpleParametersWithOptionalType):
        SimpleParametersWithOptionalType.accept(self)
    def visitCompoundParametersWithOptionalType(self,CompoundParametersWithOptionalType):
        CompoundParametersWithOptionalType.parametersWithOptionalTypeRecursive.accept(self)
        print('parametersWithOptionalTypeRecursive')
    def visitSimpleParametersWithOptionalTypeRecursive(self,SimpleParametersWithOptionalTypeRecursive):
        SimpleParametersWithOptionalTypeRecursive.parameterWithOptionalType.accept(self)
        print('parameterWithOptionalType')
    def visitCompoundParametersWithOptionalTypeRecursive(self,CompoundPwot):
        CompoundPwot.parameterWithOptionalType.accept(self)
        print('parameterWithOptionalType')
        CompoundPwot.parametersWithOptionalTypeRecursive.accept(self)
        print('parametersWithOptionalTypeRecursive')
    def visitParameterWithOptionalTypeConcrete(self,ParameterWithOptionalTypeConcrete):
        ParameterWithOptionalTypeConcrete.simpleIdentifier.accept(self)
        print('simpleIdentifier')
        ParameterWithOptionalTypeConcrete.optionalParameterModifiers.accept(self)
        print('optionalParameterModifiers')
        ParameterWithOptionalTypeConcrete.optionalType.accept(self)
        print('optionalType')
    def visitParameterWithOptionalTypeConcrete(self,OptionalParameterModifiersConcrete):
        OptionalParameterModifiersConcrete.parameterModifiers.acccept(self)
        print('parameterModifiers')
    def visitVararg(self,VarargConcrete):
        VarargConcrete.accept(self)
    def visitNoinline(self,NoinlineConcrete):
        NoinlineConcrete.accept(self)
    def visitCrossinline(self,CrossinlineConcrete):
        CrossinlineConcrete.accept(self)
    def visitlambdaLiteral(self,LambdaLiteral):
        LambdaLiteral.optionsLambdaLiteral.accept(self)
        print('optionsLambdaLiteral')
    def visitSimpleOptionsLambdaLiteral(self,SimpleOptionsLambdaLiteral):
        SimpleOptionsLambdaLiteral.statements.accept(self)
        print('statements')
    def visitCompound1OptionsLambdaLiteral(self,Compound1OptionsLambdaLiteral):
        Compound1OptionsLambdaLiteral.statements.accept(self)
        print('statements')
    def visitCompound2OptionsLambdaLiteral(self,Compound2OptionsLambdaLiteral):
        Compound2OptionsLambdaLiteral.lambdaParameters.accept(self)
        print('lambdaParameters')
        Compound2OptionsLambdaLiteral.statements.accept(self)
        print('statements')
    def visitSimpleLambdaParameters(self,SimpleLambdaParameters):
        SimpleLambdaParameters.lambdaParameter.accept(self)
        print('lambdaParameter')
    def visitCompoundLambdaParameters(self,CompoundLambdaParameters):
        CompoundLambdaParameters.lambdaParameter.accept(self)
        print('lambdaParameter')
        CompoundLambdaParameters.lambdaParameters.accept(self)
        print('lambdaParameters')
    def visitVariableDeclaration(self,VariableDeclarationConcrete):
        VariableDeclarationConcrete.multiVariableDeclaration.accept(self)
        print('multiVariableDeclaration')
    def visitCompoundLambdaParameter(self,MultiVariableDeclarationConcrete):
        MultiVariableDeclarationConcrete.multiVariableDeclaration.accept(self)
        print('multiVariableDeclaration')
        MultiVariableDeclarationConcrete.optionalType.accept(self)
        print('optionalType')
    def visitAnonymousFunctionConcrete(self,AnonymousFunctionConcrete):
        AnonymousFunctionConcrete.optinalTypePonto.accept(self)
        print('optinalTypePonto')
        AnonymousFunctionConcrete.parametersWithOptionalType.accept(self)
        print('parametersWithOptionalType')
        AnonymousFunctionConcrete.optionalType.accept(self)
        print('optionalType')
        AnonymousFunctionConcrete.optionalTypeConstraints.accept(self)
        print('optionalTypeConstraints')
        AnonymousFunctionConcrete.optionalFunctionBody.accept(self)
        print('optionalFunctionBody')
    def visitOptinalTypePontoConcrete(self,OptinalTypePontoConcrete):
        OptinalTypePontoConcrete.type.accept(self)
        print('type')
    def visitOptionalTypeConstraintsConcrete(self,OptionalTypeConstraintsConcrete):
        OptionalTypeConstraintsConcrete.typeConstraints.accept(self)
        print('typeConstraints')
    def visitOptionalFunctionBodyConcrete(self,OptionalFunctionBodyConcrete):
        OptionalFunctionBodyConcrete.functionBody.accept(self)
        print('functionBody')
    def visitTypeConstraint(self,TypeConstraintConcrete):
        TypeConstraintConcrete.simpleIdentifier.accept(self)
        print('simpleIdentifier')
        TypeConstraintConcrete.type.accept(self)
        print('type')
    def visitSimpleIfExpression(self,SimpleIfExpression):
        SimpleIfExpression.expression.accept(self)
        print('expression')
        SimpleIfExpression.controlStructureBodyOrPV.accept(self)
        print('controlStructureBodyOrPV')
    def visitSimpleIfExpression(self,CompoundIfExpression):
        CompoundIfExpression.expression.accept(self)
        print('expression')
        CompoundIfExpression.controlStructureBodyOrPV.accept(self)
        print('controlStructureBodyOrPV')
        CompoundIfExpression.optionalPV.accept(self)
        print('optionalPV')
        CompoundIfExpression.optionalControlStructureBody.accept(self)
        print('optionalControlStructureBody')
    def visitPV(self,PV):
        PV.PV.accept(self)
        print('PV')
    def visitControlStructureBody(self,ControlStructureBody):
        ControlStructureBody.controlStructureBody.accept(self)
        print('controlStructureBody')
    def visitReturnConcrete(self,ReturnConcrete):
        ReturnConcrete.expression.accept(self)
        print('expression')
    def visitReturnAtConcrete(self,ReturnAtConcrete):
        ReturnAtConcrete.expression.accept(self)
        print('expression')
    def visitContinueConcrete(self,ContinueConcrete):
        ContinueConcrete.accept(self)
    def visitContinueAtConcrete(self,ContinueAtConcrete):
        ContinueAtConcrete.accept(self)
    def visitBreakConcrete(self,BreakConcrete):
        BreakConcrete.accept(self)
    def visitBreakAtConcrete(self,BreakAtConcrete):
        BreakAtConcrete.accept(self)
    def visitCallableReferenceConcrete(self,CallableReferenceConcrete):
        CallableReferenceConcrete.optionalReceiverType.accept(self)
        print('optionalReceiverType')
        CallableReferenceConcrete.simpleIdentifierOrClass.accept(self)
        print('simpleIdentifierOrClass')
    def visitCallableReferenceConcrete(self,OptionalReceiverType):
        OptionalReceiverType.receiverType.accept(self)
        print('receiverType')
    def visitClassConcrete(self,ClassConcrete):
        ClassConcrete.CLASS.accept(self)
        print('CLASS')
    def visitMAISIGUAL(self,MAISIGUAL):
        MAISIGUAL.maisIgual.accept(self)
        print('maisIgual')
    def visitMENOSIGUAL(self,):
        MENOSIGUAL.menosIgual.accept(self)
        print('menosIgual')
    def visitMULTIGUAL(self,MULTIGUAL):
        MULTIGUAL.multiIgual.accept(self)
        print('multiIgual')
    def visitDIVIGUAL(self,DIVIGUAL):
        DIVIGUAL.divIgual.accept(self)
        print('divIgual')
    def visitMODIGUAL(self,MODIGUAL):
        MODIGUAL.modIgual.accept(self)
        print('modIgual')
    def visitDiferente(self,Diferente):
        Diferente.diferente.accept(self)
        print('Diferente')
    def visitIdentidade(self,Identidade):
        Identidade.identidade.acccept(self)
        print('identidade')
    def visitIgualdade(self,Igualdade):
        Igualdade.igualdade.accept(self)
        print('igualdade')
    def visitSemIdentidade(self,SemIdentidade):
        SemIdentidade.semIdentidade.accept(self)
        print('semIdentidade')
    def visitMenor(self,Menor):
        Menor.accept(self)
    def visitMAIOR(self,Maior):
        Maior.accept(self)
    def visitMenorIgual(self,MenorIgual):
        MenorIgual.accept(self)
    def visitMaiorIgual(self,MaiorIgual):
        MaiorIgual.accept(self)
    def visitIn(self,In):
        In.In.accept(self)
        print('In')
    def visitNotIn(self,NotIn):
        NotIn.notIn.accept(self)
        print('notIn')
    def visitNotIs(self,NotIs):
        NotIs.notIs.accept(self)
        print('notIs')
    def visitIs(self,Is):
        Is.Is.accept(self)
        print('Is')
    def visitPlus(self,Plus):
        Plus.plus.accept(self)
        print('plus')
    def visitMINUS(self,Minus):
        Minus.minus.accept(self)
        print('minus')
    def visitMult(self,Mult):
        Mult.mult.accept(self)
    def visitMod(self,Mod):
        Mod.mod.accept(self)
        print('mod')
    def visitDivide(self,Divide):
        Divide.divide.accept(self)
        print('divide')
    def visitSimpleAsOperator(self,SimpleAsOperator):
        SimpleAsOperator.accept(self)
    def visitCompoundAsOperator(self,CompoundAsOperator):
        CompoundAsOperator.asOperator.accept(self)
        print('asOperator')
    def visitNot(self,Not):
        Not.NOT.accept(self)
        print('NOT')
    def visitIncremento(self,Incremento):
        Incremento.incremento.accept(self)
        print('incremento')
    def visitDecremento(self,Decremento):
        Decremento.decremento.accept(self)
        print('decremento')
    def visitPonto(self,Ponto):
        Ponto.ponto.accept(self)
        print('ponto')
    def visitColonColon(self,ColonColon):
        ColonColon.colonColon.accept(self)
        print('colonColon')
    def visitSafeNavConcrete(self,SafeNavConcrete):
        SafeNavConcrete.safeNav.accept(self)
        print('safeNav')
    









    
    



    

