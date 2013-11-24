from abc import ABCMeta, abstractmethod

class RESTFormatter(metaclass=ABCMeta):
    
    #Public
    
    @abstractmethod
    def format(self):
        pass #pragma: no cover