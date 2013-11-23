from abc import ABCMeta, abstractmethod

class Formatter(metaclass=ABCMeta):
    
    #Public
    
    @abstractmethod
    def process(self):
        pass #pragma: no cover