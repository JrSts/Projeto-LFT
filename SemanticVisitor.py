from AbstractVisitor import AbstractVisitor
import SymbolTable as st
from Visitor import Visitor
from lex import lex
import ConcretaClass as co

def coercion(type1, type2):
    if (type1 in st.Number and type2 in st.Number):
        if (type1 == st.FLOAT or type2 == st.FLOAT):
            return st.FLOAT
        else:
            return st.INT
    else:
        return None

class SemanticVisitor(AbstractVisitor):

    def __init__(self):
        self.printer = Visitor()
        st.beginScope('Start')
        
    def visitSimpleKotlinFile(self, SimpleKotlinFile):
        SimpleKotlinFile.functionDeclaration.accept(self)

    def visitCompoundKotlinFile(self,CompoundKotlinFile):
        CompoundKotlinFile.functionDeclaration.accept(self)
        CompoundKotlinFile.kotlinFile.accept(self)  

    def visitSimpleFunctionDeclaration(self, SimpleFunctionDeclaration):
        print('fun')
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
