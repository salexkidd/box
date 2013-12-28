from abc import ABCMeta, abstractmethod
from lib31.python import cachedproperty
from .command import Command

class Program(metaclass=ABCMeta):
    
    #Public
        
    def __init__(self, argv):
        self._argv = argv
        
    @abstractmethod
    def __call__(self):
        pass #pragma: no cover
    
    #Protected
      
    @cachedproperty
    def _command(self):
        config = dict(Command.config)
        config['prog'] = self.__class__.__name__.lower()
        return Command(self._argv, config=config)