from abc import ABCMeta, abstractmethod

class RestFormatter(metaclass=ABCMeta):
    
    #Public
    
    @abstractmethod
    def format(self):
        pass #pragma: no cover