from abc import abstractmethod
from abc import ABCMeta


class Exp(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
        pass

class Call(metaclass=ABCMeta):
    @abstractmethod
    def accept(self,Visitor):
        pass

class Params(metaclass=ABCMeta):
    @abstractmethod
    def accept(self,Visitor):
        pass

class Assign(metaclass=ABCMeta):
     @abstractmethod
     def accept(self,Visitor):
        pass
