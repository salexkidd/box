from abc import ABCMeta, abstractmethod
from .command import Command

class Program(metaclass=ABCMeta):
    
    #Public
        
    def __init__(self, argv):
        self._argv = argv
        
    @abstractmethod
    def __call__(self):
        pass #pragma: no cover
            
    #Protected
    
    @property
    def _command(self):
        return Command(self._argv, schema=self._command_schema)
    
    @property
    @abstractmethod    
    def _command_schema(self):
        pass #pragma: no cover                  