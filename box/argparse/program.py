from abc import ABCMeta, abstractmethod
from ..functools import cachedproperty
from .command import Command
from .settings import Settings

class Program(metaclass=ABCMeta):
    """Abstract console program representation.
    
    :param list argv: sys.argv like list of arguments
    
    Client have to implement __call__ method and can adjust
    _command(_class) and _settings(_class) attributes using
    compatible with module's :class:`box.argparse.Command`, 
    :class:`box.argparse.Settings` replacements.
    
    Usage exmaple::
    
      >>> from box.argparse import Program, Settings
      >>> class Settings(Settings):
      ...   argparse = {'arguments': [{'name': 'arguments', 'nargs':'*'}]}
      >>> class Program(Program):
      ...   def __call__(self):
      ...     print(self._command.arguments)
      ...   _settings_class = Settings
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