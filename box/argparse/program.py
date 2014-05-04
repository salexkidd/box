from abc import ABCMeta, abstractmethod
from box.functools import cachedproperty
from .command import Command

class Program(metaclass=ABCMeta):
    """Console command representation.
    """
    
    #Public
        
    def __init__(self, argv):
        self._argv = argv
        
    @abstractmethod
    def __call__(self):
        pass #pragma: no cover
    
    #Protected
    
    _command_class = Command
      
    @cachedproperty
    def _command(self):
        prog = type(self).__name__.lower()
        return self._command_class(self._argv, prog=prog)