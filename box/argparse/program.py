from abc import ABCMeta, abstractmethod
from ..functools import cachedproperty
from .command import Command
from .settings import Settings

class Program(metaclass=ABCMeta):
    """Abstract console program representation.
    
    Client have to implement __call__ method:
    
    >>> from box.argparse import Program
    >>> class Program(Program):
    ...   def __call__(self):
    ...     print(self._command.arguments)
    ...
    >>> program = Program(['program', 'arg'])
    >>> program()
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
    _settings_class = Settings
      
    @cachedproperty
    def _command(self):
        return self._command_class(
            self._argv, config=self._settings.argparse)
    
    @cachedproperty    
    def _settings(self):
        return self._settings_class()