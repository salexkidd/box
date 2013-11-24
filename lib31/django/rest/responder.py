from abc import ABCMeta, abstractmethod
from .exceptions import ConstraintsAreNotSuppported

class RestResponder(metaclass=ABCMeta):
    
    #Public
    
    def __init__(self, constraints={}):
        if constraints:
            raise ConstraintsAreNotSuppported(constraints)
    
    @abstractmethod
    def respond(self):
        pass #pragma: no cover 