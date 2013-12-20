from abc import ABCMeta, abstractmethod
from lib31.python import cachedproperty
from .command import Command

class Program(metaclass=ABCMeta):
    
    #Public
        
    def __init__(self, argv):
        self.argv = argv
        
    @abstractmethod
    def __call__(self):
        pass #pragma: no cover
      
    @cachedproperty
    def command(self):
        schema = dict(Command.shema)
        schema['prog'] = self.__class__.__name__.lower()
        return Command(schema=schema)