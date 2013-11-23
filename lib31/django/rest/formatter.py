from abc import ABCMeta, abstractmethod

class RestFormatter(metaclass=ABCMeta):
    
    #Public
    
    @abstractmethod
    def process(self):
        pass #pragma: no cover