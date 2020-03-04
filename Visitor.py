class Visitor():
    def visitSomaExp(self, somaExp):
        somaExp.exp1.accept(self)
        print ('+')
        somaExp.exp2.accept(self)

    def visitMulExp(self, mulExp):
        mulExp.exp1.accept(self)
        print ('*')
        mulExp.exp2.accept(self)
        
    def visitAssignExp(self, assignExp):
        assignExp.assign.accept(self)