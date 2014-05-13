from abc import ABCMeta, abstractmethod
from box.functools import cachedproperty
from .command import Command

class Program(metaclass=ABCMeta):
    """Abstract console program representation.
    
    Client have to implement __call__ method:
    
    >>> from box.argparse import Program
    >>> class Program(Program):
    ...   def __call__(self):
    ...     print(self._command.arguments)
    ...
    >>> p = Program(['program', 'arg'])
    >>> p()
    ['arg']
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
        return self._command_class(self._argv)