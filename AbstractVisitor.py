from abc import abstractmethod
from abc import ABCMeta

class AbstractVisitor(metaclass=ABCMeta):

    # @abstractmethod
    # def visitSimpleKotlinFile(self, KotlinFile):
    #     pass

    @abstractmethod
    def visitCompoundKotlinFile(self,KotlinFile):
        pass

    @abstractmethod
    def visitSimpleFunctionDeclaration(self,FunctionDeclaration):
        pass

    @abstractmethod
    def visitCompoundFunctionDeclaration(self,FunctionDeclaration):
        pass


    @abstractmethod
    def visitSimpleFunctionValueParameters(self,SimpleFunctionValueParameters):
        pass

    @abstractmethod
    def visitCompoundFunctionValueParameters(self,CompoundFunctionValueParameters):
        pass

    # @abstractmethod
    # def visitSimpleParameters(self, Parameters):
    #     pass

    @abstractmethod
    def visitCompoundParameters(self, Parameters):
        pass


    @abstractmethod
    def visitSimpleParameter(self, Parameter):
        pass

    # @abstractmethod
    # def visitCompoundParameter(self, Parameter):
    #     pass

    @abstractmethod
    def visitParenthesizedTypeConcrete(self, ParenthesizedType):
        pass

    # @abstractmethod
    # def visitSimpleFunctionBody(self, FunctionBody):
    #     pass

    @abstractmethod
    def visitCompoundFunctionBody(self, FunctionBody):
        pass

    # @abstractmethod
    # def visitSimpleStatements(self, Statements):
    #     pass

    @abstractmethod
    def visitCompoundStatements(self, Statements):
        pass


    @abstractmethod
    def visitIf_statement(self, Open_statement):
        pass

    @abstractmethod
    def visitIf_block(self, Open_statement):
        pass

    @abstractmethod
    def visitWhile_Open_statement(self, Open_statement):
        pass

    @abstractmethod
    def visitSimpleIf_else(self, Open_statement):
        pass

    @abstractmethod
    def visitCompoundIf_else(self, Open_statement):
        pass

    @abstractmethod
    def visitFor_Open_statement(self, Open_statement):
        pass

    @abstractmethod
    def visitDoWhile_Open_statement(self, Open_statement):
        pass

    @abstractmethod
    def visitIf_Blocks_Closed_statement(self, Closed_statement):
        pass

    @abstractmethod
    def visitIf_Mix1_Closed_statement(self, Closed_statement):
        pass

    @abstractmethod
    def visitIf_Mix2_Closed_statement(self, Closed_statement):
        pass

    @abstractmethod
    def visitIf_Closeds_Closed_statement(self, Closed_statement):
        pass

    @abstractmethod
    def visitFor_Closed_statement(self, Closed_statement):
        pass

    @abstractmethod
    def visitWhile_Closed_statement(self, Closed_statement):
        pass

    @abstractmethod
    def visitDoWhile_Closed_statement(self, Closed_statement):
        pass

    @abstractmethod
    def visitFor_Non_if_statement_block(self, Non_if_statement_block):
        pass

    @abstractmethod
    def visitWhile_Non_if_statement_block(self, Non_if_statement_block):
        pass

    @abstractmethod
    def visitDoWhile_Non_if_statement_block(self, Non_if_statement_block):
        pass

    @abstractmethod
    def visitAssignmentConcrete(self,Assignment):
        pass

    @abstractmethod
    def visitAssignmentAndOperatorConcrete(self, AssignmentAndOperator):
        pass

    @abstractmethod
    def visitBlockConcrete(self, Block):
        pass

    @abstractmethod
    def visitPropertyDeclarationStm_Var(self, PropertyDeclarationStm):
        pass

    @abstractmethod
    def visitPropertyDeclarationStm_Val(self, PropertyDeclarationStm):
        pass

    @abstractmethod
    def visitSimpleChamadaDeFuncao(self, ChamadaDeFuncao):
        pass

    @abstractmethod
    def visitCompoundChamadaDeFuncao(self, ChamadaDeFuncao):
        pass

    # @abstractmethod
    # def visitSimpleVariableDeclaration(self, VariableDeclaration):
    #     pass

    @abstractmethod
    def visitCompoundVariableDeclaration(self, VariableDeclaration):
        pass

    # @abstractmethod
    # def visitSimpleVariableDeclarations(self, VariableDeclarations):
    #     pass

    @abstractmethod
    def visitCompoundVariableDeclarations(self, VariableDeclarations):
        pass

    @abstractmethod
    def visitSimpleMultiVariableDeclaration(self, VariableDeclaration):
        pass

    @abstractmethod
    def visitCompoundMultiVariableDeclaration(self, VariableDeclaration):
        pass

    # @abstractmethod
    # def visitSimpleParametersFunction(self, ParametersFunction):
    #     pass

    @abstractmethod
    def visitCompoundParametersFunction(self, ParametersFunction):
        pass

    # @abstractmethod
    # def visitSimpleDisjunction(self, Disjunction):
    #     pass

    @abstractmethod
    def visitCompoundDisjunction(self, Disjunction):
        pass

    # @abstractmethod
    # def visitSimpleEquality(self,SimpleEquality):
    #     pass

    @abstractmethod
    def visitCompoundEquality(self,CompoundEquality):
        pass


    # @abstractmethod
    # def visitSimpleComparison(self,SimpleComparison):
    #     pass

    @abstractmethod
    def visitCompoundComparison(self,CompoundComparison):
        pass

    @abstractmethod
    def visitSimpleInfixOperation(self,SimpleInfixOperation):
        pass

    @abstractmethod
    def visitCompoundInfixOperation(self,CompoundInfixOperation):
        pass

    # @abstractmethod
    # def visitSimpleElvisExpression(self,SimpleElvisExpression):
    #     pass

    @abstractmethod
    def visitCompoundElvisExpression(self,CompoundElvisExpression):
        pass

    # @abstractmethod
    # def visitSimpleRangeExpression(self,SimpleRangeExpression):
    #     pass

    @abstractmethod
    def visitCompoundRangeExpression(self,CompoundRangeExpression):
        pass

    # @abstractmethod
    # def visitSimpleAdditiveExpression(self,SimpleAdditiveExpression):
    #     pass

    @abstractmethod
    def visitCompoundAdditiveExpression(self,CompoundAdditiveExpression):
        pass

    # @abstractmethod
    # def visitSimpleMultiplicativeExpression(self,SimpleMultiplicativeExpression):
    #     pass

    @abstractmethod
    def visitCompoundMultiplicativeExpression(self,CompoundMultiplicativeExpression):
        pass

    # @abstractmethod
    # def visitSimpleAsExpression(self,SimpleAsExpression):
    #     pass

    @abstractmethod
    def visitCompoundAsExpression(self,CompoundAsExpression):
        pass

    @abstractmethod
    def visitSimpleUnaryExpressionConcrete(self, UnaryExpression):
        pass

    @abstractmethod
    def visitCompoundUnaryExpressionConcrete(self, UnaryExpression):
        pass

    @abstractmethod
    def visitIncremento(self,Incremento):
        pass

    @abstractmethod
    def visitDecremento(self,Decremento):
        pass

    @abstractmethod
    def visitReturn(self, Return):
        pass

    @abstractmethod
    def visitParenthesizedExpressionConcrete(self, ParenthesizedExpression):
        pass

    @abstractmethod
    def visitMAISIGUAL(self,MAISIGUAL):
        pass

    @abstractmethod
    def visitMENOSIGUAL(self,MENOSIGUAL):
        pass

    @abstractmethod
    def visitMULTIGUAL(self, MULTIGUAL):
        pass

    @abstractmethod
    def visitDIVIGUAL(self,DIVIGUAL):
        pass

    @abstractmethod
    def visitMODIGUAL(self,MODIGUAL):
        pass

    @abstractmethod
    def visitDiferente(self,Diferente):
        pass

    @abstractmethod
    def visitIdentidade(self,Identidade):
        pass

    @abstractmethod
    def visitIgualdade(self,Igualdade):
        pass

    @abstractmethod
    def visitSemIdentidade(self,SemIdentidade):
        pass

    @abstractmethod
    def visitMenor(self,Menor):
        pass

    @abstractmethod
    def visitMaior(self,MAIOR):
        pass

    @abstractmethod
    def visitMenorIgual(self,MenorIgual):
        pass

    @abstractmethod
    def visitMaiorIgual(self,MaiorIgual):
        pass

    @abstractmethod
    def visitIn(self,In):
        pass

    @abstractmethod
    def visitNotIn(self,NotIn):
        pass

    @abstractmethod
    def visitNotIs(self,NotIs):
        pass

    @abstractmethod
    def visitIs(self,Is):
        pass

    @abstractmethod
    def visitPlus(self,Plus):
        pass

    @abstractmethod
    def visitMinus(self,MINUS):
        pass

    @abstractmethod
    def visitMult(self,Mult):
        pass

    @abstractmethod
    def visitMod(self,Mod):
        pass

    @abstractmethod
    def visitDivide(self,Divide):
        pass

    @abstractmethod
    def visitSimpleAsOperator(self,SimpleAsOperator):
        pass

    @abstractmethod
    def visitCompoundAsOperator(self,CompoundAsOperator):
        pass

    @abstractmethod
    def visitNot(self,Not):
        pass


   #
   #  @abstractmethod
   #  def visitOptionalTypeModifiersConcrete(self,OptionalTypeModifiersConcrete):
   #      pass
   #
   #  @abstractmethod
   #  def visitParenthesizedType(self,ParenthesizedType):
   #      pass
   #
   #  @abstractmethod
   #  def visitFunctionType(self,FunctionType):
   #      pass
   #
   #  @abstractmethod
   #  def visitUserType(self,UserType):
   #      pass
   #  @abstractmethod
   #  def visitSimpleTypeModifiers(self,SimpleTypeModifiers):
   #      pass
   #
   #  @abstractmethod
   #  def visitCompoundTypeModifiers(self,CompoundTypeModifiers):
   #      pass
   #
   #  @abstractmethod
   #  def visitTypeModifierConcrete(self,TypeModifierConcrete):
   #      pass
   #
   #  @abstractmethod
   #  def visitTypeProjectionModifierConcrete(self,TypeProjectionModifierConcrete):
   #      pass
   #
   #  @abstractmethod
   #  def visitVariaceModifierIn(self,VariaceModifierIn):
   #      pass
   #
   #  @abstractmethod
   #  def visitVariaceModifierOut(self,VariaceModifierOut):
   #      pass
   #
   #  @abstractmethod
   #  def visitSimpleSimpleUserType(self,SimpleSimpleUserType):
   #      pass
   #
   #  @abstractmethod
   #  def visitSimpleSimpleUserType(self,SimpleSimpleUserType):
   #      pass
   #
   #  @abstractmethod
   #  def visitCompoundSimpleUserType(self,CompoundSimpleUserType):
   #      pass
   #
   #  @abstractmethod
   #  def visittypeSimpleProjection(self,typeSimpleProjection):
   #      pass
   #
   #  @abstractmethod
   #  def visitCompoundTypeProjection(self,CompoundTypeProjection):
   #      pass
   #
   #  @abstractmethod
   #  def visitSimpleTypeProjectionModifiers(self,SimpleTypeProjectionModifiers):
   #      pass
   #
   #  @abstractmethod
   #  def visitCompoundTypeProjectionModifiers(self,CompoundTypeProjectionModifiers):
   #      pass
   #
   #  @abstractmethod
   #  def visitSimpleFunctionType(self,SimpleFunctionType):
   #      pass
   #
   #  @abstractmethod
   #  def visitCompoundFunctionType(self,CompoundFunctionType):
   #      pass
   #
   #  @abstractmethod
   #  def visitFunctionTypeParametersConcrete(self,FunctionTypeParametersConcrete):
   #      pass
   #
   #  @abstractmethod
   #  def visitSimpleParameterOrTypeRecursive(self,SimpleParameterOrTypeRecursive):
   #      pass
   #
   #  @abstractmethod
   #  def visitCompoundParameterOrTypeRecursive(self,CompoundParameterOrTypeRecursive):
   #      pass
   #
   #  @abstractmethod
   #  def visitReceiverTypeConcrete(self,ReceiverTypeConcrete):
   #      pass
   #
   #  @abstractmethod
   #  def visitSimpleStatemnts(self,visitSimpleStatemnts):
   #      pass
   #
   #  @abstractmethod
   #  def visitCompoundStatemnts(self,CompoundStatemnts):
   #      pass
   #
   #  @abstractmethod
   #  def visitFunctionDeclaration(self,FunctionDeclaration):
   #      pass
   #
   #  @abstractmethod
   #  def visitAssignment(self,Assignment):
   #      pass
   #
   #  @abstractmethod
   #  def visitLoopStatement(self,LoopStatement):
   #      pass
   #
   #  @abstractmethod
   #  def visitExpression(self,Expression):
   #      pass
   #
   #  @abstractmethod
   #  def visitBlock(self,Block):
   #      pass
   #
   #  @abstractmethod
   #  def visitBlock(self,StatementConcrete):
   #      pass
   #
   #  @abstractmethod
   #  def visitForStatement_MD(self,ForStatement_MD):
   #      pass
   #
   #  @abstractmethod
   #  def visitForStatement_VD(self,ForStatement_VD):
   #      pass
   #
   #  @abstractmethod
   #  def visitWhileStatement_PV(self,WhileStatement_PV):
   #      pass
   #
   #  @abstractmethod
   #  def visitWhileStatement_CBS(self,WhileStatement_CBS):
   #      pass
   #
   #  @abstractmethod
   #  def visitWhileStatementD(self,WhileStatementD):
   #      pass
   #
   #  @abstractmethod
   #  def visitDoWhileStatement(self,DoWhileStatement):
   #      pass
   #
   #  @abstractmethod
   #  def visitSimpleForStatement_MD(self,SimpleForStatement_MD):
   #      pass
   #
   #  @abstractmethod
   #  def visitCompoundForStatement_MD(self,CompoundForStatement_MD):
   #      pass
   #
   #  @abstractmethod
   #  def visitSimpleForStatement_VD(self,SimpleForStatement_VD):
   #      pass
   #
   #  @abstractmethod
   #  def visitCompoundForStatement_VD(self,CompoundForStatement_VD):
   #      pass
   #
   #  @abstractmethod
   #  def visitSimpleDoWhileStatement(self,SimpleDoWhileStatement):
   #      pass
   #
   #  @abstractmethod
   #  def visitCompoundDoWhileStatement(self,CompoundDoWhileStatement):
   #      pass
   #
   #  @abstractmethod
   #  def visitAssignmentConcrete(self,AssignmentConcrete):
   #      pass
   #
   #  @abstractmethod
   #  def visitAssignmentAndOperatorConcrete(self,AssignmentAndOperatorConcrete):
   #      pass
   #
   #  @abstractmethod
   #  def visitDisjunctionConcrete(self,DisjunctionConcrete):
   #      pass
   #
   #  @abstractmethod
   #  def visitSimpleDisjunction(self,SimpleDisjunction):
   #      pass
   #
   #  @abstractmethod
   #  def visitCompoundDisjunction(self,CompoundDisjunction):
   #      pass
   #
   #  @abstractmethod
   #  def vistSimpleConjunction(self,SimpleConjunction):
   #      pass
   #
   #  @abstractmethod
   #  def vistCompoundConjunction(self,CompoundConjunction):
   #      pass
   #
   # x
   #  @abstractmethod
   #  def visitSimpleInfixOperationRecursive(self,SimpleInfixOperationRecursive):
   #      pass
   #
   #  @abstractmethod
   #  def visitCompoundInfixOperationRecursive(self,CompoundInfixOperationRecursive):
   #      pass
   #
   #  @abstractmethod
   #  def visitInOperator(self,InOperator):
   #      pass
   #
   #  @abstractmethod
   #  def visitIsOperator(self,IsOperator):
   #      pass
   #
   #  @abstractmethod
   #  def visitElvisExpressionConcrete(self,ElvisExpressionConcrete):
   #      pass
   #
   #
   #  @abstractmethod
   #  def visitSimpleInfixFunctionCall(self,SimpleInfixFunctionCall):
   #      pass
   #
   #  @abstractmethod
   #  def visitCompoundInfixFunctionCall(self,CompoundInfixFunctionCall):
   #      pass
   #
   #
   #  @abstractmethod
   #  def visitSimplePrefixUnaryExpression(self,SimplePrefixUnaryExpression):
   #      pass
   #
   #  @abstractmethod
   #  def visitCompoundPrefixUnaryExpression(self,CompoundPrefixUnaryExpression):
   #      pass
   #
   #  @abstractmethod
   #  def visitSimplePrefixUnaryExpressionRecursive(self,SimplePrefixUnaryExpressionRecursive):
   #      pass
   #
   #  @abstractmethod
   #  def visitCompoundPrefixUnaryExpressionRecursive(self,CompoundPrefixUnaryExpressionRecursive):
   #      pass
   #
   #  @abstractmethod
   #  def visitPrefixUnaryOperatorConcrete(self,PrefixUnaryOperatorConcrete):
   #      pass
   #
   #  @abstractmethod
   #  def visitLabelConcrete(self,LabelConcrete):
   #      pass
   #
   #  @abstractmethod
   #  def visitSimplePostfixUnaryExpression(self,SimplePostfixUnaryExpression):
   #      pass
   #
   #  @abstractmethod
   #  def visitCompoundPostfixUnaryExpression(self,CompoundPostfixUnaryExpression):
   #      pass
   #
   #  @abstractmethod
   #  def visitSinglePostfixUnaryExpressionRecursive(self,SinglePostfixUnaryExpressionRecursive):
   #      pass
   #
   #  @abstractmethod
   #  def visitCompoundPostfixUnaryExpressionRecursive(self,CompoundPostfixUnaryExpressionRecursive):
   #      pass
   #
   #  @abstractmethod
   #  def visitPostfixUnaryOperatorConcrete(self,PostfixUnaryOperatorConcrete):
   #      pass
   #
   #  @abstractmethod
   #  def visitTypeArgumentsConcrete(self,TypeArgumentsConcrete):
   #      pass
   #
   #  @abstractmethod
   #  def visitCallSuffixConcrete(self,CallSuffixConcrete):
   #      pass
   #
   #  @abstractmethod
   #  def visitIndexingSuffixConcrete(self,IndexingSuffixConcrete):
   #      pass
   #
   #  @abstractmethod
   #  def visitNavigationSuffixConcrete(self,NavigationSuffixConcrete):
   #      pass
   #
   #  @abstractmethod
   #  def visitSimpleTypeArguments(self,SimpleTypeArguments):
   #      pass
   #
   #  @abstractmethod
   #  def visitTa(self,Ta):
   #      pass
   #
   #  @abstractmethod
   #  def visitIndexingSuffix(self,IndexingSuffix):
   #      pass
   #
   #  @abstractmethod
   #  def visitCallSuffix(self,CallSuffix):
   #      pass
   #
   #  @abstractmethod
   #  def visitSimpleIdentifier(self,SimpleIdentifier):
   #      pass
   #
   #  @abstractmethod
   #  def visitParenthesizedDirectlyAssignableExpression(self,ParenthesizedDirectlyAssignableExpression):
   #      pass
   #
   #  @abstractmethod
   #  def visitSimpleDirectlyAssignableExpression(self,SimpleDirectlyAssignableExpression):
   #      pass
   #
   #  @abstractmethod
   #  def visitParenthesizedDirectlyAssignableExpressionConcrete(self,ParenthesizedDirectlyAssignableExpressionConcrete):
   #      pass
   #
   #  @abstractmethod
   #  def visitParenthesizedAssignableExpressionConcrete(self,ParenthesizedAssignableExpressionConcrete):
   #      pass
   #
   #  @abstractmethod
   #  def visitPrefixUnaryExpressionConcrete(self,PrefixUnaryExpressionConcrete):
   #      pass
   #
   #  @abstractmethod
   #  def visitAssignableExpressionConcrete(self,AssignableExpressionConcrete):
   #      pass
   #
   #  @abstractmethod
   #  def visitSimpleIndexingSuffix(self,SimpleIndexingSuffix):
   #      pass
   #
   #  @abstractmethod
   #  def visitCompoundIndexingSuffix(self,CompoundIndexingSuffix):
   #      pass
   #
   #  @abstractmethod
   #  def visitSimpleIndexingSuffixRecursive(self,SimpleIndexingSuffixRecursive):
   #      pass
   #
   #  @abstractmethod
   #  def visitCompoundIndexingSuffixRecursive(self,CompoundIndexingSuffixRecursive):
   #      pass
   #
   #  @abstractmethod
   #  def visitparenthesizedExpressionConcrete(self,parenthesizedExpressionConcrete):
   #      pass
   #
   #  @abstractmethod
   #  def visitSimpleCallSuffixConcrete(self,SimpleCallSuffixConcrete):
   #      pass
   #
   #  @abstractmethod
   #  def visitCompoundCallSuffixConcrete(self,CompoundCallSuffixConcrete):
   #      pass
   #
   #  @abstractmethod
   #  def visitValueArgumentsConcrete(self,ValueArgumentsConcrete):
   #      pass
   #
   #  @abstractmethod
   #  def visitAnnotatedLambdaConcrete(self,AnnotatedLambdaConcrete):
   #      pass
   #
   #  @abstractmethod
   #  def visitLambdaLiteralConcrete(self,LambdaLiteralConcrete):
   #      pass
   #
   #  @abstractmethod
   #  def visitSimpleTypeArguments(self,SimpleTypeArguments):
   #      pass
   #
   #  @abstractmethod
   #  def visitCompoundTypeArguments(self,CompoundTypeArguments):
   #      pass
   #
   #  @abstractmethod
   #  def visitSimpleTypeArgumentsRecursive(self,SimpleTypeArgumentsRecursive):
   #      pass
   #
   #  @abstractmethod
   #  def visitCompoundCompoundTypeArgumentsRecursive(self,CompoundCompoundTypeArgumentsRecursive):
   #      pass
   #
   #  @abstractmethod
   #  def visitSimpleValueArguments(self,SimpleValueArguments):
   #      pass
   #
   #  @abstractmethod
   #  def visitCompoundValueArguments(self,CompoundValueArguments):
   #      pass
   #
   #  @abstractmethod
   #  def visitSimpleValueArgumentsRecursive(self,SimpleValueArgumentsRecursive):
   #      pass
   #
   #  @abstractmethod
   #  def visitCompoundValueArgumentsRecursive(self,CompoundValueArgumentsRecursive):
   #      pass
   #
   #  @abstractmethod
   #  def visitSimpleValueArgument(self,SimpleValueArgument):
   #      pass
   #
   #  @abstractmethod
   #  def visitCompound1ValueArgument(self,Compound1ValueArgument):
   #      pass
   #
   #  @abstractmethod
   #  def visitCompound2ValueArgument(self,Compound2ValueArgument):
   #      pass
   #
   #  @abstractmethod
   #  def visitLITERAL_STRINGConcrete(self,LITERAL_STRINGConcrete):
   #      pass
   #
   #  @abstractmethod
   #  def visitableReferenceConcrete(self,ableReferenceConcrete):
   #      pass
   #
   #  @abstractmethod
   #  def visitFunctionLiteralConcrete(self,FunctionLiteralConcrete):
   #      pass
   #
   #  @abstractmethod
   #  def visitCollectionLiteralConcrete(self,CollectionLiteralConcrete):
   #      pass
   #
   #  @abstractmethod
   #  def visitIfExpressionConcrete(self,IfExpressionConcrete):
   #      pass
   #
   #  @abstractmethod
   #  def visitJumpExpressionConcrete(self,JumpExpressionConcrete):
   #      pass
   #
   #  @abstractmethod
   #  def visitSimpleCollectionLiteral(self,SimpleCollectionLiteral):
   #      pass
   #
   #  @abstractmethod
   #  def visitCompoundCollectionLiteral(self,CompoundCollectionLiteral):
   #      pass
   #
   #  @abstractmethod
   #  def visitSimpleCollectionLiteralRecursive(self,SimpleCollectionLiteralRecursive):
   #      pass
   #
   #  @abstractmethod
   #  def visitCompoundCollectionLiteralRecursive(self,CompoundCollectionLiteralRecursive):
   #      pass
   #
   #  @abstractmethod
   #  def visitSimpleParametersWithOptionalType(self,SimpleParametersWithOptionalType):
   #      pass
   #
   #  @abstractmethod
   #  def visitCompoundParametersWithOptionalType(self,CompoundParametersWithOptionalType):
   #      pass
   #
   #  @abstractmethod
   #  def visitSimpleParametersWithOptionalTypeRecursive(self,SimpleParametersWithOptionalTypeRecursive):
   #      pass
   #
   #  @abstractmethod
   #  def visitCompoundParametersWithOptionalTypeRecursive(self,CompoundParametersWithOptionalTypeRecursive):
   #      pass
   #
   #  @abstractmethod
   #  def visitParameterWithOptionalTypeConcrete(self,ParameterWithOptionalTypeConcrete):
   #      pass
   #
   #  @abstractmethod
   #  def visitOptionalParameterModifiersConcrete(self,OptionalParameterModifiersConcrete):
   #      pass
   #
   #  @abstractmethod
   #  def visitVararg(self,Vararg):
   #      pass
   #
   #  @abstractmethod
   #  def visitNoinline(self,Noinline):
   #      pass
   #
   #  @abstractmethod
   #  def visitCrossinline(self,Crossinline):
   #      pass
   #
   #  @abstractmethod
   #  def visitlambdaLiteral(self,lambdaLiteral):
   #      pass
   #
   #  @abstractmethod
   #  def visitSimpleOptionsLambdaLiteral(self,SimpleOptionsLambdaLiteral):
   #      pass
   #
   #  @abstractmethod
   #  def visitCompound1OptionsLambdaLiteral(self,Compound1OptionsLambdaLiteral):
   #      pass
   #
   #  @abstractmethod
   #  def visitCompound2OptionsLambdaLiteral(self,Compound2OptionsLambdaLiteral):
   #      pass
   #
   #  @abstractmethod
   #  def visitSimpleLambdaParameters(self,SimpleLambdaParameters):
   #      pass
   #
   #  @abstractmethod
   #  def visitCompoundLambdaParameters(self,CompoundLambdaParameters):
   #      pass
   #
   #  @abstractmethod
   #  def visitVariableDeclaration(self,VariableDeclaration):
   #      pass
   #
   #  @abstractmethod
   #  def visitCompoundLambdaParameter(self,CompoundLambdaParameter):
   #      pass
   #
   #  @abstractmethod
   #  def visitAnonymousFunctionConcrete(self,AnonymousFunctionConcrete):
   #      pass
   #
   #  @abstractmethod
   #  def visitOptinalTypePontoConcrete(self,OptinalTypePontoConcrete):
   #      pass
   #
   #  @abstractmethod
   #  def visitOptionalTypeConstraintsConcrete(self,OptionalTypeConstraintsConcrete):
   #      pass
   #
   #  @abstractmethod
   #  def visitOptionalFunctionBodyConcrete(self,OptionalFunctionBodyConcrete):
   #      pass
   #
   #  @abstractmethod
   #  def visitTypeConstraint(self,TypeConstraint):
   #      pass
   #
   #  @abstractmethod
   #  def visitSimpleIfExpression(self,SimpleIfExpression):
   #      pass
   #
   #  @abstractmethod
   #  def visitCompoundIfExpression(self,CompoundIfExpression):
   #      pass
   #
   #  @abstractmethod
   #  def visitPV(self,PV):
   #      pass
   #
   #  @abstractmethod
   #  def visitControlStructureBody(self,ControlStructureBody):
   #      pass
   #
   #  @abstractmethod
   #  def visitReturnConcrete(self,ReturnConcrete):
   #      pass
   #
   #  @abstractmethod
   #  def visitReturnAtConcrete(self,ReturnAtConcrete):
   #      pass
   #
   #  @abstractmethod
   #  def visitContinueConcrete(self,ContinueConcrete):
   #      pass
   #
   #  @abstractmethod
   #  def visitContinueAtConcrete(self,ContinueAtConcrete):
   #      pass
   #
   #  @abstractmethod
   #  def visitBreakConcrete(self,BreakConcrete):
   #      pass
   #
   #  @abstractmethod
   #  def visitBreakAtConcrete(self,BreakAtConcrete):
   #      pass
   #
   #  @abstractmethod
   #  def visitCallableReferenceConcrete(self,CallableReferenceConcrete):
   #      pass
   #
   #  @abstractmethod
   #  def visitOptionalReceiverType(self,OptionalReceiverType):
   #      pass
   #
   #  @abstractmethod
   #  def visitClassConcrete(self,ClassConcrete):
   #      pass
   #
   #
   #
   #  @abstractmethod
   #  def visitIncremento(self,Incremento):
   #      pass
   #
   #  @abstractmethod
   #  def visitDecremento(self,Decremento):
   #      pass
   #
   #  @abstractmethod
   #  def visitPonto(self,Ponto):
   #      pass
   #
   #  @abstractmethod
   #  def visitColonColon(self,ColonColon):
   #      pass
   #
   #  @abstractmethod
   #  def visitSafeNavConcrete(self,SafeNavConcrete):
   #      pass
