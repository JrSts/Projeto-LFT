from abc import abstractmethod
from abc import ABCMeta

class AbstractVisitor(metaclass=ABCMeta):
    @abstractmethod
    def visitSimpleKotlinFile(self, KotlinFile):
        pass
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

