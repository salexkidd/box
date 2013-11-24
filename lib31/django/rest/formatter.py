from abc import ABCMeta, abstractmethod

class Formatter(metaclass=ABCMeta):
    
    #Public
    
    @abstractmethod
    def format(self):
        pass #pragma: no cover